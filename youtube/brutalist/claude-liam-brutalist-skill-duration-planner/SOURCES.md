# Sources

## Primary source (the skill we're tearing down)

- `skills/make/duration-planner/SKILL.md` — SOURCE-SNAPSHOT SHA-256
  `07dc8136f0ea345b4c4e39bb86ba68d0f4112efbac559a87919b7179228ff1a5`.
  Supervisor `episode.source_sha256`: `3a51e3741b189e85c786cf21c7dfd68eec7cd545d992bd319b650b89a620cd92`.
  Verbatim quotes shown on-screen in B04 (thesis), B05 (floor), B06 (audio-first sync),
  B07 (padding rule). Every quote appears exactly as written in the SKILL.md.

## Related toolkit doctrine (context, not on-screen)

- `skills/make/ai-explainer/SKILL.md` — parent skill (cold open + hesitant writer
  + verdict + your-turn + outro structure; skill-teardown modifier auto-arms
  because the source is a SKILL.md).
- `skills/make/nopunt/SKILL.md` — SHOW/HOLD/CARD classification and teaching-arc
  checklist.
- `runtime/prose/teardown/PROSE.md` — Teardown register (Feynman × MKBHD).
- `CLAUDE-BRAND.md` — palette + typography lock.
- `OUTRO-LOCK.md` — @NikBearBrown handle is hardcoded in `ClaudeTitleOutro`
  regardless of channel; @HumanitariansAI appears as the folder chip in the
  composer beats only.
- `docs/PIPELINE-SAFETY.md` — audio-first policy, pending approvals policy.
- `CLAUDE-CODE-VISUAL-QC-CHECK.md` — the 9-point rubric applied in QC.

## Read-only example leads (NOT reused as this run's outputs)

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — Your Weekly Video,
  Handled. Adaptation: this reel's spine follows the same skill-teardown act
  structure (framework → mechanism → falsifiability → verdict → handoff)
  established by the exemplar reels. No prose reused; no signature attributed.
- `mohammed-h/Bond-Pricing/beat_sheet.json` — Bond Pricing and Duration.
  Adaptation: the *word* "duration" is coincidence — bond duration is a
  financial concept, unrelated to video pacing duration. Not used for content.

## Facts corrected vs. source

None. The SKILL.md is treated as authoritative — the reel *quotes and judges*
it in the Teardown register. Where the SKILL.md itself hedges (e.g. the
6-minute engagement rule "doesn't replicate in enrolled courses"), the reel
carries the hedge, not a stronger claim.

## Corrections applied to stale toolkit guidance

- The SKILL.md says the storyboard file is `whiteboard/reference/storyboard.md`
  and the pace check script is `scripts/pace_check.py`. These are described
  accurately as **skill-internal doctrine** in the reel; we did not run
  `pace_check.py` in this build (that would be circular — the skill checks
  someone else's reel, not its own teardown). The B03 pipeline diagram shows
  the flow the skill implements; it is not a screenshot of pace_check.py output.

## Registered scene sources (rendered natively — no external assets)

- `runtime/remotion/src/scenes/ClaudeComposerAsk.tsx` (B00, B09)
- `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx` (B01)
- `runtime/remotion/src/scenes/SkillTeardownAnatomy.tsx` (B02)
- `runtime/remotion/src/scenes/SkillTeardownPipeline.tsx` (B03)
- `runtime/remotion/src/scenes/SkillTeardownMechanism.tsx` (B04, B05, B06, B07)
- `runtime/remotion/src/scenes/ClaudeVerdictArtifact.tsx` (B08)
- `runtime/remotion/src/scenes/ClaudeTitleOutro.tsx` (B10)

For the portrait companion, the same three SkillTeardown components render at
1080×1920 via native 916 compositions added to Root.tsx (`SkillTeardownAnatomy916`,
`SkillTeardownPipeline916`, `SkillTeardownMechanism916`). Same components, same
schemas — the components use `useVideoConfig()` for all layout math.

## Public repository (viewer-facing setup)

- https://github.com/nikbearbrown/brutalist.art — the public DOT toolkit fellows
  clone. Not shown as a card in this reel (the reel is a teardown, not a setup
  tutorial), but appears in metadata.links for the build record.
