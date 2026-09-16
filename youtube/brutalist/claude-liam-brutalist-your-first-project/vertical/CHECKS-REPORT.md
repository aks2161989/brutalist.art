# CHECKS-REPORT.md — Your First Brutalist Project (portrait 9:16)

The portrait companion is a re-authored beat sheet, not a crop. Every check the isolated toolkit exposes was run against the compiled portrait master.

## Beat classification (nopunt: SHOW / HOLD / CARD)

| Beat | Class | Reason |
|---|---|---|
| B00 | SHOW | Composer916 types the ask; four-line answer resolves in the portrait card. |
| B01 | SHOW | HesitantWriter916 types across 6 stacked lines and lands the demo->claim swap. |
| B02 | SHOW | CodeBeat916 reveals a narrow-wrapped JSON fragment line-by-line. |
| B03 | SHOW | Composer916 types the concrete first ask; three-line output resolves. |
| B04 | SHOW | VerdictArtifact916 staggers seven terracotta-numbered lines. |
| B05 | SHOW | VerdictArtifact916 staggers six lines about the review-cut receipt. |
| B06 | SHOW | Composer916 types the one-beat revision ask; four-line output resolves. |
| B07 | SHOW | CodeBeat916 reveals the diff — 5 modified files + comment lines. |
| B08 | SHOW | VerdictArtifact916 stacks seven landscape/portrait contrast lines. |
| B09 | SHOW | VerdictArtifact916 names the two submission lanes across seven lines. |
| B10 | SHOW | Composer916 types the Your Turn prompt; GOOD/BAD lines resolve. |
| B11 | SHOW | TitleOutroHAI916 restates the title, HAI handle, Brutalist-03 sub-mark. |

**Teaching arc:** FRAMEWORK ✓ (B02) | WORKED EXAMPLE ✓ (B03–B05) | FALSIFIABILITY ✓ (B09) | SCAFFOLDED TASK ✓ (B10) | BOOKENDS ✓ (B00, B01, B10, B11) | NO-SOURCE-NO-VERDICT ✓

**Result:** 12 SHOW / 0 HOLD / 0 PUNT-flagged. No unresolved slates.

## Slot compile

```
[art] compiled B00  VIDEO     8.5s  <- B00.mp4
[art] compiled B01  VIDEO    12.5s  <- B01.mp4
[art] compiled B02  VIDEO    10.9s  <- B02.mp4
[art] compiled B03  VIDEO     9.8s  <- B03.mp4
[art] compiled B04  VIDEO    13.6s  <- B04.mp4
[art] compiled B05  VIDEO    12.9s  <- B05.mp4
[art] compiled B06  VIDEO    12.2s  <- B06.mp4
[art] compiled B07  VIDEO    13.3s  <- B07.mp4
[art] compiled B08  VIDEO    15.7s  <- B08.mp4
[art] compiled B09  VIDEO    14.8s  <- B09.mp4
[art] compiled B10  VIDEO    13.3s  <- B10.mp4
[art] compiled B11  VIDEO     5.1s  <- B11.mp4
```

All 12 conformed per-beat clips are in `vertical/clips/`. Master mux completed to `exports/vertical/claude-liam-brutalist-your-first-project-vertical.mp4` (142.7 s).

## Gate V — visual QC (`runtime/qc/final_frame_check.py`)

```
Frames sampled: 24  ·  BLOCKER: 0  ·  MAJOR: 0
Clean — no BLOCKER/MAJOR defects. ✓
```

Full report: `vertical/_qc/REPORT.md`. Contact sheet: `vertical/_qc/contact_sheet.png` (24 beat-aware samples at 50 % / 85 %). Human-review contact sheet at 1 fps: `vertical/_qc/human-review-contact.png` (24 frames drawn from 143 second-by-second samples).

The portrait-tuned Gate V uses `SAFE916 = {x:54, y:96, w:972, h:1728}` (in 1080x1920, scaled to 2160x3840). To pass FILL_MIN = 0.55 the following portrait-specific adjustments were made in the isolated toolkit:

- **B01 hesitant writer** — fontSize raised from 138 -> 340 and the line count adjusted (6 short lines instead of 5 medium ones). At the 85 % steady-state sample the text spans ~73 % of the safe height.
- **B04, B05, B08, B09 verdict artifact cards** — the isolated `ClaudeVerdictArtifact916` component's sizing was tuned: card width 90 % -> 94 %, FONT_TITLE 0.018 -> 0.024, FONT_HEADING 0.024 -> 0.034, FONT_LINE 0.017 -> 0.023, padding proportionally larger. The old sizing was consistently 42 – 46 % coverage; the new sizing lands each card safely above 55 %.

The toolkit's `ClaudeVerdictArtifact916` was the only shared portrait file changed; it is used only by this reel per `runtime/remotion/_bench/consumers.json`. No live-library file was altered.

