# Where the steps come from — the source ladder, and what to do when there is no record

## Executive summary

**What this is.** A ranking of the places a build's steps can be recovered from, how to harvest each
one, and what you may honestly say about a step depending on where it came from.

**Why read it.** Most models are finished before anyone thinks of documenting them. The question is
always the same: *what do we actually have?* A tape of every command is proof. A finished `.blend` is
only proof of what exists. The ladder keeps the record from claiming the first when it only has the
second.

**What it found.** On the real mascot build (Bear's MCP run, 2026-10-06) the headless `claude -p`
transcripts held every Blender call, its stated reason (`user_prompt`) and its reply: 22 scene-changing
commands, one of which failed and was corrected. `tape.py harvest` recovered all of them. The two
mascot routes came out with the same 108 triangles and the same nine-bone rig but different
structure: nine separate part meshes plus a camera and a light (12 objects) from the MCP, one joined
mesh (2 objects) from the script. `census.py compare` said so, and the totals alone (triangles,
bones) would not have. Without the transcripts, only the finished file would have remained.

## The ladder, most trusted first

| Rung | Source | How to get it | What it proves | Tier |
|---|---|---|---|---|
| 1 | **A live tape** recorded while building | `tape.py code|run|call` through the add-on socket | every command, reason, reply and duration | `recorded` |
| 2 | **Claude Code transcripts** of the build | `tape.py harvest <transcript.jsonl…>` (stream-json from `claude -p`, or project transcripts under `~/.claude/projects/`) | every Blender tool call and Bash-run Blender command, with replies | `recorded` |
| 3 | **Headless build scripts** in the project (git-tracked) | list them in `record.sources`, hash them; `scripts/` | exactly what the script does; run order is yours to establish | `scripted` |
| 4 | **Versioned saves** (`name_v001.blend`, `name_v002.blend` …) | census each; `census.py compare` consecutive ones | what changed between saves, not how | `inspected` |
| 5 | **Build logs / handoff prose** (`BUILD-LOG.md`, `HANDOFF.md`) | read; quote | what the builder said they did | a claim, not a record: tier `inspected` at best, and only if the file bears it out |
| 6 | **Scripts embedded in the `.blend`** | `census.py` lists `bpy.data.texts` with hashes | that a script travelled with the file | `inspected` |
| 7 | **The finished file only** | `census.py census` | what exists | `inspected` |

A step you reason out from rung 7 is `inferred`. It is never told as history.

## What each rung can and cannot say

**Tapes and transcripts** say what was *sent* and what came *back*. They do not prove the saved file
matches (the builder may have changed things in the GUI, or saved over it): census the file and
compare. Transcripts carry no wall-clock time unless the line has a `timestamp`; the tape records
`t_utc: null` rather than inventing one. A transcript's `user_prompt` field (on the MCP's execute
call) is the builder's own stated reason: a good first draft of the card's goal, never a substitute
for the `why`.

**Scripts** can be run again (the replay check, below), which is stronger than reading them. A script
read from disk *now* may have changed since the build: `tape.py harvest --resolve-scripts` marks
that `script_read: "now"`, and `record.sources` hashes pin the version you mean.

**Versioned saves** are the best defence against a missing tape: they give you milestones for free.
Census and render each (`census.py milestone`) from the **same comparison cameras**.

## Walker and the Blender MCP in this repository

- **Walker's rules** for building game assets are `books/walker/BLENDER.md`: names, origins, applied
  scale, `EXPORT`/`WORK` collections, the build order (blockout → engine test → deformation geometry →
  detail → game-res mesh → UVs/shading/triangulation → bake and verify), and the validation scripts in
  `books/walker/scripts/blender/`. A walker build should already satisfy them; the build record says
  so by listing the validator run as a step.
- **The MCP route that works here** (Blender 5.1.2): the add-on is started by Blender, the stdio MCP
  server is not necessarily registered in the Claude session, and the socket speaks one JSON object per
  request on port 9876. `tape.py` speaks the same protocol, so a build driven through it is recorded
  without the MCP server. The add-on **has no authentication**: its socket runs any Python. Run it only
  for the build, then disable the add-on or quit Blender, and say so.
