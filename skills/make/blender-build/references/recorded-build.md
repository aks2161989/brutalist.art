# Historical build record mode

Read this only for an explicit original-build history, record, replay or build-breakdown request.
The default image-based lesson lives in [SKILL.md](../SKILL.md) and does not require this workflow.

# blender-build — what were all the steps, so a human could redo them

```text
blender-build /path/to/model-folder              # recover the record of a build that already happened
blender-build /path/to/model-folder record       # set up recording for a build that is starting now
blender-build /path/to/model-folder film         # the breakdown film, from a finished record
```

An **agent-driven builder**, like [godot-waikthrough](../../godot-waikthrough/SKILL.md). It does not
model anything. The model is built by Walker (`books/walker/BLENDER.md`), by the Blender MCP, by
headless scripts, or by hand. This skill answers the question that comes after: **what were all the
steps used to make the thing, written so that a person could repeat them?**

It is the second of two **companion films** for any model:

| | [building-walkthrough](../../building-walkthrough/SKILL.md) | **blender-build** (this) |
|---|---|---|
| Question | what is the finished place or asset like to experience? | how was it modelled, textured, lit and filmed? |
| Footage | Blender renders from a measured camera route | the real Blender window, milestone renders from fixed cameras |
| Spine | the route | the stages |
| Honesty | what the model is and is not | how each step is known, and what was checked |

Plan both while you build: the camera route shows where detail matters, and the recorded stages are the
material for the breakdown.

Read this file, then [step-cards.md](step-cards.md) (the record format and what the gate
checks), [source-ladder.md](source-ladder.md) (where steps come from, and what to do with no
record), [gui-translation.md](gui-translation.md) (Python to the mouse) and
[breakdown-film.md](breakdown-film.md) (stages, the film, the construction reveal). For the
film's chassis read the [lecture](../../lecture/SKILL.md) skill; for its voice, endings and rules, the
toolkit's `CLAUDE.md` and [OUTRO-LOCK.md](../../../../OUTRO-LOCK.md).

## The one test

A stranger with Blender, the model's references and this guide should be able to **get the same model**,
and the guide should say honestly *how sure it is of each step*. "Same model" is checked, not hoped:
a script replay reproduces the model's census signature, and a person has followed at least one module
through the interface. Where neither has happened, the guide says so in its first screen.

Films show only what was actually done and recorded (Bear's law for every Brutalist film). A step that was
not recorded is inspected, demonstrated or inferred, and the film says which.

## 0. What do we have? (decide the route)

Ask what record exists, in this order of trust ([source-ladder.md](source-ladder.md)):

1. a **live tape** (a build that was run through `tape.py`),
2. **Claude Code transcripts** of the build (`claude -p` stream-json, or project transcripts),
3. **headless build scripts** in the project,
4. **versioned saves** of the model,
5. **build logs and handoff notes**,
6. scripts **embedded in the `.blend`**,
7. **the finished file only**.

Rungs 1–3 give `recorded` or `scripted` steps. Rungs 4–7 give `inspected` ones. A step reasoned out from
the finished file is `inferred`. Never claim a higher rung than you have. If a build starts now, set up
recording first (§1) and the rest is easy.

## 1. Record while you build (when the build has not happened yet)

- **Tape every command.** Drive Blender through `tape.py`, not a bare socket: every command, its reason
  (`--why`), its reply and its duration land in `build-record/tape/live.jsonl`.

  ```bash
  SK=brutalist.art/skills/make/blender-build/scripts
  python3 $SK/tape.py code "import bpy; print(len(bpy.data.objects))" --tape REC/tape/live.jsonl --stage 04-blockout --why "count what exists"
  python3 $SK/tape.py run  build_part.py --tape REC/tape/live.jsonl --stage 06-modules --label "window module"
  ```

  It speaks the Blender MCP add-on's wire protocol directly (port 9876, no MCP server needed). The add-on
  has **no authentication**; enable it for the build, then disable it or quit Blender, and say so.
- **Save increments**, `name_v001.blend`, `name_v002.blend`, one per stage (Walker's rule: never rely on
  undo, and work on copies).
- **Fix the comparison cameras** (`CMP_ISO`, `CMP_FRONT`, …) at the first blockout and never move them. Name them
  `CMP_*`: the census records them but leaves them out of the signature and totals, so adding them to a file does
  not change what the file says about itself.
  At each stage run `census.py milestone`, which renders them with Workbench and writes the census:

  ```bash
  "$BLENDER" -b name_v003.blend --python $SK/census.py -- milestone --stage 04-blockout \
      --out-dir REC/milestones/04-blockout --views CMP_ISO,CMP_FRONT --blend-ref /abs/name_v003.blend
  ```
- **Explain as you go.** The *why* is easiest to write at the moment of the decision.

## 2. Recover the record (when the build already happened)

```bash
# transcripts → a tape (every Blender MCP call and Bash-run Blender command, with its reply)
python3 $SK/tape.py harvest session/turn1.jsonl session/turn2.jsonl --out REC/tape/harvested.jsonl
python3 $SK/tape.py show REC/tape/harvested.jsonl
# census the model, and every saved version you have
"$BLENDER" -b final.blend --python $SK/census.py -- census --out REC/milestones/11-render-export/census.json
```

Hash every source you rely on (tapes, scripts) into `record.json` so a later edit is noticed. A transcript
has no wall-clock time unless a line carries one; the tape says `null` rather than invent it. If the model
was built partly by parallel headless workers and only assembled through the MCP (as the SEIS bot was), the
record says that. If nothing but the finished file exists, the guide describes **what the file contains**,
not how it was made ([source-ladder.md](source-ladder.md), "When there is no record").

## 3. Draft the steps, then author them

```bash
python3 $SK/draft_steps.py REC/tape/harvested.jsonl --out REC/BUILD-STEPS.jsonl \
        --tape-ref tape/harvested.jsonl --stage-map "1-4:01-define,5-18:04-blockout,19-26:09-rig"
python3 $SK/draft_steps.py gui REC/tape/harvested.jsonl --seq 4       # see one translation
```

The drafter reads each scene-changing command's Python and produces a **card**: the exact code (a pointer
into the tape), a **draft** interface route, the settings used, and the reply. A failed command becomes a
failed-attempt card; the next success with the same stated purpose is recorded as its correction. It never
drafts judgment: **you write `goal` and `why`** (what changed; the decision and its evidence), clear
`needs_author`, delete probe and clean-up lines, and replace each `UNMAPPED` and `~` line. See
[gui-translation.md](gui-translation.md) for what it does and does not know. Interface routes
stay `gui_source: "draft"` until someone has followed them.

