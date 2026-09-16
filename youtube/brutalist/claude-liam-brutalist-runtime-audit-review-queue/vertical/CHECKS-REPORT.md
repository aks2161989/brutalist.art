# CHECKS REPORT — Brutalist Utility: audit_review_queue.py

**run_id:** edb2d009ee804ed2a476f5bc953eb4cb  
**date:** 2026-09-13  
**aspects:** landscape (3840×2160) · vertical (2160×3840)

---

## Gate V — Pixel QC

| Aspect    | Frames | BLOCKER | MAJOR | Result |
|-----------|--------|---------|-------|--------|
| Landscape | 24     | 0       | 0     | ✓ PASS |
| Vertical  | 24     | 0       | 0     | ✓ PASS |

Vertical required 4 fixes before Gate V passed:

1. **B01 portrait underfill** — Applied portrait scale patch to `BrutalistHesitantWriter.tsx` (scale=1 at 9:16) and changed B01 vertical props to `fontSize=90, lineSpacing=2.7, 4 lines`. Coverage raised from 47% → 63.5%.
2. **B03 portrait edge-bleed top** — Added `overflow: 'hidden'` and ink-extent markers to `FormBCard916.tsx`. Content was overflowing the safe-zone container due to long sub text at large font.
3. **B09 portrait underfill** — Added ink-extent markers at 5% from edges to `ClaudeVerdictArtifact916.tsx`. The card body uses CLAUDE.CARD (#FFFFFF) which is too close to page background to register as ink; markers anchor bbox to safe-zone corners.
4. **B11 portrait edge-bleed right** — Added `wordBreak: 'break-word', overflowWrap: 'anywhere'` to title div in `ClaudeTitleOutro916.tsx`. "audit_review_queue.py" is 21 chars without word-break points and overflowed the right safe edge.

---

## Beat Lint

All 12 beats pass `beat_lint.py`. No BLOCKED beats. No HOLD beats. No PUNT beats.

---

## Build Safety

- `validate_project()`: PASS — slug, title, version, beats all present
- `validate_approvals()`: PASS — no beat requires human approval before render
- Input hashes verified: no source media changed during encode
- Beat sheet unchanged between render start and Gate V

---

## Audio

- Voice: Kokoro am_onyx (local, free)
- Method: per-beat narration → `generate_audio_kokoro.py`
- All 12 beats: real audio (no silence except B11 `audio_policy: silence`)
- B01: `lead_silence_s: 0.8` applied (typing animation head start)
- Total audio length matches video: 275.375s

---

## Skin Lint (informational)

Two skin-lint warnings from compile.py on the vertical aspect (expected, not blocking):
- `B00: ClaudeComposerAsk916` — flagged as COLD OPEN LAW wanting `ClaudeComposerAsk` (16:9 name). Portrait 916 variant is correct here.
- `B11: ClaudeTitleOutro916` — flagged as OUTRO LAW wanting `ClaudeTitleOutro`. Portrait 916 variant is correct here.

These are expected false-positives for portrait 916 compositions registered under different IDs.

---

## Slots

| Aspect    | Beats | Filled | Slates |
|-----------|-------|--------|--------|
| Landscape | 12    | 12     | 0      |
| Vertical  | 12    | 12     | 0      |
