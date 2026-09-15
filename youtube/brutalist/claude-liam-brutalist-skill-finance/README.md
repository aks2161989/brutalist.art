# The finance Skill — episode 12

Skill teardown of `skills/make/finance/SKILL.md` on the AI Explainer chassis,
Teardown register, Liam in for Bear, Kokoro `am_onyx`, published to the
`@HumanitariansAI` Brutalist playlist.

## Deliverables

- Landscape 4K master: [`exports/landscape/claude-liam-brutalist-skill-finance.mp4`](exports/landscape/claude-liam-brutalist-skill-finance.mp4)
  · 3840×2160 · h264 · AAC · 323.4s
- Portrait 4K companion: [`exports/vertical/claude-liam-brutalist-skill-finance-vertical.mp4`](exports/vertical/claude-liam-brutalist-skill-finance-vertical.mp4)
  · 2160×3840 · h264 · AAC · 323.4s

The portrait companion is a **full-length native 9:16** cut, not a shortened
Short and not a center-crop of the landscape master. Every beat's Remotion
composition was rewired to its `Pattern916` sibling and re-rendered.

## Twelve-beat spine

| # | Act | Scene | ⌛ |
|---|---|---|---|
| B00 | ASK | ClaudeComposerAsk | 15.0s |
| B01 | BLUF | BrutalistHesitantWriter | 14.7s |
| B02 | FRAMEWORK · anatomy | SkillTeardownAnatomy | 21.6s |
| B03 | FRAMEWORK · pipeline | SkillTeardownPipeline | 21.4s |
| B04 | MECHANISM 1 · shape logic locked | SkillTeardownMechanism | 26.7s |
| B05 | MECHANISM 2 · never retyped (EDGAR/XBRL) | SkillTeardownMechanism | 37.1s |
| B06 | MECHANISM 3 · the two audits | SkillTeardownMechanism | 36.9s |
| B07 | MECHANISM 4 · colour is not the only channel | SkillTeardownMechanism | 34.5s |
| B08 | FALSIFIABILITY · knows its own limit (banks) | SkillTeardownMechanism | 39.0s |
| B09 | VERDICT | ClaudeVerdictArtifact | 36.0s |
| B10 | YOUR TURN | ClaudeComposerAsk | 36.9s |
| B11 | OUTRO | ClaudeTitleOutro | 3.4s |

## Human review

Bear's viewing and editing is the next step. **These films are not published**;
they live in this reel folder for review. Publishing, YouTube ingest, and
transcoding checks all happen later in the human pipeline.

If a change is requested, note it in [`FEEDBACK.md`](FEEDBACK.md) and re-run the
build against the same `run_id: e9d0a40ece9b404f8f731f406e0504b9`.

## Paperwork

- [`SCRIPT.md`](SCRIPT.md) — per-beat narration
- [`SOURCES.md`](SOURCES.md) — the primary source (`SKILL.md`) and every claim's anchor
- [`FACTCHECK.md`](FACTCHECK.md) — verification of each on-screen assertion
- [`SHOTLIST.md`](SHOTLIST.md) — per-beat visual plan
- [`PROMPTS.md`](PROMPTS.md) — the B10 Your Turn prompt
- [`CHECKS-REPORT.md`](CHECKS-REPORT.md) — landscape build log, commands, outputs
- [`TYPECHECK.md`](TYPECHECK.md) — landscape typography review
- [`VISUAL-REVIEW.json`](VISUAL-REVIEW.json) — landscape ai review record
- [`vertical/CHECKS-REPORT.md`](vertical/CHECKS-REPORT.md) — portrait build log
- [`vertical/TYPECHECK.md`](vertical/TYPECHECK.md) — portrait typography review
- [`vertical/VISUAL-REVIEW.json`](vertical/VISUAL-REVIEW.json) — portrait ai review record

Landscape and portrait were reviewed independently. Both passed Gate V (frame-
level visual QC) with zero blockers and zero majors at 24 sampled frames each.

## Known limitations

- No live SEC EDGAR pull was executed. This teardown teaches the mechanism from
  the primary source per SELF-DEMO LAW's feasibility fallback (rationale in
  `SOURCES.md`).
- The legacy `scripts/type_check.py` referenced in
  `CLAUDE-CODE-VISUAL-QC-CHECK.md` is not present in this isolated toolkit;
  typography was reviewed by frame inspection instead (see `TYPECHECK.md`).
- The compile motion-histogram WARNING (`reveal 66% > 40% pantry cap`) fires
  because five MECHANISM/FALSIFIABILITY beats share the SkillTeardownMechanism
  scene family. Each rendered beat is a distinct concept illustration, not
  wallpaper. The warning is a soft guide, not a build blocker.
