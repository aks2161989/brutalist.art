# The logo-motion Skill — episode 16

Brutalist playlist · claude-liam voice · @HumanitariansAI · Kokoro `am_onyx`
narration. Skill teardown of `skills/make/logo-motion/SKILL.md` and
`skills/make/logo-motion/reference/TIMING.md`.

## Deliverables

- **Landscape 16:9 (3840×2160):**
  `exports/landscape/claude-liam-brutalist-skill-logo-motion.mp4`
  — 363.4 s, 24 fps, AAC audio. Gate V clean.
- **Portrait 9:16 (2160×3840):**
  `exports/vertical/claude-liam-brutalist-skill-logo-motion-vertical.mp4`
  — 363.4 s, 24 fps, AAC audio. Gate V clean.

Bear's viewing / editing is the next step. **These are not published.**

## Twelve beats

1. B00 — cold-open composer, `Hola, Liam` (ClaudeComposerAsk)
2. B01 — hesitant-writer BLUF, `scene → prop` (BrutalistHesitantWriter)
3. B02 — anatomy: SKILL.md, TIMING.md, trace_logo.py, LogoMotion.tsx, per-brand parts.ts, beat-sheet props (SkillTeardownAnatomy)
4. B03 — pipeline: trace parts → measure lockup → set phase map → render + look (SkillTeardownPipeline)
5. B04 — MECHANISM 1: the build is a camera move (SkillTeardownMechanism)
6. B05 — MECHANISM 2: the ghost hold IS the effect (SkillTeardownMechanism)
7. B06 — MECHANISM 3: length is a prop (SkillTeardownMechanism)
8. B07 — MECHANISM 4: the audio-first exception (SkillTeardownMechanism)
9. B08 — FALSIFIABILITY: three tells of a cheap sting (SkillTeardownMechanism)
10. B09 — VERDICT: `One composition. Every mark.` (ClaudeVerdictArtifact)
11. B10 — Your Turn: paste-ready sting-audit prompt (ClaudeComposerAsk)
12. B11 — outro: title restate + @NikBearBrown handle + mascot (ClaudeTitleOutro)

## Paperwork

Landscape: `SCRIPT.md`, `SOURCES.md`, `FACTCHECK.md`, `SHOTLIST.md`,
`PROMPTS.md`, `CHECKS-REPORT.md`, `TYPECHECK.md`, `BUILD-PROMPT.md`,
`VISUAL-REVIEW.json`.

Portrait: `vertical/SOURCES.md`, `vertical/FACTCHECK.md`,
`vertical/SHOTLIST.md`, `vertical/PROMPTS.md`, `vertical/CHECKS-REPORT.md`,
`vertical/TYPECHECK.md`, `vertical/BUILD-PROMPT.md`,
`vertical/VISUAL-REVIEW.json`.

## Remaining limitations

- Static `type_check.py` isn't shipped in this toolkit snapshot; `TYPECHECK.md`
  notes the gap and uses Gate V + frame Read as the substitute.
- Motion-histogram warning (`reveal` used in 8/12 beats) is intrinsic to the
  skill-teardown structure — five SkillTeardownMechanism beats + Anatomy +
  Pipeline + Verdict. Non-blocker.
- Portrait `SkillTeardown*916` wrappers were copied from the previous
  logo-skill workspace overlay and registered in `Root.tsx`. See
  `vertical/CHECKS-REPORT.md`.
- The reel is a textual teardown of the `LogoMotion` scene rather than a live
  new-brand demo — it uses the shipped `MEDHAVY_PARTS` trace as its citation
  base. The narration explicitly labels each citation.
