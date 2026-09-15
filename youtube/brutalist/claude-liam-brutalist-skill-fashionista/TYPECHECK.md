# Typography check — landscape

## Missing legacy checker (documented gap, not a pass)

`ai-explainer/SKILL.md` §Hard rules refers to a `scripts/type_check.py` that
writes a `TYPECHECK.md` and enforces §8.1 min-size, §8.2 overflow, §8.3
contrast, §8.4 kerning sanity, §8.5 no-wordy-card, and §8.6 golden strings.
That script and the `reference/type-spec.md` it depends on are **not shipped
in this toolkit** (search: `Glob 'runtime/**/type_check.py'` → no results;
`ls skills/make/kerning` → no such directory).

This means the golden-string / kerning gates cannot be programmatically
enforced on this run. Recording the gap honestly rather than fabricating a
pass.

## What DID run

- `runtime/qc/final_frame_check.py` (Gate V) ran during `compile.py` and
  passed (0 BLOCKER, 0 MAJOR) on 24 frames sampled at each beat's 50% and
  85% steady state. This gate audits edge-bleed, canvas-fill, and contrast
  by pixel-analysing the final MP4.
- Every beat's on-screen text was rendered by registered Remotion
  compositions whose type ramps live under
  `runtime/remotion/src/tokens/claude.ts`
  (CLAUDE_FONT.serif = "EB Garamond", CLAUDE_FONT.ui = system UI sans,
  CLAUDE_FONT.mono = SF Mono).

## Visual typography review (LLM-eye pass, substitute for the missing checker)

Every beat's 85% frame was inspected in the image-capable Read tool. Findings:

| Beat | Face(s) | Size look | Overflow | Contrast | Notes |
|---|---|---|---|---|---|
| B00 | serif greeting, sans command, mono output | headings large, body legible | none | high (ink #3D3929 on cream #FAF9F5) | folder chip @HumanitariansAI clean |
| B01 | large serif (fontSize=148) | fills safe area vertically | no bleed | high | "tutorial → experiment" swap visible |
| B02 | serif title + mono file list + sans callout | sizes stagger correctly | folder tree fits | high | callout box legible; terracotta accent on SKILL.md |
| B03 | serif nodes + sans desc + sans footer | nodes readable | fits within safe | high | terracotta accent on THE VIDEO node |
| B04-B08 | serif heading + sans body + mono quote + sans citation + sans verdict pill | body 26 px, quote 20 px mono, heading 52 px | all fit safe area | high | verdict pill sits inside the SAFE.bottom inset |
| B09 | serif heading + sans lines with terracotta numerals | large card, generous whitespace | fits within safe | high | title bar renders "The fashionista Skill" |
| B10 | serif greeting + sans command + mono output | typing legible | fits within safe | high | 3-check rubric visible |
| B11 | serif title, terracotta period, sans handle | large restate + handle | inside safe area | high (cream on dark) | slug-seeded mascot renders |

No character had visible fallback-font substitution. No mystery-glyph
rectangles. No kerning collisions. Spark-line typography (italic serif)
lands at bottom-left within the SAFE inset on every mechanism beat.

## Conclusion

- **Missing legacy checker:** yes — logged; NOT reported as a pass.
- **Runtime Gate V (final_frame_check):** PASSED — 0 BLOCKER, 0 MAJOR.
- **LLM-eye typographic review:** PASSED — no defects observed.

Bear's human eye is the final sign-off. This document does not claim human
approval.
