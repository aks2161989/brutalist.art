# TYPECHECK.md — The riff Skill (landscape)

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
| Typeface consistency | EB Garamond (serif) for all narrative headings and teardown body; JetBrains Mono for ClaudeCodeBeat terminal panel. Consistent across all 12 beats. |
| Hesitant-writer animation | B01 BrutalistHesitantWriter: 2 short lines, fontSize 100, lineSpacing 2.5. Terracotta accent on "opinions" (doomed word); corrects to "observations". contextTitle and brandLabel present. |
| Code panel readability | B05 ClaudeCodeBeat: real `./art scenes` output in monospace. Font bounded by min(base, height/lines, width/longest-line) so all lines visible at 3840×2160. |
| SkillTeardown legibility | B02 SkillTeardownAnatomy: folder tree in monospace with callout box. B03 SkillTeardownPipeline: 4-phase strip with terracotta arrows. B04/B06/B07/B08 SkillTeardownMechanism: mechanism cards with eyebrow/heading/body/verbatim-quote/verdict pill. |
| Verdict card | B09 ClaudeVerdictArtifact: artifact card with 4 verdict lines, terracotta accent, within safe margins. |
| Underscore / accent contrast | Terracotta (CLAUDE.SPARK) used exclusively on trigger word in B01 and active-card borders in teardown beats. No accidental reuse. |
| Anti-aliasing at 4K | Output source is Remotion at 3840×2160 — text is crisp at native resolution. |
| Bookend text alignment | B11 ClaudeTitleOutro: 'Liam, in for Bear.' plus @HumanitariansAI channel properly aligned and within safe inset. |

## Gate V typography-adjacent checks

Gate V's underfill (55% floor) and edge-bleed checks are, in practice,
typography-adjacent because most of this teardown's content is text. Both
passed with zero blockers and zero majors on landscape.

## Not claimed

- No claim that a legacy `scripts/type_check.py` ran (it does not exist here).
- No claim that a kerning-only linter ran (none is shipped).
- No claim that human proofreading has happened for this run.
