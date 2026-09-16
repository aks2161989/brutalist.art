# PROMPTS.md — The godot-gamedev Skill
# Episode 13 · Brutalist playlist · Run ID: 04c05055640542eaa4f9b9082b7b516c

## Paste-ready prompt shown in B11 (Your Turn beat)

> Read `skills/make/godot-gamedev/SKILL.md` in full. Then apply it to the game project at `./my-game` — produce a complete developer's walk-through in `GAMEDEV-GUIDE.md` covering the player loop, scene inventory, signal map, and at least two open questions the code raises but does not answer.

**Expected artifact**: `GAMEDEV-GUIDE.md` — structured markdown guide, four phases, all claims traceable to source.

**Test of success**: Open the guide, pick any claim, find its source in the game project. If untraceable, the skill violated its reconstruction rule — flag in FEEDBACK.md.

---

## Prompt used in B00 (cold open composer)

> What does `godot-gamedev` actually do? Read `skills/make/godot-gamedev/SKILL.md` — is this a game builder, a game player, or something else entirely?

---

## Internal production prompts (not shown in film)

### Skill reading prompt
Used to read and understand the full skill before authoring:
> Read `skills/make/godot-gamedev/SKILL.md` in full, including all section headers, rules, phases, and notes. Summarize: (1) what the skill does, (2) what it requires as input, (3) what it produces as output, (4) its reconstruction constraint, (5) its known limitations.

### BLUF design prompt
Used to design the B01 hesitant-writer beat:
> Design a single-sentence BLUF for godot-gamedev that corrects the most common misconception (that the skill generates game code). The sentence should correct exactly one token (the misconception word) mid-sentence. Keep tokens as single words for triggerWords/replacementWords compatibility.

### Teaching illustration prompt (not executed — documented limitation)
> The following would be the prompt to generate a real demo if a Godot project were available: `art godot-gamedev --project ./my-game` — this is documented as an unexecuted step in B09.

---

## No fabricated prompts
No narration or visual in this episode claims to show actual Claude responses that were not obtained during this run. The cold open output lines are authored based on the skill's documented behaviour, not a live Claude call. This is consistent with BUILD-PROMPT.md's requirement to use source-backed demonstrations and label them accurately.
