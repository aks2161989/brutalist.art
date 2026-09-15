# FACTCHECK — Brutalist Command: art shorts

Every claim in the narration was verified against the isolated toolkit at
`.repoloop/workspaces/claude-liam-brutalist-command-shorts/toolkit/` and its
`runtime/scripts/shorts.py`. Source SHA-256 of the two named sources at the
top of this build: `art` → `9bb77a7c84701d23ab6e73f0a4f48592f17748ffad2c7114b62687bb7f97d0e9` ·
`runtime/scripts/shorts.py` → `7109a3d0c29c00181a876db80e34238eb9c0c146a97a639a2bbab6d95d28d6e5`
(from `SOURCE-SNAPSHOT.json`).

## Dispatcher

- `./art shorts <reel>` is a top-level case at `art:81-83` that runs
  `exec python3 "$ART_HOME/runtime/scripts/shorts.py" "$@"`. Verified:
  `grep -n "shorts)" toolkit/art` returns `81:  shorts)` immediately followed
  by the exec line.
- `./art vertical <reel>` at `art:84-86` runs the same script with the extra
  argument `--vertical` appended: `exec python3 shorts.py "$@" --vertical`.
- No aliases: the dispatcher `case` matches only the literal strings
  `shorts` / `vertical`. Anything else falls through to the skill-directory
  lookup in `art:107-116` and either shows a SKILL.md or errors out.

## Editorial law (from the module docstring, lines 3-22)

- `SHORTS_CAP_S = 180.0` is defined in `runtime/scripts/build_safety.py:210`
  and imported at `shorts.py:59-61`. The comment on the constant reads
  "Editorial rule: strictly LESS than 3:00, including tails."
- `require_short_duration()` at `build_safety.py:213-218` raises `BuildError`
  when `duration >= SHORTS_CAP_S` — the >= is the strict-under enforcement.
- `CAP_HEADROOM_S = 5.0` at `shorts.py:67`. The auto-plan computes
  `budget = SHORTS_CAP_S - CAP_HEADROOM_S - end_s` (`shorts.py:180`), so a
  4.5-second endcard leaves the planner aiming at `≤ 170.5s` of retained beats.
- `--vertical`: at `shorts.py:251-254`, when `a.vertical` is set the script
  raises `BuildError('--vertical preserves the full film; --drop is not allowed')`
  if `--drop` is present, and forces `no_endcard = no_outro_rewrite = True`.

## The auto-planner (`plan_drops`, `shorts.py:176-192`)

Verified by reading. The planner:
1. Computes `budget = SHORTS_CAP_S - CAP_HEADROOM_S - end_s`.
2. Returns `[]` if total already fits.
3. Otherwise sorts unprotected beats by duration descending and appends
   `beat_id` to the drop list until the running total is under budget.

`is_protected` at `shorts.py:159-173` returns True for: any beat in `keep_ids`;
any `source_report` beat (`is_source_report`); the first and last beat in
`beats`; any beat whose `act` (upper-cased) is `INTRO` or `OUTRO`; any beat
whose `graphic.production_viz.mechanic` or `.label` contains the substring
`hero` (case-insensitive).

## THE ONDA CHECK (`shorts.py:36-42`, `370-385`)

- Every REMOTION beat is detected by its sheet, not by its folder: an
  `is_remotion()` beat has `shot.type == 'REMOTION'` (uppercase) or a truthy
  `shot.remotion`. Verified at `shorts.py:124-127`.
- `portrait_pattern(pattern, tsx)` at `shorts.py:139-144` looks up `<pattern>916`
  in `Root.tsx`'s composition ids: if `f'id="{pattern}916"' in tsx`, that id is
  used; otherwise `None` is returned and the beat is added to `onda_blocked`.
- If rewired, `b['shot']['remotion']['pattern']` is reassigned to the 916 id and
  `b['shot']['remotion'].pop('rendered', None)` clears the stale landscape stamp,
  so the next `remotion_scenes.py` pass on the derivative renders portrait.
- If blocked, the printed message says: "no {pattern}916 composition in Root.tsx
  — add one, or drop pantry/{bid}-916.mp4". This is verbatim at `shorts.py:383`.

## Pantry precedence

- `pantry/<bid>-916.{mp4,png,jpg}` is checked before the ONDA CHECK for every
  kept beat (`shorts.py:361-368`). If it exists, `override` is set and the file
  is copied into the derivative's `media/` slot with the original beat id name
  (`shorts.py:445-448`). No other path can undo it.
- Human-made non-generated `-916` files (captured media only) are checked
  after the ONDA CHECK at `shorts.py:389-398`. For generated (Remotion or
  Manim) beats the script explicitly refuses to fall through to the crop path
  and treats a stray `media/<bid>-916.mp4` next to a generated render as
  stale (`shorts.py:41-42`, `shorts.py:388`).

## Center-cut fallback (captured media only)

- `shorts.py:422-443`: for captured media, `ffmpeg -vf crop='min(iw,ih*9/16)':ih:'…':0`
  is invoked with the crop offset biased by `shot.focus[0]` (the horizontal
  focus fraction 0..1). Written into `short/media/<bid>-916.<ext>`.
- Explicit narration on `shorts.py:441-442`: "replace via pantry/<bid>-916.<ext>
  if the cut doesn't work" — the human's escape hatch is right there in the log.

## Endcard

- `endcard_png()` at `shorts.py:81-116` draws a 1080×1920 dark card with the
  channel handle and a wrapped "Next:" line, using Georgia if available.
- The Next: line defaults to the last dropped CARD beat's narration
  (`shorts.py:295-297`) and `--next` overrides it.
- Silent 4.5s mp3 companion is generated with `ffmpeg -f lavfi -i anullsrc`
  (`shorts.py:455-457`). Both files land in `short/media/END.png` and
  `short/mp3/beat-END.mp3`.

## Failure cases verified by direct invocation

Every failure narrated in the film was run against the fixture reel
`/tmp/claude-501/claude-shorts-demo` and the exact stdout/stderr is saved in
`demo/SHORTS-LOG.txt`:

| Invocation | Exit | Message |
|---|---|---|
| `./art shorts <reel>` (auto, 214s) | 0 | "over the cap → auto-plan drops 1 beat(s): B02"; 163.5s OK |
| `./art shorts <reel> --keep B02` | 0 | "over the cap → auto-plan drops 1 beat(s): B04"; 168.5s OK |
| `./art vertical <reel>` | 0 | "full-length companion: every source beat is retained" |
| `./art shorts <reel> --vertical --drop B02` | 1 | REFUSED "--vertical preserves the full film; --drop is not allowed" |
| `./art shorts <reel> --drop B99` | 1 | REFUSED "Unknown --drop beat(s): ['B99']" |

## Publishing gate

- `shorts.py:52` (module docstring) states verbatim: "Publishing requires a
  separate authorized handoff; see docs/FELLOWS-SUBMISSION.md." No upload
  code exists in this module and no HTTP client is imported.

## Not asserted — honest gaps

- Fresh install/network cloning was not exercised in this run: rendering used
  the already-installed local toolkit. The narration reflects that.
- The `--rewrite-outro` audio-regeneration path was not exercised (auto-plan
  drops kept the parent outro intact in every demo above). The rule is
  described from source (`shorts.py:299-306`, `rewrite_outro()` at
  `shorts.py:195-211`) but no audio was regenerated to prove it end-to-end.
- The Remotion beats in the fixture were fully generated in the shorts demo
  section only to prove the ONDA CHECK log lines — the fixture reel was not
  taken all the way through compile, and the film says so.
