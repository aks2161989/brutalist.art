# CHECKS-REPORT — vertical (2160×3840)

Episode: `claude-liam-brutalist-runtime-align`
Run: `d295e86979c344a7b9b979f8bdf6d514`
Source: `runtime/scripts/align.py` (snapshot SHA-256 `1a028fbdb1e705ca5005394f40ceda11267d1c2f631fb339ef46c64edc259111`; file SHA-256 `b2ee07253e474cbce79820dc90199929570880e012062e5b8c4980ca31bc3058`, 183 lines)
Master: `exports/vertical/claude-liam-brutalist-runtime-align-vertical.mp4` (SHA-256 `bd94b7252670e9c1ff526cd9daa0a4a6f64dca7c72ace6f491a56e1f089d6500`)

## Runtime gates that ran

| gate | invoker | input | outcome |
|------|---------|-------|---------|
| scene-render fit | `runtime/scripts/remotion_scenes.py` | `vertical/beat_sheet.json` | 12/12 beats VIDEO, portrait-native compositions (…916 variants) |
| clip assembly | `runtime/scripts/compile.py` | `vertical/beat_sheet.json` + portrait `media/*.mp4` + `mp3/*.mp3` | 12/12 clips concatenated |
| Gate V (final_frame_check) | `runtime/qc/final_frame_check.py` | candidate MP4 + `_work/resolved-sheet.json` | 24 frames sampled · BLOCKER 0 · MAJOR 0 · **PASS** (re-run this invocation) |
| atomic master write | `runtime/scripts/compile.py` | verified candidate | portrait master written, `.verified.json` receipt beside it |
| ffprobe on master | `ffprobe -v error` | master MP4 | width=2160, height=3840, duration=224.4s, 24 fps, aac audio track present |
| audio decode | `ffprobe -show_streams -select_streams a` | master MP4 | single AAC stream, ~224.4s, matches per-beat mp3 concat |
| motion histogram | compile.py summary | 12 beats | code-cascade 6/12 (50%) — over ~40% pantry cap, WARNING only |

## Fixes made this run to reach Gate V

The previous attempt for this aspect failed Gate V with two portrait-specific defects. Both fixed in this run:

- **B01 (BrutalistHesitantWriter916)** — was 2 lines (`align.py / transcribes audio.` → `align.py / times words.`) at fontSize 150 / lineSpacing 2.6, which measured only 21% content-bbox coverage of `SAFE916` (min 55%). Rewritten to 5 short lines at fontSize 150 / lineSpacing 2.25 with two comma-separated single-token triggers (`transcribes`, `guesses`) and matched replacements (`times`, `knows`). Final settled text reads `align dot py / times / the audio then / knows the / spoken words.` — coherent, on-message, and each replacement token is unique in the source string (per the trigger-collision rule). Gate V now measures 60%+ coverage on both 50% and 85% samples.
- **B10 (ClaudeComposerAsk916)** — the "Your Turn" ask command was ~700 characters, which overflowed the portrait composer's minHeight and bled ink past SAFE916's right/bottom edges. Trimmed to the paste-ready core (~260 chars) that still names the exact command, the deliverables per beat, and the "don't bump `--model`" trap. The narration remains verbatim (audio unchanged) — only the visual composer text was shortened.

## Static / structural checks

- `vertical/beat_sheet.json` metadata: `aspect_ratio: "9:16"`, slug `claude-liam-brutalist-runtime-align-vertical`, `reformat: "full-length; native portrait graphics; preserve source framing"`, `derived_from: "claude-liam-brutalist-runtime-align"`. All beats use portrait-native scene compositions (`ClaudeComposerAsk916`, `BrutalistHesitantWriter916`, `SkillTeardownMechanism916`, `ClaudeCodeBeat916`, `ClaudeVerdictArtifact916`, `ClaudeTitleOutro916`). Nothing is a landscape scene cropped after the fact.
- Cold open (B00), BLUF (B01), Your-Turn (B10), Outro (B11) laws satisfied by the …916 counterparts.
- Every beat carries `audio_file: mp3/beat-B*.mp3` and `render_duration_s` inside 1 frame of `actual_duration_s`.

## Visual review (AI, this run)

`vertical/VISUAL-REVIEW.json` updated for this invocation (`run_id d295e86979c344a7b9b979f8bdf6d514`). Video SHA unchanged. Gate V re-run: BLOCKER 0, MAJOR 0. Fresh frames extracted at 4s, 24s, 110s, 223s and visually inspected: ClaudeComposerAsk916 cold open fills portrait card cleanly; BrutalistHesitantWriter916 BLUF 5-line settled text covers safe area; ClaudeCodeBeat916 align_words() code fits within SAFE916; ClaudeTitleOutro916 outro shows title and @NikBearBrown handle with decorative top/bottom rules. No edge-bleed, no unresolved slates, no subtitle track, no captions.

## Gaps and honest caveats

- `type_check.py` and `reference/type-spec.md` still absent in the isolated toolkit — same as landscape. `TYPECHECK.md` distinguishes actual visual typography review from the missing legacy checker.
- `SkillTeardownPipeline` (B02 short-cut validator) reported blocked in `metadata.short_validation` — that's a Shorts-only note; the full-length portrait uses `SkillTeardownMechanism916` and renders cleanly.
- Motion histogram warning about `code-cascade` 6/12 body beats — same acknowledged tradeoff as landscape.

## Human review pending

This is an AI frame-review record. Human review by Bear is next, per the reel-root `README.md`.
