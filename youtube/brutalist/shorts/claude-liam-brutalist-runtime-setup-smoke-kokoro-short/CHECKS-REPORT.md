# CHECKS-REPORT — Brutalist Utility: setup_smoke_kokoro.py — Short

## Run information

**Run ID:** `7a78e158da124455b3fd947396bd80bc`  
**Rendered:** 2026-09-14  
**Strategy:** whole-beat-cut  
**Beats kept:** 6/11 (B00, B01, B06, B08, B09, B10)  
**Beats dropped:** B02, B03, B04, B05, B07

## Beat classification

| Beat | Class | Scene | Kept/Dropped | Reason |
|---|---|---|---|---|
| B00 | SHOW | ClaudeComposerAsk916 | KEPT | Cold open — Liam intro + core question |
| B01 | SHOW | BrutalistHesitantWriter916 | KEPT | BLUF — misconception correction (import→synthesis) |
| B02 | SHOW | ClaudeCodeBeat916 | DROPPED | Framework pipeline — concept already in B00 narration |
| B03 | SHOW | ClaudeCodeBeat916 | DROPPED | Guard code detail — long-form only |
| B04 | SHOW | ClaudeCodeBeat916 | DROPPED | Synthesis code detail — long-form only |
| B05 | SHOW | ClaudeCodeBeat916 | DROPPED | Volume gate code detail — long-form only |
| B06 | SHOW | ClaudeCodeBeat916 | KEPT | Failure messages — highly practical, actionable |
| B07 | SHOW | ClaudeCodeBeat916 | DROPPED | Design tell (try/finally) — interesting but not essential |
| B08 | SHOW | ClaudeVerdictArtifact916 | KEPT | Verdict — clean summary of the gate |
| B09 | SHOW | ClaudeComposerAsk916 | KEPT | Your turn — paste-ready handoff prompt |
| B10 | SHOW | ClaudeTitleOutroHAI916 | KEPT | Outro — title + "Liam, in for Bear." |

## Narrative coherence check

- **B00→B01**: Clean. B00 asks "why synthesize?" B01 delivers the BLUF answer with hesitant-writer correction.
- **B01→B06**: Works. B01 closes on "not whether the code runs, but whether it makes sound." B06 opens on the five failure paths — what the gate actually catches. B00 already named the five-check structure so no dangling reference.
- **B06→B08**: Clean. B06 closes noting setup reads exit code only. B08 verdict restates the gap ("Kokoro is installed" vs "Kokoro makes sound") — callbacks to B00/B01 work without the intervening code beats.
- **B08→B09**: Clean. Verdict → handoff is standard pattern.
- **B09→B10**: Clean. Your turn → outro sign-off.

## Duration check

| Measurement | Value |
|---|---|
| Planned (beat sheet) | 107.5s |
| Container duration | 107.5s |
| Video stream duration | 107.5s |
| Audio stream duration | 107.5s |
| Cap | 180.0s (strictly under) |
| Headroom | 72.5s |

## Dimension check

- **Declared:** 2160×3840 (9:16)
- **Measured:** 2160×3840 ✓

## Gate V

- **BLOCKER:** 0
- **MAJOR:** 0
- **Frames sampled:** 12
- **Report:** `_qc/REPORT.md`

## Short export

`exports/short/claude-liam-brutalist-runtime-setup-smoke-kokoro-short.mp4`  
SHA-256: `60e385c546f7f97c93bcd51d0d89a02b01d1ede6a61fbe7dcc3c7d8f44e20677`

## Known skin lint

- B00: `ClaudeComposerAsk916` vs COLD OPEN LAW — intentional (portrait variant)
- B10: `ClaudeTitleOutroHAI916` vs OUTRO LAW — intentional (HAI-locked component)

## Human review required

Visual QC frames in `_qc/`. Contact sheet and export files must be reviewed by a human before publication. No fabricated approvals.
