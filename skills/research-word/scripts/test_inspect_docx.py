"""Standard-library package checks runnable without Word or python-docx."""

import importlib.util
from pathlib import Path
import tempfile
import unittest
import zipfile

MODULE = Path(__file__).with_name("inspect_docx.py")
SPEC = importlib.util.spec_from_file_location("research_word_inspect", MODULE)
inspect_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(inspect_module)

DOCUMENT = '''<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
 xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math"><w:body>
 <w:p><w:pPr><w:pStyle w:val="Heading1"/></w:pPr><w:r><w:t>Model</w:t></w:r></w:p>
 <w:p><m:oMath><m:r><m:t>x</m:t></m:r></m:oMath></w:p>
 <w:p><w:r><w:drawing/></w:r></w:p></w:body></w:document>'''
RELATIONS = '''<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
 <Relationship Id="rId1" Type="image" Target="media/figure.png"/>
 <Relationship Id="rId2" Type="hyperlink" Target="https://example.com" TargetMode="External"/>
 </Relationships>'''


class PackageChecks(unittest.TestCase):
    def make_docx(self, folder, with_image=True):
        path = Path(folder) / "fixture.docx"
        with zipfile.ZipFile(path, "w") as archive:
            archive.writestr("[Content_Types].xml", "<Types/>")
            archive.writestr("word/document.xml", DOCUMENT)
            archive.writestr("word/_rels/document.xml.rels", RELATIONS)
            if with_image:
                archive.writestr("word/media/figure.png", b"fixture")
        return path

    def test_inventory_does_not_claim_layout_verification(self):
        with tempfile.TemporaryDirectory() as folder:
            report = inspect_module.inspect(self.make_docx(folder))
        self.assertTrue(report["package_ok"])
        self.assertFalse(report["layout_verified"])
        self.assertEqual(report["native_equation_count"], 1)
        self.assertEqual(report["drawing_count"], 1)
        self.assertEqual(report["external_relationship_count"], 1)

    def test_missing_embedded_figure_is_reported(self):
        with tempfile.TemporaryDirectory() as folder:
            report = inspect_module.inspect(self.make_docx(folder, with_image=False))
        self.assertFalse(report["package_ok"])
        self.assertEqual(report["missing_relationship_targets"][0]["target"], "media/figure.png")

    def test_non_docx_does_not_pass(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "invalid.docx"
            path.write_text("not a DOCX", encoding="utf-8")
            report = inspect_module.inspect(path)
        self.assertFalse(report["package_ok"])
        self.assertTrue(report["errors"])


if __name__ == "__main__":
    unittest.main()
