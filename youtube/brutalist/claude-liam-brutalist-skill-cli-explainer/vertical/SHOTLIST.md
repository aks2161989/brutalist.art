# SHOTLIST.md — The cli-explainer Skill (landscape 16:9 · 3840×2160)

13 beats. Cream stage, warm ink, one terracotta accent per beat. NBB/@HAI corner mark disabled by design (channel adaptation — the outro carries the handle at full size).

| Beat | Scene (Remotion id) | What appears | Terracotta moment |
|---|---|---|---|
| B00 | `ClaudeComposerAsk` | Cold-open composer, greeting "Namaste, Liam", ask types in, `runningText` "reading the skill…", three result lines. | Send button arms; `runningText` glyph. |
| B01 | `BrutalistHesitantWriter` | Two-line serif claim types out: "cli-explainer is a screen recorder." then "a screen recorder" is struck and replaced by "a set of instructions". | The doomed phrase renders in `CLAUDE.SPARK` before backspacing. |
| B02 | `SkillTeardownAnatomy` | Folder tree of `skills/make/cli-explainer/`: SKILL.md (accented, 365 lines · 3,262 words), reference/example-cli-beat_sheet.json. Callout: "Claude reads the file. The file writes the reel." | `SKILL.md` line + callout arrow. |
| B03 | `SkillTeardownPipeline` | Horizontal pipeline: TRIGGER → INTRO → PROBLEM → **ASK·CODE·OUTPUT (cycle 1)** → ASK·CODE·OUTPUT (cycle 2) → SUMMARY → NEXT STEPS → OUTRO → REEL. Cycle 1 phase is accented. | The accented phase card; connector arrows. |
| B04 | `ClaudeComposerAsk` | Inner beat — composer with the trigger already typed: `cli The cli-explainer Skill`. Greeting "The ask,". `runningText` "loading skills/make/cli-explainer…". | Send button + `runningText` glyph. |
| B05 | `ClaudeCodeBeat` | Real SKILL.md excerpt: "§ The required beat spine" — the three mandatory items numbered. Filename tab: `skills/make/cli-explainer/SKILL.md`. Spark: "The revision is not optional." | Active traffic-light dot on the code card. |
| B06 | `SkillTeardownMechanism` | Heading "The Revision Law." · body sentence · verbatim quote block · citation. Verdict chip: "The doctrine names its own edge case." (positive). | The quote's opening quote glyph + verdict chip. |
| B07 | `ClaudeComposerAsk` | Inner beat — composer with the revised trigger already typed: `cli The cli-explainer Skill --tool codex`. Greeting "The revision,". `runningText` "switching skin: claude → codex…". | Send button + `runningText` glyph. |
| B08 | `ClaudeCodeBeat` | Real SKILL.md excerpt: "§ Skins — chosen by --tool" — the three verbatim renames plus the CodexComposerAsk nuance. Filename tab identical to B05. Spark: "One rename. Same reel." | Active traffic-light dot on the code card. |
| B09 | `SkillTeardownMechanism` | Heading "The spine survives the skin." · body · verbatim quote. Verdict chip: "This is the thing the file gets right." (positive). | Verdict chip + quote glyph. |
| B10 | `ClaudeVerdictArtifact` | Artifact card. Title "The cli-explainer Skill." Heading "What cli-explainer actually is". Three staggered lines. | Terracotta period after the title. |
| B11 | `ClaudeComposerAsk` | Handoff beat — greeting "Your turn." Composer types the paste-ready prompt. `runningText` "paste this into Claude…". | Send button + `runningText` glyph. |
| B12 | `ClaudeTitleOutro` | Title restate "The cli-explainer Skill" with terracotta period. `@HumanitariansAI` beneath in serif. Slug-seeded mascot. | Terracotta terminal punctuation. |

## Ordering / dependencies

- B00 cold-opens on the Claude UI (COLD OPEN LAW).
- B01 is the EXECUTIVE-SUMMARY hesitant-writer beat with `lead_silence_s: 0.8` and target audio ≥ 9 s.
- B02–B03 = "what is a skill" + pipeline (skill-teardown modifier § body).
- B04–B05 = first ASK → CODE pair (worked example — the trigger and the rule that owns THIS reel).
- B06 = mechanism 1 verbatim (VERBATIM QUOTE LAW).
- B07–B08 = the revision (REVISION LAW satisfied inline — the video is itself a two-cycle build).
- B09 = mechanism 2, the design tell.
- B10 = verdict artifact page.
- B11 = HANDOFF LAW composer with the "Your turn." greeting; prompt read aloud.
- B12 = OUTRO LAW title restate.

## Portrait shot list

The `vertical/beat_sheet.json` mirrors the same 13 beats but swaps every scene id
for its native 9:16 variant (`*916`). Text reflows via percentage-based positioning;
no crops.
