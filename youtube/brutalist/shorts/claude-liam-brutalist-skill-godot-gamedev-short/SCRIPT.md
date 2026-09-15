# SCRIPT.md — The godot-gamedev Skill — Short
# Derived from: claude-liam-brutalist-skill-godot-gamedev (vertical)
# Run ID: 91d8e873ca5e413e8379a0c0c9179ed4 · 2026-09-12
# Kept beats: B00 B01 B04 B05 B08 B09 B10 B11 B12 (159.625s)
# Dropped: B02 (pipeline), B03 (anatomy), B06 (scene tree), B07 (walker flow)

---

**B00 — ASK / COLD OPEN** · 14.0s · ClaudeComposerAsk916

Bula — this is Liam, in for Bear. There is a Brutalist skill called godot-gamedev. Most fellows read that name and assume it writes Godot game code for you. It does not. So I asked Claude to read the full skill and explain what actually happens when you point it at a game.

---

**B01 — BLUF** · 12.3s · BrutalistHesitantWriter916

The name fools you. godot-gamedev is a game reader, not a maker. It takes a Godot project you already built and produces a teaching film that explains how it works — component by component, traced from actual source.

---

**B04 — MECHANISM** · 18.3s · GodotDevWorkbench916 (code mode)

When the skill runs on a real game, Claude starts with project-dot-godot: config, autoloads, input map, renderer settings. Then it reads every runtime script. The teaching unit is a pair: one focused, readable excerpt — then immediately the visible result that excerpt produces in the game. A verbal description alone is not a result.

---

**B05 — MECHANISM** · 21.0s · SkillTeardownMechanism916

The design tell is explicit in the skill file: label reconstructed editor views as Godot editor reconstruction, and supply source path and line numbers. The skill cannot draw a plausible-looking scene tree and call it the game. Every node, property, and texture path must come from a file Claude actually read. Code-result pairs are logged in the evidence ledger as teaching-contract-v1.

---

**B08 — FALSIFIABILITY** · 17.1s · WalkerGodotSetup916 (comparison mode)

godot-gamedev is one of two Godot skills in this toolkit. The other is godot-walkthrough. The distinction is the question asked. Walkthrough asks: how does the player experience the game — level by level. gamedev asks: how does the code make that experience — component by component. Same project, two films, different lens.

---

**B09 — LIMITATION** · 18.6s · SkillTeardownMechanism916

The self-demo gate is honest about its limit. To actually run godot-gamedev, you need a real Godot game with a project-dot-godot file. The skill runs a coverage check first — art godot-gamedev dash-dash-check. This reel shows the mechanism and the output scenes; a full end-to-end build requires bringing a game project as input.

---

**B10 — VERDICT** · 18.25s · ClaudeVerdictArtifact916

What the skill gets right: it mandates code-and-result pairs — each excerpt is immediately followed by the game consequence, not deferred to a summary. It makes the evidence contract explicit: reconstruct, don't invent. The limitation is clear: this is a reader, not an omniscient explainer. Give it a shallow game and the teaching film will be shallow too.

---

**B11 — HANDOFF** · 33.0s · ClaudeComposerAsk916 ("Your turn.")

Your turn. Here is the paste-ready prompt. 'Read skills-slash-make-slash-godot-gamedev-slash-SKILL-dot-M-D in full. I have a Godot 4 project at [path]. Produce a complete beat sheet for a godot-gamedev teaching film, standard mode. For each major component, name where it lives in the project, what data enters it, what it changes, and what the player sees.' Replace [path] with any Godot 4 project folder you have. When Claude comes back, check the component inventory against what you know about the game. If it misses a system, ask it to read that specific file and trace the dependency. The check is the work. Liam, in for Bear.

---

**B12 — OUTRO** · 7.0s · ClaudeTitleOutro916 · audio_policy: silence

Liam, in for Bear.

---

## Dropped beats (in long film only)

- **B02** (PIPELINE): four-phase walkthrough — covered at summary level by B01
- **B03** (ANATOMY): two-mode file anatomy — detail for the 16:9 long
- **B06** (MECHANISM/scene tree): world.tscn scene tree deep-dive — detail for the 16:9 long
- **B07** (MECHANISM/walker flow): 6-stage walker-mode flow — detail for the 16:9 long
