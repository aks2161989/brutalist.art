# SHOTLIST — Brutalist Utility: capture_sim.py (Short)

7 beats · palette `claude` · Kokoro `am_onyx` · aspect `9:16` native portrait (2160×3840). Every kept beat is the same registered scene composition the vertical parent already used; nothing was re-rendered.

| Beat | Act              | Portrait component                                    | Motion         | Key visual                                                                                                     |
|------|------------------|-------------------------------------------------------|----------------|----------------------------------------------------------------------------------------------------------------|
| B00  | ASK              | `ClaudeComposerAsk916`                                | type-on        | Composer card on cream. Greeting `Tere, Liam` types above; ask + 3 answer lines cascade in; chip = `@HumanitariansAI`. |
| B01  | BLUF             | `BrutalistHesitantWriter916`                          | hesitant-type  | Three lines settle from `capture_sim / renders / the sim.` → `capture_sim / RECORDS / the browser.`             |
| B02  | FRAMEWORK        | `SkillTeardownMechanism916`                           | phase-flow     | Eyebrow `UTILITY · PIPELINE`, heading `Serve. Launch. Drive. Record. Remux.`, body paragraph, spark line.       |
| B07  | WORKED EXAMPLE   | `ClaudeCodeBeat916`                                   | code-cascade   | `demo/sim-source/00-tiny-wave.html` head + `demo/scripts/tiny-wave-sweep.json` + docstring rule footer.         |
| B08  | FAILURE          | `ClaudeCodeBeat916`                                   | code-cascade   | Verbatim `[capture_sim] FAILED` + `[FATAL:…Mach…Permission denied (1100)]` + environmental-fix commentary.      |
| B09  | VERDICT          | `ClaudeVerdictArtifact916`                            | artifact-in    | Six-line artifact restating the whole surface (serve/launch/drive/record/remux/assert) in run order.            |
| B11  | OUTRO            | `ClaudeTitleOutro916` (OUTRO-LOCK, hardcoded `@NikBearBrown`) | outro-card | Title restate `Brutalist Utility: capture_sim.py.`, mascot animation, handle. Flagged in `README.md` for human review. |

## Dropped from the Short (belong in the long)

- **B03** `ClaudeCodeBeat916` — verbatim `capture_sim.py -h` CLI surface.
- **B04** `ClaudeCodeBeat916` — `capture()` default two-context sweep code.
- **B05** `ClaudeCodeBeat916` — `capture_click_through()` code + `count<2` guard.
- **B06** `ClaudeCodeBeat916` — `capture_scripted()` 7-verb DSL dispatch.
- **B10** `ClaudeComposerAsk916` — Your Turn assignment prompt.

## Actual measured durations (per beat, from parent `beat_sheet.json`)

| Beat | Audio | Video (render) |
|------|------:|---------------:|
| B00  | 16.98 | 17.000         |
| B01  | 14.57 | 14.583         |
| B02  | 26.67 | 26.708         |
| B07  | 25.34 | 25.375         |
| B08  | 26.65 | 26.667         |
| B09  | 22.83 | 22.833         |
| B11  |  6.04 |  6.042         |
| **Total** | **139.08** | **139.208** |

Container / video / audio durations per ffprobe: `139.208 s / 139.167 s / 139.208 s` — all strictly below 180 s.

## Invariants that must hold in every kept beat

- B00: composer folder chip reads `@HumanitariansAI` (frame `_qc/frames/first.png` confirms).
- B01: hesitant-writer settles on `capture_sim / RECORDS / the browser.` with BLUF coverage ≥ 55% of SAFE916.
- B02: `Serve. Launch. Drive. Record. Remux.` heading and spark line `The browser draws. The tool records.` both fit inside SAFE916 (`_qc/frames/B02-50.png`).
- B07: docstring rule footer starts with `# capture_sim.py docstring, line 43-45:`.
- B08: `[FATAL:base/apple/mach_port_rendezvous_mac.cc:159]` line is the crash citation, quoted verbatim.
- B09: 6 numbered artifact lines, one per pipeline phase + the assert-guard.
- B11: title reads `Brutalist Utility: capture_sim.py.` — one period, handle `@NikBearBrown` per OUTRO-LOCK.
