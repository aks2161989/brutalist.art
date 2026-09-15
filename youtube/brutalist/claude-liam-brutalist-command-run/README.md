# Brutalist Command: art run

Episode 33 of the Brutalist playlist, adapted for @HumanitariansAI.
Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`. Register: Teardown.
12 beats. Command teardown of `./art run` — the dispatcher case at
`art:99-101` that wraps `bash runtime/scripts/run.sh` and drives the
whole review loop (Gate F → L → SHAPE → A → W → render + B →
Remotion → compile → V). Aliases: none.

**Re-rendered 2026-09-12** (run_id `df4ab48ebf354eecb12e6a7d2316a270`): the
`art` dispatcher grew a longer `--list` section (20 skills), moving the
`run)` case from lines 78-80 to 99-101. Beat B02 title card was corrected
and re-rendered in both aspects; all other beats and audio are unchanged.

**Vertical B09 fix 2026-09-12** (run_id `c1279719c5a743589fcfc4f9dc2a4468`): the
vertical B09 clip (ClaudeVerdictArtifact916) was stale — the beat_sheet.json
already carried `art:99-101` in verdict line 6 but the clip had not been
re-rendered when landscape B09 was fixed. Vertical B09 re-rendered using a
C binary chrome wrapper with `--disable-features=MojoIpcz` (Apple App Sandbox
Mach-port fix). Vertical recompiled; Gate V: 0 BLOCKER / 0 MAJOR. Both
aspects now correctly read `art:99-101` in the verdict card.

## Deliverables (local files — not published)

- **Landscape (16:9, 4K):** `exports/landscape/claude-liam-brutalist-command-run.mp4` · 3840×2160 · 245.583 s · h.264 + AAC.
- **Vertical (9:16, 4K):** `exports/vertical/claude-liam-brutalist-command-run-vertical.mp4` · 2160×3840 · 245.583 s · h.264 + AAC.

Both files are native 4K layouts (not upscaled cropped masters). Both
passed `final_frame_check.py` (Gate V) with 0 BLOCKER and 0 MAJOR
defects. Each ships alongside its `verified.json` receipt.

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
- [`demo/RUN-LOG.txt`](./demo/RUN-LOG.txt) — the actual `./art run` output captured against `/tmp/claude-501/art-run-demo/`.

### Vertical (`/vertical`)

Independent paperwork for the portrait aspect:

- [`vertical/beat_sheet.json`](./vertical/beat_sheet.json) — same 12 beats, `*916` scene ids.
- [`vertical/CHECKS-REPORT.md`](./vertical/CHECKS-REPORT.md) — portrait Gate F/V + skin-lint notes.
- [`vertical/TYPECHECK.md`](./vertical/TYPECHECK.md) — portrait-specific manual review.
- [`vertical/FACTCHECK.md`](./vertical/FACTCHECK.md) — portrait-specific claims (identical to landscape apart from the B01/B10 wording deltas noted in the report).
- [`vertical/VISUAL-REVIEW.json`](./vertical/VISUAL-REVIEW.json) — AI review record for the supervisor.

## What's next

Bear watches both files and (if needed) writes edits to
[`FEEDBACK.md`](./FEEDBACK.md). Nothing has been uploaded, transcoded,
published or committed. Publishing, YouTube-side transcoding, and any
final approval remain human workflows.

## Playlist adaptation notes

- Playlist `Brutalist`, channel `@HumanitariansAI`. Composer folder chip
  reads `@HumanitariansAI`; the OUTRO card is the locked `ClaudeTitleOutro`
  with the hardcoded `@NikBearBrown` handle (per `OUTRO-LOCK.md`) —
  intentional and flagged for the human reviewer to confirm before any
  publication.
- Voice unchanged: Kokoro `am_onyx` (Liam, in for Bear) — no paid TTS,
  no captions, no subtitle track.
- Hello lexicon: `Ciao` (Italian, one word). Fresh — does not repeat the
  scene-index (Bonjour), scenes (Namaste), icons (Sawubona), list
  (Salaam), icon-build (Merhaba), or help (Namaste) episodes. Slug
  character-sum mod 10 = 3, so no Wagwan slot; Wagwan is Bear's alone.

## Known limitations (documented, not suppressed)

- `runtime/qc/type_check.py`, `reference/type-spec.md` and the `kerning`
  skill are referenced by SKILL.md but not shipped in this toolkit
  revision. GATE T's automated typography pass is unavailable; each
  aspect's `TYPECHECK.md` documents the manual visual review that
  filled in.
- `ClaudeCodeBeat916` does not word-wrap; long code lines are
  horizontally clipped inside the code card in portrait. The Gate V
  frame-safe check still passes (the card itself is inside SAFE916) —
  fellows should prefer the landscape master when reading raw script
  contents.
- Motion histogram: `code-cascade` is 58% of beats (over MOTION.md's
  ~40% pantry cap). The command's evidence IS its dispatcher, its
  source, and its observed output, so this is the honest illustration
  per ILLUSTRATE LAW; documented, not "fixed" by swapping in a
  decorative mechanic.
- Two sandbox workarounds were applied before Remotion could render:
  a `node_modules` shadow (webpack `.cache/` writability) and an
  `ART_CHROME` wrapper (`chrome-headless-shell --single-process`).
  Neither changes what `art run` does; both are documented in
  `PROMPTS.md` and in agent memory.
- `BrutalistHesitantWriter` needed a 4-line portrait-scale patch in
  the isolated toolkit's copy of the component so the 9:16 canvas
  didn't collapse `scale` to 0.5625. The shared toolkit is unchanged.
