# CHECKS-REPORT — The godot-gdd Skill — Short
# run_id: 2d281e32b355480b8350968778f9d049
# Re-verified: trigger was build script updates (compile.py/shorts.py/build_safety.py),
# not a content change. Parent beat_sheet and FEEDBACK.md unchanged. Render preserved.

## 1. Duration gate

```
ffprobe -v quiet -show_format -of json exports/short/claude-liam-brutalist-skill-godot-gdd-short.mp4
```

Result:
- Container duration: 139.291667s
- Video stream (h264 2160×3840 24fps): 139.291667s
- Audio stream (aac): 139.291000s
- **All three durations strictly < 180.0s — PASS**

## 2. Dimension check

```
ffprobe → [video] h264 2160x3840
```

- Matches required 2160×3840 (9:16) — PASS
- Source clips copied from parent vertical unchanged; no center-cut of landscape footage

## 3. Shorts.py cut validation

```
python3 runtime/scripts/shorts.py \
  .../claude-liam-brutalist-skill-godot-gdd/vertical \
  --output-dir .../claude-liam-brutalist-skill-godot-gdd-short \
  --slug claude-liam-brutalist-skill-godot-gdd-short \
  --drop B02 B03 B05 B07 \
  --no-endcard --no-outro-rewrite
```

Output: `8 beats · ~139.3s (2:19.3) OK · dropped: B02, B03, B05, B07`
- short_validation.status: "ready", errors: [] in beat_sheet.json
- All 8 kept beats confirmed as native portrait reused unchanged

## 4. Compile check

```
python3 runtime/scripts/compile.py \
  .../claude-liam-brutalist-skill-godot-gdd-short \
  --height 3840 \
  --out .../exports/short
```

Output: All 8 beats compiled, no errors. Skin lint warnings (B00 ClaudeComposerAsk916, B11 ClaudeTitleOutro916) are expected — these are registered 916 variants, not missing components.
- 8/8 filled: B00:VIDEO B01:VIDEO B04:VIDEO B06:VIDEO B08:VIDEO B09:VIDEO B10:VIDEO B11:VIDEO
- Output: exports/short/claude-liam-brutalist-skill-godot-gdd-short.mp4 — 139.3s

## 5. Beat sheet metadata validation

- kind: "short" ✓
- aspect_ratio: "9:16" ✓
- playlist: "Brutalist" ✓
- voice: "am_onyx" ✓
- voice_kokoro: "am_onyx" ✓
- captions: false ✓
- in_for_bear: true ✓
- channel: "@HumanitariansAI" ✓
- dropped_beats: ["B02","B03","B05","B07"] ✓
- total_estimated_duration_seconds: 139.29 ✓

## 6. Frame inspection (visual QC)

24 frames extracted (beat-relative 15%/50%/85% for each of 8 kept beats) using ffmpeg.
See VISUAL-REVIEW.json for hashes and notes. No blockers or majors found.

Key findings:
- All frames show proper 9:16 portrait framing (no landscape content)
- No burned-in captions or subtitle tracks
- No text clipped at left/right edges
- @HumanitariansAI present on ClaudeComposerAsk/Verdict/CodeBeat scenes
- @NikBearBrown on WalkerGodotSetup/GodotDesignBoard/ClaudeTitleOutro scenes — inherited from 916 component defaults, consistent with parent film's Gate-V pass
- B11 outro: "The godot-gdd Skill." title, locked per OUTRO-LOCK.md
- Liam sign-off confirmed (B11 narration_text: "Liam, in for Bear.")

## 7. Audio decode check

```
ffprobe → aac duration=139.291000s
```

Audio channel verified. B11 is audio_policy:silence (no narration mp3 for outro — correct behavior, clip has title-card jingle from component).

## Gaps / limitations

- No formal Gate V (frame-contrast-region) run in this session; parent's Gate-V clean status inherited for reused clips. Supervisor may re-run if required.
- Skin lint warnings for ClaudeComposerAsk916/ClaudeTitleOutro916 are expected (registered 916 variants, not violations).
- Human viewing and approval pending.

## Conclusion

All measurable checks pass. Short is 139.29s, 2160×3840, 8 beats, native portrait footage, no captions, Liam signs off, under the 180s cap with 40.7s headroom.
