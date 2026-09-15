# Typography check — vertical (portrait)

## Missing legacy checker (documented gap, not a pass)

Same gap as landscape: `scripts/type_check.py` and `reference/type-spec.md` are
NOT shipped in this toolkit. Documented in landscape `TYPECHECK.md`; not
reported as a pass here either.

## What DID run

- `runtime/qc/final_frame_check.py` (Gate V — portrait branch, `SAFE916`) ran
  during `compile.py` and passed cleanly on 24 frames (0 BLOCKER, 0 MAJOR).
- Portrait-native compositions: `ClaudeComposerAsk916`, `BrutalistHesitantWriter`
  (portrait-aware scale patched in the isolated toolkit only — see
  `feedback_hesitant_writer_portrait_scale`), `SkillTeardownAnatomy916`,
  `SkillTeardownPipeline916`, `SkillTeardownMechanism916`, `ClaudeVerdictArtifact916`,
  `ClaudeTitleOutro916`. The three SkillTeardown\*916 wrappers were copied into
  this isolated toolkit's `runtime/remotion/src/scenes/` and registered in
  Root.tsx for this run only.

## Portrait typography ramp

The 916 wrappers use slightly different scale ramps than their landscape
counterparts, keyed off `useVideoConfig()`:

- `SkillTeardownMechanism916`: heading 82 px, body 40 px, quote 34 px (mono),
  citation 22 px, verdict pill 24 px, spark 34 px.
- `SkillTeardownAnatomy916`: title 72 px, mono file rows 32 px, callout 32 px, spark 34 px.
- `SkillTeardownPipeline916`: title 68 px, phase heading 42 px, phase desc 22 px,
  footer 26 px, spark 34 px.
- `BrutalistHesitantWriter` (portrait scale): `fontSize=118 * scale(2.0) = 236` px
  effective, `lineSpacing=2.2` — chosen per iteration to fit horizontally AND
  meet Gate V's 55% canvas-fill minimum (final coverage 56%).

## Visual typography review (LLM-eye pass)

Inspected every hero frame directly. Findings:

| Beat | Face(s) | Size look | Overflow | Contrast | Notes |
|---|---|---|---|---|---|
| B00 | serif greeting, sans command, mono output | portrait scale-down | none | high | folder chip `@HumanitariansAI` legible |
| B01 | large serif (fontSize=118, portrait scale=2.0 → 236 px effective) | fills ~56% of safe | none after iteration | high | five-line reflow keeps `re-cuts → frames` correction visible |
| B02 | serif title + mono file list + sans callout | vertical stack | none | high | callout box legible |
| B03 | serif nodes + sans desc + sans footer | vertical stack with down-arrows | none | high | terracotta accent on THE REPORT node |
| B04–B08 | serif heading + sans body + mono quote + sans cite + sans verdict pill | portrait ramp — body 40 px, quote 34 px | all fit portrait safe | high | verdict pill inside SAFE.b |
| B09 | serif heading + sans lines + terracotta numerals | portrait card | fits within safe | high | six lines reveal in order |
| B10 | serif greeting + sans command + mono output | fits portrait comp | none | high | 3-check rubric visible below |
| B11 | serif title, terracotta period, sans handle | large restate | inside safe | high | slug-seeded mascot renders |

No fallback substitution, no mystery glyphs, no kerning collisions. Spark
lines fit inside the portrait SAFE.b (`height * 0.05` in the 916 wrappers —
tested to be legible without bleed on the compiled output).

## Conclusion

- **Missing legacy checker:** yes — logged; NOT reported as a pass.
- **Runtime Gate V (portrait branch):** PASSED — 0 BLOCKER, 0 MAJOR.
- **LLM-eye typographic review:** PASSED — no defects observed.

Bear's human eye is the final sign-off. This document does not claim human
approval.
