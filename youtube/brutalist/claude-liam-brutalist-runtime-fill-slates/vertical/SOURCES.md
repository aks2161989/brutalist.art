# SOURCES — Brutalist Utility: fill_slates.py

Every claim and code snippet in this episode traces back to a specific file in the local Brutalist toolkit copied into the isolated workspace.

## Primary source

| Path (repo-relative) | Role | SHA-256 (current) |
|---|---|---|
| `runtime/scripts/fill_slates.py` | THE tool under teardown — module docstring, `_truncate`, `slate_resolves`, `find_slates`, `stamp_slates`, `render_reel`, and the `main()` loop. | `de9efcbdc25a385a5678bde0d8093d0ede06e81da8c5c7af1efdcab2e4d7863a` |

Episode source SHA-256 recorded on invocation: `b6afa2184bdbfa41e1d6be36caf8d4d70179fda94dd031f7368fe966d121f8d8`.
The current file SHA differs from the invocation-time SHA because the local isolated toolkit's copy also carries an unrelated build-safety edit; the substantive `fill_slates.py` behavior is unchanged. Every quoted line in beat 3–6 and beat 8 was cross-checked against the current file.

## Read-only example leads (BRIEF.md)

These were read as staging leads only. No human signature, private path, or previous rendered result was reused.

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — SHA-256 `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22` — reference for "Your Weekly Video, Handled." pacing.
- `yatra-r/2026-09-03-this-week-gordy/beat_sheet.json` — SHA-256 `7e3ea1f61c421e605e583be9b2a7b5f554aa8cadfb6e14dabaee66f471856083` — reference for concise handoff cues.

## Supporting toolkit files consulted (not narrated)

- `runtime/scripts/remotion_scenes.py` — used to render every visual beat; behavior described in B06.
- `runtime/scripts/run.sh` — invoked by `render_reel()`'s second subprocess call; behavior described in B06.
- `runtime/scripts/compile.py` — used to assemble the final 4K masters (landscape 3840×2160, portrait 2160×3840).
- `runtime/qc/final_frame_check.py` — Gate V frame-review script; results in CHECKS-REPORT.md.
- `runtime/remotion/src/Root.tsx` and `runtime/remotion/src/scenes/*.tsx` — component registry the beat-sheet patterns resolve against.

## Public repo referenced in narration

- `https://github.com/nikbearbrown/brutalist.art` (linked via metadata.links.toolkit_repo; not narrated as this episode's clone target).

## Preservation

All quoted code in the ClaudeCodeBeat cards is verbatim from the current `fill_slates.py`. Wrapping/whitespace was tightened for portrait/landscape card legibility only. Nothing was invented, and no external services were called.
