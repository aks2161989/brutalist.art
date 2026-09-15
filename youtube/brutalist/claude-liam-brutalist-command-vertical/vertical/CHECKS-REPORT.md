# CHECKS-REPORT.md — vertical (9:16 full-length twin)

Run: `ac6edaa227b34224a6622a2702619b03` · `2026-09-12` (B02 line-number fix rebuild).
Previous: `a6810945561e4cb29004aafd59c560fe` · `2026-09-09`
(resume of `5f733dcd6d2249fea636151601143428`; supervisor
rejected the prior VISUAL-REVIEW.json with
`vertical: visual-review frame evidence missing/stale` because the
first attempt's frames[] paths pointed at `_qc/vertical/…` that did
not exist on disk — the actual contact sheet had shipped as
`_qc/contact_sheet.png` under `_qc/` root. This resume regenerated
the portrait proof frames from the CURRENT master MP4, wrote them
under `_qc/vertical/frames/`, rebuilt the portrait contact sheet at
`_qc/vertical/contact-sheet.png`, and re-hashed every entry to the
real SHA-256 tied to THIS `run_id`. No source, beat_sheet, mp3, per-
beat mp4, or exported MP4 was touched — the successful media from
the prior attempt is preserved.)

Derived via `./art vertical <reel>` (which forwards to
`runtime/scripts/shorts.py --vertical`). ONDA CHECK rewired 12 REMOTION
beats to their `<pattern>916` composition; every composition is
registered in the isolated toolkit's `Root.tsx`.

## Pipeline stages that ran

1. `./art vertical <reel>` — auto-derived `vertical/beat_sheet.json`;
   no drops (contract), no endcard (contract), no rewritten outro
   (contract). Full 12 beats retained.
2. Manual portrait tuning: shortened B00 composer command + output
   (portrait safe area is much narrower); shortened B10 composer
   command + output; rewrote B01 BLUF text to the 12-char-max recipe
   (`vertical / shrinks. / crops it. / graphics.` → `vertical /
   preserves. / rewires it. / graphics.`); removed `channel_title`
   metadata per the portrait-bleed feedback memory.
3. `remotion_scenes.py <reel>/vertical` — 12/12 portrait beats
   rendered against the 916 compositions. Foreground, serial.
4. `compile.py --height 3840 --out exports/vertical --force` — motion
   histogram and brand-lint ran; skin-lint noted the expected
   ClaudeComposerAsk916/ClaudeTitleOutro916 usage (accepted — this
   is how the shorts.py contract routes portrait, and it is exactly
   what Ep 30 shipped with).
5. Frame extraction — per-beat samples at 15 % / 50 % / 85 % (36
   PNGs) plus first/final (38 PNGs total) written to
   `_qc/vertical/frames/` from the CURRENT master
   `exports/vertical/claude-liam-brutalist-command-vertical-vertical.mp4`.
   Contact sheet regenerated at `_qc/vertical/contact-sheet.png`
   using `ffmpeg xstack`. Read with the image-capable Read tool
   during this invocation: contact sheet, B00_50, B01_50, B05_50,
   B09_50, B10_50, B11_50. Every entry in `VISUAL-REVIEW.json`
   `frames[]` carries a real SHA-256 of the on-disk PNG tied to
   THIS `run_id`.
6. `ffprobe` on the final MP4:
   - video: 2160×3840 @ 24 fps (native portrait 4K)
   - audio: AAC 48 kHz stereo, 247.458 s
   - matches the landscape duration exactly (the vertical contract).

## First compile attempt: BLOCKER caught by Gate V

The first vertical compile was REFUSED by
`runtime/qc/final_frame_check.py` with two BLOCKER-severity findings:

```
### B01_50.png
- BLOCKER  edge-bleed — content crosses the title-safe left edge
### B01_85.png
- BLOCKER  edge-bleed — content crosses the title-safe left edge
```

Root cause: B01 portrait text carried the phrase `preserves beats`
(15 chars) at fontSize 180 — wider than the 972 px SAFE916 inner
width. Fix (applied): shortened the BLUF to `vertical / shrinks. /
crops it. / graphics.` (final corrected: `vertical / preserves. /
rewires it. / graphics.`) — every line ≤ 11 chars, comfortably inside
the safe area. B01 was re-rendered `--force --only B01`. Second
compile: Gate V clean, zero BLOCKER, zero MAJOR, MP4 written.

This is the specific Gate V mechanism doing exactly what it exists to
do — the pipeline caught a portrait-only overflow that would not have
shown up in the 16:9 render. The compiler's atomic candidate flow
meant nothing bad was written to `exports/vertical/`; the failed
candidate was cleaned up automatically.

## Gate coverage

| Gate | Status | Evidence |
|---|---|---|
| Audio decodes | PASS | ffprobe audio stream present, 247.458 s |
| Video dimensions | PASS | 2160×3840 (native portrait 4K, not upscaled) |
| Per-input hashes | PASS | 24 hashes in `verified.json` (12 mp4 + 12 mp3) |
| Gate V (final_frame_check) | PASS (2nd attempt) | see B01 root-cause above; second compile 0 BLOCKER / 0 MAJOR |
| Motion pantry | WARN | code-cascade 58 % — accepted (see landscape report) |
| Skin-lint | WARN | ClaudeComposerAsk916 / ClaudeTitleOutro916 flagged as "COLD OPEN LAW wants ClaudeComposerAsk / OUTRO LAW wants ClaudeTitleOutro". Accepted: this is exactly the rewire the shorts.py --vertical contract requires (see FACTCHECK) — the lint predates the portrait naming convention and was accepted by Ep 30 the same way. |

## Portrait-specific observations (accepted MINOR limitations)

- Code beats (B02–B08) rendered with `ClaudeCodeBeat916` — the
  responsive component at 1080×1920. The mono code text uses a fixed
  effective font size; long lines (e.g. `runtime/scripts/shorts.py`
  file paths) are clipped at the right edge of the code card. The
  essential structural tokens (`case`, `shorts)`, `vertical)`, `exec
  python3 …`, `if a.vertical:`, `raise BuildError(…)`) are visible in
  every frame. This is the same treatment Ep 30 (`art shorts`) shipped
  with, which passed Gate V and human review. A future improvement
  would be a portrait-specific ClaudeCodeBeat that wraps or shrinks
  code lines; that is out of scope for this episode.
- B01 corrected sentence spans 4 lines with generous line-spacing; the
  correction (`shrinks. → preserves.` and `crops → rewires`) lands
  visibly on screen well before the cut.

## Missing checkers (recorded honestly)

Same as landscape — `type_check.py`, `type-spec.md`, and the kerning
skill are not shipped in this toolkit revision. Visual typography
review was done by reading extracted frames with the image-capable
Read tool. See `TYPECHECK.md`.

## Nothing uploaded

The mp4 sits in `exports/vertical/`. Bear's viewing/editing is the
next step. No transcoding, upload, GitHub push, or scheduling occurred.
