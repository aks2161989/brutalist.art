# SCRIPT.md — The godot-gamedev Skill
# Episode 13 · Brutalist playlist · @HumanitariansAI
# Persona: Liam (in for Bear) · Voice: Kokoro am_onyx
# Run ID: d6a7b8125f8a4bc4bbd1122f104532f0

---

## B00 — Cold Open (ClaudeComposerAsk) · ~14s

Bula — this is Liam, in for Bear. There is a Brutalist skill called godot-gamedev. Most fellows read that name and assume it writes Godot game code for you. It does not. So I asked Claude to read the full skill and explain what actually happens when you point it at a game.

**Visual**: Composer card, greeting "Bula, Liam". Ask types live. Three output lines land:
"It takes games apart." / "Not a builder — a reader." / "It makes teaching films from source."

---

## B01 — BLUF (BrutalistHesitantWriter) · ~12s ≥9s ✓

godot-gamedev is a Godot game-maker — not a builder, a teacher.

*(writer types "game-maker", hesitates, corrects to "game-reader", sentence resolves: "godot-gamedev is a Godot game-reader — not a builder, a teacher.")*

---

## B02 — Pipeline (SkillTeardownPipeline) · ~17s

The skill runs in four phases. First, you point it at a Godot 4 project and it reads every scene, script, and asset manifest. Second, Claude traces signals — what triggers what, what health or state each node tracks. Third, it builds a structured walk-through: a written guide that a new student could follow without running the game. Fourth, optionally, it hands that guide to the ai-explainer skill to produce a full teaching film. Each phase consumes the previous one's output — no phase is optional.

---

## B03 — Anatomy (SkillTeardownAnatomy) · ~18s

The skill lives in two files. SKILL.md is the full instruction set — it defines what Claude reads in the project, how to identify the player loop, and what the guide must cover. PROMPT.md is the agent primer — the specific system context and task framing passed at invocation. Supporting that, the skill references the Godot 4 project root: project.godot names the entry scene, the scenes folder holds the game tree, the scripts folder holds GDScript logic, and the assets folder names the visual and audio inventory. You do not need all of these to start — the skill documents which are required versus optional.

---

## B04 — Worked Example: Code Mode (GodotDevWorkbench) · ~18s

When the skill runs on a real game, Claude starts with project-dot-godot: config, autoloads, input map, renderer settings. Then it reads every runtime script. The teaching unit is a pair: one focused, readable excerpt — then immediately the visible result that excerpt produces in the game. A verbal description alone is not a result.

**Visual**: GodotDevWorkbench code mode. player.gd open with `_physics_process` highlighted. Output bar reads "player.gd · code → visible result · Godot editor reconstruction". Notes panel: "Visible result — Player moves at 200px/s horizontal; jump sets velocity.y=-400 when is_on_floor." Teaching illustration label present.

---

## B05 — Mechanism: Reconstruct (SkillTeardownMechanism) · ~21s

The core design principle of godot-gamedev is reconstruction, not generation. The skill's exact instruction is: "Reconstruct — don't invent." That means every claim in the guide must trace back to a specific node, script, or line in the actual project. If Claude cannot find evidence for a statement in the source, the skill requires it to omit the claim rather than synthesise one. Code-result pairs are logged in the evidence ledger as teaching-contract-v1. This is not a limitation — it is the specification. The guide is only as reliable as the code it reads.

---

## B06 — Worked Example: Tree Mode (GodotDevWorkbench) · ~20s

The scene tree pass maps the hierarchy. In this teaching illustration — world.tscn — the top node is World, a Node3D. Under it lives the Player, a CharacterBody3D that carries the controller script. Platforms and walls are StaticBody3D nodes under a Level group. A camera arm follows the player. A HUD is a CanvasLayer with score and health labels. Claude's job here is not to describe what each node does from general Godot knowledge — it reads the actual tree and reports what it finds. The guide names nodes verbatim and flags any orphan nodes the skill cannot explain from script evidence alone.

---

## B07 — WalkerGodotSetup: Flow (WalkerGodotSetup) · ~17s

The full skill flow runs in six stages. Point at the project root. The skill reads project.godot and identifies the main scene. Claude opens every scene file and every script, building a dependency graph. It then traces the player loop: spawn, input, physics, health, win and lose conditions. It assembles a written walk-through structured as: overview, player loop, scene inventory, signal map, open questions. Finally — optionally — it routes that document to ai-explainer or a companion skill to produce narrated film.

---

## B08 — WalkerGodotSetup: Comparison (WalkerGodotSetup) · ~17s

It helps to compare godot-gamedev to the godot-walkthrough skill. Both read Godot source. The difference is scope and audience. godot-walkthrough produces a player's guide — how to complete the game, where the secrets are. godot-gamedev produces a developer's guide — how the game works internally, what the code does and why. Fellows working with students who are learning to build games want godot-gamedev. Fellows creating content for players who just want to finish a level want godot-walkthrough.

---

## B09 — Limitation (SkillTeardownMechanism) · ~19s

The self-demo limitation is real and worth naming. To run godot-gamedev, you need a Godot 4 project with a project.godot file at the root. This reel does not have one — so the command `art godot-gamedev --project ./my-game` cannot be demonstrated live here. What the skill produces is a structured markdown document and, optionally, a film. The quality of that output is bounded entirely by the quality of the source code. A game with no comments and ambiguous node names will produce a less useful guide than a well-structured one. That is documented behaviour, not a bug.

---

## B10 — Verdict (ClaudeVerdictArtifact) · ~18s

What the skill gets right: it mandates code-and-result pairs — each excerpt is immediately followed by the game consequence, not deferred to a summary. It makes the evidence contract explicit: reconstruct, don't invent. The limitation is clear: this is a reader, not an omniscient explainer. Give it a shallow game and the teaching film will be shallow too.

**Visual**: ClaudeVerdictArtifact card with four verdict lines:
1. "Code → visible result: each excerpt, then its game consequence — not deferred." (terracotta)
2. "Evidence contract: Reconstruct, don't invent."
3. "Limitation: reader, not omniscient explainer."
4. "Shallow game → shallow film."

---

## B11 — Your Turn (ClaudeComposerAsk) · ~33s

Your turn. Open Claude Code in your Brutalist project. Type this:

"Read skills/make/godot-gamedev/SKILL.md in full. Then apply it to the game project at ./my-game — produce a complete developer's walk-through in GAMEDEV-GUIDE.md covering the player loop, scene inventory, signal map, and at least two open questions the code raises but does not answer."

What you get: a markdown guide named GAMEDEV-GUIDE.md, structured by the skill's four phases, with all claims traceable to specific nodes or scripts. Test of success: open the guide, pick any claim, find its source in the game project. If you cannot, the skill has violated its own reconstruction rule and you should flag it in FEEDBACK.md.

---

## B12 — Outro (ClaudeTitleOutro) · ~7s

*(No narration. Title card: "The godot-gamedev Skill". Mascot. Handle: @NikBearBrown per OUTRO-LOCK.md.)*
