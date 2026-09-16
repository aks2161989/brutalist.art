# TYPECHECK — Brutalist Command: art keys — Short

Run: `b1097e088b3744ed874f3bcc50a2cebb`  ·  Date: 2026-09-13

No new TypeScript sources were compiled for this Short — no Remotion
re-render was required. Every retained media file is the parent vertical's
already-compiled render. `runtime/scripts/shorts.py` and
`runtime/scripts/compile.py` are both Python 3, guarded by
`runtime/scripts/build_safety.py`; both ran to completion with exit 0.

Rebuild was triggered by a SKILL.md source_sha256 change; the parent
vertical media and exported mp4 sha256 were confirmed unchanged.

## Contract checks that passed

- `validate_project(sheet)` — the derivative beat_sheet passed the same
  schema/contract validation as the parent (called by shorts.py at the
  end of derivation, and again by compile.py at load).
- `require_short_duration(planned)` — planned 99.62 s < 180 s, PASSED.
- `require_short_duration(measured)` — measured 99.625 s < 180 s, PASSED.
  Enforced by compile.py's Gate D and re-verified by ffprobe.
- Every retained `media/<bid>.mp4` was probed as 2160×3840, matching the
  compile height. No portrait re-render or center-cut was needed for any
  beat (all are REMOTION renders reused via shorts.py's "native portrait
  reused unchanged" path).
- Every retained `mp3/beat-<bid>.mp3` was copied as an independent file
  (no symlinks — `copy_asset` semantics per build_safety.py).

## Skin lints (informational)

`compile.py` re-emitted the parent's two skin lints:

- `B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD
  OPEN LAW wants ClaudeComposerAsk`
- `B11: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW
  wants ClaudeTitleOutro`

Both are the standing 916-naming convention (portrait shim), not defects.
The parent shipped with the same lints and its own `_qc/REPORT.md` was
clean; this Short's `_qc/REPORT.md` is clean too.

## Command trail

```
python3 runtime/scripts/shorts.py \
    <parent_reel>/vertical \
    --output-dir <reel> --slug claude-liam-brutalist-command-keys-short \
    --drop B02 B03 B05 B06 B07 B10 \
    --no-endcard --no-outro-rewrite
# → 6 beats · ~99.6s (1:39.6) OK

python3 runtime/scripts/compile.py <reel> \
    --height 3840 --out <reel>/exports/short
# → 6/6 filled  · 99.6s · Gate V BLOCKER:0 MAJOR:0
```

No `--review` flag, no bypass flags, no mock renderer, no fake approval.
