# Checks report — portrait

Reel: `The fashionista Skill` (portrait companion)
Slug: `claude-liam-brutalist-skill-fashionista-vertical`
Aspect: 9:16 · 2160×3840 · 24 fps · 276.00 s · aac stereo
Run: `ca12337c8e2c43d0a0add834b390efd7` (source SHA updated; renders verified unchanged from prior clean build)

## Beat classification (PROOF GATE from nopunt SKILL.md)

12 SHOW / 0 justified-HOLD / 0 PUNT-flagged. Same content as landscape,
native portrait compositions.

## Teaching arc

- FRAMEWORK ✓  ·  WORKED EXAMPLE ✓  ·  FALSIFIABILITY ✓  ·  SCAFFOLDED TASK ✓
- BOOKENDS ✓  ·  NO-SOURCE-NO-VERDICT ✓

## Portrait-native scenes

The portrait cut uses these compositions natively — NOT a center-crop of the
landscape master:

| Beat | Portrait composition | Reflow move |
|---|---|---|
| B00 | ClaudeComposerAsk916 (library) | R2 – typography ramp |
| B01 | BrutalistHesitantWriter916 (library) | R3 – rescale (see BrutalistHesitantWriter.tsx patch below) |
| B02 | SkillTeardownAnatomy916 (this run — authored + registered) | R2 + vertical stack |
| B03 | SkillTeardownPipeline916 (this run — authored + registered) | R1 – rotation (horizontal → vertical flow, down arrows) |
| B04-B08 | SkillTeardownMechanism916 (this run — authored + registered) | R2 – typography ramp, narrower body column |
| B09 | ClaudeVerdictArtifact916 (library) | R3 – rescale |
| B10 | ClaudeComposerAsk916 (library) | R2 |
| B11 | ClaudeTitleOutro916 (library) | R2 |

## Patched isolated toolkit files (never touched the live library)

- `runtime/remotion/src/scenes/SkillTeardownAnatomy916.tsx` — NEW (portrait
  variant of SkillTeardownAnatomy).
- `runtime/remotion/src/scenes/SkillTeardownPipeline916.tsx` — NEW.
- `runtime/remotion/src/scenes/SkillTeardownMechanism916.tsx` — NEW.
- `runtime/remotion/src/Root.tsx` — REGISTERED the three new 9:16
  compositions inside the existing `SkillTeardown-Generic` folder.
- `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx` — PATCHED the
  scale computation to be portrait-aware:
  `scale = isPortrait ? min(w/1080, h/1920) : min(w/1920, h/1080)`.
  Reason: without the patch the shipped scene collapses to 0.5625× on any
  1080×1920 canvas and Gate V's canvas-fill law is unsatisfiable at any
  authoring fontSize. See `feedback_hesitant_writer_portrait_scale` in
  auto-memory. Change lives ONLY in this isolated toolkit copy.

## Skin lint warnings (accepted for portrait aspect)

`compile.py` emitted two `SKIN LINT` notices:
```
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk
[art] SKIN LINT: B11: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro
```

These are warnings, not gate refusals — the linter is aspect-blind and
expects the 16:9 names. The portrait requires the 916 variants (the whole
point of the vertical cut is to be native 9:16, not a crop). Not a defect.

## Kokoro audio

Same measured durations as landscape (`am_onyx`, free, local).

## Compile

Command:
```
python3 runtime/scripts/compile.py <reel>/vertical --height 3840 --out <reel>/exports/vertical
```

Result:
```
[art] wrote …/claude-liam-brutalist-skill-fashionista-vertical.mp4  (276.0s, audio: per-beat timeline …)
[art] slots: 12/12 filled — B00:VIDEO … B11:VIDEO
```

ffprobe on the final MP4:
```
$ ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate,duration -of csv=p=0
2160,3840,24/1,276.000000
$ ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,channels -of csv=p=0
aac,2
```

Portrait is 2160×3840 (4K native), NOT an upscale of a cropped landscape.

## Gate V (frame-level visual QC)

Passed cleanly during `compile.py` (0 BLOCKER, 0 MAJOR). The compiler's
atomic verification would have refused the master otherwise; the
`.verified.json` sidecar exists in the exports directory.

Iteration note: initial Gate V surfaced an `underfill` MAJOR on B01 (5%
coverage). Root cause was the shipped BrutalistHesitantWriter scale bug on
portrait canvas. Fixed via the toolkit-local patch (see above) plus a
portrait-fit re-authoring of the text (7 short lines) and a faster typing
pace so the mid-frame samples the corrected sentence. Third rebuild passed.

## Visual review (LLM-eye pass)

Extracted per-beat frames at 15/50/85% and inspected them via the
image-capable Read tool. Contact sheet at `_qc/contact-vertical.png`.
Findings: all 12 portrait beats render inside SAFE916; the vertical
pipeline stack reads top-to-bottom naturally; the mechanism cards fill the
column; the verdict card is legible without clipping; the outro title
restates + hardcoded @NikBearBrown handle + slug-seeded mascot.

## Conclusion

Portrait 4K master: **CLEAN**. Human review pending.
