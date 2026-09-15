# SOURCES — Brutalist Utility: brand_variant.py

## Primary source

- `runtime/scripts/brand_variant.py`
  - Source SHA-256 (episode contract, from `THIS INVOCATION.episode.source_sha256`): `bbdce06cb6b9f833342550139061afd29969efcbab74bbd0db6b46b10a835427`
  - Snapshot SHA-256 (SOURCE-SNAPSHOT.json, working-toolkit copy at build time): `ced0d3f79d98e5d9b18e005679474b64f8fe3b897f5f6fef6b5b3ee2ed02756e`
  - Public path: https://github.com/nikbearbrown/brutalist.art/blob/main/runtime/scripts/brand_variant.py
  - Every code snippet in the film is quoted verbatim from that file's docstring, `AUD` dict, `get_brand_dir()`, and `main()` body.

## Referenced (read-only) toolkit docs

- `skills/make/ai-explainer/SKILL.md` — governs the beat spine, ILLUSTRATE LAW, ASK→RESULT, COLD OPEN, BLUF (hesitant writer), HANDOFF, OUTRO.
- `skills/make/nopunt/SKILL.md` — SHOW / HOLD / CARD classification; whole-sheet exit condition.
- `skills/make/hai/SKILL.md`, `skills/make/nbb/SKILL.md` — referenced by the two per-audience `_variant_todo` lists this utility writes (verified by opening the files during factcheck).
- `runtime/prose/teardown/PROSE.md` — Teardown register cues (Feynman × MKBHD).
- `runtime/prose/plain/PROSE.md`, `brands/hai.md`, `brands/nbb.md`, `CLAUDE-BRAND.md` — charter files referenced by `brand_variant.py:32-40`; presence spot-checked, not opened for narration.
- `docs/PIPELINE-SAFETY.md` — never publish; free-only pipeline; audio-first.
- `docs/FELLOWS-SUBMISSION.md` — landscape + portrait; both native 4K.
- `OUTRO-LOCK.md` — outro card is `@NikBearBrown` hardcoded, slug-seeded mascot.
- `CLAUDE-BRAND.md` — cream `#FAF9F5`, ink `#3D3929`, terracotta `#D97757`, EB Garamond serif.
- `CLAUDE-CODE-VISUAL-QC-CHECK.md` — the frame rubric.

## Read-only example leads (from BRIEF.md — treated as leads, not reused verbatim)

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — SHA-256 `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22` (Your Weekly Video, Handled).
- `yatra-r/2026-08-30-one-tool-a-week-brandy/beat_sheet.json` — SHA-256 `e219593a27eaf6d68b43d3c9c89243cb90fd1e9dab7fd1199abc000d757af38e` (One Tool a Week).

Neither fellow's audio, signature, or Drive URL is reused. What their beat sheets validate is the shape of a "single-command utility" episode: cold open on the ask, one hesitant-writer correction, an anchored framework diagram, code beats in the middle, verdict, handoff, outro. That structure is native to the ai-explainer skill; the examples are consistent with it.

## Reference toolchain (verified live during the demo)

- `runtime/scripts/brand_variant.py` — used to produce every variant in `demo/` on this workstation.
- `runtime/scripts/generate_audio_kokoro.py` — used to produce the film's per-beat MP3s; Kokoro `am_onyx`.
- `runtime/scripts/remotion_scenes.py` — renders each beat's MP4 with the correct dimensions.
- `runtime/scripts/compile.py --height 2160` / `--height 3840` — assembles landscape / vertical.
- Chrome shim (`ART_CHROME=…/chrome-single-process.sh`, `ART_CHROME_MODE=chrome-for-testing`) — collapses Chrome renderer processes to work around Apple sandbox Mach-port bind restrictions; behaviour tracked in memory `feedback_chrome_sandbox.md`.
- `runtime/remotion/node_modules` shadow directory — per-entry symlinks + writable `.cache/` so webpack can rotate its pack files inside the isolated toolkit; tracked in memory `feedback_isolated_toolkit_node_modules_shadow.md`.

## Demonstration fixtures (all disposable, all in `demo/`)

- `demo/canonical/beat_sheet.json` — a 2-beat seed sheet with intentionally stale `engine: "elevenlabs"`, `voice_id: "legacy-eleven-id-should-be-dropped"`, and `shot.rendered` stamps, to prove the deterministic transforms and the strip-stale-timings loop.
- `demo/claude-liam-canonical/beat_sheet.claude-liam.json` — variant emitted by `python3 runtime/scripts/brand_variant.py demo/canonical claude-liam`.
- `demo/nbb-canonical/beat_sheet.nbb.json` — variant emitted by the `nbb` run.
- `demo/hai-canonical/beat_sheet.hai.json` — variant emitted by the `hai` run (also demonstrates `--force`).
- `demo/book-example/lectures/chap01-lecture/beat_sheet.json` + `demo/book-example/hai-lectures/chap01-lecture/beat_sheet.hai.json` — lecture-layout example proving `get_brand_dir()` picks the `<book>/<suffix>-lectures/<chap>/` branch when the path contains `lectures`.

The full verbatim command / output log is `demo/RUN-LOG.txt`.

## Nothing invented, nothing paid

No paid API was called. No network service was contacted. Every second of narration in the film is fresh Kokoro `am_onyx` audio produced on this workstation for this run_id (`0ff7fe5fe3054305bc9f24dfce896045`). The demo variants were produced by the real `brand_variant.py` in the isolated toolkit; the canonical fixture SHA-256 (`7da66eeff7b59c7af7304d555ba2529caca28b932155ffec69fea508b640dd16`) is identical before the first run and after every subsequent run — see FACTCHECK D2 and RUN-LOG §14.
