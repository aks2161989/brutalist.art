# PROMPTS — Brutalist Utility: fill_slates.py

## Composer prompts on-screen

### B00 — the ask (cold open)

Greeting: `Hej, Liam`
Segment: `runtime/scripts/fill_slates.py`
Topic: `BRUTALIST · UTILITY: FILL_SLATES.PY`

Command shown in composer:

> Three beats across two reels have no video and no remotion pattern. Fill them all with a Form A card so the review cuts play through. Do NOT touch the beats that are already good.

Running text: `invoking fill_slates.py…`

Result lines:
- walk books/ — find every reel with a beat_sheet.json
- for each SLATE beat (no media, no pattern, not silent) — stamp FormACard
- then shell out to remotion_scenes.py + run.sh to recut the review reel

### B10 — Your Turn (HANDOFF LAW)

Greeting: `Your Turn`
Segment: `Dry-run fill_slates, then upgrade one card`
Topic: `BRUTALIST · YOUR TURN`

Prompt shown in composer (read aloud verbatim by the narrator, then discussed):

> Point Claude Code at a books/ tree with at least one reel currently in mid-build. (1) Run `python3 runtime/scripts/fill_slates.py --books <that path>` — dry-run — and paste back the reel/beat list it prints. (2) Pick ONE slate beat from that list and open its parent beat_sheet.json. (3) Read the beat's narration and role_note; propose a REAL Remotion pattern (not FormACard) that would teach that narration — from `./art scenes` if a fit exists, or a new component if not. (4) Show me the exact diff you would make to `shot.remotion` for that one beat — do NOT run --apply.

Running text: `paste this into Claude Code…`

Grading lines:
- step 1 — the printed reel/beat list, verbatim (no --apply)
- step 2 — the chosen beat_id, its narration + role_note, and why it deserves better than a card
- step 3 — the proposed pattern, either from `./art scenes` or a new-component spec

## Why this Your-Turn prompt

`fill_slates` is the SAFETY NET for unrendered beats — it stamps a FormACard as a fallback so review cuts play through. Every time the fallback fires you lose a bit of teaching, because a serif-lines card is not a moving diagram, a code block, or an artifact. The prompt asks the fellow to (a) surface the fallbacks in their own repo and (b) *upgrade one*, which is the exact discipline the tool exists to enable — not replace.

## Not a step-by-step

The prompt is deliberately dry-run only. `--apply` performs `remotion_scenes.py + run.sh` on every affected reel; that is a batch operation with side-effects on beat sheets that the fellow may not want stamped. The film's B08 (falsifiability) covers what would happen if the fellow ran `--apply` blindly.
