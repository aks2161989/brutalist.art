# CHECKS-REPORT — vertical (2160×3840)

## Re-build summary (run_id c4164e0244ae43b184b1671e8a80a477)

Source change: `fill_slates.py` sha256 `de9efcbdc…`. Vertical beats B04, B05, B06 re-rendered with ClaudeCodeBeat916 carrying updated code props (type annotations, `_topic()` helper defined-but-unused label, corrected line numbers: :51-74, :34-106, :109-130). B02 `cite` field updated to match. B00-B03, B07-B11 unchanged from prior build.

## Video probe

```
ffprobe -select_streams v -show_entries stream=width,height,duration,codec_name,r_frame_rate
  → codec=h264  width=2160  height=3840  r_frame_rate=24/1  duration=237.0s
ffprobe -select_streams a -show_entries stream=codec_name,duration
  → codec=aac  duration=237.0s
```

Native portrait — this is NOT a cropped landscape master; every beat was rendered at 1080×1920 composition size against the same portrait-native pattern registrations (ClaudeComposerAsk916, BrutalistHesitantWriter916, SkillTeardownMechanism916, ClaudeCodeBeat916, ClaudeVerdictArtifact916, ClaudeTitleOutro916). The compile then scaled to 2160×3840 for the deliverable.

## Isolated-toolkit patches required for portrait Gate V

Three edits were made to the ISOLATED toolkit copy (never the read-only public library) so the portrait cards clear Gate V's FILL_MIN=0.55 floor without edge-bleed:

1. `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx` — the shipped `Math.min(width/1920, height/1080)` collapses to 0.5625 on portrait; replaced with a portrait-aware ternary `height > width ? Math.min(width/1080, height/1920) : Math.min(width/1920, height/1080)` (memory: feedback_brutalist_hesitant_writer_portrait_scale_patch). Landscape behavior is unchanged.
2. `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx` — trigger-word hesitation pause shortened from 1000–1500 ms to 350–550 ms and the post-correction pause from 300 ms to 150 ms, so the four-line correction completes before the 50% sample time on a 10.4-second B01 clip.
3. `runtime/remotion/src/scenes/ClaudeVerdictArtifact916.tsx` — FONT_TITLE, FONT_HEADING, FONT_LINE, PAD_V and per-line marginBottom bumped up so the six-line verdict card clears 55% coverage in the portrait safe area without bottom bleed.

Beat-sheet knobs adjusted alongside the scene patch:

- B01 `fontSize: 150 → 175`, `lineSpacing: 2.5 → 2.2` — clears 55% with four full lines rendered.
- B10 `segment` shortened from `Dry-run fill_slates, then upgrade one card` to `Dry-run + upgrade a card`, and `command` trimmed to ≈300 chars, so the composer fits without right/bottom edge-bleed.

## Gate V final frame check

`runtime/qc/final_frame_check.py` sampled 24 frames from the finished 4K portrait master.

```
Frames sampled: 24  ·  BLOCKER: 0  ·  MAJOR: 0
Clean — no BLOCKER/MAJOR defects. ✓
```

Contact sheet `_qc/contact_sheet.png` (SHA-256 `8bc396662dd5c24062ed3f0e4109f01a20a0f4da82ef403e146108682ef90473`) and individual frames at B04/B05/B06 50% marks read visually — all legible within SAFE916. Portrait adaptive font clamping in ClaudeCodeBeat916 handles the updated (longer) code snippets correctly.

## Compile receipt

`build-state.json` (`vertical/`) records `status=ready`, output path, hash of the final MP4 (`5f75111fcda2b52b0af8c1f5c49963d0fc45e81e3fe5f811ab4d135b3ee9d159`), and every per-beat input hash. `exports/vertical/claude-liam-brutalist-runtime-fill-slates-vertical.verified.json` mirrors the atomic-verification record.

## Beat-sheet integrity

- Slug: `claude-liam-brutalist-runtime-fill-slates-vertical`
- Aspect: 9:16
- Beats: 12/12 filled (no unresolved slates)
- Total duration (audio-derived): 237.0s (matches landscape narration timeline)
- Beat sheet SHA-256: `c07815a8fb70ec313677bb826457ad3501cf410b878a86da7fa6451cb5210202`.

## Gate V history

Two prior compile attempts recorded these Gate V defects; the third pass (this record) is clean:

1. Initial pass — `B01 underfill 9%/16%`, `B09 underfill 49%/48%`, `B10 edge-bleed right/bottom`.
2. After scale patch + first font bump — `B01 underfill 39% at 50%` (typing not yet done at 50% sample time), `B09 pass`, `B10 pass`.
3. After scene-code trigger-pause trim + beat-sheet retune — `all 24 frames clean, 0 blockers, 0 majors`.

## Deliberately un-run demonstrations

Same as landscape — no `--apply` invocation, no publishing, no paid API. Local disposable-fixture description in B07 only.

## Known limitations

Same as landscape; see landscape CHECKS-REPORT.md.
