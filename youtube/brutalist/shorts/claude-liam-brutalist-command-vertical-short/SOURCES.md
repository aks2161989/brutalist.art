# SOURCES — Brutalist Command: art vertical — Short

## Derivation

This Short is a whole-beat cut of the parent full-length vertical
companion (`youtube/brutalist/claude-liam-brutalist-command-vertical/vertical/`).
No narration was rewritten; no visual was re-rendered. `shorts.py`
byte-copied the parent's approved per-beat mp4s and mp3s for the seven
kept beats.

- Parent beat sheet (source):
  `youtube/brutalist/claude-liam-brutalist-command-vertical/vertical/beat_sheet.json`
  SHA-256 (this invocation): `969393ab4032d07ee4d04d8fac3a477aed0ea417e2f775710c06a62bc5009b32`.
- Parent master (16:9 long, read-only reference):
  `youtube/brutalist/claude-liam-brutalist-command-vertical/exports/vertical/claude-liam-brutalist-command-vertical-vertical.mp4`
  SHA-256: `fed6f4ea25722b1c6768b360d3899215781c1cec7f4da50166893820019b8df3`.

## Primary sources (verbatim, quoted on screen in retained beats)

- **`art`** — the top-level dispatcher.
  Beats using verbatim excerpts in THIS Short: **B02** (help line at
  `art:15`; case block at `art:78-86`).
  Cited on screen as "Source: brutalist.art/art".

- **`runtime/scripts/shorts.py`** — the script both `art shorts` and
  `art vertical` invoke.
  Beats using verbatim excerpts in THIS Short: **B04** (the guardrail at
  `shorts.py:251-254`), **B07** (the actual shell log from
  `demo/VERTICAL-LOG.txt` INVOCATION 1, an unedited excerpt of what
  `shorts.py` printed when run against the fixture reel).
  Cited on screen as "Source: brutalist.art/runtime/scripts/shorts.py".

Both files are the exact toolkit revision captured in the parent
workspace's `SOURCE-SNAPSHOT.json`.

## Read-only example leads (never republished; adapted staging only)

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — SHA-256
  `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`.
  Used only as a staging lead for the `ClaudeComposerAsk` +
  `ClaudeVerdictArtifact` + `ClaudeTitleOutro` cadence. No signature, no
  Drive URLs, no old outputs reused.
- `swara-madison/08-28-video-update/loon-metadata-pipeline-vertical/beat_sheet.json`
  — SHA-256 `a34f0854671962d4bf8030ff4b53e4d69686866dc80acd0e4246105e8db95e66`.
  Used only to confirm the ClaudeComposerAsk916 / ClaudeTitleOutro916
  patterns exist as first-class portrait compositions. No signature, no
  Drive URLs, no old outputs reused.

## Demo fixture

- `/tmp/claude-501/claude-shorts-demo` — synthetic 7-beat REMOTION reel,
  214 s total, aspect 16:9. Contents of the `[short] ...` shell log
  shown in B07 are the actual output of running `./art vertical` on
  this fixture; nothing on it was uploaded, published, or committed.

## Rendering stack (retained beats)

- Kokoro TTS `am_onyx` — the seven parent-authored mp3s are reused
  byte-identical; no re-synthesis.
- Remotion `<pattern>916` compositions in the isolated toolkit
  (`runtime/remotion/src/Root.tsx`) — the seven parent-authored mp4s are
  reused byte-identical; no re-render.
- Compiler `runtime/scripts/compile.py --height 3840` — no `--review`
  fast-check as a final pass.

## Nothing here is uploaded or published

The mp4 lives at
`exports/short/claude-liam-brutalist-command-vertical-short.mp4`.
Publishing is a separate authorized human workflow.
