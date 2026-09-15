# SHOTLIST — Brutalist Command: art icons (vertical / 9:16)

Portrait companion to the landscape master. 12 beats · same narration · same audio ·
native 1080×1920 compositions (upsampled to 2160×3840 at compile).

| # | Beat | Portrait scene | Duration | Notes |
|---|---|---|---|---|
| B00 | ASK — cold open | `ClaudeComposerAsk916` | ~16 s | Greeting "Sawubona, Liam"; ask + result lines. Portrait composer layout. |
| B01 | BLUF — hesitant writer | `BrutalistHesitantWriter916` | ~12 s | Stacked lines "art icons / draws / new icons" → "art icons / finds / existing icons". fontSize 220, lineSpacing 2.5 (portrait BLUF recipe). |
| B02 | FRAMEWORK — dispatcher | `ClaudeCodeBeat916` | ~15 s | Same code content; portrait code-card layout. |
| B03 | MECHANISM — the set | `ClaudeCodeBeat916` | ~18 s | icons.json header + two sample records. |
| B04 | MECHANISM — the ranker | `ClaudeCodeBeat916` | ~19 s | Four ranking rules + IDF one-liner. |
| B05 | WORKED EXAMPLE — "money" | `ClaudeCodeBeat916` | ~17 s | Verbatim `./art icons "money"` output. |
| B06 | WORKED EXAMPLE — check/show | `ClaudeCodeBeat916` | ~17 s | `--check` three-name run + `--show database`. |
| B07 | WORKED EXAMPLE — brands filter | `ClaudeCodeBeat916` | ~19 s | `--brands` narrows corpus; `--no-brands` inverse. |
| B08 | FALSIFIABILITY — the miss | `ClaudeCodeBeat916` | ~18 s | "quantum entanglement" → no match, exit 0. |
| B09 | VERDICT — the surface | `ClaudeVerdictArtifact916` | ~20 s | 7 lines: bare / query / --check / --show / --brands / aliases / miss. |
| B10 | YOUR TURN | `ClaudeComposerAsk916` | ~23 s | Paste-ready audit prompt for Claude Code. |
| B11 | OUTRO — title restate | `ClaudeTitleOutro916` | ~6 s | "Brutalist Command: art icons."; hardcoded `@NikBearBrown`. |

## What changes from the landscape

- Every scene is a native portrait composition registered in Root.tsx at
  `1080×1920` — nothing is cropped from a landscape master.
- `ClaudeCodeBeat916` was added in this episode's isolated toolkit Root.tsx
  (same component, portrait wrapper). It reflows around a taller,
  narrower code card.
- `BrutalistHesitantWriter916` bumps line spacing to 2.5 per the portrait
  BLUF recipe (lineSpacing, not fontSize, is what lifts ink coverage past
  55% on 9:16).
- The remaining paperwork (FACTCHECK, PROMPTS, SOURCES) is shared with
  the landscape master; no fact changes between aspects.

## Portrait-specific caveats

- **Skin warnings** (from compile): `ClaudeComposerAsk916` and
  `ClaudeTitleOutro916` are correct portrait variants of the required
  scenes; the compiler's simple string match warns because it wants
  "ClaudeComposerAsk" / "ClaudeTitleOutro" verbatim. Confirmed acceptable —
  same pattern the help-command portrait cut carried.
