# SHOTLIST — Brutalist Command: art doctor — Short

Portrait 9:16 (2160×3840) · 8 kept beats · 140.75 s · Kokoro `am_onyx` ·
Claude palette · @HumanitariansAI folder chip.

Whole-beat cut of the parent vertical companion; every kept beat's native
portrait render is reused unchanged (no re-render, no crop).

| # | Beat | Act | Pattern | Motion | Runtime | Show anchors |
|---|---|---|---|---|---:|---|
| B00 | ASK cold-open composer, "Jambo, Liam" greeting | ASK | ClaudeComposerAsk916 | type-on | 9.54 s | composer in → greeting → ask → runningText → output cascade |
| B01 | BLUF hesitant writer — art doctor / installs deps. → verifies live. | BLUF | BrutalistHesitantWriter916 | hesitant-type | 14.92 s | caret blinks → first line types → installs→verifies swap → deps→live swap → settled |
| B03 | two modes, one FEATURES table (setup:142-150) | FRAMEWORK | ClaudeCodeBeat916 | code-cascade | 22.08 s | card in → bare branch → --install branch → 7 rows → spark |
| B04 | verbatim ready run — 7 rows green, exit 0 | WORKED_EXAMPLE | ClaudeCodeBeat916 | code-cascade | 15.75 s | card in → FEATURE header → 7 ready rows → cost + exit 0 → spark |
| B06 | live-verification, not receipts — kokoro_synth (setup:137) | MECHANISM | ClaudeCodeBeat916 | code-cascade | 23.46 s | card in → kokoro_synth check → smoke summary → top-of-file rationale → spark |
| B08 | failure + recovery — hide the .onnx, red row, exit 1, restore | FAILURE_RECOVERY | ClaudeCodeBeat916 | code-cascade | 27.17 s | card in → BEFORE mv → AFTER red row + exit 1 → RECOVERY → spark |
| B09 | verdict artifact — 6-line surface recap | VERDICT | ClaudeVerdictArtifact916 | artifact-in | 22.67 s | artifact card → heading → six lines cascade |
| B11 | outro — title restate + @NikBearBrown + slug-seeded mascot | OUTRO | ClaudeTitleOutro916 | outro-card | 5.17 s | cream in → title types → handle → mascot animates |

## Dropped for the Short (present in the parent 16:9 and vertical)

- B02 (FRAMEWORK) — dispatcher case source at `art:96-99`.
- B05 (MECHANISM) — bash 3.2 compat trick, `check()` body + `OK_<id>/MISS_<id>` via eval.
- B07 (MECHANISM) — aggregation loop at `setup:156-172` (13 atomics → 7 features).
- B10 (YOUR_TURN) — Claude Code composer with the paste-ready prompt.

See `CUT-PLAN.json` for per-beat reasoning.

## Recurring visual anchors

- Cream page `#FAF9F5` under every beat.
- Warm ink `#3D3929`, terracotta `#D97757` reserved for one accent per beat
  (send button spark, red-turn in the hesitant writer, active traffic-light dot
  on code cards, spark line on the verdict artifact, the terracotta period
  after the title in the outro).
- Folder chip reads `@HumanitariansAI` in the composer beat (B00).
- Outro handle is `@NikBearBrown` per `OUTRO-LOCK.md` — flagged for the
  human reviewer at publication (Short is not published from this run).

## Known portrait limitation (carried from the parent vertical)

Long monospace code lines in the portrait `ClaudeCodeBeat916` beats
(B03/B04/B06/B08) truncate at the card's right edge. Ink stays inside the
card, Gate V passes, and the salient parts of every line (row labels, status
column, hint indentation, verbs) remain legible. Full lines are visible in
the parent 16:9 master and preserved in
`youtube/brutalist/claude-liam-brutalist-command-doctor/demo/RUN-LOG.txt`.
