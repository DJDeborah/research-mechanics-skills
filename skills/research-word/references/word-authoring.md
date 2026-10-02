# Scientific Word authoring

## Source and formatting

Keep the scientific source and the authoring script in the working project. For an existing Word version, inspect its paragraph styles, page setup, equation treatment, figure placement and numbering before making a major rewrite. A supplied document controls the design unless the user requests a change.

Use a maintained Word library or available artifact tools. When a document skill or runtime dependency loader is available, use its supported runtime and authoring workflow. Do not install a new rendering application merely because one converter failed.

Use real heading styles, caption styles, accessible image descriptions and ordinary paragraph text. Do not turn narrative sections into tables solely to organize them. Honor a no-table request. Preserve approved highlighting without applying it to whole pages.

## Equations

Prefer native Office Math Markup Language equations when an available conversion can be verified. A typical path is LaTeX to MathML followed by Microsoft's MathML-to-OMML transform, where the required converter and stylesheet are installed. Retain the LaTeX source alongside the artifact.

Do not insert literal LaTeX strings or Unicode approximations and call them Word equations. If native conversion is unavailable or misrenders, a high-resolution rendered equation is a practical fallback for a draft; explain that it is not editable. Use vector or transparent raster output at an intentional physical size. Check subscripts, Greek symbols, matrix dimensions, minus signs and equation numbers after rendering.

Break long derivations at meaningful equalities. Do not shrink a full stiffness matrix to unreadable text; use block form, a dedicated landscape page, or a separate data artifact according to the user's purpose. Introduce every block and its physical meaning in the text.

## Figures and references

Generate scientific curves from the selected source data or computation and keep the script. Retain vector figures for submission and use a reliable embedded format for Word. Size figures according to their smallest axis labels rather than simply forcing full page width.

Use sequential figure and equation references, and verify that every referred item exists. Native fields are useful when supported; explicit numbers are acceptable in a stable draft when fields cannot be refreshed reliably. Keep captions with the relevant figure and define all line colors, markers, units and specimen labels.

Use normal scholarly citations and a consistent reference list. Tool reference identifiers must not appear in the document. Verify bibliographic details when a source is unfamiliar or when quoting a specific result.

## Practical rendering and delivery

First use the available document renderer and inspect its logs if it fails. When authorized and installed, Word PDF export is a useful Windows fallback; open only the intended document, use a hidden/background instance if supported, and close only the instance owned by this task. Convert the resulting PDF to page images with an available tool.

Inspect all rendered pages for clipped equations, unreadable figures, split captions, accidental empty pages and page-header/footer defects. Structural checks help find missing media and count equations; they cannot verify page layout.

If neither renderer works, preserve the DOCX and its source. When the user permits delivery at this stage, provide the working draft and state that layout verification remains incomplete. Do not repeatedly seek permission for the same authorized action. Never relabel a failed render as a successful review.

Keep QA images and temporary exports internal unless the user asks for them. A user who requested Word should receive the actual DOCX, rather than only a prose promise or a link to Markdown.
