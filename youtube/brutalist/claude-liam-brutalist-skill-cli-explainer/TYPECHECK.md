# Typography check — landscape

The legacy `scripts/type_check.py` referenced in some public docs is not shipped in this toolkit. The `runtime/qc/final_frame_check.py` gate covers ink-vs-background contrast and safe-area coverage but does not do kerning, tracking, or false-italic detection.

This file records a manual, frame-level typography read.

## Method

- Extracted 26 steady-state frames (13 beats × 50%/85%) via `runtime/qc/final_frame_check.py`.
- Read the `_qc/contact_sheet.png` (sha256 6736bc66…) with the image-capable Read tool for the ordered tour, then read individual PNGs where a beat needed a closer look (B01 fontSize verification, B12 handle rendering).

## Findings

- **Serif family (Playfair-derived).** Titles and body copy render with expected weight; no synthesized italic; no missing glyph substitution (no fallback rectangles).
- **Terracotta accent.** Applied only where designed — the terminal period on B12's outro title; the SPARK edge on accent phases in B03; the trigger-word ink on B01 during the hesitation; three verdict numerals on B10; header underline in B05/B08 code cards. No stray terracotta.
- **Ink contrast.** All body text sits at >= 0.30 luminance separation from the `#FAF9F5` page ground — gate V's `LOW-CONTRAST` check reports 0 defects.
- **B01 sizing.** `cli-explainer` at fontSize 270 in landscape scale = 2 renders at ~2900 output px wide inside the 3456 px safe width — under-safe by ≈ 550 px, no clip. Height 3 × 540 × 1.14 = 1847 px < 1944 safe height. Measured bbox coverage 68%, over the 55% floor.
- **B02/B05/B08 code panel.** Filename tab / code column render in `CLAUDE_FONT.mono`; no line wraps mid-token; the top-left filename tab does not overlap the code column.
- **B12 outro.** Title serif in cream on ink; handle `@HumanitariansAI` in a smaller weight; the terracotta period lands correctly (no drift). See `feedback_channel_title_portrait_bleed` in the shared memory — this reel does not set `metadata.channel_title`, so the compile-overlay channel title is off; the outro carries the handle natively via the `handle` prop on the isolated ClaudeTitleOutro.

## Documented gaps

- No `type_check.py` runtime tool → cannot mechanically verify kerning/tracking; the frame-level read is the current bar. Not a substitute for a human eye on the master.
- Font-fallback detection would require reading the actual font stack — not done here; the frames show no rendered fallback so this is a low-risk gap.
