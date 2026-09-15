# FACTCHECK.md — Your First Brutalist Project (landscape 16:9)

Every on-screen claim in this reel is checked against the isolated toolkit that
built it. Nothing here rests on outside quotes or unverifiable metrics.

## Structural claims (verified against the isolated toolkit)

| Claim on screen | Verified against | Notes |
|---|---|---|
| The video is a file (`beat_sheet.json`) | `runtime/scripts/compile.py:614–620` reads `beat_sheet.json` and stamps a `build` record back into it. | The B02 code fragment is a real, structurally valid beat — checked against the schema for keys `beat_id`, `act`, `narration_text`, `engine`, `voice`, `shot.remotion.pattern`. |
| Kokoro `am_onyx` is the local, free voice | `runtime/scripts/generate_audio_kokoro.py` (see docstring: "Kokoro is FREE — a local 82M-parameter Apache-2.0 model"); `KOKORO_MODEL` / `KOKORO_VOICES` env vars point at local `.onnx` and `.bin` files (325 MB / 28 MB). | No API, no meter — the audio for this reel was generated locally with `am_onyx`; per-beat durations are in `beat_sheet.json` (`actual_duration_s`). |
| Renders scenes as `media/*.mp4` (one per Remotion beat) | `runtime/scripts/remotion_scenes.py:71–102`. | 11 filled beats produced files in `media/` this run; `B11` uses `ClaudeTitleOutroHAI`, an isolated-toolkit variant of `ClaudeTitleOutro` registered in `runtime/remotion/src/Root.tsx`. |
| Compiles `clips/ → review-cut.mp4` at 3840×2160 | `runtime/scripts/compile.py:647–651` computes `h,w` from `metadata.aspect_ratio` and `--height`. With `aspect_ratio: "16:9"` and `--height 2160`, the master is `3840×2160`. | This reel's landscape master is compiled with `--height 2160 --out exports/landscape`. |
| One revision changes ONE beat, everything else cached | `runtime/scripts/compile.py` retains a per-slot input hash manifest (`clips/manifest.json`) and rebuilds only when a slot's input changed; per-beat clips live in `clips/<BID>.mp4`. | The B07 diff card names exactly the files a single-beat revision touches. |
| 9:16 vertical is a separate beat sheet, not a crop | Landscape reads `beat_sheet.json` with `aspect_ratio: "16:9"`; the vertical reel lives in `<reel>/vertical/beat_sheet.json` with `aspect_ratio: "9:16"` and slug `<slug>-vertical`. `./art vertical` PLANS a portrait sheet (per its skill doc); portrait-native compositions like `ClaudeComposerAsk916`, `ClaudeTitleOutroHAI916` exist in `Root.tsx`. | The B08 artifact lines say exactly this. |
| Source ≤ 25 MB → GitHub; MP4/MP3 → Drive | `docs/FELLOWS-SUBMISSION.md` documents the 25 MB rule and the branch/PR workflow. | The B09 card restates the current rule and disclaims "runtime receipt ≠ publication approval". |
| Runtime receipt is not publication approval | `docs/PIPELINE-SAFETY.md` — Brutalist does not upload or publish; that is a separate human decision. | Named plainly in B09 narration. |

## Persona / channel claims

| Claim | Verification |
|---|---|
| "Liam, in for Bear" — narrator | Kokoro voice `am_onyx` is the working default for `claude-liam` per `skills/make/ai-explainer/SKILL.md` Channels table. B00 narration introduces "This is Liam, in for Bear" per IN-FOR-BEAR LAW; the outro B11 signs off the same way. |
| Handle: `@HumanitariansAI` | The Brutalist playlist targets `@HumanitariansAI` per the supervisor's episode contract. The stock `ClaudeTitleOutro` hardcodes `@NikBearBrown` (see `runtime/remotion/src/scenes/ClaudeTitleOutro.tsx`), so this reel uses the isolated variant `ClaudeTitleOutroHAI` (registered in `Root.tsx`) which accepts `handle` as a prop. Neither the live `ClaudeTitleOutro` nor `OUTRO-LOCK.md` was modified. |
| No captions, no burned-in transcript | `metadata.captions: false`. `compile.py` does not emit SRT/VTT for this reel. |

## What is NOT claimed on screen

- **No** claim of paid Claude API or unlimited use. B00 says "one ask into Claude Code"; the subscription vs. API distinction is honored by the brief and not asserted anywhere.
- **No** claim that this reel is published. The narration and the B09 card explicitly frame the compile as a runtime receipt, with human review still ahead.
- **No** demonstration of `./setup --install`, `./art keys`, or a live `git clone` against the public repo. The B00–B10 composer beats show paste-ready prompts and the artifact cards describe what the pipeline does; the actual pipeline that built THIS reel is the demonstration.
- **No** fellow's name or private Drive URL. The Google Drive folder link from the read-only example (`746409a8715e.json`, Rohan V's weekly-video reel) is NOT republished here — the B09 card mentions "Google Drive folder" without a URL.

## Gaps recorded honestly

- **`scripts/type_check.py` and `reference/type-spec.md` are absent** in this toolkit. The AI Explainer SKILL.md references GATE T (`type_check.py`), but the file does not ship in this isolated cut. `TYPECHECK.md` documents this and reports the actual visual typography check that was performed on the extracted frames (Read tool inspection at 15/50/85 %).
- **`ILLUSTRATIONS.md` is present** at `runtime/remotion/src/illustrations/ILLUSTRATIONS.md` — no gap here.
- **`_qc/REPORT.md` procedure** is documented in `CLAUDE-CODE-VISUAL-QC-CHECK.md`; the checks used here are recorded in `CHECKS-REPORT.md`.
