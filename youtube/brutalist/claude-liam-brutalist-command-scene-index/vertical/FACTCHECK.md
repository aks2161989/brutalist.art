# FACTCHECK — vertical (9:16) — Brutalist Command: art scene-index

Every on-screen claim carries over from the landscape [`../FACTCHECK.md`](../FACTCHECK.md).
Same tool, same output, same LAW. Portrait re-lays the same evidence in
native 9:16 compositions; no new claims are introduced by the reformat.

## Vertical-specific claims

- **619 renderable · 118 undocumented · 0 unresolved.** Identical to the
  landscape claim. Captured on the isolated toolkit before the portrait
  build added `ClaudeCodeBeat916`. Since the portrait re-run bumps the
  count to 620, the on-screen figure represents the state at capture
  time (documented in the landscape FACTCHECK); the 620 addendum is
  called out in the beat sheet note.

- **`ClaudeCodeBeat916` was registered here for the portrait companion.**
  Verified by inspecting `runtime/remotion/src/Root.tsx` — the new
  Composition is inserted immediately below the landscape `ClaudeCodeBeat`
  registration at width=1080, height=1920.

- **`BrutalistHesitantWriter.tsx` portrait-scale patch.** The shipped
  scale `Math.min(width/1920, height/1080)` collapses to `0.5625` on
  1080×1920 and drops portrait BLUF fill below the Gate V 55% floor.
  The isolated component was patched to a portrait-aware branch:

  ```ts
  const scale = height > width
    ? Math.min(width / 1080, height / 1920)
    : Math.min(width / 1920, height / 1080);
  ```

  Landscape behaviour is unchanged. This patch is local to the workspace
  and is not published upstream by this run.

## Portrait shortening on B10

The landscape B10 command line contains a full paste-ready prompt. In
portrait the composer card wraps that prompt to ~8 lines and pushes past
the bottom safe. The portrait beat uses the same 4-step recipe in a
tighter phrasing (`"(1) Run ./art scene-index; record X renderable, Y
undocumented. (2) Add a <Composition id=\"YourNewScene\" .../> to
Root.tsx. (3) Re-run — expect X + 1. (4) Add one header sentence to any
SCENE-DOC-TODO row; re-run — expect Y - 1."`). Same recipe, same steps —
condensed only to respect the portrait safe area. The landscape master
carries the full prompt fellows will actually paste.

## Nothing else changes

Narration is the identical Kokoro `am_onyx` render Liam gave for the
landscape master (source MP3s are byte-identical; measured durations
match). No captions, no subtitle track. The outro card remains locked
per `OUTRO-LOCK.md` (`@NikBearBrown`) with the composer folder chip
still `@HumanitariansAI`.
