# Typography check — portrait

The legacy `scripts/type_check.py` referenced in some public docs is not shipped in this toolkit. This file records a manual, frame-level typography read against the portrait master.

## Method

- Extracted 26 steady-state frames via `runtime/qc/final_frame_check.py`.
- Read the compile-time `_qc/contact_sheet.png` (sha256 a8aa5896…) with the image-capable Read tool for the ordered tour; then re-extracted single frames for B01, B02, B03, B10, B11, B12 for closer inspection.

## Findings

- **Portrait reflow, not center-cut.** Every REMOTION beat re-rendered at 2160×3840 via its `<Pattern>916` composition. No frame is a landscape crop.
- **Serif family (Playfair-derived).** Titles and body copy render with expected weight; no synthesized italic; no missing glyph substitution.
- **B01 sizing verification.** `cli-explainer` line at fontSize 175 (portrait scale = 1 in design ref, output ×2 = 350 px) measures ≈ 1730 px wide at the 85% steady-state sample — inside the 1944 px portrait safe width. Six lines × 175 × 1.14 × 2 = 2394 px vertical — inside the 3456 px safe height. Measured coverage 60% (over the 55% floor).
- **B03 pipeline nodes.** Five phases (INTRO / PROBLEM / BUILD LOOP / REVISION / HANDOFF) plus INPUT + OUTPUT = 7 nodes fit `boxW=100` + arrows in the portrait row; no left/right bleed. Node text is legible; the accented BUILD LOOP node shows the terracotta border on the correct edge.
- **Terracotta accent.** Applied only where designed — same policy as landscape: B01 trigger words during hesitation, B03 BUILD LOOP node, B05/B08 header underlines, B10 numerals, B12 outro period.
- **B10 verdict artifact.** Four numbered lines stack cleanly; last line ends about a line above the bottom safe edge — no crowding, no clip.
- **B12 outro.** Portrait outro card centers the title over the handle; the isolated `ClaudeTitleOutro916` renders `@HumanitariansAI` as its handle (not the hardcoded `@NikBearBrown`).

## Documented gaps

Same as the landscape file: no `type_check.py` runtime tool; the frame-level read is the current bar. Not a substitute for a human eye on the master.
