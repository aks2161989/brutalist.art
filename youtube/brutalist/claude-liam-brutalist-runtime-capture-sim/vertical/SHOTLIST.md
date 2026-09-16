# SHOTLIST — Brutalist Utility: capture_sim.py

12 beats · palette `claude` · Kokoro `am_onyx` · aspect `16:9` for landscape, `9:16` (native, full-length) for vertical. Every beat is a real registered scene composition; no slates, no ad-hoc filler.

| Beat | Act              | Component (landscape / portrait)                                  | Motion             | Key visual                                                                                          |
|------|------------------|--------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------------------------------|
| B00  | ASK              | `ClaudeComposerAsk`                                                | type-on            | Composer card on cream. Greeting `Tere, Liam` types above; the ask + 3 answer lines cascade in.     |
| B01  | BLUF             | `BrutalistHesitantWriter`                                          | hesitant-type      | Three lines settle from `capture_sim / renders / the sim.` → `capture_sim / RECORDS / the browser.` |
| B02  | FRAMEWORK        | `SkillTeardownPipeline`                                            | phase-flow         | INPUT `sim.html` → 5 phases (SERVE / LAUNCH / DRIVE / RECORD / REMUX) → OUTPUT `media/*.mp4`.       |
| B03  | MECHANISM 1      | `ClaudeCodeBeat`                                                   | code-cascade       | Verbatim `capture_sim.py -h` — positional args, mode-selecting flags, capture-shaping flags.        |
| B04  | MECHANISM 2      | `ClaudeCodeBeat`                                                   | code-cascade       | Trimmed `capture()` — the baseline + change contexts, the 40-step sweep, the `input`/`change` fires.|
| B05  | MECHANISM 3      | `ClaudeCodeBeat`                                                   | code-cascade       | Trimmed `capture_click_through()` — the `count < 2` guard and the per-click re-query.               |
| B06  | MECHANISM 4      | `ClaudeCodeBeat`                                                   | code-cascade       | Trimmed `capture_scripted()` — the verb dispatch and `assert_sel()`.                                |
| B07  | WORKED EXAMPLE   | `ClaudeCodeBeat`                                                   | code-cascade       | The tiny-wave fixture head + the 5-step DSL JSON, side-by-side. Docstring rule cited underneath.    |
| B08  | FAILURE          | `ClaudeCodeBeat`                                                   | code-cascade       | Verbatim `[capture_sim] FAILED: BrowserType.launch: …` + `[FATAL:…Mach…Permission denied (1100)]`.  |
| B09  | VERDICT          | `ClaudeVerdictArtifact`                                            | artifact-in        | Six-line artifact restating the whole surface in the order it does its job.                         |
| B10  | YOUR TURN        | `ClaudeComposerAsk` (greeting `Your Turn`)                         | type-on            | Composer card with a paste-ready prompt + 3 grading criteria. Liam reads the prompt aloud.          |
| B11  | OUTRO            | `ClaudeTitleOutro` (locked; hardcoded `@NikBearBrown` per OUTRO-LOCK.md) | outro-card    | Title restate, mascot animation, handle. Flagged in `README.md` for human review.                   |

Vertical (`9:16`) uses the same landscape components (`ClaudeComposerAsk`, `BrutalistHesitantWriter`, `SkillTeardownPipeline`, `ClaudeCodeBeat`, `ClaudeVerdictArtifact`) with `fit: pad` so nothing crops or bleeds — same recipe used by ep39/ep40/ep41. The outro uses `ClaudeTitleOutro916` and the verdict uses `ClaudeVerdictArtifact916` (native portrait registered variants). Portrait skin lint warnings on B00 / B11 will call out the ClaudeComposerAsk / ClaudeTitleOutro variant swap, and that's expected — same as ep41.

## Duration budget (rough — audio is ground truth)

Aim total: ~200–240 s across the 12 beats. Actuals will follow measured Kokoro output. No padding, no target-time engineering.

## What each beat MUST show before narration explains it (`shot.show` invariants)

- B00: composer chip must read `@HumanitariansAI` (not the hardcoded @NikBearBrown default).
- B01: seed is stable — `csim-b01-landscape-v1` / `csim-b01-vertical-v1`. Lead silence 0.8s per the SKILL modifier.
- B02: the arrow between phases uses accent (terracotta) on `SERVE` and `RECORD` — the two irreducible steps.
- B03/B04/B05/B06/B07/B08: `sparkLine` is a one-line "so what" under the code card. Never omitted.
- B09: the six artifact lines are the exact recap points from `SCRIPT.md#B09`.
- B10: the greeting reads `Your Turn`, the `runningText` reads `paste this into Claude Code…`.
- B11: title reads `Brutalist Utility: capture_sim.py.` — one period, no trailing whitespace.
