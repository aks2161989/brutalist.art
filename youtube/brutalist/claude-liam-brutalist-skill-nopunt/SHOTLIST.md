# SHOTLIST.md — The nopunt Skill

| Beat | Pattern | Duration | Function |
|---|---|---|---|
| B00 | `ClaudeComposerAsk` | 14.57 s | COLD OPEN — Liam introduces the teardown; composer answers with three-line mental model. |
| B01 | `BrutalistHesitantWriter` | 20.37 s | BLUF — corrects "linter" misread → "catalog"; single-token trigger. |
| B02 | `SkillTeardownAnatomy` | 33.26 s | FRAMEWORK — one file, five jobs; sibling skills reference it. |
| B03 | `SkillTeardownPipeline` | 39.85 s | FRAMEWORK — five gates, step zero is the library. |
| B04 | `SkillTeardownMechanism` | 27.95 s | MECHANISM 1 — HOLD vs PUNT; only photographs HOLD. |
| B05 | `SkillTeardownMechanism` | 36.44 s | MECHANISM 2 — the catalog; six families cover it. |
| B06 | `SkillTeardownMechanism` | 32.09 s | MECHANISM 3 — five punt costumes; same bug, different hats. |
| B07 | `SkillTeardownMechanism` | 33.17 s | MECHANISM 4 — SHOW / HOLD / CARD vocabulary. |
| B08 | `SkillTeardownMechanism` | 33.26 s | FALSIFIABILITY — a miss is a design card, never a slate. |
| B09 | `ClaudeVerdictArtifact` | 32.79 s | VERDICT — six-line artifact recap of the skill. |
| B10 | `ClaudeComposerAsk` | 38.34 s | YOUR TURN — paste-ready audit prompt with a scorable rubric. |
| B11 | `ClaudeTitleOutro` | 3.46 s | OUTRO — title restate + `@NikBearBrown` handle (OUTRO-LOCK). |

Total measured duration: **345.55 s** (5 min 45 s).

## Notes

- Cold open uses **ClaudeComposerAsk** per COLD-OPEN LAW. Answer lines are
  concrete (not "let's see what happens").
- Second beat (**BrutalistHesitantWriter**) is at least nine seconds long
  (20.37 s here). Trigger word is a single token (`linter`) with no trailing
  punctuation — per the trigger-syntax memory.
- Mechanism beats (B04-B08) use the same `SkillTeardownMechanism` component,
  with different eyebrow / heading / quote / cite / verdict props for each
  design decision. This is per the skill-teardown modifier in
  `skills/make/ai-explainer/SKILL.md`.
- Second-last beat (B10) is **ClaudeComposerAsk** with `greeting: "Your Turn"`
  per HANDOFF LAW. The command is paste-ready; the three output lines are the
  scorable checks.
- Outro (B11) uses `ClaudeTitleOutro` — the shipped component hardcodes
  `@NikBearBrown` per `OUTRO-LOCK.md`. Composer beats use
  `folderLabel: "@HumanitariansAI"` for the inner-composer folder chip.

## Beat-level `shot.show` timing

Each beat's `shot.show` array carries fractional cues (0.02, 0.15, 0.35 …)
indicating what appears at that fraction of the beat's duration, BEFORE
narration explains it. See `beat_sheet.json` for the full per-beat cue table.
