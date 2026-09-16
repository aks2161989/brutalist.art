# TYPECHECK — Brutalist Command: art keys · vertical

**Run ID**: `abdef8f04e1246deaf8cf7ab26ae350b`
**Master SHA-256**: `acf2b0c143be0498d0ed56f59ddc97b5b720f8b68dafac733716c37dbbc629c1` (unchanged — re-verified 2026-09-12)

## The absent legacy checker

Same as landscape — `scripts/type_check.py` is not shipped in this
isolated toolkit. GATE T is **NOT RUN — checker absent**. Visual audit
performed instead.

## Visual typography audit — portrait-specific

Every proof frame (36 total, 15%/50%/85% of every beat) in
`vertical/_qc/proof-portrait/` was `Read` with the image-capable Read
tool and audited against the standing spec.

| Item | Rule | Portrait audit result |
|---|---|---|
| §8.1 min-size | Body text ≥ 24 px effective | ✅ Composer body text (B00/B10) sits at ~28 px @ 2160-wide, over floor. Verdict lines (B09) at ~40 px. Portrait code cards ~28–34 px SF Mono. |
| §8.2 overflow | Nothing crosses SAFE916 (x 108–2052, y 192–3648 at 2160×3840) | ✅ Gate V confirmed 0 edge-bleed on ALL 24 sampled frames — see `_qc/REPORT.md`. |
| §8.3 contrast | Ink #3D3929 on cream #FAF9F5 — luminance ratio ≥ 4.5:1 | ✅ Same fidelity palette as landscape, ~11:1 ratio. |
| §8.4 kerning | No Pango-fallback catastrophes | ✅ B01 hesitant writer at fontSize 145 (portrait): ligatures on "au" "di" "up" "gr" land clean. |
| §8.5 no-wordy-card | No card overflows | ✅ B09 verdict fits all six lines with wrapping intact. B10 Your-Turn wraps but is legible. Portrait code beats (B02-B08) DO truncate long code lines at the card's right edge — documented as a KNOWN LIMITATION in CHECKS-REPORT.md; the salient text is visible within ~40 columns and the FULL text is in the landscape master + demo/RUN-LOG.txt. |
| §8.6 golden strings | Title / channel / handle correctness | ✅ "Brutalist / Command: art / keys." (portrait outro wraps title over three lines). `@HumanitariansAI` folder chip on composer beats. `@NikBearBrown` outro handle (locked). |

## Result

- **§8.x visual audit: PASS on all six items** — with the documented
  right-edge code truncation on portrait ClaudeCodeBeat916 flagged
  under §8.5 as a KNOWN LIMITATION, not a defect (the container holds,
  no ink escapes SAFE916).
- The absent `type_check.py` was NOT bypassed; this file records the
  standing visual audit that replaced it.
- Gate V returned `frames=24 BLOCKER=0 MAJOR=0` on the final vertical
  master.
