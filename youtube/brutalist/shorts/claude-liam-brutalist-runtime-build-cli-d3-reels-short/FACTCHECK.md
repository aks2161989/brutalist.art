# FACTCHECK — Brutalist Utility: build_cli_d3_reels.py — Short

Derivative fact-check. Every claim made in a RETAINED beat is verified against
`runtime/scripts/build_cli_d3_reels.py` in the isolated toolkit at
`toolkit_baseline_sha256 92432609980c8ffc03bc1f00a1300fe1ac78bd7363b5b8ba9f2d389407d72b9d`.
Claims made only in dropped beats (B03/B04/B05/B06/B08/B10) are not repeated
here — the Short does not make them.

- Invocation `episode.source_sha256` (supervisor): `6d2d56ae2262b93e8d5864933bcd5c9dbd3c3b79a39a222b5a03b3a98356722f`
- Current file `shasum -a 256` of `build_cli_d3_reels.py`: `c37d17288291b4b7ca3ec7e06a23863f99b5c1c29c9f80554330829f459d172d`
- Line count: 432

| Beat | Narration claim | Where in source | Verified |
|---|---|---|---|
| B00 | "folder of D3 simulations already built, one HTML each" — the input is one HTML per sim | Module docstring L26–36; `sim['html']` is an INPUT path | YES |
| B00 | "batch WRAP" — one config in, N Claude-skin review cuts out, one row each in the log | `main()` L409–428 + `build_one()` L307–406 | YES |
| B01 | "build cli d3 reels does not generate the sim — the sim is already built; this tool WRAPS it from one HTML" | Module docstring L2–37; `sim['html']` never written | YES |
| B02 | Pipeline order STAMP → CAPTURE → AUDIO → REMOTION → COMPILE → log-append | `build_one()` L327–388 | YES |
| B02 | "idempotence — a >50KB slate mp4 short-circuits back to SKIP" (chip) | L314–319 (`stat().st_size > 50_000`) | YES |
| B07 | Worked-example dry-run: `greeting_for('00-tiny-wave')='Yo'` | `GREETINGS` list L52–56 + `greeting_for()` L59–60 | YES |
| B07 | `make_title` extracts "Sinusoidal wave with adjustable wavenumber k" from the note | L63–66 (`concept = note.split(";")[0].strip()`) | YES |
| B07 | 10 beats stamped `B00..B09` | `make_beat_sheet()` L200–290 | YES (10 beats exactly) |
| B09 | Verdict lines: input schema (slug · book · html · note · title?) | Module docstring L26–36 | YES |
| B09 | `make_beat_sheet()` writes the fixed 10-beat Claude template into `<book>/youtube/<reel_slug>/` | L125–291 + `build_one()` L309–310 | YES |
| B09 | `extract_code()` lifts the sim's OWN inline JS (ACTUAL-CODE LAW) | L69–106 (`max(blocks, key=len)`) | YES |
| B09 | Shell-out chain `capture_sim → kokoro → remotion_scenes → compile.py --review → compile.py master` | L341–388 | YES |
| B09 | One row per sim in `CLI-EXPLAINERS-OVERNIGHT-LOG.md`; SKIP if >50KB slate exists | L314–319 + `append_log()` | YES |
| B09 | `remotion_scenes` soft-fails to slates; other exceptions FAILED one sim, not the batch | L376–378 (soft-fail) + L402–406 (hard-fail) | YES |
| B11 | Outro title restated verbatim | Matches `metadata.title` | YES |

## Claims deliberately NOT made in the Short

- No claim of a specific overnight batch — the retained beats reference the disposable fixture only.
- No claim the Short itself was published — local review only; human viewing next.
- No claim about `capture_sim.py` running here — the sandbox blocks Chrome-driven HTML capture; the Short describes what the tool WOULD do.
- Dropped-beat code-walkthrough claims (`--help` verbatim, `make_beat_sheet` metadata dict, `extract_code` regex, `build_one` SKIP-guard code, soft-fail/hard-fail lines, Your-Turn paste-ready prompt) are NOT in the Short — the parent 16:9 long covers them.

## Cross-references verified

- OUTRO-LOCK.md — outro card hardcodes `@NikBearBrown`. Composer folder chip reads `@HumanitariansAI` on B00.
- CLAUDE-BRAND.md — palette + typography defaults match what the retained composer/code/verdict beats render.

## Human review pending

Human still owns final approval for the Short cut before any upload.
