# The logo Skill — Brutalist ep. 15

Skill teardown of `skills/make/logo/SKILL.md` — the one command that appends a
random-once brand sting after a reel's last beat.

## Two aspects, both native 4K

- **Landscape (16:9)** — `exports/landscape/claude-liam-brutalist-skill-logo.mp4`
  · 3840×2160 · 317.25s · 12 beats · Gate V clean
- **Portrait (9:16)** — `exports/vertical/claude-liam-brutalist-skill-logo-vertical.mp4`
  · 2160×3840 · 317.25s · 12 beats · Gate V clean

Both compiled via `runtime/scripts/compile.py` with the shipped final-frame
Gate V (`runtime/qc/final_frame_check.py`) passing 0 BLOCKER / 0 MAJOR. Both
verified atomically to `.verified.json`.

## Structure

- `beat_sheet.json` / `vertical/beat_sheet.json` — the 12-beat sheets
- `mp3/` / `vertical/mp3/` — per-beat Kokoro `am_onyx` narration (local, free)
- `media/` / `vertical/media/` — per-beat 4K Remotion renders
- `clips/` / `vertical/clips/` — per-beat conformed clips
- `_qc/` / `vertical/_qc/` — Gate V report + samples + contact sheet
- `qc-sheet.png` / `vertical/qc-sheet.png` — contact sheet for the review
- `demo/` — a synthetic `fixture-reel/` with `logo-run.log` capturing four live
  `logo.py` invocations (hai/first, hai/reroll, hai/reuse, medhavy/reroll →
  drawOn) — the reel's evidence for random-once-then-locked and pool curation.

## Paperwork

`BRIEF.md`, `BUILD-PROMPT.md`, `FEEDBACK.md`, `SOURCE-SNAPSHOT.json` come from
the supervisor. This session authored:

- `SCRIPT.md` — narration script (per-beat)
- `SOURCES.md` — SHA-256s and provenance
- `FACTCHECK.md` — every claim verified against source line
- `SHOTLIST.md` — 12-beat shot list + live demo evidence
- `PROMPTS.md` — the cold-open ask + Your Turn prompt
- `CHECKS-REPORT.md` — proof-gate, audio, renders, Gate V, gaps
- `TYPECHECK.md` — visual typography audit (substitute for missing legacy check)
- `VISUAL-REVIEW.json` — this session's AI review record with real SHA-256s

The vertical directory carries its own aspect-appropriate copies plus
portrait-only findings.

## Next

**Bear's viewing and editing is next.** These are rendered films, not
published clips. The Brutalist toolkit renders, humans schedule. No git push,
no upload, no publishing has occurred.
