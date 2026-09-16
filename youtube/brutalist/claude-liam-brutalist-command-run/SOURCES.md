# SOURCES — Brutalist Command: art run

Primary sources for every on-screen claim. All lines quoted below can be
read verbatim from the isolated toolkit at
`.repoloop/workspaces/claude-liam-brutalist-command-run/toolkit/` on
2026-09-09.

## Command sources (per SOURCE-SNAPSHOT.json)

| Path | SHA-256 | Role |
|---|---|---|
| `art` | 85cf6a0a7a0c3d7b8bd6c2476522102460002fcbbc55b14f55065c46bc244ac1 | dispatcher; `run)` case at art:99-101 (re-verified 2026-09-12; `--list` grew to 20 skills, moving the case from 78-80) |
| `runtime/scripts/run.sh` | da4ec56878188c132575f889f84203a90bcc05aacc300982cd03da5b0b725b16 | the workflow the case wraps |

`episode.source_sha256` from THIS INVOCATION: `f9c007cae04ca87ddb005388bf8c0835e220369e6f2d2377dd54f02e1f6c65c2`
(digest over both files as recorded by the supervisor; updated 2026-09-12 for run_id `df4ab48ebf354eecb12e6a7d2316a270`).

## Doctrine sources

| Path | SHA-256 | Why cited |
|---|---|---|
| `skills/make/ai-explainer/SKILL.md` | a7421d4d861b44a983a31e9fcd7451cd32312a139366e74acc2123dfdefbd3c0 | AI-Explainer chassis + skill-teardown structure |
| `skills/make/nopunt/SKILL.md` | ef38a574fe22f2fca1dfa0774bc51681252776f8ef2bd6f2b1e52d6478cab505 | PROOF GATE, SHOW/HOLD/CARD |
| `runtime/prose/teardown/PROSE.md` | 6accc1a576ca9b52713abd31507f5deece6dc2612ca90967b25b661e59111786 | Teardown register cues |
| `docs/PIPELINE-SAFETY.md` | 4619f0d4702317d654cd6498cadc8c277691e4c7565920ef851dbb628aa6298d | pipeline safety context |
| `docs/FELLOWS-SUBMISSION.md` | 7825c728f040b0f7a49bbd950a5a2bef70c8a59ff2fbe0538716c8d3381f5223 | two-video weekly cadence context |
| `REPOLOOP-PROMPT.md` | abf55bdc729a9c30216e4375dff0c62b4bf5af4c717ad28be69709de64d5bc97 | supervisor charter (episode context) |
| `CLAUDE.md` | (workspace snapshot) | entry-point rules table: `art run <reel>` = review cut |
| `OUTRO-LOCK.md` | (workspace snapshot) | outro card contract; `@NikBearBrown` handle locked |

## Read-only example leads (per BRIEF.md)

| Path | SHA-256 | What was studied |
|---|---|---|
| `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` | 746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22 | "Your Weekly Video, Handled." — HAI submission pipeline visuals for pacing reference only. |
| `sainikhil-madison/2026-08-28-what-else-did-you-run/beat_sheet.json` | 1d871a3753aa83f1bc2819c92962fffbd0b13a2504ae547722a2d01d354535ea | "What Else Did You Run?" — ClaudeComposerAsk / ClaudeVerdictArtifact / ScaleComparison / DivergentFates / BinaryBranch / ClaudeScienceChipGrid usage patterns. |

Studied for staging and pattern-selection; no copied narration; no reused human
signature; results are not this run's outputs. Local copies live at
`.repoloop/workspaces/claude-liam-brutalist-command-run/examples/`.

## Live observation log (all local, no paid calls)

Two demo captures live in `demo/RUN-LOG.txt`:

1. `./art run /tmp/claude-501/art-run-demo` on a beat sheet with **no**
   `FACTCHECK.md/SHOTLIST.md/PROMPTS.md` → **Gate F failure**, verbatim.
2. The exact same reel after touching the three paperwork files → moves past
   Gate F into Gate L / Gate SHAPE and reports its next honest state.

The messages shown in B05, B08 and elsewhere are cut and pasted from that
`RUN-LOG.txt`. Nothing is invented or paraphrased.

## Adaptations applied (DOUBLE-CHECK LAW)

- OUTRO-LOCK contract preserved: title restate + hardcoded `@NikBearBrown`
  handle. The playlist targets `@HumanitariansAI`; the composer folder chip
  reads `@HumanitariansAI` on every ASK beat, but the outro handle stays as
  locked. Flagged in `README.md` for the human reviewer.
- No caption / SRT / burned-in transcript.
- No paid TTS or paid video API calls. Kokoro `am_onyx` for every beat.
- No `setup --install`, `art keys` or remote-clone demos — the workspace
  toolkit was cloned by the supervisor before this invocation started.

## Related memories consulted

- `feedback_isolated_toolkit_node_modules_shadow` — shadow `node_modules` so
  webpack can rotate `.cache/` inside the workspace.
- `feedback_chrome_sandbox` — `open-browser.js` darwin patch + direct `node` CLI invocation (2026-09-12 revision; shell wrapper no longer works in sandbox).
- `feedback_channel_title_portrait_bleed` — omit `metadata.channel_title`
  from portrait beat sheet.
- `feedback_remotion_prop_names` — exact schema fields for
  `ClaudeComposerAsk`, `ClaudeCodeBeat`, `ClaudeVerdictArtifact`,
  `ClaudeTitleOutro`.
- `feedback_hesitant_writer_portrait_bluf_recipe` — portrait BLUF fill via
  `lineSpacing` 2.4–2.7 rather than fontSize alone.
- `feedback_gate_v_underfill` — FILL_MIN 0.55 requires multi-line layouts.
