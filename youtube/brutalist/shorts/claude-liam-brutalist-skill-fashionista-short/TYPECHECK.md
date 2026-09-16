# Typecheck — The fashionista Skill (Short)

There is no separate legacy type checker for this pipeline. Beat sheet /
metadata schema validation is enforced by `runtime/scripts/build_safety.py`
(`validate_project`) at every `shorts.py` and `compile.py` invocation; both
passed for this Short.

What was checked visually (typography, layout, legibility) in the eight
retained portrait frames:

| Beat | Composition | Typography check |
|---|---|---|
| B00 | ClaudeComposerAsk916 | Eyebrow `BRUTALIST · SKILL TEARDOWN` and title `The fashionista Skill` render at the composer card's portrait scale; ask text wraps cleanly at ~44 char/line; three-line running output reads without truncation. |
| B01 | BrutalistHesitantWriter916 | Portrait-aware serif, `fontSize: 168`, `lineSpacing: 1.12` — text fills the safe column, `tutorial` → `experiment` swap lands on the same visual row. Per feedback_hesitant_writer_portrait_scale the shipped landscape scale would have collapsed to ~0.56× on 9:16; this beat uses the tuned portrait metrics. |
| B04–B07 | SkillTeardownMechanism916 | Eyebrow / heading / body / mono-quote / verdict pill / spark line all sit inside the portrait safe area; the quote block has a terracotta left border; the verdict pill uses positive tint for B04/B05/B06 and neutral tint for B07 (`verdictPositive: false`) — visible in `_qc/B07-p50.jpg`. |
| B09 | ClaudeVerdictArtifact916 | 6-line verdict list renders inside a rounded card with an ink title band; numbered enumeration is legible and does not overflow. |
| B11 | ClaudeTitleOutro916 | Ink ground, `The fashionista Skill.` (terracotta period), `@NikBearBrown` handle. Handle is hardcoded per OUTRO-LOCK.md. |

No burned-in captions on any beat (metadata.captions: false). No on-screen
text was clipped by the 2160×3840 canvas or the safe-area padding.

Beat-sheet shape:

- 8 beats, ids `[B00, B01, B04, B05, B06, B07, B09, B11]`, all
  `re.fullmatch(r'[A-Z][A-Z0-9_]*')`.
- `metadata.slug = claude-liam-brutalist-skill-fashionista-short`
  (matches `metadata.slug` regex).
- `metadata.aspect_ratio = 9:16`, `metadata.kind = short`,
  `metadata.playlist = Brutalist`, `metadata.voice = am_onyx`,
  `metadata.voice_kokoro = am_onyx`, `metadata.captions = false`.
- `metadata.short_validation.status = ready`, `errors = []`.
- `metadata.total_estimated_duration_seconds = 160.83`, less than the
  180-second cap (SHORTS_CAP_S).
