# Frontend Encoding Guardrails

Apply to: frontend/**/*.html, frontend/**/*.js, frontend/**/*.css

## Objective
Prevent mojibake source corruption (for example: ``, `--`, `Y`) by enforcing safe text/encoding practices in source files.

## Rules
- Save files as UTF-8 without BOM.
- Prefer ASCII literals in frontend source whenever possible.
- Avoid direct pasted Unicode punctuation/symbols when ASCII works:
  - em dash -> `--`
  - en dash -> `-`
  - minus sign -> `-`
  - multiplication sign -> `x`
  - ellipsis -> `...`
  - greater/less-equal -> `>=`, `<=`
- If visual glyphs are required in HTML output, use HTML entities instead of literal glyphs:
  - `&mdash;`, `&ndash;`, `&times;`, `&ge;`, `&le;`, `&yen;`, `&middot;`
- For JS-created UI text, prefer ASCII-safe strings; when symbols are required, use explicit escape/entity strategy consistently.

## Verification (required before finishing)
- Search changed frontend files for suspicious markers: ``, ``, ``.
- If found, repair source text before finalizing changes.

## Notes
- Runtime sanitizers are not a substitute for source hygiene.
- Source correctness is the canonical fix.
