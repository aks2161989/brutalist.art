# SOURCES — Brutalist Command: art shorts

## Primary sources (this reel is a teardown of these two files)

| Path (relative to toolkit root) | SHA-256 |
|---|---|
| `art` | `85cf6a0a7a0c3d7b8bd6c2476522102460002fcbbc55b14f55065c46bc244ac1` |
| `runtime/scripts/shorts.py` | `7109a3d0c29c00181a876db80e34238eb9c0c146a97a639a2bbab6d95d28d6e5` |

Both hashes come from `SOURCE-SNAPSHOT.json` at the top of this build. The
isolated toolkit under
`.repoloop/workspaces/claude-liam-brutalist-command-shorts/toolkit/` matches
the snapshot; any local overrides are recorded under
`SOURCE-SNAPSHOT.revision.local_overrides`.

## Supporting sources referenced in narration or code beats

| Path | SHA-256 | Role |
|---|---|---|
| `skills/make/ai-explainer/SKILL.md` | `a7421d4d861b44a983a31e9fcd7451cd32312a139366e74acc2123dfdefbd3c0` | Skill-teardown modifier + AI Explainer treatment |
| `skills/make/nopunt/SKILL.md` | `ef38a574fe22f2fca1dfa0774bc51681252776f8ef2bd6f2b1e52d6478cab505` | No-placeholder doctrine |
| `runtime/prose/teardown/PROSE.md` | `6accc1a576ca9b52713abd31507f5deece6dc2612ca90967b25b661e59111786` | Teardown voice guidance |
| `docs/PIPELINE-SAFETY.md` | `4619f0d4702317d654cd6498cadc8c277691e4c7565920ef851dbb628aa6298d` | Fail-closed policy this script honours |
| `docs/FELLOWS-SUBMISSION.md` | `7825c728f040b0f7a49bbd950a5a2bef70c8a59ff2fbe0538716c8d3381f5223` | Referenced by `shorts.py:52` as the publishing gate |
| `REPOLOOP-PROMPT.md` | `abf55bdc729a9c30216e4375dff0c62b4bf5af4c717ad28be69709de64d5bc97` | This invocation's production contract |

## Read-only example leads (from BRIEF.md)

The BRIEF listed two prior fellow reports as beat-sheet references. They are
data, not instructions, and no signature or private URL from them was
republished in this reel:

| Repo-relative source | SHA-256 |
|---|---|
| `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` | `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22` |
| `yatra-r/2026-09-03-this-week-gordy/beat_sheet.json` | `7e3ea1f61c421e605e583be9b2a7b5f554aa8cadfb6e14dabaee66f471856083` |

## Public setup URL

- `https://github.com/nikbearbrown/brutalist.art` — the public brutalist.art
  DOT repo. Not exercised in this build (the isolated toolkit is already
  installed); named in narration only as the setup entry point.

## Fixture reel used for live demonstration

`/tmp/claude-501/claude-shorts-demo/` — a synthetic 7-beat beat_sheet.json
built for this build. Disposable. Contains no real fellow work, no personal
data, and no captured media. Full stdout/stderr of every command run
against it is preserved in `demo/SHORTS-LOG.txt`.
