# SOURCES.md — The nopunt Skill (Short)

This Short is a derivative cut. The narration, all seven per-beat mp3s, and
all seven native-portrait mp4s are reused unchanged from the parent
`claude-liam-brutalist-skill-nopunt` (its vertical companion). No new
narration, no re-renders, no captured footage were created for this Short.

## Parent reel (read-only for this job)
- `youtube/brutalist/claude-liam-brutalist-skill-nopunt/` — the 16:9 skill teardown film.
  - `vertical/beat_sheet.json` — full-length 9:16 beat sheet used as the cut source (SHA-256 for episode source: `2867520a80894532255b63f20b281832994d7980ac135a95dfd51f2cab83011d`).
  - `vertical/media/B*.mp4` — native 2160×3840 Remotion renders (unchanged).
  - `vertical/mp3/beat-B*.mp3` — Kokoro `am_onyx` per-beat narration (unchanged).
- Parent master mp4 SHA-256 (informational, not muxed here): `0a345d44717058db9e6164b0acf6936b0031489cc422c930056018d1594d2ba9`.

## Primary content source (transitive, via the parent)
- `skills/make/nopunt/SKILL.md`
  - Public path: `nikbearbrown/brutalist.art` → `skills/make/nopunt/SKILL.md`
  - Isolated-toolkit copy SHA-256: `ef38a574fe22f2fca1dfa0774bc51681252776f8ef2bd6f2b1e52d6478cab505`
  - Episode `source_sha256`: `db5dbdc4e0f8f59497d64b7e5665a89405a57e6f93e906a17bd632f1a00b5bf8`

## Sections cited by beats KEPT in this Short
- SKILL.md opening paragraph → B00, B01
- §"The one rule: HOLD vs PUNT" → B04 quote block, B07 body
- §"How to choose the tool" → B05 quote block
- §"The catalog" (six family section headings) → B05 body
- §"Punt costumes to reject" → B06 quote block
- §"SHOW / HOLD / CARD" → B07 quote block and closing pill

## Sections NOT cited by this Short (present in the 16:9 long)
- §"SKILL anatomy" — parent B02 (dropped)
- §"Step zero — ask the library" and §"Pipeline" — parent B03 (dropped)
- §"Step zero" miss-logging behaviour — parent B08 (dropped)
- Six-line verdict recap — parent B09 (dropped)
- §"Whole-sheet teaching-arc checklist" (audit rubric) — parent B10 (dropped)

## Read-only example leads (for shape, not narration)
- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — Your Weekly Video, Handled. (SHA-256 `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`)
- `sanjana-rao/08-24-2026-playlist-architecture-as-product-strategy/playlist-architecture-short/beat_sheet.json` — Playlist Architecture — Short. (SHA-256 `787621776bcd8810d8719a61f577f3589707bbf59151655fcbbdd10555b318a0`)

Neither example's beat sheet, narration, mp3s, or human signature was reused
in this Short. Their production shape (skill-teardown structure over the
parent Vox skeleton; Short cut discipline) informed layout only.

## What is NOT a source
- No public URLs, no private Drive links, no email or contact info are narrated on screen.
- No human collaborator's prior recording, mp3, or signature is reused as this run's output.
- No paid API generation. Narration was produced (by the parent) with the local Kokoro `am_onyx` voice; this Short reuses the parent's mp3 files unchanged.
- No captured footage / photography. All visuals are Remotion renders.

## Derivative artifacts of this Short
- `beat_sheet.json` — the derivative sheet (SHA-256 `8d5f4be5c594dc11bb8a8ef22773be6a81382dc576507533fc271c2e1a633eb3`).
- `exports/short/claude-liam-brutalist-skill-nopunt-short.mp4` — the final Short (SHA-256 `7bc4e3ee6ecbc1757952353a6b7314357c55068231e4aac9fb46a99cda03da69`, 168.208 s container).
