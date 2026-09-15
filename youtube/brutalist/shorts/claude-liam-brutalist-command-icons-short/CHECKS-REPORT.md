# CHECKS-REPORT — Brutalist Command: art icons — Short

Run ID: `5940cae5467d448eb67578534d454790`
Rendered: 2026-09-09 (workspace `claude-liam-brutalist-command-icons-short`)

## Deliverable

- Path: `youtube/brutalist/shorts/claude-liam-brutalist-command-icons-short/exports/short/claude-liam-brutalist-command-icons-short.mp4`
- SHA-256: `49237925aef4fe82bd9e5b32dc45c05abb0bf50a3d7154c80c2d0d21c410c18a`
- Dimensions: 2160 × 3840 (native portrait 4K, no crop/pad)
- Codecs: H.264 video + AAC audio
- Container duration: 107.625 s (ffprobe FORMAT)
- Video stream duration: 107.625 s
- Audio stream duration: 107.625 s
- Shorts cap (< 180.0 s): **PASS** — measured 107.625 s < 180.0 s with 72.4 s of headroom

## Cap check (all three durations strictly < 180.0)

| Stream    | Duration (s) | < 180.0 |
| --------- | -----------: | :-----: |
| container |     107.625  |   OK    |
| video     |     107.625  |   OK    |
| audio     |     107.625  |   OK    |

## Cut plan

Strategy: `whole-beat-cut` (no rewrite required)

- Kept (7): `B00`, `B01`, `B04`, `B05`, `B08`, `B09`, `B11`
- Dropped (5): `B02`, `B03`, `B06`, `B07`, `B10`
- Planned duration from `render_duration_s` sum: 107.625 s
- Measured container duration: 107.625 s (exact match — 30 fps, integer frame counts)

See `CUT-PLAN.json` for per-beat drop reasons and the narrative-join review.

## Source reuse

`shorts.py` reused every retained beat's native portrait media byte-for-byte
from the parent (`youtube/brutalist/claude-liam-brutalist-command-icons/vertical`):

    [short] B00 native portrait reused unchanged
    [short] B01 native portrait reused unchanged
    [short] B04 native portrait reused unchanged
    [short] B05 native portrait reused unchanged
    [short] B08 native portrait reused unchanged
    [short] B09 native portrait reused unchanged
    [short] B11 native portrait reused unchanged

No frame was re-rendered, cropped from a wider aspect, or up/down-sampled.
Every `mp3/beat-<bid>.mp3` was copied independently (no symlinks). The
`--no-endcard --no-outro-rewrite` flags were passed so the parent's outro
narration is preserved as the final beat and no silent branded card is
appended.

## Compiler run

`python3 runtime/scripts/compile.py <reel> --height 3840 --out <reel>/exports/short`
returned 0 with all seven beats stamped VIDEO. No `--review` pass used.
Compiler skin-lint warnings for `B00` (`ClaudeComposerAsk916` cold open)
and `B11` (`ClaudeTitleOutro916` outro) are inherited from the parent long —
those pattern names are the shipped 916 compositions in `Root.tsx`; the
compile-time linter looks for the base names and is a known false positive
documented in the parent's CHECKS-REPORT.md.

## Audio decode

Decoded to 22050 Hz mono WAV (`_qc/audio/track.wav`), duration
107.6267 s (matches container within one sample). Boundary RMS at every
kept beat join is well above the silence floor (voice active into and out of
each join). The six inter-beat silences (0.64–0.68 s each) are the parent's
natural per-beat lead-in silence, preserved unchanged. One additional
in-beat pause at ~38.8 s inside B04 (between "put the right hit at the top"
and "Four rules") is source narration, not a cut artefact. Final tail
silence 0.67 s (106.96 → 107.63 s) sits under the outro card's hold.

## Portrait-frame QC

- 2 fps contact-strip: 215 frames in `_qc/frames/f-*.jpg` (107.5 s × 2 fps).
- Beat-relative frames at 15% / 50% / 85%: 21 frames in `_qc/beats/`
  (7 beats × 3 timestamps), extracted at 720 × 1280.
- Boundary frames: 14 frames in `_qc/joins/` (start + each transition + end),
  extracted at 540 × 960.
- All frames viewed. Every kept beat is a native 2160 × 3840 render, not
  a landscape crop; typography reads at BLUF scale; the outro card lands
  with `@NikBearBrown` and the slug-seeded mascot.

## Findings

- **BLOCKER: 0**
- **MAJOR:  0**
- **MINOR: 1** — Inherited right-edge clipping in the `ClaudeCodeBeat916`
  template affects three retained beats (B04 ranker code, B05 money-query
  output, B08 miss doctrine). Long code / output lines run past the code
  card's right clip on the parent's native portrait render (e.g. `svg/mo`
  truncated from `svg/money-square.svg`, `svg/ba` from `svg/banknote.svg`,
  `commo` from `common one`, `documen` from `document frequency (IDF):`).
  These frames were shipped in the parent (Ep 24, Gate-V clean per the
  playlist review) and are copied byte-for-byte into this Short — the
  Short cut cannot fix them without re-rendering the parent's ClaudeCodeBeat916
  scenes, which is out of scope (parent is read-only). The narration reads
  the full form aloud in every case, so meaning is preserved on-audio.

## Editorial adjacencies

- Opening (B00) introduces Liam-in-for-Bear and states the library-first
  thesis. Outro (B11) closes with the title restate and Liam disclosure.
- B01 → B04 join: "the difference this whole reel turns on." → "The ranker
  has one job:" — clean thesis-to-mechanism.
- B04 → B05: "'sankey flow' finds chart-sankey and not every flower" → "Here
  is the shape on a real query." — theory-to-example.
- B05 → B08: "…tokens the ranker matched." → "And here is what a miss looks
  like." — worked-hit to worked-miss.
- B08 → B09: "'nothing fits' is the real answer." → "So the surface." —
  falsifiability to full-surface summary.
- B09 → B11: verdict artifact list → title restate. No dangling numbered
  transition; no repeated conclusion; no removed caveat.

The B09 verdict names every dropped-beat feature (`--check`, `--show`,
`--brands`, `--no-brands`, dispatcher aliases, bare-invocation banner) with
enough definition that the summary stands alone.

## What this Short covers vs the long

- Kept: library-first thesis · misconception correction · IDF ranker
  mechanism · one worked query · the miss · full-surface verdict · outro.
- Deferred to the 16:9 long (`../../claude-liam-brutalist-command-icons`):
  dispatcher case-statement code walk (B02), full icons.json geometry
  walk (B03), `--check`/`--show` worked example (B06), `--brands`
  filter worked example (B07), extended "Your turn" audit prompt (B10).

## Human review

- No human reviewer signed off on this Short. The parent long's
  VISUAL-REVIEW.json is not carried across; a fresh AI review for this
  Short is at `VISUAL-REVIEW.json` with this invocation's `run_id` and
  the actual Short's beat-sheet + video hashes. Publication and playlist
  scheduling remain a separate human workflow — no upload was performed.
