# CHECKS-REPORT — landscape (3840×2160)

Episode: `claude-liam-brutalist-runtime-brand-variant`
Run: `2105289f3f3846c2870c68ad6e4c57dc`
Source: `runtime/scripts/brand_variant.py` (invocation source SHA-256 `1ab627266e10e1ed8a0e4e704f38180f261b647013dd27eeac51767b61381560`; working-toolkit copy SHA-256 `ced0d3f79d98e5d9b18e005679474b64f8fe3b897f5f6fef6b5b3ee2ed02756e` per `SOURCE-SNAPSHOT.json`)
Master: `exports/landscape/claude-liam-brutalist-runtime-brand-variant.mp4` (SHA-256 `bdd2734e347886af13c93f11a651d25228fde504c80bf6492d7768c6bc4656f4`)

## What changed from the previous build (run 0ff7fe5f)

The public source SHA changed. Comparing current `brand_variant.py` to what beats B04/B07/B08 showed in the prior film:

1. **Output format changed to single-line** — `print(f"[variant] wrote {out}  audience=…  …")` used to be multi-line indented; now emits a single long line. B04 and B08 showed stale multi-line format.
2. **`copy_build_scripts()` added** — new helper copies `build_deck.py`, `render.py`, `make_audio*.py` from the canonical reel into the variant folder. B07 code prop omitted this entirely.
3. **Segment beat strip added** — `for seg in sheet.get("segments", []):` loop strips `actual_duration_s` from lecture-segment beats too. B07 code prop showed only the reel-beats loop.

**Beats re-rendered:** B04, B07, B08.
**Audio regenerated:** B07 only (narration updated from "three things" to "four things", now 30.51s from 26.62s).

## Runtime gates that ran

| gate | invoker | input | outcome |
|------|---------|-------|---------|
| audio generation | `runtime/scripts/generate_audio_kokoro.py` | B07 narration (updated) | 30.51s, am_onyx, $0.00 |
| scene-render fit | `runtime/scripts/remotion_scenes.py --force` | B04/B07/B08 | 3 beats re-rendered VIDEO |
| clip assembly | `runtime/scripts/compile.py` | `beat_sheet.json` + `media/*.mp4` + `mp3/*.mp3` | 12/12 clips concatenated |
| Gate V (final_frame_check) | `runtime/qc/final_frame_check.py` | candidate MP4 + beat_sheet | 24 frames sampled · BLOCKER 0 · MAJOR 0 · **PASS** |
| atomic master write | `runtime/scripts/compile.py` | verified candidate | landscape master written, `.verified.json` receipt beside it |
| ffprobe on master | `ffprobe -v error` | master MP4 | width=3840, height=2160, duration=222.8s, h264, AAC audio present |

## Demo evidence

All CLI/output shown in the film is verbatim from `demo/RUN-LOG.txt` (14 sections, captured live with the working-toolkit `brand_variant.py`). The updated beats show:

- **B04**: single-line `[variant] wrote ... audience=HAI register=Plain ... engine=kokoro voice=af_bella` + `[variant] 2 beats to rewrite in Plain — next: follow skills/make/hai/SKILL.md` (verbatim from RUN-LOG §2+5)
- **B07**: main() body now includes `for seg in sheet.get("segments", [])` loop and `copy_build_scripts(reel, out_dir)` call (source lines 130-140)
- **B08**: single-line refusal `already exists (use --force to reset it from canonical)` and single-line `--force` success (verbatim from RUN-LOG §10+11+12)

## Static / structural checks

- `beat_sheet.json` metadata: `playlist: "Brutalist"`, `voice_kokoro: "am_onyx"`, `captions: false`, `channel: "@HumanitariansAI"`, `persona: "Liam (in for Bear)"`, `in_for_bear: true`, `aspect_ratio: "16:9"` — all present.
- B00 `ClaudeComposerAsk`, B01 `BrutalistHesitantWriter`, B10 `ClaudeComposerAsk` with `greeting: "Your Turn"`, B11 `ClaudeTitleOutro` — Cold-Open / BLUF / Your-Turn / Outro laws satisfied.
- B11 narration contains "liam" and "in for bear" — LIAM SIGN-OFF LAW satisfied.
- All beats carry `audio_file: mp3/beat-B*.mp3` and measured `actual_duration_s` from Kokoro.

## Visual review (AI, this run)

`VISUAL-REVIEW.json` at the reel root captures current frame evidence with real SHA-256s and this invocation's `run_id`. Contact sheet opened with the image-capable Read tool: cold open (composer with Yassou greeting), BLUF corrected settle, pipeline strip, CLI help, single-line hai variant output, AUD dict, get_brand_dir(), updated main() body with segment loop and copy_build_scripts, single-line refusal cases, verdict card, Your-Turn composer, title outro. All beats sit inside SAFE with no edge-bleed, no unresolved slates, no subtitle track, no caption overlay.

## Gaps and honest caveats

- Motion histogram: `code-cascade` covers 6/12 beats (50%) — over the ~40% pantry cap. Teardown of a 152-line Python file; code-heavy body is intentional. Warning only, not a gate.
- `runtime/scripts/type_check.py` — not present in this isolated toolkit revision. Typography reviewed visually via contact sheet only.
- `runtime/qc/kerning_check.py` — not present. Kerning inspected visually in extracted frames.
- Outro card shows hardcoded `@NikBearBrown` per OUTRO-LOCK.md; composer folder chip reads `@HumanitariansAI`. Flagged for human reviewer before publication.

## Environment

- Chrome wrapper: `youtube/brutalist/claude-liam-brutalist-download-and-set-up/scene-source/runtime/scripts/chrome-single-process.sh` via `ART_CHROME` + `ART_CHROME_MODE=chrome-for-testing` (same workaround as prior build — Apple App Sandbox Mach-port block).
- Isolated toolkit `node_modules` at `toolkit/runtime/remotion/node_modules/` (not a symlink — per prior build's shadow fix).

## Human review pending

This is an AI frame-review record satisfying the "current AI frame-review record" gate; it is NOT a human sign-off. Bear's viewing/editing is the next step, per `README.md`.
