# SOURCES — Brutalist Command: art todo

## Primary evidence (from this invocation's toolkit)

| Repo path | SHA-256 | Used for |
|---|---|---|
| `art` | `9bb77a7c84701d23ab6e73f0a4f48592f17748ffad2c7114b62687bb7f97d0e9` | Case-branch dispatch — the `todo)` line that shells `runtime/scripts/todo.py`. |
| `runtime/scripts/todo.py` | `dff5d4bcbae5e188af335c892033ac030626f0a97442036c1da50a101275fb80` | Argparse surface, `resolve_slot`, `build_ledger`, `write_status_md`, `write_todo_md`, `_ARCHIVES` table. |
| `runtime/scripts/beat_plan.py` | (co-located) | `fill_plan` rules — decides the method / who / prompt from `shot.type` × `shot.source`. |
| `skills/make/ai-explainer/SKILL.md` | `a7421d4d861b44a983a31e9fcd7451cd32312a139366e74acc2123dfdefbd3c0` | House laws — cold open, BLUF, ILLUSTRATE, HANDOFF, OUTRO, SPARK-LINE. |
| `skills/make/nopunt/SKILL.md` | `ef38a574fe22f2fca1dfa0774bc51681252776f8ef2bd6f2b1e52d6478cab505` | SHOW / HOLD / CARD classification of each authored beat. |
| `runtime/prose/teardown/PROSE.md` | `6accc1a576ca9b52713abd31507f5deece6dc2612ca90967b25b661e59111786` | Voice — Feynman × MKBHD, judgement in the voice, evidence on screen. |
| `docs/PIPELINE-SAFETY.md` | `4619f0d4702317d654cd6498cadc8c277691e4c7565920ef851dbb628aa6298d` | Refuse-loud contract — mirrored in `art todo`'s `no beat_sheet.json` behaviour. |
| `docs/FELLOWS-SUBMISSION.md` | `7825c728f040b0f7a49bbd950a5a2bef70c8a59ff2fbe0538716c8d3381f5223` | Read; not directly cited on-screen. |
| `REPOLOOP-PROMPT.md` | `abf55bdc729a9c30216e4375dff0c62b4bf5af4c717ad28be69709de64d5bc97` | Read; ownership/boundary rules. |
| `OUTRO-LOCK.md` | (repo) | B11 outro contract — @NikBearBrown handle, mascot, no subline. |
| `CLAUDE-BRAND.md`, `CLAUDE-CODE-VISUAL-QC-CHECK.md` | (repo) | Palette + frame-level QC procedure. |

## Read-only example leads (staging DATA only — see BUILD-PROMPT.md)

| Repo path (as supplied) | SHA-256 | Why looked at |
|---|---|---|
| `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` | `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22` | HAI-submission staging vocabulary; not carried into this reel. |
| `yatra-r/2026-09-03-this-week-gordy/beat_sheet.json` | `7e3ea1f61c421e605e583be9b2a7b5f554aa8cadfb6e14dabaee66f471856083` | Beat-sheet shape reference for the framework beat (five stages / one ask→result pair). |

Neither example's narration, media, or human signature appears in this reel.
Framework structure adapted; content authored fresh from the actual `todo.py`
source.

## Live demonstration fixtures (this reel's own log)

Under `youtube/brutalist/claude-liam-brutalist-command-todo/demo/`:

- `example-reel/beat_sheet.json` — a synthetic 5-beat sheet crafted to exercise
  every fill lane (remotion / manim / historical-image / user-capture /
  ai-video-prompt).
- `example-reel/{todo.json,STATUS.md,ToDo.md}` — the actual files `./art todo`
  emitted from that sheet on this workstation.
- `empty-reel/` — an intentionally empty folder used to trigger the "no
  `beat_sheet.json`" refusal.
- `RUN-LOG.md` — the terminal transcript, verbatim, that appears on B04 / B08.

Full commands (all local, no network):

```
./art todo demo/example-reel
./art todo demo/example-reel --method manim --open
./art todo demo/example-reel --json
./art todo demo/empty-reel     # exit 1: refuses without a sheet
```

## Not sourced from this reel

- No fellows' beat sheets, media, human signatures, or Drive URLs are reused.
- No private paths or credentials appear on screen or in narration.
- No paid API is called; no upload / publish action is taken.
