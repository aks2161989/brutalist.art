# SHOTLIST — Brutalist Command: art icons

12 beats · Kokoro `am_onyx` · Claude fidelity palette · @HumanitariansAI folder chip · @NikBearBrown outro (locked)

| # | Beat | Scene / pattern | Duration | Notes |
|---|---|---|---|---|
| B00 | ASK — cold open | `ClaudeComposerAsk` | ~16 s | Greeting "Sawubona, Liam"; ask + result lines (7,330 · IDF · aliases). Introduces Liam in for Bear. |
| B01 | BLUF — hesitant writer | `BrutalistHesitantWriter` | ~12 s | Corrects "draws / new" → "finds / existing". Seeded `command-icons-b01`. |
| B02 | FRAMEWORK — dispatcher | `ClaudeCodeBeat` | ~15 s | Real bash `case` block from `art:60-63`: `icons\|icon\|icon-search` → `exec` icon_search.py. |
| B03 | MECHANISM — the set | `ClaudeCodeBeat` | ~18 s | `icons.json` header: 7,330 icons, 24-unit viewBox, stroke 2, currentColor. Two sample records. |
| B04 | MECHANISM — the ranker | `ClaudeCodeBeat` | ~19 s | Four ranking rules; IDF one-liner from `icon_search.py:62`; two worked examples. |
| B05 | WORKED EXAMPLE — "money" | `ClaudeCodeBeat` | ~17 s | Verbatim stdout: 31 hits, top 10 from live capture. |
| B06 | WORKED EXAMPLE — check/show | `ClaudeCodeBeat` | ~17 s | `--check` three-name run (2 in set, 1 miss); `--show database` prints the raw SVG. |
| B07 | WORKED EXAMPLE — brands filter | `ClaudeCodeBeat` | ~19 s | `--brands` narrows corpus to 376 logos; `--no-brands` narrows to 6,954 concepts. |
| B08 | FALSIFIABILITY — the miss | `ClaudeCodeBeat` | ~18 s | "quantum entanglement" → no match, exit 0, explicit anti-redraw instruction. |
| B09 | VERDICT — the four moves | `ClaudeVerdictArtifact` | ~18 s | bare / query / --check / --show / --brands. One line each. |
| B10 | YOUR TURN | `ClaudeComposerAsk` | ~23 s | Paste-ready audit prompt: nine runs + alias diff + one own concept. |
| B11 | OUTRO — title restate | `ClaudeTitleOutro` | ~6 s | "Brutalist Command: art icons."; hardcoded `@NikBearBrown` (OUTRO-LOCK); slug-seeded mascot. |

## Visual language

- **Palette**: Claude fidelity — cream page `#FAF9F5`, warm ink `#3D3929`, terracotta spark `#D97757`. One terracotta moment per beat.
- **Type**: EB Garamond (serif) for greetings + segment titles; UI sans for chrome; SF Mono for terminal/code lines.
- **Folder chip**: `@HumanitariansAI` on the composer beats (B00, B10).
- **Outro handle**: `@NikBearBrown` — locked constant per `OUTRO-LOCK.md`. Slug-seeded polarity, mascot, and jingle.
- **Motion**: type-on for composer/hesitant beats; code-cascade for ClaudeCodeBeat; artifact-in for the verdict.

## ILLUSTRATE LAW compliance

Claude UI appears only where the UI is the subject:
- B00 — cold-open ASK (the UI is the interface being introduced)
- B10 — HANDOFF ASK (the composer is the paste target)
- B11 — OUTRO title card
- Every other beat (B01–B09) illustrates the concept: hesitant writer (B01), and code cards for the dispatcher, index, ranker, worked examples, and miss (B02–B09).

## SPARK-LINE LAW compliance

Each ClaudeCodeBeat carries a short serif spark line under the card:
- B02: "Three words. One script. One index."
- B03: "One viewBox. One stroke. One color hook."
- B04: "Exact > all-words > prefix > token. Rare wins."
- B05: "31 hits. Top of the ranking, in order."
- B06: "--check answers. --show hands you the SVG."
- B07: "--brands: 376 logos. --no-brands: 6,954 concepts."
- B08: "A miss is the answer. Not a licence to draw."
