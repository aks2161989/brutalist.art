# SHOTLIST — The guests Skill (portrait 9:16, 2160×3840)

Same twelve beats, same measured Kokoro audio, native portrait layouts.

| # | Beat | Composition | Motion | Audio (s) |
|---|---|---|---|---|
| B00 | ASK / cold open | `ClaudeComposerAsk916` | type-on | 13.16 |
| B01 | BLUF / hesitant writer | `BrutalistHesitantWriter916` | type-on with correction | 15.51 |
| B02 | Anatomy | `SkillTeardownAnatomy916` | reveal | 22.36 |
| B03 | Pipeline | `SkillTeardownPipeline916` | reveal | 22.34 |
| B04 | Mechanism 1 — Absence, not a toggle | `SkillTeardownMechanism916` | reveal | 30.42 |
| B05 | Mechanism 2 — GATE G | `SkillTeardownMechanism916` | reveal | 26.37 |
| B06 | Mechanism 3 — The recording | `SkillTeardownMechanism916` | reveal | 36.31 |
| B07 | Mechanism 4 — Naming and voice | `SkillTeardownMechanism916` | reveal | 28.95 |
| B08 | Falsifiability | `SkillTeardownMechanism916` | reveal | 27.50 |
| B09 | Verdict — artifact card | `ClaudeVerdictArtifact916` | scale-in + reveal | 27.37 |
| B10 | Your Turn | `ClaudeComposerAsk916` | type-on | 39.17 |
| B11 | Outro | `ClaudeTitleOutro916` | hold | 3.24 |

Measured audio total: **292.72 s** (~4:53).

## Portrait-specific layout changes

- B01: text `"The guests skill\ncopies the\nfellows spine.\nA board member\nis not a fellow."` (5 lines vs landscape 4) at `fontSize 118 / lineSpacing 2.2` — meets FILL_MIN 0.55 on portrait under the portrait-aware scale patch on `BrutalistHesitantWriter`.
- `metadata.channel_title` removed to prevent compile-overlay bleed past portrait safe.b (memory `feedback_channel_title_portrait_bleed`). Folder chip inside the composer beats still shows `@HumanitariansAI`.

## Skin lint

The compiler's skin lint flags the `916` composition names against the
aspect-blind landscape names (`ClaudeComposerAsk916` on a claude-palette cold
open; `ClaudeTitleOutro916` on the outro). Same warnings as the sibling
`fellows` portrait companion — the portrait-native trade-off, not defects.
