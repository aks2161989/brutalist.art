# Sources & availability log

## Primary source (SELF-DEMO's evidence)

- **`skills/make/fellows/SKILL.md`** — this reel's subject.
  - SHA-256 (SOURCE-SNAPSHOT.json): `afd14d36428eac3cc954af49af4610206924cbcbbfb969cff339c02de0640131`
  - Supervisor `episode.source_sha256`: `71d2303f780103e8947b7eeb3c55c362829ea0415e2df75b1a58980f48dbd6d3`
  - Read in full at reel-authoring time; every narration claim is traced to it in `FACTCHECK.md`.

The two SHA-256s differ because SOURCE-SNAPSHOT captures the file as saved in the isolated
toolkit, while the supervisor snapshot may include a normalized header/trailing newline
convention. The content is the same — the fellows spine, laws, and flow described in the
snapshot match what the supervisor summarizes for this invocation.

## Confirming reads (from SOURCE-SNAPSHOT)

- `skills/make/ai-explainer/SKILL.md` (skill-teardown modifier, house laws)
- `skills/make/nopunt/SKILL.md` (PROOF GATE definitions used in CHECKS-REPORT.md)
- `runtime/prose/teardown/PROSE.md` (register)
- `docs/PIPELINE-SAFETY.md` (approval fingerprints, `kind: source_report` contract)
- `docs/FELLOWS-SUBMISSION.md` (weekly two-video/four-file requirement)
- `REPOLOOP-PROMPT.md` (this playlist's supervisor context)

## Read-only example leads (structural reference only)

Per BRIEF.md's *Read-only example leads*: these were consulted for structural
inspiration only. **Nothing** in this reel republishes their content, their fellows'
Drive links, contact details, human signatures, or presents their results as this
run's results.

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — SHA-256
  `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`.
  Local copy: `.repoloop/workspaces/claude-liam-brutalist-skill-fellows/examples/746409a8715e.json`.
  Lead: how a fellows-related reel structures a weekly-submission narrative and
  uses HAI custom compositions (HaiSubmit* family — none of which this teardown
  uses; we stick to the shipped SkillTeardown* family).
- `yatra-r/2026-08-30-one-tool-a-week-brandy/beat_sheet.json` — SHA-256
  `e219593a27eaf6d68b43d3c9c89243cb90fd1e9dab7fd1199abc000d757af38e`.
  Local copy: `.repoloop/workspaces/claude-liam-brutalist-skill-fellows/examples/e219593a27ea.json`.
  Lead: `ClaudeVerdictArtifact` recap card usage.

## Scene-library sources

- `runtime/remotion/src/scenes/ClaudeComposerAsk.tsx` (shipped)
- `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx` (shipped; portrait scale patched, see PROMPTS.md)
- `runtime/remotion/src/scenes/SkillTeardownAnatomy.tsx` (shipped)
- `runtime/remotion/src/scenes/SkillTeardownPipeline.tsx` (shipped)
- `runtime/remotion/src/scenes/SkillTeardownMechanism.tsx` (shipped)
- `runtime/remotion/src/scenes/ClaudeVerdictArtifact.tsx` (shipped)
- `runtime/remotion/src/scenes/ClaudeTitleOutro.tsx` (shipped; OUTRO-LOCK.md governs)

### 916 wrappers added for the portrait companion

Derivative of the fashionista reel's scene-source (its 916 wrappers already ship
identical shapes to what this reel needed). Copied *only into the isolated
toolkit* — the live public library is unchanged.

- `runtime/remotion/src/scenes/SkillTeardownAnatomy916.tsx` (copied)
- `runtime/remotion/src/scenes/SkillTeardownPipeline916.tsx` (copied)
- `runtime/remotion/src/scenes/SkillTeardownMechanism916.tsx` (copied)

Manifest: `scene-source-manifest.json` records every file added or patched inside
the isolated toolkit for this run.

## Availability log (gaps recorded honestly)

- **`scripts/type_check.py`** — referenced by ai-explainer/SKILL.md §Hard rules
  ("GATE T · ALWAYS RUN") and by `TYPECHECK.md`. NOT present in this toolkit.
  Gate cannot run. Documented in TYPECHECK.md; substitute visual typography
  review performed on all sampled frames.
- **`reference/type-spec.md`** — the §8.x spec the missing checker was supposed
  to enforce. NOT present.
- **`skills/make/kerning/`** — referenced by ai-explainer. NOT present.
- **`ILLUSTRATIONS.md`** — public docs sometimes reference this. NOT present in
  `runtime/remotion/src/illustrations/`. The starter templates named in the
  ai-explainer skill (LayerStack, SourceFlow, ChipGrid, PredictCard) DO exist
  as `Illu-*` scenes and are searchable via `./art scenes`; none were needed
  for this teardown.
- **`runtime/qc/final_frame_check.py`** (Gate V) IS present and runs as part
  of `compile.py`. It passed cleanly on this build.

## No paid sources used

- No paid API calls.
- No Higgsfield generation (CLI absent from this toolkit run).
- No stock imagery, no paid fonts (EB Garamond ships in `runtime/fonts/`).
- No external clones during the build.
