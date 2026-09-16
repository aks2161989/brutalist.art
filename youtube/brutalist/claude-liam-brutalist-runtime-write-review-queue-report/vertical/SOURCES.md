# SOURCES — Brutalist Utility: write_review_queue_report.py

run_id: aef36acf6a354924acd1af29d9d319cf

## Primary source

| File | Repo path | SHA-256 |
|---|---|---|
| write_review_queue_report.py | runtime/scripts/write_review_queue_report.py | 8de57eb1bb0e4f1345c7a7e26ad99365969eda321c3a7fc81d897867e50d904d |

## Scene-source files added to isolated toolkit

| File | Source | Purpose |
|---|---|---|
| ClaudeTitleOutroHAI.tsx | Copied from ep54 (setup-smoke-kokoro) scene-source | @HumanitariansAI outro for 16:9 |
| ClaudeTitleOutroHAI916.tsx | Copied from ep54 (setup-smoke-kokoro) scene-source | @HumanitariansAI outro for 9:16 |
| Root.tsx (modified) | Isolated toolkit only | Registers ClaudeTitleOutroHAI, ClaudeTitleOutroHAI916, ClaudeCodeBeat916, SkillTeardownMechanism916 (added in run aef36acf) |

## Example leads consulted

| Title | Source path | SHA-256 | Use |
|---|---|---|---|
| Your Weekly Video, Handled. | rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json | 746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22 | Pattern reference for @HumanitariansAI ClaudeComposerAsk props |
| This Week, Gordy. | yatra-r/2026-09-03-this-week-gordy/beat_sheet.json | 7e3ea1f61c421e605e583be9b2a7b5f554aa8cadfb6e14dabaee66f471856083 | Pattern reference for verdict/outro structure |

## Demo fixtures

All demo fixtures are disposable synthetic data created for this episode only. They do not represent real reel data and are stored in demo/ alongside this reel for reproducibility.

- demo/audit.json — synthetic one-reel audit.json matching the script's expected schema
- demo/review-notes.json — synthetic findings for the fixture reel
- demo/fixture-reel/beat_sheet.json — minimal beat sheet with two pantry references for testing
- demo/AUDIT.md — observed output of write_review_queue_report.py on the fixture data

## Failure mode evidence

All four failure modes were tested locally with the isolated toolkit:

1. `IndexError: list index out of range` — no argument supplied
2. `FileNotFoundError: .../audit.json` — audit.json absent from output dir
3. `KeyError: '1'` — reel number in audit.json not present in review-notes.json
4. `FileNotFoundError: .../beat_sheet.json` — reel folder moved (simulated by wrong reel path)

No paid APIs, external services, or network calls were used. All evidence is locally reproducible.
