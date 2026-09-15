# CHECKS-REPORT — Brutalist Utility: audit_review_queue.py — Short

run_id: 51f5933e39e74631bacd3698e3be0613  
Built: 2026-09-13

## Dimensions

| Check | Result |
|---|---|
| Expected | 2160×3840 (9:16) |
| Actual | 2160×3840 ✓ |
| Codec | h264 ✓ |

## Duration

| Measurement | Value | Limit | Status |
|---|---|---|---|
| Container duration | 121.958s | < 180.0s | ✓ PASS |
| Video stream duration | 121.916667s | < 180.0s | ✓ PASS |
| Audio stream duration | 121.958s | < 180.0s | ✓ PASS |
| Timeline planned | ~122.0s | ≤ 175s target | ✓ PASS |

## Beat fill

6/6 beats filled — all VIDEO (no slates).

| Beat | Status | Pattern | Duration |
|---|---|---|---|
| B00 | VIDEO | ClaudeComposerAsk916 (native portrait reused) | 25.2s |
| B01 | VIDEO | BrutalistHesitantWriter916 (native portrait reused) | 19.2s |
| B05 | VIDEO | ClaudeCodeBeat916 (native portrait reused) | 20.5s |
| B07 | VIDEO | ExecutedData916 (native portrait reused) | 22.3s |
| B09 | VIDEO | ClaudeVerdictArtifact916 (native portrait reused) | 28.7s |
| B11 | VIDEO | ClaudeTitleOutro916 (native portrait reused) | 6.0s |

## Skin lint warnings (inherited from parent vertical)

- B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk
- B11: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro

These warnings are pre-existing in the parent vertical beat sheet and are non-blocking for the Short cut. The 916 compositions are the correct portrait variants.

## Audio

All per-beat MP3s present and copied independently from parent vertical/mp3/.  
B11 uses audio_policy: silence (6.0s silent outro — by design).

## Short validation

`short_validation: {status: ready, errors: []}` — no blocked beats, no 916 gaps.

## Liam sign-off

B11 narration: "That was Brutalist Utility: audit_review_queue.py. Liam, in for Bear." ✓

## Visual review

All 6 beats reviewed via frame extraction at 15%/50%/85% per beat plus 2fps uniform sampling.
- B00: ClaudeComposerAsk916 — topic label, segment title, composer card, output lines — clean and legible ✓
- B01: BrutalistHesitantWriter916 — "documents reels for human review." settled text — large serif, clear ✓
- B05: ClaudeCodeBeat916 — stale master mtime comparison code, "Timestamp delta. The design tell." sparkline — legible ✓
- B07: ExecutedData916 — table with 12/12/0 data, note below — legible ✓
- B09: ClaudeVerdictArtifact916 — "Source evidence, not approval" with 3 numbered verdict lines — clear ✓
- B11: ClaudeTitleOutro916 — title wraps "audit_review_queue.py" across 2 lines (inherited from parent, readable) ✓

**Blockers: 0 | Majors: 0**

## Output

`exports/short/claude-liam-brutalist-runtime-audit-review-queue-short.mp4`  
SHA-256: cb0dcf1aba7f8b5416c860f4b1f4e1d35dd5406bf98e8a6f79c0c468caa97ea8
