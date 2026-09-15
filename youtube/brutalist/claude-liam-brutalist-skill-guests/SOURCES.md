# SOURCES — The guests Skill (claude-liam-brutalist-skill-guests)

## Primary source (doctrine)

- `skills/make/guests/SKILL.md` — the whole skill file, read verbatim.
  Snapshot SHA-256: `dc9db967b2b68d1da40f7e2135679105196d48aedb72faa84040ced60f838218`
  (SOURCE-SNAPSHOT.json). Supervisor's own `episode.source_sha256`:
  `c2de13f94ed1ee511d5932c1e9fea29d4a17d556afb51f1d0f0c4f148be6cbb6` — both
  reference the same file inside the isolated toolkit copy at capture time.
  All verbatim on-screen quotes and the FACTCHECK trace are against this file.

## Doctrine consulted (this run only)

Read in full from the isolated toolkit before authoring:

| File | Snapshot SHA-256 | Why |
|---|---|---|
| `skills/make/ai-explainer/SKILL.md` | `a7421d4d861b44a983a31e9fcd7451cd32312a139366e74acc2123dfdefbd3c0` | parent chassis + `skill-teardown` modifier (bookends, ILLUSTRATE LAW, SELF-DEMO LAW's feasibility fallback, HANDOFF LAW, VERBATIM QUOTE LAW) |
| `skills/make/nopunt/SKILL.md` | `ef38a574fe22f2fca1dfa0774bc51681252776f8ef2bd6f2b1e52d6478cab505` | no-slate discipline (every beat filled or the reel does not ship) |
| `runtime/prose/teardown/PROSE.md` | `6accc1a576ca9b52713abd31507f5deece6dc2612ca90967b25b661e59111786` | register (Feynman × MKBHD teardown warmth) |
| `docs/PIPELINE-SAFETY.md` | `4619f0d4702317d654cd6498cadc8c277691e4c7565920ef851dbb628aa6298d` | GATE F (paperwork) + atomic verification law |
| `docs/FELLOWS-SUBMISSION.md` | `7825c728f040b0f7a49bbd950a5a2bef70c8a59ff2fbe0538716c8d3381f5223` | sibling-skill submission workflow (context for the guests / fellows contrast) |
| `REPOLOOP-PROMPT.md` | `abf55bdc729a9c30216e4375dff0c62b4bf5af4c717ad28be69709de64d5bc97` | the unattended-production owner brief |
| `skills/make/fellows/SKILL.md` | (baseline, not in snapshot) | Explicitly named as `guests`'s sibling in the source; consulted to describe the beat GATE G replaces |
| `OUTRO-LOCK.md` | (baseline) | `@NikBearBrown` handle-lock on ClaudeTitleOutro |
| `CLAUDE-BRAND.md` | (baseline) | palette + typography fidelity for `palette: claude` |
| `CLAUDE-CODE-VISUAL-QC-CHECK.md` | (baseline) | Gate V rubric (FILL_MIN, contrast, no clipping) |

## Read-only example leads (structural only, credited)

Read for structural patterns; never re-used, never re-published, never
misattributed. These come from `../example-sources.json` in the isolated
workspace.

| Path | SHA-256 | Title | Use here |
|---|---|---|---|
| `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` | `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22` | *Your Weekly Video, Handled.* | Structural reference for a HAI-channel reel with a composer cold open and a series-outro contract. |
| `yatra-r/2026-08-30-one-tool-a-week-brandy/beat_sheet.json` | `e219593a27eaf6d68b43d3c9c89243cb90fd1e9dab7fd1199abc000d757af38e` | *One Tool a Week.* | Structural reference for a verdict-artifact card at the end of a claude-liam explainer. |

Neither example's script text, transcript, results, or human signatures are
carried into this reel. No fellow is impersonated. No board member's name,
work, or standing is claimed.

## Scene-library availability log (this run)

Every landscape composition and its portrait `*916` wrapper is REGISTERED and
searchable through the isolated toolkit's Root.tsx + `scenes.json` index.
Confirmed with `runtime/scripts/scene_search.py --check <Name>`:

- `ClaudeComposerAsk` — RENDERABLE 16:9
- `BrutalistHesitantWriter` — RENDERABLE 16:9
- `SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` — RENDERABLE 16:9
- `ClaudeVerdictArtifact` — RENDERABLE 16:9
- `ClaudeTitleOutro` — RENDERABLE 16:9
- `ClaudeComposerAsk916` / `BrutalistHesitantWriter916` / `SkillTeardownAnatomy916` / `SkillTeardownPipeline916` / `SkillTeardownMechanism916` / `ClaudeVerdictArtifact916` / `ClaudeTitleOutro916` — RENDERABLE 9:16

No PUNT. No SLATE. Every beat resolved to a registered composition.

## Reused scene changes credited to the sibling episode

The following files were copied verbatim from the sibling
`claude-liam-brutalist-skill-fellows` episode's `scene-source/` directory
into this isolated toolkit — they are that episode's original work, not this
run's:

- `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx` (portrait-aware scale patch)
- `runtime/remotion/src/scenes/SkillTeardownAnatomy916.tsx` (portrait wrapper)
- `runtime/remotion/src/scenes/SkillTeardownPipeline916.tsx` (portrait wrapper)
- `runtime/remotion/src/scenes/SkillTeardownMechanism916.tsx` (portrait wrapper)
- `runtime/remotion/src/Root.tsx` (patched to register the three `*916` compositions)

They are recorded in `scene-source-manifest.json` and mirrored under
`scene-source/`. The live public toolkit is not modified.

## Infrastructure (render side-effects, not scenes)

- `runtime/remotion/node_modules` — the symlink in the isolated toolkit is
  repointed to a writable copy at `$TMPDIR/nmroot/node_modules`. Package tree
  is identical to the public toolkit's; only writability changed so webpack's
  cache can be maintained (the sandbox denies unlink on files carrying
  `com.apple.provenance`). Live public `runtime/remotion/node_modules` is
  untouched.
- Chrome launched via `ART_CHROME=/tmp/claude-501/rw/chrome-wrap.sh` +
  `ART_CHROME_MODE=chrome-for-testing` (single-process + in-process-gpu
  headless-shell) per memory `feedback_chrome_sandbox`. Both are documented
  Remotion hooks, not a sandbox bypass.
