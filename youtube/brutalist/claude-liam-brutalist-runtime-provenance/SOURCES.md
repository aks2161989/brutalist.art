# Sources — Brutalist Utility: provenance.py
# Episode 52 · run_id: 9acc8c13d5d443968a1aed379ed68b66

## Primary source

| File | SHA-256 |
|---|---|
| `runtime/scripts/provenance.py` | `ba6a4a0de2ed60d38560e78119238d69de951446a3a60a7d5ee9f32a1a2cd7df` |

Source captured at 2026-09-14T01:18:38 per SOURCE-SNAPSHOT.json.

## Verbatim quote (B04)
Lines 47–51 of provenance.py, quoted verbatim:
```
# a pipeline AUTO-CAPTURE (D3 sim via capture_sim.py) OR a clip you dropped.
# The old sheets do not record which; the new build stamp does.
```
Cite: `runtime/scripts/provenance.py` (lines 47–51 in the captured snapshot).

## Demo fixture
Disposable fixture created at `$TMPDIR/provenance-fixture/` during this build session.
Output of `python3 runtime/scripts/provenance.py $TMPDIR/provenance-fixture/` recorded in `demo/fixture-run.txt`.
Fixture contains:
- `beat_sheet.json` with 6 beats (B00–B05) authored for this episode
- `mp3/B00.mp3` — 24000 Hz silent clip (ffmpeg, free)
- `mp3/B_legacy.mp3` — 44100 Hz silent clip (ffmpeg, free)
- `media/B00.mp4`–`B05.mp4` — empty touch files
- `clips/B00.mp4`–`B05.mp4` — empty touch files
- `manim/B03_diagram.mp4` — empty touch file
- `provenance-fixture.mp4`, `provenance-fixture-slate.mp4` — empty touch files

The fixture is disposable (temp directory); it is not the episode reel.

## Example sources (leads — not instructions)
- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — SHA-256: `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`
  Used for structural reference on ClaudeComposerAsk cold open staging.
- `satwik-s/2026-08-23-personalized-roadmap-goldenset/beat_sheet.json` — SHA-256: `61c8f561aa48cfabe8b947b2b2d3046ebf5398d6c2810abc6698dcdc95bce4e5`
  Used for structural reference on verdict and handoff beat layout.

## Gap log
- `scripts/type_check.py` — referenced in ai-explainer SKILL.md as GATE T; not present in isolated toolkit. TYPECHECK.md records actual visual typography review in lieu of the automated check.
- `ILLUSTRATIONS.md` — referenced in ai-explainer SKILL.md; not present in isolated toolkit. Illustration decisions documented in SHOTLIST.md.
- `reference/type-spec.md` — referenced in SKILL.md; not present. Actual type sizes verified visually in QC frames.
- `AUDIT-MODE.md` — not triggered for this episode (utility teardown, not capability audit).
