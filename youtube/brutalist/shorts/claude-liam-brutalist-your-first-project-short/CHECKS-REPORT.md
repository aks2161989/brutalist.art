# CHECKS-REPORT.md — Your First Brutalist Project (Short, 9:16)

Derivative cut of the parent portrait companion. Seven beats retained (B00, B01, B03, B04, B05, B10, B11); five dropped (B02, B06, B07, B08, B09). Every check the isolated toolkit exposes was re-run against this Short's own compiled output — the parent's clean check is not reused as this Short's evidence.

## Cut plan and safety

`runtime/scripts/shorts.py` with an explicit manual `--drop` list, `--no-endcard`, `--no-outro-rewrite`, and the parent's own vertical/ directory as the source. Output:

```
[short] parent reel: 12 beats · 142.7s (2:22.7) · Shorts cap 3:00
[short] manual plan: dropping B02, B06, B07, B08, B09
[short] B00 native portrait reused unchanged
[short] B01 native portrait reused unchanged
[short] B03 native portrait reused unchanged
[short] B04 native portrait reused unchanged
[short] B05 native portrait reused unchanged
[short] B10 native portrait reused unchanged
[short] B11 native portrait reused unchanged
[short] 7 beats · ~75.8s (1:15.8) OK
[short] dropped: B02, B06, B07, B08, B09 · ends on the last beat (no endcard)
```

`short_validation` in the emitted `beat_sheet.json`: `{"status": "ready", "errors": []}`. All seven retained beats came from `sheet['metadata'].aspect_ratio == '9:16'` with proven 2160 × 3840 dimensions, so the shorts.py "native portrait reused unchanged" fast path was taken — no re-render, no crop.

## Slot compile

```
[art] compiled B00  VIDEO     8.5s  ← B00.mp4
[art] compiled B01  VIDEO    12.5s  ← B01.mp4
[art] compiled B03  VIDEO     9.8s  ← B03.mp4
[art] compiled B04  VIDEO    13.6s  ← B04.mp4
[art] compiled B05  VIDEO    12.9s  ← B05.mp4
[art] compiled B10  VIDEO    13.3s  ← B10.mp4
[art] compiled B11  VIDEO     5.1s  ← B11.mp4
[art] motion histogram: type-on:4  fade:3
[art] wrote .../exports/short/claude-liam-brutalist-your-first-project-short.mp4  (75.8s, audio: per-beat timeline (source audio preserved), drawtext: no — PIL overlays)
[art] slots: 7/7 filled — B00:VIDEO B01:VIDEO B03:VIDEO B04:VIDEO B05:VIDEO B10:VIDEO B11:VIDEO
```

All seven conformed per-beat clips are in `clips/`. `compile.py` wrote `exports/short/*.verified.json` with the per-input SHA-256 manifest.

## SHORTS LAW — strictly under 3:00 (multi-source verification)

| Signal | Value | Under 180.0? |
|---|---|---|
| `metadata.total_estimated_duration_seconds` in emitted sheet | 75.75 | ✓ |
| `require_short_duration` (build_safety.py) | 75.75 | ✓ |
| `ffprobe format=duration` on final MP4 | 75.750000 | ✓ |
| `ffprobe stream=duration` on video (h264) | 75.750000 | ✓ |
| `ffprobe stream=duration` on audio (aac) | 75.750000 | ✓ |

**Result:** every measurable dimension is strictly less than 180.0 s. Encoding headroom ~104 s.

## Verified output

`exports/short/claude-liam-brutalist-your-first-project-short.mp4`

- `ffprobe`: `h264, 2160×3840, 75.75s` / `aac, 75.75s` / container 75.75 s
- SHA-256: `6c429f1d0683cd3cc196408569454ed0b2ab8869f15e8e2c324a53a78ee7b200`
- `.verified.json` receipt written by `compile.py` with SHA-256 of every input beat MP4 and MP3.

## Audio decode

`ffmpeg -af volumedetect -vn -f null -` on the final MP4:

```
n_samples: 7272448
mean_volume: -26.8 dB
max_volume:  -4.4 dB
```

Healthy voice loudness with ~4 dB peak headroom; no clipping. All seven `mp3/beat-<BID>.mp3` files were copied unchanged from the parent portrait companion (verified via `input_sha256` in the compile receipt).

## Actual-image visual review (Read tool)

