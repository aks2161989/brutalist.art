# The godot-gamedev Skill — episode 13

Two native 4K files ready for Bear's viewing/editing pass. **Not published.**

| Aspect | File | Duration | Dimensions | SHA-256 |
|---|---|---|---|---|
| Landscape 16:9 | [`exports/landscape/claude-liam-brutalist-skill-godot-gamedev.mp4`](exports/landscape/claude-liam-brutalist-skill-godot-gamedev.mp4) | 231.8 s | 3840 × 2160 | `da36f3e53e00d7599708d5ff36adecc03aa89c6501f51f8877de41aae9a9ddd0` |
| Vertical 9:16 | [`exports/vertical/claude-liam-brutalist-skill-godot-gamedev-vertical.mp4`](exports/vertical/claude-liam-brutalist-skill-godot-gamedev-vertical.mp4) | 231.8 s | 2160 × 3840 | `3c4c7be38b1c1534736e254ca9614040d2a434bf5edfc53e83d6cc37b7167483` |

> **Rebuilt in run\_id d6a7b8125f8a4bc4bbd1122f104532f0** — SKILL.md updated with "Code → visible result is the teaching unit" section and `teaching_contract: code-then-result-v1` evidence requirement. B04/B05/B10 audio, scene renders, and both exports rebuilt. Duration increased by ~6.5s due to new narration in those beats.

Both files share the same 13-beat spine:

- **B00** cold-open Claude composer — `Bula, Liam` greeting, ask about the godot-gamedev skill.
- **B01** BLUF hesitant writer — corrects in view; introduces the skill's mechanism ("source reader").
- **B02** SkillTeardownPipeline — 5-stage pipeline: READ → PLAN → WALK → FILM → QC.
- **B03** SkillTeardownAnatomy — 7-section SKILL.md anatomy: Intent, Inputs, Mechanism, GDD, Film, Walker, QC.
- **B04** GodotDevWorkbench (beat 1) — player.gd code excerpt + "code → visible result" pairing principle introduced.
- **B05** SkillTeardownMechanism — evidence contract: "Reconstruct, don't invent." + `teaching_contract: code-then-result-v1` reference.
- **B06** GodotDevWorkbench (beat 2) — scene node structure illustration.
- **B07** WalkerGodotSetup — Walker mode GDD bookend: how Walker adds the game-design context.
- **B08** WalkerGodotSetup — real project.godot requirement; shallow game → shallow teaching film.
- **B09** SkillTeardownMechanism — limitation card: "reader, not omniscient explainer."
- **B10** ClaudeVerdictArtifact — four verdict lines, evidence-contract recap.
- **B11** ClaudeComposerAsk — handoff composer with full skill recap prompt for the fellow.
- **B12** ClaudeTitleOutro — title restate + `@NikBearBrown` handle per OUTRO-LOCK.

## Watch & edit next

1. `exports/landscape/claude-liam-brutalist-skill-godot-gamedev.mp4` (~13 MB · 4K H.264 + AAC)
2. `exports/vertical/claude-liam-brutalist-skill-godot-gamedev-vertical.mp4` (~12 MB · 4K H.264 + AAC)
3. QC evidence: `_qc/frames/*.png` (13 stills) + `_qc/contact_sheet.png` (26-frame sheet).
4. `VISUAL-REVIEW.json` and `vertical/VISUAL-REVIEW.json` record what was reviewed.

## Self-demo limitation — documented

The godot-gamedev skill requires a **real Godot 4 game project** with a `project.godot` file.
This reel demonstrates the mechanism and output using teaching illustrations clearly labeled as
such. The limitation is made explicit in B08 (Walker mode beat: "shallow game → shallow film")
and B09 (limitation card: "reader, not omniscient explainer"). All mechanism quotes are verbatim
from `skills/make/godot-gamedev/SKILL.md`. No invented output.

## Playlist adaptation for @HumanitariansAI — one open flag for Bear

Every Claude composer beat (B00, B11) carries the `@HumanitariansAI` folder chip.
The outro card (B12) is the locked `ClaudeTitleOutro` with `@NikBearBrown` hardcoded
per `OUTRO-LOCK.md`. Compile emitted a `SKIN LINT` warning on both aspects — expected
behavior, recorded in each aspect's `CHECKS-REPORT.md`. If Bear wants the outro to read
`@HumanitariansAI`, that requires a `OUTRO-LOCK.md` policy change, not a per-reel edit.

## Portrait B10 repair note

The initial vertical B10 render had 6 artifact lines, making the card height (~2067px)
exceed the 1920px portrait canvas, causing a top-edge-bleed BLOCKER. Fixed by:
- Reverting `artifactLines` to the 4 landscape lines.
- Widening `ClaudeVerdictArtifact916` card to `CARD_W = width * 0.90` (~63% ink coverage).
- Gate V re-ran: 0 blockers, 0 majors.

## What happens next

Bear watches both files, records notes in `FEEDBACK.md`, and either signs off or requests
targeted per-beat rebuilds. Nothing here is published; nothing is uploaded; no external
API was called during this build.

## Artifact tree

```
claude-liam-brutalist-skill-godot-gamedev/
├── beat_sheet.json                    landscape source (SHA-256 a1f17bda…)
├── vertical/
│   ├── beat_sheet.json                portrait source (SHA-256 e49b59cb…)
│   ├── VISUAL-REVIEW.json             AI frame review for portrait
│   ├── CHECKS-REPORT.md               portrait checks
│   ├── TYPECHECK.md                   portrait typography
│   ├── FACTCHECK.md                   portrait factcheck (refs landscape)
│   ├── SHOTLIST.md                    portrait scene-swap table
│   └── media/, _qc/                   portrait renders + QC
├── exports/
│   ├── landscape/                     4K landscape master + verified.json
│   └── vertical/                      4K portrait master + verified.json
├── media/, mp3/                       landscape renders
├── _qc/                               landscape QC frames + contact sheet + report
├── BRIEF.md                           supervisor brief
├── SCRIPT.md                          narration script
├── SOURCES.md                         source file list
├── SOURCE-SNAPSHOT.json               source hashes at build time
├── FACTCHECK.md                       landscape claim verification
├── SHOTLIST.md                        landscape beat table
├── PROMPTS.md                         visible prompts documented
├── FEEDBACK.md                        Bear's edit notes (pending)
├── CHECKS-REPORT.md                   landscape checks
├── TYPECHECK.md                       landscape typography
├── VISUAL-REVIEW.json                 AI frame review for landscape
├── BUILD-PROMPT.md                    the build prompt used
└── README.md                          this file
```

## Human review pending

The films have been generated, gate-checked, and inspected frame-by-frame by an AI
reviewer. Bear is the human reviewer. Human sign-off is required before any publication.
