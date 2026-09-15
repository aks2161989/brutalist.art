# CHECKS-REPORT — vertical (9:16)

`claude-liam-brutalist-command-scenes-vertical.mp4` — 2160x3840 @ 30 fps,
256.29 s, h.264 + AAC. Full-length native portrait companion; every source
beat retained (no Short cap applied — `art vertical` was used, not
`art shorts`).

## Gate F — factcheck

- `FACTCHECK.md` (copied from landscape — still accurate for this aspect):
  every claim traces to the same two source files.
- `SOURCES.md` also carried over; hashes unchanged.

Pass.

## Gate V — visual QC (final_frame_check.py, portrait safe area)

```
Frames sampled: 24  ·  BLOCKER: 0  ·  MAJOR: 0
Clean — no BLOCKER/MAJOR defects. ✓
```

Full report at `_qc/REPORT.md`; contact sheet at `_qc/contact_sheet.png`.

The BLUF beat (B01) took three passes to converge:
- fontSize 280 / 1.35 (default from landscape) → 20 % underfill (MAJOR).
- fontSize 170 / 2.7 → edge-bleed (BLOCKER) — "existing scenes." was ~995 px
  wide against the 972 px SAFE916 width.
- fontSize 165 / 2.7 → clean (55 % coverage, no bleed).

The portrait-aware scale patch to `BrutalistHesitantWriter.tsx` (matching the
one used in the icons episode) was reapplied to this isolated toolkit so the
serif reads native size at 1080x1920 instead of collapsing to 0.5625 scale
(see `feedback_hesitant_writer_portrait_scale.md`).

The B10 (Your Turn) composer text was also tightened for portrait — segment
shortened from `Audit art scenes on your own beat` (bled) to
`Audit art scenes`; the four output lines were compressed to fit the
portrait output card. The narration was unchanged, so the audio still
recites the full paste-ready command aloud; the on-screen prompt shows the
core moves.

## Audio decode

`ffprobe` confirms an AAC stream matching per-beat MP3 SHA-256s in the
compiler's `.verified.json` receipt. No beat is silent.

Pass.

## Compiler receipts

- `status: ready`
- output SHA-256 `06eb7031e272bac545d3a16c0ce48e0ebaeb9a3fedaeeb0b16d294233ce3aea8`
- 256.29 s duration; 2160x3840 native dimensions confirmed by ffprobe.

## Skin lint

The compiler emitted two SKIN LINT warnings on the portrait cut:

- B00 uses `ClaudeComposerAsk916`; the linter expects the landscape
  `ClaudeComposerAsk` for COLD OPEN LAW.
- B11 uses `ClaudeTitleOutro916`; the linter expects the landscape
  `ClaudeTitleOutro` for OUTRO LAW.

Both are expected for a native-portrait cut: the 916 siblings are the
portrait implementations of the same laws. The lint pattern doesn't
recognize the `-916` suffix as a portrait variant. Recorded, not
suppressed.

## Known limitations

- ClaudeCodeBeat916 does not word-wrap long code lines; long lines (present
  in landscape at fontSize 34 px) are horizontally clipped inside the code
  card in portrait. The Gate V safe-area check passes because the code card
  itself is inside SAFE916. Fellows should prefer the landscape master for
  detailed reading of the raw script contents (all lines are visible in
  16:9). This is consistent with the icons vertical (same limitation, same
  Gate V verdict).
- The same absent legacy `type_check.py` gap noted in the landscape
  `TYPECHECK.md` applies here. Manual visual typography review was
  performed; see `TYPECHECK.md`.
