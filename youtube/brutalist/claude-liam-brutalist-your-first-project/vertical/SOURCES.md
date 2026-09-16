# SOURCES.md — Your First Brutalist Project

The reel's structural claims are all local — the pipeline that built it IS the
subject. External inputs are limited to two read-only example leads and the
supplied episode sources.

## Episode sources (from `SOURCE-SNAPSHOT.json`, verified)

| Path | SHA-256 |
|---|---|
| `README.md` | ca2eacdb6366bca0ae09d48ea0855da46aa003691a4f08a2f06b4b83e1b86588 |
| `art` | 9bb77a7c84701d23ab6e73f0a4f48592f17748ffad2c7114b62687bb7f97d0e9 |
| `setup` | 75040062dfcb20d0437a5a358abc516ed6e4b1e4e9020aaac926e1b9d5b2208d |
| `skills/make/ai-explainer/SKILL.md` | a7421d4d861b44a983a31e9fcd7451cd32312a139366e74acc2123dfdefbd3c0 |
| `skills/make/nopunt/SKILL.md` | ef38a574fe22f2fca1dfa0774bc51681252776f8ef2bd6f2b1e52d6478cab505 |
| `runtime/prose/teardown/PROSE.md` | 6accc1a576ca9b52713abd31507f5deece6dc2612ca90967b25b661e59111786 |
| `docs/PIPELINE-SAFETY.md` | 4619f0d4702317d654cd6498cadc8c277691e4c7565920ef851dbb628aa6298d |
| `docs/FELLOWS-SUBMISSION.md` | 7825c728f040b0f7a49bbd950a5a2bef70c8a59ff2fbe0538716c8d3381f5223 |
| `REPOLOOP-PROMPT.md` | abf55bdc729a9c30216e4375dff0c62b4bf5af4c717ad28be69709de64d5bc97 |

All eight files were read in this session. The visible on-screen artifacts
(seven-step "what claude reads" card, two-lane submission card, 9:16 sheet
rules) are paraphrased directly from these files — nothing is invented.

## Read-only example leads (structure only — never republished)

| Path | SHA-256 | Used how |
|---|---|---|
| `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` | 746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22 | Referenced for its 13-beat "seven steps the agent handles / three yours" structure. This reel deliberately re-uses NEITHER its Google Drive URL nor Rohan's name/signature. Local copy: `examples/746409a8715e.json`. |
| `uday-s/2026-08-27-weekly-fixtures-before-validators/beat_sheet.json` | 9e97abd5857ab5ab6e01230bf201f53e66ec455ef86c72208e67bce6416fd4f1 | Referenced for its ASK → EVIDENCE → REVISION → RESULT rhythm and its handoff prompt shape. Local copy: `examples/9e97abd5857a.json`. |

Neither example's video, mp3, or human signature is reused. This reel's
narration, palette prompts, and cards are its own.

## Scene sources (isolated toolkit)

| Composition | Origin | This reel's use |
|---|---|---|
| `ClaudeComposerAsk` | `runtime/remotion/src/scenes/ClaudeComposerAsk.tsx` (shipped) | Cold open (B00), ASK beats (B03, B06), handoff (B10). |
| `BrutalistHesitantWriter` | `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx` (shipped) | BLUF (B01). |
| `ClaudeCodeBeat` | `runtime/remotion/src/scenes/ClaudeCodeBeat.tsx` (shipped) | FRAMEWORK (B02), REBUILD-diff (B07). |
| `ClaudeVerdictArtifact` | `runtime/remotion/src/scenes/ClaudeVerdictArtifact.tsx` (shipped) | Numbered-list body beats: B04, B05, B08, B09. |
| `ClaudeTitleOutroHAI` | **NEW** — `runtime/remotion/src/scenes/ClaudeTitleOutroHAI.tsx` | Isolated-toolkit variant of `ClaudeTitleOutro` that accepts `handle` as a prop and defaults to `@HumanitariansAI`. Registered in `Root.tsx`. The shipped `ClaudeTitleOutro` (hardcoded `@NikBearBrown` per `OUTRO-LOCK.md`) is untouched. |
| `ClaudeTitleOutroHAI916` | **NEW** — sibling for portrait 9:16. | Portrait outro in the vertical reel. |

## Voice source

- Kokoro-ONNX model, `am_onyx` voice. Model files at
  `KOKORO_MODEL=/Users/bear/…/runtime/models/kokoro/kokoro-v1.0.onnx` and
  `KOKORO_VOICES=…/voices-v1.0.bin`. Both files are on-disk local artifacts,
  325 MB / 28 MB — no network call was made to synthesize this reel's audio.
