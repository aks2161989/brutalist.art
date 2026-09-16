# SOURCES — Brutalist Command: repoloop.sh

## Primary sources (episode input; from SOURCE-SNAPSHOT.json)

| Repo-relative path | SHA-256 (captured 2026-09-10T04:28:37Z) |
|---|---|
| `repoloop.sh` | `2d10a246b7bbf5b52abecaaa668fc6f065d1ff937e8492be8054654b631477a0` |
| `runtime/scripts/repoloop.py` | `7b82920a93a41eafffd3ddf1c5e62c56d8a79b24576cbc3e06ed9c71dd3020f0` |
| `REPOLOOP-PROMPT.md` | `abf55bdc729a9c30216e4375dff0c62b4bf5af4c717ad28be69709de64d5bc97` |

## Doctrine referenced

| Path | SHA-256 |
|---|---|
| `skills/make/ai-explainer/SKILL.md` | `a7421d4d861b44a983a31e9fcd7451cd32312a139366e74acc2123dfdefbd3c0` |
| `skills/make/nopunt/SKILL.md` | `ef38a574fe22f2fca1dfa0774bc51681252776f8ef2bd6f2b1e52d6478cab505` |
| `runtime/prose/teardown/PROSE.md` | `6accc1a576ca9b52713abd31507f5deece6dc2612ca90967b25b661e59111786` |
| `docs/PIPELINE-SAFETY.md` | `4619f0d4702317d654cd6498cadc8c277691e4c7565920ef851dbb628aa6298d` |
| `docs/FELLOWS-SUBMISSION.md` | `7825c728f040b0f7a49bbd950a5a2bef70c8a59ff2fbe0538716c8d3381f5223` |
| `CLAUDE.md` (toolkit root) | read for framing rules — no code shown |
| `CLAUDE-BRAND.md` | read for palette/typography — cream/ink/terracotta |
| `OUTRO-LOCK.md` | governs B11 (hardcoded @NikBearBrown handle) |

## Read-only example leads (from BRIEF.md)

| Path | Title | SHA-256 |
|---|---|---|
| `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` | Your Weekly Video, Handled. | `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22` |
| `yatra-r/2026-09-03-this-week-gordy/beat_sheet.json` | This Week, Gordy. | `7e3ea1f61c421e605e583be9b2a7b5f554aa8cadfb6e14dabaee66f471856083` |

These examples were READ only. No signature, media, human name, or Drive
URL was reused. Reference language ("fresh Claude context per film",
"the loop drains the pending list") is my own paraphrase of the
`repoloop.py` code — verified in FACTCHECK.md line by line.

## Public references

- Toolkit repository: <https://github.com/nikbearbrown/brutalist.art>
  (public DOT repo — the URL is spoken in narration once, in B10's prompt,
  and shown on screen in the outro).

## Local demo evidence

All demo output in `demo/RUN-LOG.txt` was captured by running
`./repoloop.sh --help`, `--dry`, `--status`, `--only totally-fake-id`,
`--shorts-only --landscape-only`, and `--n -1` against the live
parent-repo checkout during this session. Each command is read-only
(no queue mutation, no worker spawn, no network). The `--status` block
shows this very reel as the active `building` item, `id=command-repoloop`,
`run_id=cd46b905ecb54c35b0f71b2db5a04ab1` — matching `metadata.run_id`
here and `episode.run_id` in BUILD-PROMPT.md.

## Deterministic authoring seeds

- BrutalistHesitantWriter B01 seed: `repoloop-b01` (locked; identical
  performance every render).
- ClaudeTitleOutro mascot: slug-seeded from
  `claude-liam-brutalist-command-repoloop` per OUTRO-LOCK.md.
- No other stochastic scenes.

## No paid or upstream API used

- Voice: Kokoro `am_onyx` (local model at
  `runtime/models/kokoro/kokoro-v1.0.onnx`).
- Renderer: Remotion via `runtime/scripts/remotion_scenes.py`, using
  `chrome-headless-shell` locally installed at
  `~/node_modules/.remotion/chrome-headless-shell/mac-arm64/…`.
- No ElevenLabs, no OpenAI, no Anthropic API calls, no Higgsfield calls,
  no Smithsonian/pantry fetches.

## No fellow signatures reused

Rohan and Yatra's example beat sheets shaped my `output` list phrasing
and `spark_line` tone. Their names, media, human review records and
Drive URLs are NOT republished here.
