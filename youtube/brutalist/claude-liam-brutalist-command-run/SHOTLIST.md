# SHOTLIST — Brutalist Command: art run

| Beat | Pattern | Duration (est.) | Visual |
|---|---|---:|---|
| B00 | ClaudeComposerAsk | 24 s | Ciao greeting, ask types, three output lines cascade. |
| B01 | BrutalistHesitantWriter | ≥20 s | `art run renders / a master.` → correction → `art run compiles / a review.` |
| B02 | ClaudeCodeBeat | 18 s | Dispatcher case at `art:99-101` — three lines of shell. |
| B03 | ClaudeCodeBeat | 40 s | Full gate order: F → L → SHAPE → A → W → render + B → Remotion → compile → V. |
| B04 | ClaudeCodeBeat | 26 s | Audio-first + slot-skip: mp3 → clip retime, and the `run.sh` skip loop. |
| B05 | ClaudeCodeBeat | 22 s | Verbatim Gate F failure output against `/tmp/claude-501/art-run-demo/`. |
| B06 | ClaudeCodeBeat | 24 s | The four knobs: `ART_QC`, `ART_STRICT`, `ART_FACTS`, `--height`. |
| B07 | ClaudeCodeBeat | 28 s | `run` vs `final`: two verbs, two files, receipt is the difference. |
| B08 | ClaudeCodeBeat | 30 s | Same reel, paperwork added → Gate F/L/SHAPE pass, Remotion is next stage. |
| B09 | ClaudeVerdictArtifact | 34 s | 8-line surface artifact. |
| B10 | ClaudeComposerAsk (Your Turn) | 32 s | Paste-ready 4-step iteration prompt for a real reel. |
| B11 | ClaudeTitleOutro | 6 s | Title restate + `@NikBearBrown` (OUTRO-LOCK). |

All Remotion beats fill from live registered scenes in the isolated
toolkit's `runtime/remotion/src/Root.tsx`; `ClaudeCodeBeat916` was
registered as part of this build (see `scene-source-manifest.json`).

## Motion histogram (planned)

```
code-cascade: 7   type-on: 2   hesitant-type: 1   artifact-in: 1   outro-card: 1
```

Same shape as `command-scene-index` (58% code-cascade). The command's
evidence IS its dispatcher, its `run.sh` source, and its observed output
— per ILLUSTRATE LAW the honest illustration is code, not a decorative
pattern grafted on to hit the ~40% pantry cap. Documented, kept.

## Fill plan

1. `generate_audio_kokoro.py` for every beat (Kokoro `am_onyx`).
2. `remotion_scenes.py` fills every Remotion pattern.
3. `compile.py --review --height 2160 --out exports/landscape` for
   landscape; `compile.py --review --height 3840 --out exports/vertical`
   for the portrait sibling in `vertical/`.
