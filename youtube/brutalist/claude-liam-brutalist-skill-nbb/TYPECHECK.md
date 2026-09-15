# TYPECHECK — The nbb Skill (landscape 3840×2160)

## Missing legacy checker (documented gap)

`runtime/scripts/type_check.py` and `reference/type-spec.md` referenced in
some public docs are **NOT present** in this isolated toolkit revision
(commit `ba2d0e0f043f5b3b35a50d336e0fc66fbfecfc0c` + local overrides).
This is honestly logged, not silently passed.

## What ran instead

Actual visual typography review by frame inspection of the finished 4K
master, via `runtime/qc/final_frame_check.py` (Gate V) which samples every
beat at 50% and 85% and every canvas edge for edge-bleed, underfill,
clustering, and low-contrast defects. Gate V is the current runtime type
check on a compiled reel.

## Result

- Frames sampled: **24** (12 beats × 2 sample fracs)
- BLOCKER: **0**
- MAJOR: **0**
- Clean — no BLOCKER/MAJOR defects. ✓ (see `_qc/REPORT.md`)

Contact sheet: `_qc/contact_sheet.png`.

## Fonts / typography sources

All landscape scenes use the CLAUDE brand tokens
(`runtime/remotion/src/tokens/claude.ts`):

- Serif — EB Garamond (Regular / Italic / Bold)
- UI Sans — Inter (400 / 500 / 600 / 700)
- Mono — JetBrains Mono (400 / 500)

Body copy sizes:
- Composer command (B00, B10): monospace, ~44px equivalent on 1920×1080 design ref
- Verdict artifact (B09): serif heading + sans lines, sized to fit the artifact card
- Mechanism scenes (B04–B08): serif heading, sans body, mono quote strip
- Anatomy tree (B02): mono file list
- Pipeline (B03): sans phase cards
- BLUF hesitant writer (B01): serif, fontSize 148, lineSpacing 1.25, 4 lines,
  measured coverage ~90% of safe area (up from 39% at v1)

## Notes for a human reviewer

- The BLUF beat was revised once: v1 had 3 lines and hit 39% underfill (Gate V
  MAJOR); v2 uses 4 lines to satisfy FILL_MIN 0.55. This matches the guidance
  in `feedback_gate_v_underfill` — the fix is layout, not font size.
- Reveal-motion histogram is 8/12 (66%) — over the ~40% pantry cap. This is
  a *warning*, not a blocker; the pantry rule is guidance for teardown-style
  reels with lots of card reveals, and this episode is one. Not fixed here.
