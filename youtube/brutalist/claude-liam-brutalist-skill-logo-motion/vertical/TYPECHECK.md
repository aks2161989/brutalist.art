# TYPECHECK — The logo-motion Skill (portrait 9:16)

## Static `type_check.py`

Same gap as landscape: not shipped in this isolated toolkit. TYPECHECK is
visual review of the final master + Gate V's `final_frame_check.py`.

## Gate V — actual result

```
Frames sampled: 24  ·  BLOCKER: 0  ·  MAJOR: 0
Clean — no BLOCKER/MAJOR defects. ✓
```

Portrait safe area: `SAFE916 = {x:54, y:96, r:1026, b:1824, w:972, h:1728}`
(from `runtime/qc/final_frame_check.py`).

## Frame-level Read-tool inspection

Per-beat mid-frames (spot-check) plus Gate V's contact sheet were read:

- **B00 — portrait composer:** greeting "Hola, Liam" sits above the composer
  card; command line wraps naturally to two lines within safe width; three
  result lines below the composer land inside SAFE916. Terracotta spark visible.
- **B01 — hesitant writer 4-line BLUF:** at portrait scale 1.0 (patched from
  the collapsed 0.5625), fontSize 155 renders as full-cap serif ~155 px tall.
  Widest line "a new prop." fits inside safe.w = 972. Correction `scene → prop`
  visible; the cursor blink at the end of "Add the prop." stays inside safe.r.
- **B02 — SkillTeardownAnatomy916:** eyebrow, title, folder tree (10 rows,
  vertical stack), callout box. Each row's monospace label + accent tag
  wraps within column. Portrait safe bottom margin preserved.
- **B03 — SkillTeardownPipeline916:** INPUT ↓ four phase boxes (SET PHASE MAP
  in terracotta accent) ↓ OUTPUT. All boxes stay inside portrait column.
- **B04–B08 — SkillTeardownMechanism916:** heading in serif at 82 px wraps to
  two lines in portrait; body copy at 40 px reads; quote block with terracotta
  left rule stays inside SAFE916 with padding; verdict pill and spark line
  land at bottom of safe area.
- **B09 — ClaudeVerdictArtifact916:** six recap lines stack; each stays
  inside safe area.
- **B10 — Your Turn composer916:** paste-ready audit prompt renders across
  multiple lines; three-line output rubric visible.
- **B11 — ClaudeTitleOutro916:** portrait title-restate + @NikBearBrown handle
  + slug-seeded mascot fit inside portrait safe area.

## Kerning / min-size

- Serif greetings + outro title: >72 px effective — legible.
- Sans body copy: 40 px — legible.
- Mono code/quote: 30-34 px — legible.
- No Pango-fallback kerning defect observed.

## Conclusion

**PASS (visual review).** Gate V clean; per-beat frame Read matches. Missing
static checker is a documented gap, not a hidden failure.
