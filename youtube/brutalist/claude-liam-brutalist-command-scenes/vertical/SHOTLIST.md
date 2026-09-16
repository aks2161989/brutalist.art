# SHOTLIST — Brutalist Command: art scenes

12 beats, all Remotion-native, all on the Claude fidelity stage
(page `#FAF9F5`, ink `#3D3929`, spark `#D97757`). No Manim, no supplied media,
no captions.

| # | ID | Act | Duration (s) | Pattern | On screen |
|---|---|---|---|---|---|
| 1 | B00 | ASK | 18.65 | `ClaudeComposerAsk` | Greeting "Namaste, Liam"; command types; output cascades (620 compositions · id/synonym/haystack IDF · three aliases) |
| 2 | B01 | BLUF | 12.35 | `BrutalistHesitantWriter` | Hesitant serif: "art scenes writes / new scenes." → the words *writes* and *new* correct to *finds* and *existing* |
| 3 | B02 | FRAMEWORK | 14.61 | `ClaudeCodeBeat` | The `art:67-70` case branch; three aliases; one `exec python3 scene_search.py` |
| 4 | B03 | MECHANISM | 23.70 | `ClaudeCodeBeat` | `runtime/remotion/src/scenes.json` schema — count, id/aspect/folder/desc/synonyms/props, one sample record |
| 5 | B04 | MECHANISM | 27.35 | `ClaudeCodeBeat` | `scene_search.py` `score()` — id 3× / synonym 2× / haystack 1×; IDF re-weighting; derived-only penalty |
| 6 | B05 | WORKED_EXAMPLE | 25.92 | `ClaudeCodeBeat` | Verbatim `./art scenes "sankey flow"` — FinanceSankey wins at 8.5, three SourceFlow at 4.5 |
| 7 | B06 | WORKED_EXAMPLE | 26.37 | `ClaudeCodeBeat` | `--check ClaudeComposerAsk BarChart NotAScene` + `--undocumented` (118 scenes) |
| 8 | B07 | WORKED_EXAMPLE | 21.29 | `ClaudeCodeBeat` | Three aliases print byte-identical; a stop-word query is rejected |
| 9 | B08 | FALSIFIABILITY | 25.34 | `ClaudeCodeBeat` | Miss on `yak shaving trombone`; exit 1; row appended to TEMPLATE-MISSES.md |
| 10 | B09 | VERDICT | 27.16 | `ClaudeVerdictArtifact` | Seven-line surface summary — bare / query / --check / --undocumented / --reel + --no-log / aliases / a miss |
| 11 | B10 | YOUR_TURN | 28.03 | `ClaudeComposerAsk` | "Your turn." with the paste-ready audit script; expected outcomes cascade |
| 12 | B11 | OUTRO | 5.31 | `ClaudeTitleOutro` | Title restate + hardcoded `@NikBearBrown` + slug-seeded mascot |

## Timeline

Total narrated length: **255.08 s** (≈ 4 min 15 s).

Per-beat MP3 durations are the ground truth (`generate_audio_kokoro.py` prints
them at build time). Every scene rendered against those durations via
`remotion_scenes.py`. No beat is padded to a target time.

## Registered compositions used

- `ClaudeComposerAsk` (16:9, `runtime/remotion/src/scenes/ClaudeComposerAsk.tsx`)
- `BrutalistHesitantWriter` (16:9, `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx`)
- `ClaudeCodeBeat` (16:9, `runtime/remotion/src/scenes/ClaudeCodeBeat.tsx`)
- `ClaudeVerdictArtifact` (16:9, `runtime/remotion/src/scenes/ClaudeVerdictArtifact.tsx`)
- `ClaudeTitleOutro` (16:9, `runtime/remotion/src/scenes/ClaudeTitleOutro.tsx`)

All five checked via `./art scenes --check` before authoring. Portrait
companions live under `/vertical` with the `-916` sibling ids, including
`ClaudeCodeBeat916` which was registered natively in this isolated toolkit's
`Root.tsx` (durationInFrames=300, 1080×1920) to satisfy the vertical schema.

## Doctrine bindings honored

- COLD OPEN LAW: B00 is `ClaudeComposerAsk` with real answer lines.
- EXECUTIVE-SUMMARY LAW: B01 is `BrutalistHesitantWriter`; the correction
  `writes → finds, new → existing` is the reel's actual misconception; audio
  ≥ 9 s (12.35 s measured) with `lead_silence_s: 0.8`.
- ILLUSTRATE LAW: the UI appears only in cold open, verdict, your-turn, and
  outro. Inner beats (B02-B08) are `ClaudeCodeBeat` illustrations of real code
  and real terminal output — never composer wallpaper.
- HANDOFF LAW: B10 is `ClaudeComposerAsk` with `greeting: "Your turn."`, a
  concrete paste-ready prompt, and its expected outcomes; narration reads the
  whole prompt.
- OUTRO LAW / OUTRO-LOCK: B11 restates the title verbatim with `@NikBearBrown`
  handle (hardcoded per lock), slug-seeded mascot.
- SPARK-LINE LAW: every inner code beat carries a ≤4-word summary line.
