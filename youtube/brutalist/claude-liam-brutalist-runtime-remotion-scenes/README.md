# Brutalist Utility: remotion_scenes.py

**Channel:** @HumanitariansAI · **Playlist:** Brutalist · **Episode:** 53
**Persona:** Liam (in for Bear) · **Voice:** Kokoro am_onyx
**Run ID:** `5886489043694263be44af6a46ffbcaf`

Teaches Humanitarians AI fellows how `remotion_scenes.py` works: its entry-ticket gate (`shot.remotion.pattern`), four-step pipeline (detect → render → extend → stamp), failure-isolation mode, and the `--list` / `--force` / `--only` flags. Companion to Ep 29 (`art run`) and Ep 43 (`fill_slates.py`).

## Exports

| Aspect | Path | Dimensions | Duration | Gate V |
|--------|------|-----------|----------|--------|
| 16:9 landscape | `exports/landscape/claude-liam-brutalist-runtime-remotion-scenes.mp4` | 3840×2160 | 212.0 s | 0/0 ✓ |
| 9:16 portrait | `vertical/exports/claude-liam-brutalist-runtime-remotion-scenes.mp4` | 2160×3840 | 212.0 s | 0/0 ✓ |

## Beat layout (12 beats)

| ID | Act | Scene | Duration |
|----|-----|-------|----------|
| B00 | COLD OPEN | ClaudeComposerAsk | 16.3 s |
| B01 | BLUF | BrutalistHesitantWriter | 12.8 s |
| B02 | FRAMEWORK | SkillTeardownMechanism | 21.8 s |
| B03 | THE ENTRY TICKET | ClaudeCodeBeat | 13.9 s |
| B04 | THE RENDER CORE | ClaudeCodeBeat | 22.9 s |
| B05 | MATCHING THE AUDIO CLOCK | ClaudeCodeBeat | 21.0 s |
| B06 | THREE GATES | FormBCard | 17.8 s |
| B07 | DEMO: --list | ClaudeCodeBeat | 21.8 s |
| B08 | FAILURE MODE | SkillTeardownMechanism | 23.0 s |
| B09 | VERDICT | ClaudeVerdictArtifact | 17.5 s |
| B10 | HANDOFF — YOUR TURN | ClaudeComposerAsk | 17.4 s |
| B11 | OUTRO | ClaudeTitleOutro | 6.0 s |

## QC documents

- `CHECKS-REPORT.md` — landscape build log and gate evidence
- `TYPECHECK.md` — landscape typography review
- `VISUAL-REVIEW.json` — landscape frame hashes (run_id verified)
- `vertical/CHECKS-REPORT.md` — portrait build log (includes bug-fix history)
- `vertical/TYPECHECK.md` — portrait typography review
- `vertical/VISUAL-REVIEW.json` — portrait frame hashes

## Adaptation notes

- B11 outro handle `@NikBearBrown` is locked per OUTRO-LOCK.md. Update `ClaudeTitleOutro` props before publication on a different channel.
- `channel_title` is NOT set in the portrait beat sheet metadata (would bleed past portrait safe.b).
- All code beat props quote `remotion_scenes.py` source directly — verify against the source before channel updates that may change the utility.

## Notable bugs fixed this run

1. **compile.py aspect ratio** — read `aspect_ratio` field; beat sheets use `aspect`. Defaulted to 16:9 for portrait, producing 6826×3840 landscape crops. Fixed: `meta.get("aspect_ratio") or meta.get("aspect") or "16:9"`.
2. **Ink anchor placement** — ClaudeCodeBeat916 and SkillTeardownMechanism916 placed anchors at 4% (outside SAFE916 5% boundary). Fixed to 5.5%.
3. **ClaudeVerdictArtifact916 underfill** — no ink anchors; centered card alone < 55% height coverage. Added anchors at 5.5%.