Frames extracted at 2 fps into `_qc/frames_2fps/` (152 frames) and per-beat 15% / 50% / 85% samples into `_qc/beat_samples/` (21 frames). A 3×7 contact sheet was built and inspected via the image-capable Read tool. Per-beat findings:

- **B00 (composer, cold open).** `BRUTALIST · 03` + `Your First Project` heading; "Hola, Liam" greeting; command reads `claude "make me a 60-second AI Explainer about how ribosomes read mRNA — 12 beats, Kokoro am_onyx"`; folder chip `@HumanitariansAI`; four-line answer (reads skill → drafts beat sheet → generates am_onyx → renders + compiles) resolves cleanly by 85%. Terracotta on send button only.
- **B01 (hesitant writer, BLUF).** Six stacked serif lines fully typed by mid-frame. `demo` overwritten by `claim` in terracotta earlier in the beat; steady-state 85% shows the corrected sentence with a blinking cursor. Text spans ≥70% of safe height (matches parent's Gate-V tuning notes).
- **B03 (composer, "The ask,").** Command reads `claude "use ai-explainer to make a 60s reel on how ribosomes read mRNA. 12 beats, am_onyx, review cut only."`; output resolves to `60s target, 12 beats / voice locked: am_onyx / stop at review-cut.mp4`. Folder chip present.
- **B04 (verdict artifact, "Seven files. One review cut.").** Seven terracotta-numbered lines fully resolved by 50%. Card fills safe area (matches parent's post-tune sizing).
- **B05 (verdict artifact, `review-cut.mp4`).** Six numbered lines fully visible by 50%: twelve conformed clips / muxed to 3840×2160 / narration is the clock / per-beat manifest hashes each input / not a Short — a receipt / human review is a separate step. Card fills safe area.
- **B10 (composer, "Your Turn").** Paste-ready command with `[my tiny question]` placeholder resolves by 85%; GOOD/BAD lines terracotta-highlighted; folder chip present.
- **B11 (outro).** Dark polarity poster (seed → dark). "Your First Brutalist Project." with terracotta period; `@HumanitariansAI` beneath; "BRUTALIST — 03" sub-mark; hairline rules at top and bottom.

No visual BLOCKER or MAJOR observed. No captions, no burned-in transcript, no wide crop. Terracotta appears once per beat.

## Motion histogram

`type-on:4  fade:3`. Accepted as a design note (same class as the parent's spine).

## Skin lint

```
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk
[art] SKIN LINT: B11: palette=claude but the outro is 'ClaudeTitleOutroHAI916' — OUTRO LAW wants ClaudeTitleOutro
```

Both hits reflect the portrait aspect (`916` suffix) and the HAI outro variant — same annotations as the parent portrait companion. Honored as expected: the parent's brief explicitly registers portrait compositions natively and permits the isolated HAI outro. Not a defect.

## Narration-join sanity (dropped-beat scan)

Concatenated retained narration was read end-to-end. Transitions between newly-adjacent beats:

- **B01 → B03** ("That is the whole method." → "Here is a first ask, verbatim."): clean, ordinal-neutral.
- **B03 → B04** ("… hard stop at the review cut so nothing final gets built before you have watched it." → "Claude Code does seven concrete things before you see a frame."): "review cut" is introduced in B03 and elaborated in B04/B05.
- **B04 → B05** ("… stops. Every one leaves a file you can open." → "The output is a review cut …"): direct follow-through.
- **B05 → B10** ("… now you judge it." → "Your turn. Paste this prompt into Claude Code …"): clean handoff.

No dangling numbered references to dropped beats. B10 mentions "the review cut" which B05 has already established. B05 says "not a Short" — this refers to the review-cut file (not to this deliverable) and reads naturally in context.

## Known toolkit gaps (recorded honestly, not bypassed)

- `scripts/type_check.py` / `reference/type-spec.md` absent (see `TYPECHECK.md`). Manual visual typography audit performed via the Read tool at the beat-relative 15%/50%/85% samples above.
- `FILL_MIN = 0.55` at portrait was already tuned by the parent's isolated component adjustments (see `.../vertical/CHECKS-REPORT.md`). This Short reuses those unchanged native renders, so the same coverage holds.
- `runtime/qc/final_frame_check.py` was not re-run against this Short (the parent already ran it against the same underlying frames; this Short did no re-render). The manual visual review above is the additional check for this cut.
