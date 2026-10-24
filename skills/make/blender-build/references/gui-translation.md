# From Python to the mouse — what the drafter knows, and what it does not

## Executive summary

**What this is.** How `draft_steps.py` turns the Python a build ran into "what a person does in
Blender's interface", what it covers, and how to finish and verify the result by hand.

**Why read it.** A tape is exact but unreadable to someone learning Blender, and a hand-written
walkthrough is readable but can drift from what was really done. The drafter gives you both: a
first pass in plain steps taken from the exact commands. It is a *draft*. Nobody has followed
these menu paths click by click, and the tool says so on every step.

**What it found.** On the 22 real scene-changing commands of Bear's mascot MCP build, the drafter
produced 21 cards (one command failed and was kept as a failed attempt), covering every cube,
dimension, rename, transform-apply, material and render setting. One line is UNMAPPED
(`bpy.data.images.load`, the build inspecting one of its own renders) and 28 are approximate,
mostly Python properties on armature bones and helper values it could not fold. Those need a person. The interface
map's operator, modifier, constraint and property **names** were checked against the installed
Blender 5.1.2: 94 operators, 23 modifier types, 13 constraint types and 97 property names, all
present; the check itself was tested to fail on a deliberately wrong name. The **menu paths and
labels** were written from the manual and the 4.2–5.x interface and were not checked in the
application.

## What it translates

| Python | Becomes |
|---|---|
| `bpy.ops.<module>.<operator>(…)` for 94 listed operators | the menu route and shortcut, with the call's arguments as the Adjust Last Operation panel values |
| `obj.dimensions / location / rotation_euler / scale = …` | Sidebar (N) ▸ Item tab, with rotation converted from radians to degrees |
| `obj.name = …`, `obj.data.name = …` | rename (F2, Outliner double-click), object data name field |
| `obj.modifiers.new(name, type)` and `mod.<prop> = …` | Add Modifier ▸ menu ▸ type, with each property under its interface label (23 types) |
| `obj.constraints.new(type)` and `c.<prop> = …` | Add Object Constraint ▸ menu ▸ type, with interface labels (13 types) |
| `bpy.data.materials.new`, `bsdf.inputs['X'].default_value = …`, `obj.data.materials.append` | Material tab: New, Surface ▸ X, Browse Material |
| `scene.render.*`, `scene.camera`, unit settings, shading, camera data | the Properties-editor location of each (54 paths) |
| `for`, `if`, helper `def`s that change the scene | "Repeat for each …", "If …", "Do the helper step …" with its arguments |
| `bpy.data.objects.remove`, `…collections.new`, `….link` | delete, New Collection, drag in the Outliner |

It folds constants (`math.radians(90)`, tuples, arithmetic) so a card can say "Rotation X 90°".
Where it cannot (a value computed earlier from other variables) it prints the Python expression, never
a guess. **Numbers are metres at unit scale 1** unless the census says otherwise.

## What it marks instead of guessing

- `UNMAPPED: <source>  [why]` — an operator, modifier, constraint or call not in `gui_map.py`.
  Translate it by hand, or write `no_gui_reason`.
- `~ …` (approximate) — a Python property with no known interface label ("find the field with the same
  label"), data-block creation with no menu of its own (`bpy.data.objects.new`), and similar.
- Mesh built from raw vertex data (`from_pydata`, `bmesh`) is UNMAPPED on purpose: there is no
  interface equivalent. The step's honest route is the script, or modelling the shape with primitives
  and Edit Mode and measuring the result against the census.
- Pure computation (helpers that only return values), prints, reads, "put the setting back" lines
  (`x = orig_x`) and script bookkeeping (dicts, lists) are not steps and are dropped.

## What the drafter cannot know

- **Judgment.** The goal and the reason. It copies the MCP's stated `user_prompt` as a *hint* for the goal
  and leaves `why` empty with `needs_author`.
- **Which steps belong to which module or stage**, beyond the first name it sees and a `--stage-map` you give.
- **Whether a human would do it that way.** Placing 1,800 parts from a table is a script job; the card
  says so through `repeats` and the script door.
- **Colour.** A recorded Base Color is *linear* RGBA. The colour picker's RGB tab takes those linear
  numbers; its Hex tab shows the sRGB equivalent. If the Python derived the colour from a hex string,
  give the hex in `settings` so the reader can type it.

## Finish a card

1. Read the Python (`operation.python.ref`) and the draft lines side by side.
2. Delete lines that are not part of the model (probe calls, snapshots, clean-up of earlier attempts).
3. Write `goal` and `why`; clear `needs_author`.
4. Replace every `UNMAPPED` and `~` line with a real instruction, or write `no_gui_reason`.
5. Fill `result.measured` from the census (`dimensions_m`, counts), not from adjectives.
6. Leave `gui_source` as `draft` until someone has followed the steps in a fresh file. Then set it to `human`.

## Verify the map after a Blender upgrade

```bash
"$BLENDER" -b --factory-startup --python brutalist.art/skills/make/blender-build/scripts/check_gui_map.py
```

It asks Blender for each operator's RNA type (the check `hasattr(bpy.ops.mesh, name)` is **always true**,
operators are looked up lazily, so it proves nothing), and adds each modifier and constraint to a
scratch object to read its real properties. It prints how many properties it checked against how many
the map lists, so a check that silently skipped some cannot pass. Exit 1 when any name has gone.
It does **not** check menu paths or labels.

## Pattern versus instance

A person cannot follow 1,809 "Add cube" steps. Document **one instance in full** (its `Do` list,
settings, result, why) and give the rest as `repeats`: the rule ("one per 24 ft bay"), the number, and a
placement table (`placements.csv`) or an explicit list. In the guide the hands door does one instance
and the script door does the table.
