# FACTCHECK.md — Brutalist Command: art vertical

Every factual claim in the narration and every code excerpt shown on
screen is checked against the two source files at the SHA-256s recorded
in `SOURCES.md`. Nothing here was invented for the reel.

## Dispatcher (B02)

- The `art` script's `case "$cmd" in` block registers **both** `shorts`
  (art:102-103) and `vertical` (art:105-106). Verified by direct read of
  `toolkit/art` (136 lines total). Line numbers shifted from art:81-83/84-86
  in the prior build due to additional commands added earlier in the file.
- `vertical` execs `python3 "$ART_HOME/runtime/scripts/shorts.py" "$@"
  --vertical`. Verified at `toolkit/art:105-106`.
- The help block at `toolkit/art:15` reads
  `./art vertical <reel>       full-length 9:16 companion (no shortening)`.
  This is quoted on screen verbatim in B02. B02 code card annotation
  updated from `art:78-86` to `art:102-107` to reflect the current file.

## The vertical contract (B03)

- `shorts.py` module docstring rule 5 reads:
  `5. --vertical creates a full-length companion, not a Short: no drops,
  no duration cap, no rewritten outro, no added endcard.`
  Verified at `toolkit/runtime/scripts/shorts.py:20-22`. Quoted on screen
  verbatim in B03.

## The guardrails (B04)

Verified at `toolkit/runtime/scripts/shorts.py:251-254`:

```python
if a.vertical:
    if a.drop:
        raise BuildError('--vertical preserves the full film; --drop is not allowed')
    a.no_endcard = a.no_outro_rewrite = True
```

Quoted verbatim in B04 and B08.

## ONDA CHECK (B05)

The `is_remotion` and `portrait_pattern` helpers are shared between
`art shorts` and `art vertical` — vertical does not soften the check.
Verified at `toolkit/runtime/scripts/shorts.py:124-127` (`is_remotion`)
and `139-144` (`portrait_pattern`). Quoted verbatim in B05.

## Cap check skipped for vertical (B06)

Verified at `toolkit/runtime/scripts/shorts.py:480-484`:

```python
if not a.vertical:
    try:
        require_short_duration(total, 'Planned Short')
    except BuildError as exc:
        blocked.append(str(exc))
```

Quoted verbatim in B06. The condition `if not a.vertical` is the one
line that gates cap enforcement.

## Vertical planning branch (B07 support)

`shorts.py:260-263`:

```python
if a.vertical:
    drops = []
    print('[vertical] full-length companion: every source beat is retained')
```

The banner line `[vertical] full-length companion: every source beat is
retained` appears verbatim in the demo log — see
`demo/VERTICAL-LOG.txt` invocations 1 and 2.

## Verbatim demo output (B07)

The B07 "worked example" beat shows an excerpt of `demo/VERTICAL-LOG.txt`
INVOCATION 1 exactly as printed by the isolated toolkit. Line counts,
whitespace, arrows and beat ids are the shell's actual output. Not
edited, not paraphrased.

## The refusal (B08)

The refusal line printed to stderr —
`[short] REFUSED: --vertical preserves the full film; --drop is not
allowed` — is emitted from `shorts.py:253` via `raise BuildError(...)`
and formatted by the `except (BuildError, ...) as exc: raise
SystemExit(f'[short] REFUSED: {exc}')` block at `shorts.py:529-530`.
Verified by running the command twice — once as `./art vertical … --drop
B02` and once as `./art shorts … --vertical --drop B02` — see
`demo/VERTICAL-LOG.txt` invocations 3 and 4. Both hit the same line and
both exit 1.

## Everything else

- "Same script, opposite editorial contract" — mechanically true: both
  verbs exec `shorts.py`; the `--vertical` flag flips exactly three
  behaviours (drop-refusal, force-off endcard, force-off outro-rewrite)
  and skips one check (`require_short_duration`).
- "No cropping" — captured media in a native portrait reel is preserved
  by the vertical branch at `shorts.py:340-354`, which copies the native
  file when the parent's aspect_ratio is `9:16` and the file's real
  dimensions confirm 9:16 (probed via ffmpeg). For 16:9 landscape source,
  captured media is cropped, but generated (Remotion / Manim) beats are
  never cropped — the ONDA rewire or a portrait scene rewrite handles
  them. This is fully consistent with the shipped module docstring.

Nothing in the narration promises publishing, YouTube 4K approval, or
any behaviour that runs outside the local toolkit.
