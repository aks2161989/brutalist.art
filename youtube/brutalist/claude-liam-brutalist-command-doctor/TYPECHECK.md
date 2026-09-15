# TYPECHECK — landscape 16:9

## What the legacy `scripts/type_check.py` would have covered

The parent `ai-explainer` SKILL and the toolkit docs reference a GATE T
static type checker (`scripts/type_check.py`) that would enforce §8.1
min-size, §8.2 overflow, §8.3 contrast, §8.4 kerning sanity, §8.5
no-wordy-card, §8.6 golden strings.

**That checker is not shipped in this toolkit revision.** Its absence has
been catalogued for prior episodes in the same batch. This document
substitutes an explicit visual-typography review; it does NOT claim that a
missing checker passed.

## Substitute — visual-typography review this build actually performed

Every landscape frame in `_qc/frames-landscape/*.png` (3 frames per beat ·
36 stills) was extracted and read with the image-capable Read tool. Two
programmatic checks were also run on B01's steady-state samples (the beat
that failed Gate V at earlier fontSize/lineSpacing settings): safe-area
bbox coverage and edge-bleed against the 3840×2160 SAFE inset (192, 108,
3648, 2052 with a 15-pixel margin, mirroring `runtime/qc/final_frame_check.py`).

## Per-beat notes (typography, not motion)

- **B00 composer** — `Jambo, Liam` greeting sits inside the composer's
  serif greeting slot; the ask wraps once at ~1500 CSS-px and stays inside
  the card's inner padding. `@HumanitariansAI` folder chip legible below
  the composer. Output lines land in mono at ~24 CSS-px effective ≥ floor.
- **B01 hesitant writer** — `fontSize: 260`, `lineSpacing: 2.5` at the
  1920×1080 design canvas. Programmatic bbox coverage 62% (0.5) and
  56.5% (0.85) of SAFE, no edge overflow (see `CHECKS-REPORT.md`).
- **B02-B08 code beats** — Onda-style mono at the shipped ClaudeCodeBeat
  scale. Every line fits inside the white card at 1920×1080; no landscape
  clipping. Title bar reads black on cream; spark line is one line under
  the card in serif ≤ 4 words.
- **B09 verdict artifact** — 6 lines of body text on the artifact card;
  each line wraps once at most; terracotta numerals are the ONE accent
  per beat (§8.3 contrast is satisfied — ink `#3D3929` on cream `#FAF9F5`
  passes the CONTRAST_MIN 0.30 floor Gate V uses).
- **B10 composer (Your Turn)** — long paste-ready prompt wraps inside the
  composer's inner content area; the ✅ / ❌ emojis in the grading lines
  render with the mono fallback; nothing crosses the composer's card edge.
- **B11 outro** — title "Brutalist Command: art doctor." breaks across
  two serif lines in the shipped ClaudeTitleOutro layout; terracotta
  period visible; `@NikBearBrown` handle beneath in serif; polarity and
  mascot are slug-seeded per OUTRO-LOCK.

## Gate V exit state (the substitute type gate that IS shipped)

Gate V, which does check safe-area, edge-bleed, canvas-fill and
contrast on every sampled frame, reported: **BLOCKER 0 · MAJOR 0 · Clean ✓**
(`_qc/REPORT.md`).

## Conclusion

No typography defect surfaced in visual review or in Gate V. Bear's
editorial pass is welcome to flag anything the sampled frames missed;
this build is not a substitute for a human read.
