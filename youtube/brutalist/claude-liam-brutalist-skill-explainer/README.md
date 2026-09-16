# The explainer Skill — episode 9 (Brutalist playlist, @HumanitariansAI)

AI-Explainer skill-teardown reel for `skills/make/explainer`. Persona:
Liam, in for Bear. Voice: Kokoro `am_onyx` (local, free). Register: Teardown.

**Rebuilt 2026-09-11** (run_id `251584521128464e8b35431dce545cb1`): SKILL.md source
changed — VOX LAW gained a reference to `EXECUTABLE-EVIDENCE.md`. Beat B07 was
updated to cover the new content (locally reproducible code/tables/charts must be
executed and rendered, not photographed as terminal screenshots). Both landscape and
vertical recompiled; Gate V clean for both.

## Outputs (Bear's viewing — not published)

- Landscape 16:9 (3840×2160, 253.7 s):
  - `exports/landscape/claude-liam-brutalist-skill-explainer.mp4`
  - `exports/landscape/claude-liam-brutalist-skill-explainer.verified.json`
- Portrait 9:16 (2160×3840, 253.7 s) full-length companion:
  - `exports/vertical/claude-liam-brutalist-skill-explainer-vertical.mp4`
  - `exports/vertical/claude-liam-brutalist-skill-explainer-vertical.verified.json`

## Aspect-specific paperwork

- **Landscape:** `BRIEF.md`, `BUILD-PROMPT.md`, `SCRIPT.md`, `SOURCES.md`,
  `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`, `CHECKS-REPORT.md`,
  `TYPECHECK.md`, `VISUAL-REVIEW.json`.
- **Portrait:** `vertical/BUILD-PROMPT.md`, `vertical/SOURCES.md`,
  `vertical/FACTCHECK.md`, `vertical/SHOTLIST.md`, `vertical/PROMPTS.md`,
  `vertical/CHECKS-REPORT.md`, `vertical/TYPECHECK.md`,
  `vertical/VISUAL-REVIEW.json`.
- QC contact sheets: `_qc/contact_sheet.png` (landscape),
  `vertical/_qc/contact_sheet.png` (portrait).

## Next: Bear's viewing and editing

The films are ready for Bear to watch and decide about. Nothing has been
published — no YouTube upload, no Drive push, no git push. If Bear wants
edits, add them to `FEEDBACK.md` and the next autonomous pass will pick
them up.

## Known limitations (recorded honestly)

- No `slate cut` self-demo. The reel *explains* the command word; running
  it in this build would produce a different reel (a new topic reel), not
  a teardown of the skill. The B09 handoff prompt is paste-ready so a
  fellow can execute `slate cut` in their own environment.
- No `pantry.py` demo. This reel deliberately has zero pantry stills —
  VOX LAW makes zero-vox a correct outcome for a doctrine teardown whose
  evidence is text.
- No GATE T `scripts/type_check.py` run (checker not shipped in this
  toolkit snapshot). Typography was reviewed by hand-reading every
  50 %/85 % Gate V frame — see TYPECHECK.md and vertical/TYPECHECK.md.
- The compile.py motion-histogram warning ("reveal at 63 %") is a house
  pantry-cap advisory, not a failure — reveal-heavy body is inherent to
  skill-teardown Mechanism/Pipeline/Anatomy scenes (matches Ep 06/07/08).
- Two SKIN LINT warnings on portrait (B00/B10) are the known
  portrait-lint false positive — the 916 variants ARE the portrait-native
  cold-open and outro; every prior portrait episode in this playlist
  emits the same warnings.
- First-pass B01 hesitant-writer landscape frame bled the safe area at
  fontSize 190 × 5 lines (2026-09-08); repaired to fontSize 180 × 4 lines
  and re-rendered — final Gate V clean. Repair intact in this rebuild.
- Portrait build required the `BrutalistHesitantWriter` portrait-scale
  patch (`feedback_hesitant_writer_portrait_scale`) — applied to the
  isolated toolkit copy only. Live library untouched.
