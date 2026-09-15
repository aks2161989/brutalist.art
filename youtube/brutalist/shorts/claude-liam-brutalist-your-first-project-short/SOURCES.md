# SOURCES.md — Your First Brutalist Project (Short, 9:16)

This Short is a derivative cut of the parent portrait companion; no new footage was sourced.

## Parent reel (independent copies of media/, mp3/, paperwork)

- **Reel:** `youtube/brutalist/claude-liam-brutalist-your-first-project/`
- **Portrait companion (this Short's direct source):** `youtube/brutalist/claude-liam-brutalist-your-first-project/vertical/`
- **Portrait companion beat sheet SHA-256:** `d8d08b74e70c53040f1f45e050baf928e004b11f90884fff2ea7b949eb047235`
- **Portrait companion master MP4 SHA-256:** `1d01e65c3c45d6b0864bbf9145aacc4d681ad72fbc12d37527b6f06cbbd68ee4` (verified via `shasum -a 256`)
- **Cut utility:** `runtime/scripts/shorts.py --drop B02 B06 B07 B08 B09 --no-endcard --no-outro-rewrite`

Retained beats (B00, B01, B03, B04, B05, B10, B11) had their `media/<BID>.mp4` and `mp3/beat-<BID>.mp3` copied byte-for-byte into this reel by `shorts.py` (verified by the `input_sha256` map in `exports/short/*.verified.json`).

## Toolkit (isolated workspace, read-only public repo untouched)

- **Toolkit path:** `.repoloop/shorts/workspaces/claude-liam-brutalist-your-first-project-short/toolkit/`
- **Scripts used:** `runtime/scripts/shorts.py`, `runtime/scripts/compile.py`, `runtime/scripts/build_safety.py`
- **Remotion registry:** `runtime/remotion/src/Root.tsx` — portrait compositions `ClaudeComposerAsk916`, `BrutalistHesitantWriter916`, `ClaudeCodeBeat916`, `ClaudeVerdictArtifact916`, `ClaudeTitleOutroHAI916` present (verified via `grep`).
- **Skill under test:** `skills/make/ai-explainer/SKILL.md` — the pipeline the parent reel teaches.

No live library files in the public toolkit were modified by this build.

## Read-only example leads (from `example-sources.json`)

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` (SHA-256 `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`)
- `uday-s/2026-08-27-weekly-fixtures-before-validators/beat_sheet.json` (SHA-256 `9e97abd5857ab5ab6e01230bf201f53e66ec455ef86c72208e67bce6416fd4f1`)

Consulted only as pattern leads (which compositions the fellows used, how the cold-open composer + verdict artifact + outro cadence works). No narration, media, or signatures were copied.

## External / paid resources

- **None.** No paid API, no upload, no external asset ingest. The audio is local Kokoro `am_onyx`; the visuals are local Remotion renders inherited from the parent portrait companion; the compile is `ffmpeg` + Python stdlib.