## Actual-image visual review (Read tool)

Extracted per-beat mid-frames and read via the image-capable Read tool.

- **B00** — Portrait composer with the first-project ask, four-line plan, folder chip @HumanitariansAI, terracotta only on send button.
- **B01** — Hesitant writer completes 6 stacked serif lines; `demo` is overwritten by `claim` in terracotta; correction lands cleanly.
- **B02** — Portrait code card wraps JSON so line 5 `"A ribosome walks / the messenger..."` is a two-line indented string; all fits inside card.
- **B03** — Portrait composer with the concrete first ask; 3-line output resolves.
- **B04, B05, B08, B09** — Verdict cards with tuned sizes fill the safe area; artifact list is readable at portrait scale.
- **B06** — Portrait composer with revision ask; 4-line output.
- **B07** — Portrait code diff card wraps 5 modified files across 2-line indented entries.
- **B10** — Portrait composer with the Your Turn prompt; GOOD/BAD output lines terracotta-highlighted.
- **B11** — Portrait outro on dark polarity (slug seed 43 mod 2 = 1); title, HAI handle, Brutalist-03 sub-mark stack centered.

## Motion histogram

Same class/warning as the landscape spine: `fade:7 / type-on:5`. Accepted as a design note. Same reasoning: card content ANIMATES per beat (line-stagger, terracotta reveals, correction sweeps).

## Skin lint

`compile.py` reports:

```
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk
[art] SKIN LINT: B11: palette=claude but the outro is 'ClaudeTitleOutroHAI916' — OUTRO LAW wants ClaudeTitleOutro
```

**Explanation.** Both hits reflect the portrait aspect (916 suffix) and the HAI outro variant, respectively. Per the invocation brief:

- "Register portrait compositions natively (stack/reflow/relabel); do not crop a landscape scene."
- "Native custom outro variants may live in the isolated scene source."

Both flags are the mechanism the lint uses to flag the switch; both are honored as expected.

## Verified output

`exports/vertical/claude-liam-brutalist-your-first-project-vertical.mp4`

- ffprobe: `h264,video,2160,3840,142.667` / `aac,audio,142.666`
- SHA-256: `1d01e65c3c45d6b0864bbf9145aacc4d681ad72fbc12d37527b6f06cbbd68ee4`
- `.verified.json` receipt written by `compile.py`.

## Re-verification — run 35a283c4 (2026-09-11)

Source SHA changed: REPOLOOP-PROMPT.md was added to the episode source list for this invocation, changing source_sha256 to `eaeb9039c38691606a165ceba147dfd3ca0334ca593fe38b9199f6823d35b863`. Video and beat-sheet hashes unchanged. Gate V re-run against the existing portrait export:

```
python3 toolkit/runtime/qc/final_frame_check.py \
  vertical --mp4 exports/vertical/claude-liam-brutalist-your-first-project-vertical.mp4 \
  --sheet vertical/beat_sheet.json
[gate-v] frames=24 BLOCKER=0 MAJOR=0 → vertical/_qc/REPORT.md
```

Per-beat JPG hashes in `vertical/_qc/frames-run-bed96fa6/` match all previous passing runs exactly — bitwise video identity confirmed. Visual review repeated via Read tool (B00_b, B01_c, B10_b, B11_b + contact sheet); observations consistent with prior runs. VISUAL-REVIEW.json updated to run_id 35a283c44f7e4830a26c6a84abf10319.

## Re-verification — run bed96fa6 (2026-09-11)

Source SHA changed (README.md updated in parent repo). Video and beat-sheet hashes unchanged. Gate V re-run against the existing portrait export:

```
python3 toolkit/runtime/qc/final_frame_check.py \
  vertical --mp4 exports/vertical/claude-liam-brutalist-your-first-project-vertical.mp4 \
  --sheet vertical/beat_sheet.json
[gate-v] frames=24 BLOCKER=0 MAJOR=0 → vertical/_qc/REPORT.md
```

Per-beat JPG hashes at 15/50/85% of each beat match the previous passing run (e1330e48) exactly — bitwise video identity confirmed. Visual review repeated via Read tool on fresh portrait frame set (B00_b, B01_c, B10_b, B11_b + contact sheet); observations consistent with prior run. VISUAL-REVIEW.json updated to run_id bed96fa645304cbcb0ba69c0bddd8820.

## Known toolkit gaps (recorded honestly, not bypassed)

- `scripts/type_check.py` / `reference/type-spec.md` absent (see `TYPECHECK.md`). Manual visual audit performed.
- `FILL_MIN = 0.55` at portrait proved tight for the hesitant writer and shipped verdict-artifact card sizing. Repair path (per the brief): fix the reel, not the check. Component's own sizes were tuned in the isolated toolkit; the check was not modified or bypassed.
