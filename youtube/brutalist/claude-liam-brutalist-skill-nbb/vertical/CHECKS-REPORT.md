# CHECKS-REPORT — The nbb Skill (portrait 2160×3840)

Run ID: `176246a8e8ea447f812f68cd066bcb46`
(Original build run_id: `fdf9abc5ba3f40eba314b9262f54a0bc` — exports unchanged)
Toolkit commit: `ba2d0e0f043f5b3b35a50d336e0fc66fbfecfc0c` + local overrides
Source SHA-256 (SOURCE-SNAPSHOT capture, 2026-09-12T06:05:52): `395389a3f3f1b249fda8ab67de2d0668210b50174270d531242b3c737f4626e4`

## Compile — `runtime/scripts/compile.py`

```
python3 runtime/scripts/compile.py \
  youtube/brutalist/claude-liam-brutalist-skill-nbb/vertical \
  --height 3840 \
  --out youtube/brutalist/claude-liam-brutalist-skill-nbb/exports/vertical
```

- 12/12 beats compiled with per-beat VIDEO source
- Total duration matches landscape (audio timeline shared)
- Master output: `exports/vertical/claude-liam-brutalist-skill-nbb-vertical.mp4`
- ffprobe should report width=2160 height=3840 (native 4K portrait)

## Scene renderer — vertical patterns

All 12 patterns rendered at native 9:16 supersampled 2× (2160×3840):

- B00 → ClaudeComposerAsk916
- B01 → BrutalistHesitantWriter916 (portrait-scale patched)
- B02 → SkillTeardownAnatomy916
- B03 → SkillTeardownPipeline916
- B04–B08 → SkillTeardownMechanism916
- B09 → ClaudeVerdictArtifact916
- B10 → ClaudeComposerAsk916
- B11 → ClaudeTitleOutro916

New (this isolated toolkit only) portrait natives:
`SkillTeardownAnatomy916.tsx`, `SkillTeardownPipeline916.tsx`,
`SkillTeardownMechanism916.tsx` — brought in from the ep-15 (logo)
scene-source snapshot; same schemas, portrait reflow.

`BrutalistHesitantWriter.tsx` carries the portrait-scale patch per
`feedback_hesitant_writer_portrait_scale` — `Math.min(width/1080, height/1920)`
when `height > width`.

## Audio — `runtime/scripts/generate_audio_kokoro.py`

- 12/12 beats generated with voice `am_onyx`
- Same durations as landscape (shared narration text; only B01 differs
  slightly in on-screen `text` prop shape, narration is unchanged)
- Cost: **$0.00**

## Gate V — `runtime/qc/final_frame_check.py`

Run automatically inside `compile.py`. See `_qc/REPORT.md`.

## Notes vs landscape

- `metadata.channel_title` deliberately OMITTED for portrait per
  `feedback_channel_title_portrait_bleed`.
- Outro handle is `@NikBearBrown` (ClaudeTitleOutro916 hardcode per OUTRO-LOCK).
- Inner composer beats still carry `folderLabel: "@HumanitariansAI"`.

## Gaps

Same as landscape (`scripts/type_check.py`, `reference/type-spec.md`,
`ILLUSTRATIONS.md` — NOT present in this isolated toolkit revision).
