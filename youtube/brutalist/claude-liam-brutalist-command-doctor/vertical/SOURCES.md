# SOURCES — Brutalist Command: art doctor

## Primary sources (this invocation, verified live)

- `art` (toolkit root) — the dispatcher.
  - Source path: `brutalist.art/art`
  - This run's SHA-256: `9bb77a7c84701d23ab6e73f0a4f48592f17748ffad2c7114b62687bb7f97d0e9`
  - Reel citations: `art:96-99` (dispatcher case), `art:18` (help-block line).
- `setup` (toolkit root) — the readiness auditor executed by `art doctor`.
  - Source path: `brutalist.art/setup`
  - This run's SHA-256: `75040062dfcb20d0437a5a358abc516ed6e4b1e4e9020aaac926e1b9d5b2208d`
  - Reel citations: `setup:57` (mode branch), `setup:117-140` (check() +
    dynamic OK_/MISS_), `setup:137` (kokoro_synth), `setup:142-150` (FEATURES
    array), `setup:156-172` (aggregation loop), `setup:178` (exit 1 line).
- `runtime/scripts/setup_smoke_kokoro.py` — the phrase-and-decode smoke test
  invoked by the `kokoro_synth` check row. Not on screen; referenced by name.

## Adaptation examples (read-only leads from example-sources.json)

Both examples were read in full and used as staging leads only. No text,
narration, signature, or asset from either file was reused verbatim.

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — "Your Weekly
  Video, Handled." SHA-256 `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`.
  Adaptation lead: how a Brutalist agent-first reel introduces a toolkit
  script as the true subject and lets a live run answer the ask. Not
  republished; no private paths or URLs carried across.
- `yatra-r/2026-09-03-this-week-gordy/beat_sheet.json` — "This Week, Gordy."
  SHA-256 `7e3ea1f61c421e605e583be9b2a7b5f554aa8cadfb6e14dabaee66f471856083`.
  Adaptation lead: bookending a technical body with a clean cold-open ask
  and a title-restate outro. Same rejection: nothing personal reused.

## Playlist doctrine sources (already documented in the toolkit)

- `skills/make/ai-explainer/SKILL.md` (COLD OPEN LAW, ILLUSTRATE LAW,
  EXECUTIVE-SUMMARY LAW, HANDOFF LAW, OUTRO LAW).
- `skills/make/nopunt/SKILL.md` (SHOW / HOLD / CARD classification).
- `OUTRO-LOCK.md` (hardcoded @NikBearBrown handle on `ClaudeTitleOutro`; the
  known @HumanitariansAI/@NikBearBrown card mismatch is flagged in README.md).
- `CLAUDE-BRAND.md`, `CLAUDE-CODE-VISUAL-QC-CHECK.md`, `docs/PIPELINE-SAFETY.md`,
  `docs/FELLOWS-SUBMISSION.md` — read to hold the palette, gating, and
  fellows-workflow contract in mind while authoring.

## Demonstrations captured for this reel

All in `demo/RUN-LOG.txt` — verbatim command + output. Ran against this
isolated toolkit at `/Users/bear/…/claude-liam-brutalist-command-doctor/toolkit`.

- Section 2 — `./art doctor` on a fully green toolkit, exit 0.
- Section 3 — `./art doctor` with `runtime/models/kokoro/kokoro-v1.0.onnx`
  temporarily moved aside, one red row + two hint lines, exit 1.
- Section 4 — `./art doctor` after restoring the file, exit 0.

No network calls, no paid API, no upload, no publication.
