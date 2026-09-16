# CHECKS-REPORT — The logo-motion Skill — Short

Run ID: `9a15cd534e8541e39d125daabe5a3e2d`
Episode ID: `skill-logo-motion`
Slug: `claude-liam-brutalist-skill-logo-motion-short`
Deliverable: `exports/short/claude-liam-brutalist-skill-logo-motion-short.mp4`

## Cut plan → final

- Kept: **B00 B01 B04 B05 B09 B11** (6 beats).
- Dropped: **B02 B03 B06 B07 B08 B10** (6 beats). Rationale per beat in
  `CUT-PLAN.json`.
- Strategy: `whole-beat-cut`. No narration or beat was rewritten.
- Endcard: none (`--no-endcard`). Ends on parent outro B11.
- Outro rewrite: none (`--no-outro-rewrite`).

## Duration budget

- Sum of parent `render_duration_s` for kept beats: **139.04 s**.
- Compile.py measured runtime: **139.0 s** (compile line: "139.0s").
- ffprobe container duration: **139.041667 s**.
- ffprobe video stream duration: **139.041667 s**.
- ffprobe audio stream duration: **139.041000 s**.
- Sum of per-beat MP3 durations (ffprobe): **138.965 s**.
- SHORTS_CAP: 180.0 s (strict). All four measured values above **< 180.0 s**.

## Portrait framing

- All six kept beats identified by `shorts.py` as native 9:16 (2160×3840) and
  reused unmodified. Log lines: `[short] Bxx native portrait reused unchanged`.
- ffprobe on final: `width=2160, height=3840` → aspect ratio exactly 9:16.
- No landscape master was cropped. No pantry override was used.

## Audio integrity

- Byte-independent copies of parent `mp3/beat-<bid>.mp3` files, one per kept
  beat. Six MP3 files, six audio stream durations that match the parent's
  reported `actual_duration_s` values (rounded).
- `ffmpeg silencedetect noise=-45dB d=0.5` on the final audio produced **no
  matches** — no unexpected long silences at joins.
- Every kept beat's audio duration is positive and less than the beat's
  render duration (audio ≤ video per beat).

## Video integrity

- Six `media/Bxx.mp4` copies. SHA-256 of each recorded in `_qc/frames.json`
  build log and repeated below.
- Compile stamp: 6/6 filled, all VIDEO.
- Motion histogram: `reveal:3 type-on:2 hold:1`.

## Frame evidence

Frames were extracted at beat-relative 15% / 50% / 85% timestamps and stored
under `_qc/frames/`. Eighteen PNGs total, each SHA-256'd — see
`VISUAL-REVIEW.json` for the full list. Read-tool inspection of B00-50,
B01-50, B04-50, B05-50, B09-50, and B11-50 confirmed:

- B00 composer (`Hola, Liam` + typed command + three result lines) fits inside
  portrait SAFE916.
- B01 `A new logo / needs / a new prop. / Add the prop.` shows the corrected
  serif line with visible cursor bar; wraps clean, no bleed.
- B04 mechanism card: eyebrow `MECHANISM · ACT 1`, heading "The build is a
  camera move.", quote block with `Source: logo-motion reference/TIMING.md`
  cite, verdict pill `PULL BACK, NOT FADE IN`, sparkline `Camera pulls. Mark
  holds.` — all inside the portrait column.
- B05 mechanism card: eyebrow `MECHANISM · ACT 2`, heading "The ghost hold IS
  the effect.", full phase-map body copy, quote, verdict pill `44% OF THE
  RUNTIME, INVISIBLE`.
- B09 verdict artifact: title "The logo-motion Skill", heading "One
  composition. Every mark.", six numbered recap lines readable.
- B11 outro: title "The logo-motion Skill." with terracotta period, handle
  "@NikBearBrown".

## SHA-256 provenance

Final render:
`7414ce4fbd82f54cdd2ffe19d826a41799e4a3beaec4deb925a87aeffb57b6b8  exports/short/claude-liam-brutalist-skill-logo-motion-short.mp4`

Derivative beat sheet:
`4a193b04ae04a32bf3f86aa5ac1323058c3166582bba34233bfd0a0c1d6ae862  beat_sheet.json`

Media copies:
`416fffd44fd6a5cb714421a105f091016e53fb1211e17749ea9bca39f55753c5  media/B00.mp4`
`a1d9f57da94aa3749d30fe355789a2faed512c6f2fe426be94104fbfc912092f  media/B01.mp4`
`8f8c55e26d34e647036ba5a7133ab06d744dd48f7a84353f28a4264c8450aabb  media/B04.mp4`
`42a29850881cc8a20276a67fc328fc80aa3de73d459739262fce80870538c4b6  media/B05.mp4`
`04898e47f03167418627779785bc7c334097e6eeb816812a6e96471fac8f27a9  media/B09.mp4`
`423d9612c48163787ede18a07dfbef2ef595e9e260ce19063f9a01a8ce473059  media/B11.mp4`

Audio copies:
`d36c203227e64f7f95c40958abcc80edf325a9af9cfae41231d06371711dc4e0  mp3/beat-B00.mp3`
`13fd3071079a7e95fb6b2b90f52e14fc23683f4f9bf0f1031857efa5dc258d4a  mp3/beat-B01.mp3`
`6432a773ecd258e15afca4258dcc5254d76edd043b83a622c4bf85fc52c27027  mp3/beat-B04.mp3`
`f602a730cbbd8bf68ceb4d4e83f14192e9e14645fb7819334e06ba227f3b4e4e  mp3/beat-B05.mp3`
`6ff8838da4fcced72e091f18605d1213b895d6897db850da16ab9da16ab9c6ea  mp3/beat-B09.mp3`
`1bcf7852a3a0ca54eeb651be2b88fbc812bbb320305ce6046e0261e7d8f67711  mp3/beat-B11.mp3`

Parent master:
`604bfb62a0cfcc34606cb8defe8a042671b4eb4d58b4c951284a8dc6d6c5dff2  (parent .../vertical/claude-liam-brutalist-skill-logo-motion-vertical.mp4)`

Source-of-record (from BUILD-PROMPT episode.source_sha256):
`eca4952b8cf9f4a246e2d541eb631d3a23554831f1a64ed48129ffa1654021d1`

## Blockers / majors / minors

- Blockers: **0**.
- Majors: **0**.
- Minors: **2** (skin-lint on B00 and B11 for `*916` wrappers — carried over
  from parent, documented non-blockers).

## No forbidden actions

- No file was written outside this Short's workspace or its `exports/short/`
  directory.
- No git push, no upload, no publish, no external network call.
- No parent beat sheet, parent master, or parent media/audio file was
  modified. The parent's `exports/`, `media/`, `mp3/` remain byte-identical to
  their state before this run.
- No fabricated human review; the VISUAL-REVIEW.json below is an AI review
  under the current run_id, and its `notes` explicitly declare that human
  review is pending.
