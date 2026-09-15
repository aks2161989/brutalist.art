# PROMPTS — The godot-waikthrough Skill
# run_id: ba2520ca602d4f778cd158dd8646d0c3

## B00 — Ask (ClaudeComposerAsk)

```
What does `godot-waikthrough` actually do? Read
skills/make/godot-waikthrough/SKILL.md — is this a screen recorder,
a game builder, or something else entirely?
```

Result lines:
- "It plays the game."
- "Riff captures the why."
- "It makes a narrated walkthrough film."

## B11 — Your Turn (paste-ready prompt for viewer)

```
Read skills/make/godot-waikthrough/SKILL.md in full. I have a Godot 4
project at [path]. Produce a Phase 1 feature inventory: list every
implemented feature from source and mark each as built, planned, or broken.
Then write coverage.json for my game.
```

**Rubric:** Replace [path] with any Godot 4 project folder. When Claude
returns, verify the inventory against what you know the game actually does.
If a feature is missing from the inventory, ask Claude to read that specific
script and trace the input path. The quality of the inventory determines the
quality of the walkthrough film.

## Walker mode GDD prompt (B07 reference — illustrative reconstruction)

The SKILL.md specifies: "Prompt begins 'Please use Walker to convert my game
design document about …' and describes this game's actual idea, then asks
for a playable Godot project."

Example (reconstructed for illustration — not a historical transcript):

```
Please use Walker to convert my game design document about a simple 2D
platformer called walker-jumpman. The player jumps over spikes and gaps to
reach a finish flag. Read skills/make/godot-waikthrough/SKILL.md and
skills/make/godot-gamedev/SKILL.md for the walkthrough and gamedev workflows.
Then produce a playable Godot 4 project for me.
```

Labeled as: "Illustrative reconstruction — not a historical transcript"
per SKILL.md §3 B00 requirement.

## Scene search log

Scenes searched before beat authoring per GATE L (Library-first):

- `./art scenes "gameplay walkthrough riff"` → WalkerGodotSetup (hit — used B02, B05, B07)
- `./art scenes "feature inventory GDD"` → GodotDesignBoard (hit — used B04)
- `./art scenes "riff mechanic RIFF.md"` → GodotDevWorkbench code mode (nearest hit — used B06)
- `./art scenes "skill pipeline phases"` → SkillTeardownPipeline/Anatomy/Mechanism (hits — used B03, B08, B09)
- `./art scenes "skill teardown mechanism quote"` → SkillTeardownMechanism (hit — used B08, B09)
- No PUNT beats — all content types map to catalog rows in nopunt/SKILL.md
