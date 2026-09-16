# Sources (Short cut)

## Primary source (what the reel tears down)

- `skills/make/fashionista/SKILL.md`
  - SOURCE-SNAPSHOT SHA-256 (captured 2026-09-08T13:52:38): `22614f443c156cf903878e5ff0781ba1d8b34170e0622bfee962b58f7d7bf12b`
  - Supervisor's authoritative `episode.source_sha256`:
    `0f3c1370180aa7829a7cf993c808cf40b66f38aec44689fae3d19b9dc0e42609`
    (combined hash of all tracked source files as of run
    `5112069ad63347e9ab02657ed099ad9d`; see SOURCE-SNAPSHOT.json.
    Previous run source_sha256 was
    `5bfdc4f743d275cd7eae2b47d090d1450b1f038e196ca9df0efe5105269aa4ca`
    — the change was in REPOLOOP-SHORTS-PROMPT.md; fashionista SKILL.md
    and all media files are bit-identical to the previous build).

## Derivative source (this Short's parent)

- `youtube/brutalist/claude-liam-brutalist-skill-fashionista/` — full 16:9 long
  and its `vertical/` full-length portrait companion. The Short reuses eight
  of the twelve portrait beats unchanged (see `CUT-PLAN.json`); dropped beats
  are B02/B03/B08/B10.
- Parent portrait master SHA-256:
  `efe5ebdf0ae8c8ee6cabcedfaaef1e6b6482069cdbbf2709a2f4b3155146fd1f`.

## Doctrine consulted (unchanged from the parent reel)

- `skills/make/ai-explainer/SKILL.md` — the parent chassis and skill-teardown
  modifier (cold-open ask → hesitant writer → body → verdict card → outro).
- `skills/make/explainer/SKILL.md` — the register grounding.
- `skills/make/nopunt/SKILL.md` — the PROOF GATE classification and
  “render only, no publishing” contract.
- `REPOLOOP-SHORTS-PROMPT.md` — the strictly-under-180-seconds Shorts rule
  and cut-first-then-rewrite editorial rubric.

## Registered scenes used in this Short

Portrait wrappers (all live in the isolated toolkit's
`runtime/remotion/src/Root.tsx`):

- `ClaudeComposerAsk916` — B00.
- `BrutalistHesitantWriter916` — B01.
- `SkillTeardownMechanism916` — B04, B05, B06, B07.
- `ClaudeVerdictArtifact916` — B09.
- `ClaudeTitleOutro916` — B11.

## Read-only example leads

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — “Your Weekly
  Video, Handled.” (SHA-256 `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`).
- `sanjana-rao/08-24-2026-playlist-architecture-as-product-strategy/playlist-architecture-short/beat_sheet.json` —
  “Playlist Architecture — Short” (SHA-256 `787621776bcd8810d8719a61f577f3589707bbf59151655fcbbdd10555b318a0`).

Neither example is a fashionista source and neither is presented as this run's
output. Credit is preserved via original repo-relative paths.

## What the Short does NOT source from

- No stock footage, no photography, no AI image or video model output.
- No YouTube upload, no publishing action, no paid API call.
- The captions track is deliberately absent (`metadata.captions: false`).
