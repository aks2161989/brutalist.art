# CHECKS-REPORT — vertical (9:16)

## PROOF GATE

- 12 SHOW  ·  0 justified-HOLD  ·  0 PUNT-flagged
- Same teaching arc as the landscape master (see landscape CHECKS-REPORT.md).

## GATE V — final_frame_check.py

```
$ python3 runtime/qc/final_frame_check.py <reel>/vertical --mp4 <candidate.mp4>
Frames sampled: 24  ·  BLOCKER: 0  ·  MAJOR: 0
Clean — no BLOCKER/MAJOR defects. ✓
```

- Portrait canvas (1080×1920 native → 2160×3840 4K). Safe area
  x 54–1026 · y 96–1824 (per `runtime/remotion/src/tokens/layout.ts`
  SAFE916).
- Contact sheet: `_qc/contact_sheet.png`. Read visually — the composer
  cards fit inside safe area; hesitant-writer BLUF fills; code cards
  reflow to portrait; verdict artifact stacks lines cleanly; outro is
  centered.
- Portrait-specific iterations:
  - B01 needed the well-documented `BrutalistHesitantWriter.tsx` design-box
    patch (memory feedback: `feedback_brutalist_hesitant_writer_portrait_scale_patch`)
    applied to the isolated toolkit — the shipped `scale` collapses to
    0.5625 on 9:16. Post-patch, fontSize 170 + lineSpacing 2.7 clears
    FILL_MIN 0.55 without edge-bleed.
  - B10 needed a shorter composer command and shorter output lines so the
    prompt does not overflow the narrower composer card. Same narration
    (audio unchanged); only the ON-SCREEN typed text was tightened.
    Segment title shortened from "Audit art icons on your own idea" →
    "Audit art icons" (the long form triggered edge-bleed on the right
    boundary of SAFE916).

## Audio decode

```
$ ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,duration,channels,sample_rate -of csv=p=0 <mp4>
aac,48000,2,199.333000
```

- Same 12 Kokoro `am_onyx` narration files as landscape (bit-identical
  where the wording is identical). B10 uses the SAME audio; only the
  visible composer text differs.

## Video

```
$ ffprobe -v error -select_streams v:0 -show_entries stream=width,height,duration,codec_name,r_frame_rate -of csv=p=0 <mp4>
h264,2160,3840,24/1,199.291667
```

- 2160×3840 (native 4K portrait). 24 fps.

## Compiler skin-lint notices (not defects)

```
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk
[art] SKIN LINT: B11: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro
```

- These are FALSE POSITIVES: the compiler's simple string match sees the
  `916` suffix as a wrong name. In reality `ClaudeComposerAsk916` /
  `ClaudeTitleOutro916` are the correct portrait wrappers around the
  landscape components (same schema, same render logic, portrait
  dimensions). Same warnings appeared on the reference episode
  `claude-liam-brutalist-command-help/vertical/` which shipped cleanly.

## Motion histogram (same as landscape)

```
code-cascade:7  type-on:2  hesitant-type:1  artifact-in:1  outro-card:1
WARNING: 'code-cascade' carries 7/12 beats (58%) — over the ~40% pantry cap
```

- Same explanation as landscape: this is a command teardown, each
  code-cascade beat is a different real code artifact.

## Portrait-specific paperwork status

- BUILD-PROMPT.md, SHOTLIST.md (this aspect), FACTCHECK.md, SOURCES.md,
  CHECKS-REPORT.md, TYPECHECK.md, PROMPTS.md — all present.
- SOURCES + FACTCHECK + PROMPTS copied from landscape (same facts hold
  across aspects). SHOTLIST is portrait-specific.

## Re-verification — 2026-09-12 (run_id 9c6d30d53da2466ea7266f53a51cf4ef)

Source SHA changed from `a83e2aa2…` to `0959b926…`; changes were to
SKILL.md files and unrelated Remotion components — no beat content,
scene components, audio, or clips changed. Gate V re-run:
frames=24 BLOCKER=0 MAJOR=0. Portrait contact sheet re-inspected visually
— all 12 beats clean, same conclusions as original review.
Video sha256 `d2c828fd…` unchanged.

## Conclusion

Vertical gate log: PROOF GATE ✓ · GATE V ✓ (0 BLOCKER / 0 MAJOR) ·
compile ✓ · atomic-verify ✓ · dimensions verified 2160×3840 · audio
verified. Ready for human review.
