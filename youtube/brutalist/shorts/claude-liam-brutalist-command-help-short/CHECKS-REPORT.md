# CHECKS-REPORT — Brutalist Command: art help (9:16 Short)

Invocation `run_id = 2c495c5f99c840f6adc567ad1aa16613` — 2026-09-12.
Slug: `claude-liam-brutalist-command-help-short`.
Derived from parent `claude-liam-brutalist-command-help-vertical`
(parent master SHA-256 `b35bce6f260ee81026a027eba381258f6c0df605408b8a84cfb01f68b65e18d3`).

## What this Short is

A **whole-beat cut** of the parent vertical companion. 8 beats retained
(B00, B01, B03, B04, B05, B06, B09, B11); 4 dropped (B02, B07, B08, B10)
per `CUT-PLAN.json`. **No narration rewrite. No new Remotion render.**

**Rebuild trigger (2026-09-12):** The parent vertical was rebuilt on 2026-09-11
after a godot-* dispatch block was inserted before the main case statement in the
`art` script. This shifted the help sed call from `art:39` → `art:56` and the
alias case pattern from `art:38` → `art:55`. Beats B03 and B04 in the previous
Short export referenced the old line numbers. Updated B03.mp4 and B04.mp4 were
copied from the parent vertical and the Short recompiled.

Final export:
`youtube/brutalist/shorts/claude-liam-brutalist-command-help-short/exports/short/claude-liam-brutalist-command-help-short.mp4`
- Container: 107.375 s · 2160×3840 · h264 24 fps · 6.7 MB
- Video stream: 107.375 s · 2160×3840
- Audio stream: 107.375 s · aac stereo 48 kHz
- SHA-256: `47ec0037bbf09798a48f9242457ef175421a42b4f89e883d9a43e2e75b150e60`

## Cut plan

- Cut: whole-beat-cut, 8/12 beats, drop B02 B07 B08 B10
- `shorts.py` reported `8 beats · ~107.4s (1:47.4) OK` (original run).
- Recompile: `compile.py` with `--height 3840`; only B03 and B04 slots needed
  recompile (changed input SHAs); all other clips cached.

## Updated beat media

| Beat | Old SHA (stale) | New SHA (current) | Changed |
|------|-----------------|-------------------|---------|
| B03  | `a615262a…` | `171cbd74…` | art:39→art:56 title bar |
| B04  | `154c0321…` | `303cb955…` | smoke+keys note added, descriptions expanded |
| B05  | `2e447836…` | `2e447836…` (unchanged) | art:38→art:55 in code comment (visual match) |

All other beats (B00, B01, B06, B09, B11) confirmed matching parent vertical.

## Runtime gates

- **Duration cap** — 107.375 s measured on the container. Cap is strictly
  under 180 s; **72.6 s of headroom**. Passes.
- **`compile.py`** — 8 / 8 filled, all VIDEO slots. Audio per-beat timeline
  (source audio preserved). Wrote MP4 with atomic verification.
- **Audio decode** — final container audio stream present, aac stereo, same
  duration as video. Per-beat mp3s unchanged (narration is identical).
- **Motion histogram** — `code-cascade:4  type-on:1  hesitant-type:1
  artifact-in:1  outro-card:1`. code-cascade at 4/8 = 50%; same ratio as
  parent (6/12 = 50%). Not a blocker.
- **Skin lint** — same two non-fatal warnings the parent already carries:
  `B00 ClaudeComposerAsk916` and `B11 ClaudeTitleOutro916` under
  `palette=claude`. Both are 916 twins of the base compositions, approved
  for portrait in the parent. Not new to this Short.
- **Frame checks** — Beat-relative 15%/50%/85% samples for changed beats
  B03 and B04 (6 frames) re-extracted and SHA-256 hashed; remaining 18
  frames carry validated hashes from prior run (beats/clips unchanged).
  All hashes recorded in `VISUAL-REVIEW.json`.
- **Legibility / portrait framing (B03, B04 re-inspected)**:
  - B03 mid-sample confirms title bar `art:56` (correct updated line number);
    sed mechanism code legible in left column; spark line "The help IS the
    header, minus the hash." inside SAFE916. Clean.
  - B04 mid-sample confirms updated 17-line output with smoke+keys footnote
    at bottom; command column (`./art --list`, `./art <skill> --help`, etc.)
    all legible inside SAFE916; right-edge bleed on description column
    inherited from parent (accepted). Spark line "17 lines. Exits 0. (smoke
    + keys beyond sed range)" at bottom. Clean.

## Coherence of joins

Retained order B00 → B01 → B03 → B04 → B05 → B06 → B09 → B11 intact.
The art source update (godot-* dispatch added) does not affect the help
output visible to users (sed '2,18p' still extracts the same 17-line header;
smoke and keys at lines 19-20 are outside the range). Teaching arc is
unchanged; line-number corrections in B03/B04 are factual fixes, not
editorial changes.

## Blockers / majors

- Blockers: **0**.
- Majors: **0**.

## Limitations

- **Human review pending.** No human viewing signature was applied.
- **No paid API used, no upload, no publish.** Output is a local file only.
- **Skin-lint 916-twin warnings** carried from the parent (see above).
- **Code-card horizontal bleed** carried from the parent (see above).

## Non-actions (safety)

- Parent vertical/media and mp3 files are untouched.
- No changes to the toolkit, the public `runtime/remotion/`, or any other
  reel's `exports/`.
- No git commit, push, publish, or scheduling side effect.
