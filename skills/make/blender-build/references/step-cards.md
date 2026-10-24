# The build record — `record.json`, `BUILD-STEPS.jsonl`, and what the gate reads

## Executive summary

**What this is.** The format of the record that lets a person rebuild a Blender model: one
`record.json` describing the model, its stages, its sources and what was verified, and one line
per step in `BUILD-STEPS.jsonl`.

**Why read it.** The record is only worth having if it can be believed. Every field below exists
because its absence lets a guide claim more than the evidence shows: a "step" with no recording
behind it, an interface route nobody followed, a "verified" that was never replayed.

**What the gate does with it.** `verify_breakdown.py` checks that each step's stated evidence
tier is backed by evidence that exists and has not changed, that corrections point at what they
corrected, that outside assets are credited, that every stage is shown from the same cameras, and
that the verification claims are true. It cannot tell whether a goal or a reason is *correct*.
The example is **not evidence**: replace every value.

## Folder

```
<model folder>/build-record/
  record.json            the model, stages, sources, credits, verification
  BUILD-STEPS.jsonl      one step card per line
  RECONSTRUCT.md         the guide (written by reconstruct_md.py)
  tape/                  live.jsonl, harvested-*.jsonl   (the commands, with replies)
  scripts/               the headless build scripts that ran (hash-tracked)
  milestones/<stage>/    milestone.json, census.json, views/<camera>.png
  reveals/               order.json files for any build-up animation
```

Paths inside the record are relative to this folder. Report the folder to Bear by absolute path.

## `record.json`

```json
{
  "schema_version": 1,
  "model": {
    "name": "west-end", "kind": "building",
    "built_by": ["Walker", "the Blender MCP (Claude)", "headless scripts"],
    "path": "/abs/path/west-end_v012.blend", "sha256": "<64 hex>",
    "census_signature": "<64 hex, from census.py on that file>", "blender": "5.1.2"
  },
  "units": "metres, unit scale 1",
  "stages": [
    {"id": "01-define", "title": "Define the project", "summary": "what it is for and what was gathered"},
    {"id": "04-blockout", "title": "Block out the building",
     "milestone": "milestones/04-blockout/milestone.json", "milestone_summary": "plain shaded overview"},
    {"id": "05-journey", "title": "Test the journey", "skipped_reason": "an asset has no route"}
  ],
  "sources": [
    {"id": "T1", "kind": "tape", "path": "tape/live.jsonl", "sha256": "<64 hex>"},
    {"id": "G1", "kind": "script", "path": "scripts/build_slice.py", "sha256": "<64 hex>"}
  ],
  "credits": [{"id": "C1", "what": "wood texture", "source": "polyhaven.com", "licence": "CC0"}],
  "comparison_views": ["CMP_ISO", "CMP_FRONT"],
  "reconstruction": {
    "replay":  {"status": "pass", "how": "replay.py on tape/harvested.jsonl: ran 16, skipped #14,#15,#18,#26 (file writes), #20 (failed when recorded), #19 (--skip: only reads a render); census.py compare: same signature",
                "census_signature": "<must equal model.census_signature>"},
    "by_hand": {"status": "done", "by": "Bear", "date": "2026-10-20", "module": "one window module",
                "note": "followed the Do lists in a fresh file; dimensions matched"}
  },
  "film": {"reveals": [{"order": "reveals/order.json", "labelled_in_film": true}],
           "told_as_history": ["S001", "S004"]}
}
```

`reconstruction.replay.status` is `pass`, `fail` or `pending`. `by_hand.status` is `done` or
`pending`. A `pass` replay must have produced the delivered model's census signature.

## A step card (one line of `BUILD-STEPS.jsonl`)

```json
{"id": "S014", "stage": "06-modules", "module": "window",
 "goal": "Build one window module with its origin at the lower corner",
 "start_state": "The blockout wall with an opening cut for the window",
 "operation": {
   "python": {"source": "tape", "ref": "tape/live.jsonl#31"},
   "gui": ["Add ▸ Mesh ▸ Cube (Shift+A) — then ... Location X 0, Y 0, Z 0.56",
           "Sidebar (N) ▸ Item tab ▸ Dimensions on Frame = X 1.2, Y 0.1, Z 1.4"],
   "gui_source": "draft", "no_gui_reason": "", "bl_idnames": ["mesh.primitive_cube_add"]},
 "settings": {"Dimensions": "1.2 x 0.1 x 1.4 m", "Origin": "lower corner"},
 "result": {"measured": {"dimensions_m": [1.2, 0.1, 1.4]}, "reply": "Code executed successfully: ..."},
 "why": "An origin at the corner makes every copy snap to the grid with one number",
 "tier": "recorded",
 "evidence": [{"path": "tape/live.jsonl", "seq": 31}],
 "repeats": {"rule": "one window per bay, 8 ft apart", "instances": 24, "table": "placements.csv"},
 "correction": {"of": "S012", "evidence": "tape/live.jsonl#29: Error ... 'Bone' has no attribute 'roll'"},
 "uses_external_asset": {"name": "wood texture", "credit_id": "C1"}}
```

