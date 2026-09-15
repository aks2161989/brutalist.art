# SOURCES — Brutalist Command: art todo — Short (9:16)

Derivative of the parent's 16:9 / vertical companion. Narration is UNCHANGED
from the parent for every retained beat (B00, B01, B02, B03, B04, B07, B08,
B09, B11). Nothing new is claimed on-screen. The sources below are the same
primary evidence the parent used; this Short does not introduce new sources.

## Primary evidence carried from the parent

| Repo path | SHA-256 (parent-verified) | Used for (retained-beat coverage) |
|---|---|---|
| `art` | `9bb77a7c84701d23ab6e73f0a4f48592f17748ffad2c7114b62687bb7f97d0e9` | Case-branch dispatch — the `todo)` line that shells `runtime/scripts/todo.py` (B00 command demo). |
| `runtime/scripts/todo.py` | `dff5d4bcbae5e188af335c892033ac030626f0a97442036c1da50a101275fb80` | Argparse surface (B03), `resolve_slot` / `build_ledger` (B02/B04), refuse-loud path (B08). |
| `runtime/scripts/beat_plan.py` | (co-located) | Method dispatch — the five lanes named in B03's `--method` chip and demonstrated in B04's five rows. |
| `skills/make/ai-explainer/SKILL.md` | `a7421d4d861b44a983a31e9fcd7451cd32312a139366e74acc2123dfdefbd3c0` | House laws — cold open (B00), BLUF (B01), ILLUSTRATE (B02/B03/B04/B07/B08), OUTRO (B11), SPARK-LINE (all illustration beats). |
| `skills/make/nopunt/SKILL.md` | `ef38a574fe22f2fca1dfa0774bc51681252776f8ef2bd6f2b1e52d6478cab505` | SHOW / HOLD / CARD classification of each retained beat. |
| `runtime/prose/teardown/PROSE.md` | `6accc1a576ca9b52713abd31507f5deece6dc2612ca90967b25b661e59111786` | Voice — Feynman × MKBHD (unchanged narration). |
| `docs/PIPELINE-SAFETY.md` | `4619f0d4702317d654cd6498cadc8c277691e4c7565920ef851dbb628aa6298d` | Refuse-loud contract — mirrored in `art todo`'s `no beat_sheet.json` behaviour (B08). |
| `OUTRO-LOCK.md` | (repo) | B11 outro contract — @NikBearBrown handle, mascot, no subline. |
| `CLAUDE-BRAND.md`, `CLAUDE-CODE-VISUAL-QC-CHECK.md` | (repo) | Palette + frame-level QC procedure applied to this Short. |

## Read-only example leads (BRIEF.md)

| Repo path (as supplied) | SHA-256 (as supplied) | Why looked at |
|---|---|---|
| `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` | `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22` | HAI-submission staging vocabulary; not carried into this Short. |
| `anjana-s/2026-08-21-ecis-explained/beat_sheet.json` | `1deb9bfc4fd4acf81ae98fccbc1fb3c1c400e370299db7bbc34d3ba527a57516` | ClaudeVerdictArtifact recap pattern reference; content authored fresh. |

Neither example's narration, media, or human signature is reused.

## Parent media reuse (independent copies, hashes verified)

Every retained beat's `media/<BID>.mp4` and `mp3/beat-<BID>.mp3` was copied
from `youtube/brutalist/claude-liam-brutalist-command-todo/vertical/` via
`runtime/scripts/shorts.py --output-dir …` (no symlinks). Per-file SHA-256
values are logged in `VISUAL-REVIEW.json`. Parent master SHA-256:
`400eb021c8011e14810b8beb1256b6bc79cb3ab79457c1189f5bd15e2eb6ed27`.

## Live demonstration fixtures

Not re-run for this Short — the B04, B07, B08 clips are the same MP4s the
parent generated from `youtube/brutalist/claude-liam-brutalist-command-todo/demo/`
(read-only for this workspace).

## Not sourced from this Short

- No fellows' beat sheets, media, human signatures, or Drive URLs are used.
- No private paths or credentials appear on screen or in narration.
- No paid API is called; no upload / publish action is taken.
- No new narration is generated; no audio is regenerated.
