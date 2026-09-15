# SHOTLIST — The screen-clean Skill — Short

Six retained beats, all native portrait 2160×3840, palette Claude (cream
`#FAF9F5` / ink `#2F2A26` / terracotta `#D97757`), one accent per beat. No
burned-in captions. Compiler treats measured audio as the master clock;
motion cues are timed as fractions of each beat's audio duration.

## B00 · ClaudeComposerAsk916 — Bonjour, Liam (16.0 s)
- 0.02 composer card fades in on cream.
- 0.15 greeting `Bonjour, Liam` types above the composer.
- 0.35 command types the ask about the `screen-clean` skill.
- 0.65 send button arms terracotta.
- 0.78 three result lines fade in one at a time.

## B01 · BrutalistHesitantWriter916 — auto-blurs → flags (18.6 s)
- 0.8 s lead silence before serif text lands.
- 0.05 typed line 1: `The screen-clean skill`.
- 0.20 typed line 2: `auto-blurs your desktop`.
- 0.55 `auto-blurs` flashes terracotta (about-to-delete).
- 0.62 `auto-blurs` deletes; `flags` types in.
- 0.78 line 3 lands: `into a safe reel beat.` closing on `The proof is the sheet.`
- Trigger words: `auto-blurs` → `flags` (comma-token contract; no trailing punct).

## B03 · SkillTeardownPipeline916 — Five passes. One review artifact. (26.6 s)
- 0.05 eyebrow `SKILL · PIPELINE` lands.
- 0.12 title `Five passes. One review artifact.` lands.
- 0.20 input node `screen recording · 16:10 · Zoom / Teams / Meet / QuickTime`.
- 0.35 phase nodes reveal — `PROBE` lit terracotta.
- 0.85 output node `cleaned 1920×1080 beat · contact sheet · numbers report`.
- Spark line: `One gate. Four flags. A sheet.`

## B07 · SkillTeardownMechanism916 — Flag. Never decide. (32.1 s)
- 0.05 eyebrow `MECHANISM · ACT 4 · PASS 4` lands.
- 0.12 heading `Flag. Never decide.` fades in.
- 0.30 body enumerates every incidental surface + wait-for-a-human doctrine.
- 0.60 verbatim quote block from SKILL.md lands (`Source: screen-clean SKILL.md · Pass 4`).
- 0.85 verdict pill `JUDGMENT, NOT ARITHMETIC`.
- Spark line: `Not arithmetic. Judgment.`

## B09 · ClaudeVerdictArtifact916 — A gate. A crop. A flag. A sheet. (30.8 s)
- 0.05 artifact card scales in.
- 0.15 heading `A gate. A crop. A flag. A sheet.` lands.
- 0.25 six numbered verdict lines reveal one at a time.

## B11 · ClaudeTitleOutro916 — sign-off (4.0 s)
- 0.05 cream ground with pixel-mascot corner.
- 0.15 title `The screen-clean Skill.` lands, terracotta period.
- 0.55 handle `@NikBearBrown` fades in.
- 0.80 seeded mascot animation plays under the handle (slug seed
  `claude-liam-brutalist-skill-screen-clean`).

## Cuts, joins, motion

- All six beats are the parent's native 2160×3840 renders, copied
  independently (no symlinks, no re-render, no crop). ONDA CHECK not
  triggered because sources were already `-916` compositions.
- Silence at joins measured with `ffmpeg silencedetect` at `-40 dB` /
  `d=0.5`: every join is a natural 0.5–0.8 s breath. No dead-air clip and no
  chopped speech.

## Dropped shots (in the parent long only)

- **B02** SkillTeardownAnatomy916 — on-disk anatomy of `screen-clean/`.
- **B04** SkillTeardownMechanism916 · ACT 1 — shared-preprocessor rationale.
- **B05** SkillTeardownMechanism916 · ACT 2 · PASS 1 — audio-gate demo.
- **B06** SkillTeardownMechanism916 · ACT 3 · PASS 2 — A/B/C aspect table.
- **B08** SkillTeardownMechanism916 · FALSIFIABILITY — four-frame contact sheet.
- **B10** ClaudeComposerAsk916 · Your Turn — paste-ready dry-run prompt.
