# CHECKS-REPORT — landscape (16:9)

Run: `e66ff34b0ab34b038ee5d5d5b8cb13b4`
Source SHA: `30d1a0602e5816a06a443392ae6edbf3ac24abec02a10d14a575c6dd6aa13f46`

`claude-liam-brutalist-command-todo.mp4` — 3840x2160 @ 24 fps, 167.875 s,
h.264 (yuv420p) + AAC 48 kHz stereo. Duration matches the measured per-beat
audio timeline recorded in `exports/landscape/claude-liam-brutalist-command-todo.verified.json`.

## Gate F — factcheck

- `FACTCHECK.md` present, non-empty; every on-screen claim traces to the
  isolated toolkit's `art todo` implementation
  (`runtime/scripts/todo.py` @ SHA `050b07d7...` per SOURCE-SNAPSHOT.json)
  and the `art` dispatcher (`SHA` fingerprinted in SOURCES.md).
- `SOURCES.md` records the two primary source hashes matching
  `SOURCE-SNAPSHOT.json`.

Pass.

## Gate V — visual QC (final_frame_check.py)

```
Frames sampled: 24  ·  BLOCKER: 0  ·  MAJOR: 0
Clean — no BLOCKER/MAJOR defects. ✓
```

Full report in `_qc/REPORT.md`; contact sheet at `_qc/contact_sheet.png`
(inspected via image-capable Read). Supplemental single-beat evidence frames
extracted from the CURRENT master this invocation:
`_qc/B00_evidence.png`, `_qc/B01_evidence.png`, `_qc/B04_evidence.png`,
`_qc/B09_evidence.png`, `_qc/B10_evidence.png`, `_qc/B11_evidence.png`
— each hashed and recorded in `VISUAL-REVIEW.json`.

Pass.

## Audio decode

`ffprobe` confirms a single AAC-LC stereo stream in the final master
(48000 Hz), matching the per-beat MP3 SHA-256 map in
`exports/landscape/claude-liam-brutalist-command-todo.verified.json`
(12 mp3s, ba9ff174... through 0f7a29da...). No beat is silent; narration
decodes cleanly across every seam.

Pass.

## Compiler receipts

`exports/landscape/claude-liam-brutalist-command-todo.verified.json` records:
- `status: ready` (automated export checks passed — human review pending)
- output SHA-256 `cc0a885f6663f08270f5c169a707be66ab48e1055e9ea754c9a0bf1f159c4327`
- 12 per-beat mp4 hashes + 12 per-beat mp3 hashes
- 167.875 s duration
- built at `2026-09-09T14:37:03.010885+00:00`

## Skin lint / motion histogram

The landscape reel emits no SKIN LINT warnings — every beat uses the native
landscape composition. Motion histogram is well distributed across
`type-on / write-and-correct / flow-in / stagger / type-and-stagger /
field-scan / table-stagger / loop-step / fail-then-fix / artifact-stagger /
fade`; no single mechanic passes the ~40% pantry cap.

## Known limitations

- The absent legacy `scripts/type_check.py` / `reference/type-spec.md` /
  `kerning` skill mean GATE T's automated typography pass could not run.
  The manual visual review documented in `TYPECHECK.md` fills that role.
- `ILLUSTRATIONS.md` (referenced by SKILL.md) is not shipped; not needed
  for this reel — recorded gap, not a defect.

Every current runtime check that exists in this toolkit was run against
the episode and returned clean. Nothing was disabled or bypassed.

Human review is pending (Bear's viewing and any edits to `FEEDBACK.md`).
