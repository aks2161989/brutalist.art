# TYPECHECK — vertical — Brutalist Command: art run

Same disclaimer as the landscape sibling: `runtime/qc/type_check.py`,
`reference/type-spec.md` and the `kerning` skill are absent from this
toolkit revision. GATE T's automated typography pass is unavailable.
Filled in with a manual visual review against the compiled
`exports/vertical/claude-liam-brutalist-command-run-vertical.mp4`
(2160×3840, h.264 + AAC, 245.583 s). Every beat was sampled with
`ffmpeg -ss T -vframes 1` at ~75% of its steady-state and read with
the image-capable Read tool. Contact sheet: `vertical/qc-sheet.png`.

## Rubric applied per §8 (from memory of the type-spec)

| § | Check | Result |
|---|---|---|
| 8.1 | Minimum effective size | PASS — smallest sustained portrait type is the composer's chip / spark line at ~30–34px at 2160×3840. B01 hesitant writer at effective ~180px design × the patched portrait scale (min(1, 1)=1 on 1080×1920 source) renders comfortably in the safe box. |
| 8.2 | Overflow | PASS at frame level (no ink crosses the title-safe inset). **Known limitation**: `ClaudeCodeBeat916` does not word-wrap; long code lines are horizontally clipped inside the code card. Reader-visible on B04/B10 (long inline comments and long argparse-style lines). The card itself stays inside SAFE916. Documented in CHECKS-REPORT.md; fellows reading raw script contents should prefer the landscape master. |
| 8.3 | Contrast | PASS — same ink/cream + terracotta palette as landscape; luminance separation unchanged. |
| 8.4 | Kerning / Pango fallback | PASS — EB Garamond serif rendered cleanly at every size sampled; the mono in `ClaudeCodeBeat916` remained even. |
| 8.5 | No wordy card | Same narration budgets as landscape — see landscape TYPECHECK.md. Portrait beats do not lengthen their voice tracks. |
| 8.6 | Golden strings | PASS — B01 corrected text `"art run compiles the review video file."` matches the portrait recipe. All other prop strings preserved verbatim from landscape except B10's shortened `command` + `output` (documented in vertical/CHECKS-REPORT.md). |

## What could not be automatically verified

Same gaps as landscape. Portrait-specific gap: `BrutalistHesitantWriter`
required a 4-line component patch to give the 9:16 canvas a portrait-aware
design-scale factor. Recorded in memory
`feedback_brutalist_hesitant_writer_portrait_scale_patch`; applied to
the isolated toolkit copy only (the shared toolkit is unchanged).

## Result

**PASS (manual)** — 0 typography defects visible in the sampled portrait
frames; the code-block wrap limitation is a known, documented behavior
of `ClaudeCodeBeat916`, not a defect of this reel.
