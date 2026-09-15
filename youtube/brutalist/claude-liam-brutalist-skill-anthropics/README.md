# The anthropics Skill — Brutalist playlist, Episode 05

Skill teardown of `skills/make/anthropics/SKILL.md`. AI Explainer treatment,
teardown register, `Liam, in for Bear` persona on Kokoro `am_onyx`. Channel:
`@HumanitariansAI`. No captions. Not published — Bear's viewing and
editing is the next stage.

Re-reviewed 2026-09-11 under run `3d80d6c77f6e4febae4b0621b229c773`:
source_sha256 changed (framework skills ai-explainer/SKILL.md etc. updated);
anthropics SKILL.md subject is unchanged; exports preserved verbatim.

## Deliverables

| Aspect | File | Duration | Dimensions | SHA-256 |
|---|---|---:|---:|---|
| Landscape | `exports/landscape/claude-liam-brutalist-skill-anthropics.mp4` | 228.9 s | 3840×2160 | `0a7cf8e4535532f32fdd04089490cc9244928b7b2314fd687ad2e56d721ebc00` |
| Vertical | `exports/vertical/claude-liam-brutalist-skill-anthropics-vertical.mp4` | 228.9 s | 2160×3840 | `73f730baa0e438bef99eddc9f5970b3fbd55afbd94967cd7948930fd5e818170` |

Both are native 4K renders (Remotion `--scale=2` from a 1920×1080 /
1080×1920 composition; compiler final gate at `--height 2160` and
`--height 3840` respectively). The vertical is a full-length native
portrait companion — not a shortened Short and not a cropped landscape.

## Reviewer's paperwork

Landscape (this dir):
- `VISUAL-REVIEW.json` — reviewer record, pass, `run_id` matches this
  invocation.
- `CHECKS-REPORT.md` — every runtime check and its output; motion +
  skin-lint dispositions.
- `TYPECHECK.md` — actual visual typography review vs the absent
  legacy checker.
- `SOURCES.md`, `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`,
  `SCRIPT.md` — the authored materials.
- `_qc/REPORT.md` + `_qc/frames/*.png` + `_qc/contact_sheet.png` — Gate
  V steady-state samples.

Vertical (`vertical/`):
- `VISUAL-REVIEW.json`, `CHECKS-REPORT.md`, `TYPECHECK.md`,
  `SOURCES.md`, `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`,
  `BUILD-PROMPT.md` — mirror set for the portrait aspect.
- `_qc/REPORT.md` + `_qc/frames/*.png` + `_qc/contact_sheet.png` — Gate
  V portrait samples.

## Next step

Bear's viewing and editing. `FEEDBACK.md` is where review notes land
after that pass. The reel does **not** publish, and no one has been
signed in to any account to prepare it for publication.

## Known limitations (recorded honestly)

- The `anthropics` skill dispatches to sibling skills `git-explainer`
  and `ai-paper` for its `--repo` and `--paper` modes. Neither sibling
  ships in this isolated toolkit snapshot, so no live artifact analysis
  was run. B07 (`DESIGN · TELL — Where it bites.`) names that gap on
  screen instead of faking a demonstration — the SKILL file's own
  fairness rail: *absence of code is never evidence of bad faith*.
- The reel is self-referential: the anthropics skill is explained by
  reading its `SKILL.md` in place, with verbatim quotes cited to
  `anthropics SKILL.md · <section>`. That satisfies the spine-beat
  requirement (B04 quotes the disqualifier verbatim from the file the
  viewer can go check).
- Legacy typography checker (`scripts/type_check.py`) is absent from
  this toolkit snapshot; `TYPECHECK.md` records what was visually
  reviewed instead. Not claimed as "checker passed".
- The vertical B01 layout was iterated to satisfy the 55 % canvas-fill
  law on 9:16 without cropping the landscape scene. Documented in
  `vertical/CHECKS-REPORT.md` and `vertical/TYPECHECK.md`.
