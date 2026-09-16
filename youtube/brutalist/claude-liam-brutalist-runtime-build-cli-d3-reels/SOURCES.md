# SOURCES — Brutalist Utility: build_cli_d3_reels.py

## Primary source

- **File:** `runtime/scripts/build_cli_d3_reels.py`
- **Repo:** `https://github.com/nikbearbrown/brutalist.art`
- **Toolkit path (isolated):** `.repoloop/workspaces/claude-liam-brutalist-runtime-build-cli-d3-reels/toolkit/runtime/scripts/build_cli_d3_reels.py`
- **SHA-256 (current file):** `c37d17288291b4b7ca3ec7e06a23863f99b5c1c29c9f80554330829f459d172d`
- **Line count:** 432
- **`episode.source_sha256` in invocation:** `6d2d56ae2262b93e8d5864933bcd5c9dbd3c3b79a39a222b5a03b3a98356722f` (the supervisor's earlier snapshot; recorded verbatim in VISUAL-REVIEW.json)

## Doctrine read before scripting

| Path (relative to toolkit) | SHA-256 (from SOURCE-SNAPSHOT.json) |
|---|---|
| `skills/make/ai-explainer/SKILL.md` | `a7421d4d861b44a983a31e9fcd7451cd32312a139366e74acc2123dfdefbd3c0` |
| `skills/make/nopunt/SKILL.md` | `ef38a574fe22f2fca1dfa0774bc51681252776f8ef2bd6f2b1e52d6478cab505` |
| `runtime/prose/teardown/PROSE.md` | `6accc1a576ca9b52713abd31507f5deece6dc2612ca90967b25b661e59111786` |
| `docs/PIPELINE-SAFETY.md` | `4619f0d4702317d654cd6498cadc8c277691e4c7565920ef851dbb628aa6298d` |
| `docs/FELLOWS-SUBMISSION.md` | `7825c728f040b0f7a49bbd950a5a2bef70c8a59ff2fbe0538716c8d3381f5223` |
| `REPOLOOP-PROMPT.md` | `abf55bdc729a9c30216e4375dff0c62b4bf5af4c717ad28be69709de64d5bc97` |
| `CLAUDE.md`, `CLAUDE-BRAND.md`, `OUTRO-LOCK.md`, `CLAUDE-CODE-VISUAL-QC-CHECK.md` | read in-session |

## Reference leads (from BRIEF.md — read, not lifted)

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — "Your Weekly Video, Handled." (SHA-256 `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`) — informs the "batch of D3 reels overnight" framing.
- `uday-s/2026-08-27-weekly-fixtures-before-validators/beat_sheet.json` — "Build the Defects First" (SHA-256 `9e97abd5857ab5ab6e01230bf201f53e66ec455ef86c72208e67bce6416fd4f1`) — the fixture-first discipline informs the disposable-config approach in `demo/`.

Neither source is republished. Neither human's signature is reused. The beat sheet in this reel is authored fresh for the utility episode.

## Related utility teardowns already delivered in this playlist

- `youtube/brutalist/claude-liam-brutalist-runtime-align/` (episode 39, align.py)
- `youtube/brutalist/claude-liam-runtime-brand-variant/` (episode 40, brand_variant.py) — noted in memory; folder slug in this repo may differ

These share the 12-beat spine used here (ClaudeComposerAsk cold open · BrutalistHesitantWriter BLUF · SkillTeardownPipeline framework · five ClaudeCodeBeat mechanisms/example · ClaudeVerdictArtifact · ClaudeComposerAsk your turn · ClaudeTitleOutro).

## Disposable fixtures (this reel only)

- `demo/config.json` — one-row synthetic config; SHA-256 in `demo/config.probe.txt`.
- `demo/sim-source/00-tiny-wave.html` — a 26-line HTML with a D3 v7 sine-wave sim + one k-slider. Written for this reel. Not published as an example.
- `demo/beat_sheet_dryrun.json` — the exact 10-beat sheet `make_beat_sheet()` stamps for the fixture (captured by importing the module).
- `demo/help.txt` — `python3 build_cli_d3_reels.py -h` verbatim.
- `demo/failure-html-missing.txt` — verbatim stdout/stderr of the FAILED-1 path (HTML not found).
- `demo/RUN-LOG.txt` — human-readable walkthrough of the six evidence sections above.

## Non-sources (explicitly not used)

- No ElevenLabs, no OpenAI voice, no paid API. Kokoro `am_onyx` only.
- No YouTube upload, no publish. Output stays in the reel folder for human review.
- No `capture_sim.py` execution as part of this build (Chrome-driven HTML → mp4 is out of scope for the tutorial; the reel explains the tool's role in the pipeline, not the sim rendering).
