# CHECKS-REPORT — vertical (2160×3840)

Episode: `claude-liam-brutalist-runtime-brand-variant`
Run: `2105289f3f3846c2870c68ad6e4c57dc`
Source: `runtime/scripts/brand_variant.py` (invocation source SHA-256 `1ab627266e10e1ed8a0e4e704f38180f261b647013dd27eeac51767b61381560`; working-toolkit SHA-256 `ced0d3f79d98e5d9b18e005679474b64f8fe3b897f5f6fef6b5b3ee2ed02756e`)
Master: `exports/vertical/claude-liam-brutalist-runtime-brand-variant-vertical.mp4` (SHA-256 `030d552849d7d9f9836d7fbf048a3bdee6280b816fe675b395c8f6c7e98f5117`)

## What changed from the previous vertical build

Same source-triggered corrections as the landscape: B04, B07, B08 code props updated for current single-line output format; B07 narration updated to cover `copy_build_scripts()` and segment loop (audio 30.51s from 26.62s). See landscape CHECKS-REPORT.md for the full diff.

## Runtime gates that ran

| gate | invoker | input | outcome |
|------|---------|-------|---------|
| audio (B07 only) | shared from landscape | B07 updated narration | 30.51s · am_onyx · $0.00 |
| scene-render fit | `remotion_scenes.py --force` | B04/B07/B08 vertical (ClaudeCodeBeat916) | 3 beats re-rendered VIDEO |
| clip assembly | `compile.py --height 3840 --sheet beat_sheet.json` | 12 clips | 12/12 concatenated |
| Gate V | `runtime/qc/final_frame_check.py` | vertical master + beat_sheet | 24 frames · BLOCKER 0 · MAJOR 0 · **PASS** |
| atomic master write | `compile.py` | verified candidate | vertical master written, `.verified.json` receipt beside it |
| ffprobe on master | `ffprobe -v error` | vertical MP4 | width=2160, height=3840, duration=223.1s, h264, AAC audio present |

## Static / structural checks

- `beat_sheet.json` metadata: `aspect_ratio: "9:16"`, `fit: "pad"`, `slug: "claude-liam-brutalist-runtime-brand-variant-vertical"` — vertical contract satisfied.
- All 12 beats use native portrait compositions: ClaudeComposerAsk916 (B00, B10), BrutalistHesitantWriter916 (B01), SkillTeardownMechanism916 (B02), ClaudeCodeBeat916 (B03-B08), ClaudeVerdictArtifact916 (B09), ClaudeTitleOutro916 (B11).
- Compile skin lint for B00/B11 (palette=claude vs 916 pattern names) is expected for native portrait — noted in prior CHECKS-REPORT and memory.
- `metadata.channel_title` removed from vertical beat_sheet to prevent compile-time PIL overlay bleed past SAFE916.b — consistent with prior build.

## Visual review (AI, this run)

`VISUAL-REVIEW.json` in `vertical/` captures current frame evidence with real SHA-256s. Contact sheet opened with the image-capable Read tool. Cold open shows ClaudeComposerAsk916 (Yassou, Liam, composer in portrait). BLUF (B01 BrutalistHesitantWriter916) shows five-line text with "narration" in terracotta before correction to "metadata" — ink bbox stable past 55% at 50% per portrait scale patch. B02 shows SkillTeardownMechanism916 scaffold. Code beats (B03-B08 ClaudeCodeBeat916) show corrected single-line output, updated main() body, updated refusal cases. Verdict, Your Turn, and outro clean.

## Gaps and honest caveats

- Motion histogram: code-cascade 50% — same as landscape; intentional for teardown film.
- `type_check.py` and `kerning_check.py` not present in this isolated toolkit revision. Visual inspection via contact sheet.
- Outro `@NikBearBrown` hardcoded per OUTRO-LOCK.md — flagged for human reviewer.

## Human review pending

This is an AI frame-review record. Bear's viewing/editing is the next step, per `README.md`.
