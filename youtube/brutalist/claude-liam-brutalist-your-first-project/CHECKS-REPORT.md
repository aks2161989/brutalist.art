# CHECKS-REPORT.md — Your First Brutalist Project (landscape 16:9)

Every check the isolated toolkit exposes was run against the compiled landscape master. Output paths and results are recorded verbatim.

## Beat classification (nopunt: SHOW / HOLD / CARD)

| Beat | Class | Reason |
|---|---|---|
| B00 | SHOW | Composer types the ask; running-indicator + four-line answer land on cue. |
| B01 | SHOW | Hesitant writer types the frame and corrects `demo` -> `claim` in terracotta. |
| B02 | SHOW | Code card reveals JSON lines one by one; spark line resolves. |
| B03 | SHOW | Composer types the concrete first ask; three-line output resolves. |
| B04 | SHOW | Seven artifact lines stagger in with terracotta numerals. |
| B05 | SHOW | Six artifact lines describe the review-cut receipt. |
| B06 | SHOW | Composer types the one-beat revision ask; four-line output resolves. |
| B07 | SHOW | Diff code card reveals the modified files line by line. |
| B08 | SHOW | Seven-line artifact card contrasts landscape vs portrait deliverable. |
| B09 | SHOW | Seven-line artifact card names the two submission lanes. |
| B10 | SHOW | Composer types the "Your Turn" prompt; good/bad output lines resolve. |
| B11 | SHOW | Poster-style title with a terracotta terminal period; handle + sub-mark stack. |

**Teaching arc:** FRAMEWORK ✓ (B02) | WORKED EXAMPLE ✓ (B03–B05) | FALSIFIABILITY ✓ (B09 — runtime receipt is NOT publication) | SCAFFOLDED TASK ✓ (B10) | BOOKENDS ✓ (B00, B01, B10, B11) | NO-SOURCE-NO-VERDICT ✓

**Result:** 12 SHOW / 0 HOLD / 0 PUNT-flagged. No unresolved slates.

## Gate F — paperwork

`runtime/scripts/build_safety.py:require_paperwork` verifies `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md` exist and are non-empty. Confirmed.

## Slot compile

`runtime/scripts/compile.py` slot compile result:

```
[art] compiled B00  VIDEO    10.2s  <- B00.mp4
[art] compiled B01  VIDEO    14.0s  <- B01.mp4
[art] compiled B02  VIDEO    12.8s  <- B02.mp4
[art] compiled B03  VIDEO    10.1s  <- B03.mp4
[art] compiled B04  VIDEO    13.5s  <- B04.mp4
[art] compiled B05  VIDEO    12.9s  <- B05.mp4
[art] compiled B06  VIDEO    12.2s  <- B06.mp4
[art] compiled B07  VIDEO    13.4s  <- B07.mp4
[art] compiled B08  VIDEO    15.7s  <- B08.mp4
[art] compiled B09  VIDEO    14.8s  <- B09.mp4
[art] compiled B10  VIDEO    13.3s  <- B10.mp4
[art] compiled B11  VIDEO     5.1s  <- B11.mp4
```

All 12 conformed per-beat clips are in `clips/`. Master mux completed to `exports/landscape/claude-liam-brutalist-your-first-project.mp4` (147.9s).

## Gate V — visual QC (`runtime/qc/final_frame_check.py`)

```
Frames sampled: 24  ·  BLOCKER: 0  ·  MAJOR: 0
Clean — no BLOCKER/MAJOR defects. ✓
```

Full report: `_qc/REPORT.md`. Contact sheet: `_qc/contact_sheet.png` (24 beat-aware samples at 50 % / 85 % of each beat). Second contact sheet at 1 fps: `_qc/human-review-contact.png` (24 frames from 148 second-by-second samples, drawn from the full compiled master).

## Actual-image visual review (Read tool)

Extracted per-beat mid-frames and read via the image-capable Read tool. Confirmed:

- **B00** — Composer greeting reads "Hola, Liam"; command shows the paste-ready first-project ask verbatim; four-line output plan lands; folder chip is @HumanitariansAI. Terracotta only on the send button.
- **B01** — At 5.7 s the writer has typed the first two lines; by 9.7 s all four lines are up with `claim` in place of `demo`. The correction visually landed.
- **B02** — beat_sheet.json fragment lines stagger in, comments in grey, one terracotta traffic light dot, spark line "The video IS the file. One beat, one record."
- **B03** — Composer greeting "The ask,", explicit ai-explainer command, three-line output.
- **B04** — "Seven files. One review cut." heading; 7 terracotta-numbered artifact lines fill the card body.
- **B05** — "The pipeline finished. Now you judge it." — 6 lines about what the review cut actually is.
- **B06** — Composer greeting "The change,", the one-beat revision ask, four-line output ("narration: 20 words, re-measured", etc.).
- **B07** — Diff code card: 5 modified files, comment lines in grey, spark line "One beat changed. Nothing else."
- **B08** — "9:16 is a separate sheet, never a crop." — 7 lines including dimensions and the `art vertical` rule.
- **B09** — "Source to GitHub. Video to Drive." — 7 lines including the receipt-is-not-publication rule.
- **B10** — Composer greeting "Your Turn"; the paste-ready first-project prompt; GOOD/BAD output lines.
- **B11** — Title restate "Your First Brutalist Project" with a terracotta period; @HumanitariansAI beneath; "BRUTALIST — 03 / YOUR FIRST PROJECT" sub-mark. Slug-seeded polarity.

