# TYPECHECK — Brutalist Command: art scenes — Short

The Short's derivative `beat_sheet.json` was validated by
`build_safety.validate_project` inside `runtime/scripts/shorts.py` before the
cut file was written (any schema violation would have raised `BuildError`
and aborted the run). The subsequent `compile.py` invocation re-validates
before rendering.

## Portrait composition props (retained beats)

Every retained beat's `shot.remotion.props` continues to satisfy the
parent's schema for its `-916` composition. Since we reused native portrait
media unchanged, no prop was changed and the ONDA CHECK confirmed:

| Beat | Portrait pattern | Props source | Result |
|---|---|---|---|
| B00 | `ClaudeComposerAsk916` | parent B00 verbatim (`greeting`, `topic`, `segment`, `command`, `runningText`, `output`, `folderLabel`, `modelLabel`, `effortLabel`) | schema-clean |
| B01 | `BrutalistHesitantWriter916` | parent B01 verbatim (`text`, `triggerWords`, `replacementWords`, `seed`, `face`, `fontSize`, `lineSpacing`, `align`, `charMs`, `jitter`, `mistakeRate`, `hesitateWithin`, `hesitateBetween`) | schema-clean; portrait-scale patch already applied in parent |
| B04 | `ClaudeCodeBeat916` | parent B04 verbatim (`title`, `code`, `sparkLine`) | schema-clean |
| B05 | `ClaudeCodeBeat916` | parent B05 verbatim (`title`, `code`, `sparkLine`) | schema-clean |
| B08 | `ClaudeCodeBeat916` | parent B08 verbatim (`title`, `code`, `sparkLine`) | schema-clean |
| B11 | `ClaudeTitleOutro916` | parent B11 verbatim (`title`, `slug`) | schema-clean; `@NikBearBrown` handle hardcoded per OUTRO-LOCK |

The portrait-aware BrutalistHesitantWriter scale patch (min(w/1080, h/1920))
is already in the toolkit; it's a load-bearing precondition for B01 reading
at ~55 % ink coverage on 9:16. Not re-applied in this build.

## Metadata schema

The derivative `metadata` block was written by shorts.py:

- `kind: short`
- `aspect_ratio: 9:16`
- `fit: pad`
- `derived_from: claude-liam-brutalist-command-scenes-vertical`
- `dropped_beats: ["B02","B03","B06","B07","B09","B10"]`
- `total_estimated_duration_seconds: 115.08`
- `short_validation.status: ready`
- `short_validation.errors: []`

Voice/palette fields (`voice: am_onyx`, `voice_kokoro: am_onyx`,
`captions: false`, `palette: claude`) were inherited from the parent and
are consistent with the Brutalist playlist contract.

## Runtime types

No Python or TypeScript files were edited in this build:

- Scripts updated upstream (`compile.py`, `build_safety.py`) — rebuild on
  2026-09-12 confirmed they produce byte-identical output for this Short.
- `math_layout_check.py` added to the isolated toolkit (`dd00f18c`) to satisfy
  the new import added by `build_safety.validate_project`; this module has no
  effect on this reel (it checks prose-card scenes only; none are retained).
- No changes to `runtime/remotion/src/**/*.tsx` (native portrait media was
  reused; no Remotion render invoked).

Any type warnings visible from the parent's build carry over unchanged and
are not introduced by this Short.

## Result

Type/schema check clean. No new type violations, no schema drift versus the
parent, and the derivative file passed `validate_project` before compile.
