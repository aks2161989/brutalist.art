# SHOTLIST — Brutalist Command: art icons — Short (9:16)

Derivative of the parent long's vertical companion
(`youtube/brutalist/claude-liam-brutalist-command-icons/vertical`). Every
retained beat's native 2160×3840 render is reused byte-for-byte via
`runtime/scripts/shorts.py`'s native-portrait-reuse path — no crop, no
re-render, no down-sample.

7 beats · 107.6 s · portrait 2160 × 3840 · H.264 + AAC · MP4.

| #   | Beat                       | Portrait scene              | Duration | Source (parent vertical)      |
| --- | -------------------------- | --------------------------- | -------: | ----------------------------- |
| B00 | ASK — cold open            | `ClaudeComposerAsk916`      |  16.17 s | `vertical/media/B00.mp4`      |
| B01 | BLUF — hesitant writer     | `BrutalistHesitantWriter916`|  12.17 s | `vertical/media/B01.mp4`      |
| B04 | MECHANISM — the ranker     | `ClaudeCodeBeat916`         |  18.63 s | `vertical/media/B04.mp4`      |
| B05 | WORKED EXAMPLE — "money"   | `ClaudeCodeBeat916`         |  17.08 s | `vertical/media/B05.mp4`      |
| B08 | FALSIFIABILITY — the miss  | `ClaudeCodeBeat916`         |  17.54 s | `vertical/media/B08.mp4`      |
| B09 | VERDICT — the whole surface| `ClaudeVerdictArtifact916`  |  20.46 s | `vertical/media/B09.mp4`      |
| B11 | OUTRO — title restate      | `ClaudeTitleOutro916`       |   5.58 s | `vertical/media/B11.mp4`      |
| —   | **TOTAL**                  |                             | **107.63 s** |                          |

## Dropped from the parent long (deferred to the 16:9 film)

| # | Beat | Portrait scene | Duration | Why dropped |
|---|---|---|---:|---|
| B02 | FRAMEWORK — dispatcher | `ClaudeCodeBeat916` | 15.00 s | Case-statement internals — anatomy, not high-level. |
| B03 | MECHANISM — the set | `ClaudeCodeBeat916` | 18.33 s | Full icons.json geometry walk — numbers already appear in B00 output and B09 verdict. |
| B06 | WORKED EXAMPLE — check/show | `ClaudeCodeBeat916` | 17.00 s | Both flags named + defined in B09 verdict. |
| B07 | WORKED EXAMPLE — brands filter | `ClaudeCodeBeat916` | 18.71 s | Flag + corpus split (376 / 6,954) restated in B09 verdict. |
| B10 | YOUR TURN | `ClaudeComposerAsk916` | 22.67 s | Extended Your Turn explicitly overridden by the cut-first Shorts prompt. |

## Portrait framing evidence

- Contact strip @ 2 fps: 215 frames in `_qc/frames/f-*.jpg`.
- Beat-relative 15% / 50% / 85% frames: 21 frames in `_qc/beats/` (720×1280).
- Boundary frames (start / end + each transition): 14 frames in `_qc/joins/`
  (540×960).
- SHA-256 for every beat-relative frame is recorded in `VISUAL-REVIEW.json`.

## Portrait-specific caveats (inherited from the parent)

- **Skin warnings** on B00/B11 are inherited from the parent long: the
  compiler's simple string match wants `ClaudeComposerAsk` / `ClaudeTitleOutro`
  verbatim but `Root.tsx` registers the shipped portrait ids as
  `ClaudeComposerAsk916` / `ClaudeTitleOutro916`. Same false-positive the
  parent shipped with, documented in `CHECKS-REPORT.md`.
- **ClaudeCodeBeat916 right-edge clip**: long code / output lines on B04,
  B05 and B08 clip past the code card's right edge in the parent's shipped
  native render. The narration reads the full form aloud in every case, so
  on-audio meaning is preserved. This Short reuses the parent frames
  byte-for-byte; re-rendering the parent scenes is out of scope.
