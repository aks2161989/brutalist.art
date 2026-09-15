# TYPECHECK.md — The hai Skill (Short)

The toolkit has no legacy type-checker for beat sheets; this document is
the visual-typography review the current spec asks for.

## Typography survey (portrait, 2160×3840)

Frames inspected: `_qc/beat-frames/*-{15,50,85}.png` (24 frames total plus
the 2 fps contact sheet at `_qc/contact-2fps.png`).

### Serif register — headings and body

- ClaudeComposerAsk916 title "The hai Skill" and greeting "Hallo, Liam"
  (B00) — EB Garamond-style serif, high contrast on cream, no baseline
  overlap with the composer card. Sits above the horizontal center.
- BrutalistHesitantWriter916 body text (B01) — portrait-aware scale patch
  is doing what it should: the four-line serif ("The hai skill / forks a /
  source reel / The source stays intact") fills the safe area without
  collapsing to ~56%. This confirms `feedback_hesitant_writer_portrait_bluf_recipe`
  is still applied.
- SkillTeardownPipeline916 heading "Six steps. One shape." (B03) — serif
  heading + sans phase labels; six phase boxes fit vertically with even
  gutters and no bleed past safe.b.
- SkillTeardownMechanism916 heading + eyebrow (B04, B05, B08) — eyebrow
  in tracked sans caps, heading in serif with terracotta period ("Non-
  destructive fork.", "Plain register.", "Three files, three voices.").
  Body text is 8–9 lines wrapped inside safe area; quote block is inset;
  verdict pill sits above sparkLine footer.
- ClaudeVerdictArtifact916 (B09) — artifact card scaled ~92% of frame
  width, six numbered lines each 2 lines wrapped, terracotta numbers,
  title chip "The hai Skill" top-left.
- ClaudeTitleOutro916 (B11) — restated title in serif with terracotta
  period, "@NikBearBrown" handle in serif below, horizontal rules above
  and below.

### Mono / code register

- ClaudeComposerAsk916 command block (B00) — mono paste-ready ask; small
  send-arrow chip terracotta; folder chip "@HumanitariansAI" ink. No mono
  overflow.
- B00 output lines — mono, three lines, no wrap needed.
- Mechanism quote blocks (B04, B05, B08) — mono inside a light rule,
  cite line below in muted sans caps. Legible.

### Palette adherence

Cream `#F3EBDD` ground, ink `#2F2A26` type, terracotta `#D35F43` for
accents and the final outro period — consistent every beat. No stray
colors.

### Safe-area coverage

At beat 50% samples every kept beat's ink bbox covers well over the
55% Gate V minimum. No beat clips its heading, body, or verdict pill.
No `channel_title` compile overlay is present — deliberately omitted
per the parent build's `feedback_channel_title_portrait_bleed` recipe.

### Captions

None. `metadata.captions = false` in `beat_sheet.json` and the compile
plane does not burn captions on this Short.

## Beat-sheet lint

`shorts.py` and `compile.py` both ran `validate_project` on the derivative
sheet and returned zero fatal errors. `short_validation.status = ready`,
`errors = []` in the saved sheet.

## Skin-lint acknowledgement

`compile.py` emitted two SKIN LINT lines:

- `B00: palette=claude but the cold open is 'ClaudeComposerAsk916'`
- `B11: palette=claude but the outro is 'ClaudeTitleOutro916'`

These are inherited from the parent teardown and are false-positive
against the 916 portrait variants (the linter recognises the 16:9 names
only). The compositions are the correct Claude-palette portraits. No
change required.

## Conclusion

Typography is on-brand, portrait-legible, and free of clipping. The
retained cut inherits the parent's finished type layouts unchanged
because every beat was reused from native 2160×3840 renders.
