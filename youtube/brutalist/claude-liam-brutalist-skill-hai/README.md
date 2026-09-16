# The hai Skill — Brutalist playlist, episode 14

A claude-liam Teardown of `skills/make/hai/SKILL.md` for the @HumanitariansAI channel.

## Deliverables

- Landscape 4K master: [`exports/landscape/claude-liam-brutalist-skill-hai.mp4`](exports/landscape/claude-liam-brutalist-skill-hai.mp4) — 3840×2160, 24fps, 280.1s, H.264 + AAC.
- Portrait 4K companion: [`exports/vertical/claude-liam-brutalist-skill-hai-vertical.mp4`](exports/vertical/claude-liam-brutalist-skill-hai-vertical.mp4) — 2160×3840, 24fps, 280.1s, H.264 + AAC. Native portrait reflow, not a center-crop.

Both files are atomic-verified (`.verified.json` sidecars beside each master).

## Status

Bear's viewing and editing are next. **Nothing is published.** No upload attempted; the compiler wrote to local paths only. If a fix is required, add it to [`FEEDBACK.md`](FEEDBACK.md) and the next automatic pass will resume.

## Paperwork

Landscape: [`SCRIPT.md`](SCRIPT.md) · [`SOURCES.md`](SOURCES.md) · [`FACTCHECK.md`](FACTCHECK.md) · [`SHOTLIST.md`](SHOTLIST.md) · [`PROMPTS.md`](PROMPTS.md) · [`CHECKS-REPORT.md`](CHECKS-REPORT.md) · [`TYPECHECK.md`](TYPECHECK.md) · [`VISUAL-REVIEW.json`](VISUAL-REVIEW.json) · [`BUILD-PROMPT.md`](BUILD-PROMPT.md)

Portrait: [`vertical/CHECKS-REPORT.md`](vertical/CHECKS-REPORT.md) · [`vertical/TYPECHECK.md`](vertical/TYPECHECK.md) · [`vertical/VISUAL-REVIEW.json`](vertical/VISUAL-REVIEW.json) (plus shared paperwork copied into `vertical/`).

## Demo evidence

The film shows `brand_variant.py` running as its worked example. The demo itself is captured under [`demo/`](demo/) — a synthetic fixture reel, the `scaffold-run.log` from an actual invocation, and the resulting `hai-example-reel/beat_sheet.hai.json`. Pre/post SHA-256 of the fixture's `beat_sheet.json` is recorded in [`SOURCES.md`](SOURCES.md) to prove the source stayed byte-identical (the whole point of the skill).

## Falsifiability finding

Reading the three source files together surfaces a real disagreement about the HAI Kokoro voice — `SKILL.md` says `af_kore`, `brand_variant.py` writes `af_bella`, and `brands/hai.md` says `am_onyx` after ElevenLabs was permanently removed on 2026-09-03. All three line-cited in [`FACTCHECK.md`](FACTCHECK.md). This is a finding, not a correction — the SKILL.md is not modified by this build.
