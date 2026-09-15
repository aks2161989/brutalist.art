# Typography check — portrait

## Missing legacy checker

Same as landscape TYPECHECK.md: `scripts/type_check.py` and its
`reference/type-spec.md` companion are absent from this toolkit. Gap
documented, NOT reported as a pass.

## What DID run

- `runtime/qc/final_frame_check.py` (Gate V) ran during `compile.py` and
  passed on portrait (0 BLOCKER, 0 MAJOR) after the B01 re-authoring described
  in CHECKS-REPORT.md.
- All body compositions use the same CLAUDE_FONT ramp as landscape
  (EB Garamond serif, UI sans, SF Mono).

## Visual typography review (LLM-eye pass)

| Beat | Face(s) | Portrait fit | Notes |
|---|---|---|---|
| B00 | serif greeting + sans command + mono output | fills portrait column | folder chip inside SAFE.b |
| B01 | large serif (fontSize=168, portrait-aware scale patch applied) | fills 7 short lines within SAFE916 | correction "tutorial → experiment" lands mid-beat |
| B02 | serif title + mono file list + sans callout | stacked vertically | terracotta accent on SKILL.md |
| B03 | serif nodes + sans desc + sans footer | vertical stack | INPUT + 3 phases + OUTPUT + footer + spark all inside safe |
| B04-B08 | portrait mechanism cards | narrower body wraps cleanly | quote block + citation + verdict pill all inside safe |
| B09 | serif heading + sans lines with terracotta numerals | six lines wrap cleanly | title bar renders "The fashionista Skill" |
| B10 | serif greeting + sans command + mono output | rubric lines fit | 3 checks legible |
| B11 | serif title, terracotta period, sans handle | inside portrait safe area | slug-seeded mascot renders |

No character had visible fallback-font substitution. No mystery-glyph
rectangles. No kerning collisions. Spark-line typography lands at
bottom-left within SAFE916 on every mechanism beat.

## Conclusion

- **Missing legacy checker:** yes — logged; NOT reported as a pass.
- **Runtime Gate V:** PASSED (portrait) — 0 BLOCKER, 0 MAJOR.
- **LLM-eye typographic review:** PASSED — no defects observed.

Human eye remains the final sign-off.