- **Never credit a tool that did not run.** If the guide says "the MCP built the rig", a tape or a
  transcript must show it. When part of a build ran as parallel headless workers (as in the SEIS bot),
  and only assembly went through the MCP, the guide says that.

## When there is no record

1. Say so in the guide's executive summary. The guide then describes **what the file contains**, not how it was made.
2. Census the file; write `inspected` steps for the structure (collections, parts, materials, rig).
3. Offer a **demonstration** rebuild if useful: build one module fresh, **recording it on a tape**, and
   label every step `demonstrated`, with `demonstration_of` naming what it stands for. The film calls it
   "a rebuild of one module to show the method", never "how we built it".
4. If a session would settle the question, write the exact session for Bear to run and record (see the
   two-stage rule); do not fake one.

## Replay: the check that a record is a recipe

A record is a recipe only if it can be run. `replay.py` rebuilds the model from a tape in a fresh Blender
and censuses the saved result:

```bash
SK=brutalist.art/skills/make/blender-build/scripts
"$BLENDER" -b --factory-startup --python $SK/replay.py -- REC/tape/harvested.jsonl \
    --out /private/tmp/replay/rebuilt.blend --census REC/replay-census.json --report REC/replay-report.json
python3 $SK/census.py compare REC/milestones/11-render-export/census.json REC/replay-census.json
```

- It runs every tape line that changed the scene, succeeded and has code, in order, each in a fresh
  namespace (`--shared-namespace` if a command uses a variable from an earlier one), starting from
  Blender's factory scene, which is where a recorded MCP session starts. A command that raises **stops
  the replay**: the record is not yet a recipe, and the report names the line.
- **It will not run a command that writes files.** A replay re-executes what the tape did, and recorded
  commands save the `.blend` to its real path, export glTFs, render images. Replaying those would overwrite
  the deliverable being checked. Anything that looks like a write is skipped and listed with the reason
  (a command that both builds and writes is skipped whole; the census comparison shows whether anything
  was lost). `--allow-writes` exists for a copy of the project and nowhere else.
- A command that only *reads* a file that is not on this machine (a render it inspected) will fail the
  replay; `--skip N` leaves it out, and the decision goes into `reconstruction.replay.how`.
- The result is censused **after saving and reopening the file**, because a deleted object's mesh and
  material linger in memory with no user and are dropped on save (the factory scene carries a "Material"
  and a "Dots Stroke" that would otherwise show up as differences).

`same_signature: true` and no `DIFF` lines: `reconstruction.replay.status = "pass"`, with the signature and
a `how` that names the skipped lines. Any difference: `fail`, and the `DIFF` lines say where the record and
the model part company. A replay proves the *tape* rebuilds the model. It does not prove the interface
steps work (that is the by-hand check) and it cannot judge how the model looks.

**Verified on a real build.** Replaying the harvested transcripts of Bear's MCP mascot run
(2026-10-06): 16 of the 22 scene-changing commands ran; 4 were skipped as file writes (two renders, two
saves/exports), 1 failed when recorded (the armature attempt that was then corrected), 1 only read a render
that is no longer on disk (`--skip`). The rebuilt model matched the delivered `claude_mascot_mcp.blend`
**exactly**: same signature, 12 objects, 72 vertices, 108 triangles, 9 bones, 2 materials. Nothing in his
project folders was touched; the replay wrote to a scratch folder.

## The by-hand check

Pick one module (one window, one bone chain, one material). In a **fresh** file, follow only that
module's `Do` lists, in the interface. Census the result and compare it with the same module in the
delivered model. Record who, when, which module, and what differed: `reconstruction.by_hand`. Fix
the `Do` list wherever you had to guess, and change its `gui_source` from `draft` to `human`. Never mark
this done for a step nobody followed.
