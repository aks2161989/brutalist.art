# Brutalist Command: art scenes

Episode 26 of the Brutalist playlist, adapted for @HumanitariansAI.
Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`. Register: Teardown.
12 beats. Command teardown of `./art scenes` and its aliases `scene` /
`scene-search`.

## Deliverables (local files — not published)

- **Landscape (16:9, 4K):** `exports/landscape/claude-liam-brutalist-command-scenes.mp4`  ·  3840x2160  ·  256.29 s  ·  h.264 + AAC.
- **Vertical (9:16, 4K):** `exports/vertical/claude-liam-brutalist-command-scenes-vertical.mp4`  ·  2160x3840  ·  256.29 s  ·  h.264 + AAC.

Both files are native 4K layouts (not upscaled cropped masters). Both
passed `final_frame_check.py` (Gate V) with 0 BLOCKER and 0 MAJOR defects.

## Paperwork index

### Landscape (root)

- [`beat_sheet.json`](./beat_sheet.json) — 12 filled Remotion beats.
- [`SCRIPT.md`](./SCRIPT.md) — narration script + timing table.
- [`SHOTLIST.md`](./SHOTLIST.md) — beat-by-beat visual plan.
- [`FACTCHECK.md`](./FACTCHECK.md) — every on-screen claim, traced.
- [`SOURCES.md`](./SOURCES.md) — primary and doctrine sources with SHA-256s.
- [`PROMPTS.md`](./PROMPTS.md) — reproducible command sequence + handoff prompt.
- [`CHECKS-REPORT.md`](./CHECKS-REPORT.md) — Gate F / Gate V / audio / receipts.
- [`TYPECHECK.md`](./TYPECHECK.md) — manual visual typography review.
- [`VISUAL-REVIEW.json`](./VISUAL-REVIEW.json) — AI review record for the supervisor.
- [`demo/RUN-LOG.txt`](./demo/RUN-LOG.txt) — the actual `./art scenes` output captured against this workspace.

### Vertical (`/vertical`)

Independent paperwork for the portrait aspect:

- [`vertical/beat_sheet.json`](./vertical/beat_sheet.json) — same 12 beats, 916 scene ids.
- [`vertical/CHECKS-REPORT.md`](./vertical/CHECKS-REPORT.md) — portrait Gate F/V + skin-lint notes.
- [`vertical/TYPECHECK.md`](./vertical/TYPECHECK.md) — portrait-specific manual review.
- [`vertical/VISUAL-REVIEW.json`](./vertical/VISUAL-REVIEW.json) — AI review record for the supervisor.

## Re-verification (run_id 55a09dc2)

Re-verified 2026-09-12 under new repoloop run_id `55a09dc2004f4348be10c7ea7756eb86`
(source_sha256 `384e2c88…`). No content change in `art` or `scene_search.py`
versus the Sep-09 build; audio and scene renders are unchanged. Gate V
re-run on both aspects: 0 BLOCKER / 0 MAJOR each. `VISUAL-REVIEW.json`
records updated in landscape root and `vertical/`.

## What's next

Bear watches both files and (if needed) writes edits to
[`FEEDBACK.md`](./FEEDBACK.md). Nothing has been uploaded, transcoded,
published or committed. Publishing, YouTube-side transcoding, and any final
approval remain human workflows.

## Playlist adaptation notes

- Playlist `Brutalist`, channel `@HumanitariansAI`. Composer folder chip
  reads `@HumanitariansAI`; the OUTRO card is the locked `ClaudeTitleOutro`
  with the hardcoded `@NikBearBrown` handle (per `OUTRO-LOCK.md`) —
  intentional and flagged for the human reviewer to confirm before any
  publication.
- Voice unchanged: Kokoro `am_onyx` (Liam, in for Bear) — no paid TTS,
  no captions, no subtitle track.
- Hello lexicon: `Namaste` (Hindi, one word). Fresh — does not repeat the
  icons episode's `Sawubona`. Slug character-sum mod 10 = 3, so no Wagwan
  slot; Wagwan is Bear's alone.

## Known limitations (documented, not suppressed)

- `scripts/type_check.py`, `reference/type-spec.md` and the `kerning` skill
  are referenced by SKILL.md but not shipped in this toolkit revision.
  GATE T's automated typography pass is unavailable; each aspect's
  `TYPECHECK.md` documents the manual visual review that filled in.
- `ClaudeCodeBeat916` does not word-wrap; long code lines are horizontally
  clipped inside the code card in portrait. The Gate V frame-safe check
  still passes (the card itself is inside SAFE916) — fellows should prefer
  the landscape master when reading raw script contents.
- Motion histogram: `code-cascade` is 58 % of beats (over MOTION.md's ~40 %
  pantry cap). The command's evidence IS code and terminal, so this is the
  honest illustration per ILLUSTRATE LAW; documented, not "fixed" by
  swapping in a decorative mechanic.
