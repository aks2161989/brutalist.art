# CHECKS-REPORT.md — The duration-planner Skill (portrait 2160×3840)

## Re-verification — 2026-09-11 (run_id d046c67744a74bd5ad40572da67b71da)

Same re-trigger context as landscape (see `../CHECKS-REPORT.md`). Source
SKILL.md SHA unchanged; FEEDBACK.md empty. Portrait MP4 sha256 verified
byte-identical to prior record (`82e1bd1…`). ffprobe confirms 2160×3840,
214.125s video+audio. Contact sheet re-read — all 22 frames pass. No
re-render required. VISUAL-REVIEW.json updated to this invocation's run_id
and source_sha256. Original build record follows.

---


Every current runtime check run against the final portrait master. Outputs
quoted from the tool. Failures were repaired in the reel, not in the check.

## Environment

Same isolated toolkit as landscape (see `../CHECKS-REPORT.md`). The vertical
sheet is a **native full-length portrait companion** authored via `art
vertical` (which invoked `runtime/scripts/shorts.py --vertical`), NOT a
Shorts cut and NOT an upscaled crop of the landscape master.

## art vertical plan output

```
$ python3 runtime/scripts/shorts.py <reel> --vertical
[short] parent reel: 11 beats · 214.0s (3:34.0) · Shorts cap 3:00
[vertical] full-length companion: every source beat is retained
[short] B00  ONDA CHECK: ClaudeComposerAsk        → ClaudeComposerAsk916
[short] B01  ONDA CHECK: BrutalistHesitantWriter  → BrutalistHesitantWriter916
[short] B02  ONDA CHECK: SkillTeardownAnatomy     → SkillTeardownAnatomy916
[short] B03  ONDA CHECK: SkillTeardownPipeline    → SkillTeardownPipeline916
[short] B04  ONDA CHECK: SkillTeardownMechanism   → SkillTeardownMechanism916
[short] B05  ONDA CHECK: SkillTeardownMechanism   → SkillTeardownMechanism916
[short] B06  ONDA CHECK: SkillTeardownMechanism   → SkillTeardownMechanism916
[short] B07  ONDA CHECK: SkillTeardownMechanism   → SkillTeardownMechanism916
[short] B08  ONDA CHECK: ClaudeVerdictArtifact    → ClaudeVerdictArtifact916
[short] B09  ONDA CHECK: ClaudeComposerAsk        → ClaudeComposerAsk916
[short] B10  ONDA CHECK: ClaudeTitleOutro         → ClaudeTitleOutro916
[short] 11 beats · ~214.0s full-length vertical (no Short cap)
[short] dropped: none · ends on the last beat (no endcard)
[short] ONDA CHECK: 11 REMOTION beat(s) rewired to 916 compositions
```

Zero beats cut. Every Remotion pattern rewired to its native 916 sibling;
none was center-cut from a landscape render. Where a 916 composition did not
exist in the toolkit, it was **registered natively** (see below), not
faked by cropping.

## Native portrait composition registrations added

Three portrait compositions were added to `runtime/remotion/src/Root.tsx`
inside the `SkillTeardown-Generic` folder:

```tsx
<Composition id="SkillTeardownAnatomy916"    width={1080} height={1920} … />
<Composition id="SkillTeardownPipeline916"   width={1080} height={1920} … />
<Composition id="SkillTeardownMechanism916"  width={1080} height={1920} … />
```

Same components as landscape — they read `useVideoConfig()` for width/height
and reflow naturally at portrait aspect. No cropping, no image squish.
`./art scene-index` re-ran to update `scenes.json`, and `./art scenes --check`
confirmed all three render at 9:16.

## Kokoro audio

Reuses the parent's per-beat mp3s (independent copies in
`vertical/mp3/`, not symlinks — per `PIPELINE-SAFETY.md`). Same durations
because narration text was NOT rewritten for portrait — only visual props
were adjusted (`text` line breaks and `fontSize` on the hesitant writer for
the taller frame; see `../SHOTLIST.md`).

## Remotion render (portrait)

