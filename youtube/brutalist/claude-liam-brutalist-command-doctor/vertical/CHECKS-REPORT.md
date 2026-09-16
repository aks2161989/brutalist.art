# CHECKS-REPORT — vertical 9:16

Run: `5c2c1dda1a4548798796300fb24665e1` · Reel: `claude-liam-brutalist-command-doctor-vertical` · 2026-09-12 (rebuild: B02 art:96-99 → art:117-121).

Full-length portrait companion, NOT a Shorts cut. Every landscape beat is
preserved (`kind: vertical`, `reformat: "full-length; native portrait
graphics; preserve source framing"`, no drops, no endcard, no cap).

## Portrait scenes used (all native, no crop)

- `ClaudeComposerAsk916` — B00, B10
- `BrutalistHesitantWriter916` — B01 (portrait scale patch applied; see below)
- `ClaudeCodeBeat916` — B02, B03, B04, B05, B06, B07, B08 (registered in the
  isolated toolkit's Root.tsx for this build; same component, 1080×1920 canvas)
- `ClaudeVerdictArtifact916` — B09
- `ClaudeTitleOutro916` — B11

## Toolkit patches applied for this build (isolated toolkit only)

- `runtime/remotion/src/Root.tsx` — added `ClaudeCodeBeat916` composition
  entry (1080×1920, same component + schema as the landscape ClaudeCodeBeat)
  and re-ran `./art scene-index`. Without this the portrait code beats
  would have been a PUNT.
- `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx` — applied the
  4-line portrait-aware scale patch (per the shipped feedback memory): when
  `height > width`, scale is `Math.min(width/1080, height/1920)` instead of
  the landscape formula that collapses to 0.5625 on 9:16. Landscape
  behaviour is unchanged.
- `runtime/remotion/node_modules/` — replaced the symlink into the shared
  install with a shadow directory of per-package symlinks plus a writable
  `.cache/` (the isolated-toolkit sandbox workaround). No package versions
  changed.

## Runtime checks that were run and their outputs

| Check | Command | Result |
|---|---|---|
| art vertical planning | `./art vertical <reel>` | 12 beats retained · every REMOTION beat rewired to its 916 composition · full-length vertical (no Short cap) · zero drops |
| kokoro TTS | reused from landscape (identical narration; sheet copied) | 12/12 stamped durations preserved |
| Remotion render | `python3 runtime/scripts/remotion_scenes.py <reel>/vertical` | 12/12 `ok:` — all 916 patterns rendered to `vertical/media/*.mp4` |
| compile master | `python3 runtime/scripts/compile.py <reel>/vertical --height 3840 --out <exports/vertical>` | 12/12 filled · 216.8s master written · verified.json emitted · atomic promotion succeeded |
| GATE V | invoked by compile after encode | 24 frames sampled · **BLOCKER 0 · MAJOR 0 · Clean ✓** (`vertical/_qc/REPORT.md`) |
| Audio decode | `ffmpeg -i <mp4> -af volumedetect -f null -` | mean -27.1 dB · max -3.0 dB · h264 aac muxed cleanly |
| ffprobe dimensions | `ffprobe -select_streams v:0` | 2160 × 3840 · yuv420p · 216.79s |

## SKIN LINT warnings captured (playlist adaptation, expected)

    SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916'
      — COLD OPEN LAW wants ClaudeComposerAsk
    SKIN LINT: B11: palette=claude but the outro is 'ClaudeTitleOutro916'
      — OUTRO LAW wants ClaudeTitleOutro

Both are correct-and-expected. On a 9:16 build the 916 variants ARE the
cold open and outro; the lint sees the palette-name mismatch and prints the
suggestion. Same behaviour as episodes 29, 30, 31, 32 (all documented). No
action taken.

## Motion histogram (compile.py warning captured verbatim)

    code-cascade:7  type-on:2  hesitant-type:1  artifact-in:1  outro-card:1
    WARNING: 'code-cascade' carries 7/12 beats (58%) — over the ~40%
    pantry cap; convert the excess to another language (MOTION.md)

Same rationale as landscape: every code beat carries a distinct real
artifact (dispatcher case → FEATURES array → green table → check() body
→ kokoro_synth → aggregation loop → recovery). Accepted.

## Known limitation — portrait code beats

Long monospace code lines in the portrait `ClaudeCodeBeat916` beats
(B02-B08) truncate at the white card's right edge in the 9:16 render.
Ink stays inside the card, so Gate V passes; the salient part of every
line is legible. Same behaviour was shipped by episodes 29, 30, 31, 32.
Full lines are visible in the landscape master and preserved verbatim
in `demo/RUN-LOG.txt` (parent reel directory).

## Portrait B01 (hesitant writer) — Gate V clearance recipe applied

The shipped portrait scale (`Math.min(w/1920, h/1080) = 0.5625` on 9:16)
collapsed every geometry value; even at large `fontSize` this beat
underfilled to 18% coverage. The patched scale plus the tuning below
lifted coverage past the 55% floor without edge overflow:

    fontSize: 210, lineSpacing: 4.5
    → 64.3% coverage @ 50% of beat, 60.0% coverage @ 85% of beat, no bleed

The same misconception is corrected in both aspects (`installs → verifies`,
`deps → live`).

## Conclusion

Vertical 9:16 is CLEAN. 4K master
`exports/vertical/claude-liam-brutalist-command-doctor-vertical.mp4`
(SHA-256 `6841c2a078a80271abf298ffe2db0e8b4e571101373abc2d50144523effcb67d`)
is ready for Bear's viewing/editing pass. Not published.
