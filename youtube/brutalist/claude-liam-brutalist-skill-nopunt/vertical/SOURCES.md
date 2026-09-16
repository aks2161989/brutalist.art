# SOURCES.md — The nopunt Skill

## Primary source

- `skills/make/nopunt/SKILL.md`
  - Repo path (public): `nikbearbrown/brutalist.art` → `skills/make/nopunt/SKILL.md`
  - Isolated-toolkit copy SHA-256: `ef38a574fe22f2fca1dfa0774bc51681252776f8ef2bd6f2b1e52d6478cab505`
  - Episode `source_sha256` at invocation: `db5dbdc4e0f8f59497d64b7e5665a89405a57e6f93e906a17bd632f1a00b5bf8`
  - Read fully. Every claim in the narration ties back to a labelled section in this file.

## Cross-referenced sibling skills (read for context, not directly narrated)

- `skills/make/ai-explainer/SKILL.md` — the parent register; references nopunt.
- `skills/make/deep-explainer/SKILL.md` — likewise references nopunt.
- `skills/make/cli-explainer/SKILL.md` — likewise references nopunt.
- `skills/make/explainer/SKILL.md` — parent Vox contract.

## Runtime references (component names shown or narrated)

- `runtime/remotion/src/scenes/` — the current Remotion scene registry (the
  catalog must stay synced with this).
- `runtime/remotion/src/Root.tsx` — where `./art scenes --check <Name>`
  confirms renderability.
- `TEMPLATE-MISSES.md` — where genuine catalog gaps get logged. Existence
  described by the skill; not opened in this reel.

## Read-only example leads (leads, not verified facts)

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — Your Weekly
  Video, Handled. (SHA-256 `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`)
- `yatra-r/2026-09-03-this-week-gordy/beat_sheet.json` — This Week, Gordy.
  (SHA-256 `7e3ea1f61c421e605e583be9b2a7b5f554aa8cadfb6e14dabaee66f471856083`)

Neither example's beat sheet, narration, mp3s, or human signature was reused
in this reel. Their production shape (skill-teardown structure over the parent
Vox skeleton) informed layout only.

## Live demonstration log (isolated toolkit)

- `demo/nopunt-run.log` — four real `./art scenes` invocations captured
  2026-09-08T23:19:08Z against the isolated toolkit. No network calls, no paid
  services, no publishing.

## What is NOT a source

- No public URLs, no private Drive links, no email or contact info are
  narrated on screen.
- No human collaborator's prior recording, mp3, or signature is reused as this
  run's output.
- No paid API generation. The audio was produced by the isolated
  `generate_audio_kokoro.py` script; the visuals were rendered by the isolated
  `remotion_scenes.py`.
