# SOURCES — Brutalist Command: art doctor — Short

The Short is a whole-beat cut of the parent vertical companion; every source
listed below was already verified for the parent build and re-used unchanged
for this Short. No new source files were introduced.

## Primary sources (parent build, verified live)

- `art` (toolkit root) — the dispatcher.
  - Source path: `brutalist.art/art`
  - Parent-build SHA-256: `9bb77a7c84701d23ab6e73f0a4f48592f17748ffad2c7114b62687bb7f97d0e9`
  - Kept-beat citations in this Short: none on-screen (the B02 dispatcher
    walkthrough was dropped); referenced verbally in B09's verdict
    ("bare invocation — `./art doctor [--install]`; wraps the setup script
    with `$@` forwarded" — corresponds to `art:96-99`).
- `setup` (toolkit root) — the readiness auditor executed by `art doctor`.
  - Source path: `brutalist.art/setup`
  - Parent-build SHA-256: `75040062dfcb20d0437a5a358abc516ed6e4b1e4e9020aaac926e1b9d5b2208d`
  - Kept-beat citations in this Short: `setup:57` (mode branch, cited in B03),
    `setup:137` (kokoro_synth check, shown verbatim in B06),
    `setup:142-150` (FEATURES array, shown verbatim in B03),
    `setup:178` (exit 1 line, quoted in B09).
- `runtime/scripts/setup_smoke_kokoro.py` — the phrase-and-decode smoke test
  invoked by the `kokoro_synth` check row. Not on screen; referenced by name
  in B06.

The B05 walkthrough of `setup:117-140` (check() + dynamic OK_/MISS_) and the
B07 walkthrough of `setup:156-172` (aggregation loop) are dropped for the
Short; both remain in the parent 16:9 master and the vertical companion.

## Parent reel provenance

- Parent 16:9 reel: `youtube/brutalist/claude-liam-brutalist-command-doctor`.
- Parent vertical companion: `.../vertical/` — the direct source for this
  Short's media, mp3 and beat_sheet.
- Parent vertical master: `.../vertical/exports/vertical/claude-liam-brutalist-command-doctor-vertical.mp4`
  (SHA-256 `6841c2a078a80271abf298ffe2db0e8b4e571101373abc2d50144523effcb67d`) — not modified.

## Demonstrations reused verbatim (parent's `demo/RUN-LOG.txt`)

- Section 2 — `./art doctor` on a fully green toolkit, exit 0
  (source of B04's rendered green table).
- Section 3 — `./art doctor` with `runtime/models/kokoro/kokoro-v1.0.onnx`
  temporarily moved aside, one red row + two hint lines, exit 1
  (source of B08's "AFTER" section).
- Section 4 — `./art doctor` after restoring the file, exit 0
  (source of B08's "RECOVERY" section).

## Adaptation examples (read-only leads from example-sources.json)

The Shorts prompt supplied two leads from the shorts adaptation pool. Both
were read as staging references; nothing from either file was reused verbatim.

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — "Your Weekly
  Video, Handled." SHA-256 `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`.
- `anjana-s/2026-08-21-ecis-explained/beat_sheet.json` — "ECIS — Episode 3:
  Three Models, Zero Shortcuts." SHA-256 `1deb9bfc4fd4acf81ae98fccbc1fb3c1c400e370299db7bbc34d3ba527a57516`.

## Playlist doctrine sources (already documented in the toolkit)

- `skills/make/ai-explainer/SKILL.md`, `skills/make/nopunt/SKILL.md`.
- `OUTRO-LOCK.md` (hardcoded @NikBearBrown handle on `ClaudeTitleOutro`).
- `CLAUDE-BRAND.md`, `docs/PIPELINE-SAFETY.md`, `docs/FELLOWS-SUBMISSION.md`.

## Boundaries

No network calls, no paid API, no upload, no publication. The Short is a
render-only derivative built inside the supplied isolated toolkit and the
supplied `reel` directory; the parent reel and public toolkit are read-only.
