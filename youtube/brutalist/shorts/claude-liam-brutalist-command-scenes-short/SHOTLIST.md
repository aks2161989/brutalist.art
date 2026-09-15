# SHOTLIST — Brutalist Command: art scenes — Short

6 retained beats, all Remotion-native portrait (`*916`) reused unchanged from
the parent's native 2160×3840 vertical companion. No new renders, no captions.

| # | ID | Act | Render s | Pattern (portrait) | On screen |
|---|---|---|---|---|---|
| 1 | B00 | ASK | 18.67 | `ClaudeComposerAsk916` | Greeting "Namaste, Liam"; command types; running text "searching the scene index…"; output cascades (620 renderable compositions · id/synonym/haystack IDF · three aliases share one code path) |
| 2 | B01 | BLUF | 12.38 | `BrutalistHesitantWriter916` | Hesitant serif: "art scenes writes / new scenes." → the words *writes* and *new* correct to *finds* and *existing* — the misconception is that `art scenes` authors a scene; it finds one |
| 3 | B04 | MECHANISM | 27.38 | `ClaudeCodeBeat916` | `scene_search.py` `score()` — id 3× / synonym 2× / haystack 1× (weighted by IDF); derived-only entry loses 0.5; note that a rare word beats a common one |
| 4 | B05 | WORKED_EXAMPLE | 25.96 | `ClaudeCodeBeat916` | Verbatim `./art scenes "sankey flow"` — FinanceSankey wins at 8.5 (rare word, id-hit); three SourceFlow variants tie at 4.5 |
| 5 | B08 | FALSIFIABILITY | 25.38 | `ClaudeCodeBeat916` | Miss on `yak shaving trombone`; exit status 1; punt instruction; row appended to `TEMPLATE-MISSES.md` — a miss is a design card, filed automatically |
| 6 | B11 | OUTRO | 5.33 | `ClaudeTitleOutro916` | Title restate + hardcoded `@NikBearBrown` + slug-seeded mascot |

## Timeline

Total render length: **115.08 s** (1:55.1). Final container/video/audio durations
verified strictly under 180.0 s (see CHECKS-REPORT.md).

Per-beat MP3 durations are the ground truth, unchanged from the parent's build.
Media/audio files were copied independently (never symlinked) via
`runtime/scripts/shorts.py --drop B02 B03 B06 B07 B09 B10 --no-endcard --no-outro-rewrite`.

## Dropped beats (from the 12-beat vertical parent)

- B02 FRAMEWORK — the `art:67-70` case-branch dispatcher walk (belongs in the long).
- B03 MECHANISM — `scenes.json` schema tour (index anatomy belongs in the long).
- B06 WORKED_EXAMPLE — `--check` + `--undocumented` walk (adjacent surfaces belong in the long).
- B07 WORKED_EXAMPLE — alias byte-identity + stop-word guard (second-order after B04+B05).
- B09 VERDICT — seven-line whole-surface catalog (the very catalog the Short brief warns against).
- B10 YOUR_TURN — extended paste-prompt (long-only exercise).

## Registered portrait compositions used

- `ClaudeComposerAsk916` (9:16)
- `BrutalistHesitantWriter916` (9:16)
- `ClaudeCodeBeat916` (9:16)
- `ClaudeTitleOutro916` (9:16)

All four are registered in this toolkit's `runtime/remotion/src/Root.tsx`; the
ONDA CHECK confirmed native portrait media exists for every retained beat and
no re-render was necessary.
