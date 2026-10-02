---
name: research-word
description: Create or revise scientific Word documents with clear derivations, section-specific postprocessing, figures and mechanical interpretation. Use for research reports and manuscript sections; preserve the user's chosen template, Main/SI structure and evidence.
license: MIT
---

# Research Word

Produce the requested scientific document, with the equations, observations and figures needed to understand the result. A concise manuscript and a full analysis report need different levels of detail; follow the user's choice rather than imposing a journal format.

## Establish the working version

- Identify the intended Word file, requested language, source configuration and energy model. Inspect the latest full evidence-bearing version and the relevant older results before replacing sections. Keep an original when revising.
- Carry forward the user's choices about Main/SI, tables, word count, captions, highlighting and reference style. When asked for a unified explanation, finish that explanation before splitting Main and SI.
- Use an available `documents` skill for document authoring, templates and rendering. Use `research-writing` or `research-significance` when the task calls for scientific restructuring or contribution framing; their audits support review rather than substitute for reading the evidence. If those skills are unavailable, the references below are sufficient to continue.

## Build the argument and its figures

Read [Scientific argument](references/scientific-argument.md) for derivations or mechanics analysis. For each substantial section, record its question, sample and controlled variables, inputs, calculation or postprocessing, observed result, figure panels and concluding statement. The optional [section map](assets/section-map.example.json) gives a reusable structure. A map may remain a private working file; do not force it into a user-facing table.

Write the physical explanation, not merely a list of operations. Introduce symbols before their first equation, state what is held fixed, show which calculation produces the plotted quantity, and explain how the result answers the section's question. Preserve cross terms in the full energy. A reduced expression is appropriate only after a stated substitution, constraint or condensation.

For each chosen example, include a geometry or sample reference, a meaningful observable and the quantitative mechanical test needed for the claim. Cite the source data and code in the working map. Do not invent missing plots or treat a numerical fluctuation as an established transition. Existing approximate comparisons can still be useful: state what agrees and what remains different, without making the whole section unreadable with repeated qualifications.

## Author the Word file

Read [Word authoring](references/word-authoring.md) when creating or editing the artifact. Preserve a supplied template's styles and use native editable Word equations when a working conversion is available. Keep equation numbering, figure numbering, captions and citations consistent. Scientific plots come from the actual data or model; use a standard plotting library and retain the plotting script.

The standard-library helper can inventory the resulting DOCX without launching Word:

```text
python <skill-dir>/scripts/inspect_docx.py result.docx --out docx-structure.json
```

This detects packaging issues and counts equations and figures; it does not verify mathematical correctness or rendered layout.

## Check and deliver

Render and inspect the document using the available document workflow. If the packaged renderer fails, inspect its logs and try an available authorized fallback, such as Word PDF export followed by page rendering. Do not keep retrying the same broken interface or ask for the same permission again.

When the user permits a working draft despite unavailable rendering, deliver the usable DOCX and briefly state the remaining layout check. Do not call it visually verified or publication-ready. A scientific limitation should qualify the relevant statement; it should not prevent delivery of the completed derivation, analysis and figures the evidence supports.

Deliver the requested Word file with a concise change summary. Keep rendering images and temporary files internal unless requested. Include the organized data/code/figure package when requested. Upload to an external repository only within the user's explicit authorization and the identified destination; document creation alone does not authorize publication.