Document **one instance in full and the rule for the rest** (`repeats`: the rule, the count, a placement
table). Bulk placement, mesh built from raw vertex data and similar steps have no honest mouse route: say
so (`no_gui_reason`) and point at the script door. Credit every outside asset.

## 4. Verify the recipe

A record is a recipe only if it can be run.

- **Replay** (tapes, scripts): `replay.py` rebuilds the model from the tape in a fresh Blender, in order,
  and censuses the saved result; `census.py compare` against the delivered model. Same signature and no
  `DIFF` lines → `replay: pass` with the signature and a `how` that names what was skipped. A difference →
  `fail`, and the `DIFF` lines say where record and model disagree. **It refuses to run commands that write
  files** (they would overwrite the deliverable); `--skip N` leaves out a command that only reads a file that
  is gone. Verified on Bear's real mascot MCP run: 16 recorded commands rebuilt the delivered model exactly.

  ```bash
  "$BLENDER" -b --factory-startup --python $SK/replay.py -- REC/tape/harvested.jsonl \
      --out /private/tmp/replay/rebuilt.blend --census REC/replay-census.json --report REC/replay-report.json
  python3 $SK/census.py compare REC/milestones/11-render-export/census.json REC/replay-census.json
  ```
- **By hand**: a person (or an agent driving the real interface) follows one module's `Do` list in a fresh
  file; census; compare with that module in the delivered model. Record who, when, which module. Fix
  anything they had to guess and mark those steps `human`. **Never mark this done for a step nobody
  followed**, and never present a draft route as verified.
- **Recensus** guards the other direction: `verify_breakdown.py --recensus` re-measures the model and
  fails if it changed after the record was written.

The census sees objects, dimensions, placements, counts, modifier stacks, materials and bones. It does not
see vertex positions inside a mesh beyond counts and dimensions, or how a surface renders.

## 5. Write the guide

```bash
python3 $SK/reconstruct_md.py --record REC/record.json --steps REC/BUILD-STEPS.jsonl --out REC/RECONSTRUCT.md
```

`RECONSTRUCT.md` opens with an **executive summary** (what this is, why read it, what the record found and
did not do), then the verification status, what to have before starting, **the two doors** (the script door:
exact, run the recorded Python; the hands door: the interface, one module at a time), one section per stage
with its milestone image and each step as a card (tier, interface route, settings, measured result, why,
corrections, repeats, credits), and a closing section on what the guide cannot tell you. Every claim of
certainty is generated from the record, so a guide cannot say more than the record holds. Paths inside it are
relative; report the file to Bear by absolute path.

## 6. The breakdown film

