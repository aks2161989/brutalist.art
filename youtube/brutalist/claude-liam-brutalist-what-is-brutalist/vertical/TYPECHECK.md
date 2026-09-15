# TYPECHECK.md — What Is Brutalist? · 9:16 portrait companion

## Legacy checker status: NOT SHIPPED

Same as the landscape (see `../TYPECHECK.md`): `scripts/type_check.py` and
its typography spec are not present in this toolkit snapshot. What follows
is an honest visual audit of the portrait master, not a claim that a missing
checker passed.

## Portrait-specific type observations

For every beat I Read the frames sampled by Gate V (`_qc/frames/`, 50%/85%
per-beat samples) and the full `_qc/contact_sheet.png`.

| Rule | Portrait result | Notes |
|---|---|---|
| §8.1 min-size | ✓ | All body copy ≥ 24 px effective. `useVideoConfig`-driven scale = min(2160/1920, 3840/1080) = 1.125 in portrait, so declared font sizes render at 112% of the value in the beat sheet. |
| §8.2 overflow | ✓ | Gate V edge-bleed check reports 0 defects for the portrait build after the safe-area fixes documented in `CHECKS-REPORT.md § Iteration history`. |
| §8.3 contrast | ✓ | Same palette as landscape — CLAUDE.INK on CLAUDE.PAGE separation ≈ 0.75. Gate V low-contrast check reports 0 defects. |
| §8.4 kerning sanity | ✓ | EB Garamond, system UI sans, SF Mono render as expected; no fallback boxes; italic-serif SparkLine overhang no longer crosses safe.x = 54 after padX = 96 fix. |
| §8.5 no-wordy-card | ✓ | Portrait B01 uses 6 short lines (each ≤ 9 chars); WibVerdict lines wrap to two lines each but never crowd the card; no beat presents a paragraph on screen. |
| §8.6 golden strings | ✓ | Spot-checked B00, B04, B08, B09 — every on-screen string matches `vertical/beat_sheet.json`. `@HumanitariansAI` renders correctly (not `@Humanitarians AI` — no accidental space). |

## Portrait-specific kerning spot-checks

- B00 composer chip `Claude · Desktop` — separator ` · ` renders with expected
  hairspace; no baseline shift.
- B01 six-line text — line breaks are hard-newlines from the beat sheet; each
  line's baseline aligns cleanly.
- B02 mono file tab `beat_sheet.json` renders with the terracotta bullet at
  the correct baseline offset.
- B04 rendered composer greeting `Ciao, Liam.` / `Hola, Liam.` — the terracotta
  punctuation stays baseline-aligned with the serif body.
- B07 numbered artifact lines `1.` `2.` `3.` — terracotta numerals aligned with
  first-line baselines of each wrapped sentence.
- B09 outro title `What Is Brutalist?` on two lines — the terracotta question
  mark hangs on the correct baseline; `@HumanitariansAI` handle centered with
  no orphaned space around the `@`.

## Distinction from Gate V

Gate V passed clean (0/0). Gate V covers edge-bleed, canvas-fill, low-contrast.
GATE T's remaining rules (min-size, wordy-card, golden strings) were audited
visually above. When `scripts/type_check.py` ships, running it against the
frames already in `vertical/_qc/frames/` should confirm every rule.
