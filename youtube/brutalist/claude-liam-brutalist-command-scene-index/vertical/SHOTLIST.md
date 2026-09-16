# SHOTLIST — vertical (9:16) — Brutalist Command: art scene-index

Portrait companion to [`../SHOTLIST.md`](../SHOTLIST.md). Same 12 beats,
same narration, native 9:16 compositions in `ClaudeComposerAsk916`,
`BrutalistHesitantWriter916`, `ClaudeCodeBeat916`, `ClaudeVerdictArtifact916`,
`ClaudeTitleOutro916`. Not a cropped master.

| # | Beat | Duration | Scene (9:16 variant) | Note |
|---|------|---------:|----------------------|------|
| 0 | ASK | 15.85 s | `ClaudeComposerAsk916` | composer, greeting, running text, output — same layout laws, portrait-native |
| 1 | BLUF | 13.80 s | `BrutalistHesitantWriter916` | 3-line layout · fontSize 155 · lineSpacing 2.9 (portrait BLUF recipe) |
| 2 | FRAMEWORK | 20.03 s | `ClaudeCodeBeat916` | added to Root.tsx as part of this build; code card, cascade in place |
| 3 | MECHANISM | 21.74 s | `ClaudeCodeBeat916` | THE LAW verbatim |
| 4 | MECHANISM | 29.78 s | `ClaudeCodeBeat916` | three passes over Root.tsx |
| 5 | WORKED_EXAMPLE | 22.04 s | `ClaudeCodeBeat916` | verbatim scene-index output |
| 6 | WORKED_EXAMPLE | 29.40 s | `ClaudeCodeBeat916` | documented vs derived record |
| 7 | WORKED_EXAMPLE | 22.21 s | `ClaudeCodeBeat916` | SCENE-DOC-TODO.md head |
| 8 | FALSIFIABILITY | 28.71 s | `ClaudeCodeBeat916` | orphan scene / recovery — long code lines get horizontal clipping in the portrait card (known limitation) |
| 9 | VERDICT | 26.65 s | `ClaudeVerdictArtifact916` | artifact card, 8 lines to lift portrait fill above 55% |
| 10 | YOUR_TURN | 32.45 s | `ClaudeComposerAsk916` | shortened prompt to keep the composer inside portrait safe (see FACTCHECK.md) |
| 11 | OUTRO | 5.59 s | `ClaudeTitleOutro916` | @NikBearBrown locked handle |

## Local scene edits vs the shipped toolkit

- `runtime/remotion/src/Root.tsx` — added a `ClaudeCodeBeat916` Composition
  under `id="ClaudeCodeBeat916"` at 1080×1920 (component is unchanged;
  duration-agnostic, uses `useVideoConfig`).
- `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx` — one-line
  portrait-scale patch documented in FACTCHECK.md.
- Both changes live only inside the isolated toolkit (workspace scratch);
  the shared toolkit is untouched by this run.

## Known portrait limitation (from CHECKS-REPORT.md)

`ClaudeCodeBeat916` does not word-wrap long code lines. B04-B08 code
cards contain some horizontal clipping in portrait. Frame-safe checks
still pass (the card itself lives inside `SAFE916`). Fellows watching the
9:16 cut should prefer the landscape master for reading full script
contents.
