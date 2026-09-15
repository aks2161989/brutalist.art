# CHECKS-REPORT.md — Brutalist Command: art smoke (vertical companion)

Run at: 2026-09-12 UTC · run_id `e6fb28666cd04b18b360c7b6af6d7995`.
This is a full-length native 9:16 companion (per `art vertical`), not a Short.
No drops, no duration cap, no rewritten outro.

## Aspect adaptation

- Every 16:9 Remotion beat re-rendered against its native 9:16 sibling —
  `ClaudeComposerAsk` → `ClaudeComposerAsk916`, `BrutalistHesitantWriter` →
  `BrutalistHesitantWriter916`, `ClaudeCodeBeat` → `ClaudeCodeBeat916`
  (registered locally in this isolated toolkit's Root.tsx — see
  `scene-source-manifest.json`), `ClaudeVerdictArtifact` →
  `ClaudeVerdictArtifact916`, `ClaudeTitleOutro` → `ClaudeTitleOutro916`.
- No center-cropping. Media/*.mp4 in this `vertical/` folder are native
  1080×1920 renders (then compiled to 4K portrait 2160×3840).
- Adaptations for portrait:
  - `BrutalistHesitantWriter.tsx` local patch: swap the design-reference box
    to 1080×1920 when portrait so the shipped `Math.min(w/1920, h/1080)`
    scale does not collapse to 0.5625 (per known BLUF-coverage recipe).
  - `ClaudeCodeBeat.tsx` local patch: the adaptive fontSize now also
    considers the longest line's monospace width, not just line count. Fixes
    horizontal clipping of code cards in portrait.
  - B01 portrait fontSize 155, lineSpacing 7.0 — measured on the compiled
    master until GATE V's canvas-fill floor cleared (55% minimum).
  - B09 portrait composer text shortened to keep the ask + running indicator
    inside the safe area; narration is unchanged and matches the on-screen
    (HANDOFF LAW). Landscape B09 keeps the full 5-step outputs list.

## Automated gates run

| Gate | Command | Result |
|---|---|---|
| Kokoro synth | audio inherited from landscape sheet (identical narration) | 11 beats · durations preserved |
| Remotion beat render | `python3 runtime/scripts/remotion_scenes.py <reel>/vertical` | 11/11 native portrait beats rendered |
| compile.py | `python3 runtime/scripts/compile.py <reel>/vertical --height 3840 --out <reel>/exports/vertical` | wrote 238.7s master, atomic verify passed |
| GATE V (final_frame_check) | invoked by compile.py | 22 frames · BLOCKER 0 · MAJOR 0 · PASS |

## Visual QC (image inspection)

- Per-beat portrait frames at 15/50/85% in `vertical/_qc/per-beat/`, opened
  via image-capable Read.
- Contact sheet `_qc/contact-sheet-vertical.png` (SHA-256
  `34ee3a40ba117f43872b17937263e948b2cf7197b83f91b1304ce35bb4d3d58c`).
- Spot frames from the compiled 4K portrait master at multiple time offsets
  in `_qc/final-vertical/` — inspected for edge bleed, clipping and burn-in
  overlays. None present in the master (the `-slate` cut carries a review
  label; the `-master` cut does not).

Observations:
- B00 composer: portrait composer with topic band, greeting, ask, folder
  chip and three output lines — all inside SAFE916 (x 54–1026, y 96–1824
  → 108–2052, 192–3648 at 4K).
- B01 hesitant writer: two lines spread comfortably from mid-upper to
  mid-lower half of the frame; fill coverage cleared 55% floor.
- B02–B07 code cards: adaptive font holds every line inside the card
  without horizontal clipping in portrait.
- B08 verdict artifact: six numbered lines in the portrait card, no
  overflow.
- B09 Your Turn composer: shortened portrait prompt keeps composer +
  output inside the safe area; running indicator at bottom.
- B10 outro: dark ground title card, `@NikBearBrown` handle beneath — the
  slug-seeded mascot animation is preserved.

## Container / stream checks (portrait master)

```
$ ffprobe -v error -select_streams v:0 -show_entries stream=width,height,codec_name,duration,r_frame_rate \
    exports/vertical/claude-liam-brutalist-command-smoke-vertical.mp4
codec_name=h264
width=2160
height=3840
r_frame_rate=24/1
duration=238.666667

$ ffmpeg -i exports/vertical/…-vertical.mp4 -af volumedetect -f null - 2>&1 | grep mean_volume
mean_volume: -27.0 dB
max_volume: -3.1 dB
```

- Aspect: 2160×3840 (native 4K UHD portrait) ✓ — not an upscaled crop.
- Duration: 238.67s = same as landscape (audio unchanged) ✓
- Audio: stereo 48 kHz AAC, mean_volume -27.0 dB ✓

## Skin-lint warnings (expected, non-blocking)

`compile.py` emits SKIN LINT warnings for B00 and B10 in portrait: "palette=
claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants
ClaudeComposerAsk". This is the documented false-positive when the beat
legally uses portrait 916 variants for the vertical companion. The lint's
rule was written before native portrait bookends existed; the current
BUILD-PROMPT explicitly allows portrait variants of those beats.

## Conclusion

Portrait 2160×3840 master at
`exports/vertical/claude-liam-brutalist-command-smoke-vertical.mp4` passes
every runtime gate available for the portrait aspect. Human review pending;
no publication.
