# SOURCES — Brutalist Utility: pantry.py
## run_id: 1df027e6acef4cf1ad6843ed3815ffb7

## Primary source

| File | Repo path | SHA-256 (SOURCE-SNAPSHOT.json) |
|---|---|---|
| pantry.py | `runtime/scripts/pantry.py` | `5b059be171601690a436487ba1eb1d0ebefd58d4d4b0b796e971a427e201ba35` |

All code shown on screen is verbatim from this file. Line references are accurate to
the version above (146 lines total). No lines were altered, summarized, or invented.

## Secondary sources read

| File | Role |
|---|---|
| `runtime/scripts/build_safety.py` | Referenced by pantry.py (`is_source_report`, `writable_path`, `validate_project`) |
| `docs/PIPELINE-SAFETY.md` | Pipeline safety contract — source-report audio preservation |

## Example lead sources (read-only reference)

| Example | Path | SHA-256 | Used for |
|---|---|---|---|
| "Your Weekly Video, Handled." | `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` | `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22` | Beat-sheet schema reference only; no narration or scenes reused |
| "This Week, Gordy." | `yatra-r/2026-09-03-this-week-gordy/beat_sheet.json` | `7e3ea1f61c421e605e583be9b2a7b5f554aa8cadfb6e14dabaee66f471856083` | Beat-sheet schema reference only; no narration or scenes reused |

## Image/video assets

None. All beats are native Remotion compositions. No pantry/ assets, no archival
stills, no b-roll. No source photography or third-party media required.

## Registered scenes used

All scenes are from the isolated toolkit's registry. No custom scenes authored
for this episode. All are registered in `runtime/remotion/src/scenes.json` (via Root.tsx).

| Scene | Source | License |
|---|---|---|
| `ClaudeComposerAsk` | toolkit/runtime/remotion/src/scenes/ | Project license |
| `ClaudeComposerAsk916` | toolkit/runtime/remotion/src/scenes/ | Project license |
| `BrutalistHesitantWriter` | toolkit/runtime/remotion/src/scenes/ | Project license; adapted from base44 canvas toy (see component JSDoc) |
| `SkillTeardownMechanism` | toolkit/runtime/remotion/src/scenes/ | Project license |
| `SkillTeardownPipeline` | toolkit/runtime/remotion/src/scenes/ | Project license |
| `ClaudeCodeBeat` | toolkit/runtime/remotion/src/scenes/ | Project license |
| `ClaudeVerdictArtifact` | toolkit/runtime/remotion/src/scenes/ | Project license |
| `ClaudeVerdictArtifact916` | toolkit/runtime/remotion/src/scenes/ | Project license |
| `ClaudeTitleOutro` | toolkit/runtime/remotion/src/scenes/ | Project license |
| `ClaudeTitleOutro916` | toolkit/runtime/remotion/src/scenes/ | Project license |

## Corrections applied

- Narration avoids model-version-specific claims (Kokoro version, ffmpeg version).
- The episode does not claim pantry.py handles all media types — webm/mkv are accepted
  by the code but the episode focuses on the canonical mp4/png paths.
- "restored" and "upscaled" steps (Higgsfield WARMONO/NATGEO, Topaz) are noted as
  out-of-scope for pantry.py itself — pantry.py receives already-restored assets.
