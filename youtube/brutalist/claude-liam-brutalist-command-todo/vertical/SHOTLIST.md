# SHOTLIST — Brutalist Command: art todo

12 beats. AI Explainer skin (cream `#FAF9F5`, ink `#3D3929`, terracotta
`#D97757` as the one accent). Every non-bookend beat carries a custom scene
authored for this reel (`TodoPipeline`, `TodoCommand`, `TodoRun`, `TodoEntry`,
`TodoMethods`, `TodoAgentLoop`, `TodoFailure`), registered under folder
`ClaudeLiamCommandTodo` in `Root.tsx`.

| Beat | Pattern | Purpose | On-screen event lattice (audio-clock fractions) |
|---|---|---|---|
| B00 | `ClaudeComposerAsk` | Cold open — the ask, answered with a three-line output. | 0.00 cream page + `Hola, Liam` serif greeting · 0.12 command types in · 0.60 send arms terracotta · 0.76 three result lines stagger — the answer is on screen when the ask lands. |
| B01 | `BrutalistHesitantWriter` (seed 4828) | BLUF — "a to-do list I write" corrected to "a receipt of the beat sheet". Correction changes the whole sentence. | Component-driven: writer types, pauses, terracotta marks the trigger phrase, replacement types in. `lead_silence_s: 0.8` on the audio. ≥9 s. |
| B02 | `TodoPipeline` | FRAMEWORK — one arrow: `beat_sheet.json` → `art todo` → three receipts. | 0.10 left node lands: `beat_sheet.json` · 0.35 middle node lands: `art todo` · 0.55 right stack lands (three cards: `todo.json`, `STATUS.md`, `ToDo.md`) with the middle card lit terracotta as the human-owed one · 0.90 tagline settles: "Edit the sheet, not the receipts." |
| B03 | `TodoCommand` | FRAMEWORK 2 — the command's exact syntax. | 0.10 command bar lands (`./art todo <reel> [flags]`) · 0.28–0.90 the three flags land one at a time as each is named, with a one-line effect chip beside each; the last flag lands terracotta. |
| B04 | `TodoRun` | WORKED EXAMPLE — a live terminal transcript. | 0.05 cursor + `$ ./art todo demo/example-reel` · 0.20 header line (`0/5 filled → …`) · 0.30–0.90 the five beat rows stagger in on their own spoken cue; the human-owed rows carry a terracotta chip. |
| B05 | `TodoEntry` | ANATOMY — one beat entry, six labelled fields. | 0.10 JSON-shaped card lands on cream · 0.20–0.90 the six field lines light one at a time (`status`, `method`, `who`, `slot`, `prompt`, `label`), with the currently-narrated field carrying the terracotta bar. |
| B06 | `TodoMethods` | MECHANISM — five fill lanes as a five-row table. | 0.05 header row lands · 0.15–0.85 five rows stagger — `remotion` and `manim` pill-labelled `pipeline` (muted); `historical-image`, `user-capture`, `ai-video-prompt` labelled `human` in terracotta. |
| B07 | `TodoAgentLoop` | THE AGENT LOOP — `--method manim --open` as a loop diagram. | 0.05 command bar with the filter chips lit · 0.25 arrow to a boxed queue of two beat IDs · 0.50 arrow back to `render → drop mp4` · 0.75 arrow back to a re-run of the ledger with the queue now empty (all filled). |
| B08 | `TodoFailure` | FAILURE + RECOVERY — the "no beat_sheet.json" refusal. | 0.05 command bar lands (`$ ./art todo demo/empty-reel`) · 0.20 red-ink stderr line: `[todo] no beat_sheet.json in …/empty-reel` · 0.35 exit-1 chip lands terracotta · 0.50 recovery card lands: "Author the sheet OR point at a folder that has one" — the ledger does not guess. |
| B09 | `ClaudeVerdictArtifact` | VERDICT — the four-line artifact. | 0.05 artifact opens · 0.20/0.44/0.64/0.86 the four lines stagger; last line holds through the outro. |
| B10 | `ClaudeComposerAsk` (`greeting: "Your turn."`) | HANDOFF — the paste-ready prompt, read aloud, then a three-item look-for rubric. | 0.04 greeting swaps to `Your turn.` · 0.12 the prompt types itself as the narration reads it · 0.60 terracotta send arms · 0.72 three-item rubric stacks in. |
| B11 | `ClaudeTitleOutro` | Title restate — poster serif with terracotta period, `@NikBearBrown`, mascot. | 0.10 title lands · 0.45 handle settles · 0.60 mascot lands, jingle plays out. No subline. |

## Portrait companion (9:16)

Each of the seven custom scenes is authored to read the video config and
re-flow: cards stack vertically, event bar/tables switch to full-width rows,
the terminal transcript keeps its 3840-tall body and drops its right chip
column into a fourth row per beat.

## Frame laws honoured

- COLD OPEN LAW: B00 opens on `ClaudeComposerAsk` with output lines populated.
- EXECUTIVE-SUMMARY LAW: B01 is `BrutalistHesitantWriter` with `lead_silence_s: 0.8`, ≥ 9 s.
- ILLUSTRATE LAW: UI appears only at B00, B09, B10, B11 — every other beat illustrates.
- ASK → RESULT LAW: the cold open shows the ask + its answer (result lines). The B07 diagram carries the paired prompt→queue→re-run receipt.
- SPARK-LINE LAW: every illustration beat carries the spark + one short serif line, top-left.
- HANDOFF LAW: B10 reads the prompt aloud and adds the three-item look-for rubric.
- OUTRO LAW / OUTRO-LOCK: `@NikBearBrown`, mascot lower area, no subline.
