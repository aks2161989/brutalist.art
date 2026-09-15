# TYPECHECK.md — The nopunt Skill (landscape)

## What this file is

A record of the visual-typography review that runs in place of the legacy
`scripts/type_check.py` referenced in some older docs. That legacy checker is
NOT present in this isolated toolkit; claiming it passed would be false. This
file documents the actual review that was performed.

## Substitute review

Frames sampled at 15%, 50%, and 85% of every beat (36 frames total, plus a
per-beat contact sheet) were opened with the image-capable Read tool and
inspected for:

| Property | Observation |
|---|---|
| Typeface consistency | EB Garamond (serif) for all narrative headings; JetBrains Mono / Iosevka for code and composer output. Consistent across all 12 beats. |
| Kerning at large sizes | The B01 BrutalistHesitantWriter (bumped to fontSize 148, lineSpacing 1.25) shows clean serif tracking with no touching glyphs at any sampled frame. |
| Line-length legibility | Composer and quote blocks (B00, B02-B08, B10) wrap inside the ~65-character comfortable range at 3840×2160. |
| Underscore / hyphen / em-dash contrast | Terracotta accent used exclusively on active/state elements; ink text stays neutral. No accidental underline artefacts. |
| Anti-aliasing at 4K | 3840×2160 output source is Remotion at design 1920×1080 rendered at 2× — text is crisp at native resolution. |
| Bookend text alignment | ClaudeTitleOutro B11 title landing, terracotta period, and @NikBearBrown handle are properly aligned. |

## Gate V typography-adjacent checks

Gate V's underfill (55% floor) and edge-bleed checks are, in practice,
typography-adjacent because most of this teardown's content is text. Both
passed with zero blockers and zero majors on landscape.

## Not claimed

- No claim that a legacy `scripts/type_check.py` ran (it does not exist here).
- No claim that a kerning-only linter ran (none is shipped).
- No claim that human proofreading has happened for this run. Bear's viewing
  is next.
