# Brutalist Utility: audit_review_queue.py

**Channel:** @HumanitariansAI · **Playlist:** Brutalist  
**Voice:** Liam, in for Bear (Kokoro am_onyx)  
**run_id:** edb2d009ee804ed2a476f5bc953eb4cb  
**Date:** 2026-09-13

---

## What this episode covers

`audit_review_queue.py` is the read-only batch inspector for Brutalist reels. It reads a list of reel IDs from a text file, runs four pipeline checks on each (beat sheet hash, master MP4 probe, math layout check, and frame sampling), and writes a numbered JSON report per reel plus a rolled-up `audit.json`. It does not modify any reel files — it only reads and reports.

Teaching arc: FRAMEWORK → WORKED EXAMPLE → FALSIFIABILITY → SCAFFOLDED TASK

12 beats. 275.4 seconds.

---

## Exports

| Aspect    | File | Resolution | Duration |
|-----------|------|------------|---------|
| Landscape | `exports/landscape/claude-liam-brutalist-runtime-audit-review-queue.mp4` | 3840×2160 | 275.4s |
| Vertical  | `exports/vertical/claude-liam-brutalist-runtime-audit-review-queue-vertical.mp4` | 2160×3840 | 275.4s |

SHA-256:
- Landscape: `1f52ded1f929a35bffa27e98ac290b201e5f63d83899dab5b2f60903e837cff1`
- Vertical: `a6c0604570d25bed4a14f35f2c8cb0f3644704ac0ba338bab579340d60b29348`

---

## QC Status

| Gate | Landscape | Vertical |
|------|-----------|---------|
| Gate V (pixel) | ✓ 0/0 BLOCKER/MAJOR | ✓ 0/0 BLOCKER/MAJOR |
| Slots | ✓ 12/12 filled | ✓ 12/12 filled |
| Slates | ✓ 0 | ✓ 0 |

---

## Paperwork

- `SCRIPT.md` — full narration all 12 beats
- `SOURCES.md` — source code SHA-256 and demo run provenance
- `FACTCHECK.md` — every narration claim verified against source line numbers
- `SHOTLIST.md` — 12 SHOW beats, 0 HOLD, 0 PUNT
- `PROMPTS.md` — paste-ready Your Turn prompt and demo command
- `CHECKS-REPORT.md` — Gate V results and build log
- `TYPECHECK.md` — TypeScript and Python pipeline status
- `VISUAL-REVIEW.json` — frame hashes for both aspects

---

## Toolkit fixes shipped with this episode

1. **BrutalistHesitantWriter portrait scale patch** — `scene/BrutalistHesitantWriter.tsx`: `scale = height > width ? min(w/1080,h/1920) : min(w/1920,h/1080)` — fixes 9:16 BLUF underfill (documented in [[feedback-brutalist-hesitant-writer-portrait-scale-patch]])
2. **FormBCard916 overflow clamp** — `overflow: hidden` + ink markers prevent safe-zone bleed when item count × font height exceeds container
3. **ClaudeVerdictArtifact916 ink markers** — thin bars at 5% from edges force bbox to span safe zone on portrait
4. **ClaudeTitleOutro916 word-break** — `wordBreak: break-word, overflowWrap: anywhere` on title — fixes long filenames with underscores overflowing portrait right edge
5. **ClaudeCodeBeat adaptive font** — `min(base, height/lines, width/longest-line)` sizing — fixes code card horizontal overflow on portrait

---

**Next:** Bear's review before publishing to @HumanitariansAI.
