# The duration-planner Skill — episode 8 (Brutalist playlist, @HumanitariansAI)

AI-Explainer skill-teardown reel for `skills/make/duration-planner`. Persona:
Liam, in for Bear. Voice: Kokoro `am_onyx` (local, free). Register: Teardown.

## Outputs (Bear's viewing — not published)

- Landscape 16:9 (3840×2160, 214.1 s):
  - `exports/landscape/claude-liam-brutalist-skill-duration-planner.mp4`
  - `exports/landscape/claude-liam-brutalist-skill-duration-planner.verified.json`
- Portrait 9:16 (2160×3840, 214.1 s) full-length companion:
  - `exports/vertical/claude-liam-brutalist-skill-duration-planner-vertical.mp4`
  - `exports/vertical/claude-liam-brutalist-skill-duration-planner-vertical.verified.json`

## Aspect-specific paperwork

- **Landscape:** `BRIEF.md`, `BUILD-PROMPT.md`, `SCRIPT.md`, `SOURCES.md`,
  `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`, `CHECKS-REPORT.md`,
  `TYPECHECK.md`, `VISUAL-REVIEW.json`.
- **Portrait:** `vertical/BUILD-PROMPT.md`, `vertical/SOURCES.md`,
  `vertical/FACTCHECK.md`, `vertical/SHOTLIST.md`, `vertical/PROMPTS.md`,
  `vertical/CHECKS-REPORT.md`, `vertical/TYPECHECK.md`, `vertical/VISUAL-REVIEW.json`.
- QC contact sheets: `_qc/contact_sheet.png` (landscape), `vertical/_qc/contact_sheet.png` (portrait).

## Build history

- **2026-09-08** — Original build (run_id `7385b5694ce94579bc3e260bb879c388`):
  11/11 beats, Gate V clean, both aspects delivered.
- **2026-09-11** — Re-verified (run_id `d046c67744a74bd5ad40572da67b71da`):
  Source SKILL.md unchanged, no feedback applied; both MP4s byte-identical to
  prior build. VISUAL-REVIEW.json updated to this invocation's run_id.

## Next: Bear's viewing and editing

The films are ready for Bear to watch and decide about. Nothing has been
published — no YouTube upload, no Drive push, no git push. If Bear wants
edits, add them to `FEEDBACK.md` and the next autonomous pass will pick
them up.

## Known limitations (recorded honestly)

- No `pace_check.py` self-demo (the reel *explains* the skill's advisory
  script; running it on the teardown itself would be circular). B03 pipeline
  diagram illustrates the flow the script implements; SOURCES.md is
  explicit that this is a rebuild, not a screenshot.
- No GATE T `scripts/type_check.py` run (checker not shipped in this
  toolkit snapshot). Typography was reviewed by hand-reading every 50 %/85 %
  Gate V frame — see TYPECHECK.md.
- The compile.py motion-histogram warning ("reveal at 63 %") is a house
  pantry-cap advisory, not a failure — reveal-heavy body is inherent to
  skill-teardown Mechanism/Pipeline/Anatomy scenes.
- Two SKIN LINT warnings on portrait (B00/B10) are the known portrait-lint
  false positive — the 916 variants ARE the portrait-native cold-open and
  outro; anthropics portrait shows the same warning.
