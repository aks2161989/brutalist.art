# SOURCES — The logo Skill

## Primary — the skill under teardown

- `skills/make/logo/SKILL.md` — the doctrine, laws, brand table, pool spec.
  Isolated-toolkit copy SHA-256: `badfb2bc1b6598049174fd79c57b41ee30d177d9c89b20d38b93574ad5547a6d`.
- `skills/make/logo/scripts/logo.py` — the scaffolder.
  SHA-256: `1a8376bd1d1702d3dc13bf5e619eae5b5ffc3969309710184b15c85c16c73b5e`.
- `runtime/remotion/src/scenes/LogoOutro.tsx` — the 8-technique scene.
  SHA-256: `7e2675615c99ce46f0a2bf22fb50b643131f2cfb9c3bb9a30ff2f2666306809c`.
- `OUTRO-LOCK.md` — the counterexample referenced in B08.
  SHA-256: `a642621c1073604ff350381f58e2fbfa7dee1c0f586d8a285c44ed2c4ab51e01`.

## Brand pool disk evidence (used in B02 anatomy + B06 curation)

- `logos/bear-brown/` — 2 svgs, 6 mp3s (confirmed by `ls logos/bear-brown/*.svg | wc -l`).
- `logos/humanitarians/` — 1 svg, 9 mp3s.
- `logos/medhavy/` — 42 visible svgs, 12 in `_rejected/`, 2 mp3s.
- `logos/musinique/` — 2 svgs, 5 mp3s.

## Chassis + register laws referenced but not the primary subject

- `skills/make/ai-explainer/SKILL.md` — visual treatment, cold-open law, BLUF
  law, illustrate law, spark-line law, handoff law, outro law.
- `skills/make/nopunt/SKILL.md` — SHOW/HOLD/CARD classification, teaching-arc
  checklist.
- `runtime/prose/teardown/PROSE.md` — the Teardown register.
- `CLAUDE-BRAND.md` — cream + terracotta + EB Garamond palette.
- `CLAUDE-CODE-VISUAL-QC-CHECK.md` — the 9-point rubric applied at frame
  inspection.
- `docs/PIPELINE-SAFETY.md`, `docs/FELLOWS-SUBMISSION.md`.

## Read-only example leads (per BRIEF.md)

Two example beat sheets were consulted for staging patterns; no content copied:

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` (SHA-256
  `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`) — used
  as a reference for Claude-liam handoff prompt shape only.
- `sainikhil-madison/2026-09-04-the-cast-that-hid-the-bug/beat_sheet.json`
  (SHA-256 `15674c254cc0a11282c17826ac0db1db6adfe22e895a7e2fc8a21701c7b5b783`)
  — has a real `LogoOutro` beat (humanitarians, `springEntrance`,
  `humanitarians-logo-1.svg`) that confirms the LogoOutro props shape used by
  live reels.

Neither example was published, quoted, or reused as output.

## Portrait scene wrappers — credit + provenance

The three `SkillTeardown*916.tsx` portrait wrappers used by the vertical
companion (`vertical/beat_sheet.json`) are byte-identical copies of the
wrappers produced for the guests episode:
- source: `youtube/brutalist/claude-liam-brutalist-skill-hai/scene-source/runtime/remotion/src/scenes/SkillTeardown{Anatomy,Pipeline,Mechanism}916.tsx`
- copied into: `<toolkit>/runtime/remotion/src/scenes/` and registered in
  the isolated `Root.tsx`.

The `BrutalistHesitantWriter` portrait-scale patch (per
`feedback_hesitant_writer_portrait_scale`) was applied to the isolated
toolkit's copy only.

## Environment / runtime references

- Kokoro model + voices: `runtime/models/kokoro/`.
- Chrome for Remotion: `chrome-headless-shell` at
  `/Users/bear/node_modules/.remotion/chrome-headless-shell/mac-arm64/…`.
- Node 25.9.0; ffmpeg + ffprobe from Homebrew.

## Public toolkit repository

- https://github.com/nikbearbrown/brutalist.art — the DOT repo where this
  skill lives. All setup/install instructions in the reel point there
  (`skills/make/logo/`).

Nothing outside these paths shaped the reel. No API-key calls, no external
downloads, no paid services.
