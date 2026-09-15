# Brutalist Utility: setup_smoke_kokoro.py

Episode 54 of the Brutalist playlist. AI Explainer teardown of `runtime/scripts/setup_smoke_kokoro.py` — the audio gate that `./setup` calls to confirm Kokoro TTS is actually producing audible speech, not just importing cleanly. It synthesizes a short phrase, probes mean volume with ffprobe, and exits zero only if the dB reading is above −40 dB.

- **Voice:** Kokoro `am_onyx` (Liam, in for Bear)
- **Playlist:** Brutalist · Channel: `@HumanitariansAI`
- **Run ID:** `030891286f944a7f9f0175823eff81cd`
- **Length:** 207.5 s across 11 beats, both aspects

## Deliverables (both native 4K, Gate V clean)

| Aspect | File | Dimensions |
|---|---|---|
| Landscape | `exports/landscape/claude-liam-brutalist-runtime-setup-smoke-kokoro.mp4` | 3840×2160 |
| Vertical  | `exports/vertical/claude-liam-brutalist-runtime-setup-smoke-kokoro-vertical.mp4` | 2160×3840 |

SHA-256 hashes are in each aspect's `VISUAL-REVIEW.json`.

## Contents

- `beat_sheet.json` (11 beats, landscape) · `vertical/beat_sheet.json` (11 beats, portrait)
- `SCRIPT.md`, `SOURCES.md`, `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`, `TYPECHECK.md`, `CHECKS-REPORT.md` — landscape
- `vertical/` mirror of the six paperwork files
- `media/`, `mp3/`, `clips/`, `_qc/` — per-beat working files (landscape); mirrored under `vertical/`
- `VISUAL-REVIEW.json` and `vertical/VISUAL-REVIEW.json` — AI review records (current run_id, real SHAs)

## Teaching arc

| Beat | Scene | Content |
|---|---|---|
| B00 | ClaudeComposerAsk | Cold open: why synthesis — not import — is the correct gate |
| B01 | BrutalistHesitantWriter | BLUF: "setup checks Kokoro by verifying the synthesis works. Loading the model is insufficient." |
| B02 | SkillTeardownPipeline | Five-phase chain: guard → synth → probe → gate → cleanup |
| B03 | ClaudeCodeBeat | Guard section: model files · ffmpeg · kokoro_onnx prerequisites |
| B04 | ClaudeCodeBeat | Synthesis: `KokoroTTS(model, voices)` + `generate()` → temp wav |
| B05 | ClaudeCodeBeat | Volume probe: `ffprobe mean_volume` extraction |
| B06 | ClaudeCodeBeat | Failure modes: missing model / missing ffmpeg / silent audio / decode error |
| B07 | ClaudeCodeBeat | try/finally cleanup: temp file always deleted regardless of outcome |
| B08 | ClaudeVerdictArtifact | Verdict: synthesis gate vs. import-only, the −40 dB threshold, cleanup design |
| B09 | ClaudeComposerAsk | HANDOFF: paste-ready prompt — "look for what's synthesized vs. what's imported" |
| B10 | ClaudeTitleOutroHAI | "Brutalist Utility: setup_smoke_kokoro.py." — Liam, in for Bear. @HumanitariansAI |

## Notable fixes from this build session

**HAI outro channel fix (run 030891286f)** — B10 used `ClaudeTitleOutro` which is locked to `@NikBearBrown` per OUTRO-LOCK.md. Created isolated `ClaudeTitleOutroHAI` / `ClaudeTitleOutroHAI916` components with `@HumanitariansAI` handle. Both exports recompiled and Gate V re-run.

**BrutalistHesitantWriter portrait-scale bug** — the shipped component used `scale = Math.min(width/1920, height/1080)` which collapses to 0.5625 at 1080×1920, producing ~4% ink coverage (Gate V BLOCKER). Patched to a portrait-aware ternary that gives scale = 1.0 on both orientations. Fix is in the production toolkit at `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx` line 223.

## Human review next

Bear watches the two files and can leave notes in `FEEDBACK.md`. Nothing has been published, uploaded, or committed to git.
