# SHOTLIST — landscape 3840×2160 · 24 fps

12 beats · master duration ≈ 319.5 s. Every clip 4K native; Remotion `--scale=2` on the 1920×1080 comps produces a true 3840×2160 raster.

| # | act | pattern | duration (s) | motion | media |
| - | --- | ------- | ------------ | ------ | ----- |
| B00 | ASK | ClaudeComposerAsk | 15.53 | type-on (greeting → ask → runningText → 3 output lines) | media/B00.mp4 |
| B01 | BLUF | BrutalistHesitantWriter | 10.58 | hesitant-type (`paid`→`free`, `remote`→`local`) | media/B01.mp4 |
| B02 | FRAMEWORK | SkillTeardownPipeline | 29.82 | phase-flow (LOAD → FILTER → SYNTH → ENCODE → STAMP) | media/B02.mp4 |
| B03 | MECHANISM | ClaudeCodeBeat — CLI surface (verbatim `--help`) | 25.92 | code-cascade | media/B03.mp4 |
| B04 | MECHANISM | ClaudeCodeBeat — model_paths + load_engine + lang_for | 39.64 | code-cascade | media/B04.mp4 |
| B05 | MECHANISM | ClaudeCodeBeat — the five skip rules | 29.87 | code-cascade | media/B05.mp4 |
| B06 | MECHANISM | ClaudeCodeBeat — normalize + write_mp3 + measure | 38.95 | code-cascade | media/B06.mp4 |
| B07 | WORKED_EXAMPLE | ClaudeCodeBeat — demo/fixture-reel dry-run (observed) | 27.41 | code-cascade | media/B07.mp4 |
| B08 | MECHANISM | ClaudeCodeBeat — four failure modes | 35.14 | code-cascade | media/B08.mp4 |
| B09 | VERDICT | ClaudeVerdictArtifact — six lines | 31.04 | artifact-in | media/B09.mp4 |
| B10 | YOUR_TURN | ClaudeComposerAsk (greeting "Your Turn") | 28.80 | type-on | media/B10.mp4 |
| B11 | OUTRO | ClaudeTitleOutro (@NikBearBrown per OUTRO-LOCK) | 6.83 | outro-card | media/B11.mp4 |

## Legibility
- Serif family for the BLUF hesitant-writer sentence; monospace for all code cards.
- Palette is `claude` on cream (`#FAF9F5`).
- Code-cascade cards use the adaptive font clamp (bounded by BOTH card height and card width) so the 24-line snippets in B04/B06 remain readable at 4K.

## Motion pantry
- 4× code-cascade (B03/B04/B05/B06/B07/B08) — six is above the 50 % motion-cascade advisory. Accept as a documented deviation on utility teardowns; the source's shape *is* code, and every beat teaches a different function.
- 2× composer type-on (B00/B10) — bookend law.
- 1× hesitant-type (B01) — BLUF law.
- 1× phase-flow (B02) — framework law.
- 1× artifact-in (B09) — verdict law.
- 1× outro-card (B11) — outro law.

## Continuity
- Colour ground constant. Palette constant. Every beat has an on-screen title tying it back to file+lineno of the source.
- Ground truth: no captions burned in. Legible cards only.
