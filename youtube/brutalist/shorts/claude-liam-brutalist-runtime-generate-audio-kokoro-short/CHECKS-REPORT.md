# CHECKS-REPORT — Brutalist Utility: generate_audio_kokoro.py — Short

Run ID: `bfec6685c4764c0797e6f75c2cb9b7b5`
Date: 2026-09-11

## Duration

| Check | Value | Status |
|-------|-------|--------|
| Planned cut (beat durations) | 91.39 s | PASS |
| Compiler reported | 91.4 s | PASS |
| ffprobe container duration | 91.416667 s | PASS (< 180.0 s) |
| ffprobe video stream | 2160×3840, h264 | PASS |
| ffprobe audio stream | aac | PASS |

## Beats

| Beat | Status | Pattern | Duration |
|------|--------|---------|----------|
| B00 | VIDEO — native portrait reused | ClaudeComposerAsk916 | 15.53 s |
| B01 | VIDEO — native portrait reused | BrutalistHesitantWriter916 | 10.58 s |
| B07 | VIDEO — native portrait reused | ClaudeCodeBeat916 | 27.41 s |
| B09 | VIDEO — native portrait reused | ClaudeVerdictArtifact916 | 31.04 s |
| B11 | VIDEO — native portrait reused | ClaudeTitleOutro916 | 6.83 s |

0 slates. 5/5 filled.

## Cut integrity

- No re-render required (all beats are native 9:16 from parent vertical).
- No ONDA CHECK rewiring (beats already in 916 composition form in parent).
- No outro rewrite (whole-beat cut, transitions coherent).
- No dangling references in retained narration.

## Skin lint (inherited from parent vertical)

- B00: palette=claude but pattern=ClaudeComposerAsk916 — COLD OPEN LAW expects ClaudeComposerAsk. Inherited; not a Short-specific issue.
- B11: palette=claude but pattern=ClaudeTitleOutro916 — OUTRO LAW expects ClaudeTitleOutro. Inherited; not a Short-specific issue.

## Visual QC (frame evidence)

15 beat-relative frames extracted (15%/50%/85% per beat) and contact sheet inspected. See VISUAL-REVIEW.json.

- B00: ClaudeComposerAsk916 — cream ground, "Ahoj, Liam" greeting, ask fully typed, output lines cascade. PASS.
- B01: BrutalistHesitantWriter916 — corrected text "kokoro is / free and / local." fills portrait safe area. PASS.
- B07: ClaudeCodeBeat916 — dry-run fixture code card legible, spark line "2 speak. 4 skip. $0.00." visible. PASS.
- B09: ClaudeVerdictArtifact916 — all 6 verdict lines legible, card fills portrait. PASS.
- B11: ClaudeTitleOutro916 — dark outro, title + @NikBearBrown handle. Title word-wraps as expected for long filename. PASS.

## Output

```
exports/short/claude-liam-brutalist-runtime-generate-audio-kokoro-short.mp4
SHA-256: 70f1fc24ff61cebb0c54988955ef57fa76a2bc334c1343337f6e78839008b117
Size: 5,910,762 bytes
Duration: 91.416667 s
Dimensions: 2160×3840
```

## Gates

| Gate | Result |
|------|--------|
| Duration < 180s | PASS (91.4s) |
| 5 beats filled (0 slates) | PASS |
| Native portrait (no landscape crop) | PASS |
| No burned captions | PASS |
| Parent unchanged | PASS (read-only) |
| No fabricated approvals | PASS |
| No invented URLs | PASS |
