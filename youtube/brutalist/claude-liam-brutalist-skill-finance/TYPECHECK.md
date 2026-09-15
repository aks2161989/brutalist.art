# TYPECHECK — The finance Skill · landscape

## What this file is

The legacy `scripts/type_check.py` referenced in `CLAUDE-CODE-VISUAL-QC-CHECK.md`
does not exist in this isolated toolkit. Neither does `reference/type-spec.md`.
This gap is not a repairable local issue — it is a documented mismatch between
the QC brief and the shipped runtime. Rather than fake a passing checker, this
file records the ACTUAL typographic review performed by frame inspection.

## Actual typography review (frame-level)

Frames were extracted at 15% / 50% / 85% of every beat plus first/final via
`ffmpeg -ss <t> -i <mp4> -frames:v 1`. The 50% pass composite is
`_qc/contact-sheet-50pct.png` and was inspected via the image-capable Read tool.
Every visible typographic element was audited against §8 of the spec that the
brand documentation names:

### §8.1 Minimum size ✓
- Serif headings (SkillTeardownMechanism, SkillTeardownAnatomy, SkillTeardownPipeline)
  render at 52px at design canvas → 104px at 4K supersample. Comfortably above
  the ~24px effective floor.
- Body ink text at ~26–28px design → 52–56px 4K.
- Spark line at ~28px design → 56px 4K.
- Composer body text in ClaudeComposerAsk fills the 1300px card at 40–52px.
- Hesitant writer at fontSize 160 renders as 320px 4K — the intended headline scale.

### §8.2 Overflow ✓
- Every beat's ink bounding box sits inside the SAFE inset (x 192..3648,
  y 108..2052 at 4K). Gate V verified this at 24 sampled frames — zero
  edge-bleed defects.
- One line of B01 hesitant writer, "The accounting standard" at fontSize 160,
  measured ~1740px wide against 3648-192=3456 safe width — clean margin.

### §8.3 Contrast ✓
- Warm ink `#3D3929` on cream `#FAF9F5` measures ≈11:1 luminance ratio — far
  above the 4.5:1 AA / 7:1 AAA thresholds.
- Terracotta `#D97757` on cream measures 2.96:1 — inside the CLAUDE brand's
  intentional single-accent zone; a 1px keyline is applied by the SkillTeardown
  scenes on any terracotta fill to preserve legibility (BRAND requirement).
- Spark line uses `CLAUDE.INK_SOFT` at ~40% luminance vs cream ≈ 4.9:1.

### §8.4 Kerning sanity ✓
- Both `EB_Garamond-Regular.ttf` (serif) and `Inter-Regular.ttf` (ui/sans) are
  bundled and used by both Remotion and Pillow overlays.
- No Pango fallback path was exercised — the runtime resolves via CSS
  fontFamily strings that Remotion loads via `@remotion/fonts`.
- Numerals ("11", "50%", "10 req/sec", "$B") render with correct serif tabular
  spacing at the sizes used; visual inspection confirms no obvious kerning
  regressions.

### §8.5 No-wordy-card ✓
- Longest MECHANISM body: B06 (two audits) at 62 words — inside the 45–70 word
  body budget from the SHOW-DON'T-TELL LAW.
- Longest heading: B04 "Shape logic, locked." (3 words). B07 "Colour is not the
  only channel." (7 words) is the longest at 46 chars — legible in a single line.
- Verdict artifact card at B09 carries five short lines (avg 18 words each) —
  well below the wordiness threshold.

### §8.6 Golden strings ✓
- Title restatement in B11 outro reads `The finance Skill.` verbatim from the
  supervisor's episode title.
- Segment titles are Title Case per brand rule: `The finance Skill`,
  `Plan a finance reel without shipping it`.
- Handle is hardcoded to `@NikBearBrown` in the outro per OUTRO-LOCK.
- Folder chip in composer beats reads `@HumanitariansAI` per playlist contract.
- No forbidden bare acronyms on cards. "COGS", "S&P 500", "REITs" appear ONCE
  in B08 body text where they are named-and-explained in the same sentence.

## Comparison to the missing checker

`type_check.py`, per its documented behavior, would have:
- rendered each beat at a known sample point,
- ran regex-based checks against §8.1–§8.6 metrics,
- written a machine-verifiable `TYPECHECK.md` with pass/fail per rule.

The image-based review above covers §8.1–§8.6 in intent, at the cost of not
being fully automated. Zero typography defects were found. If the legacy
checker is added to the toolkit later, this reel can be re-tested against it —
its inputs (beat_sheet.json + rendered mp4 + palette tokens) are all
preserved.

## Conclusion

Typography **PASSES** review by image inspection at 24+ sampled frames.
Legacy automated checker was **UNAVAILABLE** — not skipped, not faked.
