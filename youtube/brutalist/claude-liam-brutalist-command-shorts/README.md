# Brutalist Command: art shorts

Ep 30 of the Brutalist playlist. Command teardown of `./art shorts` — the
dispatcher case at `art:102-104` that execs
`python3 runtime/scripts/shorts.py`, plus its sibling `./art vertical` at
`art:105-107` that forwards the same script with `--vertical`. Aliases: none.

## Deliverables (local, unpublished)

- **Landscape** (16:9, 3840×2160 · 296.29 s · h.264 + AAC)
  `exports/landscape/claude-liam-brutalist-command-shorts.mp4`
- **Vertical companion** (9:16, 2160×3840 · 296.29 s · h.264 + AAC)
  `exports/vertical/claude-liam-brutalist-command-shorts-vertical.mp4`

Both files carry the compiler's `verified.json` receipt beside them. Both
aspects passed Gate V (final_frame_check) with 0 BLOCKER / 0 MAJOR.

## Contents

- 12 beats across ~296 s of Kokoro `am_onyx` narration.
- Beat spine: B00 Salam ASK → B01 hesitant BLUF → B02 dispatcher (art:102-107)
  → B03 THE SHORTS LAW → B04 `plan_drops()` greedy algorithm → B05 THE ONDA
  CHECK → B06 per-beat precedence (pantry / ONDA / hand-made / center-cut)
  → B07 real fixture invocation (`214s → drops B02 → 163.5s OK`) → B08
  failure `./art shorts --vertical --drop B02` REFUSED + recovery → B09
  verdict artifact → B10 Your Turn paste prompt → B11 title outro.

## Human review is next

Bear's viewing and editing pass is the next step. Nothing here has been:
- uploaded to YouTube or any external service,
- transcoded outside the local Remotion + ffmpeg pipeline,
- committed to any git remote.

Publishing to `@HumanitariansAI` is a separate authorized human handoff.
See `docs/FELLOWS-SUBMISSION.md` inside the toolkit for the pipeline.

## Files in this reel

| Path | Purpose |
|---|---|
| `beat_sheet.json` | Landscape master sheet (12 beats, 4K 16:9) |
| `vertical/beat_sheet.json` | Portrait sheet (12 beats, 4K 9:16) — every Remotion pattern rewired to its `…916` sibling; B01 rewritten to 4-line portrait BLUF |
| `SCRIPT.md` | Every narration line, per beat |
| `SHOTLIST.md` | Twelve-beat shot list |
| `SOURCES.md` | Primary + supporting sources with SHA-256 |
| `FACTCHECK.md` | Line-by-line source-backed verification of every claim |
| `PROMPTS.md` | Remotion prop payloads per beat |
| `CHECKS-REPORT.md` | Which gates ran, what passed, what was repaired |
| `TYPECHECK.md` | Manual typography review (in place of the absent legacy checker) |
| `VISUAL-REVIEW.json` | Machine-readable review record + evidence hashes |
| `demo/SHORTS-LOG.txt` | Verbatim stdout/stderr from every `./art shorts` / `./art vertical` invocation used in B07/B08 |
| `_qc/final-contact-sheet.png` | 3×4 sample of the landscape master (opened during review) |
| `vertical/_qc/final-contact-sheet.png` | 3×4 sample of the vertical master (opened during review) |
