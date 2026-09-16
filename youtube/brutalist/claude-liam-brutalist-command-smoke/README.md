# Brutalist Command: art smoke

Playlist: **Brutalist** · Channel: **@HumanitariansAI** · Persona: **Liam,
in for Bear** (Kokoro `am_onyx`, free local pipeline) · Run:
`e6fb28666cd04b18b360c7b6af6d7995` (2026-09-12 UTC).

Command teardown of `./art smoke` — the two-line dispatcher case at
`art:121-123` that execs `runtime/scripts/smoke_test.sh`, which builds
the `examples/_smoke/` fixture in a throwaway scratch dir and verifies
the compiled mp4 with three DECODED gates (SIZE > 20000 bytes, TYPE =
both a video and an audio stream, AUDIO = ffmpeg `volumedetect` mean
volume above -40 dB). Contrast with `./art doctor`: doctor checks deps
in isolation; smoke proves the mp4 actually renders.

## The two films

Bear's viewing / editing is next — **these files are not published**.

- **Landscape 3840×2160** ·
  [`exports/landscape/claude-liam-brutalist-command-smoke.mp4`](exports/landscape/claude-liam-brutalist-command-smoke.mp4)
  — 238.7s · 11 beats · mean_volume -27.0 dB · h264 / AAC.
- **Portrait 2160×3840** (native, not a crop) ·
  [`exports/vertical/claude-liam-brutalist-command-smoke-vertical.mp4`](exports/vertical/claude-liam-brutalist-command-smoke-vertical.mp4)
  — 238.7s · 11 beats · mean_volume -27.0 dB · h264 / AAC.

## Paperwork

Landscape reel root:
- [`beat_sheet.json`](beat_sheet.json) — authored beat sheet (11 beats).
- [`SCRIPT.md`](SCRIPT.md) — narration per beat.
- [`FACTCHECK.md`](FACTCHECK.md) — every on-screen claim verified against
  `art:121-123`, `smoke_test.sh:22-83`, `build_safety.py:186-187`,
  `examples/_smoke/beat_sheet.json` and the verbatim demo log.
- [`SOURCES.md`](SOURCES.md) — repo-relative source paths + SHAs.
- [`SHOTLIST.md`](SHOTLIST.md), [`PROMPTS.md`](PROMPTS.md).
- [`CHECKS-REPORT.md`](CHECKS-REPORT.md) — commands run and observed output.
- [`TYPECHECK.md`](TYPECHECK.md) — visual typography review (in place of
  the unshipped legacy `type_check.py`).
- [`VISUAL-REVIEW.json`](VISUAL-REVIEW.json) — AI-review record with real
  hashes; human review pending.
- [`demo/RUN-LOG.txt`](demo/RUN-LOG.txt) — verbatim capture of `./art smoke`
  on this workstation (both the current shipped-fixture failure and the
  reproduced pass path).

Vertical companion (`vertical/`): its own `beat_sheet.json`, and per-aspect
`FACTCHECK.md`, `SOURCES.md`, `SHOTLIST.md`, `PROMPTS.md`, `CHECKS-REPORT.md`,
`BUILD-PROMPT.md`, `TYPECHECK.md` and `VISUAL-REVIEW.json`.

## Flags for the human reviewer

1. **Outro handle.** `ClaudeTitleOutro` is locked to `@NikBearBrown` per
   OUTRO-LOCK.md, but this reel is destined for `@HumanitariansAI`. The
   composer folder chip in every non-outro beat correctly reads
   `@HumanitariansAI`; the outro card does not. Decide whether to (a) keep
   the outro-lock and file a downstream HAI outro variant, or (b) hand-edit
   the outro title card to swap the handle.
2. **Live regression exposed by this reel.** The reel's B07 documents that
   `./art smoke` currently fails on tip of tree because
   `examples/_smoke/beat_sheet.json` ships with `metadata.slug = "_smoke"`
   and the recent `build_safety.validate_project` slug regex rejects the
   leading underscore. The fix is one character — either rename the fixture
   slug to `smoke` (and update the `smoke_test.sh:60` hardcoded
   `_smoke-slate.mp4` reference) or widen the regex to allow a leading
   underscore for the fixture. This is a genuine current bug; the reel
   surfaces it because that is exactly what `./art smoke` exists to catch.
3. **Sandbox note (recording environment only).** This build was rendered
   inside a macOS App Sandbox that blocks `mktemp -d`'s default target. A
   local `.mktemp-shim/mktemp` wrapper was prepended to PATH ONLY to
   capture `./art smoke`'s own output for the demo log; the shipped script
   was not modified and the shim does not travel with the exports.
