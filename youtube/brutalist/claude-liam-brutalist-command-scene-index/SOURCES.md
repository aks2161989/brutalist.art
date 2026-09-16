# SOURCES — Brutalist Command: art scene-index

Primary evidence for every on-screen claim. All sources are files in
the isolated toolkit copy at
`.repoloop/workspaces/claude-liam-brutalist-command-scene-index/toolkit`
and were captured 2026-09-09.

## Primary sources (this reel's subject)

| Path (repo-relative) | SHA-256 (SOURCE-SNAPSHOT.json) | Role |
|---|---|---|
| `art` | 9bb77a7c84701d23ab6e73f0a4f48592f17748ffad2c7114b62687bb7f97d0e9 | the dispatcher; case at art:71-74 |
| `runtime/scripts/build_scene_index.py` | 82b9f52b24d85c823c71d50e19603133dc71980da24d0b3668ad6323d891de5b | the tool the wrapper runs |
| `runtime/remotion/src/Root.tsx` | (workspace-local; not in snapshot — patched here to add `ClaudeCodeBeat916`) | the file the tool reads |
| `runtime/remotion/src/scenes.json` | (build product) | the file the tool writes |
| `SCENE-DOC-TODO.md` | (build product) | the second file the tool writes (via `--todo`) |

Episode source SHA-256 (this invocation): `84ddd4414379ad5440ff553369bfc74c57dbd6dea7951d0c32a683bfcf594cb3`.

## Doctrine and lineage

- `skills/make/ai-explainer/SKILL.md` (SHA-256 `a7421d4d861b44a983a31e9fcd7451cd32312a139366e74acc2123dfdefbd3c0`)
  — bookends: cold open on `ClaudeComposerAsk`, hesitant writer for
  BLUF, ILLUSTRATE LAW governing the middle, HANDOFF LAW for Your Turn,
  OUTRO LAW for the title restate.
- `skills/make/nopunt/SKILL.md` (SHA-256 `ef38a574fe22f2fca1dfa0774bc51681252776f8ef2bd6f2b1e52d6478cab505`)
  — SHOW/HOLD/CARD classification; every beat here is SHOW.
- `runtime/prose/teardown/PROSE.md` (SHA-256 `6accc1a576ca9b52713abd31507f5deece6dc2612ca90967b25b661e59111786`)
  — the Teardown register (Feynman × MKBHD) Liam narrates in.
- `docs/PIPELINE-SAFETY.md` (SHA-256 `4619f0d4702317d654cd6498cadc8c277691e4c7565920ef851dbb628aa6298d`)
  — GATE F/V doctrine, atomic verification, ready receipt.
- `docs/FELLOWS-SUBMISSION.md` (SHA-256 `7825c728f040b0f7a49bbd950a5a2bef70c8a59ff2fbe0538716c8d3381f5223`)
  — the "two videos a week, four files" workflow explained on-screen
  in adjacent episodes; not directly quoted here.
- `REPOLOOP-PROMPT.md` (SHA-256 `abf55bdc729a9c30216e4375dff0c62b4bf5af4c717ad28be69709de64d5bc97`)
  — the unattended-production contract this build honours.

## Sibling command episodes (structure reference only, not republication)

Both are read-only leads per BRIEF.md; nothing was copied or replayed.

| Path (repo-relative) | SHA-256 | Note |
|---|---|---|
| `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` | 746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22 | example command beat sheet, staging reference |
| `yatra-r/2026-09-03-this-week-gordy/beat_sheet.json` | 7e3ea1f61c421e605e583be9b2a7b5f554aa8cadfb6e14dabaee66f471856083 | example command beat sheet, staging reference |
| `youtube/brutalist/claude-liam-brutalist-command-scenes/beat_sheet.json` | (workspace baseline) | closest sibling — the `./art scenes` search episode |
| `youtube/brutalist/claude-liam-brutalist-command-icons/beat_sheet.json` | (workspace baseline) | icons episode; similar 12-beat command layout |

## Corrections applied vs the source

None. The reel paraphrases the tool's own header and dispatcher case
in Teardown register; verbatim quotes appear on the code cards, each
cited to `build_scene_index.py` in FACTCHECK.md.

## No external / paid sources

- Voice: Kokoro `am_onyx` (local, Apache-2.0, no account).
- Rendering: Remotion + Chrome-for-testing (local).
- No API calls, no cloud storage, no upload, no publication.
- No fellow signatures or private paths reproduced.
