# 07. The deep-explainer Skill

Playlist: **Brutalist** · Channel: **@HumanitariansAI** · Persona:
**Liam, in for Bear** (Kokoro `am_onyx`) · Register: **Teardown**.
Compile run ID: `9a0276f36c7f460da489b867130af37b` (2026-09-11 update).
Verification run ID: `1acd0dfc2b404516baa047d32365869e` (2026-09-12 #3, resumed after usage-limit pause; prior run_ids 3675182de1… and af2c6d0b…).

Both files below are Bear-viewing candidates, not published cuts. Bear's
viewing / editing / upload is the next step; nothing here has been
pushed to Git or uploaded to YouTube.

## What changed in this update (2026-09-11)

`skills/make/deep-explainer/SKILL.md` updated between the 2026-09-08 render
and this run. Key doctrinal shift: the skill's body is now described as
"documentary-register body built from executed examples, data and diagrams"
rather than primarily a VOX body with pantry stills. `EXECUTABLE-EVIDENCE.md`
added as a reference in the VOX BEATS section.

**B07 updated** — narration adds "The updated doctrine names the preferred mode:
executed examples, data, and diagrams." On-screen heading changed to "Executed
examples first." and verdict pill to "EXECUTED EXAMPLES FIRST." Audio regenerated
(17.13s, was 14.89s). Total runtime increased by ~2.2s.

## Rendered deliverables

- **Landscape 16:9, 3840×2160, 216.2 s**
  `exports/landscape/claude-liam-brutalist-skill-deep-explainer.mp4`
  Gate V clean (30 frames, 0 BLOCKER, 0 MAJOR). See
  [CHECKS-REPORT.md](CHECKS-REPORT.md), [_qc/REPORT.md](_qc/REPORT.md),
  [VISUAL-REVIEW.json](VISUAL-REVIEW.json).

- **Vertical 9:16, 2160×3840, 216.2 s (native portrait, not cropped)**
  `exports/vertical/claude-liam-brutalist-skill-deep-explainer-vertical.mp4`
  Gate V clean (30 frames, 0 BLOCKER, 0 MAJOR). See
  [vertical/CHECKS-REPORT.md](vertical/CHECKS-REPORT.md),
  [vertical/VISUAL-REVIEW.json](vertical/VISUAL-REVIEW.json).

Verified receipts:
`exports/landscape/claude-liam-brutalist-skill-deep-explainer.verified.json`
and
`exports/vertical/claude-liam-brutalist-skill-deep-explainer-vertical.verified.json`
written by compile.py alongside each master.

## Structure

15 beats (B00–B04, B06–B08, B10–B16). The two authored `FormACard` act
dividers (B05 "Act II" and B09 "Act III") were dropped at the original
build because a minimalist center-typography CARD fills only ~3% of the
safe area and fails Gate V's FILL_MIN ≥ 0.55 canvas-fill law. Narration
bridges the acts without an interstitial.

## Known limitations (for the human reviewer)

- `SkillTeardownPipeline916` B04: "Title outro" node visually overlaps
  the footer note in portrait — Gate V's bbox check does not flag it.
  Cosmetic; out of scope for this episode.
- Motion histogram lint: `illustrate` carries 7/15 beats (46%), above
  the ~40% cap. Structural — six of the seven are SkillTeardownMechanism
  beats because the film's subject IS the skill's mechanisms.
- `runtime/scripts/type_check.py` and `reference/type-spec.md` absent
  from this isolated toolkit — see [TYPECHECK.md](TYPECHECK.md) for
  the honest gap note and what ran instead.
- Outro card: `@NikBearBrown` is hardcoded per OUTRO-LOCK.md; narration
  reads "at Humanitarians A-I" so the channel is audible. The on-screen
  handle mismatch is flagged for human review before publication.

## Next step

Bear watches both mp4s. Feedback in [FEEDBACK.md](FEEDBACK.md) as usual;
the supervisor picks up any requested revisions.
