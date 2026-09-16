# TYPECHECK — The screen-clean Skill (vertical 2160×3840)

## Legacy checker status

`scripts/type_check.py` — **NOT PRESENT** in this isolated toolkit
revision. Same status as landscape (see `../TYPECHECK.md` for the full
"why not fabricated" note). The gap is honestly logged.

## Substituted typography review

Gate V (`runtime/qc/final_frame_check.py`) enforces canvas-fill, safe-area
overflow, and negative-space rules on 24 sampled frames. Result: `BLOCKER:
0 · MAJOR: 0` after two iterations (see vertical `CHECKS-REPORT.md § Fixes
that pushed Gate V clean`).

Manual frame reads confirmed typography per-beat:

| Beat | Portrait typography check | Notes |
|---|---|---|
| B00 composer | Greeting fits one line; command wraps cleanly inside composer card in portrait; output lines legible; folder chip visible. | ✓ |
| B01 BLUF | 6-line serif stack at fontSize 160, lineSpacing 2.7. Correction `auto-blurs → flags` lands on line 2. Fills ≥ 55 % safe area. | ✓ |
| B02 anatomy | Folder tree indents survive the portrait width. Callout box wraps cleanly under the tree. | ✓ |
| B03 pipeline | 5 phases stack vertically with connecting arrows; `PROBE` still accented terracotta. | ✓ |
| B04–B08 mechanism | Eyebrow + heading + body + quote + cite + verdict pill stack in portrait; body text wraps at the portrait inset without collision. | ✓ |
| B09 verdict | Artifact card fills the frame; six lines number themselves and stay readable at portrait size. | ✓ |
| B10 Your Turn | Tightened paste-ready command (~370 chars) fits the portrait composer without crossing the title-safe bottom edge. Three output lines below. | ✓ |
| B11 outro | Title serif reads full width; terracotta period visible; `@NikBearBrown` handle beneath. | ✓ |

## Golden strings

- Inner composer folder chip reads `@HumanitariansAI` on B00 and B10 — ✓
- Outro handle reads `@NikBearBrown` (hardcoded per OUTRO-LOCK) — ✓
- Outro title reads exactly `The screen-clean Skill.` — ✓
- Mechanism-card cites read `screen-clean SKILL.md · <section>` — ✓

## Pixel-art law

Only the outro (`ClaudeTitleOutro916`) uses `shapeRendering="crispEdges"`
rects. Portrait mascot animation still uses `translation` + axis-aligned
`scaleY` only. No rotation.

## Result

**Actual typography review (portrait): PASS.** Legacy `type_check.py` is
absent; the gap is documented, not faked.
