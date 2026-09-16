# TYPECHECK.md — The anthropics Skill (landscape 3840×2160)

*Actual typography review versus the absent legacy checker.*

## The legacy checker

`scripts/type_check.py` and `reference/type-spec.md` are referenced in
older Brutalist docs. Neither ships in this isolated toolkit snapshot.
Their absence is recorded honestly rather than claimed as "checker
passed" — that would be dishonest and forbidden by the BUILD-PROMPT.

## What was actually reviewed

Frames were sampled with `runtime/qc/final_frame_check.py` at the 50 %
and 85 % steady-state points of each beat, plus first/final frames from
the compiler's own gate. All 22 frames plus the reel-wide contact sheet
were opened with the image-capable Read tool and inspected against the
following typographic contract:

- **Face selection.** Serif is used for narrative headings and the
  BLUF; UI mono for the composer chrome and code-block chrome; small
  bold uppercase (`CLAUDE_FONT.ui`) for eyebrows and pill labels.
  Correct across every beat.
- **Weight and colour.** Ink `CLAUDE.INK` on `CLAUDE.PAGE`; the terracotta
  `CLAUDE.SPARK` is the one accent — used for the outro period, the
  hesitant-writer "about-to-be-deleted" flash, the composer send button,
  and the outro rule. No secondary accents were introduced. WCAG
  luminance separation (Gate V's `low-contrast` check) reported no
  frames under `CONTRAST_MIN = 0.30`.
- **Kerning + spacing.** Serif titles at 4K show clean glyph pairs; no
  metric-hinting artefacts, no double-spaced words, no line-length
  breakage.
- **Numerals.** The single on-screen number, "142 lines" on B02,
  reconciles with `wc -l skills/make/anthropics/SKILL.md` = 142
  (`FACTCHECK.md`). No other numbers appear, so internal consistency
  holds by construction.
- **Punctuation as accent.** The outro title's terminal period is the
  brand's one terracotta glyph on that beat. Present.
- **Eyebrow / body / verdict hierarchy.** Every `SkillTeardownMechanism`
  beat (B04–B07) uses the same eyebrow ▸ heading ▸ body ▸ quote ▸
  verdict rhythm — checked in the contact sheet at a glance.
- **Cite lines.** Every quote block on B04–B07 carries a
  `anthropics SKILL.md · <section>` cite. Present.

## Findings

- **No overlap, no clipping, no unresolved slates.** Gate V confirms
  0 blocker / 0 major.
- **No burned-in captions or SRT/VTT overlays** — the BUILD-PROMPT
  bans captions; the diagrams, code snippets, and legible labels are
  instructional visuals, not transcripts. Verified visually on all 11
  beats.
- **Handle: `@HumanitariansAI` throughout** — B00, B09 (composer chip)
  and B10 (outro). No `@NikBearBrown` string appears anywhere on
  screen; this required the channel-adapted `AntOutro` variant since
  the shipped outro hardcodes the wrong handle.
- **In-for-Bear signoff** on B10: `LIAM, IN FOR BEAR.` (verbatim, per
  the OUTRO LAW).

## Conclusion

Legacy checker absent — noted and worked around by direct visual
inspection. No typographic defects, no accessibility failures, no
brand drift. Human review pending.
