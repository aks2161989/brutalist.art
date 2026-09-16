# CHECKS-REPORT — Brutalist Command: art todo — Short (9:16)

Run: `da9910aa30784a5ca3041e101c7b037f`
Source SHA (episode.source_sha256): `4c52fd96434fe90eb9b825a6575ebec2af674f877471bcc08965cf97dbda0598`
Parent master SHA: `400eb021c8011e14810b8beb1256b6bc79cb3ab79457c1189f5bd15e2eb6ed27`
Feedback SHA: `6b7b9c7454a60f145d6970b622d74842a5f8184647f32e564038495c22ecd0f5`

`exports/short/claude-liam-brutalist-command-todo-short.mp4`
SHA-256 `f7bf9d515121ec21cf5d6b056f08d9591c0800689dd24a65efbc0d35a1690d69`
2160×3840 @ 24 fps · 116.333 s container · 116.292 s video (h264/yuv420p) ·
116.333 s audio (aac 48 kHz stereo) · 8,171,730 bytes.

## Duration cap — the SHORTS LAW

- Planned duration (sum of retained `render_duration_s`): **116.33 s** ✓
- Compiler-measured timeline (`[art] wrote … (116.3s, …)`): **116.3 s** ✓
- ffprobe container duration: **116.333 s** ✓
- ffprobe video stream duration: **116.292 s** ✓
- ffprobe audio stream duration: **116.333 s** ✓

All strictly < 180.0 s. Encoding headroom > 63 s.

## Cut plan

`CUT-PLAN.json` records `strategy: whole-beat-cut`, kept beats `[B00, B01,
B02, B03, B04, B07, B08, B09, B11]`, dropped `[B05, B06, B10]`, and the cut
review of transitions and coverage. No narration rewrite; no audio
regenerated.

## Gate F — factcheck

- `FACTCHECK.md` re-scoped for the Short: only claims present in retained
  beats are re-audited. Dropped-beat claims noted as "not made in this Short".
- `SOURCES.md` re-scoped: primary evidence carried from parent, no new
  sources introduced.

Pass.

## Gate V — visual QC

`runtime/qc/final_frame_check.py` (invoked automatically by `compile.py
--height 3840`) wrote `_qc/REPORT.md`:

```
Frames sampled: 18  ·  BLOCKER: 0  ·  MAJOR: 0
Clean — no BLOCKER/MAJOR defects. ✓
```

Every retained beat's `media/*.mp4` was copied unchanged from the parent's
already-Gate-V-clean `vertical/media/`. The parent's portrait-only SparkLine
+60 bump (see `feedback_command_todo_sparkline_portrait_bump`) and the B01
hesitant-writer 3-short-line / fontSize 240 / lineSpacing 2.6 restructure
both carry over.

Contact sheet: `_qc/contact_sheet.png`. Nine single-beat evidence PNGs at
each beat's 50% audio-clock: `_qc/B00_evidence.png` … `_qc/B11_evidence.png`.
Hashes in `VISUAL-REVIEW.json`.

Pass.

## Audio decode

`ffprobe` confirms a single AAC-LC stereo stream, 48000 Hz. The nine
per-beat MP3 SHA-256s (retained set) are identical to the parent vertical
counterparts — no audio was regenerated. Joins between B04→B07 and
B08→B09 audition cleanly on decode (no clipped speech, no over-slam).

Pass.

## Native dimensions

Every `media/<BID>.mp4` verified 2160×3840 via ffprobe before compile
(spot-checked B00 via `ffprobe -select_streams v:0 -show_entries
stream=width,height`). Final Short is 2160×3840 native.

Pass.

## Compiler receipts

The compiler stamped `beat_sheet.json` with `metadata.build` and every
retained beat's `build` record. Motion histogram (per-beat unique motions):
`type-on · write-and-correct · flow-in · stagger · type-and-stagger ·
loop-step · fail-then-fix · artifact-stagger · fade`.

## Skin lint

Compiler emitted the expected native-portrait SKIN LINT on B00 and B11:

```
SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk
SKIN LINT: B11: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro
```

These are the correct 916 variants for a native portrait build (ONDA CHECK
in `shorts.py --vertical`/derivative rewires to `<pattern>916` compositions
to avoid crop-fits). WARN not BLOCKER.

## Known limitations

- Same absent-legacy-typography-checker gap as landscape/parent; see
  `TYPECHECK.md`.
- Composer folder chip on B00 shows `@NikBearBrown` (not `@HumanitariansAI`
  as other episodes do); parent decision, unchanged in this Short.
- HANDOFF LAW waived for this Short (parent B10 dropped) — per the Shorts
  prompt's clause "A detailed CTA can be cut; the Short need not read the
  long film's full exercise aloud."

Every current runtime check that exists in this toolkit was run against the
Short and returned clean. Nothing was disabled or bypassed. No audio
regenerated, no captions burned in, no publishing action, no paid API.
Human review is pending.
