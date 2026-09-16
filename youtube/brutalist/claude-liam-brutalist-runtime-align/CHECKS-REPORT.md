# CHECKS-REPORT — landscape (3840×2160)

Episode: `claude-liam-brutalist-runtime-align`
Run: `d295e86979c344a7b9b979f8bdf6d514`
Source: `runtime/scripts/align.py` (snapshot SHA-256 `1a028fbdb1e705ca5005394f40ceda11267d1c2f631fb339ef46c64edc259111`; file SHA-256 `b2ee07253e474cbce79820dc90199929570880e012062e5b8c4980ca31bc3058`, 183 lines)
Master: `exports/landscape/claude-liam-brutalist-runtime-align.mp4` (SHA-256 `1e1106847b5092837a314b29aa8a15b8a2f3158d737e8b96c7d32d3cf83c13ac`)

## Runtime gates that ran

| gate | invoker | input | outcome |
|------|---------|-------|---------|
| scene-render fit | `runtime/scripts/remotion_scenes.py` | `beat_sheet.json` | 12/12 beats VIDEO |
| clip assembly | `runtime/scripts/compile.py` | `beat_sheet.json` + `media/*.mp4` + `mp3/*.mp3` | 12/12 clips concatenated |
| Gate V (final_frame_check) | `runtime/qc/final_frame_check.py` | candidate MP4 + `_work/resolved-sheet.json` | 24 frames sampled · BLOCKER 0 · MAJOR 0 · **PASS** (re-run this invocation) |
| atomic master write | `runtime/scripts/compile.py` | verified candidate | landscape master written, `.verified.json` receipt beside it |
| ffprobe on master | `ffprobe -v error` | master MP4 | width=3840, height=2160, duration=224.4s, 24 fps, aac audio track present |
| audio decode | `ffprobe -show_streams -select_streams a` | master MP4 | single AAC stream, 224.375s, matches per-beat mp3 concat |
| motion histogram | compile.py summary | 12 beats | code-cascade 6/12 (50%) — over ~40% pantry cap, WARNING only (no gate) |

## Static / structural checks

- `beat_sheet.json` metadata matches the AI Explainer skill's teardown contract: `playlist: "Brutalist"`, `voice_kokoro: "am_onyx"`, `captions: false`, `channel: "@HumanitariansAI"`, `persona: "Liam (in for Bear)"`, `in_for_bear: true`, `aspect_ratio: "16:9"`.
- Cold open (B00) uses `ClaudeComposerAsk`; second beat (B01) uses `BrutalistHesitantWriter`; second-last beat (B10) uses `ClaudeComposerAsk` with `greeting: "Your Turn"`; outro (B11) uses `ClaudeTitleOutro`. All required Cold-Open / BLUF / Your-Turn / Outro laws satisfied.
- Every beat carries `audio_file: mp3/beat-B*.mp3` and `render_duration_s` inside 1 frame of `actual_duration_s`.

## Visual review (AI, this run)

`VISUAL-REVIEW.json` at the reel root captures frame evidence for this invocation (`run_id d295e86979c344a7b9b979f8bdf6d514`). Video SHA unchanged from the previous successful build; source snapshot updated (align.py re-read and confirmed still accurate for all beat code excerpts — line numbers 49-66, 69-101, 104-109, 157-165 verified against the 183-line current file). Gate V re-run: BLOCKER 0, MAJOR 0. Frames extracted from the existing master at 4s, 24s, 60s, 110s, 165s, 223s and visually inspected — cold-open composer, BLUF settled, CLI help cascade, align_words code, drift-case words.json, and title outro. No edge-bleed, no unresolved slates, no subtitle track, no unwanted captions. Outro shows the reel title and hardcoded `@NikBearBrown` handle (per OUTRO-LOCK.md); composer folder chip carries `@HumanitariansAI` — flagged for human reviewer.

## Gaps and honest caveats

- Public docs reference some checkers that are not shipped in this isolated toolkit revision:
  - `runtime/scripts/type_check.py` — not present. Static typography validation was not run as a separate gate. The Remotion components used (`ClaudeComposerAsk`, `BrutalistHesitantWriter`, `ClaudeCodeBeat`, `SkillTeardownMechanism`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`) render through registered scene compositions with typed prop schemas; TYPECHECK.md distinguishes this actual visual typography review from the absent legacy checker.
  - `runtime/qc/kerning_check.py` — not present. Kerning was inspected visually in the extracted frames.
- Motion histogram warns that `code-cascade` covers 6/12 body beats (50%) — over the ~40% pantry cap suggested in MOTION.md. Because this episode is a teardown of a single 182-line Python file, the code-heavy body is intentional; called out honestly rather than papered over.
- Skin lint warnings printed by `compile.py`: B00 uses `ClaudeComposerAsk` and B11 uses `ClaudeTitleOutro`, which is exactly what COLD OPEN LAW and OUTRO LAW require — the compile lint text appears to be looking for the wrong pattern name. Not a defect in this episode.

## Human review pending

This is an AI frame-review record satisfying the "current AI frame-review record" gate; it is NOT a human sign-off. Bear's viewing/editing is the next step, per README.md.
