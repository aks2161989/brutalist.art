# SHOTLIST — Brutalist Utility: fill_slates.py (Short)

7 beats retained from the parent's 12. Every SHOW block in `beat_sheet.json`
is the authoritative shot list; this file summarizes only the retained beats.
All portrait renders are byte-for-byte copies of the parent's `vertical/media/`
(no re-render).

| Beat | Duration (audio) | Pattern | Purpose | Key visual event |
|---|---|---|---|---|
| B00 | 14.68s | `ClaudeComposerAsk916` | Cold open — ask lands answered | Greeting `Hej, Liam` → typed ask → running-text `invoking fill_slates.py…` → 3 result output lines cascade |
| B01 | 10.43s | `BrutalistHesitantWriter916` | BLUF hesitant writer | `fill_slates / rewrites / all beats / in a reel.` → `rewrites`→`stamps`, `all`→`empty` |
| B02 | 23.06s | `SkillTeardownMechanism916` | Framework — the whole pipeline | Heading `Dry-run by default. --apply stamps + renders + recuts.` → WALK → FIND → STAMP → RENDER → RECUT → quote of the four skip conditions → verdict + spark |
| B07 | 22.42s | `ClaudeCodeBeat916` | Worked example — disposable fixture | 5-beat fixture description + observed `--books demo/` dry-run + post-stamp shot record |
| B08 | 27.39s | `ClaudeCodeBeat916` | Failure modes (falsifiability) | The 4 failure modes + main-loop FAIL detection |
| B09 | 19.54s | `ClaudeVerdictArtifact916` | Verdict artifact | 6 lines summarizing input · define · find · stamp · render · output |
| B11 | 6.10s | `ClaudeTitleOutro916` | Outro | Title restate `Brutalist Utility: fill_slates.py.` + `@NikBearBrown` handle |

Total narration ~123.79 s (measured Kokoro `am_onyx`).

## Dropped from the long teardown

- B03 · `ClaudeCodeBeat916` — CLI surface (`--help`) + docstring usage lines
- B04 · `ClaudeCodeBeat916` — `slate_resolves()` + `find_slates()` bodies
- B05 · `ClaudeCodeBeat916` — `_truncate()` + `stamp_slates()` bodies
- B06 · `ClaudeCodeBeat916` — `render_reel()` two-subprocess block
- B10 · `ClaudeComposerAsk916` — extended YOUR TURN prompt

The four MECHANISM code cascades and the YOUR TURN handoff are preserved in
the full-length vertical parent; the Short's B02 / B07 / B08 / B09 already
carry the pipeline-level truths at the surface the Short is teaching for.
