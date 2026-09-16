# SHOTLIST — The logo-motion Skill — Short (portrait 9:16)

Native portrait 2160×3840. Six kept beats; every visual is a Root.tsx 916
Remotion composition reused unmodified from the parent portrait companion (no
crops, no re-renders).

| Beat | Duration (s) | Scene (Remotion) | What's on screen |
|---|---|---|---|
| B00 | 16.62 | `ClaudeComposerAsk916` | Cream composer; greeting `Hola, Liam` above; command types + three result lines below. |
| B01 | 18.86 | `BrutalistHesitantWriter916` | Cream page. Serif corrects `scene → prop`. `fontSize 155`, `lineSpacing 2.5` (portrait BLUF recipe). |
| B04 | 31.62 | `SkillTeardownMechanism916` | Eyebrow `MECHANISM · ACT 1`; heading "The build is a camera move."; body + quote + verdict pill `pull back, not fade in`. |
| B05 | 37.83 | `SkillTeardownMechanism916` | Eyebrow `MECHANISM · ACT 2`; heading "The ghost hold IS the effect."; phase-map body + quote + verdict pill `44% of the runtime, invisible`. |
| B09 | 30.33 | `ClaudeVerdictArtifact916` | Portrait artifact card; heading "One composition. Every mark."; six numbered recap lines stack. |
| B11 | 3.73 | `ClaudeTitleOutro916` | Portrait title restate `The logo-motion Skill.` with terracotta period + `@NikBearBrown` + seeded mascot. |

Total measured runtime: **139.04 s**.

## Reformat log

- All six Remotion beats were rewired to their `*916` portrait wrappers in the
  parent's build. This Short's `shorts.py` invocation detected each as native
  9:16 (2160×3840) and reused the parent's `media/<bid>.mp4` unmodified — see
  `[short] Bxx native portrait reused unchanged` lines.
- No center-cut of any landscape master. No pantry override. No new render.
- No endcard beat was appended (`--no-endcard`) — the film ends on the parent
  outro (B11) exactly as in the long. No outro was rewritten
  (`--no-outro-rewrite`).

## Slate policy

Zero unresolved slates. All six kept beats carry the parent's rendered
`media/<bid>.mp4` (status VIDEO).

## Dropped beats

B02, B03, B06, B07, B08, B10 — see CUT-PLAN.json for the per-beat rationale.
