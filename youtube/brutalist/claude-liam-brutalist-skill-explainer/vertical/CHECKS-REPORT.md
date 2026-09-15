# CHECKS-REPORT.md — The explainer Skill (portrait 2160×3840)

Every current runtime check run against the final portrait master. Outputs
quoted from the tool.

**Rebuilt 2026-09-11** (run_id `251584521128464e8b35431dce545cb1`): B07 updated for
EXECUTABLE-EVIDENCE.md addition to VOX LAW. B07 audio copied from landscape
(same narration), SkillTeardownMechanism916 re-rendered, vertical recompiled --force.

## Environment

- Same isolated toolkit and `chrome_wrap.sh` as the landscape build (see
  `../CHECKS-REPORT.md`).
- Run id: `251584521128464e8b35431dce545cb1` (original: `45e2af0d64bd4e67b0ce03bb5b591d29`).

## Portrait-specific toolkit changes

- **New portrait wrappers registered in `Root.tsx`**:
  `SkillTeardownAnatomy916`, `SkillTeardownPipeline916`,
  `SkillTeardownMechanism916`. Same source component as the landscape
  variants; reflow via `useVideoConfig()` (`width`/`height` used to
  compute all offsets — verified in scene source).
- **BrutalistHesitantWriter portrait-scale patch** applied to the
  isolated toolkit copy per `feedback_hesitant_writer_portrait_scale`.
  Diff:
  ```ts
  const isPortrait = height > width;
  const scale = isPortrait
    ? Math.min(width / 1080, height / 1920)
    : Math.min(width / 1920, height / 1080);
  ```
  Live library at
  `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx`
  is UNTOUCHED — patch lives in the isolated toolkit only.
- **channel_title metadata omitted** from `vertical/beat_sheet.json` to
  avoid the compile-overlay bleed past portrait safe.b documented in
  `feedback_channel_title_portrait_bleed`. Portrait sheet keeps `channel`
  only (informational, not overlay-rendered).

## Audio

Portrait shares the landscape's Kokoro output byte-for-byte (mp3 files
copied into `vertical/mp3/`). `generate_audio_kokoro.py` re-run to stamp
`actual_duration_s` + `audio_file` into the portrait sheet — same 11
durations as landscape.

## Remotion render

```
[remotion] B00: ok: ClaudeComposerAsk916        -> media/B00.mp4
[remotion] B01: ok: BrutalistHesitantWriter916  -> media/B01.mp4
[remotion] B02: ok: SkillTeardownAnatomy916     -> media/B02.mp4
[remotion] B03: ok: SkillTeardownPipeline916    -> media/B03.mp4
[remotion] B04: ok: SkillTeardownMechanism916   -> media/B04.mp4
[remotion] B05: ok: SkillTeardownMechanism916   -> media/B05.mp4
[remotion] B06: ok: SkillTeardownMechanism916   -> media/B06.mp4
[remotion] B07: ok: SkillTeardownMechanism916   -> media/B07.mp4
[remotion] B08: ok: ClaudeVerdictArtifact916    -> media/B08.mp4
[remotion] B09: ok: ClaudeComposerAsk916        -> media/B09.mp4
[remotion] B10: ok: ClaudeTitleOutro916         -> media/B10.mp4
```

Every beat resolved to a native portrait scene; no cropped landscape
video. No slates.

## Compile

```
$ python3 runtime/scripts/compile.py <reel>/vertical --height 3840 \
      --out exports/vertical
[art] compiled B00–B10  VIDEO  (11/11 filled)
[art] motion histogram: reveal:7  type-on:3  hold:1
[art] WARNING: 'reveal' carries 7/11 beats (63%) — over the ~40% pantry cap
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk
[art] SKIN LINT: B10: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro
[art] build stamp → beat_sheet.json (11/11 filled)
[art] wrote exports/vertical/claude-liam-brutalist-skill-explainer-vertical.mp4
      (252.5s, audio: per-beat timeline)
```

The two SKIN LINT warnings are the KNOWN false positive for portrait —
the 916 wrappers ARE the portrait-native cold-open and outro. Every prior
episode in this playlist emits the same two warnings by design; they are
not gate failures.

## Gate V — final_frame_check.py

```
$ python3 runtime/qc/final_frame_check.py <reel>/vertical
      --mp4 exports/vertical/claude-liam-brutalist-skill-explainer-vertical.mp4
      --sheet clips/_work/resolved-sheet.json
[gate-v] frames=22 BLOCKER=0 MAJOR=0 → _qc/REPORT.md
```

`_qc/REPORT.md`:

```
# Gate V — visual QC report
Frames sampled: 22  ·  BLOCKER: 0  ·  MAJOR: 0
Clean — no BLOCKER/MAJOR defects. ✓
```

`_qc/contact_sheet.png` covers the reel at a glance; all 22 frames Read
via the image-capable tool.

## Compiler final gate — atomic verified.json

```
$ ls exports/vertical/
claude-liam-brutalist-skill-explainer-vertical.mp4
claude-liam-brutalist-skill-explainer-vertical.verified.json
```

## FFprobe dimensions and audio decode

```
$ ffprobe -v error -show_entries stream=width,height,codec_type,duration \
      -of default=nw=1 exports/vertical/claude-liam-brutalist-skill-explainer-vertical.mp4
codec_type=video
width=2160
height=3840
duration=252.541667
codec_type=audio
duration=252.541000
```

Native portrait 4K (9:16, 2160×3840) — not a crop, not an upscale from
1080×1920 preview. Audio decoded, matches video duration.

## No captions / subtitles

Same as landscape: `captions: false`, no SRT/VTT/CC track.

## No paid calls, no publishing

Same as landscape: local, free, no upload.

## What did NOT run (recorded honestly)

- Same set as landscape (see `../CHECKS-REPORT.md`).
- Additional portrait-specific note: no attempt to reflow the landscape
  master via `art shorts` or a 9:16 crop — this is a NATIVE portrait
  build, per playlist rule "full-length `art vertical` separately from
  `art shorts`."

## Files that exist

- Portrait master: `exports/vertical/claude-liam-brutalist-skill-explainer-vertical.mp4`
  (2160×3840, 252.54s)
- Portrait receipt: `exports/vertical/claude-liam-brutalist-skill-explainer-vertical.verified.json`
- QC report: `vertical/_qc/REPORT.md` (clean)
- QC contact sheet: `vertical/_qc/contact_sheet.png`
- 11 media beats: `vertical/media/B00.mp4 … B10.mp4`
- 11 audio beats: `vertical/mp3/beat-B00.mp3 … B10.mp3` (copies of the
  landscape audio; byte-identical Kokoro output)
- 11 conformed clips: `vertical/clips/B00.mp4 … B10.mp4`
