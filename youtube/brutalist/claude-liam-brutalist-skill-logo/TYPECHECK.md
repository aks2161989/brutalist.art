# TYPECHECK — The logo Skill (landscape)

## Legacy `scripts/type_check.py` — MISSING

`skills/make/ai-explainer/SKILL.md §Hard rules · GATE T` requires
`scripts/type_check.py` (§8.1 min-size, §8.2 overflow, §8.3 contrast,
§8.4 kerning sanity, §8.5 no-wordy-card, §8.6 golden strings). That script is
**not shipped** in this toolkit copy — grep confirms no matching file exists
under `runtime/scripts/` or `scripts/`. This gap is a known one referenced in
`docs/` and `SCENE-DOC-TODO.md`; it is recorded honestly per BUILD-PROMPT
guidance, not silently claimed as passed.

## Substitute — visual typography review

Every beat's frames at 15/50/85% were extracted (`_qc/samples/`) and Read as
images via the image-capable Read tool. Typography audit against the rubric
GATE T *would* enforce:

### §8.1 minimum size

- Body copy on mechanism cards (B04–B08) renders at effective ~34px on the 4K
  master (SkillTeardownMechanism `fontSize: 34`, letter-spacing default,
  EB Garamond fallback via Claude tokens). Comfortably above the 24px floor.
- Cite lines under quote blocks (~18px) are labels, not primary text —
  intentional secondary weight.
- Composer body (B00, B10): monospace body at ~30px on 4K; well legible.
- Hesitant writer serif at design fontSize 148 (landscape, 1920x1080 reference),
  super-sampled to 4K — the largest type in the reel by design.
- Verdict artifact (B09) six lines at ~28px — legible at every sample.

### §8.2 overflow

- No visible clipping at any sampled frame.
- The B09 six-line verdict card fits within the artifact card at all reveals.
- The B10 handoff prompt wraps naturally inside the composer input — no
  off-canvas text.
- Composer output lines (B00, B10) wrap; no truncation.

### §8.3 contrast

- Warm ink `#3D3929` on cream `#FAF9F5` — measured luminance ratio > 8.7:1
  (Claude palette by construction).
- Terracotta `#D97757` used only as accent — not for body.
- The dark polarity outro (B11) uses cream on ink — high contrast by
  construction.

### §8.4 kerning sanity (Pango fallback catch)

- All type sizes and families sampled resolve to EB Garamond (serif) or system
  UI sans (SF Pro on macOS) or SF Mono (mono). No fallback to Pango's default
  DejaVu family (which would be the classic FAIL signal).
- Spot-checked B00 greeting "Hola, Liam" — serif ligatures visible, no
  fallback square-box glyphs.

### §8.5 no-wordy-card

- Every card carries ≤ ~35 words of body text (SkillTeardownMechanism body
  props all ≤ 55 words, cited to source, deliberately compact — the *voice*
  carries the extra explanation).
- The B10 composer prompt is longer (~130 words) — but that IS the paste-ready
  prompt for the viewer; it is intended to be read at pause.

### §8.6 golden strings

Not applicable — this toolkit has no `golden.json` fixture for this reel; the
substitute test is the frame-level read audit itself.

## Verdict

**No PANGO fallback observed. No overflow observed. No contrast defect
observed.** The absent legacy `type_check.py` gate is a known toolkit gap,
substituted here by visual review with the image-capable Read.

Bear's editing pass is next.
