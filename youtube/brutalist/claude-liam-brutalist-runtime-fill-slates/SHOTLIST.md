# SHOTLIST — Brutalist Utility: fill_slates.py

12 beats total. Every SHOW block in `beat_sheet.json` is the authoritative shot list; this file summarizes them for review.

| Beat | Duration (audio) | Pattern | Purpose | Key visual event |
|---|---|---|---|---|
| B00 | 14.68s | `ClaudeComposerAsk` | Cold open — ask lands answered | Greeting `Hej, Liam` → typed ask → running-text `invoking fill_slates.py…` → 3 result output lines cascade |
| B01 | 10.43s | `BrutalistHesitantWriter` | BLUF hesitant writer | `fill_slates / rewrites / all beats / in a reel.` → `rewrites`→`stamps`, `all`→`empty` |
| B02 | 23.06s | `SkillTeardownPipeline` | Framework — the whole pipeline | INPUT `books/  --apply` → WALK → FIND → STAMP → RENDER → RECUT → OUTPUT `<reel>-slate.mp4 refreshed` |
| B03 | 18.24s | `ClaudeCodeBeat` | Mechanism 1 — CLI surface | `fill_slates.py -h` verbatim + docstring usage lines |
| B04 | 24.06s | `ClaudeCodeBeat` | Mechanism 2 — slate definition | `slate_resolves()` + `find_slates()` bodies, verbatim |
| B05 | 22.02s | `ClaudeCodeBeat` | Mechanism 3 — the stamp | `_truncate()` + `stamp_slates()` bodies, verbatim |
| B06 | 24.10s | `ClaudeCodeBeat` | Mechanism 4 — render_reel | Two `subprocess.run()` calls, remotion → run.sh |
| B07 | 22.42s | `ClaudeCodeBeat` | Worked example — disposable fixture | 5-beat fixture description + observed `--books demo/` dry-run + post-stamp shot record |
| B08 | 27.39s | `ClaudeCodeBeat` | Mechanism 5 — falsifiability | The 4 failure modes + main-loop FAIL detection |
| B09 | 19.54s | `ClaudeVerdictArtifact` | Verdict artifact | 6 lines summarizing input · define · find · stamp · render · output |
| B10 | 24.70s | `ClaudeComposerAsk` | Your Turn (HANDOFF) | Prompt to run fill_slates dry-run on your own books tree and upgrade ONE card |
| B11 | 6.10s | `ClaudeTitleOutro` | Outro | Title restate `Brutalist Utility: fill_slates.py.` + `@NikBearBrown` + slug-seeded mascot |

Total narration ~236.74s (measured Kokoro `am_onyx`).
