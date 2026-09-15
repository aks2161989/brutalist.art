# TYPECHECK.md — The nopunt Skill (vertical 9:16)

## What this file is

A record of the visual-typography review that runs in place of the legacy
`scripts/type_check.py` referenced in some older docs. That legacy checker is
NOT present in this isolated toolkit; claiming it passed would be false. This
file documents the actual review that was performed on the portrait master.

## Substitute review

Frames sampled at 15%, 50%, and 85% of every beat (36 frames total, plus a
contact sheet) were opened with the image-capable Read tool and inspected
for:

| Property | Observation |
|---|---|
| Portrait fit — no cropped landscape | Every 916 composition is registered at 1080×1920 in `Root.tsx`, rendered natively at 2160×3840. Confirmed by ink-bounds analysis (per-beat text is centered, not cut off at a landscape crop line). |
| B01 hesitant writer readable in portrait | fontSize 300 × scale 0.5625 × 2 = ~338px actual serif. Three short balanced lines. Trigger swap (`linter` → `catalog`) renders through the mistake/repair animation. |
| Composer legibility in portrait | Composer card in B00 and B10 wraps within safe.r=2052. The three output lines under the card fit inside safe.b=3648. |
| Kerning at large sizes | EB Garamond serif at 300px in B01 shows clean tracking, no touching glyphs at any sampled frame. |
| Anti-aliasing at 4K portrait | 2160×3840 output is Remotion at design 1080×1920 rendered at 2× — text is crisp at native resolution. |
| Outro alignment | ClaudeTitleOutro916 title, terracotta period, and @NikBearBrown handle centered per OUTRO-LOCK. |

## Gate V typography-adjacent checks

Gate V's underfill (55% floor) and edge-bleed checks apply the portrait safe
inset (SAFE916: x=54-1026, y=96-1824 at design). All 24 sampled portrait
frames passed with zero blockers, zero majors.

## Not claimed

- No claim that a legacy `scripts/type_check.py` ran (it does not exist here).
- No claim that a kerning-only linter ran (none is shipped).
- No claim that human proofreading has happened. Bear's viewing is next.
