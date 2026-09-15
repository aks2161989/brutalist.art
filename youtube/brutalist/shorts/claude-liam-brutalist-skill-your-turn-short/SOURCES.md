# SOURCES — The your-turn Skill (Short)

The Short is a whole-beat derivative of the parent's native 9:16 companion. No
new sources are introduced.

## Parent reel (source of every retained media/mp3 file)

- Path: `youtube/brutalist/claude-liam-brutalist-skill-your-turn/vertical/`
- Parent master video: `exports/vertical/claude-liam-brutalist-skill-your-turn-vertical.mp4`
- Parent master SHA-256: `bdeb47c89ce4ecf05cf70313aedee7f0e65a4c14a3f793aaaa2bf8362ee12d5a`
- Parent beat sheet path (source of this Short's plan): `vertical/beat_sheet.json`
- Parent narration engine: Kokoro `am_onyx` (Liam, in for Bear)

## Underlying skill under teardown

- `skills/make/your-turn/SKILL.md` — episode `source_sha256` per parent metadata: `a78e89d72b9770dca820ea922194e86e39c251b8acab17028921cd8edf5d0193`
- `skills/make/your-turn/scripts/apply_your_turn.py`
- Public repository: https://github.com/nikbearbrown/brutalist.art

## Read-only example leads (not reused)

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` (SHA-256 746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22) — "Your Weekly Video, Handled." — reviewed as reference material only; nothing from it copied.
- `tanmay-kulkarni/2026-08-12-bs-01-pick-and-scope/beat_sheet.json` (SHA-256 9d9b8d625efe99c46166dabdb05b6706fba83c3e91d81ca5ec44df088d26a299) — "Your Job Description Is Too Generic for AI" — reviewed as reference material only; nothing from it copied.

## What this Short does NOT reuse

- No fellow signatures, private URLs, or third-party recordings.
- No paid API generation (voice, image, chat) — all narration mp3s are the parent's local Kokoro renders.
- No new frames rendered — every media/*.mp4 is byte-copied from the parent's vertical/media/ slot; SHA-256 of each is listed in `_qc/` and CHECKS-REPORT.md.
