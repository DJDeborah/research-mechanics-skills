#!/usr/bin/env python3
"""Inventory a DOCX package; this does not assess science or rendered layout."""

import argparse
import json
from pathlib import Path
import posixpath
import zipfile
import xml.etree.ElementTree as ET

NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "m": "http://schemas.openxmlformats.org/officeDocument/2006/math",
    "r": "http://schemas.openxmlformats.org/package/2006/relationships",
}


def inspect(path):
    report = {"path": str(path.resolve()), "layout_verified": False, "errors": []}
    try:
        with zipfile.ZipFile(path) as archive:
            names = set(archive.namelist())
            corrupt = archive.testzip()
            if corrupt:
                report["errors"].append(f"CRC failure: {corrupt}")
            required = ("[Content_Types].xml", "word/document.xml")
            for name in required:
                if name not in names:
                    report["errors"].append(f"Missing package part: {name}")
            if "word/document.xml" not in names:
                return report
            root = ET.fromstring(archive.read("word/document.xml"))
            paragraphs = root.findall(".//w:p", NS)
            captions = []
            headings = []
            for paragraph in paragraphs:
                text = "".join(n.text or "" for n in paragraph.findall(".//w:t", NS))
                style = paragraph.find("w:pPr/w:pStyle", NS)
                style_name = style.get(f"{{{NS['w']}}}val", "") if style is not None else ""
                if "caption" in style_name.lower() or text.startswith(("Figure ", "Fig. ")):
                    captions.append(text)
                if style_name.lower().startswith(("heading", "title")):
                    headings.append({"style": style_name, "text": text})
            missing_targets = []
            external_links = 0
            for name in sorted(names):
                if not name.endswith(".rels"):
                    continue
                relations = ET.fromstring(archive.read(name))
                folder = posixpath.dirname(name)
                base = posixpath.dirname(folder) if folder.endswith("/_rels") else ""
                for relation in relations:
                    if relation.get("TargetMode") == "External":
                        external_links += 1
                        continue
                    target = relation.get("Target", "")
                    resolved = posixpath.normpath(posixpath.join(base, target)).lstrip("/")
                    if target and resolved not in names:
                        missing_targets.append({"relationships": name, "target": target})
            report.update({
                "paragraph_count": len(paragraphs),
                "table_count": len(root.findall(".//w:tbl", NS)),
                "native_equation_count": len(root.findall(".//m:oMath", NS)),
                "drawing_count": len(root.findall(".//w:drawing", NS)),
                "media_part_count": sum(name.startswith("word/media/") for name in names),
                "headings": headings,
                "captions": captions,
                "external_relationship_count": external_links,
                "missing_relationship_targets": missing_targets,
            })
            if missing_targets:
                report["errors"].append("Some internal relationship targets are missing")
    except (OSError, zipfile.BadZipFile, ET.ParseError) as error:
        report["errors"].append(str(error))
    report["package_ok"] = not report["errors"]
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("docx", type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    result = inspect(args.docx)
    output = json.dumps(result, ensure_ascii=False, indent=2)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(output + "\n", encoding="utf-8")
    else:
        print(output)
    return 0 if result.get("package_ok", False) else 1


if __name__ == "__main__":
    raise SystemExit(main())
