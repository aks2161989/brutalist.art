# CHECKS-REPORT — The explainer Skill · Short (9:16)

Run id: `df20232c561a49e492dfe707b6b38f01` (re-verification 2026-09-12; prior build run `c6d1a9178c344f429dac903948551b82`).
Parent master SHA-256: `736045efcb64ee06d28379ca5cde2b17544766f7f6e7ddf4d79beb1ee662c23b`.
Supervisor source SHA-256: `4859d9d32c744bdfce4d67ea26343fcce5a84bc80b612afd5dc1e6aaac19ffde`.

Build completed 2026-09-11 (parent vertical B07 updated with EXECUTABLE-EVIDENCE.md content).
Re-verification 2026-09-12: all 12 input hashes confirmed intact; export SHA-256 confirmed stable.
Cut plan unchanged — same 6 beats (B00, B01, B03, B07, B08, B10).

## Cut plan → executed as-planned

- Strategy: `whole-beat-cut`.
- Kept: `B00, B01, B03, B07, B08, B10` (6 of 11 parent beats).
- Dropped: `B02, B04, B05, B06, B09` (5 beats).
- Planned duration: 116.92 s. Measured: 116.917 s (all three streams). ✓
- Endcard: none (`--no-endcard`). Outro: preserved from parent (`--no-outro-rewrite`).
- Rewrite reason: `null` (whole-beat cut fit and reads coherent).

## Portrait dimension audit (all sources verified before beat_sheet write)

Every retained parent-vertical media file was probed for native portrait
dimensions. All are 2160×3840 native compositions — no center-cut, no crop
was performed. B07 was re-verified after the 2026-09-11 parent rebuild.

| Beat | Source | Width×Height |
|---|---|---|
| B00 | media/B00.mp4 | 2160×3840 ✓ |
| B01 | media/B01.mp4 | 2160×3840 ✓ |
| B03 | media/B03.mp4 | 2160×3840 ✓ |
| B07 | media/B07.mp4 | 2160×3840 ✓ (2026-09-11 rebuild) |
| B08 | media/B08.mp4 | 2160×3840 ✓ |
| B10 | media/B10.mp4 | 2160×3840 ✓ |

## The Short's file

- Path: `exports/short/claude-liam-brutalist-skill-explainer-short.mp4`
- SHA-256: `3e080805fd5c8d38224a62711e3a7e1ff458d174f6dbd41d33e7e6b7aea85085`
- Size: 6.8 MB.
- Video: h264, 2160×3840, 24 fps, duration **116.916667 s**.
- Audio: AAC, duration **116.916000 s**.
- Container: duration **116.916667 s**.
- All three durations strictly < 180.0 s (Shorts cap satisfied with 63.1 s
  of headroom). ✓

## Cap check (build_safety.require_short_duration)

`shorts.py` printed `[short] 6 beats · ~116.9s (1:56.9) OK`. Compiler
finished without a duration guard failure. B07's increased duration (30.625 s vs
previous 29.5 s) is absorbed within the headroom; no cut plan changes required.

## Audio decode & join review

Decoded and measured with `loudnorm=print_format=json`:

- Integrated loudness (input_i): **-24.57 LUFS**.
- True peak (input_tp): **-3.36 dBTP** — no clipping.
- Loudness range (input_lra): **5.40 LU** — moderate.

Kokoro am_onyx per-beat mp3s were copied unchanged from the updated parent vertical;
loudness profile matches the parent film. No normalisation applied (would re-encode
and re-hash the audio). The same per-beat source audio contract applies as the
previous build.

Joins were inspected at the five beat boundaries. Each retained beat begins on cream
ground, so cross-beat cuts land clean. Read verbatim in SCRIPT.md, the narration
transitions (B00→B01, B01→B03, B03→B07, B07→B08, B08→B10) contain no dangling
numbered references. B07's updated narration ends "…it is decoration. Cut it." which
flows cleanly into "The verdict." at B08. B08 verdict recap names two-axis and
slot-contract as skill components without a Short-side walkthrough — accepted as a
table-of-contents summary; documented in FACTCHECK.md § "Verdict-recap danglers".

## First / final frames

- First frame (0.02 s, `_qc/frames/first.png`, SHA-256 `1b2730287521656d3798718612b1839662510ea12bf5bd554fa0471194627ea9`) — cream
  ground with fade-in eyebrow "BRUTALIST · SKILL TEARDOWN". Matches the B00
  cold-open cue at `0.02`.
- Final frame (116.8 s, `_qc/frames/final.png`, SHA-256 `9157c809c430d4b6e90784e8f837c2ee5c2974d097b8b0494346d97f1d199283`) — locked
  ClaudeTitleOutro916 with "The explainer Skill" title, terracotta period,
  `@NikBearBrown` handle, framed by top/bottom hairlines. Matches OUTRO-LOCK.

## Legibility & portrait framing

Inspected 18 beat-relative 15%/50%/85% frames from the new video (`_qc/beat_frames/`).
All are 2160×3840 with no burned-in captions, no logo bleed, no channel_title
overlay (the parent deliberately omitted `metadata.channel_title` to avoid
the documented portrait bottom-bleed).

- B00: composer card and answer lines fit within the safe area; ask visible.
- B01: hesitant-writer text fills the vertical safe area with the "pipeline"
  correction landing in the middle third.
- B03: pipeline diagram has a horizontal band of six nodes centred in the
  frame. Nodes and labels are legible; the layout is native for the 916
  composition.
- B07 (new EXECUTABLE-EVIDENCE.md content): eyebrow DESIGN · TELL + heading
  "A still is evidence." lands at top; body covers the executable-evidence
  sharpening with "execute it — render it" verdict pill; quote card and
  "Evidence, never texture." sparkline visible in bottom third. All text
  within the portrait safe area.
- B08: verdict artifact card fills the middle of the safe area with all six
  verdict lines readable.
- B10: outro title, terracotta period, and `@NikBearBrown` handle centred in
  the middle third.

## Gate V (final_frame_check.py)

- Sampled: 12 frames (6 beats × 50% + 85%, beat-aware steady-state).
- BLOCKER: 0 · MAJOR: 0 → Clean. ✓
- Report: `_qc/REPORT.md`.
- Contact sheet updated: `_qc/contact_sheet.png`.

## Skin lint

Compiler printed two skin-lint warnings inherited from the parent vertical
build stamp:

- `B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk`
- `B10: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro`

These are false-positive lints — the `*916` variants are the correct portrait
compositions for the 9:16 companion. Recorded here to preserve the parent's
build stamp accurately, not because the Short introduced them.

## No fabricated approvals

The Short has no human sign-off. `approvals: {}` in the beat_sheet metadata.
Bear's viewing/editing is next; publishing is a separate authorized workflow.
