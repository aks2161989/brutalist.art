# SOURCES

## Primary source (the skill under teardown)

- `skills/make/ai-explainer/SKILL.md` — SHA-256 `db5dbdc4e0f8f59497d64b7e5665a89405a57e6f93e906a17bd632f1a00b5bf8`
  Read from the isolated toolkit copy at:
  `/.repoloop/workspaces/claude-liam-brutalist-skill-ai-explainer/toolkit/skills/make/ai-explainer/SKILL.md`.
  The read matches the invocation's `episode.source_sha256`.

## Companion references (read in full during authoring)

- `skills/make/nopunt/SKILL.md` — SHA-256 (per SOURCE-SNAPSHOT) `ef38a574fe22f2fca1dfa0774bc51681252776f8ef2bd6f2b1e52d6478cab505`
- `runtime/prose/teardown/PROSE.md` — `6accc1a576ca9b52713abd31507f5deece6dc2612ca90967b25b661e59111786`
- `docs/PIPELINE-SAFETY.md` — `4619f0d4702317d654cd6498cadc8c277691e4c7565920ef851dbb628aa6298d`
- `docs/FELLOWS-SUBMISSION.md` — `7825c728f040b0f7a49bbd950a5a2bef70c8a59ff2fbe0538716c8d3381f5223`
- `REPOLOOP-PROMPT.md` — `abf55bdc729a9c30216e4375dff0c62b4bf5af4c717ad28be69709de64d5bc97`
- `CLAUDE-BRAND.md`, `OUTRO-LOCK.md`, `CLAUDE.md`, `CLAUDE-CODE-VISUAL-QC-CHECK.md` — read directly from the isolated toolkit; hashes not captured in the invocation snapshot but content read verbatim.

## Verbatim quotes on screen

- B04 — "The bookends do not change… The modifier governs the MIDDLE." — ai-explainer SKILL.md (§skill-teardown modifier).
- B05 — "Two consecutive beats sharing the same visual scheme is the smell; seven videos of composer wallpaper is the failure this law exists to prevent." — ai-explainer SKILL.md (§ILLUSTRATE LAW).
- B06 — "The Claude interface is never shown alone as decoration — it is always followed by what it produced. Ask beats stay in the fixed Claude skin; RESULT graphics render in the episode's CHANNEL palette." — ai-explainer SKILL.md (§ASK→RESULT LAW).
- B07 — "A named voice, never a clone. Liam does not imitate Bear's delivery or claim to be him." — ai-explainer SKILL.md (§Liam / IN-FOR-BEAR LAW).

All four quotes verified against the file on disk during authoring — the words on screen match the SKILL.md exactly.

## Example reels (read-only leads)

Per BRIEF.md, only staging patterns were used; no signatures, credentials, personal Drive URLs, or old rendered results are republished here.

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — SHA-256 `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`
  Used only for the shape of a HAI-branded onboarding cold open and the ASK→RESULT rhythm; no narration, no props, no output claims lifted.
- `sanjana-rao/09-02-2026 monte-carlo-schedule-risk-explainer/beat_sheet.json` — SHA-256 `86452e39919248a4bec3bb521fab376697aa4b61e1ca2b9a5e86155075b49c63`
  Used only for the four-bookend beat count and the audio-first framing hint; no numeric result or narration copied.

Both example files were preserved unchanged in `examples/` and never overwritten.

## Voice

- Kokoro-82M via `kokoro-onnx` (Apache-2.0), voice `am_onyx` — free, local, no key.
  Model files: `runtime/models/kokoro/kokoro-v1.0.onnx`, `voices-v1.0.bin` (resolved from `$KOKORO_MODEL` / `$KOKORO_VOICES`).

## Fonts

- EB Garamond (SIL OFL) — bundled at `runtime/fonts/EB_Garamond/static/*.ttf`.
- Inter (SIL OFL) — bundled at `runtime/fonts/Inter/static/*.ttf`.
- System UI sans (SF Pro Text / Segoe UI / Helvetica Neue) via CSS fallback stack.

## Seeds

- BrutalistHesitantWriter seed (B01): `ai-explainer-bluf-2026`. Same seed → identical performance every render.

## Publishing / uploads

None. Local render only. No YouTube upload, no Drive upload, no git push in this run. Human review pending.
