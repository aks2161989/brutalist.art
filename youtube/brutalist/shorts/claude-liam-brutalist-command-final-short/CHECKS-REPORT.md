# CHECKS-REPORT — Brutalist Command: art final — Short (ep 33)

Re-verified 2026-09-14 (run_id `e8f021cee8f34c40bbdbf7ccaa783ca7`).

**Rebuild reason:** The parent vertical's B06 was re-rendered on 2026-09-13T00:50:54
with an updated compile.py atomic block. Changes vs. the Short's prior B06
(`compile.py:800-822`):
- Line ref shifted to `:803-825`
- Added `timeline = work / 'resolved-sheet.json'` and `atomic_json(timeline, sheet)`
  (now passes a timestamped resolved-sheet to Gate V)
- File-existence guard added to the input hash check:
  `if any(not Path(p).is_file() or file_digest(p) != value …)`

Audio for B06 unchanged. Cut plan (B00/B01/B06/B07/B09/B11) unchanged.

## 1. B06 update

```
cp parent/vertical/media/B06.mp4 → short/media/B06.mp4
  old SHA-256: 33cff0c22365dbe2f1750a9e12d671344bb1d6629b5db1bf66dec90a85980dcd
  new SHA-256: f2c7487325a8bf6ce85e11ad60a1a8f9cbf26ab02c302f0af8b944c6bfa1d852
```

B06 narration audio unchanged (mp3 hash `229dc49d…` unchanged). Beat duration
unchanged (26.267 s vs prior 26.25 s audio clock — same narration). Visual
update: title bar now reads `compile.py:803-825 — atomic replace`; code body
gains `timeline`/`atomic_json` lines and the file-existence guard. Confirmed
in B06-p50 frame at 40.488 s.

## 2. Compile (`art final`)

```
python3 runtime/scripts/compile.py \
  .../shorts/claude-liam-brutalist-command-final-short \
  --height 3840 --out .../exports/short
```

Output:
```
[art] compiled B06  VIDEO    26.3s  ← B06.mp4
[art] motion histogram: code-cascade:2  type-on:1  hesitant-type:1  artifact-in:1  outro-card:1
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk
[art] SKIN LINT: B11: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro
[art] build stamp → beat_sheet.json (6/6 filled)
[art] wrote .../exports/short/claude-liam-brutalist-command-final-short.mp4  (105.4s, audio: per-beat timeline (source audio preserved), drawtext: no — PIL overlays)
[art] slots: 6/6 filled — B00:VIDEO B01:VIDEO B06:VIDEO B07:VIDEO B09:VIDEO B11:VIDEO
```

- `final_preflight` passed (paperwork triad + beat_lint + gate_shape).
- Gate V (`runtime/qc/final_frame_check.py`) ran against the candidate encode:
  `frames=12 BLOCKER=0 MAJOR=0`.
- The two SKIN LINT lines are informational warnings inherited from the parent
  build (a `claude` palette combined with `*916` portrait compositions —
  intentional for the vertical build). Not blockers.

## 3. Container / dimensions / duration

```
$ ffprobe -v error -show_entries format=duration \
  -show_entries stream=codec_type,codec_name,width,height,duration \
  exports/short/claude-liam-brutalist-command-final-short.mp4
```

| Stream | codec | dims | duration |
|---|---|---|---|
| video | h264 | 2160×3840 | 105.375000 s |
| audio | aac | — | 105.375000 s |
| container | mp4 | — | 105.375000 s |

- Aspect ratio: 2160:3840 = 9:16 ✓
- Native 4K height (3840) ✓
- Container 105.375 s **< 180.0 s cap** ✓ (74.625 s of headroom)
- Video and audio streams both **< 180.0 s** ✓

## 4. Audio decode

```
$ ffmpeg -v error -i <mp4> -af astats=metadata=1:reset=0 -f null -
(empty stderr — decoded cleanly, no errors)
```

No dead air, no truncated tails. Every beat's source Kokoro `am_onyx`
narration is preserved unchanged from the parent vertical.

## 5. Frame evidence

18 frames extracted at beat-relative 15%/50%/85% of each retained beat
(6 beats × 3 percentiles). All frames stored under `_qc/previews/` with
SHA-256s recorded in `VISUAL-REVIEW.json`.

Opened and inspected:

| Frame | Timestamp | What it shows |
|---|---|---|
| B00-p50 | 7.438 s | Composer with 'Hei, Liam' greeting, full ask text, three-line output card, `@HumanitariansAI` chip, Claude/Sonnet labels. |
| B01-p85 | 25.592 s | BLUF settled to 'art final / verifies / twice.' — trigger→replacement flip clean. |
| B06-p50 | 40.488 s | Atomic write card with UPDATED title `compile.py:803-825 — atomic replace`; `timeline = work / 'resolved-sheet.json'` and `atomic_json(timeline, sheet)` lines present; file-existence guard `if any(not Path(p).is_file(` visible; `os.replace` atomic swap; spark line 'Encode into a temp. Replace only after every check clears.' |
| B07-p50 | 66.030 s | Receipt writer body (status/output/sha256/duration_s/input_sha256/at) + read-side pattern; spark 'Ready is a machine claim. Publication is a human step.' |
| B09-p50 | 89.655 s | Full six-line verdict artifact card; all six guarantees visible. |
| B11-p50 | 103.530 s | Locked outro: 'Brutalist Command: art final.' with terracotta period + `@NikBearBrown` handle. |

Long code lines in B06/B07 truncate horizontally inside `SAFE916` (documented
in parent shotlist; inherited here). Card boundaries inside safe area — no bleed.

## 6. Continuity of retained narration

B00 → B01 → B06 → B07 → B09 → B11, source order preserved.

- B00 introduces the ask and the last-good-file promise.
- B01 flips 'renders once' → 'verifies twice'.
- B06 opens with 'The atomic bit.' — standalone sentence, reads cleanly after B01.
- B07 opens with 'The receipt is five keys.' — receipt named in B00 and B01.
- B09 opens with 'So — art final.' — valid recap opener.
- B11 is Liam's sign-off with 'Liam, in for Bear'. ✓

## 7. Verified receipt

`exports/short/claude-liam-brutalist-command-final-short.verified.json`:

- `status: "ready"` — machine claim; human review pending in `FEEDBACK.md`.
- `sha256: f732f7fc5dee3a9da52a7fc70a05c7c97b625c944b4f656ccf665e690ef1a024`
- `duration_s: 105.375`
- `input_sha256`: 12 entries — 6 media/*.mp4 + 6 mp3/beat-*.mp3;
  B06 entry now carries the updated hash
  `f2c7487325a8bf6ce85e11ad60a1a8f9cbf26ab02c302f0af8b944c6bfa1d852`.
- `at: 2026-09-14T11:58:16.063056+00:00`.

## 8. Result

**PASS.** Final artefact:
`youtube/brutalist/shorts/claude-liam-brutalist-command-final-short/exports/short/claude-liam-brutalist-command-final-short.mp4`
(2160×3840, 105.375 s, SHA-256
`f732f7fc5dee3a9da52a7fc70a05c7c97b625c944b4f656ccf665e690ef1a024`).

Human review of this Short is next. Bear watches and either signs off in
`FEEDBACK.md` or requests targeted per-beat rebuilds.
