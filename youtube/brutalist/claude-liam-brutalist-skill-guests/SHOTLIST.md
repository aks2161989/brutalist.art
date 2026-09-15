# SHOTLIST — The guests Skill (landscape 16:9, 3840×2160)

Twelve beats. All composed in Remotion via
`runtime/scripts/remotion_scenes.py`, `--scale=2` (true 4K supersample). Every
per-beat clip is `media/B##.mp4`; the compiler conforms it to the measured
Kokoro audio duration. No slates, no Manim, no external footage.

| # | Beat | Composition | Motion | Audio (s) | Notes |
|---|---|---|---|---|---|
| B00 | ASK / cold open | `ClaudeComposerAsk` | type-on | 13.16 | greeting `Hallo, Liam`, folder `@HumanitariansAI`, 3 result lines |
| B01 | BLUF / hesitant writer | `BrutalistHesitantWriter` | type-on with correction | 15.51 | trigger `copies` → `prunes`; seed `guests-bluf-2026-c073fbb7` |
| B02 | Anatomy | `SkillTeardownAnatomy` | reveal | 22.36 | folder tree; callout on REVIEW.md as third-party gate |
| B03 | Pipeline | `SkillTeardownPipeline` | reveal | 22.34 | 5 phase nodes; `THE VIDEO` accented |
| B04 | Mechanism 1 — Absence, not a toggle | `SkillTeardownMechanism` | reveal | 30.42 | verbatim quote on org-chart inversion |
| B05 | Mechanism 2 — GATE G | `SkillTeardownMechanism` | reveal | 26.37 | third-party-gate quote |
| B06 | Mechanism 3 — The recording | `SkillTeardownMechanism` | reveal | 36.31 | chapters-not-cuts quote |
| B07 | Mechanism 4 — Naming and voice | `SkillTeardownMechanism` | reveal | 28.95 | one-persistent-narrator quote |
| B08 | Falsifiability — outro follows channel | `SkillTeardownMechanism` | reveal | 27.50 | negative-polarity verdict; SKILL.md `## Never` quote |
| B09 | Verdict — artifact card | `ClaudeVerdictArtifact` | scale-in + reveal | 27.37 | six numbered verdict lines |
| B10 | Your Turn | `ClaudeComposerAsk` | type-on | 39.17 | greeting `Your Turn`; paste-ready dry-run prompt + 3-check rubric |
| B11 | Outro | `ClaudeTitleOutro` | hold | 3.24 | `@NikBearBrown` (OUTRO-LOCK.md); slug-seeded mascot |

Measured audio total (Kokoro `am_onyx`, no speed change): **292.72 s**
(≈ 4:53).

## Motion budget

`type-on` beats: B00, B01, B10 (composer-driven; caret + line reveals).
`reveal` beats: B02–B09 (element cascade under the skill-teardown modifier).
`hold` beat: B11 (final title card + slug-seeded mascot).

The reveal step-count (11 across 8 beats) is structurally inherent to the
skill-teardown modifier and will surface as a `motion` histogram warning under
Gate V — same warning class the sibling `fellows` teardown carries. Not a
defect.

## Scene provenance

All 12 compositions are registered in `runtime/remotion/src/Root.tsx` inside
the isolated toolkit copy. No slate resolved. Consumer index updated by
`remotion_scenes.py` at render time.

## Compile

Landscape master: `runtime/scripts/compile.py <REEL> --height 2160 --out
<REEL>/exports/landscape`. The compiler's atomic verifier writes a
`*.verified.json` next to the MP4 with real ffprobe measurements.
