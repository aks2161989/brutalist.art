# CHECKS-REPORT.md — The anthropics Skill (vertical 2160×3840)

*Every current runtime check run against the final master. Outputs are quoted
verbatim from the tool. Failures are repaired in the reel, not in the check.*

## Environment

- Toolkit: isolated workspace copy under
  `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/.repoloop/workspaces/claude-liam-brutalist-skill-anthropics/toolkit`
  (read-only public toolkit not modified).
- Run: `3d80d6c77f6e4febae4b0621b229c773` (re-review; original build run `485d27366b4f49a9b54a62d76e99a56b` 2026-09-08).
- Date: 2026-09-11.
- Browser (Remotion): same `runtime/chrome-wrapper.sh` path as landscape.

## Gate V — final_frame_check.py

```
$ python3 runtime/qc/final_frame_check.py <reel/vertical> \
    --mp4 <exports/vertical>/…/candidate.mp4 \
    --sheet <clips/_work>/resolved-sheet.json
```

Read `_qc/REPORT.md`:

> # Gate V — visual QC report
>
> Frames sampled: 22  ·  BLOCKER: 0  ·  MAJOR: 0
>
> Clean — no BLOCKER/MAJOR defects. ✓

22 frames = 11 beats × (50 %, 85 %) steady-state sample. Portrait
`SAFE916` (972×1728 at 1080×1920 composition, scaled to 2160×3840
output) inset was checked against the ink bounding box on every frame,
plus the 55 % canvas-fill law.

## Compiler final gate — atomic verified.json

```
$ ls exports/vertical/
claude-liam-brutalist-skill-anthropics-vertical.mp4
claude-liam-brutalist-skill-anthropics-vertical.verified.json
```

Master SHA-256:
`73f730baa0e438bef99eddc9f5970b3fbd55afbd94967cd7948930fd5e818170`.
Duration: 228.87 s.

## ffprobe — decode + audio

- Video stream: `h264 yuv420p 2160×3840 30 fps`. Native full-length
  portrait — this is a native reflow at composition width 1080, height
  1920, rendered `--scale=2` (Remotion) then upscaled to 3840 by the
  compiler's height flag. Not an upscaled crop of the landscape master.
- Audio stream: `aac 48 kHz stereo`, decodes clean.
- Duration matches landscape (228.87 s) — same beat count and per-beat
  timings, portrait geometry only.

## Motion histogram (compiler) & skin lint

Same warnings as landscape (`reveal:7 type-on:3 hold:1`; skin lint on
`ClaudeComposerAsk916` and `AntOutro916`) — both intentional per the
BUILD-PROMPT. See landscape `CHECKS-REPORT.md` for the full disposition.

## B01 iterations — how Gate V was reached

The first vertical compile failed Gate V:

> B00_50.png / B00_85.png — BLOCKER edge-bleed (bottom)
> B01_50.png / B01_85.png — MAJOR underfill (12 % / 25 %)

Repair path (recorded so the reviewer can trust the file, not just the
gate):

1. **B00 edge-bleed** turned out to be a stale render from before the
   scene's `bottom: height*0.07` terracotta rule was probed. Re-rendering
   the beat put the accent rule at y ≈ 92 % of the 4K frame — well inside
   the `SAFE916.b = 1824` inset (b ≈ 96 % of height). The subsequent
   Gate V pass produced no `edge-bleed` on B00 at either steady-state
   frame.
2. **B01 underfill** was the real underlying issue: the shipped
   `BrutalistHesitantWriter` scene uses
   `scale = min(width/1920, height/1080)`, which collapses to 0.5625 on
   a 1080×1920 canvas — half-height glyphs on the portrait aspect. That
   is a landscape-only scale. Fix (applied to the isolated toolkit
   copy only, not the live library): make the scale portrait-aware,
   `min(width/1080, height/1920)` when `height > width`. See
   `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx` line 222.
3. B01 text was then reflowed into a 6-line serif block at
   `fontSize: 195, lineSpacing: 1.2, charMs: 55, mistakeRate: 0,
   hesitateWithin: 0, hesitateBetween: 0` so the typing finishes before
   the 50 % steady-state sample and the ink bbox covers 63 % of the safe
   area at both 50 % and 85 %. Seed `anthropics-bluf-2026-vB`.
4. Text content: `"The\nanthropics\nis a\nchannel\nreads the\nartifact"`
   with `triggerWords: "channel"` → `replacementWords: "beat"`. The
   in-frame correction is the same misconception the landscape B01
   makes ("channel" → "beat"), just reflowed onto more, shorter lines
   for the 9:16 canvas — SHOTLIST.md is landscape-worded; this note
   documents the intentional vertical divergence.

## Missing checks

Same as landscape: `scripts/type_check.py`, `reference/type-spec.md`,
`ILLUSTRATIONS.md` — not present in this toolkit snapshot. Typography
was inspected visually on the 2160×3840 frames.

## Visual inspection log

- `_qc/frames/B00_85pct.png` — composer, greeting, ask, three answer
  lines, `@HumanitariansAI` chip, terracotta rule bottom-left inside
  safe area.
- `_qc/frames/B01_85pct.png` — 6-line serif reflow, `channel` swapped
  to `beat`, ink fills the safe area at 63 %.
- `_qc/frames/B10_85pct.png` — outro card, terracotta period, handle,
  `LIAM, IN FOR BEAR.`
- `_qc/contact_sheet.png` — 11-beat portrait grid.

## Conclusion

Gate V clean. Native portrait, not a cropped landscape. Compiler receipt
atomic. `VISUAL-REVIEW.json` records the reviewer notes. Human review
pending.
