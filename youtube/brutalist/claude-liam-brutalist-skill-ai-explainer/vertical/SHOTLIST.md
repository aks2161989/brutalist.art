# SHOTLIST

11 beats · 16:9 landscape master · portrait companion authored separately. Kokoro `am_onyx` throughout. No captions.

| # | Beat | Act | Scene (16:9) | Scene (9:16) | What the viewer WATCHES |
|---|---|---|---|---|---|
| 0 | B00 | ASK | ClaudeComposerAsk | ClaudeComposerAsk916 | Cream Claude composer. Greeting reads "Hej, Liam" in serif with terracotta period. Prompt types onto the composer, running indicator ("reading skills/make/ai-explainer/SKILL.md…"), three output lines resolve. |
| 1 | B01 | BLUF | BrutalistHesitantWriter | BrutalistHesitantWriter916 | Two lines type in serif. Writer types "The ai-explainer skill is a template pack / for Claude-branded videos." then reconsiders — the phrase "a template pack" flashes terracotta, is deleted, and "a workflow that reads a whole SKILL file" types in its place. |
| 2 | B02 | FRAMEWORK | SkillTeardownAnatomy | SkillTeardownAnatomy916 | Eyebrow "SKILL · ANATOMY · was claude-explainer". Title "A skill is a folder Claude reads first." A folder tree reveals file-by-file: the skill root, SKILL.md (terracotta accent), AUDIT-MODE.md, referenced files section, four referenced docs, the parent explainer folder. Terracotta-bordered callout: "The SKILL.md is the instruction." |
| 3 | B03 | FRAMEWORK | SkillTeardownPipeline | SkillTeardownPipeline916 | Eyebrow "SKILL · PIPELINE". Title "One pipeline, five phases, one master." Left-to-right row (landscape) or top-to-bottom stack (portrait): INPUT (SKILL.md + topic) → Scaffold · Narrate · Audio (terracotta) · Visuals · Compile → OUTPUT `<slug>.mp4`. Nodes reveal in narration order. Footer note: "Audio-first. Every visual conforms to the measured voice." |
| 4 | B04 | MECHANISM · ACT 1 | SkillTeardownMechanism | SkillTeardownMechanism916 | Heading "Fixed bookends. Free interior." Body naming the six moves. Terracotta quote card: "The bookends do not change… The modifier governs the MIDDLE." Cite: ai-explainer SKILL.md. Terracotta verdict pill "predictable spine, teachable frame". |
| 5 | B05 | MECHANISM · ACT 2 | SkillTeardownMechanism | SkillTeardownMechanism916 | Heading "The UI earns its beats." Body about when the UI is allowed. Terracotta quote card with the ILLUSTRATE LAW smell/failure line. Verdict pill "kills wallpaper reels". |
| 6 | B06 | MECHANISM · ACT 3 | SkillTeardownMechanism | SkillTeardownMechanism916 | Heading "Ask, then the receipt." Body about the composer-then-graphic pattern. Terracotta quote card with the ASK → RESULT LAW verbatim. Verdict pill "prompts as receipts". |
| 7 | B07 | DESIGN · TELL | SkillTeardownMechanism | SkillTeardownMechanism916 | Heading "Where it bites." Body naming the "unread paragraph = silent bug" and "Liam not Bear". Terracotta quote card with the IN-FOR-BEAR LAW verbatim "A named voice, never a clone." Neutral (non-positive) verdict pill "requires a reader". |
| 8 | B08 | VERDICT | ClaudeVerdictArtifact | ClaudeVerdictArtifact916 | Artifact card headed "The verdict." Six bulleted lines: A workflow, not a template pack. Fixed bookends. Free interior. The UI earns every beat (ILLUSTRATE LAW). Prompts as receipts (ASK → RESULT). Kokoro is the clock. compile.py conforms. Renders only. Never publishes. |
| 9 | B09 | YOUR TURN | ClaudeComposerAsk | ClaudeComposerAsk916 | Greeting "Your Turn". Prompt types in — the actual paste-ready command asking Claude to use ai-explainer on the viewer's own topic. Three success-test lines resolve as output. Liam READS the prompt aloud. |
| 10 | B10 | OUTRO | ClaudeTitleOutro | ClaudeTitleOutro916 | Poster serif title "The ai-explainer Skill" with terracotta period, seeded mascot beneath (per OUTRO-LOCK.md pixel-art contract). Silent under narration. |

## Timing intents

Estimated total duration ≈ 254s (~4:14). Real durations become ground truth after Kokoro measures each MP3 — the beats' `actual_duration_s` will be written back by `generate_audio_kokoro.py`. Every scene beat renders extending to the measured audio via `remotion_scenes.py` (`extend_clip_to_duration` freeze-pads the tail).

## Portrait companion notes

The portrait pass uses `./art vertical` (shorts.py --vertical), which rewires every Remotion pattern to its `<Pattern>916` counterpart. All eight pattern names above have registered 916 variants in the isolated toolkit's Root.tsx (three were added in this session: SkillTeardownAnatomy916, SkillTeardownPipeline916, SkillTeardownMechanism916 — the pipeline variant is a stacked layout, not a squashed landscape). The portrait audio is copied byte-for-byte from the landscape run; no re-synthesis, and no beat is dropped.
