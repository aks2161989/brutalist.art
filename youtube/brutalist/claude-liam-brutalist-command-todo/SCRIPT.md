# SCRIPT — Brutalist Command: art todo

**Persona:** Liam, in for Bear. Kokoro `am_onyx`. Register: Teardown.
**Channel:** @NikBearBrown (Bear's channel; Liam substitute — IN-FOR-BEAR LAW).
**Playlist:** Brutalist.

The one idea: `art todo` never invents work — it reads your `beat_sheet.json`,
looks at the files on disk, and writes a **derived** ledger of what is still
open, who has to close it, and how. The beat sheet is the heart. The ledger is
a receipt.

## Beat-by-beat narration

**B00 — Cold open (ClaudeComposerAsk)**
> Hola, Liam. This is Liam, in for Bear. The ask — show me what's still open on
> my reel: which beats still need a clip, whether the machine renders it or a
> human drops it in, and what to type for each one.

**B01 — BLUF (BrutalistHesitantWriter, ≥9 s)**
Final overview (typed live, corrected once):
> `art todo` is where I write my list of shots.
> — becomes —
> `art todo` is a receipt of the beat sheet I already wrote.

Narration:
> Here is the whole idea in one breath. `art todo` is not a to-do list you edit
> — it is a receipt of the beat sheet you already wrote. Change the sheet, run
> the command, watch the receipt update. That is the whole shape.

**B02 — FRAMEWORK · beat sheet → ledger**
> The mental model is one arrow. On the left, `beat_sheet.json` — one entry per
> beat, with a `shot` block. In the middle, `art todo`. On the right, three
> files: `todo.json` for agents, `STATUS.md` for you, `ToDo.md` for whoever
> owes a clip. Edit the sheet, not the receipts.

**B03 — FRAMEWORK 2 · the exact syntax**
> Four flags, all optional. Point it at a reel folder. Add `--open` for beats
> still empty. Add `--method` to filter to one lane — manim, remotion,
> ai-video-prompt, historical-image, user-capture. Add `--json` when an agent
> is on the other end. That is the whole surface.

**B04 — WORKED EXAMPLE · run it**
> Here is a live run against a five-beat demo reel. Zero out of five filled.
> One line per beat: id, status, method, who, and the pantry slot it expects.
> The prompt column is a search seed — the source for it is the beat itself.

**B05 — ANATOMY · one entry, six fields**
> Under the hood, each beat is one small dictionary. `status` is filled or
> needs-fill, decided by what is on disk. `method` and `who` come from the
> beat's `shot.type` and `shot.source`. `slot` is the filename the pantry
> expects. `prompt` and `label` are seeds — they teach whoever fills it what
> the beat is for.

**B06 — MECHANISM · the five fill lanes**
> Five ways a beat gets filled, and the sheet decides which. Remotion and
> Manim are pipeline lanes — the machine renders them. Historical image and
> user capture are on you. Ai-video-prompt is the fallback when nothing is
> annotated — the ledger drops a search seed so you are not staring at a
> blank. The last two never render themselves — the receipt tells you who owes
> the clip and where to drop it.

**B07 — THE AGENT LOOP · --method manim --open**
> This is why the ledger exists. Add `--method manim --open` and it prints
> only the Manim beats that are still empty. An agent walks that list, tries
> to render each one, drops the mp4 at the named slot, and reruns. The receipt
> refreshes. When a beat is filled, it falls off the list on its own.

**B08 — FAILURE + RECOVERY · no beat_sheet.json**
> One failure worth knowing. Point it at a folder that has no
> `beat_sheet.json` and it stops on the first line — no ledger, exit code one.
> The recovery is not a flag. Author the sheet, or point the command at the
> folder that actually has one. The ledger refuses to guess.

**B09 — VERDICT (ClaudeVerdictArtifact)**
> So — `art todo`. A derived receipt of `beat_sheet.json`. Three outputs from
> one read. Five fill lanes, two of them the pipeline handles for you. A
> `--method --open` filter that turns the ledger into an agent's work queue.
> Fails loud when the sheet is missing. Edit the sheet, not the receipt.

**B10 — HANDOFF · Your Turn (ClaudeComposerAsk)**
> Your turn. Paste this into Claude Code, pointed at any brutalist reel you
> have on disk: run art todo on this reel folder, then walk the --method
> remotion --open list and render each one, and stop and tell me which beats
> still need a human. Look for whether it names the slot filenames — that is
> how you know it read the ledger and not the sheet.

**B11 — OUTRO (ClaudeTitleOutro)**
Silent under the jingle. Voice sign-off in B11's narration:
> Brutalist Command: art todo. Liam, in for Bear. Thanks for watching.
