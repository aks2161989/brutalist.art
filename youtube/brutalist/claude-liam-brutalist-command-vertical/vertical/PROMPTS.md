# PROMPTS.md — Brutalist Command: art vertical

## B00 — the cold-open ASK (what the composer types)

```
Turn my finished 16:9 reel into its full-length 9:16 twin. Do NOT
crop the frame, do NOT shorten anything, and re-render every Remotion
beat portrait instead of chopping it. Print the plan before you touch
a file.
```

Expected answer lines (composer output):

- wraps: `python3 runtime/scripts/shorts.py <reel> --vertical`
- writes: `<reel>/vertical/beat_sheet.json`
- contract: full length — no cap, no drops, no endcard, no rewritten outro

## B10 — the YOUR TURN prompt (read aloud verbatim)

```
From the brutalist.art toolkit, against a finished 16:9 reel of yours:

  (1) run  ./art vertical <reel>  and read the plan — every source beat
      should appear as retained, and the ONDA CHECK should list each
      Remotion beat rewired to its <pattern>916 composition.

  (2) if ONDA CHECK prints BLOCKED for any beat, either register the
      missing 916 composition in runtime/remotion/src/Root.tsx (mirror
      the 16:9 pattern at width 1080 × height 1920) or drop a manual
      override at  pantry/<BID>-916.mp4  in your reel folder.

  (3) run the two commands the script prints at the end:
        python3 runtime/scripts/remotion_scenes.py <reel>/vertical
        python3 runtime/scripts/compile.py <reel>/vertical --review \
                --height 1920

  (4) inspect the resulting mp4 end-to-end. Look for cropped text or
      any Remotion beat that fell back to a center-cut instead of a
      native portrait render.
```

Expected outcome (composer output):

- step 1 — plan prints with every source beat retained, no drops
- step 2 — 916 composition or pantry/<BID>-916.mp4 clears BLOCKED
- step 3 — portrait renders land under `<reel>/vertical/media/`
- step 4 — final MP4 is a native portrait, not an upscaled crop

## Not used

- No paid API prompts.
- No `art keys` demo.
- No `setup --install` demo.
- No network clone demo — the fixture reel at
  `/tmp/claude-501/claude-shorts-demo` is a synthetic, disposable local
  reel created for the Ep 30 build and reused here to exercise the same
  `shorts.py` code path.
