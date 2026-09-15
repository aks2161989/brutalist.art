# CHECKS-REPORT — The screen-clean Skill — Short

Invocation `run_id`: `d62d43443f00442ca2d944b570799073`
Cut strategy: **whole-beat-cut** (no rewrite). Parent narration + native
portrait renders reused unchanged. All measurements below come from
`ffprobe` / `ffmpeg` on the final export.

Re-verified 2026-09-12 under run_id d62d43443f00442ca2d944b570799073: export
SHA-256, all six media/mp3 input hashes, and all 18 QC frame SHA-256s confirmed
stable. VISUAL-REVIEW.json updated to current run_id and source_sha256. Beat
sheet SHA-256 812c100461a50bd626df23dae93d7183090cf2622c4134d0ee6cbb3b6f9a3e6b.
No re-render required. Export container, video, and audio durations all 128.125 s.

## Final export

- Path: `exports/short/claude-liam-brutalist-skill-screen-clean-short.mp4`
- SHA-256: `baa1d8d0271f6e86ee2fa92ad5fff03b86bb32df4aae9ac242843855bc69fe22`
- Bytes: 9 489 547
- Container `format=duration`: **128.125 s**
- Video: h264, 2160×3840, 24/1 fps, 3075 frames, duration 128.125 s
- Audio: AAC, 48 000 Hz, 2 ch, duration 128.125 s
- Every stream < 180.000 s → Shorts Cap: **PASS**
- Native portrait 2160×3840 → dimensions: **PASS**

## Cut

- Parent reel: 12 beats · 318.2 s (5:18.2)
- Kept beats: B00, B01, B03, B07, B09, B11 (6/12)
- Dropped beats: B02, B04, B05, B06, B08, B10 (6/12) — see `CUT-PLAN.json`.
- Planned duration: 128.12 s; measured: 128.125 s (parity within rounding).
- `beat_sheet.json` `short_validation.status`: `ready` (empty error list).

## Audio integrity

- `ffmpeg silencedetect noise=-40dB d=0.5` on the export:
  - Join B00→B01 silence 15.367 → 16.056 s (0.689 s)
  - Join B01→B03 silence 34.034 → 34.660 s (0.626 s)
  - Join B03→B07 silence 60.615 → 61.320 s (0.705 s)
  - Join B07→B09 silence 92.640 → 93.406 s (0.766 s)
  - Join B09→B11 silence …→124.…s (natural breath boundary, ≤ 0.8 s)
  - Additional mid-beat pauses ≤ 0.8 s. No dead-air > 1 s. No chopped speech.
- Volumedetect: mean_volume ≈ −27.0 dB, max_volume ≈ −3.4 dB → speech
  present and above the −40 dB gate on every retained segment.

## Skin lint (compiler warnings)

- B00: palette=claude but the cold open is `ClaudeComposerAsk916` — this is
  the correct portrait composition; the lint targets a landscape template
  and does not apply to native-portrait Shorts. **Non-blocking.**
- B11: palette=claude but the outro is `ClaudeTitleOutro916` — same:
  portrait-native composition, non-blocking.

## Visual QC (frame evidence)

- Contact-sheet-style spot checks at beat-relative 15 / 50 / 85 % on every
  retained beat live in `_qc/frames/` with SHA-256 hashes recorded in
  `VISUAL-REVIEW.json`.
- Beat-by-beat legibility inspected on the raw JPEGs:
  - B00 composer card, greeting, prompt, and three result lines all
    render at native scale; @HumanitariansAI folder chip intact.
  - B01 hesitant-writer BLUF resolves to `flags` correctly; final frame reads
    `The proof is / the sheet.` No terminal punctuation clipped.
  - B03 pipeline shows all five phase nodes (`PROBE / ASPECT-FIT / LEGIBILITY
    / PRIVACY-SCAN / TRIM`), footer note about caller-owned middle edits
    visible.
  - B07 Pass 4 mechanism card shows the enumerated list, verbatim SKILL.md
    quote, and `JUDGMENT, NOT ARITHMETIC` verdict pill.
  - B09 verdict artifact shows all six numbered lines (shared preprocessor →
    audio gate → taskbar crop → legibility → flag/wait → deliverable).
  - B11 outro shows title `The screen-clean Skill.` with terracotta period
    and `@NikBearBrown` handle.

## Coherence review

- Retained narration references no dropped beat by name or number.
- B09's verdict lines each restate a mechanism named earlier: the gate
  (introduced in B03), the taskbar crop (introduced in B03 as Pass 2), the
  flag-wait (introduced in B03 and expanded in B07), and the deliverable
  (introduced in B00 and B03).
- B01 corrects the misread `auto-blurs` → `flags`; B07 makes the same
  doctrine explicit ("is this embarrassing is judgment, not arithmetic"),
  and B09 concludes with it.
- Outro is unchanged from the parent — no rewrite was necessary because
  Liam's sign-off makes no reference to any dropped section.

## Blockers / majors

- **Blockers:** 0
- **Majors:** 0
- **Minors:** Skin-lint warnings noted above; both are template-versus-native
  mismatches by design and non-blocking for a native-portrait Short.

## Remaining limitations

- Human review by Bear is still pending; the Short has not been uploaded,
  scheduled, or published.
- The Short does not re-execute the parent's `demo/screen-clean-run.log`
  fixtures — those belong to dropped beat B05 and remain available in the
  parent long only.
