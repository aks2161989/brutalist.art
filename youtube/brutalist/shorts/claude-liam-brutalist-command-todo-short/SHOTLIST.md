# SHOTLIST — Brutalist Command: art todo — Short (9:16)

Derivative of `claude-liam-brutalist-command-todo/vertical` (2160×3840 native
portrait, 12 beats, 167.9 s). This Short keeps 9 of the 12 beats and drops
B05, B06 and B10 to focus on the high-level pitch. All nine kept beats are
Remotion-rendered on cream (`#FAF9F5`) with terracotta (`#D97757`) as the one
accent. Custom illustrations registered under folder `ClaudeLiamCommandTodo`
in `Root.tsx` (portrait `*916` variants).

| # | Beat | Pattern (916) | Purpose | On-screen event lattice |
|---|------|---------------|---------|-------------------------|
| 1 | B00 | `ClaudeComposerAsk916` | Cold open — the ask, answered with a three-line output. | 0.00 cream page + `Hola, Liam` serif greeting · 0.14 command `art todo my-reel/ --open` types in · 0.60 send arms terracotta · 0.76 three result lines stagger — the answer is on screen when the ask lands. |
| 2 | B01 | `BrutalistHesitantWriter916` (seed `todo-4828`) | BLUF — "art todo is a list" flipped to "art todo is a receipt". | Component-driven: writer types the three-line phrase, pauses, terracotta marks `list`, replacement `receipt` types in. `lead_silence_s: 0.8`. Font 240, line spacing 2.6. |
| 3 | B02 | `TodoPipeline916` | FRAMEWORK — one arrow: `beat_sheet.json` → `art todo` → three receipts. | 0.10 left node lands: `beat_sheet.json` · 0.30 middle node lands: `./art todo <reel>` · 0.55 right stack lands (three cards: `todo.json`, `STATUS.md`, `ToDo.md`) with the `ToDo.md` card lit terracotta · 0.88 tagline settles: "Edit the sheet, not the receipts." |
| 4 | B03 | `TodoCommand916` | FRAMEWORK 2 — the exact syntax and every flag. | 0.08 dark terminal bar lands with `$ ./art todo <reel> [flags]` · 0.30 `--open · only beats still needing a clip` · 0.55 `--method <name> · filter to one lane (manim \| remotion \| ai-video-prompt \| historical-image \| user-capture)` · 0.80 `--json · print todo.json to stdout` lit terracotta. |
| 5 | B04 | `TodoRun916` | WORKED EXAMPLE — a live 0/5 run. | 0.05 terminal card `$ ./art todo demo/example-reel` · 0.18 header `0/5 filled → todo.json + STATUS.md + ToDo.md` · 0.32 five rows (B00 remotion / B01 manim / B02 historical-image / B03 user-capture / B04 ai-video-prompt) stagger with the three human-owed rows carrying the terracotta chip. |
| 6 | B07 | `TodoAgentLoop916` | THE AGENT LOOP — why the ledger exists. | 0.05 command bar with `--method manim --open` filter lit terracotta · 0.25 QUEUE card: B01 · manim/B01.mp4 · 0.45 RENDER + DROP card · 0.68 RE-RUN card refreshes the receipt · 0.88 QUEUE empty with terracotta "filled — drops off" caption. |
| 7 | B08 | `TodoFailure916` | FAILURE + RECOVERY — the "no beat_sheet.json" refusal. | 0.05 terminal `$ ./art todo demo/empty-reel` · 0.25 red-tint stderr `[todo] no beat_sheet.json in .../empty-reel` · 0.45 terracotta `exit 1 · refused` chip · 0.70 recovery card: "Author the sheet, or point at a folder that has one." |
| 8 | B09 | `ClaudeVerdictArtifact916` | VERDICT — five-line recap. | 0.05 artifact opens · 0.22/0.44/0.64/0.84 lines land: (1) derivation not authorship · (2) one read → three outputs · (3) five fill lanes; two pipeline, three human · (4) `--method + --open` filter turns the ledger into an agent's queue · (5) refuses loud when the sheet is missing. |
| 9 | B11 | `ClaudeTitleOutro916` | Title restate — poster serif with terracotta period, `@NikBearBrown`, mascot slug-seeded. | 0.10 title lands · 0.45 handle settles · 0.60 holds clean on cream. No subline. |

## Dropped (and where the material now lives)

| Dropped | Rationale for this cut |
|---------|------------------------|
| B05 `TodoEntry916` | Six-field dictionary anatomy is generic internals — belongs in the 16:9 long, not the Short's high-level pitch. |
| B06 `TodoMethods916` | The five lanes are already named on-screen in B03 (`--method <name>` effect chip) and demonstrated in B04's five rows; the separate table is redundant. |
| B10 `ClaudeComposerAsk916` (Your Turn) | Extended CTA reads the full assignment aloud; a detailed CTA can be cut per the Shorts prompt. B09 verdict + B11 sign-off close cleanly. |

## Frame laws honoured (Short cut)

- COLD OPEN LAW: B00 opens on `ClaudeComposerAsk916` with output lines populated.
- EXECUTIVE-SUMMARY LAW: B01 is `BrutalistHesitantWriter916` with `lead_silence_s: 0.8`, ≥ 9 s.
- ILLUSTRATE LAW: UI appears only at B00, B09 (verdict artifact page counts as UI) and B11 — B02, B03, B04, B07, B08 illustrate.
- SPARK-LINE LAW: every illustration beat carries the spark + one short serif line, top-left (with the portrait-only +60 CSS bump so the baseline-aligned flex layout clears SAFE916.y=192 — see `feedback_command_todo_sparkline_portrait_bump`).
- HANDOFF LAW: **waived for this Short** — long-form Your Turn (B10) dropped per the "cut a detailed CTA" clause of the Shorts prompt.
- OUTRO LAW / OUTRO-LOCK: `@NikBearBrown`, mascot lower area, no subline.
- SHORTS LAW: measured 116.33 s, strictly under 180 s ceiling.
