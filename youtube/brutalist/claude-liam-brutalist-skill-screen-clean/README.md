# The screen-clean Skill — Brutalist episode 19

AI Explainer / Skill Teardown of `skills/make/screen-clean/SKILL.md`.
Twelve beats. Voice: Kokoro `am_onyx` — Liam, in for Bear. Playlist:
Brutalist. Channel chip: `@HumanitariansAI`; outro handle `@NikBearBrown`
(OUTRO-LOCK).

Run ID: `dea2eb64b9844f9e916970a58f8cbdb2` (re-verified 2026-09-12 — exports unchanged, SKILL.md unchanged; toolkit local-override trigger only)

## Films to watch

- Landscape (16:9, native 4K, 318.17 s):
  `exports/landscape/claude-liam-brutalist-skill-screen-clean.mp4`
- Portrait (9:16, native 4K, 318.17 s):
  `exports/vertical/claude-liam-brutalist-skill-screen-clean-vertical.mp4`

Both pass Gate V clean (0 BLOCKER, 0 MAJOR) — re-validated 2026-09-12.

## Paperwork

- Landscape: `SCRIPT.md`, `SOURCES.md`, `FACTCHECK.md`, `SHOTLIST.md`,
  `PROMPTS.md`, `CHECKS-REPORT.md`, `TYPECHECK.md`, `VISUAL-REVIEW.json`
- Portrait: `vertical/{SOURCES,FACTCHECK,SHOTLIST,PROMPTS,CHECKS-REPORT,
  TYPECHECK}.md`, `vertical/VISUAL-REVIEW.json`

Contact sheets: `_qc/contact_sheet.png` (landscape, preserved as
`_qc/contact_sheet_landscape.png`) and `vertical/_qc/contact_sheet.png`
(portrait).

## What ran locally as a safe demo

Real `ffmpeg -af volumedetect` on two synthetic 2560×1600 fixtures
generated with `ffmpeg -f lavfi`:

- Silent fixture (`anullsrc`) → `mean_volume: -91.0 dB` → **STOP** (below
  screen-clean's -40 dB gate).
- Voiced fixture (440 Hz sine) → `mean_volume: -21.1 dB` → **proceed**.

Full command log in `demo/screen-clean-run.log`. No personal recording
touched.

## What did NOT run

- No paid TTS call. No API keys used.
- No push, no upload, no publication.
- Passes 2–5 of `screen-clean` were illustrated per REBUILD LAW from the
  SKILL.md rather than exercised against a real screen recording — the
  film's demo is Pass 1 only. Documented in `FACTCHECK.md § Boundary`.

## Next

Bear's viewing and editing is the next step. Add requests to
`FEEDBACK.md`; a future automatic run will pick them up.
