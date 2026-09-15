# SHOTLIST — The finance Skill teardown

Twelve beats, one visual per beat. Registered Remotion scenes only. Cream page,
warm ink, terracotta accent per Claude brand. `shot.show` on every beat.

| # | Scene | Motion | Duration ⌛ |
|---|---|---|---|
| B00 | `ClaudeComposerAsk` | type-on composer + result output | ~15s |
| B01 | `BrutalistHesitantWriter` | typed text with correction on "picks the chart" | ≥10s (min 9s per COLD OPEN LAW; audio ≥10s) |
| B02 | `SkillTeardownAnatomy` | folder tree reveal + callout | ~22s |
| B03 | `SkillTeardownPipeline` | pipeline nodes reveal with accent on the "four charts" phase | ~22s |
| B04 | `SkillTeardownMechanism` | heading + body + quote + verdict pill | ~26s |
| B05 | `SkillTeardownMechanism` | heading + body + quote + verdict pill | ~30s |
| B06 | `SkillTeardownMechanism` | heading + body + quote + verdict pill | ~30s |
| B07 | `SkillTeardownMechanism` | heading + body + quote + verdict pill | ~30s |
| B08 | `SkillTeardownMechanism` | heading + body + quote + verdict pill | ~28s |
| B09 | `ClaudeVerdictArtifact` | artifact card, six-line verdict | ~28s |
| B10 | `ClaudeComposerAsk` (greeting `Your Turn`) | type-on composer + rubric output | ~40s |
| B11 | `ClaudeTitleOutro` | poster serif title + terracotta period + @NikBearBrown | ~4s |

## Portrait (9:16)

Same twelve beats, native portrait compositions:

| # | Landscape scene | Portrait scene |
|---|---|---|
| B00 | ClaudeComposerAsk | ClaudeComposerAsk916 |
| B01 | BrutalistHesitantWriter | BrutalistHesitantWriter916 |
| B02 | SkillTeardownAnatomy | SkillTeardownAnatomy916 |
| B03 | SkillTeardownPipeline | SkillTeardownPipeline916 |
| B04–B08 | SkillTeardownMechanism | SkillTeardownMechanism916 |
| B09 | ClaudeVerdictArtifact | ClaudeVerdictArtifact916 |
| B10 | ClaudeComposerAsk | ClaudeComposerAsk916 |
| B11 | ClaudeTitleOutro | ClaudeTitleOutro916 |

Portrait beat sheet keeps the same script, seeds, and props; only the scene
name and the aspect-ratio metadata differ. The compile pass targets
`--height 3840` and writes `[slug]-vertical.mp4`.

## `shot.show` events per beat

See `beat_sheet.json` for the full `shot.show` array on each beat. Every body
beat names its on-screen artifact in `shot.show[0].event`, and event ordering
matches narration order (per SHOW-DON'T-TELL LAW).

## SPARK-LINE compliance

Every inner beat's sparkLine is set from the beat's key line, ≤ 4 words:

- B02 — "Toolkit side. Fellow side."
- B03 — "Eleven beats. Same order."
- B04 — "Locked shapes. No choice."
- B05 — "Never retyped. Ever."
- B06 — "Two audits. Both fail."
- B07 — "Two channels always."
- B08 — "Knows its own limit."

## ILLUSTRATE LAW compliance

The Claude interface appears only at B00 (cold open), B10 (Your Turn), and
B11 (title outro). Every body beat is a concept illustration on cream, no
composer wallpaper.