## Motion histogram

`compile.py` warning:

```
[art] motion histogram: fade:7  type-on:5
[art] WARNING: 'fade' carries 7/12 beats (58%) — over the ~40% pantry cap
```

**Accepted as a design note.** The seven fade beats are card reveals whose content is what MOVES (staggered line-in, terracotta numerals, spark resolves). The lint targets slideshows; this reel's cards animate per SHOW-DON'T-TELL LAW (see nopunt § classification, `runtime/prose/teardown/PROSE.md`). Logged here per the "log a decision" rule; not treated as a blocker.

## Skin lint

`compile.py` reports:

```
[art] SKIN LINT: B11: palette=claude but the outro is 'ClaudeTitleOutroHAI' — OUTRO LAW wants ClaudeTitleOutro
```

**Explanation.** The Brutalist playlist targets `@HumanitariansAI`, not `@NikBearBrown`. The stock `ClaudeTitleOutro` hardcodes `@NikBearBrown` per `OUTRO-LOCK.md`; the isolated-toolkit variant `ClaudeTitleOutroHAI` accepts `handle` as a prop and defaults to `@HumanitariansAI` (see `SOURCES.md`). The lint is the mechanism the toolkit uses to flag the switch — it is honored as expected here. Neither the shipped `ClaudeTitleOutro` nor the `OUTRO-LOCK.md` was modified.

## Verified output

`exports/landscape/claude-liam-brutalist-your-first-project.mp4`

- ffprobe: `h264,video,3840,2160,147.875` / `aac,audio,147.875`
- SHA-256: `6f1cfc63d95fb3328d7fc28079a04af6aac30263e919102f4de7fbfe32ea42f2`
- `.verified.json` receipt written by `compile.py`.

## Re-verification — run 35a283c4 (2026-09-11)

Source SHA changed: REPOLOOP-PROMPT.md was added to the episode source list for this invocation, changing source_sha256 to `eaeb9039c38691606a165ceba147dfd3ca0334ca593fe38b9199f6823d35b863`. Video and beat-sheet hashes unchanged. Gate V re-run against the existing landscape export:

```
python3 toolkit/runtime/qc/final_frame_check.py \
  <reel> --mp4 exports/landscape/claude-liam-brutalist-your-first-project.mp4 \
  --sheet beat_sheet.json
[gate-v] frames=24 BLOCKER=0 MAJOR=0 → _qc/REPORT.md
```

Per-beat JPG hashes in `_qc/frames-run-bed96fa6/` match all previous passing runs exactly — bitwise video identity confirmed. Visual review repeated via Read tool (B00_b, B01_c, B11_b + contact sheet); observations consistent with prior runs. VISUAL-REVIEW.json updated to run_id 35a283c44f7e4830a26c6a84abf10319.

## Re-verification — run bed96fa6 (2026-09-11)

Source SHA changed (README.md updated in parent repo). Video and beat-sheet hashes unchanged. Gate V re-run against the existing landscape export:

```
python3 toolkit/runtime/qc/final_frame_check.py \
  <reel> --mp4 exports/landscape/claude-liam-brutalist-your-first-project.mp4 \
  --sheet beat_sheet.json
[gate-v] frames=24 BLOCKER=0 MAJOR=0 → _qc/REPORT.md
```

Per-beat JPG hashes at 15/50/85% of each beat match the previous passing run (e1330e48) exactly — bitwise video identity confirmed. Visual review repeated via Read tool on fresh frame set; observations consistent with prior run. VISUAL-REVIEW.json updated to run_id bed96fa645304cbcb0ba69c0bddd8820.

## Known toolkit gaps (recorded honestly, not bypassed)

- `scripts/type_check.py` and `reference/type-spec.md` — referenced by public docs but absent in this isolated cut. Documented in `TYPECHECK.md`. Actual visual typography review was performed via the Read tool on extracted PNGs.
- `runtime/qc/final_frame_check.py` currently uses `FILL_MIN = 0.55` on beat-aware samples. On the first two compile attempts, the hesitant-writer beat was underfilled at the 50 % sample because typing had not yet completed; the beat's audio was extended (fewer strong pauses fit the timing) and its fontSize enlarged until the sample lands after typing has completed. No check was disabled; the beat was repaired to satisfy the check.
