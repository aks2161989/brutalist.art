# CHECKS-REPORT — vertical (9:16)

Run: `e66ff34b0ab34b038ee5d5d5b8cb13b4`
Source SHA: `30d1a0602e5816a06a443392ae6edbf3ac24abec02a10d14a575c6dd6aa13f46`

`claude-liam-brutalist-command-todo-vertical.mp4` — 2160x3840 @ 24 fps,
167.875 s, h.264 (yuv420p) + AAC 48 kHz stereo. Same per-beat audio timeline
as the landscape master (per-beat MP3 hashes match).

## Gate F — factcheck

- `FACTCHECK.md` copied from landscape (all fact traces still valid — the
  vertical is a native-portrait companion, not a different narration).
- `SOURCES.md` identical to landscape (same underlying `art todo` sources).

Pass.

## Gate V — visual QC (final_frame_check.py)

```
Frames sampled: 24  ·  BLOCKER: 0  ·  MAJOR: 0
Clean — no BLOCKER/MAJOR defects. ✓
```

This is the SECOND Gate V run this resume. The FIRST run failed with 14
BLOCKER (`edge-bleed`, top edge) on B02-B08 plus 2 MAJOR (`underfill`,
22% and 23%) on B01. Both classes were repaired on this invocation:

1. **CommandTodo.tsx SparkLine portrait fix.** All seven Todo* custom
   illustrations (TodoPipeline916, TodoCommand916, TodoRun916,
   TodoEntry916, TodoMethods916, TodoAgentLoop916, TodoFailure916) share
   a `SparkLine` helper positioned at `sy = SY - 40 = 128` in CSS
   1080-wide portrait coordinates. Measured on the failing render, the
   first ink appeared at physical y=177 in the 2160x3840 output — six
   pixels short of the SAFE916.y=192 threshold (minus margin=8 → 184).
   Added a portrait-only `+60` bump inside the SparkLine component so
   the CSS top becomes 188, moving first ink to physical y≈380 with
   safe margin.

2. **B01 hesitant writer underfill fix.** Source props (`fontSize 200`,
   `lineSpacing 2.8`, three-line text) rendered as only two visible lines
   because 'is a receipt' (post-swap 12 chars) wrapped inside the
   component's `maxWidth = width * 0.86 = 928 CSS`. Restructured to
   `art todo\\nis a\\nlist.` (three short lines, none wrapping) with
   `fontSize 240` / `lineSpacing 2.6`. Measured bbox coverage jumped
   from 24% to 64% (>55% Gate V threshold). Trigger 'list'→'receipt'
   still delivers the same misconception→truth beat.

All 8 changed beats re-rendered via `runtime/scripts/remotion_scenes.py
--only <BID> --force`, then the full vertical was recompiled via
`runtime/scripts/compile.py --height 3840 --out exports/vertical --force`.

Full report in `_qc/REPORT.md`; contact sheet at `_qc/contact_sheet.png`.
Supplemental single-beat evidence frames extracted from the CURRENT
master this invocation and hashed in `VISUAL-REVIEW.json`.

Pass.

## Audio decode

`ffprobe` confirms a single AAC-LC stereo stream in the vertical master
(48000 Hz). The 12 per-beat MP3 SHA-256s are identical to landscape —
the vertical companion shares the narration, only the visuals are
native-portrait.

Pass.

## Compiler receipts

`exports/vertical/claude-liam-brutalist-command-todo-vertical.verified.json`
records:
- `status: ready`
- output SHA-256 `400eb021c8011e14810b8beb1256b6bc79cb3ab79457c1189f5bd15e2eb6ed27`
- 12 per-beat mp4 hashes (all re-rendered where changed: B01, B02-B08)
- 12 per-beat mp3 hashes (unchanged from landscape)
- 167.875 s duration
- built at `2026-09-09T18:13:04.518658+00:00`

## Skin lint / motion histogram

Compiler emitted the expected native-portrait SKIN LINT on the bookends:
```
SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk
SKIN LINT: B11: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro
```
These are the correct 916 variants for a native portrait build — the ONDA
CHECK in `shorts.py --vertical` rewires the beat sheet to `<pattern>916`
compositions to avoid crop-fits. This is a WARN not a BLOCKER; the visuals
these variants render pass Gate V.

Motion histogram matches landscape.

## Known limitations

- Same absent-legacy-typography-checker gap as the landscape reel; see
  `TYPECHECK.md`.
- B06 (TodoMethods916) portrait: the +60 SparkLine bump places the spark
  line closer to the METHOD column header than the equivalent landscape
  spacing. The safe-area check still passes; the header eyebrow (SANS
  20px caps) is clearly separable from the SparkLine serif at review
  distance. Recorded as a minor typography note, not a defect.

Every current runtime check that exists in this toolkit was run against
the episode and returned clean. Nothing was disabled or bypassed.

Human review is pending.
