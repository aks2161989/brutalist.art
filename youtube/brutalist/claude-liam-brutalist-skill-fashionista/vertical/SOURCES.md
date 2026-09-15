# Sources

## Primary source (this is what the reel tears down)

- `skills/make/fashionista/SKILL.md`
  - SHA-256 (SOURCE-SNAPSHOT.json, captured 2026-09-08T13:52:38): `22614f443c156cf903878e5ff0781ba1d8b34170e0622bfee962b58f7d7bf12b`
  - Supervisor's authoritative `episode.source_sha256`: `1b129e85f0768d7b29b971f2bbecb6823f9f5f467034fd4964b4de74f3e6eb30`
  - Both values recorded verbatim from the isolated toolkit snapshot and this
    invocation's payload. Any quote shown on screen is copied from the local
    isolated-toolkit file.

## Doctrine consulted (for the skill-teardown modifier)

- `skills/make/ai-explainer/SKILL.md` — the parent chassis + skill-teardown
  modifier. Governs the bookend structure (`ClaudeComposerAsk` → hesitant
  writer → body → verdict card → HANDOFF → title-restate outro).
- `skills/make/nopunt/SKILL.md` — the PROOF GATE classification.
- `runtime/prose/teardown/PROSE.md` — the Teardown register.
- `docs/PIPELINE-SAFETY.md` — the "no publishing, no paid calls" guarantee.
- `docs/FELLOWS-SUBMISSION.md` — the 4-file weekly deliverable contract.
- `CLAUDE-BRAND.md`, `OUTRO-LOCK.md`, `CLAUDE-CODE-VISUAL-QC-CHECK.md` — brand
  and QC rules.

## Read-only example leads

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — "Your Weekly
  Video, Handled." Staging lead only; not republished.
- `yatra-r/2026-08-30-one-tool-a-week-brandy/beat_sheet.json` — "One Tool a
  Week." Staging lead only.

Neither example is a fashionista source and neither is presented as this run's
output. Credit is preserved via original repo-relative paths; SHA-256 values
copied from BRIEF.md.

## Registered scenes leaned on (from the isolated toolkit's `./art scenes`)

- Landscape (RENDERABLE at authoring time): `ClaudeComposerAsk`,
  `BrutalistHesitantWriter`, `SkillTeardownAnatomy`, `SkillTeardownPipeline`,
  `SkillTeardownMechanism`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`.
- Portrait (RENDERABLE at authoring time): `ClaudeComposerAsk916`,
  `BrutalistHesitantWriter916`, `ClaudeVerdictArtifact916`,
  `ClaudeTitleOutro916`.
- Portrait (PUNT → filled in the isolated toolkit for this run):
  `SkillTeardownAnatomy916`, `SkillTeardownPipeline916`,
  `SkillTeardownMechanism916`. See PROMPTS.md and
  `scene-source-manifest.json` for what was added and why.

## Gaps and availability log

- The isolated toolkit ships with `SkillTeardown*` for 16:9 only. To honour
  the "native portrait, not a crop" rule (RENDER-TARGETS.md §3), 9:16
  siblings were authored in this isolated toolkit only. Never touches the
  live library.
- The mandatory legacy `scripts/type_check.py` referenced by
  `ai-explainer/SKILL.md` "GATE T" is not present in this toolkit. TYPECHECK.md
  documents the gap and the visual review substituted.
- No `higgsfield` CLI, no fashion source video. The reel does not attempt to
  run a fashionista trial; it explains the skill. This is the documented
  feasibility fallback (SELF-DEMO LAW / ai-explainer SKILL.md §3).
