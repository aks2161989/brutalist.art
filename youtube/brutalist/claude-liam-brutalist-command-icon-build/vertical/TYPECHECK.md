# TYPECHECK — Brutalist Command: art icon-build (vertical)

## Legacy `scripts/type_check.py` — NOT PRESENT

Same absence as the landscape TYPECHECK.md — the legacy GATE T checker and
the kerning skill are not shipped in this toolkit revision. This report does
NOT claim the missing checker passed.

## What WAS run — visual typography review, portrait-specific

GATE V ran on the final vertical master with the same 9-point rubric.
Result:

```
[gate-v] frames=24 BLOCKER=0 MAJOR=0
```

| # | Rubric item | Vertical result |
|---|---|---|
| 1 | Edge bleed / clipping (title-safe inset) | ✓ zero |
| 2 | Container overflow (text past its box) | ✓ zero — fixed by portrait-narrow code substitutions on B02–B08 (see CHECKS-REPORT.md) |
| 3 | Collision | ✓ zero |
| 4 | Offscreen anchors | ✓ zero |
| 5 | Legibility (min effective 24 px, contrast) | ✓ all beats above floor |
| 6 | Brand-bug placement inside title-safe | ✓ folder chip within safe |
| 7 | Aspect (9:16 native, no letterbox) | ✓ 2160×3840 |
| 8 | Canvas fill (no dead space) | ✓ BLUF passes ≥ 55 % coverage floor after the portrait scale patch to `BrutalistHesitantWriter` |
| 9 | Palette discipline (one terracotta per beat) | ✓ spark line / send button / one accent |

## Portrait-specific typography notes

- **Hesitant writer scale patch** — the shipped
  `BrutalistHesitantWriter.tsx` computes `const scale = Math.min(width/1920,
  height/1080)`, which collapses to `0.5625` on a 1080×1920 canvas and
  crushes every geometry value tied to `scale`. This workspace applies the
  documented aspect-aware patch (see `feedback-brutalist-hesitant-writer-portrait-scale-patch`)
  so `fontSize 240` on landscape becomes `fontSize 150` on portrait with
  `lineSpacing 2.5`, and the 4-line stack `art / icon-build / cuts /
  existing icons.` fills the safe area on the sampled frames.
- **ClaudeCodeBeat code substitutions** — the shipped `ClaudeCodeBeat`
  scales its font off `height * 0.022`. That is roughly 42 px at 1920 tall
  vs. 24 px at 1080 tall, so the same code text that fits landscape wide
  overflows both horizontally (~37 chars/line) and vertically (~16 rows) on
  portrait. Rather than patch the component, this reel authors
  portrait-specific `code` strings per beat (B02–B08 in `vertical/beat_sheet.json`)
  that respect those limits while preserving the meaning of each landscape
  card. Line-by-line frame inspection confirms every character stays inside
  the card and every card stays inside the safe inset.

## What is NOT verified

- Subpixel kerning drift below the resolution of a 2160×3840 sampled frame.
- Automated golden-string presence checks (§8.6) — the missing checker's
  role.

Both limitations are shared with the landscape build and inherit the same
honest logging discipline.

## Conclusion

Portrait typography passes the frame-inspectable subset of the type-lock
rubric. The missing legacy `type_check.py` gate would be a stronger check
if it existed; it does not, and this report says so.
