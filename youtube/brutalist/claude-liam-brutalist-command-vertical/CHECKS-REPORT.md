# CHECKS-REPORT.md — landscape (16:9)

Run: `ac6edaa227b34224a6622a2702619b03` · `2026-09-12`.
Previous: `5f733dcd6d2249fea636151601143428` · `2026-09-09` (B02 line-number fix rebuild).

## Pipeline stages that ran

1. `generate_audio_kokoro.py` — 12 beats · Kokoro `am_onyx` · all local.
   Durations 5.42–26.90 s · total 247.18 s of narration.
2. `remotion_scenes.py` — 12/12 beats rendered against the registered
   compositions in the isolated toolkit's `Root.tsx` (patched with
   `ClaudeCodeBeat916` + the `BrutalistHesitantWriter.tsx` portrait-scale
   fix). Foreground, serial. No hand-rolled `npx remotion render`.
3. `compile.py --height 2160 --out exports/landscape` — motion histogram
   check ran, brand-lint ran, per-input SHA-256s recorded in the
   `verified.json` receipt.
4. Frame extraction — per-beat samples at 15 % / 50 % / 85 % (36 PNGs)
   written to `_qc/landscape/frames/`. Contact sheet at
   `_qc/landscape/contact-sheet.png`. Read with the image-capable Read
   tool — no BLOCKER or MAJOR observed.
5. `ffprobe` on the final MP4:
   - video: 3840×2160 @ 24 fps
   - audio: AAC 48 kHz stereo, 247.458 s
   - format duration matches sum of measured narration + per-beat pads.

## Warnings observed (accepted)

- `motion histogram: code-cascade:7/12 (58%) — over the ~40% pantry cap`.
  Accepted for a command-teardown episode whose whole point is walking
  through code excerpts; every code-cascade beat quotes a distinct
  source file/section. The alternative — replacing the code cards with
  diagrams — would defeat the "read the actual source" premise of a
  command explainer.

## Gate coverage

| Gate | Status | Evidence |
|---|---|---|
| Audio decodes | PASS | ffprobe audio stream present, 247.458 s |
| Video dimensions | PASS | 3840×2160 |
| Per-input hashes | PASS | 24 hashes in `verified.json` (12 mp4 + 12 mp3) |
| Frame-level QC (compile Gate V) | PASS | compiler completed and wrote `verified.json`; no BLOCKER or MAJOR |
| Motion pantry | WARN | code-cascade 58 % — accepted (see above) |
| Skin-lint | PASS | no COLD-OPEN / OUTRO-LOCK violations on landscape |

## Missing checkers (recorded honestly)

- `scripts/type_check.py` / `reference/type-spec.md` (referenced by
  older docs) — not present in this toolkit revision. The compiler's
  Gate V (`runtime/qc/final_frame_check.py`) ran; visual typography
  review was done by extracting per-beat frames and reading them with
  the image-capable Read tool. See `TYPECHECK.md`.
- ILLUSTRATIONS.md / kerning skills — referenced by legacy docs, not
  in this toolkit. Not applicable to this episode (no icon-grid, no
  custom kerning).

## Nothing uploaded

The mp4 sits in `exports/landscape/`. Bear's viewing/editing is the
next step. No transcoding, upload, GitHub push, or scheduling occurred.
