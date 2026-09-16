# SOURCES.md — The riff Skill (Short)

This Short is a derivative cut. The narration, all six per-beat mp3s, and all
six native-portrait mp4s are reused unchanged from the parent
`claude-liam-brutalist-skill-riff` (its vertical companion). No new narration,
no re-renders, and no captured footage were created for this Short.

## Parent reel (read-only for this job)
- `youtube/brutalist/claude-liam-brutalist-skill-riff/` — the 16:9 skill teardown film.
  - `vertical/beat_sheet.json` — full-length 9:16 beat sheet used as the cut source (SHA-256: `f03a063ad4ed53282f8f879f9a2d9aaf0d3b13a7ab172bac81f3c00f6a4bc871`).
  - `vertical/media/B*.mp4` — native 2160×3840 Remotion renders (unchanged).
  - `vertical/mp3/beat-B*.mp3` — Kokoro `am_onyx` per-beat narration (unchanged).
- Parent master mp4 SHA-256 (informational, not muxed here): `ed2ca4f709268b96450a5db5f11d9c59decc931910283bf1c43a0f0c6aa20959`.

## Primary content source (transitive, via the parent)
- `skills/make/riff/SKILL.md`
  - Public path: `nikbearbrown/brutalist.art` → `skills/make/riff/SKILL.md`
  - Isolated-toolkit copy SHA-256: `539bb5f430a28a241ab1e68188ef74eb59200b6592ca127df55b151ce8e01083`
  - Episode `source_sha256`: `f03a063ad4ed53282f8f879f9a2d9aaf0d3b13a7ab172bac81f3c00f6a4bc871`

## Sections cited by beats KEPT in this Short
- SKILL.md opening paragraph ("riff is commentary grounded in visible evidence") → B00 cold open
- §"Look before writing" premise (watch before speaking; footage = evidence) → B01 BLUF
- §"Look before writing" bullets (clip → probe/frames/timecodes; scene → find renderer/test fixture; gameplay → actual engine capture) → B04 mechanism
- §"Look before writing" example ("Never call a scripted route a human playtest…") → B08 design tell
- All four rules synthesized from §"Look before writing" and RIFF.md record line → B09 verdict
- §"Voice and rendering" (Liam, in for Bear, Teardown register, Kokoro am_onyx) → B11 outro

## Sections NOT cited by this Short (present in the 16:9 long)
- Skill folder anatomy (`skills/make/riff/`, SKILL.md line count) — parent B02 (dropped)
- Four-phase pipeline (Look / Observe / Write / Record) — parent B03 (dropped)
- Self-demo of `./art scenes` scene search — parent B05 (dropped)
- Mechanism 2: evidence before interpretation (footage vs. voice as separate jobs) — parent B06 (dropped)
- RIFF.md five-column schema detail — parent B07 (dropped)
- Full Your Turn exercise prompt with rubric — parent B10 (dropped)

## Read-only example leads (for shape, not narration)
- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — Your Weekly Video, Handled. (SHA-256 `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`)
- `sanjana-rao/08-24-2026-playlist-architecture-as-product-strategy/playlist-architecture-short/beat_sheet.json` — Playlist Architecture — Short. (SHA-256 `787621776bcd8810d8719a61f577f3589707bbf59151655fcbbdd10555b318a0`)

Neither example's beat sheet, narration, mp3s, or human signature was reused
in this Short. Their production shape (skill-teardown Short cut discipline)
informed layout only.

## What is NOT a source
- No public URLs, no private Drive links, no email or contact info are narrated on screen.
- No human collaborator's prior recording, mp3, or signature is reused as this run's output.
- No paid API generation. Narration was produced (by the parent) with the local Kokoro `am_onyx` voice; this Short reuses the parent's mp3 files unchanged.
- No captured footage / photography. All visuals are Remotion renders.

## Derivative artifacts of this Short
- `beat_sheet.json` — the derivative sheet (SHA-256 `40e108607f959cd3f12802dad074f61eb8ab9cc6385062f0d84abdfb7c404d06`).
- `exports/short/claude-liam-brutalist-skill-riff-short.mp4` — the final Short (SHA-256 `59fbc417aef8728542408e1f2bf1e05a7dd9f8cd019ba6387d195267cfe29ceb`, 102.667s container).
