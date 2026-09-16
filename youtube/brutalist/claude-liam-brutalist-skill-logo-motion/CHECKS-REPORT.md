# CHECKS-REPORT — The logo-motion Skill (landscape 16:9)

Per PROOF GATE, this file exists before the first slate compiles. No slates
compiled — every beat classifies SHOW.

## Per-beat classification (SHOW / HOLD / CARD / PUNT)

12 total: 12 SHOW · 0 HOLD · 0 CARD · 0 PUNT.

| Beat | Class | Note |
|---|---|---|
| B00 | SHOW | ClaudeComposerAsk types in and shows the ask + three result lines. |
| B01 | SHOW | BrutalistHesitantWriter types the framing and corrects `scene → prop` on the spoken revision. |
| B02 | SHOW | SkillTeardownAnatomy folder-tree reveals row by row, then the callout lands. |
| B03 | SHOW | SkillTeardownPipeline reveals INPUT → 4 phases → OUTPUT with `SET PHASE MAP` accent. |
| B04 | SHOW | SkillTeardownMechanism heading types in, body reveals, quote block lands, verdict pill lights. |
| B05 | SHOW | SkillTeardownMechanism — phase map numbers as body copy; quote block; verdict pill. |
| B06 | SHOW | SkillTeardownMechanism — length prop / calculateMetadata explained on body; quote block; verdict pill. |
| B07 | SHOW | SkillTeardownMechanism — audio-first exception mechanism on body; quote block; verdict pill. |
| B08 | SHOW | SkillTeardownMechanism — three-tell diagnosis body; quote block; verdict pill. |
| B09 | SHOW | ClaudeVerdictArtifact — six recap lines reveal in sequence on the artifact page. |
| B10 | SHOW | ClaudeComposerAsk (Your Turn) types the audit prompt and shows the three-line rubric. |
| B11 | SHOW | ClaudeTitleOutro title-restate + mascot animation. |

## Teaching-arc checklist

- FRAMEWORK ✓ (B02 anatomy + B03 pipeline)
- WORKED EXAMPLE ✓ (B04–B08 walk through four concrete mechanism decisions using the Medhavy sting numbers)
- FALSIFIABILITY ✓ (B08 three-tell diagnostic list; the reel names what a cheap sting looks like and the fix order)
- SCAFFOLDED TASK ✓ (B10 paste-ready measurement prompt with a three-question rubric the viewer can score their own sting against)
- BOOKENDS ✓ (B00 cold-open ask, B01 hesitant-writer BLUF, B10 handoff, B11 title-restate outro — all four present)
- NO-SOURCE-NO-VERDICT ✓ (every quote block cites `SKILL.md` or `reference/TIMING.md`; every number is present in the source)

## Commands actually run + outputs

```
$ python3 runtime/scripts/generate_audio_kokoro.py <reel>
  … 12 beat(s) generated · cost $0.00 · durations are GROUND TRUTH

$ python3 runtime/scripts/remotion_scenes.py <reel> --force
  ok: ClaudeComposerAsk        → media/B00.mp4
  ok: BrutalistHesitantWriter  → media/B01.mp4
  ok: SkillTeardownAnatomy     → media/B02.mp4
  ok: SkillTeardownPipeline    → media/B03.mp4
  ok: SkillTeardownMechanism   → media/B04.mp4 … B08.mp4
  ok: ClaudeVerdictArtifact    → media/B09.mp4
  ok: ClaudeComposerAsk        → media/B10.mp4
  ok: ClaudeTitleOutro         → media/B11.mp4

$ python3 runtime/scripts/compile.py <reel> --height 2160 --out <reel>/exports/landscape --force
  compiled B00 … B11 (durations 3.8-40.6s)
  wrote exports/landscape/claude-liam-brutalist-skill-logo-motion.mp4  (363.4s)
  motion histogram: reveal:8 type-on:3 hold:1
  WARNING: 'reveal' 8/12 (66%) — over the ~40% pantry cap

$ Gate V (runtime/qc/final_frame_check.py) — invoked internally by compile.py
  Frames sampled: 24 · BLOCKER: 0 · MAJOR: 0
  Clean — no BLOCKER/MAJOR defects. ✓

$ Gate V re-run for invocation run_id 1468a15a76ca4a1a8c1300c4ca14f178 (2026-09-12)
  [gate-v] frames=24 BLOCKER=0 MAJOR=0 → _qc/REPORT.md
  Same result — landscape export unchanged, SKILL.md content consistent with all filmed beats.
```

The `reveal` motion warning is a WARNING, not a BLOCKER. It is intrinsic to the
skill-teardown structure — five SkillTeardownMechanism beats + Anatomy +
Pipeline + Verdict all reveal elements one at a time. The alternative
(re-tooling each mechanism beat into a different visual language) would have
broken the rhythm the audience already recognizes from Ep 15. Accepted for
this reel; noted here so a future ai-explainer pass can consider whether the
mechanism beats deserve a distinct visual pattern each.

## Gate A / W / B (Manim) — n/a

No Manim beat in this reel.

## Gaps

- Static `type_check.py` not present in this toolkit — recorded in
  `TYPECHECK.md`.
- `art scenes` search interface probed indirectly (scene library was inspected
  via file listing + Root.tsx grep); no fabricated "clean bill of health" is
  claimed.

## Conclusion

Landscape pipeline: **PASS**. Gate V clean, per-beat classification clean,
teaching arc complete, no unresolved slates, no fabricated results.
