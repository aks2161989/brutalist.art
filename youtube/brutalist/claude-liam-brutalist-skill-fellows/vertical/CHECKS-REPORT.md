# Checks report — vertical (portrait)

Reel: `The fellows Skill` — `claude-liam-brutalist-skill-fellows-vertical`
Aspect: 9:16 · 2160×3840 · 24 fps · 261.88 s · aac stereo
Run: `616bfc2fadd2479fadc72138c055fa1a` (re-verified; previous run `e71dd104` — SKILL.md content unchanged, toolkit baseline updated)

## Portrait strategy

This is a FULL-LENGTH native 9:16 companion, not a Shorts cut and not a
center-crop of the landscape master. Same 12 beats, same audio (Kokoro
`am_onyx`), same source-of-truth beat sheet with three native 916 wrappers
substituted for their landscape siblings. `art vertical` was consulted for the
planning rules (PIPELINE-SAFETY.md §Isolated portrait companions and Shorts):
it plans; it does not magically reframe. Native compositions were required
because the mechanism/pipeline/anatomy cards do not tolerate a landscape
center-crop.

## Beat classification (PROOF GATE)

12 SHOW / 0 justified-HOLD / 0 PUNT-flagged (identical structure to landscape).
Every body beat classifies SHOW; no unresolved slates.

## Teaching arc checklist (identical to landscape)

- FRAMEWORK ✓  ·  WORKED EXAMPLE ✓  ·  FALSIFIABILITY ✓  ·  SCAFFOLDED TASK ✓
  ·  BOOKENDS ✓  ·  NO-SOURCE-NO-VERDICT ✓

## Compile

Command:
```
python3 runtime/scripts/compile.py <reel>/vertical --height 3840 --force --out <reel>/exports/vertical
```

Result:
```
[art] compiled B00–B11  VIDEO   (12 beats, all VIDEO)
[art] motion histogram: reveal:8  type-on:3  hold:1
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk
[art] SKIN LINT: B11: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro
[art] build stamp → beat_sheet.json (12/12 filled)
[art] wrote …/claude-liam-brutalist-skill-fellows-vertical.mp4  (261.9s, audio: per-beat timeline …)
[art] slots: 12/12 filled — B00:VIDEO … B11:VIDEO
```

**Two SKIN LINT warnings** on B00 and B11 are the expected portrait-native
trade-off: the 916 variants of ClaudeComposerAsk and ClaudeTitleOutro exist in
the shipped Root.tsx precisely so portrait can reflow natively. The lint is
scoring against the aspect-blind landscape name — not a defect. Not a Gate
refusal.

ffprobe on the final MP4:
```
$ ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate,duration -of csv=p=0
2160,3840,24/1,261.875000
$ ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,channels -of csv=p=0
aac,2
```

Actual dimensions match FELLOWS-SUBMISSION.md's native-portrait requirement
(vertical at **2160×3840**). Not an upscale of a center-crop.

## Gate V (frame-level visual QC)

Ran as part of `compile.py`. Passed cleanly on the final attempt (`frames=24
BLOCKER=0 MAJOR=0`) after two portrait-specific B01 iterations:

1. **Iteration 1** — after copying `SkillTeardown*916` wrappers and patching
   `BrutalistHesitantWriter`'s scale (portrait-aware `min(w/1080, h/1920)`,
   see `feedback_hesitant_writer_portrait_scale`), the hesitant writer's
   text still bled past left/right safe at the shipped fontSize=148 (2× scale
   in portrait = effective 296 px, wider than the 2160-px canvas allows).
   Repaired by reducing `fontSize` 148→92.
2. **Iteration 2** — with the text now fitting horizontally, coverage was
   only 21%–41% (under FILL_MIN=0.55). Repaired by splitting the widest line
   at a word break (`re-cuts the fellows video.` → `re-cuts the / fellows
   video.`) and using `fontSize=118, lineSpacing=2.2` — content now spans
   ~1631×2305 px of the 1944×3456-px safe area (~56% coverage).

Both iterations are recorded in `PROMPTS.md`. The landscape sheet was NOT
changed — landscape B01 uses the smaller landscape-safe font (148, lineSpacing
1.2, charMs 20).

`_qc/REPORT.md` records the final clean pass. `.verified.json` receipt sits
next to the export in `exports/vertical/` (SHA-256 03ca7eda…).

## Visual review (LLM-eye pass)

Extracted 12 hero frames (one per beat, at mid-point of the vertical master)
plus the Gate V contact sheet. Inspected directly with the image-capable Read
tool. Frames live at `_qc/frames/V_*.jpg`; combined contact sheet at
`_qc/contact-vertical.png`. Findings:

- B00 — portrait composer, greeting "Hallo, Liam" above, ask command below,
  three result lines, `@HumanitariansAI` chip. No overflow.
- B01 — five-line hesitant writer completes "The fellows skill / frames the /
  fellows video. / The fellows report / plays untouched." Correction landed.
- B02 — anatomy folder tree stacks vertically (SkillTeardownAnatomy916),
  callout box lands underneath, spark line at bottom-left of safe.
- B03 — pipeline reflows to a vertical stack (SkillTeardownPipeline916):
  INPUT ↓ ASK ↓ SUMMARY ×2–3 ↓ THE REPORT (terracotta) ↓ BEAR'S NOTES ×2 ↓
  YOUR TURN + HAI OUTRO ↓ OUTPUT.
- B04–B08 — SkillTeardownMechanism916 typography ramp — heading, body, verbatim
  quote, verdict pill all fit inside the portrait safe area.
- B09 — ClaudeVerdictArtifact916 renders the six numbered lines in a
  portrait-native card.
- B10 — portrait Your Turn composer with the same dry-run prompt + rubric.
- B11 — ClaudeTitleOutro916 renders title restate, `@NikBearBrown` handle,
  slug-seeded mascot.

No overlap, no clipping past safe, no unwanted captions, no unresolved slates.

## Availability log

- `runtime/qc/final_frame_check.py` (Gate V, portrait branch: `SAFE916 = {x:54,
  y:96, r:1026, b:1824}` scaled to 2160×3840) IS present and PASSED.
- Legacy `scripts/type_check.py` remains absent; portrait-only substitute in
  `TYPECHECK.md`.
- `art vertical` (`skills/make/vertical/`) — the planning skill was read; it
  does not generate media itself. The native portrait media was produced by
  `runtime/scripts/remotion_scenes.py` against the 916 wrappers.

## Conclusion

Vertical master: **CLEAN**. All checks that exist in this toolkit passed.
Bear's viewing/editing is next; the file is not published.
