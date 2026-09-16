# TYPECHECK — Brutalist Utility: brand_variant.py — Short

There is no legacy `runtime/scripts/type_check.py` in this toolkit. The
public docs reference such a checker; it is not shipped. This report is an
actual visual-typography review of the six kept frames, not a claim that a
missing script passed.

## Visual typography — six kept beats, cream ground `#FAF9F5`, ink `#3D3929`, terracotta `#D97757`

| Beat | Component | Serif faces | Findings |
|------|-----------|-------------|----------|
| B00 | ClaudeComposerAsk916 | EB Garamond title `brand_variant.py`; small-caps eyebrow; sans body inside the composer card; monospace running text | Title clears the top rule; composer card centred inside SAFE916 inset; five output lines fit without wrapping past the composer chip; no text within 12 px of the safe-area rectangle. |
| B01 | BrutalistHesitantWriter916 | Serif line at scale ≈ 150 px / lineSpacing 2.25 | Portrait-scale ternary from `feedback_hesitant_writer_portrait_scale_patch.md` applied by the parent; ink bbox covers >55% of SAFE916 across the 15/50/85 samples. Corrected sentence settles cleanly on the last frame; no orphaned trigger tokens. |
| B02 | SkillTeardownMechanism916 | Serif heading; sans body; verbatim quote card in mono | Portrait swap for the horizontal `SkillTeardownPipeline` per memory `feedback_skillteardown_pipeline_portrait.md`. Verdict chip `ONE CANONICAL · THREE AUDIENCES · ONE VARIANT AT A TIME` sits inside SAFE916 with terracotta pill border intact; spark line lands under the diagram. |
| B04 | ClaudeCodeBeat916 | Serif title (updated to "verbatim from demo/RUN-LOG.txt §2+5"); mono body | Re-rendered 2026-09-13 with corrected code formatting. Adaptive font (both axes, per memory `feedback_claude_code_beat_adaptive_font.md`) collapses so the two compact `[variant]` status lines and the emitted `.metadata` block fit in the portrait viewport; longest line (`"channel_title": "@HumanitariansAI",`) fits within the card bounds. |
| B09 | ClaudeVerdictArtifact916 | Serif heading; sans numbered list | Six bullets with `input · lookup · resolve · stamp · todo · emit` — every line wraps once inside the artifact card, no line touches the card's right border. |
| B11 | ClaudeTitleOutro916 | Serif title (large); serif handle | Title `Brutalist Utility: brand_variant.py.` occupies the visual centre; `@NikBearBrown` (locked handle per OUTRO-LOCK.md) sits below with slug-seeded mascot; upper and lower rules land inside SAFE916. |

## Kerning and pairs specifically checked

- `brand_variant.py` mono compound — no compressed underscore/dot pair.
- `Yassou, Liam` — the comma sits flush with the `u` descender line; no
  double-space artefact.
- `af_bella` / `am_onyx` — underscore/letter pairs typeset without spacing gap
  in the mono body of B04.
- `@NikBearBrown` / `@HumanitariansAI` — `@` sits at the correct cap-height
  vertical bearing in both the composer folder chip and the outro handle.

## Skin-lint (from compile.py)

```
SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916'
SKIN LINT: B11: palette=claude but the outro is 'ClaudeTitleOutro916'
```

Cosmetic, inherited from the parent. These portrait compositions are the
correct ones for a 9:16 render; the lint is a legacy naming check that
expects the landscape IDs. Not a blocker. Every prior Ep 30-39 Short carries
identical warnings.

## Conclusion

Typography of this cut is inherited unchanged from the parent's native-portrait
renders. No new text was drawn. No new component was invented. No 9:16
underfill (Gate V) or portrait-bleed regression observed at 15/50/85 percent
of any kept beat.
