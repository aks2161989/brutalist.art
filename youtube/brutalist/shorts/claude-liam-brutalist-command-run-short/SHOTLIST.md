# SHOTLIST — Brutalist Command: art run (Short cut)

Derivative of the 12-beat native portrait parent
(`youtube/brutalist/claude-liam-brutalist-command-run/vertical`).
Six whole beats retained; six dropped (see `CUT-PLAN.json`). Native
2160×3840; no crops, no re-renders, no captions.

| Beat | Pattern (916) | Rendered dur. | Visual |
|---|---|---:|---|
| B00 | ClaudeComposerAsk916 | 17.46 s | Ciao / Liam composer; ask cascades; three output lines (wraps run.sh, writes slate, not the final). |
| B01 | BrutalistHesitantWriter916 | 17.25 s | `art run renders / the master video file.` → hesitates, backspaces `renders`→`compiles`, `master`→`review`. |
| B03 | ClaudeCodeBeat916 | 33.21 s | `run.sh` gate order F · L · SHAPE · A · W · B · Remotion · compile · V — any gate stops the build. |
| B07 | ClaudeCodeBeat916 | 23.13 s | run vs final — two verbs, two files. `<slug>-slate.mp4` (review, no receipt) vs `<slug>.mp4` (verified master). |
| B10 | ClaudeComposerAsk916 (Your Turn) | 22.29 s | Paste-ready 4-step iteration prompt. |
| B11 | ClaudeTitleOutro916 | 5.25 s | "Brutalist Command: art run." · `@NikBearBrown` (OUTRO-LOCK). |

Total measured video: 118.54 s (audio 118.58 s, container 118.58 s) —
strictly under the 180 s Shorts cap.

## Dropped from the long

| Beat | Pattern | Rendered dur. | Why cut |
|---|---|---:|---|
| B02 | ClaudeCodeBeat916 | 15.88 s | Dispatcher case walkthrough — code-level detail for the 16:9 long. |
| B04 | ClaudeCodeBeat916 | 22.38 s | Audio-first clock + slot-skip mechanism — iteration detail, not a high-level surface. |
| B05 | ClaudeCodeBeat916 | 16.29 s | Verbatim Gate F failure demo — B07's run-vs-final is the essential distinction. |
| B06 | ClaudeCodeBeat916 | 21.79 s | Four env knobs (`ART_QC` / `ART_STRICT` / `ART_FACTS` / `--height`) — advanced usage. |
| B08 | ClaudeCodeBeat916 | 21.96 s | Recovery demo depends on the B05 setup we cut. |
| B09 | ClaudeVerdictArtifact916 | 28.71 s | 8-line verdict restates content of B03/B07/B10 — redundant once mid-body is removed. |

## Motion histogram (measured, Short cut)

```
type-on: 2   code-cascade: 2   hesitant-type: 1   outro-card: 1
```

## Reformat

Native portrait footage reused unchanged for every beat (shorts.py
`native portrait reused unchanged` for B00, B01, B03, B07, B10, B11).
No center-cut, no re-render, no endcard, no outro rewrite.
