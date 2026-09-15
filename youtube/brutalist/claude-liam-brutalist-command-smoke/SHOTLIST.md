# SHOTLIST.md — Brutalist Command: art smoke

| Beat | Act | Pattern | Duration (s) | On-screen action |
|---|---|---|---|---|
| B00 | ASK | ClaudeComposerAsk | 9.64 | Composer types the ask; runningText 'running ./art smoke…'; three output lines cascade in. |
| B01 | BLUF | BrutalistHesitantWriter | 14.34 (+0.8s lead) | Two-line writer: "art smoke / checks deps." → "art smoke / renders video." Trigger→replacement pairs `checks→renders`, `deps→video`. |
| B02 | FRAMEWORK | ClaudeCodeBeat | 13.97 | Code card of `art:121-123` — the two-line `smoke)` dispatcher case + spark line "One case. No flags. One script." |
| B03 | FRAMEWORK | ClaudeCodeBeat | 33.00 | Code card of smoke_test.sh's pipeline: scratch dir + Kokoro + run.sh + three GATE lines. |
| B04 | MECHANISM | ClaudeCodeBeat | 21.31 | Code card of `examples/_smoke/beat_sheet.json` — literal fixture body. |
| B05 | MECHANISM | ClaudeCodeBeat | 25.54 | Code card of GATE AUDIO block from smoke_test.sh:74-79 + observed reading on this box (`mean_volume: -24.2 dB`). |
| B06 | WORKED_EXAMPLE | ClaudeCodeBeat | 25.37 | Verbatim pass-run output: Kokoro synthesis lines, run.sh compile stanza, three gate readings, SMOKE PASS + exit 0. |
| B07 | FAILURE_RECOVERY | ClaudeCodeBeat | 37.93 | Verbatim shipped-fixture failure output + the offending regex + the two one-line recoveries + the AFTER pass. |
| B08 | VERDICT | ClaudeVerdictArtifact | 27.16 | Artifact card, heading + six verdict lines. |
| B09 | YOUR_TURN | ClaudeComposerAsk | 24.98 | Composer with `greeting: "Your Turn"`, paste-ready 5-step prompt, three grading output lines. |
| B10 | OUTRO | ClaudeTitleOutro | 5.23 | Title restate "Brutalist Command: art smoke." + @NikBearBrown + slug-seeded mascot. |

Total actual duration: 238.47s (11 beats).

## Legibility notes

- All beats stay inside the shared `SAFE` inset (16:9: x 96-1824, y 54-1026;
  9:16: x 40-1040, y 192-1728).
- ClaudeCodeBeat body copy runs on the shipped code-block palette (Onda-style
  ink on cream). No inline color highlighting beyond terracotta accent for
  greetings/spark lines.
- B01 uses BrutalistHesitantWriter's shipped landscape defaults (fontSize 260,
  lineSpacing 2.5, seed `smoke-b01`). Portrait variant reduces fontSize to 210
  and increases lineSpacing to 4.5 per the shipped
  BrutalistHesitantWriter916 recipe.

## Motion

- Every beat is a moving action (typing, cascading, hesitant correction).
  No static-slide beats.
- Beats B02-B07 share the ClaudeCodeBeat pattern but with different content;
  code-cascade motion is what differentiates them.
- Outro follows OUTRO-LOCK: slug-seeded mascot animation on cream.

## Audio

- Every beat: Kokoro engine, voice `am_onyx` (Liam-in-for-Bear).
- B01 has an explicit `lead_silence_s: 0.8` — verified as a 0.8s silent lead
  in the rendered mp3 (see CHECKS-REPORT.md for the measurement).
