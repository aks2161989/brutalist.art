# CHECKS-REPORT — The logo-motion Skill (portrait 9:16)

12 SHOW · 0 HOLD · 0 CARD · 0 PUNT. Same twelve narration beats as the
landscape master, rendered natively at 2160×3840.

## Per-beat classification

| Beat | Class | Portrait scene |
|---|---|---|
| B00 | SHOW | ClaudeComposerAsk916 |
| B01 | SHOW | BrutalistHesitantWriter916 (portrait BLUF recipe — 4 lines, fontSize 155, lineSpacing 2.5; scene component patched to portrait-aware scale) |
| B02 | SHOW | SkillTeardownAnatomy916 (vertical folder tree reflow) |
| B03 | SHOW | SkillTeardownPipeline916 (vertical INPUT ↓ … ↓ OUTPUT) |
| B04 | SHOW | SkillTeardownMechanism916 |
| B05 | SHOW | SkillTeardownMechanism916 |
| B06 | SHOW | SkillTeardownMechanism916 |
| B07 | SHOW | SkillTeardownMechanism916 |
| B08 | SHOW | SkillTeardownMechanism916 |
| B09 | SHOW | ClaudeVerdictArtifact916 |
| B10 | SHOW | ClaudeComposerAsk916 |
| B11 | SHOW | ClaudeTitleOutro916 |

## Teaching-arc checklist

- FRAMEWORK ✓ (B02/B03)
- WORKED EXAMPLE ✓ (B04–B08 use the same Medhavy sting numbers as landscape)
- FALSIFIABILITY ✓ (B08 three-tell diagnostic list)
- SCAFFOLDED TASK ✓ (B10 audit prompt + rubric)
- BOOKENDS ✓ (B00 cold open, B01 BLUF, B10 handoff, B11 outro)
- NO-SOURCE-NO-VERDICT ✓ (every quote block cites SKILL.md or TIMING.md)

## Commands run

```
$ python3 runtime/scripts/remotion_scenes.py <reel>/vertical --force
  ok: ClaudeComposerAsk916        → media/B00.mp4
  ok: BrutalistHesitantWriter916  → media/B01.mp4
  ok: SkillTeardownAnatomy916     → media/B02.mp4
  ok: SkillTeardownPipeline916    → media/B03.mp4
  ok: SkillTeardownMechanism916   → media/B04.mp4 … B08.mp4
  ok: ClaudeVerdictArtifact916    → media/B09.mp4
  ok: ClaudeComposerAsk916        → media/B10.mp4
  ok: ClaudeTitleOutro916         → media/B11.mp4

$ python3 runtime/scripts/compile.py <reel>/vertical --height 3840 --out <reel>/exports/vertical --force
  compiled B00 … B11
  wrote exports/vertical/claude-liam-brutalist-skill-logo-motion-vertical.mp4  (363.4s)

$ Gate V — internally invoked by compile.py
  Frames sampled: 24 · BLOCKER: 0 · MAJOR: 0
  Clean — no BLOCKER/MAJOR defects. ✓

$ Gate V re-run for invocation run_id 1468a15a76ca4a1a8c1300c4ca14f178 (2026-09-12)
  [gate-v] frames=24 BLOCKER=0 MAJOR=0 → vertical/_qc/REPORT.md
  Same result — vertical export unchanged, SKILL.md content consistent with all filmed beats.
```

## Skin-lint warnings (accepted, not blockers)

```
SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk
SKIN LINT: B11: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro
```

Standard non-blocker for portrait builds — the 916 wrappers ARE the portrait
form of those two scenes. The lint fires because the check is aspect-blind; the
same warning fires on every prior Brutalist portrait companion.

## Gate V pipeline

`runtime/qc/final_frame_check.py` internally uses `SAFE916 = {x:54, y:96, r:1026, b:1824, w:972, h:1728}` for portrait safe area. Verified via the two
per-aspect samples read below.

## B01 iteration log

1. text = `"A new logo\\nneeds a new scene.\\nOne prop, not a file."`, fontSize 130, lineSpacing 2.5 — Gate V: BLOCKER edge-bleed + MAJOR underfill 46%. Widest line (`One prop, not a file.`, 20 chars) exceeded the portrait safe width at 130 pt.
2. Shrunk fontSize to 95, lineSpacing 3.5 — edge-bleed cleared; canvas fill still under (33 %).
3. Reflowed to 5 short lines with fontSize 130 lineSpacing 2.5 — still under (47 %).
4. Settled on 4-line form `"A new logo\\nneeds\\na new scene.\\nAdd the prop."`, fontSize 155, lineSpacing 2.5 — Gate V CLEAN (0 blocker, 0 major).

The 4-line form aligns with the portrait BLUF recipe
(`feedback_hesitant_writer_portrait_bluf_recipe`) — several short lines and a
generous lineSpacing.

## Conclusion

Portrait pipeline: **PASS**. Gate V clean, native 9:16 layouts, teaching arc
complete, no unresolved slates. Human review pending.
