# TYPECHECK — Brutalist Utility: remotion_scenes.py (portrait 9:16)

## Legacy checker status

`scripts/type_check.py` and `reference/type-spec.md` are **not present** in this toolkit revision — reported honestly, no fabricated pass.

## Actual visual typography review performed

Typography reviewed by direct frame inspection on the compiled 2160×3840 portrait master. Checked against SAFE916 (x:54, y:96, r:1026, b:1824 at 1080×1920) and Claude palette tokens.

**Checked per beat:**

1. **Face** — ClaudeComposerAsk916 uses serif for title/greeting, UI sans for folder chip and output lines. ClaudeCodeBeat916 uses mono for all code lines. SkillTeardownMechanism916 uses serif heading + sans body. All per component spec.
2. **Wrapping at portrait width** — composer question in B00/B10 wraps across multiple lines at 1080px portrait width (confirmed in `port_t5s.png`). Title "Brutalist Utility: remotion_scenes.py" wraps to two lines in the portrait ClaudeComposerAsk header. No truncation.
3. **Code font sizing** — `CODE_FONT = min(height × 0.019, width × 0.038)` = min(36.48, 41.04) = 36px at 1920px composition height. At 2× render = 72px. Lines readable without horizontal overflow.
4. **Safe-area at 9:16** — ink-extent anchors at `top: '5.5%'` / `bottom: '5.5%'` in ClaudeCodeBeat916, SkillTeardownMechanism916, ClaudeVerdictArtifact916 land at y=105.6px composition (211.2px render), inside SAFE916.y=96px boundary with 8px margin.
5. **BrutalistHesitantWriter portrait** — `lineSpacing: 2.6` lifts the BLUF from <55% (animation-sample underfill) to safe-area coverage ≥ 55%, per `[[feedback_hesitant_writer_portrait_bluf_recipe]]`.
6. **Outro portrait wrapping** — ClaudeTitleOutro916 displays "Brutalist Utility: remotion_scenes.py." wrapping to two lines at portrait width. No overflow past safe side boundaries.

## Frame evidence

`vertical/_qc/contact_sheet.png`, `vertical/_qc/review/port_t5s.png`, `port_last.png`. See `CHECKS-REPORT.md` and `VISUAL-REVIEW.json` for SHA-256 hashes.

## Known deferrals

- No auto-kerning check for pathological glyph pairs in portrait layout.
- Legacy `type_check.py` absent; visual typography signed off by frame inspection only.
