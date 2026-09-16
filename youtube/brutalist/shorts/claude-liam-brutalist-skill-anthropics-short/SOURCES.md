# SOURCES.md — The anthropics Skill — Short

This Short is a whole-beat derivative of the parent film. It does not fetch or
cite any new material of its own. Its sources are:

## Primary

- Parent film: `youtube/brutalist/claude-liam-brutalist-skill-anthropics/`
  - Vertical master used as source: `vertical/exports/…-vertical.mp4` (parent, unchanged)
  - Parent master SHA-256: `73f730baa0e438bef99eddc9f5970b3fbd55afbd94967cd7948930fd5e818170`
  - Parent vertical beat sheet: `vertical/beat_sheet.json`
  - Parent-level fact-check inherited: `FACTCHECK.md` (this directory) is a
    trimmed copy that keeps only the claims covered by the retained beats.
- Skill file (verbatim quotes cited in narration): `skills/make/anthropics/SKILL.md`
  (in the isolated toolkit snapshot; see `SOURCE-SNAPSHOT.json`).

## Reused media (independent copies)

Each retained beat's portrait `media/<Bxx>.mp4` and audio `mp3/beat-<Bxx>.mp3`
were copied bit-for-bit from the parent's `vertical/` folder by
`runtime/scripts/shorts.py` (no re-render, no re-encode, no crop, no ONDA
rewire). Beat-sheet build stamps still show the parent's original render times.

## Not used, and why

- Sibling skills `git-explainer` and `ai-paper` are still absent from this
  toolkit snapshot. The Short surfaces that gap in B07 (verbatim from the
  parent narration) instead of faking a demo. This is the same rail the parent
  applies.
- No web fetch, no paid API, no image generation, no captions.

## Not this Short's claims

- The Short does not add any new factual claim to the parent's set. Anything
  visible on screen or spoken in narration is present in the parent's
  `FACTCHECK.md` under the corresponding kept beat.

## Files inherited from parent (unchanged)

`FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md` were copied by `shorts.py` and
then re-scoped in this directory to describe only the retained cut.
