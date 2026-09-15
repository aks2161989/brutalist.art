# SOURCES.md — The hai Skill (Short)

Episode: `claude-liam-brutalist-skill-hai-short` (derived from
`claude-liam-brutalist-skill-hai-vertical`).
Run id: `6b0a5edfa1ee4bd882707ab0e486cdb5`
Supervisor source SHA-256: `81e4ae65bd6363f318dd85d1564dd289c032a8fc988329ded807a8e872e7e12e`
Parent master SHA-256: `7a92bdb465492063ced20ba2a4091ad7ce5b0de20f144a187ab3cbc9d8527a31`

## What this Short is

A whole-beat cut of the parent 9:16 vertical. 8 of the parent's 12 beats
were retained unchanged. No narration rewrite. No re-render. No new visual
authoring. Every kept `mp3/beat-*.mp3` and `media/*.mp4` was copied from
the parent's `vertical/` as an independent file (not symlinked).

## Sources inherited from the parent teardown

The parent's `SOURCES.md` at
`youtube/brutalist/claude-liam-brutalist-skill-hai/vertical/SOURCES.md`
records the full lineage (SKILL.md, brand_variant.py, brands/hai.md, the
teardown/plain prose registers, and demo fixtures). Every claim retained in
this Short is line-cited in `FACTCHECK.md` against that same evidence.

## Scene-source lineage (portrait wrappers)

The parent reel authored (or copied from the `guests` teardown) these
portrait wrappers:

- `SkillTeardownAnatomy916.tsx` — not used by this Short (B02 dropped).
- `SkillTeardownPipeline916.tsx` — B03.
- `SkillTeardownMechanism916.tsx` — B04, B05, B08.
- `BrutalistHesitantWriter.tsx` (portrait-aware scale patch) — B01.
- `ClaudeComposerAsk916`, `ClaudeVerdictArtifact916`, `ClaudeTitleOutro916`
  — B00, B09, B11 (already in the isolated toolkit's Root.tsx).

Because this Short reuses the parent's already-rendered 2160×3840 media
verbatim, no Remotion re-render was required for any kept beat.

## Cut decisions

See `CUT-PLAN.json`. Kept beats: B00, B01, B03, B04, B05, B08, B09, B11
(166.4 s). Dropped beats: B02 (Anatomy), B06 (CLI-exercise deep dive), B07
(Batch mode), B10 (long Your-Turn CTA).

## What we did NOT do

- We did not modify the parent reel or its exports.
- We did not regenerate any audio (`--no-outro-rewrite` was set).
- We did not overlay the parent's `scene-source` into the toolkit's Root.tsx
  — every kept beat already had a native 9:16 render in the parent's
  `vertical/media/`, so no re-render path was exercised.
- We did not publish, upload, or push to Git.
- We did not run `hai` against a real HAI reel; the falsifiability finding
  is a code-reading result, not a shipped HAI cut.
