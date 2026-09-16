# SHOTLIST — Brutalist Command: art scene-index

12 beats. All rendered natively as Remotion compositions in the Claude
skin (cream `#FAF9F5`, warm ink `#3D3929`, terracotta `#D97757`). No
captions, no B-roll, no lifted screenshots.

| # | Beat | Duration | Scene | Purpose |
|---|------|---------:|-------|---------|
| 0 | ASK | 15.85 s | `ClaudeComposerAsk` | cold open · Bonjour, Liam · types the ask, output cascades: wraps · writes · law |
| 1 | BLUF | 13.80 s | `BrutalistHesitantWriter` | executive summary · types "art scene-index reads / the scenes." · corrects to "rewrites / the index." |
| 2 | FRAMEWORK | 20.03 s | `ClaudeCodeBeat` | the dispatcher case at art:71-74 · one branch, no aliases, --todo baked in |
| 3 | MECHANISM | 21.74 s | `ClaudeCodeBeat` | THE LAW quoted verbatim from build_scene_index.py · registered is the only truth |
| 4 | MECHANISM | 29.78 s | `ClaudeCodeBeat` | three passes: import map → composition scan → header extraction / derived fallback |
| 5 | WORKED_EXAMPLE | 22.04 s | `ClaudeCodeBeat` | verbatim `./art scene-index` output: 619 · 118 · 0; ls of the two files it wrote |
| 6 | WORKED_EXAMPLE | 29.40 s | `ClaudeCodeBeat` | scenes.json entry: HEADER-BACKED (ClaudeComposerAsk) vs DERIVED (CodexComposerAsk) |
| 7 | WORKED_EXAMPLE | 22.21 s | `ClaudeCodeBeat` | SCENE-DOC-TODO.md head, verbatim: 5 rows + placeholder for 113 more |
| 8 | FALSIFIABILITY | 28.71 s | `ClaudeCodeBeat` | the orphan scene · two .tsx, one Composition → 1 renderable · RECOVERY → 2 renderable |
| 9 | VERDICT | 26.65 s | `ClaudeVerdictArtifact` | six-line surface artifact card |
| 10 | YOUR_TURN | 32.45 s | `ClaudeComposerAsk` | greeting "Your turn." + paste-into-Claude 4-step audit prompt |
| 11 | OUTRO | 5.59 s | `ClaudeTitleOutro` | title restate · @NikBearBrown (locked handle per OUTRO-LOCK.md) · slug-seeded mascot |

## Motion budget

- `ClaudeComposerAsk` type-on: B00, B10 (2 beats).
- `BrutalistHesitantWriter` hesitant-type: B01 (1 beat).
- `ClaudeCodeBeat` code-cascade: B02, B03, B04, B05, B06, B07, B08 (7 beats).
- `ClaudeVerdictArtifact` artifact-in: B09 (1 beat).
- `ClaudeTitleOutro` outro-card: B11 (1 beat).

Code-cascade is 7 of 12 = 58%, over MOTION.md's ~40% pantry cap for a
general-purpose reel. The command's evidence IS the tool's source and its
observed output; per ILLUSTRATE LAW the honest illustration is code, not
a decorative mechanic. Documented, not "fixed" by swapping in animation
that would misrepresent the tool. Same trade-off as the scenes episode.

## Sound

Kokoro `am_onyx` (Liam, in for Bear) on all 12 beats. B01 carries an
`lead_silence_s: 0.8` so the hesitant writer's initial typing has room
to breathe before the narration lands. Actual per-beat MP3 durations
were used as the master clock; compile.py conforms every clip to the
measured audio.

## Frame safety

All beats respect the 5% title-safe inset. B01's serif line is sized
`fontSize=170` (dropped from an initial 260 → 200 → 170 after visual
review — the compound word "scene-index" needs the room). All code cards
render at the ClaudeCodeBeat container's shipped 86% width; no line
overflow in landscape. Verdict card sits inside `SAFE`.
