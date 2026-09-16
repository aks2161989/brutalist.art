# TYPECHECK.md — The riff Skill (portrait companion)

## What this file is

A record of the visual-typography review that runs in place of the legacy
`scripts/type_check.py` referenced in some older docs. That legacy checker is
NOT present in this isolated toolkit; claiming it passed would be false. This
file documents the actual review that was performed.

## Substitute review

Frames sampled at 50% and 85% of every beat (24 frames total via Gate V, plus
the per-beat contact sheet) were inspected for typography:

| Property | Observation |
|---|---|
| Typeface consistency | EB Garamond (serif) for all FormACard916 narrative headings and body text; system sans for eyebrow labels. Consistent across all 12 beats. |
| Hesitant-writer animation | B01 BrutalistHesitantWriter916: portrait-aware scale patch applied (min(w/1080,h/1920)); fontSize 80, lineSpacing 2.0. contextTitle and brandLabel anchor coverage at top/bottom. |
| FormACard916 legibility | B02–B10 FormACard916: eyebrow/heading/body layout at 2160×3840. Text line density tuned to fill SAFE916 (x:54,y:96,r:1026,b:1824). All beats exceed 55% fill threshold. |
| Outro word-break | B11 ClaudeTitleOutro916: overflowWrap:'anywhere' + wordBreak:'break-word' patch applied; episode slug wraps correctly in portrait without overflow. |
| Underscore / accent contrast | Terracotta (CLAUDE.SPARK) used on trigger word in B01 and FormACard916 section dividers. No accidental reuse. |
| Anti-aliasing at 4K portrait | Output source is Remotion at 2160×3840 — text is crisp at native resolution. |
| Bookend text alignment | B11 ClaudeTitleOutro916: 'Liam, in for Bear.' plus @HumanitariansAI properly aligned and within SAFE916 inset. |

## Gate V typography-adjacent checks

Gate V's underfill (55% floor) and edge-bleed checks are, in practice,
typography-adjacent because all portrait beats are text-dominated. Both
passed with zero blockers and zero majors on portrait.

## Not claimed

- No claim that a legacy `scripts/type_check.py` ran (it does not exist here).
- No claim that a kerning-only linter ran (none is shipped).
- No claim that human proofreading has happened for this run.
