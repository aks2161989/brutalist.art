# SOURCES — The duration-planner Skill · Short (9:16)

Whole-beat derivative of `claude-liam-brutalist-skill-duration-planner/vertical/`.
The parent's `SOURCES.md` is inherited unchanged; this file records the delta
between the parent and the Short.

## Parent film

- `youtube/brutalist/claude-liam-brutalist-skill-duration-planner/vertical/`
  — 11-beat native 9:16 companion, 214.1 s.
  - Parent master path: `youtube/brutalist/claude-liam-brutalist-skill-duration-planner/exports/vertical/claude-liam-brutalist-skill-duration-planner-vertical.mp4`
  - Parent master SHA-256: `82e1bd11b25b1243becdf762631892904c774deb296f6b5c47db59b6aafca39c` (matches supervisor `episode.parent_master_sha256`).

## Retained beats (source: parent-vertical, byte-identical reuse)

| Beat | `mp3/beat-<bid>.mp3` | `media/<bid>.mp4` |
|---|---|---|
| B00 | copied from parent | copied from parent (2160×3840) |
| B01 | copied from parent | copied from parent (2160×3840) |
| B04 | copied from parent | copied from parent (2160×3840) |
| B05 | copied from parent | copied from parent (2160×3840) |
| B07 | copied from parent | copied from parent (2160×3840) |
| B08 | copied from parent | copied from parent (2160×3840) |
| B10 | copied from parent | copied from parent (2160×3840) |

No Kokoro regeneration, no Remotion re-render, no ffmpeg re-encode of the
source audio, no crop.

## Beats dropped from the parent (present in parent 9:16, absent here)

- B02 (SkillTeardownAnatomy916 — folder tree)
- B03 (SkillTeardownPipeline916 — five-phase pipeline diagram)
- B06 (SkillTeardownMechanism916 — HOLD_FLOOR / assemble.py sync)
- B09 (ClaudeComposerAsk916 — Your Turn extended composer)

Rationale in `CUT-PLAN.json` and `FACTCHECK.md § Delta from parent`.

## Primary skill source (inherited)

- `skills/make/duration-planner/SKILL.md` — SOURCE-SNAPSHOT SHA-256
  `07dc8136f0ea345b4c4e39bb86ba68d0f4112efbac559a87919b7179228ff1a5`
  (parent's snapshot; unchanged for this Short — the Short is a cut, not a
  re-write).
  Supervisor `episode.source_sha256`: `070aeda8cb13ae68370dec38ebb9bd008db71cb25644d14b62320eb49f5ae02c`
  (the concatenated SHA over supervisor-listed brief sources for this Short).

## Related toolkit doctrine (inherited context)

- `skills/make/ai-explainer/SKILL.md` — parent skill.
- `skills/make/explainer/SKILL.md` — grandparent Vox skill.
- `skills/make/nopunt/SKILL.md` — SHOW/HOLD/CARD classification.
- `REPOLOOP-SHORTS-PROMPT.md` — the cut-first Shorts contract this build follows.
- `OUTRO-LOCK.md` — hardcoded `@NikBearBrown` handle.
- `docs/PIPELINE-SAFETY.md` — audio-first and pending-approvals policy.
- `CLAUDE-CODE-VISUAL-QC-CHECK.md` — 9-point rubric applied in QC.

## Read-only example leads (BRIEF.md)

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — Your Weekly
  Video, Handled. Structure-level lead only; no prose reused; no signature
  attributed.
- `sanjana-rao/08-24-2026-playlist-architecture-as-product-strategy/playlist-architecture-short/beat_sheet.json`
  — Playlist Architecture — Short. Structure-level lead only; no prose reused;
  no signature attributed.

## Public repository (viewer-facing setup, not on-screen)

- https://github.com/nikbearbrown/brutalist.art — public toolkit. Appears in
  the beat_sheet `metadata.links` but is not shown as a card in this Short.

## No fabricated approvals

`approvals: {}` in this Short's beat_sheet metadata. Inherited unchanged from
the parent vertical, which was `{}` at capture. Human review is pending.
