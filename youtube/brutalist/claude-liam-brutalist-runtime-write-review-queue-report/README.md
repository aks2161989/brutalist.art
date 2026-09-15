# Brutalist Utility: write_review_queue_report.py

**Channel:** @HumanitariansAI  
**Persona:** Liam, in for Bear  
**Run ID:** `aef36acf6a354924acd1af29d9d319cf`  
**Source:** `runtime/scripts/write_review_queue_report.py`  
**Source SHA-256:** `8de57eb1bb0e4f1345c7a7e26ad99365969eda321c3a7fc81d897867e50d904d`

---

## Deliverables

| Aspect    | File                                                             | Duration | Dimensions  |
|-----------|------------------------------------------------------------------|----------|-------------|
| Landscape | `exports/landscape/claude-liam-brutalist-runtime-write-review-queue-report.mp4` | 222.5s | 3840×2160 |
| Vertical  | `exports/vertical/claude-liam-brutalist-runtime-write-review-queue-report-vertical.mp4` | 222.5s | 2160×3840 |

Both masters: 12 beats, 0 slates, Gate V clean (BLOCKER=0, MAJOR=0).

---

## What This Episode Covers

`write_review_queue_report.py` is the last step in the Brutalist audit chain. It reads two JSON files — `audit.json` (machine-measured data) and `review-notes.json` (visual findings) — and writes `AUDIT.md` without touching any reel. The script is read-only by design; the docstring says it plain: never mutate reels.

Beat map:
- B00 ASK — greeting and context
- B01 BLUF — type-on hesitant writer: the script formats, not audits
- B02 FRAMEWORK — two-input, one-output pipeline
- B03 MECHANISM — reading inputs, JSON schema contract
- B04 MECHANISM — main loop, reel section structure
- B05 MECHANISM — pantry flag scanner, three legacy spellings
- B06 OUTPUT — AUDIT.md hardcoded structure
- B07 FAILURE — crash contract, no try-except
- B08 LIMITS — what the report cannot certify
- B09 VERDICT — 3-point artifact card
- B10 HANDOFF — Your Turn prompt for the viewer
- B11 OUTRO — Liam in for Bear, @HumanitariansAI

---

## Toolkit Fixes Applied This Build

1. `BrutalistHesitantWriter.tsx` — portrait scale formula: `Math.min(w/1920,h/1080)` collapses to 0.5625 on 9:16 canvas; fixed to `height>width ? Math.min(w/1080,h/1920) : Math.min(w/1920,h/1080)`
2. `ClaudeVerdictArtifact916.tsx` — ink anchors at `top:5.5%` / `bottom:7%` added for Gate V fill check (centered card alone gives <55% coverage)
3. `ClaudeComposerAsk.tsx` — `right: PAD_X` and `wordBreak:'break-word'` added to segment and topic divs; missing right constraint caused 44px right-edge bleed in portrait
4. `Root.tsx` — `SkillTeardownMechanism916` portrait composition alias registered (1080×1920)
5. B01 portrait text redesigned: 6 shorter lines at fontSize=120 to fit within safe area and achieve ≥55% coverage

---

## Status

Gate V: PASS (both aspects)  
Slates: 0  
Bear review required before publication.
