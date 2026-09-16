# SHOTLIST — The guests Skill — Short (9:16, 2160×3840)

Whole-beat cut: 5 of 12 beats retained. Dropped: B02, B04, B05, B06, B07,
B08, B10. Native portrait renders and Kokoro `am_onyx` mp3s copied unchanged
from the vertical parent. Total measured audio: **81.71 s** (~1:22).

| # | Beat | Composition | Motion | Audio (s) |
|---|---|---|---|---|
| B00 | ASK / cold open | `ClaudeComposerAsk916` | type-on | 13.16 |
| B01 | BLUF / hesitant writer | `BrutalistHesitantWriter916` | type-on with correction | 15.51 |
| B03 | Pipeline — six beats, one fixed spine | `SkillTeardownPipeline916` | reveal | 22.34 |
| B09 | Verdict — artifact card | `ClaudeVerdictArtifact916` | scale-in + reveal | 27.37 |
| B11 | Outro | `ClaudeTitleOutro916` | hold | 3.24 |

## Dropped beats (summary)

| Beat | Act | Reason |
|---|---|---|
| B02 | FRAMEWORK — Anatomy | Folder tree belongs in the long |
| B04 | MECHANISM 1 — Absence, not a toggle | Dangling 'First design decision' without acts 2–4; verdict covers in one line |
| B05 | MECHANISM 2 — GATE G | Dangling 'Second decision'; verdict names GATE G in one line |
| B06 | MECHANISM 3 — The recording | Dangling 'Third decision'; verdict covers never-cut rule in one line |
| B07 | MECHANISM 4 — Naming and voice | Dangling 'Fourth decision'; verdict covers channel voice in one line |
| B08 | FALSIFIABILITY | Outro-follows-channel craft argument belongs in the long |
| B10 | YOUR TURN | Detailed dry-run assignment belongs in the 16:9 long |

## Portrait-specific layout notes

- B01: `BrutalistHesitantWriter916` with `fontSize: 130 / lineSpacing: 2.4`,
  five-line split — meets FILL_MIN 0.55 under the portrait-aware scale patch.
- `metadata.channel_title` removed to prevent compile-overlay bleed past
  portrait `safe.b`. Folder chip inside B00 still shows `@HumanitariansAI`.

## Skin lint (inherited from vertical parent)

Two `SKIN LINT` warnings (B00, B11) noting `*916` composition names against
the aspect-blind `palette=claude` rule — portrait-native trade-off, not defects.
