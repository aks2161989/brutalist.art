# SOURCES — Brutalist Utility: setup_smoke_kokoro.py

## Primary source

| File | Repo path | SHA-256 (at capture) |
|---|---|---|
| setup_smoke_kokoro.py | `runtime/scripts/setup_smoke_kokoro.py` | `4e4df6611a34dcc1e001241769bc6479abf947effa58315d09cec4e8a04a0e30` |

Captured at: 2026-09-14T12:06:42Z  
Toolkit commit: ba2d0e0f043f5b3b35a50d336e0fc66fbfecfc0c

## Code shown on screen

All code shown in ClaudeCodeBeat beats is excerpted verbatim from the primary source file above. Lines shown:
- B03 (guards): lines 31–39 of setup_smoke_kokoro.py
- B04 (synthesis): lines 41–51 (adapted for readability — WAV write loop condensed to comment)
- B05 (volume gate): lines 53–68 (subprocess.run + parse + threshold check)
- B06 (failure messages): fail() outputs as they appear in the script; success output at line 69
- B07 (cleanup): lines 58–72 (try/finally block)

All code excerpts are source-backed. No fabricated output. The success message `[smoke] kokoro synth OK — mean_volume -14.3 dB` in B06 is a representative value; the actual measured dB varies by host.

## VERBATIM QUOTE LAW

- Docstring quote "one throwaway phrase" (B07): from module docstring, line 3 — "Synthesizes one throwaway phrase with Kokoro"
- "[smoke]" prefix: from fail() function, line 25 — `print(f"[smoke] {msg}", file=sys.stderr)`
- THRESHOLD_DB = -40.0: from line 22 of the source

## Skills documentation (read, not quoted on screen)

- `skills/make/ai-explainer/SKILL.md` — production framework
- `skills/make/explainer/SKILL.md` — parent chassis
- `skills/make/nopunt/SKILL.md` — anti-punt catalog
- `runtime/prose/teardown/PROSE.md` — Teardown register
- `CLAUDE-BRAND.md`, `OUTRO-LOCK.md`, `CLAUDE-CODE-VISUAL-QC-CHECK.md`
- `docs/PIPELINE-SAFETY.md`, `docs/FELLOWS-SUBMISSION.md`

## New component registered this build

`ClaudeCodeBeat916` — added to `runtime/remotion/src/Root.tsx` and `runtime/remotion/src/scenes.json` in the isolated toolkit. Same component as ClaudeCodeBeat, registered at 1080×1920 for portrait vertical renders.
