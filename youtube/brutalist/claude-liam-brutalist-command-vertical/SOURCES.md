# SOURCES.md — Brutalist Command: art vertical

## Primary sources (verbatim, quoted on screen)

- **`art`** — the top-level dispatcher.
  SHA-256 (this invocation): `9bb77a7c84701d23ab6e73f0a4f48592f17748ffad2c7114b62687bb7f97d0e9`.
  Repo path (public): `art`. Repo URL: https://github.com/nikbearbrown/brutalist.art.
  Beats using verbatim excerpts: B02 (`case "$cmd" in … shorts) … vertical) …`).
  Cited on screen as "Source: brutalist.art/art".

- **`runtime/scripts/shorts.py`** — the script both `art shorts` and
  `art vertical` invoke. SHA-256 (this invocation):
  `7109a3d0c29c00181a876db80e34238eb9c0c146a97a639a2bbab6d95d28d6e5`.
  Repo path: `runtime/scripts/shorts.py`. Beats using verbatim excerpts:
  B03 (module docstring, rule 5 — `--vertical creates a full-length
  companion, not a Short: …`), B04 (the two guardrail lines inside `main()`
  — `if a.vertical: … a.no_endcard = a.no_outro_rewrite = True`), B05 (the
  `is_remotion` and `portrait_pattern` helpers, unchanged from Ep 30
  because the ONDA check is one script for both verbs), B06 (the
  `require_short_duration` call gated by `if not a.vertical:`).
  Cited on screen as "Source: brutalist.art/runtime/scripts/shorts.py".

Both files are the exact toolkit revision captured in this workspace's
`SOURCE-SNAPSHOT.json` (commit `ba2d0e0f043f5b3b35a50d336e0fc66fbfecfc0c`).
The `source_sha256` for THIS INVOCATION's episode
(`cd7aa54c7426a1f839652d95ecfa6e412d5f59aecde4e66285c8c4a2b961f804`) is the
concatenation hash of `art` + `runtime/scripts/shorts.py`, computed by the
supervisor.

## Read-only example leads (never republished; adapted staging only)

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — Your Weekly
  Video, Handled. SHA-256 `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`.
  Local copy in `examples/746409a8715e.json`. Used only as a staging lead
  for the `ClaudeComposerAsk` + `ClaudeVerdictArtifact` + `ClaudeTitleOutro`
  cadence. No signature, no Drive URLs, no old outputs reused.
- `swara-madison/08-28-video-update/loon-metadata-pipeline-vertical/beat_sheet.json`
  — From Footage to Field Context. SHA-256
  `a34f0854671962d4bf8030ff4b53e4d69686866dc80acd0e4246105e8db95e66`. Local
  copy `examples/a34f08546719.json`. Used only to confirm the ClaudeComposerAsk916
  / ClaudeTitleOutro916 patterns exist as first-class portrait compositions.
  No signature, no Drive URLs, no old outputs reused.

## Sibling reference (adapted staging only, not republished)

- Ep 30 — `youtube/brutalist/claude-liam-brutalist-command-shorts/` (built
  from the same fixture reel `/tmp/claude-501/claude-shorts-demo` in a
  sibling workspace). Only the fixture is shared; every beat sheet, script
  line, and demo log in this episode was regenerated for `art vertical`.

## Demo fixture

- `/tmp/claude-501/claude-shorts-demo` — synthetic 7-beat REMOTION reel,
  214 s total, aspect 16:9. Created for Ep 30; kept on the tmpfs so the
  five verbatim invocations recorded in `demo/VERTICAL-LOG.txt` reproduce.
  Nothing on it was uploaded, published, or committed. Contents are the
  minimum needed to exercise the `art vertical` code path.

## Rendering stack

- Kokoro TTS `am_onyx` (local, free) — one MP3 per narration beat. Duration
  of the measured mp3 is the beat's authoritative clock.
- Remotion compositions in the isolated toolkit
  (`runtime/remotion/src/scenes/*.tsx`, registered in `runtime/remotion/src/Root.tsx`).
  Renderer wrapper `runtime/scripts/remotion_scenes.py`.
- Compiler `runtime/scripts/compile.py` at `--height 2160` for landscape and
  `--height 3840` for vertical.
- Chrome: `chrome-headless-shell` via `runtime/.wrappers/chrome-wrapper.sh`
  (Apple App Sandbox workaround, documented in the workspace CLAUDE.md
  ancestry; not a bypass of Remotion).

## Nothing here is uploaded or published

Bear's viewing/editing is the next step. Neither MP4 has been transcoded,
uploaded, or committed to any remote.
