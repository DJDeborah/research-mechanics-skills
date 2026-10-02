# Research Word / 科学 Word 写作

The fifth skill turns a research explanation into the actual Word artifact requested by the user. It joins source-version review, clear derivations, section-specific postprocessing and figure interpretation with practical document authoring. It complements `research-writing` and `research-significance`; it does not replace them or declare scientific truth through a file audit.

## Install and invoke

```bash
python tools/install.py --user --skill research-word
```

Use a new Codex task or turn and invoke `$research-word`. For example:

```text
$research-word
Revise my current Word analysis around the physical questions.
For every section identify the sample, controlled variables, derivation,
postprocessing, figure panels and supported conclusion. Use the full energy.
Preserve my template and produce the actual DOCX with editable equations.
```

The [section-map example](../skills/research-word/assets/section-map.example.json) is a working aid. The user-facing text need not contain a table. Main/SI division, word count, language and highlighting follow the user's request.

## Portable helper

```bash
python skills/research-word/scripts/inspect_docx.py result.docx --out docx-structure.json
python skills/research-word/scripts/test_inspect_docx.py
```

The helper needs only Python's standard library. It checks ZIP/XML packaging and embedded relationship targets, and inventories headings, captions, figures and native Office Math equations. It deliberately reports `layout_verified: false`: package inspection cannot establish that a figure is readable or an equation fits on the page.

The authoring workflow uses an available document runtime, maintained Word library or artifact tools. Optional libraries such as `python-docx` and a native math converter are not bundled or installed automatically. Rendering uses an available document renderer; an installed and authorized Word export can be a Windows fallback. The skill is a reusable instruction and audit package, not a standalone universal Markdown-to-Word converter.

## Delivery and verification

Keep derivation and figure scripts with the project, retain cross terms until a justified reduction, and map each important scientific statement to its actual example and evidence. Existing approximate comparisons may support a bounded discussion; they do not have to be discarded merely because they are not perfect.

Inspect rendered pages when possible. If both available rendering routes fail, preserve the DOCX and source, report the incomplete layout review and deliver the working draft when the user permits that stage. Do not replace the requested Word with only Markdown, repeatedly request the same authorization, or label an unperformed review as complete.

Three synthetic package tests cover a valid inventory, a missing embedded image, and a corrupt/non-DOCX input. They do not test scientific correctness, writing quality, native-equation rendering or cross-platform document layout.
