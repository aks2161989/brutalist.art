# FACTCHECK.md — Brutalist Command: art smoke

Every claim shown or spoken in this reel is checked below against the sources
in SOURCES.md. Verified on the isolated toolkit snapshot at
`.repoloop/workspaces/claude-liam-brutalist-command-smoke/toolkit/` on
2026-09-12, run_id `e6fb28666cd04b18b360c7b6af6d7995`.

## Dispatcher case (B02)

- **Claim:** `./art smoke` execs `runtime/scripts/smoke_test.sh` with `$@`
  forwarded, and the case has no aliases and no flags.
- **Evidence:** `art:121-123` (SHA-256 `c5b4e995…fc08c5b`) —
  ```
  smoke)
    exec bash "$ART_HOME/runtime/scripts/smoke_test.sh" "$@"
    ;;
  ```
  The `./art --list` help header (`art:6-19`) lists smoke as
  "real end-to-end render proof (examples/_smoke -> watchable mp4)" with no
  arguments after the verb.
- **Status:** VERIFIED.

## Pipeline stages (B03)

- **Claim:** smoke_test.sh copies `examples/_smoke/.` into a `mktemp -d`
  scratch dir, then runs `generate_audio_kokoro.py`, then
  `ART_FACTS=0 ART_QC=1 ART_STRICT=0 bash runtime/scripts/run.sh`.
- **Evidence:** smoke_test.sh lines 32-58 (SHA-256 `d5403ed9…6cae90`).
- **Status:** VERIFIED (line-for-line).

## Three decoded gates (B03, B05)

- **Claim:** GATE SIZE floor 20000 bytes; GATE TYPE requires both video and
  audio streams; GATE AUDIO requires mean_volume > -40 dB.
- **Evidence:** smoke_test.sh lines 27 (`SIZE_FLOOR_BYTES=20000`), 63-72
  (SIZE + TYPE), 74-79 (AUDIO). The `-40 dB` threshold appears on lines 78
  and mirrors `setup_smoke_kokoro.py:22` (`THRESHOLD_DB = -40.0`).
- **Status:** VERIFIED.

## The fixture (B04)

- **Claim:** `examples/_smoke/beat_sheet.json` ships as two narration slates
  (B00/B01), Kokoro `af_bella`, zero Manim, zero Remotion.
- **Evidence:** `examples/_smoke/beat_sheet.json` (SHA-256
  `5522f1ce…5f1cca97`) — literal transcription in the beat.
- **Status:** VERIFIED (transcription faithful; JSON key ordering rearranged
  for readability with no semantic change).

## The reproduction — passing path (B06)

- **Claim:** Under the pass path, generate_audio_kokoro yields two mp3s
  (B00 8.73s af_bella, B01 5.12s af_bella); run.sh compiles a slate mp4
  ~13.9s; the finished mp4 is 636229 bytes, has both streams, and reads
  mean_volume -24.2 dB.
- **Evidence:** `demo/RUN-LOG.txt` sections 3 — captured directly from
  the isolated toolkit on 2026-09-10T01:01:38+00:00.
- **Status:** VERIFIED (verbatim from RUN-LOG.txt).

## The recovery — current-shipped failure (B07)

- **Claim:** Running `./art smoke` on the tip-of-tree shipped fixture fails at
  GATE 0 with `[kokoro] REFUSED: metadata.slug must be a filename, not a
  path`; exit 1. The offending regex is at
  `runtime/scripts/build_safety.py:186-187`
  (`re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]*', slug)`). The fixture ships
  with `metadata.slug = "_smoke"`, which the regex rejects because the
  leading underscore is not in the anchor character class `[A-Za-z0-9]`.
- **Evidence:** `demo/RUN-LOG.txt` section 2 — captured under the
  `.mktemp-shim/mktemp` wrapper (which only reroutes `mktemp -d` to
  `$TMPDIR`; the failure surface is untouched by the shim).
  `runtime/scripts/build_safety.py` (SHA-256 `479e167f…56015bf`), lines
  186-187. Introduced in commit `ba2d0e0` (2026-09-07) — three days before
  this recording; before that commit, no `build_safety.py` existed and no
  slug regex ran, so `./art smoke` had been working.
- **Status:** VERIFIED — a genuine live regression, not a re-enactment.

## `./art doctor` still green (B07, B08)

- **Claim:** On this same box, `./art doctor` reports every FEATURE ready.
- **Evidence:** captured via `./art doctor` — logged in
  `demo/RUN-LOG.txt` (pass-path section preamble). All seven rows read
  `✅ ready`; exit code 0.
- **Status:** VERIFIED.

## Sandbox note (README.md and this reel's process notes)

- **Claim:** On this workstation, macOS's App Sandbox denies writes to the
  default `mktemp -d` target (`/var/folders/…`), so the smoke script's
  scratch-dir creation fails until PATH is prepended with a local shim
  that reroutes to `$TMPDIR`.
- **Evidence:** direct terminal output —
  `mktemp: mkdtemp failed on /var/folders/f4/…: Operation not permitted`;
  `.mktemp-shim/mktemp` script in the isolated toolkit reroutes to
  `/tmp/claude-501/…` and every downstream stage runs.
- **Status:** VERIFIED. This is a property of the recording environment,
  not of `./art smoke` itself, and is called out in the demo log.

## Not shown / limitations

- We did not run the FULL `smoke_test.sh` end to end against an
  unmodified fixture on this box. On the shipped fixture GATE 0 refuses;
  on the patched fixture smoke_test.sh's hardcoded `OUT="$WORK/_smoke-slate.mp4"`
  looks for a file the compile step now names `smoke-slate.mp4`.
  The B07 recovery beat calls this out honestly.
- All demonstrations use the isolated toolkit; the shipped repo is
  read-only in this environment.