- **`goal` and `why` are written by a person or an agent**, never drafted by the tool. `goal` is
  *what changed*; `why` is *the decision and the evidence for it* ("the corner origin makes copies
  snap", not "because it is good practice"). Each is at least three words.
- **`start_state` / `result.measured`**: refer to numbers from the census, not adjectives.
- **`operation.python`** points at the exact code that ran: a tape line (`path#seq`) or a script.
- **`operation.gui`** is the route through the interface. `gui_source` is `draft` (translated from
  the Python by `draft_steps.py`; **nobody has followed it**), `human` (a person did it), or `none`.
  If there is no interface route (bulk placement, mesh from raw vertex data) say why in
  `no_gui_reason` and give the script door.
- **`repeats`**: document one instance in full and the rule for the rest, with a placement table
  file or an explicit `listed` array. One complete example, then the rule.
- **`correction`**: a step that fixed an earlier one names it and quotes the evidence that
  prompted the fix (the error, the measurement). A failed command stays in the record with
  `excluded_from_procedure: true`.
- **`excluded_from_procedure`**: the command failed or was superseded; it is not part of what a
  person follows. It stays so the guide can say what went wrong.
- **`revisit`**: the step returns to an earlier stage on purpose (normally also a correction).
- **`needs_author`**: set by the drafter; lists the fields still to write. Delete as you write
  them. `--final` fails while it is non-empty.

## Evidence tiers

| Tier | Means | Evidence the gate wants | May be told as "what we did"? |
|---|---|---|---|
| `recorded` | a tape or transcript line shows the command and its reply | a tape/transcript path and line that exist; the Python ref resolves | yes |
| `scripted` | a project script ran; the steps are a translation of its calls | the script path (hash-tracked in `sources`) | yes |
| `inspected` | read from the finished file; nothing records how it was made | a census or milestone | no: it says what exists |
| `demonstrated` | redone afterwards to show the move | `demonstration_of` names the original step | only labelled as a demonstration |
| `inferred` | a plausible method, not evidence | none (the gate warns) | never |

## What the gate checks

| Area | Fails when |
|---|---|
| Record | model hash, census signature, builder, Blender version or absolute path missing; a stage id not like `04-blockout`; a source file missing or **changed since it was recorded** |
| Steps | duplicate id; stage unknown or going backwards without `revisit`/`correction`; `goal` or `why` missing or under three words; tier unknown; a recorded or scripted step with no resolvable Python ref; no interface route and no `no_gui_reason`; an inspected step with no census; a demonstration with no original; a result with no numbers, reply or note |
| Repeats | instances ≤ 1, no rule, and neither a table file nor a full `listed` array |
| Corrections | `of` is not another step, or no evidence |
| Assets | an `uses_external_asset` with no matching credit (id, what, source, licence) |
| Milestones | a view file missing or changed; **any stage missing a comparison view that others show**; the last milestone's signature is not the delivered model's |
| Reveals | an order with no `order_source`; an `explanatory` order not marked `labelled_in_film`; a `recorded` order whose items name non-steps, recorded/scripted-less steps, or are out of built order |
| Verification | replay `fail`; a `pass` whose signature is not the model's; a "done" by-hand check with no name, date and module |
| Guide | `RECONSTRUCT.md` first section is not "Executive summary", or has no "Verification status" |
| `--final` | any `needs_author`, any UNMAPPED line, a missing guide, **or neither a passing replay nor a by-hand check** |
| `--film` | any step in `film.told_as_history` that is not recorded or scripted |
| `--recensus` | the file's hash or census signature no longer matches the record (it changed after the record was written) |

Warnings you must answer in writing: inferred steps, untracked sources, interface translations
nobody has followed, stages without a milestone, no comparison cameras declared.

## Honest limits

The census sees objects, dimensions, placements, counts, modifier stacks, materials' Principled
values and bones. Objects named `CMP_*` (the fixed comparison cameras and their helpers) are recorded
but are not part of the signature or the totals, and a material that nothing uses is not counted
(it would not survive a save). It does **not** see vertex positions inside a mesh beyond counts and
dimensions, how a surface looks in a render, or anything outside Blender. Two builds with the same
signature agree on everything the census sees, not on everything.
