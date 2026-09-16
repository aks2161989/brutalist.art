# SCRIPT — Brutalist Command: art todo — Short (9:16)

**Persona:** Liam, in for Bear. Kokoro `am_onyx`. Register: Teardown.
**Channel:** @NikBearBrown. **Playlist:** Brutalist. **Runtime:** 116.33 s.

Retained narration is IDENTICAL to the parent's — no rewrites in this Short.
Beats B05, B06, B10 dropped; every other beat unchanged. See `CUT-PLAN.json`
for the editorial record.

## Beat-by-beat narration (Short cut)

**B00 — Cold open (ClaudeComposerAsk916, 10.96 s)**
> Hola, Liam. This is Liam, in for Bear. The ask — show me what is still open
> on my reel: which beats still need a clip, whether the machine renders it or
> a human drops it in, and what to type for each one.

**B01 — BLUF (BrutalistHesitantWriter916, 11.50 s, lead_silence 0.8 s)**
On-screen (types live, corrected once): `art todo / is a / list.` → `receipt.`

> Here is the whole idea in one breath. Art todo is not a list of shots you
> edit by hand. It is a receipt of shots you read from the machine. Change the
> beat sheet, run the command, watch the receipt update.

**B02 — FRAMEWORK · sheet → ledger (TodoPipeline916, 16.83 s)**
> The mental model is one arrow. On the left, beat sheet dot json — one entry
> per beat, with a shot block. In the middle, art todo. On the right, three
> files it writes: todo dot json for agents, STATUS dot markdown for you, and
> ToDo dot markdown for whoever owes a clip. Edit the sheet, not the receipts.

**B03 — FRAMEWORK 2 · the exact syntax (TodoCommand916, 11.63 s)**
> Four surfaces, three of them optional. Point it at a reel folder. Add
> --open for beats still empty. Add --method to filter to one lane. Add
> --json when an agent is on the other end. That is the whole command.

**B04 — WORKED EXAMPLE · live 0/5 run (TodoRun916, 15.17 s)**
> Here is a live run against a five-beat demo reel. Zero out of five filled.
> One line per beat: the id, the status, the fill method, who owes it, and
> the pantry slot it expects. The three human-owed rows carry the terracotta
> chip — they are the ones you drop clips for.

**B07 — THE AGENT LOOP · --method + --open (TodoAgentLoop916, 15.96 s)**
> This is why the ledger exists. Add --method manim --open and it prints only
> the manim beats that are still empty. An agent walks that list, renders
> each one, drops the mp4 at the named slot, and re-runs the command. When a
> beat is filled, it drops off the list on its own. The ledger is the queue.

**B08 — FAILURE + RECOVERY · no sheet (TodoFailure916, 15.83 s)**
> One failure worth knowing. Point it at a folder that has no beat sheet, and
> it stops on the first line — no ledger, exit code one. The recovery is not
> a flag. Author the sheet, or point the command at the folder that actually
> has one. The ledger refuses to guess. That refusal is the feature.

**B09 — VERDICT (ClaudeVerdictArtifact916, 13.88 s, lead_silence 0.4 s)**
> So — art todo. A derived receipt of the beat sheet. Three outputs from one
> read. Five fill lanes, two of them the pipeline handles for you. A
> method-and-open filter that turns the ledger into an agent's work queue.
> And it fails loud when the sheet is missing.

**B11 — OUTRO (ClaudeTitleOutro916, 4.58 s)**
> Brutalist Command: art todo. Liam, in for Bear. Thanks for watching.

## Cadence and closes

- IN-FOR-BEAR LAW: B00 introduces Liam-in-for-Bear; B11 signs off the same.
- BLUF at B01 sets the misconception→truth flip inside the first ~22 s.
- One safety limitation preserved (B08 refuse-loud) per Shorts prompt.
- No Your Turn beat — long-form CTA (parent B10) intentionally dropped;
  fellows can watch the 16:9 long / vertical companion for the paste-ready
  prompt and look-for rubric.
