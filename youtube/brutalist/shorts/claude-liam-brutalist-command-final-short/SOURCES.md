# SOURCES — Brutalist Command: art final — Short (ep 33)

This Short is a whole-beat cut of the finished native portrait companion; it
introduces no new source material. Every retained beat inherits its provenance
from the parent's `SOURCES.md`.

## Parent

| File | SHA-256 | Role |
|---|---|---|
| `youtube/brutalist/claude-liam-brutalist-command-final/vertical/beat_sheet.json` | `a8492a0366542e9bf20b7afbac501831232bab989f29dc10834101cd49ccf631` | Parent native portrait beat sheet; source of every retained beat's narration, prop set and native 2160×3840 render. |
| `youtube/brutalist/claude-liam-brutalist-command-final/exports/vertical/claude-liam-brutalist-command-final-vertical.mp4` | `8d130d003f5406bc1c37085ffb347e24842f5cc891337a5a42dd2961572dbd3e` | Approved parent master (referenced by BUILD-PROMPT `parent_master_sha256`); this Short is a subset, not a re-encode of that container. |

## Primary sources for the retained beats (from the parent's SOURCES.md)

| File | SHA-256 | Role |
|---|---|---|
| `art` | `9bb77a7c84701d23ab6e73f0a4f48592f17748ffad2c7114b62687bb7f97d0e9` | Top-level dispatcher; case `final)` at art:90-95 is named in B09's recap line 1. |
| `runtime/scripts/compile.py` | `047e9fa6d0944f54c284ed16df8b4d847f62737a0e263a0f4bf0bad2b11f446c` | Source of B06 (`compile.py:805-827`) and B07 (`compile.py:829-834`). |

## Retained beats

- B00 `ClaudeComposerAsk916` — cold open, ask, three-line output card.
- B01 `BrutalistHesitantWriter916` — BLUF misconception (`renders once` → `verifies twice`).
- B06 `ClaudeCodeBeat916` — atomic candidate write pattern (compile.py:805-827).
- B07 `ClaudeCodeBeat916` — verified.json receipt shape (compile.py:829-834).
- B09 `ClaudeVerdictArtifact916` — six-line recap.
- B11 `ClaudeTitleOutro916` — locked outro card, `@NikBearBrown`, slug-seeded mascot.

## Dropped beats

- B02 (dispatcher case), B03 (argparse), B04 (final_preflight body), B05
  (happy-path worked example), B08 (empty-FACTCHECK failure/recovery), B10
  (Your Turn). Their claims remain fact-checked in the parent's `FACTCHECK.md`.

## Human signatures

Inherited from the parent — none required (`kind: command`; no fellows or
professor-notes gate). The Short's `verified.json.status = "ready"` remains
a machine claim about the automated checks; human review of this Short is
pending in `FEEDBACK.md`.

## What is NOT a source

- No new AI-generated media. No screenshots. No captions. No paid API. No
  network calls. No uploads.
