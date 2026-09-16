# SHOTLIST — Short cut

9 beats · native 2160×3840 9:16 · Kokoro `am_onyx` throughout · no captions.
Derived from the parent's native portrait companion; every retained beat is
copied unchanged (no re-render, no crop, no audio regeneration).

| # | Beat | Act | Scene (9:16) | What the viewer WATCHES | Dur (s) |
|---|---|---|---|---|---|
| 0 | B00 | ASK | ClaudeComposerAsk916 | Cream Claude composer. Greeting reads "Hej, Liam" in serif with terracotta period. Prompt types onto the composer, running indicator ("reading skills/make/ai-explainer/SKILL.md…"), three output lines resolve. | 18.17 |
| 1 | B01 | BLUF | HesitantWriterFramed916 | Two lines type in serif. Writer types "The ai-explainer skill is a template. It reads a whole SKILL file first." then the word `template` flashes terracotta and is corrected to `workflow`. | 13.83 |
| 2 | B03 | FRAMEWORK | SkillTeardownPipeline916 | Eyebrow "SKILL · PIPELINE". Title "One pipeline, five phases, one master." Vertical stack (portrait): INPUT (SKILL.md + topic) → Scaffold · Narrate · Audio (terracotta) · Visuals · Compile → OUTPUT `<slug>.mp4`. Footer note: "Audio-first. Every visual conforms to the measured voice." | 19.83 |
| 3 | B04 | MECHANISM · ACT 1 | SkillTeardownMechanism916 | Heading "Fixed bookends. Free interior." Body naming the six moves. Terracotta quote card: "The bookends do not change… The modifier governs the MIDDLE." Cite: ai-explainer SKILL.md. Terracotta verdict pill "predictable spine, teachable frame". | 18.21 |
| 4 | B05 | MECHANISM · ACT 2 | SkillTeardownMechanism916 | Heading "The UI earns its beats." Body about when the UI is allowed. Terracotta quote card with the ILLUSTRATE LAW smell/failure line. Verdict pill "kills wallpaper reels". | 20.67 |
| 5 | B06 | MECHANISM · ACT 3 | SkillTeardownMechanism916 | Heading "Ask, then the receipt." Body about the composer-then-graphic pattern. Terracotta quote card with the ASK → RESULT LAW verbatim. Verdict pill "prompts as receipts". | 16.88 |
| 6 | B07 | DESIGN · TELL | SkillTeardownMechanism916 | Heading "Where it bites." Body naming "unread paragraph = silent bug" and "Liam not Bear". Terracotta quote card with the IN-FOR-BEAR LAW verbatim "A named voice, never a clone." Neutral (non-positive) verdict pill "requires a reader". | 21.42 |
| 7 | B08 | VERDICT | ClaudeVerdictArtifact916 | Artifact card headed "The verdict." Six bulleted lines: A workflow, not a template pack. Fixed bookends. Free interior. The UI earns every beat (ILLUSTRATE LAW). Prompts as receipts (ASK → RESULT). Kokoro is the clock. compile.py conforms. Renders only. Never publishes. | 15.00 |
| 8 | B10 | OUTRO | ClaudeTitleOutroHAI916 | Poster serif title "The ai-explainer Skill" with terracotta period, seeded mascot beneath. `Liam, in for Bear.` under the title. | 3.92 |

Total (planned): 147.93s. See CUT-PLAN.json for the drop rationale.

## Portrait media reuse

The parent reel is a native 2160×3840 build (see the parent's
`vertical/CHECKS-REPORT.md`). `shorts.py` detected 9:16 aspect and reused
every kept beat's `media/<BID>.mp4` unchanged into this Short's `media/`.
No `<BID>-916.mp4` center cut was ever produced; no Remotion 916
composition was re-rendered by this Short. The kept mp3s were also copied
byte-for-byte from `parent/vertical/mp3/beat-<BID>.mp3`.

## Dropped

- B02 (SkillTeardownAnatomy916, 17.54s) — generic anatomy of a skill folder.
- B09 (ClaudeComposerAsk916 "Your Turn", 21.46s) — extended Your Turn.
