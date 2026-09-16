# CHECKS-REPORT — The duration-planner Skill · Short (9:16)

Run id: `de2486504f054fb0952577d82d7fc24c`.
Supervisor `episode.source_sha256`: `070aeda8cb13ae68370dec38ebb9bd008db71cb25644d14b62320eb49f5ae02c`.
Parent master SHA-256: `82e1bd11b25b1243becdf762631892904c774deb296f6b5c47db59b6aafca39c`.

## Cut plan → executed as-planned

- Strategy: `whole-beat-cut`.
- Kept: `B00, B01, B04, B05, B07, B08, B10` (7 of 11 parent beats).
- Dropped: `B02, B03, B06, B09` (4 beats).
- Planned duration: 120.7 s. Measured: 120.708 s (container/audio) / 120.667 s (video). ✓
- Endcard: none (`--no-endcard`). Outro: preserved from parent (`--no-outro-rewrite`).
- Rewrite reason: `null` (whole-beat cut fit and reads coherent).

## Portrait dimension audit (all sources verified before beat_sheet write)

Every retained parent-vertical media file was probed for native portrait
dimensions. All are 2160×3840 native compositions — no center-cut, no crop
was performed.

| Beat | Source | Width×Height |
|---|---|---|
| B00 | `media/B00.mp4` | 2160×3840 ✓ |
| B01 | `media/B01.mp4` | 2160×3840 ✓ |
| B04 | `media/B04.mp4` | 2160×3840 ✓ |
| B05 | `media/B05.mp4` | 2160×3840 ✓ |
| B07 | `media/B07.mp4` | 2160×3840 ✓ |
| B08 | `media/B08.mp4` | 2160×3840 ✓ |
| B10 | `media/B10.mp4` | 2160×3840 ✓ |

## The Short's file

- Path: `exports/short/claude-liam-brutalist-skill-duration-planner-short.mp4`
- SHA-256: `2468c31d2892d652507c6181aed9cb673549dea232a5426ca099caaf63862915`
- Size: 6.92 MB (7,255,237 bytes).
- Video: h264, 2160×3840, 24 fps, duration **120.666667 s**.
- Audio: AAC, duration **120.708000 s**.
- Container: duration **120.708000 s**.
- All three durations strictly < 180.0 s (Shorts cap satisfied with 59.29 s
  of headroom). ✓

## Cap check (build_safety.require_short_duration)

`shorts.py` printed `[short] 7 beats · ~120.7s (2:00.7) OK`. Compiler finished
without a duration guard failure.

## Audio decode & join review

Decoded to `_qc/audio.wav` (mono, 22050 Hz) and scanned with `loudnorm=print_format=json`:

- Integrated loudness (input_i): **-27.68 LUFS**.
- True peak (input_tp): **-4.45 dBTP** — no clipping.
- Loudness range (input_lra): **5.20 LU** — moderate.

Kokoro `am_onyx` per-beat mp3s were copied unchanged from the parent vertical;
loudness matches the parent film. The parent film is the approved reference.
No normalisation was applied (would have re-encoded and re-hashed the audio,
breaking the byte-identity contract with the parent).

Joins were inspected at the six beat boundaries (`_qc/beat_frames/` at 15 %
and 85 % of each beat). Read verbatim in `SCRIPT.md`, the narration
transitions land clean:

- **B00 → B01**: "…here is how it actually works." → "The easy assumption is that duration is a target you hit…" Natural.
- **B01 → B04**: "…production convenience or padding." → "First design decision, and it's the thesis." Natural — B04 IS the first design decision; no dangling first/second/third pairing.
- **B04 → B05**: "Either way, learning fails." → "Second decision." The 1st/2nd pair is preserved intact; the parent's "Third decision" (B06) was dropped, and no retained beat says "third".
- **B05 → B07**: "Add a hold." → "Here is where the skill bites." Natural.
- **B07 → B08**: "…shorter watchtime, cleaner schema." → "The verdict." Natural payoff.
- **B08 → B10**: "…production wanted for its own convenience." → "That was the duration-planner Skill. Liam, in for Bear." Natural.

## First / final frames

- First frame (0.02 s, `_qc/frames/first.png`) — cream ground with fade-in
  eyebrow "BRUTALIST · SKILL TEARDOWN". Matches the B00 cold-open cue at
  `0.02`.
- Final frame (120.5 s, `_qc/frames/final.png`) — locked ClaudeTitleOutro916
  with "The duration-planner Skill." title, terracotta period, `@NikBearBrown`
  handle, framed by top/bottom hairlines. Matches OUTRO-LOCK.

## Legibility & portrait framing

Inspected the 21 beat-relative 15 %/50 %/85 % frames (`_qc/beat_frames/`).
All are 2160×3840 with no burned-in captions, no logo bleed, no
`channel_title` overlay (the parent deliberately omitted `metadata.channel_title`
to avoid the documented portrait bottom-bleed — see feedback memory
`feedback_channel_title_portrait_bleed`).

- **B00**: composer card with `Sawadee, Liam` greeting, the ask, folder chip
  `@HumanitariansAI`, and three answer lines (`duration is an OUTPUT, not a
  target` / `script-sizing and holds are the two real levers` / `content_type
  sets the consolidation floor`) — all within the safe area.
- **B01**: hesitant-writer serif fills the vertical safe area with the
  target-to-output flip landing in the middle third.
- **B04**: `SkillTeardownMechanism916` — MECHANISM · ACT 1 eyebrow, "Duration
  is an output." heading, body about 3–4 min vs 30–60 s, verbatim SKILL.md
  quote block, `KILLS THE 30S/1MIN PRODUCTION MYTH` terracotta pill, "Content
  decides the clock." sparkline.
- **B05**: `SkillTeardownMechanism916` — MECHANISM · ACT 2 eyebrow, "The
  consolidation floor." heading, floor row (title 3–5s / realworld 4–5s /
  structure 6–8s / data 6–8s / mechanism 6–10s / equation 7–12s), verbatim
  SKILL.md quote ("Floors are minimums, enforced with holds."), `THE
  LOAD-BEARING RULE` terracotta pill, "Working memory needs the seconds."
  sparkline.
- **B07**: `SkillTeardownMechanism916` — DESIGN · TELL eyebrow, "Padding is a
  coherence violation." heading, MOOC-watchtime-rule debunk body, verbatim
  SKILL.md quote ("Padding to reach 1:00 is as wrong as compressing to reach
  0:30."), grey `TRADES WATCHTIME FOR SCHEMA` pill (verdictPositive: false
  — the real cost is documented, not glossed), "Engagement is not the target."
  sparkline.
- **B08**: `ClaudeVerdictArtifact916` — six-line verdict card centred, all
  lines readable.
- **B10**: outro title, terracotta period, `@NikBearBrown` handle centred in
  the middle third; top/bottom hairlines frame the composition.

Contact sheet: `_qc/contact/f0001.png … f0241.png` at 2 fps (241 thumbnails,
270×480) retained for scrubbing.

## Skin lint

Compiler printed two skin-lint warnings inherited from the parent vertical
build stamp:

- `B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk`
- `B10: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro`

These are false-positive lints — the `*916` variants are the correct portrait
compositions for the 9:16 companion, and the parent vertical build stamp
carries the same warning history without a blocker. Recorded here to preserve
the parent's build stamp accurately, not because the Short introduced them.

## No fabricated approvals

`approvals: {}` in the beat_sheet metadata. Human review is pending; Bear's
viewing and editing is next. Publishing is a separate authorized workflow
governed by `docs/FELLOWS-SUBMISSION.md`.
