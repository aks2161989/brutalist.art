# TYPECHECK — Brutalist Utility: beat_lint.py (portrait 2160×3840)

## Legacy checker (documented gap)

`runtime/scripts/type_check.py` and `reference/type-spec.md` are **NOT
present** in this isolated toolkit revision. Honestly logged.

## What ran instead

Frame-level visual QC via `runtime/qc/final_frame_check.py` (Gate V),
sampling every beat at 50% and 85% of its duration. Portrait safe area:
SAFE916 {x:54, y:96, r:1026, b:1824, w:972, h:1728} on 1080×1920 canvas.

## Result

- Frames sampled: **24** (12 beats × 2 fracs)
- BLOCKER: **0**
- MAJOR: **0**
- Clean — no BLOCKER/MAJOR defects. ✓ (see `vertical/_qc/REPORT.md`)

## Fixes applied before clean pass

Same root causes as landscape, portrait-specific variants:

| Beat | Fix |
|------|-----|
| B01 | `charMs` reduced 42→12 (BrutalistHesitantWriter916); typing completes ~3s in |
| B02 | BeatLintPipeline916 lint-node color changed BORDER→CARD |
| B06 | FormACard916 → ClaudeCodeBeat916 (cream bg fills safe area) |
| B07 | FormACard916 → ClaudeCodeBeat916 (same) |

## Fonts / typography sources

Portrait scenes use the same CLAUDE token set as landscape. Key portrait sizes:

- BLUF hesitant writer (B01): BrutalistHesitantWriter916 with portrait-aware
  scale `min(width/1080, height/1920)` so serif fills safe area
- Pipeline diagram (B02): BeatLintPipeline916 — nodes full-width (nodeW=SAFE_W),
  stacked vertically; INK label text spans near full safe width
- Code beats (B03–B07, B09): ClaudeCodeBeat916 — portrait-native layout
- HAI outro (B11): ClaudeTitleOutroHAI916

## Notes for human reviewer

- B06/B07 vertical: original FormACard916 with centered text would have
  covered only ~27% of SAFE916 (below the 55% minimum). ClaudeCodeBeat916
  fills the card area from 8% to 82% of portrait height → ~74% coverage.