Built through the [lecture](../../lecture/SKILL.md) skill with `RECONSTRUCT.md` as the source document
(best-beat law, SHOW-THE-THING law, Liam in for Bear, the lecture spine and the channel's regular outro):
`<model folder>/youtube/claude-liam-lecture-<model>-build/`. **Acts follow the stages; each stage's
milestone is its establishing visual.** The full rules are in [breakdown-film.md](breakdown-film.md):

- every step explained as **goal, starting state, operation, key settings, result, reason**;
- the **real Blender window**, panels enlarged, settings held long enough to read; native 4K captures;
- **one complete example of repeated work, then accelerate** (the `repeats` rule and table);
- the **same comparison cameras** at every stage;
- **corrections shown with the evidence that prompted them**;
- the narrator tells as history only `recorded` and `scripted` steps; a rebuild made for the film is
  labelled a **demonstration** on screen and aloud;
- **a build-up animation states its order**: `recorded` (each piece tied to the step that built it) or
  `explanatory` (labelled in the film as not the order it was modelled in). `reveal.py` writes the order
  source into the file; the gate checks it;
- credits for reused assets, kept apart from the original work;
- a company or tool shown visually is its **logo** (toolkit rule 11), and the Blender window itself when the
  tool is the subject; a person is a **Professor Bear portrait**, never an icon (rule 9); the voice is Liam
  as the toolkit defines it, never re-decided; no video numbers or stage totals in viewer-facing text
  ("stage four of eleven" dates the film: name the stage).

Do not credit a tool that did not run. If the guide says Walker or the MCP built it, the tape or a
transcript shows it.

## 7. Gate, hand off

```bash
./brutalist.art/art blender-build --check REC/record.json            # the record
./brutalist.art/art blender-build --check REC/record.json --final    # + judgment written, nothing UNMAPPED, verified
./brutalist.art/art blender-build --check REC/record.json --film     # nothing inferred is told as history
./brutalist.art/art blender-build --check REC/record.json --recensus # the model still matches the record
```

The gate is read-only. It checks that every tier is backed by evidence that exists and has not changed,
that corrections and repeats are stated properly, that outside assets are credited, that every stage is shown
from the same cameras, that a recorded reveal follows the recorded order, and that the verification claims are
true. It **cannot** tell whether a goal or reason is correct, whether an interface route works, or whether the
model is good.

**Cowork stage** (higher effort; the two-stage rule in `books/CLAUDE.md`): recover or set up the record, author
the cards, run the replay (free) and the census, write `RECONSTRUCT.md`, lay out the film (`ACTS.md`,
`SHOTLIST.md`, `FACTCHECK.md`, `PROMPTS.md`, `make_sheet.py`, narration, the Blender captures that already
exist), write `BUILD-PROMPT.md` (absolute paths; commands as run from `books/`; the renders, audio, `art run`,
`art final`, gates; the traps below; the STOP line) and give Bear the Claude Code prompt from `books/CLAUDE.md`
"Two-stage builds". Never say a film is built when only the layout is done. **Claude Code stage:** audio,
renders, review cut, `art final`, every gate to PASS. Free steps run without approval gates; publishing and
paid generation never do.

### The tests only people can run (never fabricate)

- **Followed by hand**: someone rebuilds a module from the `Do` list in a fresh file (see §4).
- **Understood**: someone who has not seen the model watches the film and says what they would do first.
  Until both are done, the report says so.

## Traps already met

- **`hasattr(bpy.ops.mesh, "anything")` is always true**: operators are looked up lazily. A name-checker built
  on it passed vacuously until a deliberately wrong name was added and still passed. Ask for the operator's RNA
  type, and print how many names were actually checked against how many exist.
- **A "check" that iterates `Modifier.__subclasses__()` found no classes** and verified no properties. The real
  check adds each modifier and constraint to a scratch object and reads its properties.
- **`keyframe_insert()` ignores the default-interpolation preference** (Blender 5.1.2): set interpolation and
  easing on the F-curve keys, through the slot's channelbag in 5.x.
- A long-lived MCP Blender **caches helper modules** between calls; a re-run can execute stale code.
- Rendering many Blender processes at once on the Mac drove it into swap (about 7 GB each for a big figure);
  render one or two at a time from a copy of the `.blend`.
- A headless render that opens a `.blend` the GUI Blender just saved **into the project folder** stalled:
  copy it to a scratch folder and render from there.
- The two mascot routes (MCP parts versus a script's one mesh) had the same triangle count and the same rig and
  different structure. Compare structure, not totals.

## Deliverables

The record folder by absolute path (`record.json`, `BUILD-STEPS.jsonl`, `RECONSTRUCT.md`, tapes, milestones),
the gate output with every warning, the verification status (replay, by hand), the count of steps by tier, how
many interface routes are still drafts, the open `UNMAPPED` lines, and for the film its 4K MP4 (absolute path
and a quoted `open` command). No upload, publish or Git push is implied.
