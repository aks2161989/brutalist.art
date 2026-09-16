# SOURCES.md — The sri-explainer Skill

## Primary source (the skill itself)

- `skills/make/sri-explainer/SKILL.md`
  SHA-256 `63a052f7ab70c7c7ee29b0b16f70652eb5a07afc5180e43396446977afdb755b`
  (matches `episode.source_sha256` for this invocation)
  — every verbatim quote in the film's Mechanism cards is copied from
  this file.

## Referenced sibling skills

- `skills/make/ai-explainer/SKILL.md` — parent chassis for a
  single-mechanism chapter; supplies the four bookends
  (ClaudeComposerAsk cold open, BrutalistHesitantWriter BLUF,
  ClaudeVerdictArtifact recap, ClaudeComposerAsk `Your turn.`,
  ClaudeTitleOutro).
- `skills/make/deep-explainer/SKILL.md` — parent chassis for a
  multi-section chapter; supplies THE BEAT-MIX CONTRACT, VOX LAW, the
  vox-run continuity rule, and Gates D1 / D2.
- `skills/make/nopunt/SKILL.md` — SHOW / HOLD / CARD vocabulary,
  referenced in the framework beats.

## Toolkit-level references

- `CLAUDE.md` (toolkit root) — free-by-default rules, library-first,
  claude-liam default channel, IN-FOR-BEAR LAW.
- `CLAUDE-BRAND.md` — the claude-liam palette + persona table.
- `OUTRO-LOCK.md` — B13 title outro constraints (hardcoded
  `@NikBearBrown` handle, slug-seeded mascot; @NikBearBrown reels only).
- `docs/PIPELINE-SAFETY.md`, `docs/FELLOWS-SUBMISSION.md` — pipeline
  and submission rules referenced by the toolkit.
- `runtime/prose/teardown/PROSE.md` — Teardown register the narration
  uses.
- `CLAUDE-CODE-VISUAL-QC-CHECK.md` — the rubric Gate V + the manual
  frame review use.

## Read-only example leads

Provided by the supervisor as reference DATA. Neither original file was
overwritten, no human signatures were reused, and none of these leads
was cited on-screen — only their beat-sheet shape and cite-card style
were adapted for staging.

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — "Your
  Weekly Video, Handled." · SHA-256
  `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`
- `sanjana-rao/09-02-2026-monte-carlo-schedule-risk-explainer/beat_sheet.json`
  — "Monte Carlo Schedule Risk: When Will This Project Really Finish?"
  · SHA-256
  `86452e39919248a4bec3bb521fab376697aa4b61e1ca2b9a5e86155075b49c63`

## Non-sources (deliberately NOT cited)

- No Prof Sridhar chapter file was ingested for this episode. The
  Sridhar chapter register is *described* from the SKILL.md's own
  extraction rules; no chapter prose is quoted. The film's B10 flags
  this as the honest documented limitation.
- No paid API. No remote clones. No `setup --install`, no `art keys`,
  no publishing.
- The public toolkit repository referenced in the toolkit's CLAUDE.md
  is https://github.com/nikbearbrown/brutalist.art (mentioned only in
  paperwork; nothing was cloned or pushed for this run).

## Local demo evidence

- `demo/scenes-search.log` — output of `./art scenes --check <Name>`
  for the three SkillTeardown compositions and their 916 variants
  registered for this reel.
