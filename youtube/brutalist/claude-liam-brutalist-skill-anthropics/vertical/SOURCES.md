# SOURCES.md — The anthropics Skill

*Brutalist playlist · Episode 05 · Skill teardown.*

## Primary source (verbatim on-screen quotes from this file)

- **`skills/make/anthropics/SKILL.md`** — the full skill file, 142 lines,
  read in full for this reel.
  - `SOURCE-SNAPSHOT.json` records SHA-256 `79f196f3dc46afecd42d6a34be4bf04aef9aaafbceae812df19aab855f8cdfd5`.
  - The supervisor's `episode.source_sha256` recorded in `BUILD-PROMPT.md`
    is `9189aa89c3995fc581d9f0ef1fa0b4a4913cd253e6fbfb791b4085f86c890755`.
  - The `demo/01_sha_and_lines.sh` output at build time matches the
    `79f19…` snapshot value (see `demo/01_sha_and_lines.out`). The
    `9189aa…` value carried by the supervisor payload is preserved
    verbatim in this reel's `VISUAL-REVIEW.json` `source_sha256` field
    per the BUILD-PROMPT contract; both fingerprints are recorded
    honestly here so the divergence is visible to the reviewer.
  - Repo-relative path in the public toolkit:
    <https://github.com/nikbearbrown/brutalist.art/blob/main/skills/make/anthropics/SKILL.md>
    (the isolated snapshot may drift from the public tip; the SHAs above
    are authoritative for what this reel narrates).

Quotes shown on screen and read verbatim by the narration:

| Beat | Quote (verbatim) | Source line |
|---|---|---|
| B04 | "If the episode could be made by reading the docs, it is not this series." | SKILL.md §"anthropics — the beat" (bold block) |
| B05 | "a feature that exists but ships off tells a different story than the paragraph describing it" | SKILL.md §"`--repo` behavioural probes" · DEFAULTS bullet |
| B06 | "Another perspective, not a correction." | SKILL.md §"The register" (heading of the first paragraph) |
| B07 | "Never generate an image that poses as evidence of a fact." | SKILL.md §"The generation-honesty law" |

Each on-screen citation reads *"Source: Anthropic-style skill file, `anthropics/SKILL.md`"* per the skill-teardown modifier's VERBATIM QUOTE LAW.

## Read-only example leads (BRIEF.md)

These beat sheets were read for staging inspiration; nothing from them was
copied verbatim, no old recordings were reused, and no signatures were
adopted.

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — SHA-256
  `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`.
  (Repo-relative in the fellows tree.)
- `yatra-r/2026-08-30-one-tool-a-week-brandy/beat_sheet.json` — SHA-256
  `e219593a27eaf6d68b43d3c9c89243cb90fd1e9dab7fd1199abc000d757af38e`.

## Supporting toolkit files read

For the skill-teardown modifier's "read the WHOLE skill first" contract, the
following referenced files were also read (SHAs from `SOURCE-SNAPSHOT.json`):

| File | SHA-256 |
|---|---|
| `skills/make/ai-explainer/SKILL.md` | `a7421d4d861b44a983a31e9fcd7451cd32312a139366e74acc2123dfdefbd3c0` |
| `skills/make/nopunt/SKILL.md` | `ef38a574fe22f2fca1dfa0774bc51681252776f8ef2bd6f2b1e52d6478cab505` |
| `runtime/prose/teardown/PROSE.md` | `6accc1a576ca9b52713abd31507f5deece6dc2612ca90967b25b661e59111786` |
| `docs/PIPELINE-SAFETY.md` | `4619f0d4702317d654cd6498cadc8c277691e4c7565920ef851dbb628aa6298d` |
| `docs/FELLOWS-SUBMISSION.md` | `7825c728f040b0f7a49bbd950a5a2bef70c8a59ff2fbe0538716c8d3381f5223` |

Local commit at build time: `ba2d0e0` (from `SOURCE-SNAPSHOT.json`).

## Scenes used and their sources

| Composition | File | Notes |
|---|---|---|
| `ClaudeComposerAsk` | `runtime/remotion/src/scenes/ClaudeComposerAsk.tsx` | Cold open + Your Turn. |
| `BrutalistHesitantWriter` | `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx` | Beat 2 BLUF; seeded `anthropics-bluf-2026`. |
| `SkillTeardownAnatomy` | `runtime/remotion/src/scenes/SkillTeardownAnatomy.tsx` | B02 folder view. |
| `SkillTeardownPipeline` | `runtime/remotion/src/scenes/SkillTeardownPipeline.tsx` | B03 mode router. |
| `SkillTeardownMechanism` | `runtime/remotion/src/scenes/SkillTeardownMechanism.tsx` | B04/B05/B06/B07 mechanism acts. |
| `ClaudeVerdictArtifact` | `runtime/remotion/src/scenes/ClaudeVerdictArtifact.tsx` | B08 verdict card. |
| `AntOutro` / `AntOutro916` | `scene-source/runtime/remotion/src/Anthropics.tsx` (isolated toolkit only) | Native custom outro that hardcodes `@HumanitariansAI` so the shipped `ClaudeTitleOutro`'s `@NikBearBrown` lock is respected. The live library was not modified. |

## Not used, and why

- `git-explainer` and `ai-paper` sibling skills — referenced by the SKILL
  file's `--repo` and `--paper` modes, but not present in this isolated
  toolkit snapshot. The reel names the dependency (B07) rather than
  fabricating a probe.
- Real Anthropic repositories, papers, or capability comparisons — not run
  in this reel. The skill's DEMO would require pointing it at real target
  artefacts and running its siblings; that is out of scope for a
  self-referential teardown of the SKILL file itself. Recorded honestly
  under "Known limitations" in the README.
