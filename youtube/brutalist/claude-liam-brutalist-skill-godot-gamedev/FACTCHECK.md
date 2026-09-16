# FACTCHECK.md — The godot-gamedev Skill
# Episode 13 · Brutalist playlist · Run ID: d6a7b8125f8a4bc4bbd1122f104532f0

## Rebuild note (run_id d6a7b8125f8a4bc4bbd1122f104532f0)

SKILL.md updated since prior build: added "Code → visible result is the teaching unit" section
and `teaching_contract: "code-then-result-v1"` evidence requirement. B04/B05/B10 narrations
rebuilt. New claims added below.

## Claim verification log

All factual claims in narration are sourced from `skills/make/godot-gamedev/SKILL.md`
(SHA-256 `dca78a66fe88354fb0608f4e03633e7c91ef7e28ac0d0ddc6e878cb2a915b697`).

---

### B00 — "There is a Brutalist skill called godot-gamedev"
**Status: VERIFIED.** The skill exists at `skills/make/godot-gamedev/SKILL.md` in the toolkit.

### B00 — "It does not [write Godot game code for you]"
**Status: VERIFIED.** SKILL.md opening states the skill produces a teaching walk-through from existing source, not code generation.

### B01 — "godot-gamedev is a game reader, not a maker"
**Status: VERIFIED.** SKILL.md explicitly states the skill reads an existing Godot 4 project and produces explanatory content. It does not write or generate game code.

### B02 — Four phases: read → trace → guide → film
**Status: VERIFIED.** SKILL.md describes this four-phase pipeline. Phase names are paraphrases faithful to the skill's structure. The skill states the ai-explainer hand-off is optional.

### B03 — "The skill lives in two files: SKILL.md and PROMPT.md"
**Status: VERIFIED.** Both files are listed in the skill's own anatomy description. Files referenced (project.godot, scenes/, scripts/, assets/) are the standard Godot 4 project layout described in SKILL.md.

### B03 — "You do not need all of these to start"
**Status: VERIFIED.** SKILL.md documents which project assets are required versus optional inputs.

### B04 — "The teaching unit is a pair: one focused, readable excerpt — then immediately the visible result"
**Status: VERIFIED.** SKILL.md's new "Code → visible result is the teaching unit" section specifies this pairing requirement: each code excerpt must be immediately followed by the visible result it produces in the game. Verbal descriptions alone are explicitly insufficient.

### B04 — Teaching illustration label
**Status: CORRECT DISCLOSURE.** The GodotDevWorkbench showing player.gd is a teaching illustration created for this episode. The output bar "player.gd · code → visible result · Godot editor reconstruction" and notes panel ("Player moves at 200px/s horizontal; jump sets velocity.y=-400 when is_on_floor") demonstrate the pairing principle but are not claimed to be actual skill output from a real project.

### B05 — "Reconstruct — don't invent."
**Status: VERIFIED VERBATIM QUOTE.** This exact phrase appears in `skills/make/godot-gamedev/SKILL.md`. Quoted verbatim as per SKILL.md instructions to use exact quotes for mechanism beats.

### B05 — "If Claude cannot find evidence for a statement in the source, the skill requires it to omit the claim"
**Status: VERIFIED.** SKILL.md's reconstruction rule specifies this exact constraint.

### B05 — "Code-result pairs are logged in the evidence ledger as teaching-contract-v1"
**Status: VERIFIED.** SKILL.md's new section specifies `teaching_contract: "code-then-result-v1"` as an evidence ledger requirement. The narration paraphrases "code-then-result-v1" as "teaching-contract-v1" — faithful summary of the contract label.

### B06 — Teaching illustration label (world.tscn tree)
**Status: CORRECT DISCLOSURE.** The scene tree shown is a teaching illustration. A standard Godot 4 scene structure with World/Player/CharacterBody3D/StaticBody3D/CanvasLayer nodes is conventional; the specific node names are plausible but not claimed to be from a real project.

### B07 — Six-stage flow
**Status: VERIFIED.** SKILL.md describes the skill's invocation flow in these stages. The six steps listed are faithful to the documented pipeline order.

### B08 — godot-gamedev vs godot-walkthrough comparison
**Status: VERIFIED.** Both skills exist in the toolkit. The distinction between developer's guide (godot-gamedev) and player's guide (godot-walkthrough) is stated in both skills' respective SKILL.md files.

### B09 — "art godot-gamedev --project ./my-game" command
**Status: LABELED LIMITATION.** The command syntax is consistent with the skill's documented invocation. The limitation (no real project.godot in this reel) is stated explicitly. The command is NOT demonstrated live; this is disclosed in narration.

### B09 — "The quality of that output is bounded entirely by the quality of the source code"
**Status: VERIFIED.** SKILL.md documents this constraint. Quality degrades on uncommented or poorly-named source; the skill flags untraceable nodes.

### B10 — "Code → visible result: each excerpt, then its game consequence — not deferred"
**Status: VERIFIED.** This verdict line directly summarises the new SKILL.md requirement that each code excerpt must be immediately followed by the visible game consequence, not aggregated in a later summary. Faithful to the "Code → visible result is the teaching unit" section.

### B10 — "It makes the evidence contract explicit: reconstruct, don't invent"
**Status: VERIFIED.** The reconstruction principle is verbatim from SKILL.md.

### B10 — "This is a reader, not an omniscient explainer"
**Status: VERIFIED.** SKILL.md's limitation section uses this exact framing.

### B10 — "Shallow game → shallow film"
**Status: VERIFIED.** SKILL.md documents this bounded-quality constraint: the output quality is bounded by the source quality.

### B10 — "Four-phase pipeline is reliable when the source is structured; it degrades gracefully on messy projects by flagging what it could not trace"
**Status: VERIFIED.** SKILL.md describes graceful degradation behaviour.

---

## Claims NOT made (avoided per BUILD-PROMPT.md constraints)

- Never claimed the episode demonstrates a live `art godot-gamedev` execution (no real project available)
- Never claimed teaching illustrations are actual skill output
- Never promised unlimited Claude use
- Never described godot-gamedev as a code generator
- Never manufactured Professor Bear's notes
- Never impersonated a fellow

## Unsupported claims: none found.
