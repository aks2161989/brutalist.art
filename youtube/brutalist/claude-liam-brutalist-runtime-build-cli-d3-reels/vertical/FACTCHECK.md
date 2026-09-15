# FACTCHECK — Brutalist Utility: build_cli_d3_reels.py

Every claim in the beat sheet is verified against
`runtime/scripts/build_cli_d3_reels.py` in the isolated toolkit at
`toolkit_baseline_sha256 92432609980c8ffc03bc1f00a1300fe1ac78bd7363b5b8ba9f2d389407d72b9d`.

- Invocation `episode.source_sha256` (supervisor): `92253347e5028837c16c2590f4b803bb8f32e88754ba255c1424fe9eefc29abc` (re-verified 2026-09-13; previous invocation SHA `6d2d56ae2262b93e8d5864933bcd5c9dbd3c3b79a39a222b5a03b3a98356722f`)
- Current file `shasum -a 256` of `build_cli_d3_reels.py`: `c37d17288291b4b7ca3ec7e06a23863f99b5c1c29c9f80554330829f459d172d`
- Line count: 432
- All file:line references below are against the current file in the toolkit.

| Beat | Narration claim | Where in source | Verified |
|---|---|---|---|
| B00 | "one config in → per-sim beat sheet → capture → audio → Remotion → compile.py review, one row per sim in the log" | `main()` L409–428 + `build_one()` L307–406 | YES |
| B01 | "build_cli_d3_reels does not generate the sim; it wraps an already-built HTML" | Module docstring L2–37: "The input beats wear the CLAUDE Remotion template …"; `sim['html']` is the INPUT path, not written | YES |
| B02 | seven-phase pipeline STAMP → CAPTURE → AUDIO → REMOTION → COMPILE → LOG | `build_one()` L327–399 (steps executed in order) | YES (five bars shown on the diagram; the `LOG` phase is the output box + the beats' `append_log`) |
| B02 | "idempotence — a >50KB slate mp4 short-circuits back to SKIP" | L314–319 | YES |
| B03 | `--help`: usage + one required positional `config` + one optional `--log LOG` | L410–413 `argparse.ArgumentParser`; verbatim copy in `demo/help.txt` | YES |
| B03 | config schema: `sims[]` with slug, book, html, note, optional title | Module docstring L26–36 | YES |
| B04 | metadata locks `voice_kokoro=am_onyx`, `engine=kokoro`, `palette=claude`, `register=Teardown`, `channel=claude-liam` | `make_beat_sheet()` L188–199 | YES |
| B04 | 10-beat template B00–B09 | `make_beat_sheet()` L200–290 | YES (10 beats exactly) |
| B04 | B00=ClaudeComposerAsk, B03=ClaudeCodeBeat, B04/B06=video slots, B08=ClaudeComposerAsk, B09=ClaudeTitleOutro | L200–290 remotion_shot() calls | YES |
| B05 | extract_code: regex over `<script>` tags without `src=`; longest block; first 20 meaningful lines; wrap 78 chars | L69–106 | YES (`max_lines=20`, `max_width=78`, `max(blocks, key=len)`) |
| B05 | header + footer wrapping the trimmed body | L104–106 | YES |
| B06 | line 315 SKIP-guard: `review_mp4.exists() and .stat().st_size > 50_000` | L314–319 | YES (literal 50_000) |
| B06 | seven subprocess calls (capture, audio, remotion, compile review, compile master + append_log around them) | L341–388 | YES |
| B06 | every subprocess call is time-boxed | L342 (240), L358 (600), L371 (900), L380 (600), L385 (600) | YES |
| B07 | worked example `demo/config.json` → dry-run output | `demo/RUN-LOG.txt`, `demo/beat_sheet_dryrun.json`, `demo/config.probe.txt` — all captured verbatim from Python import of the module (see B04 line quotes) | YES |
| B07 | greeting_for('00-tiny-wave') = 'Yo' | L59–60 + `GREETINGS` list L52–56; observed dry-run output line 1 | YES |
| B07 | make_title extracts "Sinusoidal wave with adjustable wavenumber k" from the note | L63–66; observed dry-run | YES |
| B08 | soft-fail on remotion_scenes: `[build] WARN remotion_scenes failed — Claude beats stay slates` | L376–377 (verbatim) | YES |
| B08 | hard-fail catch: `except Exception as e:` writes FAILED row | L402–406 | YES |
| B08 | verbatim `HTML not found` example | `demo/failure-html-missing.txt` (captured live) | YES |
| B09 | verdict summary of the whole file, in the order it does its job | L307–406 | YES |
| B10 | Your-Turn suggested prompt "write me a config.json for these HTMLs, dry-run only" | scaffolded to `make_beat_sheet` interface — the prompt reads it aloud; the field the note field really does become B01 problem line + title (L142/L146/L172, `concept = note.split(";")[0].strip()`) | YES |
| B11 | outro title restated verbatim | matches metadata.title | YES |

## Claims deliberately NOT made on screen (avoiding fabrication)

- No claim that this reel was published (per BRIEF: local review only; human viewing next).
- No claim that `capture_sim.py` ran successfully as part of this demo (the sandbox blocks Chrome-driven HTML capture; the demo shows the module's INPUT/OUTPUT stamping path only). This is honest source-backed illustration, not a claimed successful capture.
- No claim of a specific overnight batch — the fixture is disposable and clearly labelled in `demo/config.json._note`.

## Cross-references verified

- OUTRO-LOCK.md — outro card hardcodes `@NikBearBrown`. Playlist channel adaptation happens only on the composer folder chip; flagged in `README.md`.
- CLAUDE-BRAND.md — palette + typography defaults match what `make_beat_sheet()` writes.
- ACTUAL-CODE LAW quote in B05 is a paraphrase in the narration; the CODE beat's TITLE and CODE prop carry the source's exact `re.findall(...)` line.

## Human review pending

Bear will watch the rendered film and can flag any residual factual issues in FEEDBACK.md.
