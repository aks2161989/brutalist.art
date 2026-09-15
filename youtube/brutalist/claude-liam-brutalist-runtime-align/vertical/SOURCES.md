# SOURCES — Brutalist Utility: align.py

## Primary source

- `runtime/scripts/align.py`
  - Source SHA-256 (episode contract): `89e0f38ded269908fab42362723f9dab3d87f449bf08e70cad05a4e4efb3c33e`
  - Snapshot SHA-256 (SOURCE-SNAPSHOT.json, working-toolkit copy at build time): `b2ee07253e474cbce79820dc90199929570880e012062e5b8c4980ca31bc3058`
  - Public path: https://github.com/nikbearbrown/brutalist.art/blob/main/runtime/scripts/align.py
  - Every code snippet in the film is quoted verbatim from that file's `__doc__` and function bodies.

## Referenced (read-only) toolkit docs

- `skills/make/ai-explainer/SKILL.md` — governs the beat spine, ILLUSTRATE LAW, ASK→RESULT, COLD OPEN, BLUF (hesitant writer), HANDOFF, OUTRO.
- `skills/make/nopunt/SKILL.md` — SHOW / HOLD / CARD classification; whole-sheet exit condition.
- `runtime/prose/teardown/PROSE.md` — Teardown register cues (Feynman × MKBHD).
- `docs/PIPELINE-SAFETY.md` — never publish; free-only pipeline; audio-first.
- `docs/FELLOWS-SUBMISSION.md` — landscape + portrait; both native 4K.
- `OUTRO-LOCK.md` — outro card is `@NikBearBrown` hardcoded, slug-seeded mascot.
- `CLAUDE-BRAND.md` — cream `#FAF9F5`, ink `#3D3929`, terracotta `#D97757`, EB Garamond serif.
- `CLAUDE-CODE-VISUAL-QC-CHECK.md` — the 9-point frame rubric.

## Read-only example leads (from BRIEF.md — treated as leads, not reused verbatim)

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — SHA-256 `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`
- `yatra-r/2026-09-03-this-week-gordy/beat_sheet.json` — SHA-256 `7e3ea1f61c421e605e583be9b2a7b5f554aa8cadfb6e14dabaee66f471856083`

Neither fellow's audio, signature, or Drive URL is reused. What their beat sheets validate is the shape of a "code utility" episode: cold open on the ask, one hesitant-writer correction, an anchored framework diagram, code beats in the middle, verdict, handoff, outro. That structure is native to the ai-explainer skill; the examples are consistent with it.

## Reference toolchain (verified live during the demo)

- `faster-whisper` 1.2.1 (`python3 -c "import faster_whisper; print(faster_whisper.__version__)"`).
- CTranslate2 model `Systran/faster-whisper-base` — cached under `~/.cache/huggingface/hub`.
- `runtime/scripts/generate_audio_kokoro.py` — used to produce the demo MP3s; Kokoro `am_onyx`.
- `runtime/scripts/remotion_scenes.py` — renders each beat's MP4 with the correct dimensions.
- `runtime/scripts/compile.py --height 2160` / `--height 3840` — assembles landscape / vertical.

## Demonstration fixtures (all disposable, all in `demo/`)

- `demo/single-beat/` — one beat, happy path, one aligned MP3.
- `demo/number-drift/` — narration_text contains `1926`; audio speaks "nineteen twenty six"; verbatim `words.json` shows the digits preserved.
- `demo/only-flag/` — three beats, then `--only B02` rerun; `words.json` merges cleanly.
- `demo/skip-cases/` — three skip reasons (no duration; no audio_file; missing file on disk).

The full verbatim command / output log is `demo/RUN-LOG.txt`.

## Nothing invented, nothing paid

No paid API was called. No network transcription service was used (the model runs locally on CPU int8). No external voice, no ElevenLabs, no cloud rendering. Every second of narration in the film is fresh Kokoro `am_onyx` audio produced on this workstation for this run_id (`33e2b4ebabdb435c9c09331280ce2f05`).