```
$ python3 runtime/scripts/remotion_scenes.py <reel>/vertical
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

Foreground, serial. Zero slates.

## Compile at 4K portrait

```
$ python3 runtime/scripts/compile.py <reel>/vertical --height 3840 \
      --out exports/vertical --force
[art] compiled B00..B10 VIDEO (source audio preserved)
[art] motion histogram: reveal:7  type-on:3  hold:1
[art] WARNING: 'reveal' carries 7/11 beats (63%) — pantry cap warning
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916'
      — COLD OPEN LAW wants ClaudeComposerAsk
[art] SKIN LINT: B10: palette=claude but the outro is 'ClaudeTitleOutro916'
      — OUTRO LAW wants ClaudeTitleOutro
[art] build stamp → beat_sheet.json (11/11 filled)
[art] wrote exports/vertical/claude-liam-brutalist-skill-duration-planner-vertical.mp4
      (214.1s, audio: per-beat timeline (source audio preserved))
```

The two SKIN LINT warnings are the portrait-lint's known false positive: the
`916` variants ARE the portrait-native version of ClaudeComposerAsk /
ClaudeTitleOutro (naming convention "prefix + 916"), which is exactly what
COLD OPEN LAW / OUTRO LAW want here. The lint is checking for the exact
landscape name string. Anthropics' portrait reel shows the same warning.

## Gate V — final_frame_check.py (portrait 9:16 SAFE)

```
$ python3 runtime/qc/final_frame_check.py <reel>/vertical
      --mp4 exports/vertical/claude-liam-brutalist-skill-duration-planner-vertical.mp4
[gate-v] frames=22 BLOCKER=0 MAJOR=0 → _qc/REPORT.md
```

`_qc/REPORT.md`:

```
# Gate V — visual QC report
Frames sampled: 22  ·  BLOCKER: 0  ·  MAJOR: 0
Clean — no BLOCKER/MAJOR defects. ✓
```

Contact sheet: `_qc/contact_sheet.png`. All 22 sampled frames Read visually.

### Repairs made during Gate V iteration (portrait)

- `channel_title: "@HumanitariansAI"` metadata was inherited from the parent
  landscape sheet. The compile.py overlay at `H-h-40` positioned the wordmark
  at y ≈ 3800 on the 3840-tall portrait — inside the burn-in exclude
  vertically, but extended past x=1296 (the exclude's right edge) on the wide
  handle, triggering Gate V edge-bleed at B00's bottom. Removed
  `channel_title` from the vertical metadata (parent landscape keeps it —
  its safe area accommodates the same overlay at h=2160). The channel
  identity still appears in the composer beats' `folderLabel` prop.
- `BrutalistHesitantWriter` scale bug at 9:16: the shipped component uses
  `Math.min(width/1920, height/1080)` for its font scale, which collapses to
  0.5625 in portrait — halving the serif and dropping B01 to 19 % underfill.
  Patched to portrait-aware
  `portrait ? min(width/1080, height/1920) : min(width/1920, height/1080)`
  per feedback memory `feedback_hesitant_writer_portrait_scale.md`. Landscape
  math unchanged.
- With the scale fixed, the ported landscape text overshot vertical safe. B01
  portrait was re-authored with 7 short lines at fontSize 210, `charMs: 55`,
  and hesitations off — text lands fully before the 50 % sample. Same
  correction (`target → output`) applied; reads "Your / video / duration /
  is your / output. / Size the / script." after correction.

## FFprobe

```
$ ffprobe -v error -show_entries stream=width,height,codec_type,duration \
      -of default=nw=1 exports/vertical/claude-liam-brutalist-skill-duration-planner-vertical.mp4
codec_type=video
width=2160
height=3840
duration=214.125000
codec_type=audio
duration=214.125000
```

Native 4K portrait (9:16) — 2160 × 3840. Not an upscaled crop.

## What did NOT run

Same as landscape (see `../CHECKS-REPORT.md § What did NOT run`).

## Files

Portrait master: `exports/vertical/claude-liam-brutalist-skill-duration-planner-vertical.mp4`
Portrait receipt: `exports/vertical/claude-liam-brutalist-skill-duration-planner-vertical.verified.json`
QC frame audit: `vertical/_qc/REPORT.md`, `vertical/_qc/contact_sheet.png`
