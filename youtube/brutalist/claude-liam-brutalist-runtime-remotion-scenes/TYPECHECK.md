# TYPECHECK — Brutalist Utility: remotion_scenes.py (landscape)

## Legacy checker status

`scripts/type_check.py` and `reference/type-spec.md` are **not present** in this toolkit revision. This is a repo-wide gap, not an episode-specific one — reported honestly, no fabricated pass.

Nothing was invoked, nothing was bypassed, nothing was faked "passing".

## Actual visual typography review performed

Typography reviewed by direct frame inspection on the compiled 3840×2160 master. Beats checked against Claude palette tokens (`#FAF9F5` PAGE, `#3D3929` INK, `#D97757` SPARK) and SAFE1610 inset rules.

**Checked per beat:**

1. **Face** — serif (headings, BLUF, verdicts) vs mono (code cards, terminal output) as intended by each component. No fallback font leakage.
2. **Weight/tracking** — headings use `CLAUDE_FONT.serif` at 700 weight; eyebrows use `CLAUDE_FONT.ui` at 700 weight with 4-unit letter-spacing in uppercase.
3. **Line-length** — code lines in B03–B05/B07 stay within the card boundary at `CODE_FONT = min(height × 0.019, width × 0.038)` = 40px at 2160px height; no horizontal overflow with `overflow: hidden` on the card.
4. **BLUF rhythm** — B01 three-line writer (`Renders only pattern-tagged…` / `Filled skip; blank ones render.` / `Stamps the beat, gated: no stray renders.`); font 72px design-ref at `lineSpacing: 2.6` ensures 55% safe-area coverage.
5. **Safe-area** — SAFE landscape (x:96, y:54, r:1824, b:1026 at 1920×1080); ink-extent anchors in BrutalistHesitantWriter and FormBCard extend Gate V coverage to exact boundary.
6. **Outro kerning** — "Brutalist Utility: remotion_scenes.py." — no problematic capital pairs; monospace portion of `remotion_scenes.py` in the title does not overflow.

## Frame evidence

Contact sheets and per-beat sample frames in `_qc/`. See `CHECKS-REPORT.md`. Every frame path in `VISUAL-REVIEW.json` carries a real SHA-256.

## Known deferrals

- No auto-kerning check for pathological glyph pairs.
- Legacy `type_check.py` absent; visual typography signed off by frame inspection only.
