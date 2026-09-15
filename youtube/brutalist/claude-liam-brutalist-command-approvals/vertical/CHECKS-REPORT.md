# CHECKS-REPORT — vertical (9:16 companion)

Derived from the landscape reel via `python3 runtime/scripts/shorts.py <REEL> --vertical`.
Full-length preservation: no beats dropped, no outro rewrite, no endcard.
Every REMOTION beat rewired to its 916 portrait composition and re-rendered natively —
no crops of a landscape master.

## Beat classification

12/12 SHOW, 0 HOLD, 0 PUNT. Same beats as landscape; same narration; same audio.

## Portrait adaptation record

- **B00 ClaudeComposerAsk916** — native portrait render; same props (folder chip
  `@HumanitariansAI`, greeting `Selam, Liam`).
- **B01 BrutalistHesitantWriter916** — RESTRUCTURED for portrait BLUF coverage
  ≥ 55% (`[[feedback_hesitant_writer_portrait_bluf_recipe]]`): text broken to
  three short lines `art approvals / signs / files.`, `fontSize: 300`,
  `lineSpacing: 3.4`. Correction still lands as `art approvals / inspects / subjects.`
- **B02-B08 ClaudeCodeBeat916** — new portrait composition registered in Root.tsx
  (see `scene-source/runtime/remotion/src/Root.tsx`). Component reflows to 1080x1920
  via `useVideoConfig()`. LIMITATION carried forward from ep 29 `art run`: long
  monospace code lines truncate at the card's right edge in portrait. Ink stays
  inside the white card, so Gate-V passes. The salient part of each line is
  visible within ~40 characters; the full line is preserved in the landscape
  master and in `demo/RUN-LOG.txt`. Not silently swallowed; called out here.
- **B09 ClaudeVerdictArtifact916** — native portrait artifact card; six lines stagger
  vertically as narration lands. No content lost.
- **B10 ClaudeComposerAsk916** — shortened for the narrower composer: segment
  `Audit — never sign`, an abridged command (still verbatim source-line-per-source-line
  in spirit, three tight grading lines). Full paste-ready prompt is preserved in the
  landscape master.
- **B11 ClaudeTitleOutro916** — native portrait outro card; title wraps to three
  lines with the terracotta period, `@NikBearBrown` handle underneath per OUTRO-LOCK.

## Gate V (frame-level QC on the finished portrait MP4)

Initial run flagged two BLOCKERs (B10 edge-bleed) + two MAJORs (B01 underfill).
Both fixed at the source and re-rendered natively. Final pass:

```
$ python3 runtime/qc/final_frame_check.py \
    <REEL>/vertical \
    --mp4  <REEL>/exports/vertical/claude-liam-brutalist-command-approvals-vertical.mp4 \
    --sheet <REEL>/vertical/clips/_work/resolved-sheet.json
[gate-v] frames=24 BLOCKER=0 MAJOR=0 → <REEL>/vertical/_qc/REPORT.md
```

## Frame-by-frame AI visual review

Ten representative stills extracted from the finished 4K portrait master and read
individually. Paths + SHA-256 in `VISUAL-REVIEW.json`. Notes:

- `start.png` — B00 portrait: composer, `@HumanitariansAI` chip, `Selam, Liam` greeting.
- `bluf.png` — B01 portrait: three-line `art approvals / inspects / subjects.` at large
  serif; fills >55% of the safe area.
- `framework.png` — B02 portrait code card: `case "$cmd" in / approvals) / exec python3
  "$ART_HOME/runtime/…` visible; long tail on the `exec` line truncates (see LIMITATION
  above).
- `worked-cmd.png` through `verdict.png` — every code beat's title, filename chip, and
  the leading portion of each line reads clearly in portrait; truncation only affects
  the tail of the longest lines.
- `your-turn.png` — B10 portrait composer with abridged command inside the safe area;
  three output lines stacked cleanly.
- `end.png` — outro card, title wraps to `Brutalist / Command: art / approvals.` with
  the terracotta period; handle beneath.

## Runtime checks not run

Same as landscape (Gate T not present in this snapshot). See TYPECHECK.md.

## Conclusion

Vertical 2160x3840 · 200.875s · H.264 + AAC. Every gate that exists in this toolkit
snapshot passed. Ten evidence stills were read individually. Long code lines
truncate in portrait — accepted precedent from ep 29, called out here for the human
reviewer. Human review pending.
