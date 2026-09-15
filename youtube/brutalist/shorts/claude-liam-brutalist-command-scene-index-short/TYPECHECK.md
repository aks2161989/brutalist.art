# TYPECHECK — Short (9:16) — Brutalist Command: art scene-index

## Sheet validation

- `runtime/scripts/build_safety.py::validate_project` ran twice during
  the build: once inside `shorts.py` before writing the derivative sheet
  and again inside `compile.py` before assembly. Both passed.
- `require_short_duration(total)` inside `compile.py` confirmed
  `short_validation = {"status": "ready", "errors": []}` on the emitted
  `beat_sheet.json` (planned 105.624 s; compiled 105.625 s).

## Remotion prop-name pass

Every retained beat reuses the exact remotion props already validated
in the parent's vertical build (`../claude-liam-brutalist-command-scene-index/vertical/beat_sheet.json`).
No prop schema changed. This preserves the parent's pass through the
per-composition zod schemas.

| Beat | Composition            | Prop keys present |
|------|------------------------|-------------------|
| B00  | `ClaudeComposerAsk916` | greeting, topic, segment, command, runningText, output[], folderLabel, modelLabel, effortLabel |
| B01  | `BrutalistHesitantWriter916` | text, triggerWords, replacementWords, seed, face, fontSize, lineSpacing, align, charMs, jitter, mistakeRate, hesitateWithin, hesitateBetween |
| B03  | `ClaudeCodeBeat916`    | title, code, sparkLine |
| B05  | `ClaudeCodeBeat916`    | title, code, sparkLine |
| B09  | `ClaudeVerdictArtifact916` | artifactTitle, artifactHeading, artifactLines[] |
| B11  | `ClaudeTitleOutro916`  | title, slug |

- Trigger-word / replacement-word syntax on B01 matches the parent's
  passing form: comma-separated single tokens, no trailing punctuation.
- Hesitant-writer `fontSize: 155`, `lineSpacing: 2.9` — matches the
  portrait BLUF recipe recorded in the parent's SHOTLIST (Gate V ≥55%
  fill on 9:16 relies on lineSpacing, not font size).
- Outro slug is the parent's slug (`claude-liam-brutalist-command-scene-index`),
  as required by `OUTRO-LOCK.md` for the seeded mascot.

## Metadata pass

Derivative sheet metadata (validated at both writes):

- `kind = "short"`, `aspect_ratio = "9:16"`, `fit = "pad"`
- `playlist = "Brutalist"`
- `voice = "am_onyx"`, `voice_kokoro = "am_onyx"`, `engine = "kokoro"`
- `captions = false`
- `derived_from = "claude-liam-brutalist-command-scene-index-vertical"`
- `dropped_beats = ["B02","B04","B06","B07","B08","B10"]`
- `total_estimated_duration_seconds = 105.624`
- `short_validation.status = "ready"`

## Media dimension pass

`ffprobe` confirms every retained `media/B*.mp4` is 2160x3840 (native
portrait — reused unchanged from the parent, not center-cut). Final
container is 2160x3840 h.264 + AAC.

## Portable text rendering

Compiler ran on an ffmpeg build without `drawtext` (see `[art] ... drawtext: no — PIL overlays`).
No timecode overlay was needed because `--review` was not used on the
final pass. Pillow overlay code path is exercised only for slates, and
none were emitted (all 6 slots filled).

## Known non-shipping-blocker gaps carried from the parent

- The shipped Gate T `type_check.py` + `reference/type-spec.md` +
  kerning skill are not part of this toolkit revision; typography
  sanity was a manual visual review (see `CHECKS-REPORT.md`), same as
  the parent build. Not introduced by this Short.
- Motion histogram inherits the parent's code-cascade weighting; on a
  6-beat Short the histogram is `code-cascade:2 type-on:1 hesitant-type:1
  artifact-in:1 outro-card:1` = 33% code-cascade, comfortably below any
  cap the shipping toolkit enforces.
