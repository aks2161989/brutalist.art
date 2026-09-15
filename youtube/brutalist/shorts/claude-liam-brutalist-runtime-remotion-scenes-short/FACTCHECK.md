# FACTCHECK — Brutalist Utility: remotion_scenes.py — Short

Derivative of the 16:9 long film. All claims verified against the actual source:
runtime/scripts/remotion_scenes.py
(SHA-256: 3e5faac58d8ecd487bc43c83f267a035d939338375aff954d3a472d14f787996)

Retained beats: B00, B01, B02, B03, B06, B08, B09, B11
Dropped beats: B04, B05, B07, B10 — those beat verifications belong to the long film's FACTCHECK.

## Verified claims (retained beats only)

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
| B06 | "validate_project checks beat sheet structure" | line 141: `validate_project(sheet)` |
| B06 | "validate_approvals is the fellows safety gate" | line 176: `validate_approvals(folder, sheet)` |
| B06 | "slate_resolves: media file already there → skip" | lines 181-183: `if not a.force and not slate_resolves(folder, bid): continue` |
| B08 | "render_beat returns FAIL: string with pattern name and last 800 bytes of stderr" | render_beat() lines 96-102 |
| B08 | "beat goes into failures list, script continues" | main() lines 197-199 |
| B08 | "exit code 2 returned at end" | main() line 203: `return 2 if failures else 0` |
| B08 | "os.replace only runs on success — no overwrite on failure" | render_beat() lines 103-106 |
| B08 | "Fix the composition, run again with --force --only BXX" | args: --force, --only in argparse |
| B09 | "supersampled 4K output" | --scale=2 in render_beat() |
| B09 | "audio-clock-matched clips" | extend_clip_to_duration() |
| B09 | "idempotent reruns" | slate_resolves() |
| B09 | "approval gates" | validate_approvals() |
| B09 | "failure isolation" | failures list, exit 2 |
| B09 | "--list audits without rendering" | list branch, lines 149-158 |
| B09 | "--only BXX targets one beat" | --only arg filter in main() |
