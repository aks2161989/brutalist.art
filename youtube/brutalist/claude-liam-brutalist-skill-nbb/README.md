# The nbb Skill — Brutalist episode 17

AI Explainer / Skill Teardown of `skills/make/nbb/SKILL.md`. Twelve
beats. Voice: Kokoro `am_onyx` — Liam, in for Bear. Playlist:
Brutalist. Channel chip: `@HumanitariansAI`; outro handle
`@NikBearBrown` (OUTRO-LOCK).

## Films to watch

- Landscape (16:9, native 4K):
  `exports/landscape/claude-liam-brutalist-skill-nbb.mp4`
- Portrait (9:16, native 4K):
  `exports/vertical/claude-liam-brutalist-skill-nbb-vertical.mp4`

Both are 346.04s (~5m 46s). Both passed Gate V clean (0 BLOCKER, 0 MAJOR).

## Paperwork

- Landscape: `SCRIPT.md`, `SOURCES.md`, `FACTCHECK.md`, `SHOTLIST.md`,
  `PROMPTS.md`, `CHECKS-REPORT.md`, `TYPECHECK.md`, `VISUAL-REVIEW.json`
- Portrait: `vertical/{SOURCES,FACTCHECK,SHOTLIST,PROMPTS,CHECKS-REPORT,TYPECHECK}.md`,
  `vertical/VISUAL-REVIEW.json`

Contact sheets: `_qc/contact_sheet.png` and `vertical/_qc/contact_sheet.png`.

## What ran locally as a demo (safe)

- `python3 runtime/scripts/brand_variant.py demo/fixture-reel nbb` —
  fully deterministic scaffold on a synthetic 3-beat fixture.
  Captured in `demo/nbb-run.log`. Source `beat_sheet.json` SHA-256 is
  identical before and after (isolation contract holds).

## What did not run

- No paid TTS call. No API keys used.
- No push, no upload, no publication.
- No batch scaffold on a real book folder — documented in FACTCHECK.md.
- No Step 2 (register rewrite by Claude) against a real reel; that is
  the viewer's Your-Turn assignment.

## Next

Bear's viewing and editing is the next step. Add requests to
`FEEDBACK.md`; a future automatic run will pick them up.
