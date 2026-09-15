# SHOTLIST — Brutalist Command: art shorts

Twelve beats. Landscape 3840×2160, Kokoro `am_onyx`, ~296s total measured audio.
All shots are Remotion — no Manim, no captured media, no captions.

| # | Beat | Pattern | Duration (audio) | Purpose |
|---|------|---------|------------------|---------|
| 1 | B00 ASK | ClaudeComposerAsk | 19.18s | Cold open — Liam intro; ask lands answered |
| 2 | B01 BLUF | BrutalistHesitantWriter | 21.16s | Hesitant BLUF corrects "speeds up + crops" → "drops + rewires" |
| 3 | B02 FRAMEWORK | ClaudeCodeBeat | 17.43s | Dispatcher cases: art:81-83 shorts / art:84-86 vertical |
| 4 | B03 MECHANISM | ClaudeCodeBeat | 25.24s | THE SHORTS LAW verbatim (5 rules) from module docstring |
| 5 | B04 MECHANISM | ClaudeCodeBeat | 25.69s | plan_drops greedy algorithm; budget = 180 - 5 - end_s |
| 6 | B05 MECHANISM | ClaudeCodeBeat | 37.78s | THE ONDA CHECK: is_remotion / portrait_pattern / rewire-or-block |
| 7 | B06 MECHANISM | ClaudeCodeBeat | 29.97s | Precedence per kept beat: pantry → ONDA → hand-made -916 → center-cut |
| 8 | B07 WORKED_EXAMPLE | ClaudeCodeBeat | 25.62s | Real fixture log: 7 beats · 214s → drops B02 · 163.5s OK |
| 9 | B08 FALSIFIABILITY | ClaudeCodeBeat | 29.59s | Failure + recovery: --vertical --drop REFUSED; two verbs, two contracts |
| 10 | B09 VERDICT | ClaudeVerdictArtifact | 28.12s | 8-line surface summary |
| 11 | B10 YOUR_TURN | ClaudeComposerAsk (Your Turn) | 31.02s | Paste-ready Claude Code prompt read aloud |
| 12 | B11 OUTRO | ClaudeTitleOutro | 5.27s | Title restate + @NikBearBrown mascot (OUTRO-LOCK) |

## Shot-level notes

- **B00 cold open** — folderLabel chip reads `@HumanitariansAI` (playlist
  adaptation). Composer output lines call out `python3 runtime/scripts/shorts.py`,
  the derivative directory path, and the editorial law in one sentence.
- **B01 hesitant** — `fontSize: 240 / lineSpacing: 2.5` on landscape hits the
  Gate V ≥55% floor with 2 short lines. Seed `command-shorts-b01` is unique
  to this reel. `triggerWords: "speeds, crops"` are single tokens per the
  hesitant-writer trigger syntax rule; the replacement text stays grammatical.
- **B02 → B08** — every code beat is ClaudeCodeBeat with `title` acting as the
  Finder-style filename in the traffic-light bar, `code` as a newline-joined
  string (not a lines array), and `sparkLine` at the bottom in italic.
- **B05 ONDA CHECK** is the longest body beat at 37.78s and is deliberately
  code-heavy — three Python fragments (`is_remotion`, `portrait_pattern`,
  rewire branch) show the check's actual shape.
- **B07 worked example** shows the fixture's stdout verbatim; `[short] over
  the cap → auto-plan drops 1 beat(s): B02` and `~163.5s (2:43.5) OK` are the
  key lines that pay off B04's algorithm explanation.
- **B08 failure** — verbatim stderr `[short] REFUSED: --vertical preserves
  the full film; --drop is not allowed`, then the two recovery invocations
  (`--drop` alone, or `art vertical` alone).
- **B09 verdict** — 8 lines exactly, one per structural claim.
- **B10 Your Turn** — composer with `greeting: "Your Turn"` per handoff law.
  Prompt read aloud verbatim; the 4 output lines summarize the expected
  behavior after each step of the prompt.
- **B11 outro** — locked `ClaudeTitleOutro` with hardcoded `@NikBearBrown`
  handle (per `OUTRO-LOCK.md`); channel adaptation to `@HumanitariansAI` is
  flagged for the human reviewer.

## Compile

- `python3 runtime/scripts/compile.py <reel> --height 2160 --out exports/landscape`
- Vertical (portrait) compiled from a native 9:16 beat sheet under
  `<reel>/vertical/beat_sheet.json` via
  `compile.py --height 3840 --out exports/vertical`.
