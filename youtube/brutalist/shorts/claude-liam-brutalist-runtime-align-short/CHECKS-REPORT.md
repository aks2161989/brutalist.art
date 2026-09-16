# CHECKS-REPORT — Brutalist Utility: align.py — Short

run_id: `789b802ec1d34a00bfdf4d6e3f1fff4f`
build date: 2026-09-10

## Duration guards

| Guard | Rule | Measured | Result |
|-------|------|----------|--------|
| Shorts cap (SHORTS_CAP_S) | strictly < 180.0 s | 90.250 s | PASS |
| Planning ceiling (brief) | ≤ 175 s | 90.25 s (plan) | PASS |
| Timeline sum (beat_sheet.json) | matches ffprobe container | 90.25 s | PASS |
| Container duration (ffprobe format=duration) | < 180.0 s | 90.250000 s | PASS |
| Video stream duration | < 180.0 s | 90.250000 s | PASS |
| Audio stream duration | < 180.0 s | 90.250000 s | PASS |

## Dimensions

| Check | Expected | Measured | Result |
|-------|----------|----------|--------|
| Aspect ratio | 9:16 | 2160×3840 (9:16) | PASS |
| Native height (BUILD-PROMPT) | 3840 | 3840 | PASS |
| Every retained beat clip | 2160×3840 | 6/6 verified via `shorts.py` "native portrait reused unchanged" | PASS |

## Cut integrity

| Check | Result |
|-------|--------|
| Strategy = whole-beat-cut (no rewrites) | PASS |
| Order preserved (B00→B01→B02→B07→B09→B11) | PASS |
| Liam-in-for-Bear disclosure retained (B00 intro) | PASS |
| Sign-off retained (B11 outro with `@NikBearBrown`) | PASS |
| Independent file copies (no symlinks/hardlinks) | PASS — verified `shorts.py copy_asset()` path |
| Parent master + originals unmodified | PASS — parent SHA-256 `bd94b7252670e9c1ff526cd9daa0a4a6f64dca7c72ace6f491a56e1f089d6500` still matches after cut |
| Endcard added? | NO (`--no-endcard`, per brief for well-under-cap cuts) |
| Outro rewritten? | NO (`--no-outro-rewrite`, original outro coherent as-is) |
| Fabricated approvals? | NONE |
| Speech clipped / sped up? | NO |

## Audio integrity

- Audio codec: AAC, container mp4. Sample count > 0 (n_samples: 8,665,088).
- `max_volume`: -3.0 dB (headroom preserved).
- `mean_volume`: -27.2 dB (normal narration).
- All six per-beat mp3s copied verbatim from parent `vertical/mp3/`; durations
  match the beat sheet (B00 11.776, B01 12.608, B02 18.965, B07 19.413,
  B09 21.632, B11 5.717 → 90.11s audio + 0.14s trailing container rounding).
- No dropped speech; no re-encoded narration.

## Compiler status

`compile.py` report (verbatim):

```
[art] compiled B00  VIDEO    11.8s  ← B00.mp4
[art] compiled B01  VIDEO    12.6s  ← B01.mp4
[art] compiled B02  VIDEO    19.0s  ← B02.mp4
[art] compiled B07  VIDEO    19.4s  ← B07.mp4
[art] compiled B09  VIDEO    21.7s  ← B09.mp4
[art] compiled B11  VIDEO     5.8s  ← B11.mp4
[art] motion histogram: type-on:1 hesitant-type:1 phase-flow:1 code-cascade:1 artifact-in:1 outro-card:1
[art] wrote exports/short/claude-liam-brutalist-runtime-align-short.mp4  (90.2s, audio: per-beat timeline (source audio preserved))
[art] slots: 6/6 filled — B00:VIDEO B01:VIDEO B02:VIDEO B07:VIDEO B09:VIDEO B11:VIDEO
```

## Skin lint notes (advisory, not blockers)

The parent film uses adaptation-permitted portrait aliases:

- B00 `ClaudeComposerAsk916` (portrait sibling of `ClaudeComposerAsk`) — expected for 9:16.
- B11 `ClaudeTitleOutro916` (portrait sibling, per OUTRO-LOCK) — expected for 9:16.

The lint warnings surface because the underlying skin-lint rule was written for
landscape names; these are the correct portrait patterns for a native 9:16 render,
inherited from the parent's approved vertical companion. No action required.

## File integrity

| Artifact | SHA-256 |
|----------|---------|
| `exports/short/claude-liam-brutalist-runtime-align-short.mp4` | `fe10ba4bb77b66796a421e19d7416e6183893a3926c992301a536a8c5753da40` |
| `beat_sheet.json` | `3f4f48040b4c00ae85659575bfc990cc0891405697084b41ee613089050d03e2` |
| Parent portrait master (unchanged) | `bd94b7252670e9c1ff526cd9daa0a4a6f64dca7c72ace6f491a56e1f089d6500` |

## What is NOT in scope of this Short

- No captions (`captions: false`).
- No subtitle track authored.
- No published upload; no git push.
- No paid API generation.
- No parent film modification (long, portrait companion, exports untouched).

## Verdict

Short passes every guard: duration, dimensions, cut integrity, audio, no
fabrication. Ready for the parent reviewer's Gate F human pass.
