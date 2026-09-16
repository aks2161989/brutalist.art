# PROMPTS — Brutalist Utility: build_cli_d3_reels.py

Prompts that appear ON SCREEN in the reel. Copy-pasteable; verbatim in the beat sheet's composer props.

## B00 — Cold-open ask (`ClaudeComposerAsk`)

```
I have a folder of D3 sims already built (one HTML each). Wrap every one in
a Claude-skin explainer reel. Unattended, overnight, one config.json in.
```

**RunningText:** `invoking build_cli_d3_reels.py…`
**Output lines** (three, cascading):
- reads sims[] from config.json — each row: slug · book · html · note
- stamps beat_sheet.json (ClaudeComposerAsk / ClaudeCodeBeat / ClaudeTitleOutro; 10 beats)
- captures the sim → audio → Remotion → compile.py --review; appends one row per sim to the log

## B10 — Handoff prompt (`ClaudeComposerAsk`, greeting = `Your Turn`)

```
Point Claude Code at a folder that already contains N single-file D3 sim
HTMLs: (1) for each .html, extract a one-line physics note by reading the
file and any adjacent README; (2) draft a config.json with one sims[] row
per HTML — slug from the filename, a book field, note verbatim from step 1,
no title field (let make_title() run); (3) dry-run only: `python3 -c 'import
build_cli_d3_reels as m; ...'` to call make_beat_sheet() for each row and
PRINT the stamped 10 beats. Do NOT run capture_sim or compile.py yet. Do
NOT invent notes you did not observe — an invented note becomes an invented
reel title.
```

**RunningText:** `paste this into Claude Code…`
**Output lines** (three grading criteria the viewer should look for):
- step 1 — one-line note per html, cited to the file/README that provided it
- step 2 — config.json with N sims[] rows; no title fields; run book fields past the human
- step 3 — 10 beats per sim printed as a table; the human verifies notes before capture starts

The prompt is scoped to a **dry-run** on purpose — the viewer inspects what the tool would stamp before any subprocess is spawned. That is the trap the note field exists to catch: `concept = note.split(";")[0].strip()` (line 132–133) becomes the reel's title, so a fabricated note becomes a fabricated reel.
