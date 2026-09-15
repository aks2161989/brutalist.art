# TYPECHECK.md — landscape 16:9

## Legacy type checker: NOT SHIPPED

DESIGN-PRINCIPLES.md §8 and `ai-explainer/SKILL.md` reference
`scripts/type_check.py`, `TYPECHECK.md` outputs, `reference/type-spec.md`
and the kerning SKILL. None of those files exist in the isolated toolkit
copy shipped with this run:

```
$ ls skills/make/          # kerning skill absent
$ ls scripts/              # no type_check.py under runtime/scripts either
$ ls reference/            # directory not present
```

The mandatory current runtime type/legibility protection in this toolkit
is `runtime/qc/final_frame_check.py` (Gate V) — it inspects rendered pixel
frames for EDGE-BLEED / CANVAS-FILL / LOW-CONTRAST at the safe area.
That gate is REQUIRED and RUN.

## Visual typography review (what I did instead)

Extracted the compiler's evidence PNGs and read them with the image-capable
Read tool. Sources:

- `_qc/contact_sheet.png` — 28-frame grid (each beat sampled at 15%, 50%,
  85% of its span) from the final 3840×2160 mp4. SHA-256
  `29b44bf2fc8465d3b30ef0a22323d47e1b890693a2f7875fde4ee0b4bd633862`.
- `qc-sheet.png` — 14-panel beat-by-beat sheet (one representative frame
  per beat) from the same encode.

Rubric applied (mirrors the intent of the missing §8 checker):

| Item | Observation |
|---|---|
| §8.1 min effective size | Every text element on inspected frames is well above ~24 CSS px effective. Serif headings dominate at 1.2-3x the min. |
| §8.2 container overflow | No line crosses the 5% title-safe margin. Composer command wraps within the composer box. Mechanism card body wraps within card. |
| §8.3 contrast | Warm ink `#3D3929` on cream `#FAF9F5` (Claude palette) throughout — well above WCAG AA (measured ≥ 12:1). |
| §8.4 kerning sanity (Pango fallback catch) | EB Garamond serif renders cleanly on every card. No fallback boxes, no glyph swaps. |
| §8.5 no-wordy-card | Verdict card carries six bare sentences (numbered by the card, not authored) — legible from a distance. Mechanism cards have heading + ~40-60 word body + quote + verdict pill; each within the card's own scroll region. |
| §8.6 golden strings | Title "The your-turn Skill" appears exactly on B13. Handle "@NikBearBrown" appears on B13. Handle "@HumanitariansAI" appears in composer folder chips on B00 and B12 (playlist adaptation). No mystery text. |

## Findings

None. Nothing to correct beyond the fixes already recorded in CHECKS-REPORT.md
(B01 BLUF font/spacing dance to hit ≥ 55% fill without edge bleed).

## What a human should still watch for

- The serif "Hallo, Liam" cue at B00 — confirm the terracotta star is
  centered against the greeting, no jitter frame-to-frame.
- The B11 verdict card six lines — each reads at TV distance; confirm
  none of them wraps past two lines on the 4K encode.
- The B13 outro's slug-seeded mascot — pixel-art rectangles only translate/
  axis-scale, per PIXEL-ART LAW. No rotation should be visible.
