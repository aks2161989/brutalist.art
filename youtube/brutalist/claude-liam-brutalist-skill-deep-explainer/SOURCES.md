# SOURCES.md — The deep-explainer Skill

## Primary source

- **`skills/make/deep-explainer/SKILL.md`** — SHA-256 `7e3ab3a9a8de25ac27aa23bd67e720b90fe41999131005e73225fde403ef9b54` (on-disk, this invocation; previous render SHA was `c268b6d698fcf117f2cb89f4f5c9efb1bed007c294ea64a5016726a4988c601e`; invocation source_sha256 `6dfb7aee6b12dc4c69c62814cadaf32e48feb76274c9072fb22a50b6e4e00a0e`)
  Read in full. Every quote in FACTCHECK.md is verbatim or near-verbatim from this
  file. Key diff from previous render: body framing shifted from "documentary-register
  vox body that leans on human-supplied static stills" to "documentary-register body
  built from executed examples, data and diagrams" — EXECUTABLE-EVIDENCE.md reference
  added in VOX BEATS section. B07 updated to reflect this new primary-mode statement.
  Repo-relative path in the public toolkit:
  https://github.com/nikbearbrown/brutalist.art/blob/main/skills/make/deep-explainer/SKILL.md

## Referenced siblings and parents

- `skills/make/ai-explainer/SKILL.md` — the parent chassis; deep-explainer inherits
  every bookend and law from here.
- `skills/make/explainer/SKILL.md` — grandparent; owns VOX LAW, MOTION.md, the
  two-axis shot system, the slot contract.
- `skills/make/nopunt/SKILL.md` — SHOW / HOLD / CARD classification and the
  teaching-arc checklist.
- `runtime/prose/teardown/PROSE.md` — Teardown register (Feynman × MKBHD).
- `skills/make/deep-explainer/reference/continuity.md`,
  `reference/shopping-list.md`,
  `reference/vox-beats.md` — the three reference files inside the skill folder,
  named in the anatomy beat (B02).

## Example beat sheets read (leads, not reused output)

- `divyank-s/2026-07-26-deep-explainer-demo/beat_sheet.json` —
  "Claude, Constitutional." (SHA-256
  `8323ffd0ff479ab66677f49261363b2520c93ec0abfe666314c34ed4de2fdbaa`) —
  copied into this workspace at `examples/8323ffd0ff47.json`. Used as a
  structural lead only (act-and-beat cadence, metadata block shape). No
  narration, media, or human signatures reused.
- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` —
  "Your Weekly Video, Handled." (SHA-256
  `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`) — read
  for HAI submission-tone reference only; no direct reuse.

## Local demo evidence

- `demo/01-skill-folder.txt` — real `ls -la` output of
  `skills/make/deep-explainer/` and `skills/make/deep-explainer/reference/` in
  the isolated toolkit at this run's revision.
- `demo/02-scenes-lookup.txt` — real output of
  `./art scenes "documentary act divider"` and
  `./art scenes --check SkillTeardownAnatomy`.
- `demo/03-skill-head.txt` — first 80 lines of the SKILL.md front-matter and
  line counts of every reference file.

## Corrections / register rewrites

- The narration compresses source lists (e.g., "Bookends, brand, laws …
  claude-explainer skill governs …") into single Teardown-register sentences.
  The SKILL's own words are only quoted where the on-screen quote block is
  used (B03, B06, B07, B08, B10, B11); those are verbatim.

## Voice, brand, license

- Voice: **Kokoro `am_onyx`** (local, free, no API). Kokoro-82M Apache-2.0.
- Persona: **Liam, in for Bear** (IN-FOR-BEAR LAW: introduced in B00, restated
  in B16).
- Channel: **@HumanitariansAI** (footer chip) — playlist adaptation. Outro
  card uses ClaudeTitleOutro which is locked to `@NikBearBrown` per
  `OUTRO-LOCK.md`; the narration reads "at Humanitarians A-I" so the channel
  identity is audible. Human reviewer decides whether to replace the outro
  card before publication.
- No paid API, no ElevenLabs, no upload, no publish — parent contract.

## Slug and outro seed

- Slug: `claude-liam-brutalist-skill-deep-explainer`
- Wagwan check: character-sum mod 10 ≠ 0 → NOT Bear's Wagwan reel.
- Hesitant-writer seed: `deep-explainer-2026-09-08` (deterministic; same seed
  same performance forever).
