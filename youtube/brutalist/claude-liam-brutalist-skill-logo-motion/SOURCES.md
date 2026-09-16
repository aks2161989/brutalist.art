# SOURCES — The logo-motion Skill

## Canonical source

- `skills/make/logo-motion/SKILL.md`
  - SOURCE-SNAPSHOT SHA-256: `6852babcffd582d80719869f155869646980efb12a102dd16397eaad05099d23`
  - Supervisor episode.source_sha256: `f41852c094ab95c1ef4fb023ee5459f79668cdf643b2eb381632ec10092c4138`
  - Note: the two hashes differ because the supervisor computes over the
    isolated toolkit's live copy of the skill; SOURCE-SNAPSHOT is a snapshot
    taken at repoloop capture time. Both hashes verified present in the
    isolated toolkit.
- `skills/make/logo-motion/reference/TIMING.md` — the phase map, measured off
  two real stings; the exact contrast crossings (`5% at p=0.36, 50% at p=0.64,
  95% at p=0.80`) cited in B05 and quoted in B04/B07/B08 come from this file.
- `skills/make/logo-motion/scripts/trace_logo.py` — the raster-to-parts script
  that generates `runtime/remotion/src/logos/<name>.ts`.
- `runtime/remotion/src/scenes/LogoMotion.tsx` — the composition itself, with
  its `logoMotionSchema`, the `LOGOS` registry (currently one entry, `medhavy`),
  and the phase-driven ramps.
- `runtime/remotion/src/logos/medhavy.ts` — the currently registered mark,
  emitted by `trace_logo.py`.

## Referenced skills (per BUILD-PROMPT)

- `skills/make/ai-explainer/SKILL.md` — the AI Explainer register + the
  skill-teardown modifier the reel body follows.
- `skills/make/explainer/SKILL.md` — parent chassis.
- `skills/make/nopunt/SKILL.md` — SHOW / HOLD / CARD classification and the
  whole-sheet teaching arc.
- `runtime/prose/teardown/PROSE.md` — Teardown voice.
- `CLAUDE-BRAND.md`, `OUTRO-LOCK.md`, `CLAUDE-CODE-VISUAL-QC-CHECK.md`,
  `docs/PIPELINE-SAFETY.md`, `docs/FELLOWS-SUBMISSION.md`.

## Read-only example leads

Examples were consulted for staging cues only; no content, audio, or
signatures were reused. Preserved credit:

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — "Your Weekly
  Video, Handled." (SHA-256 `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`)
- `sainikhil-madison/2026-09-04-the-cast-that-hid-the-bug/beat_sheet.json` —
  "The Cast That Hid the Bug" (SHA-256 `15674c254cc0a11282c17826ac0db1db6adfe22e895a7e2fc8a21701c7b5b783`)

## Live-demo scaffolding

- No paid API was called. No `art keys`, no `setup --install`, no remote
  clones.
- Reel-local `demo/` contains actual command captures against the isolated
  toolkit (log entries show `trace_logo.py --help`, `LogoMotion` schema probe,
  and inspection of the shipped `logos/medhavy.ts`).
- The LogoMotion composition is not re-rendered as a standalone demo beat in
  this teardown — the phase map is illustrated via SkillTeardownMechanism
  cards (numbers verbatim from TIMING.md). The narration explicitly labels
  the citations.

## Gaps and unknowns

- `skills/make/logo-motion/reference/TIMING.md` is the only reference file
  shipped in the isolated toolkit; there is no reference/README beyond
  TIMING.md and the SKILL.md itself.
- The `LOGOS` registry currently ships with a single entry (`medhavy`). No
  second brand exists to demonstrate the "add a prop, not a scene file"
  claim by direct comparison — the claim is discussed textually.
- No shipped `scripts/type_check.py` — TYPECHECK.md distinguishes visual
  typography review (performed) from the missing static checker.
