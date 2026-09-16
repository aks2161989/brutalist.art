# SHOTLIST — vertical 2160×3840 · 24 fps

12 beats · master duration ≈ 319.7 s. Native 4K portrait; Remotion `--scale=2` on the 1080×1920 comps produces a true 2160×3840 raster. No landscape crop.

| # | act | pattern | duration (s) | motion | media |
| - | --- | ------- | ------------ | ------ | ----- |
| B00 | ASK | ClaudeComposerAsk916 | 15.53 | type-on | media/B00.mp4 |
| B01 | BLUF | BrutalistHesitantWriter916 (fontSize 220 / lineSpacing 1.9 / 4 lines) | 10.58 | hesitant-type | media/B01.mp4 |
| B02 | FRAMEWORK | SkillTeardownMechanism916 (portrait pipeline substitute) | 29.82 | phase-flow | media/B02.mp4 |
| B03 | MECHANISM | ClaudeCodeBeat916 — CLI surface + list-voices sample | 25.92 | code-cascade | media/B03.mp4 |
| B04 | MECHANISM | ClaudeCodeBeat916 — model_paths + load_engine + lang_for | 39.64 | code-cascade | media/B04.mp4 |
| B05 | MECHANISM | ClaudeCodeBeat916 — the five skip rules | 29.87 | code-cascade | media/B05.mp4 |
| B06 | MECHANISM | ClaudeCodeBeat916 — normalize + write_mp3 + measure | 38.95 | code-cascade | media/B06.mp4 |
| B07 | WORKED_EXAMPLE | ClaudeCodeBeat916 — demo/fixture-reel dry-run (observed) | 27.41 | code-cascade | media/B07.mp4 |
| B08 | MECHANISM | ClaudeCodeBeat916 — four failure modes | 35.14 | code-cascade | media/B08.mp4 |
| B09 | VERDICT | ClaudeVerdictArtifact916 — six lines | 31.04 | artifact-in | media/B09.mp4 |
| B10 | YOUR_TURN | ClaudeComposerAsk916 (greeting "Your Turn", shortened segment) | 28.80 | type-on | media/B10.mp4 |
| B11 | OUTRO | ClaudeTitleOutro916 (patched to wrap long filenames) | 6.83 | outro-card | media/B11.mp4 |

## Portrait-only differences from the landscape shotlist

- `SkillTeardownPipeline` (horizontal 5-phase strip) swapped for `SkillTeardownMechanism916` — the pipeline strip bleeds portrait safe on the left/right, per prior episode feedback.
- `topic` on B00 shortened from `BRUTALIST · UTILITY: GENERATE_AUDIO_KOKORO.PY` to `BRUTALIST · UTILITY` (45 → 19 chars) to clear portrait-safe right edge.
- `segment` on B10 shortened from `Dry-run, then generate two beats` to `Dry-run + generate two` (32 → 22 chars).
- B01 rebuilt at fontSize 220 / lineSpacing 1.9 (portrait requires wider bbox for Gate V FILL_MIN).
- Every code beat now uses `ClaudeCodeBeat916` (1080×1920 native comp). The adaptive font clamp on `ClaudeCodeBeat.tsx` bounds by width AND height, so long code stanzas that fit landscape also fit portrait.
- Outro title unchanged in content; the component was patched (see PROMPTS.md) so the long filename wraps.

## Legibility, motion pantry, continuity

Same rules as landscape (see landscape `SHOTLIST.md`): serif on the BLUF, mono on code cards, cream ground, `code-cascade` 6/12 accepted as a documented utility-teardown deviation from the ~40 % pantry cap.
