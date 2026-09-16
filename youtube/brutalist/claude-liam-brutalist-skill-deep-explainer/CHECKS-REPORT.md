# CHECKS-REPORT.md — The deep-explainer Skill (landscape, run_id 9a0276f36c7f460da489b867130af37b)

Written after compile.py final compile and Gate V (final_frame_check.py) for this
invocation (2026-09-11). Supersedes the 2026-09-08 report.

## Aspect

- 16:9, 3840×2160 (native 4K composed at 1920×1080, rendered --scale=2), 24fps.
- File: `exports/landscape/claude-liam-brutalist-skill-deep-explainer.mp4`
- Duration: 216.2 s (previous: 214.0 s; diff: B07 narration extended from 14.89s to 17.13s
  to reflect new SKILL.md "executed examples first" doctrine).

## Source change since 2026-09-08 render

`skills/make/deep-explainer/SKILL.md` updated between renders. Key doctrinal shift:

> Old: "documentary-register vox body that leans on human-supplied static stills in `pantry/`"
> New: "documentary-register body built from executed examples, data and diagrams. Use
> human-supplied or archival stills in `pantry/` only when the artifact itself is necessary
> evidence, not to decorate a computation."

Additionally EXECUTABLE-EVIDENCE.md added as a reference in the VOX BEATS section.

**B07 updated** — narration, scene heading, body text, verdict pill, and spark line all
revised to accurately reflect the new preferred-mode statement. Audio regenerated (Kokoro
am_onyx, 17.13s). Scene re-rendered (SkillTeardownMechanism). All other beats unchanged —
the remainder of the SKILL.md doctrine (spine, gates, continuity, output contract) is
unchanged and the beats remain accurate.

## SHOW / HOLD / CARD tally (15 beats)

- **13 SHOW** — B00, B01, B02, B03, B04, B06, B07, B08, B10, B11, B12, B13, B14.
- **0 HOLD** — no archival photograph beats; film evidence is the SKILL.md (satisfies
  the "text/code/data → zero VOX beats" clause argued in B07).
- **0 CARD** — no FormACard beats (two act-divider CARDs dropped in original build).
- **2 bookend/CTA/outro** — B15 YOUR TURN (ClaudeComposerAsk) and B16 (ClaudeTitleOutro).
- **0 PUNT**.

## Teaching-arc checklist

- [x] **FRAMEWORK beat** — B03 (SkillTeardownMechanism, "It extends its parents").
- [x] **WORKED EXAMPLE** — B04 (SkillTeardownPipeline, fixed spine six nodes).
- [x] **FALSIFIABILITY / edge-case beat** — B07 (SkillTeardownMechanism, "Executed examples
  first" / zero-vox law: the old 20–25% quota was superseded; zero vox is a correct outcome).
- [x] **SCAFFOLDED viewer task** — B15 (ClaudeComposerAsk) with a real paste-ready prompt and
  a two-part rubric (linked mechanisms? push-back to ai-explainer?).
- [x] **Four bookends** — B00 cold open, B01 hesitant writer BLUF, B14 verdict, B16 outro.
- [x] **No source, no verdict** — every factual claim carries an on-screen artifact (SKILL.md
  quote block, folder tree, pipeline diagram, verdict lines). FACTCHECK.md maps every claim.

## Gate V — final_frame_check.py

```
python3 runtime/qc/final_frame_check.py <reel> --mp4 exports/landscape/...mp4
```

Result: `Frames sampled: 30 · BLOCKER: 0 · MAJOR: 0 — Clean.`

Report: `_qc/REPORT.md`. Beat sample frames inspected via Read tool:
- B00-50pct: ClaudeComposerAsk — ASK→RESULT, @HumanitariansAI folder chip, no bleed.
- B07-15pct, B07-50pct, B07-85pct: SkillTeardownMechanism — "Executed examples first."
  heading, body text, quote card, "EXECUTED EXAMPLES FIRST" verdict pill all within safe
  area; good canvas fill (~65% ink coverage), no overflow.
- B14-50pct: ClaudeVerdictArtifact — six-line split card, all lines legible.
- B16-50pct: ClaudeTitleOutro — title "The deep-explainer Skill.", @NikBearBrown
  (hardcoded per OUTRO-LOCK.md), slug-seeded pixel mascot. No subline.

## Motion-histogram lint

compile.py reported `illustrate: 7/15 (46%)` — over the ~40% cap. Same finding as
previous render — structural, not a Gate V defect. Six of the seven are
SkillTeardownMechanism beats because the skill's mechanisms ARE the film's subject.
Informational; human reviewer decides.

## Repairs made in this invocation

- B07 narration updated to reflect SKILL.md change (see above).
- B07 audio regenerated (17.13s, Kokoro am_onyx, --only B07).
- B07 scene re-rendered (SkillTeardownMechanism, updated props).
- Both aspects recompiled with --force; Gate V re-run on both.
- VISUAL-REVIEW.json updated with current run_id (9a0276f3…).
- SOURCES.md and FACTCHECK.md updated with new SKILL.md SHA.

## Schema checks

All Remotion prop names verified against toolkit's `runtime/remotion/src/scenes.json`
before authoring. No prop-name mismatches in this run (only B07 props changed; the
SkillTeardownMechanism schema is unchanged).

## Post-render conclusion

Gate V clean. Master mp4 decoded, exact-dimension and audio-decode verified by
compile.py's verify_output; `.verified.json` receipt written beside the master.
Human viewing/editing is next.

## Addendum — verification run_id 3675182de1474e65a36f82973472df95 (2026-09-12)

This invocation resumed after a Claude usage-limit pause. No rebuild was needed;
the video file hash (`c92261a3…`) is unchanged. Fresh QC frames extracted at
`_qc/frames-3675182de1474e65a36f82973472df95/`. All frames inspected via Read tool
and confirmed matching the prior Gate V report: correct scene content, no bleed,
no slates, no captions. VISUAL-REVIEW.json updated with current run_id.

## Addendum — verification run_id 2a3fc66d1cac49888a8086a1c9781797 (2026-09-12)

This invocation resumed after a Claude usage-limit pause. No rebuild was needed;
the video file hash (`c92261a30ce8c63d587d5d36821523d51f9d583f932dfc1daa98b6e826f9884f`) is
unchanged. Fresh QC frames extracted at `_qc/frames-2a3fc66d1cac49888a8086a1c9781797/`.
All frames inspected via Read tool: first-frame (ClaudeComposerAsk cold-open, @HumanitariansAI,
correct breadcrumb), B00-50pct (question typed, three answer lines), B01-50pct (BrutalistHesitantWriter
"deep-explainer is / a deeper / ai-|", no overflow), B07-50pct (SkillTeardownMechanism "Executed
examples first." heading, body, quote card, verdict pill within safe area), B14-50pct
(ClaudeVerdictArtifact 6-item split card, legible), B16-50pct (ClaudeTitleOutro "The
deep-explainer Skill." @NikBearBrown per OUTRO-LOCK.md), final-frame (outro held).
All frame hashes match the prior run_id 1acd0dfc… extraction — video byte-identical.
VISUAL-REVIEW.json updated with current run_id.
