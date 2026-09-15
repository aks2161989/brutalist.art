# SHOTLIST — Brutalist Command: art doctor

Landscape 16:9 · 12 beats · Kokoro `am_onyx` · Claude palette · @HumanitariansAI folder chip.

| # | Beat | Act | Pattern | Motion | Runtime | Show anchors |
|---|---|---|---|---|---:|---|
| B00 | ASK cold-open composer, "Jambo, Liam" greeting | ASK | ClaudeComposerAsk | type-on | audio-driven | composer in → greeting → ask → runningText → output cascade |
| B01 | BLUF hesitant writer — art doctor / installs deps. → verifies live. | BLUF | BrutalistHesitantWriter | hesitant-type | audio-driven (≥9s) | caret blinks → first line types → installs→verifies swap → deps→live swap → settled |
| B02 | dispatcher case at art:96-99 | FRAMEWORK | ClaudeCodeBeat | code-cascade | audio-driven | card in → `case "$cmd" in` → `doctor)` → exec line → spark |
| B03 | two modes, one FEATURES table (setup:142-150) | FRAMEWORK | ClaudeCodeBeat | code-cascade | audio-driven | card in → bare branch → --install branch → 7 rows → spark |
| B04 | verbatim ready run — 7 rows green, exit 0 | WORKED_EXAMPLE | ClaudeCodeBeat | code-cascade | audio-driven | card in → FEATURE header → 7 ready rows → cost + exit 0 → spark |
| B05 | bash 3.2 compat — check() + OK_/MISS_ (setup:117-140) | MECHANISM | ClaudeCodeBeat | code-cascade | audio-driven | card in → comment → check() body → two examples → spark |
| B06 | live-verification, not receipts — kokoro_synth (setup:137) | MECHANISM | ClaudeCodeBeat | code-cascade | audio-driven | card in → kokoro_synth check → smoke summary → top-of-file rationale → spark |
| B07 | aggregation loop (setup:156-172) — 13 atomics → 7 features | MECHANISM | ClaudeCodeBeat | code-cascade | audio-driven | card in → loop body → example red row → spark |
| B08 | failure + recovery — hide the .onnx, red row, exit 1, restore | FAILURE_RECOVERY | ClaudeCodeBeat | code-cascade | audio-driven | card in → BEFORE mv → AFTER red row + exit 1 → RECOVERY → spark |
| B09 | verdict artifact — 6-line surface recap | VERDICT | ClaudeVerdictArtifact | artifact-in | audio-driven | artifact card → heading → six lines cascade |
| B10 | Your Turn composer — "read art doctor without installing" | YOUR_TURN | ClaudeComposerAsk | type-on | audio-driven | composer in → Your Turn → typed prompt → runningText → grading lines |
| B11 | outro — title restate + @NikBearBrown + slug-seeded mascot | OUTRO | ClaudeTitleOutro | outro-card | audio-driven | cream in → title types → handle → mascot animates |

## Recurring visual anchors

- Cream page `#FAF9F5` under every beat.
- Warm ink `#3D3929`, terracotta `#D97757` reserved for one accent per beat
  (send button spark, red-turn in the hesitant writer, active traffic-light dot
  on code cards, spark line on the verdict artifact, the terracotta period
  after the title in the outro).
- Folder chip reads `@HumanitariansAI` in every composer beat (B00, B10).
- Outro handle is `@NikBearBrown` per `OUTRO-LOCK.md` — flagged in `README.md`.
