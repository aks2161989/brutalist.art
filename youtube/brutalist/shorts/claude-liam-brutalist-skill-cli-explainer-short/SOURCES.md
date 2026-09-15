# SOURCES — Short cut (9:16)

This Short is a whole-beat cut of the parent vertical companion at
`youtube/brutalist/claude-liam-brutalist-skill-cli-explainer/vertical/`. No
new source material was authored; retained narration and native portrait
media are byte-for-byte copies of the parent vertical's assets.

## Parent artefacts

| Artefact | SHA-256 |
|---|---|
| Parent landscape master (16:9) — NOT read or written from this build | `youtube/brutalist/claude-liam-brutalist-skill-cli-explainer/exports/landscape/*.mp4` |
| Parent vertical companion `beat_sheet.json` | `8aa8a84e9d383592d1da9e31deabf17eb50e21e0b025a1c2f5bd99eec4bb3ba5` |
| Parent vertical companion master (`.../vertical/exports/vertical/claude-liam-brutalist-skill-cli-explainer-vertical.mp4`) | `13cdc99770348dd77eac9ab6870d2d1cdd37cb80bbcfb04d9771cc6dcd74bfaa` — matches THIS INVOCATION's `parent_master_sha256`. |

## Primary skill source (unchanged from parent SOURCES.md)

| Repo-relative path | SHA-256 (from parent SOURCE-SNAPSHOT.json) |
|---|---|
| `skills/make/cli-explainer/SKILL.md` | `16104901b8037bcf936ea12069bfa40a1495b9bbf2cd439d94254fa40da7071b` |

Episode-level bundle hash (THIS INVOCATION `source_sha256`):
`fbe8d97d4d77daa4f09a40575e3dc48b9b5e615677161869c074c29152df11c5`.
Feedback hash (THIS INVOCATION `feedback_sha256`):
`6b7b9c7454a60f145d6970b622d74842a5f8184647f32e564038495c22ecd0f5`.

## Isolated-toolkit modifications carried into the Short

Same three isolated-toolkit adaptations documented in the parent's
SOURCES.md — reused unchanged by the Short:

1. `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx` portrait-aware
   scale factor (memory: `hesitant-writer-portrait-scale`).
2. `runtime/remotion/src/scenes/ClaudeTitleOutro.tsx` + `ClaudeTitleOutro916.tsx`
   `handle` prop (default `@NikBearBrown`; overridden to `@HumanitariansAI`
   by this playlist's beat sheet). OUTRO-LOCK adaptation documented in
   parent SOURCES.md.
3. `runtime/remotion/src/Root.tsx` native portrait registrations for
   `ClaudeCodeBeat916`, `SkillTeardownAnatomy916`, `SkillTeardownPipeline916`,
   `SkillTeardownMechanism916` (only the first three are actually used by
   the retained beats: `SkillTeardownAnatomy916` in B02,
   `SkillTeardownPipeline916` in B03; the others were on the dropped B05,
   B06, B08, B09 beats).

## Read but not modified by this Short build

- `BRIEF.md`, `FEEDBACK.md`, `BUILD-PROMPT.md` (this workspace) — read.
- Parent vertical `beat_sheet.json`, `SOURCES.md`, `CHECKS-REPORT.md`,
  `SHOTLIST.md`, `PROMPTS.md`, `FACTCHECK.md`, `SOURCE-SNAPSHOT.json` — read.
- Parent vertical `media/B00.mp4 … B12.mp4` and `mp3/beat-B00.mp3 …
  beat-B12.mp3` — read (probed for dimensions/duration), then only the
  retained beats' files were copied independently into this Short workspace.
- Toolkit `CLAUDE.md`, `skills/make/ai-explainer/SKILL.md`,
  `skills/make/cli-explainer/SKILL.md`, `runtime/scripts/shorts.py`,
  `runtime/scripts/compile.py`, `runtime/scripts/build_safety.py` — read.

## Never written by this Short build

- Parent landscape master, its landscape beat sheet, or any file under
  the parent's `exports/landscape/` — the 16:9 film is protected.
- Parent vertical companion — the full-length native portrait companion at
  `parent/vertical/` was read-only; the SHA-256 above matches the invocation.
- Read-only fellows/example JSONs in the workspace's `examples/` folder.
- Public toolkit outside the isolated `.repoloop/…/toolkit/` copy.
- Any `.git`, credential, or `.env` file.
- Any external service or paid API — no upload, no publish.

## Availability log — gaps recorded honestly

- `runtime/scripts/type_check.py` — not shipped in the isolated toolkit.
  TYPECHECK.md documents the visual-read fallback (same as the parent).
- `runtime/remotion/src/illustrations/ILLUSTRATIONS.md` — present, but not
  needed for this Short's authored beats.
- `kerning` skill — not present; visual-read fallback used.
- The two read-only example JSONs referenced by BRIEF.md were not opened
  during this Short build (the Short is a whole-beat cut of the parent
  vertical, not a re-derivation from examples).
