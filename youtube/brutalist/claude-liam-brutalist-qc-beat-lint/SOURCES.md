# Sources — Brutalist Utility: beat_lint.py

## Primary source

| File | Repo path | SHA-256 (snapshot) |
|---|---|---|
| beat_lint.py | `runtime/qc/beat_lint.py` | d65a938569a0aa73f6300dca7bd5e492584bbd25305cc6969bfa43fa311e1af5 |
| brand_labels.json | `runtime/qc/brand_labels.json` | (read live from isolated toolkit) |

The source SHA-256 recorded in the episode manifest is `3c912722969545db552479db79867f8ca3e2756c5cb4664d5ec391f34cdf6057` (from the invocation). The snapshot records the file hash at the time the isolated toolkit was created (2026-09-15).

## Example references

These beat sheets were read as leads for staging; their original files were not modified. No recordings, renders, Drive URLs, or human signatures from these sources appear in this episode.

| Example | Repo path | SHA-256 |
|---|---|---|
| "Your Weekly Video, Handled." | `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` | 746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22 |
| "This Week, Gordy." | `yatra-r/2026-09-03-this-week-gordy/beat_sheet.json` | 7e3ea1f61c421e605e583be9b2a7b5f554aa8cadfb6e14dabaee66f471856083 |

## Demo artifacts

Fixture files and their observed outputs are in `demo/`. All fixtures are synthetic — no real fellow data, no real reel content.

| Demo file | Purpose |
|---|---|
| `demo/fixture_clean.json` | Beat sheet that passes lint cleanly (exit 0) |
| `demo/fixture_defect.json` | Beat sheet with two RULE 3 defects (exit 2) |
| `demo/demo_output.txt` | Observed CLI output from both runs (recorded 2026-09-15) |

## Skills and docs read

- `skills/make/ai-explainer/SKILL.md`
- `skills/make/nopunt/SKILL.md`
- `skills/make/explainer/SKILL.md` (parent chassis)
- `runtime/prose/teardown/PROSE.md`
- `CLAUDE-BRAND.md`
- `OUTRO-LOCK.md`
- `CLAUDE-CODE-VISUAL-QC-CHECK.md`
- `docs/PIPELINE-SAFETY.md`
- `docs/FELLOWS-SUBMISSION.md`

## Corrections and limitations

- `beat_lint.py` RULE 7 branding check only applies to channels listed in `brand_labels.json`. The `claude-liam` persona is not listed (by design — it's a default persona, not a fixed series channel). This is correctly represented in the episode.
- The tool does NOT check whether illustration patterns are meaningful, only that they exist and are not in the text-card set. This limitation is stated in B08 (verdict beat).
- No screen recordings or external URLs are used. All demonstrations use synthetic fixtures.
