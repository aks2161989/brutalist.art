# CHECKS-REPORT — Short 9:16

Run: `582afa9ffa2e46dab272cb6ba6798bfa` · Reel: `claude-liam-brutalist-command-doctor-short` · 2026-09-12 (re-verification pass 2).

Derivative Short cut from the finished 9:16 vertical companion
(`youtube/brutalist/claude-liam-brutalist-command-doctor/vertical`, master SHA-256
`b0554d945529b6c3a8cb1791c816a92c7502fd6179b3f4cdd4fc941aa8c47591`, re-compiled 2026-09-12).
Whole-beat cut, no rewrites, no endcard, no outro rewrite.

## Re-verification context

The parent vertical's B02 beat was re-rendered on 2026-09-12, causing the parent master SHA to change.
B02 is a **dropped beat** in this Short and does not affect Short content.
All 8 kept-beat media files (B00, B01, B03, B04, B06, B08, B09, B11) are confirmed byte-for-byte
unchanged by SHA comparison against build-state.json. The Short export is unchanged.

## Cut plan (CUT-PLAN.json)

- Strategy: `whole-beat-cut`
- Kept beats (8): B00, B01, B03, B04, B06, B08, B09, B11
- Dropped beats (4): B02, B05, B07, B10 — see CUT-PLAN.json for per-beat reasoning
- Planned duration: 141.55 s (well under the 175 s planning ceiling and 180 s hard cap)

## Runtime checks that were run and their outputs

| Check | Command | Result |
|---|---|---|
| Media integrity | SHA-256 of all 8 kept-beat mp4 files vs build-state.json | **All 8 match exactly — unchanged** |
| ffprobe container/video/audio | `ffprobe -select_streams v:0 / a:0 / format` | **container 140.750 s · video 140.750 s · audio 140.750 s · 2160 × 3840 · yuv420p** — all three < 180.0 s (headroom 39.25 s) |
| Audio decode | `ffmpeg -i <mp4> -af volumedetect -vn -f null -` | mean **-27.0 dB** · max **-3.1 dB** · aac muxed cleanly |
| GATE V (original compile) | 16 frames sampled · **BLOCKER 0 · MAJOR 0 · Clean ✓** | (`_qc/REPORT.md`) — frames unchanged, hashes re-confirmed |
| Frame hash re-verification | SHA-256 of 25 QC frame files (3 per kept beat + contact sheet) vs VISUAL-REVIEW.json | **All 25 re-hashed and recorded — unchanged** |

## Duration budget

```
B00  9.541667s   Opening / ASK (composer + Jambo greeting + Do-not-install ask)
B01 14.916667s   BLUF hesitant writer ('installs deps' → 'verifies live')
B03 22.083333s   Two modes, one FEATURES table
B04 15.750000s   Verbatim green run + [exit 0]
B06 23.458333s   Live verification (Kokoro must actually SPEAK above -40 dB)
B08 27.166667s   Falsifiability: hide the model file, red row + hint + exit 1, --install recovery
B09 22.666667s   Verdict — the whole surface, 6 lines
B11  5.166667s   Outro (title restate + @NikBearBrown)
---
    140.749167s planned
    140.750000s measured (container/video/audio)
    Cap:  <180.000000 s — PASS (39.25 s headroom)
```

## SKIN LINT warnings captured (expected)

    SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916'
      — COLD OPEN LAW wants ClaudeComposerAsk
    SKIN LINT: B11: palette=claude but the outro is 'ClaudeTitleOutro916'
      — OUTRO LAW wants ClaudeTitleOutro

Correct-and-expected on a 9:16 build — the 916 variants ARE the portrait cold
open/outro; the lint sees the palette-name mismatch and prints the suggestion.
Same behaviour as every prior portrait/short in this playlist. No action taken.

## Motion histogram (compile.py warning captured verbatim)

    code-cascade:4  type-on:1  hesitant-type:1  artifact-in:1  outro-card:1
    WARNING: 'code-cascade' carries 4/8 beats (50%) — over the ~40% pantry
    cap; convert the excess to another language (MOTION.md)

Every retained code beat carries a distinct real artifact (FEATURES array →
green table → kokoro_synth check → recovery). Accepted, same rationale as the
parent 16:9 and vertical builds.

## Known limitation (carried from the parent)

Long monospace code lines in the portrait `ClaudeCodeBeat916` beats
(B03/B04/B06/B08) truncate at the white card's right edge in the 9:16 render.
Ink stays inside the card, Gate V passes, and the salient part of every line
is legible (row labels, status column, hint indentation, verbs). Full lines
are preserved in the parent 16:9 master and in
`youtube/brutalist/claude-liam-brutalist-command-doctor/demo/RUN-LOG.txt`.

## Provenance

- Parent 9:16 master: `youtube/brutalist/claude-liam-brutalist-command-doctor/exports/vertical/claude-liam-brutalist-command-doctor-vertical.mp4` (SHA-256 `b0554d945529b6c3a8cb1791c816a92c7502fd6179b3f4cdd4fc941aa8c47591`) — not modified by this run
- Short beat sheet: `beat_sheet.json` (SHA-256 `7821a52121d9f66cdcafef68939683f61cd4c5b5a6c780613113e686c50c8abc`)
- Short master: `exports/short/claude-liam-brutalist-command-doctor-short.mp4` (SHA-256 `fbcf7a25d707a7f70b565b68e09505bf69512a9f0e1b613fa86f22db0d85b9d7`)
- All native portrait media/mp3 were independently copied via `shorts.py`; no symlinks or hardlinks.

## Conclusion

Short 9:16 is CLEAN. 4K portrait Short
`exports/short/claude-liam-brutalist-command-doctor-short.mp4` (2160×3840,
140.75 s, aac + h264) rendered from the finished vertical companion via a
whole-beat cut. All three ffprobe durations < 180.0 s. Re-verified 2026-09-12
(run 582afa9ffa2e46dab272cb6ba6798bfa) against unchanged media. VISUAL-REVIEW.json
updated with current run_id and source_sha256; 25 QC frame SHAs re-hashed from files.
Not published.
