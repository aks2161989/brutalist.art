# FACTCHECK.md — The godot-gamedev Skill — Short
# Run ID: 91d8e873ca5e413e8379a0c0c9179ed4 · 2026-09-12
# Kept beats: B00 B01 B04 B05 B08 B09 B10 B11 B12

All factual claims are sourced from `skills/make/godot-gamedev/SKILL.md`.

## Claim verification

| Beat | Claim | Source |
|------|-------|--------|
| B00 | godot-gamedev does not write game code; it reads a game project | SKILL.md §Overview |
| B01 | godot-gamedev is a game reader, not a maker; produces a teaching film component-by-component | SKILL.md §Overview |
| B04 | Starts with project.godot (config, autoloads, input map, renderer settings); reads every runtime script; teaching unit = code excerpt + visible result | SKILL.md §Mechanism |
| B05 | Must label reconstructed editor views 'Godot editor reconstruction'; every node/property/texture must come from a file Claude read; code-result pairs logged as teaching-contract-v1 | SKILL.md §Design Tell |
| B08 | godot-walkthrough = player experience level-by-level; godot-gamedev = code mechanics component-by-component | SKILL.md §Falsifiability |
| B09 | Requires real Godot project with project.godot as input; --check flag available | SKILL.md §Inputs, §Self-demo |
| B10 | Mandates code-and-result pairs not deferred; evidence contract = reconstruct don't invent; reader not omniscient explainer; depth of film matches depth of game | SKILL.md §Verdict |
| B11 | Paste-ready prompt: read SKILL.md, provide game path, produce beat_sheet.json, standard mode, per-component questions | SKILL.md §Handoff |

## Updated claims (run_id d6a7b812 parent update)

- B04 updated: now explicitly states "teaching unit is a pair: code excerpt + visible result immediately after. A verbal description alone is not a result." — directly supported by SKILL.md §Mechanism.
- B05 updated: adds "Code-result pairs are logged in the evidence ledger as teaching-contract-v1" — supported by SKILL.md §Design Tell.
- B10 updated: now leads with "mandates code-and-result pairs — each excerpt immediately followed by game consequence, not deferred" — supported by SKILL.md §Verdict.

## Dropped beats

B02 (pipeline), B03 (anatomy), B06 (scene tree), B07 (walker flow) all dropped; no claims from those beats remain in this Short. B10's four verdict lines verified against SKILL.md.

## Claim status: all claims supported by SKILL.md. No unsupported claims.
