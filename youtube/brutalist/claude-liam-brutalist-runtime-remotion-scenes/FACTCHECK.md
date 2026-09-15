# FACTCHECK — Brutalist Utility: remotion_scenes.py

All claims verified against the actual source: runtime/scripts/remotion_scenes.py
(SHA-256: 3e5faac58d8ecd487bc43c83f267a035d939338375aff954d3a472d14f787996)

## Verified claims

| Beat | Claim | Verified against |
|---|---|---|
| B00 | "reads beat_sheet.json for shot.remotion.pattern entries" | line 145: `cands = [b for b in sheet["beats"] if (b.get("shot", {}).get("remotion") or {}).get("pattern")]` |
| B00 | "renders only slate beats" | slate_resolves() function, lines 33-39 |
| B00 | "stamps provenance, updates consumer index, exits 0 on success" | stamp() line 107, update_consumers() line 113, main() return 0 |
| B01 | BLUF correction: only pattern-tagged slates | slate_resolves() + pattern check |
| B02 | "slate_resolves checks each beat — if media/BXX.mp4 already exists, skip it" | slate_resolves() lines 33-39 |
| B02 | "--scale=2 --image-format=png --crf=16" | render_beat() lines 92-93 |
| B02 | "extend: freeze last frame to match audio duration" | extend_clip_to_duration() lines 52-68 |
| B02 | "stamp: provenance written back + consumer index updated" | stamp() + update_consumers() |
| B03 | "shot.remotion.pattern is the entry ticket" | main() line 145 |
| B03 | "No pattern → stays a slate" | slate_resolves() + cands filter |
| B04 | "--scale=2 supersamples 1920x1080 to true 4K" | comment at line 84: `# --scale=2 renders the 1920x1080 comps at true 3840x2160` |
| B04 | "--image-format=png removes JPEG-q80 frame step" | comment at line 85: `# --image-format=png removes Remotion's default JPEG-q80 frame step` |
| B04 | "--crf=16 for clean master" | comment at line 86: `# --crf=16 for a clean master.` |
| B04 | "props written to temp file, passed with --props" | lines 88-89: `atomic_json(props_path, rem.get('props', {}))`, cmd includes `f"--props={props_path}"` |
| B05 | "tpad filter clones last frame" | extend_clip_to_duration(), line 58: `"-vf", f"tpad=stop_mode=clone:stop_duration={duration_s:.3f}"` |
| B05 | "holds clip exactly as long as measured audio duration" | line 59: `"-t", f"{duration_s:.3f}"` |
| B06 | "validate_project checks beat sheet structure" | line 141: `validate_project(sheet)` |
| B06 | "validate_approvals is the fellows safety gate" | line 176: `validate_approvals(folder, sheet)` |
| B06 | "slate_resolves: media file already there → skip" | lines 181-183: `if not a.force and not slate_resolves(folder, bid): continue` |
| B07 | "SLATE or filled status in --list" | list branch, lines 149-158 |
| B07 | "B03 with no pattern doesn't appear" | cands filter: only beats with pattern |
| B08 | "FAIL: returns pattern name + last 800 bytes of stderr" | line 95: `return f"FAIL: {pattern}\n{r.stderr[-800:]}"` |
| B08 | "failures list, continues to next beat" | lines 187-190 |
| B08 | "exit code 2 on failures" | line 199: `return 2` |
| B08 | "previous media slot never overwritten" | os.replace only on success (line 101); candidate in tempdir on fail |
| B09 | "Run before compile.py, never after" | compiler picks up media/BXX.mp4 (doc comment line 7) |

## Claims intentionally omitted / softened

- No version numbers or model-specific claims (they drift)
- No claims about Remotion internals beyond what the script documents itself

## DOUBLE-CHECK LAW

Script rewritten in Teardown register. The source was read and verified; the narration
judges the design ("this is why it's smart"), not just describes it.
