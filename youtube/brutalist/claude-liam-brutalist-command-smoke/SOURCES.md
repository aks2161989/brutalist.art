# SOURCES.md — Brutalist Command: art smoke

All references are files inside the isolated toolkit snapshot at
`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/.repoloop/workspaces/claude-liam-brutalist-command-smoke/toolkit/`.
Original repo-relative paths are preserved.

## Primary sources

| Repo path | SHA-256 | Role |
|---|---|---|
| `art` | `c5b4e9954b15e76f4e7b9009997cdf0796d3321fbd3b9e8c9f6f54f0cfc08c5b` | Top-level dispatcher script; contains the `smoke)` case at art:121-123. |
| `runtime/scripts/smoke_test.sh` | `d5403ed9babbc5b519e3b4892c9e2c09b572e12855a230e5be8c0006767cae90` | The runner. Kokoro → run.sh → three decoded gates. |
| `examples/_smoke/beat_sheet.json` | `5522f1cea313cc0a69eb71cc3458a00ce8c523160725c8ad40f945985f1cca97` | The fixture — two bare narration slates, af_bella, zero Manim, zero Remotion. |
| `examples/_smoke/PEDAGOGY.md` | `34a913209b720313c307b53ec59cae0c22220d8b0d81c63a90e98f2a7d1bd57e` | Fixture rationale (PASS-verdict card). |
| `runtime/scripts/build_safety.py` | `479e167ffc80c4a2c235b425149b3922fd96a2e7388a40636f2dfa63b56015bf` | Fail-closed contracts. Introduced in commit ba2d0e0 (2026-09-07). Contains the slug regex at lines 186-187 that currently blocks the `_smoke` fixture. |
| `runtime/scripts/generate_audio_kokoro.py` | (unchanged from baseline) | Kokoro-onnx entry point invoked as GATE 0 of smoke_test.sh. |
| `runtime/scripts/run.sh` | (unchanged from baseline) | The render + compile driver invoked as smoke_test.sh's second stage; wraps GATE L, GATE SHAPE, Manim, Remotion, compile.py, GATE V. |
| `runtime/scripts/setup_smoke_kokoro.py` | (unchanged) | Not invoked by `./art smoke`, but referenced as the audio floor's shared authority (mean_volume > -40 dB). |

## Toolkit meta

- Toolkit baseline SHA-256: `92432609980c8ffc03bc1f00a1300fe1ac78bd7363b5b8ba9f2d389407d72b9d`
- Local Root.tsx override in this isolated toolkit: registered
  `ClaudeCodeBeat916` (portrait variant of ClaudeCodeBeat) so the vertical
  companion could render natively rather than crop. Recorded in
  `scene-source-manifest.json`. No source-of-truth Root.tsx was touched.
- Public repository (for reference only, no clones performed):
  https://github.com/nikbearbrown/brutalist.art

## Direct captures

- `demo/RUN-LOG.txt` — timestamped verbatim capture of `./art smoke`
  against the shipped fixture (fails) and of a manually reproduced pass
  path (fixture slug patched in a scratch copy).

## Cross-references

- `runtime/prose/teardown/PROSE.md` — narration register (Teardown, Liam
  in for Bear).
- `CLAUDE-BRAND.md` — palette / typography discipline.
- `OUTRO-LOCK.md` — the outro card is locked to `ClaudeTitleOutro` with
  hardcoded `@NikBearBrown` handle; the composer folder chip in every
  other beat carries `@HumanitariansAI` per playlist adaptation.
- `docs/PIPELINE-SAFETY.md`, `docs/FELLOWS-SUBMISSION.md` — governing
  contracts read but not directly narrated.
- `CLAUDE-CODE-VISUAL-QC-CHECK.md` — visual QC procedure applied per aspect.

No paid assets, no external network calls, no impersonation of any human
signature. `demo/RUN-LOG.txt` output originates from this workstation only.
