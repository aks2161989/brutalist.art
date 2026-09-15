# Brutalist Command: art todo

Episode 28 of the Brutalist Command playlist (@HumanitariansAI). Persona:
Liam, in for Bear. Voice: local Kokoro `am_onyx`. Twelve beats, 167.875 s,
0 slates, native compositions for both aspects.

Two deliverables landed on disk this session — Bear's viewing and any
`FEEDBACK.md` edits are next. Nothing has been published; nothing has been
uploaded; no GitHub push. This is the automated end of the pipeline.

## Deliverables

- **Landscape 16:9 (3840×2160)** —
  [`exports/landscape/claude-liam-brutalist-command-todo.mp4`](exports/landscape/claude-liam-brutalist-command-todo.mp4)
  · SHA-256 `cc0a885f6663f08270f5c169a707be66ab48e1055e9ea754c9a0bf1f159c4327`
  · verified: [`.verified.json`](exports/landscape/claude-liam-brutalist-command-todo.verified.json)
  · Gate V clean; VISUAL-REVIEW at [`VISUAL-REVIEW.json`](VISUAL-REVIEW.json)
  · paperwork: [`CHECKS-REPORT.md`](CHECKS-REPORT.md), [`TYPECHECK.md`](TYPECHECK.md), [`FACTCHECK.md`](FACTCHECK.md), [`SOURCES.md`](SOURCES.md), [`SHOTLIST.md`](SHOTLIST.md), [`PROMPTS.md`](PROMPTS.md), [`BUILD-PROMPT.md`](BUILD-PROMPT.md)

- **Vertical 9:16 (2160×3840)** — native portrait, NOT a Short crop —
  [`exports/vertical/claude-liam-brutalist-command-todo-vertical.mp4`](exports/vertical/claude-liam-brutalist-command-todo-vertical.mp4)
  · SHA-256 `400eb021c8011e14810b8beb1256b6bc79cb3ab79457c1189f5bd15e2eb6ed27`
  · verified: [`vertical/exports/…verified.json`](exports/vertical/claude-liam-brutalist-command-todo-vertical.verified.json)
  · Gate V clean; VISUAL-REVIEW at [`vertical/VISUAL-REVIEW.json`](vertical/VISUAL-REVIEW.json)
  · paperwork mirror: [`vertical/CHECKS-REPORT.md`](vertical/CHECKS-REPORT.md), [`vertical/TYPECHECK.md`](vertical/TYPECHECK.md), etc.

## What changed on this resume (attempt 2)

- **Landscape:** the compiled master and Gate V were already clean from
  the prior attempt (build-state `ready`, contact_sheet + REPORT.md
  intact); the only outstanding blocker was the missing AI frame-review
  record. Fresh evidence frames were extracted from the CURRENT master
  and hashed into `VISUAL-REVIEW.json`, so the record is anchored to
  this invocation's `run_id` and `source_sha256`. Landscape was NOT
  re-rendered — its content is unchanged.

- **Vertical:** the prior attempt failed Gate V with 14 top-edge bleed
  BLOCKER + 2 underfill MAJOR. Two source fixes on this resume:
  1. `runtime/remotion/src/CommandTodo.tsx` — `SparkLine` now bumps
     `sy` by +60 CSS in portrait mode. Callers still pass
     `sy = SY - 40`, but rendered ink now sits at physical y≈380 instead
     of y=177 (SAFE916.y threshold with margin is 184).
  2. `vertical/beat_sheet.json` B01 — the hesitant-writer text was
     restructured to three short lines (`art todo / is a / list.` with
     the same `list`→`receipt` swap) and `fontSize` raised 200→240.
     bbox coverage: 24% → 64%.
     B02-B08 (all seven Todo* custom illustrations) plus B01 were
     re-rendered with `remotion_scenes.py --only <BID> --force`, then
     the full vertical was recompiled.

## Notes on register + brand

- The outro card is the hardcoded `@NikBearBrown` OUTRO-LOCK card
  (`OUTRO-LOCK.md`) for the claude-liam family, not a HAI-branded card.
  The composer folder chip in this landscape carries `@NikBearBrown` too
  — the vertical beat sheet mirrors it. This is a deliberate carry-over
  from the shipped landscape and is called out for reviewer awareness;
  swapping to `@HumanitariansAI` for the composer chip would require a
  landscape re-render (B00 and B10) and is left for a future revision if
  Bear wants it.

## Human review — what's still open

1. Watch both files end-to-end and note anything into `FEEDBACK.md`.
2. Confirm whether the composer folder chip should read
   `@HumanitariansAI` (current: `@NikBearBrown`) — that decision drives
   whether B00/B10 need a landscape re-render.
3. Grade the B10 "Your Turn" prompt against a real Claude Code run.
