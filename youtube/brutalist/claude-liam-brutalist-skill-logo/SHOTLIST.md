# SHOTLIST — The logo Skill (landscape)

12 beats. AI Explainer visual treatment. Claude palette. All Remotion scenes.

| Beat | Pattern | Purpose | Est. |
|------|---------|---------|------|
| B00 | ClaudeComposerAsk | Cold open — Liam introduces the ask; three result lines land the mental model. | 15s |
| B01 | BrutalistHesitantWriter | BLUF — corrects the "fixed brand sting" misconception to "random". lead_silence_s: 0.8. | 18s |
| B02 | SkillTeardownAnatomy | Folder tree — SKILL.md · logo.py · LogoOutro.tsx · logos/[brand]/ · public/logo-outro/. | 33s |
| B03 | SkillTeardownPipeline | Six-step flow: RESOLVE · PICK & LOCK · COPY+PAD · STAGE SVG · APPEND BEAT · RENDER + COMPILE. | 32s |
| B04 | SkillTeardownMechanism | Design decision 1 — the MP3 is the clock (`--tail` pads silence, trims silence not sound). | 29s |
| B05 | SkillTeardownMechanism | Design decision 2 — random once then locked (`shot.remotion.picked`, `--reroll`). | 27s |
| B06 | SkillTeardownMechanism | Design decision 3 — pool curation is the quality bar (medhavy: 42 drawable / 25 unique / 12 rejected). | 33s |
| B07 | SkillTeardownMechanism | Design decision 4 — drawOn is earned (only for path-only SVGs). | 29s |
| B08 | SkillTeardownMechanism | Falsifiability — no `logos/nik-bear-brown/` by design; @NikBearBrown uses `ClaudeTitleOutro`. | 33s |
| B09 | ClaudeVerdictArtifact | Six-line verdict card. | 29s |
| B10 | ClaudeComposerAsk | "Your Turn" handoff — paste-ready dry-run prompt with three-line viewer rubric. | 34s |
| B11 | ClaudeTitleOutro | Title restate — "The logo Skill." · @NikBearBrown (per OUTRO-LOCK). | 3s |

## Live demo evidence (demo/)

`demo/fixture-reel/` is a synthetic minimal beat sheet used to exercise the
skill without touching a real reel. Three real runs of `logo.py` were captured
in `demo/logo-run.log`:

1. `logo.py demo/fixture-reel hai --no-render --no-compile`
   → picked animation=`rotation`, svg=`humanitarians-logo-1.svg`,
     mp3=`humanitarians-2.mp3`, jingle=11.88s, clock=12.88s (jingle + 1.0s tail),
     aspect=16:9. New beat B01 appended with `shot.remotion.picked` set and
     `reuse_audio: mp3/beat-B01.mp3`.
2. `logo.py demo/fixture-reel hai --no-render --no-compile --reroll`
   → fresh pick: animation=`kineticGrid`, mp3=`humanitarians-6.mp3`,
     jingle=14.44s, clock=15.44s. The existing beat was replaced in place
     (same beat id), not stacked.
3. `logo.py demo/fixture-reel hai --no-render --no-compile` (no `--reroll`)
   → "reusing locked pick (use --reroll to re-randomize)" — the picked block
     was found and the same animation + svg + mp3 was reused byte-for-byte.
4. `logo.py demo/fixture-reel medhavy --no-render --no-compile --reroll`
   → fresh pick landing on `drawOn` with `medhavy-logo-24.svg` — which
     confirms that a path-only SVG earned drawOn eligibility (per the
     `extract_paths` clean-SVG check in logo.py lines 93–155).

Each of the four runs terminated with a `[logo] {bid}: ...` summary line and
also appended a matching `logo: {bid}` audit line to
`demo/fixture-reel/BUILD-LOG.md`. The four resulting beat_sheet.json snapshots
are shown by ordering in the log file.

## Frame reveals (per beat)

Every beat authored with a `shot.show` block (see beat_sheet.json). Reveals
land ON the spoken word for the composer/hesitant-writer beats; the anatomy /
pipeline / mechanism beats reveal their rows on Spring-driven staggers driven
by their scene components.
