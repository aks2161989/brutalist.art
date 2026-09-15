# SOURCES.md — The your-turn Skill (ep 21)

## Primary source (episode)

- `skills/make/your-turn/SKILL.md`
  - SHA-256: `aecd503a11c413c2b7e123f5b3c0d80832a1e5d071ea523b243b5c130f514865`
    (current file and SOURCE-SNAPSHOT match; re-verified 2026-09-12)
  - episode.source_sha256 from repoloop: `8250e8ccd8779eb2629de62b05699c311dc1e5a4caeb70f1a1260e9a8d10f126`
    (differs — repoloop likely combined or salted; actual file sha used here)
  - The reel's Anatomy / Mechanism / Verdict cards quote from this file
    verbatim; each quote's `cite:` names the SKILL section.

- `skills/make/your-turn/scripts/apply_your_turn.py`
  - The deterministic transformer that mutates the closing three beats in
    place. Referenced by name on B02 (Anatomy) and executed live in `demo/`.

## Parent skills read for context

- `skills/make/ai-explainer/SKILL.md` — the parent chassis whose bookends and
  laws your-turn inherits. SHA-256 `a7421d4d861b44a983a31e9fcd7451cd32312a139366e74acc2123dfdefbd3c0`
  in this run's snapshot.
- `skills/make/nopunt/SKILL.md` — SHOW/HOLD/CARD classification cited when
  authoring each beat's show block. SHA-256 `ef38a574fe22f2fca1dfa0774bc51681252776f8ef2bd6f2b1e52d6478cab505`.
- `runtime/prose/teardown/PROSE.md` — Teardown register discipline.

## Read-only example leads (per BRIEF.md)

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json`
  - "Your Weekly Video, Handled." SHA-256 `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`
  - Consulted only for the closing-beat staging convention; the fellow's own
    narrations, recordings, or Drive links are NOT reproduced here.
- `tanmay-kulkarni/2026-08-12-bs-01-pick-and-scope/beat_sheet.json`
  - "Your Job Description Is Too Generic for AI — Four Questions That Fix It"
    SHA-256 `9d9b8d625efe99c46166dabdb05b6706fba83c3e91d81ca5ec44df088d26a299`
  - Same treatment — reference lead only, no signatures or results carried
    over.

## Toolkit setup

- Public repository: <https://github.com/nikbearbrown/brutalist.art>
  (setup + install evidence uses the LOCAL installed copy at
  `.repoloop/workspaces/claude-liam-brutalist-skill-your-turn/toolkit/`, not
  a fresh network clone.)

## Not consulted / not applicable

- No external HTTP requests, no paid TTS, no LLM generation of body prose
  beyond what appears in `SCRIPT.md`. No archival / image API. No YouTube
  API. No `art keys`, no `setup --install`.

## Provenance of live demonstrations

The `demo/` folder is entirely synthetic: `fixture-beat_sheet.json` and
`drafts.json` were written by this build session; no real fellow reel was
touched. The transformer produced `fixture-beat_sheet.applied.json` and the
three reports (`demo-report.json`, `demo-applied-report.json`,
`demo-idempotent-report.json`) directly.
