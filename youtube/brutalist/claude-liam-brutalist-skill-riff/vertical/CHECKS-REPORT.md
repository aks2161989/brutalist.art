# CHECKS-REPORT.md — The riff Skill (portrait companion)

## Environment

- Toolkit: isolated workspace at `.repoloop/workspaces/claude-liam-brutalist-skill-riff/toolkit`
- Chrome: chrome-headless-shell via `runtime/chrome-wrapper.sh` with `--single-process --in-process-gpu` (App Sandbox fix)
- Renderer: `python3 runtime/scripts/remotion_scenes.py`, foreground, serial (per BUILD-PROMPT rule #3)
- Compiler: `python3 runtime/scripts/compile.py --height 3840 --out .../exports/vertical`
- run_id: `6bdc7e3501b243bca58d7f9757d9597d`

## Fix applied this invocation

Previous error: "vertical: missing scaffolded Your Turn"

**Root cause**: B10 (YOUR_TURN, second-to-last beat) used `FormACard916` instead of a `ClaudeComposerAsk` native variant. HANDOFF LAW requires `ClaudeComposerAsk916` with `greeting: "Your Turn"`.

**Fix**:
1. Updated vertical `beat_sheet.json` B10 `pattern` from `FormACard916` → `ClaudeComposerAsk916` with full `greeting`, `topic`, `segment`, `command`, `output` props.
2. Fixed `ClaudeComposerAsk.tsx` segment div: added `right: PAD_X` constraint (was missing), which caused the long segment text "Apply the riff skill to a scene you own" to overflow the portrait right safe area (SAFE916.r = x:1026). Without the constraint, the div's auto-width extended to ~1033px, tripping the BLOCKER edge-bleed threshold.
3. Re-rendered B10 via `remotion_scenes.py --only B10 --force`.
4. Recompiled vertical via `compile.py --height 3840 --force`.

## Beat rendering (per-beat Remotion)

12 portrait beats — B10 re-rendered this invocation; all others from prior run.

| Beat | Component | Pattern |
|---|---|---|
| B00 | ClaudeComposerAsk916 | cold-open — native portrait |
| B01 | BrutalistHesitantWriter916 | BLUF — native portrait, contextTitle + brandLabel |
| B02 | FormACard916 | anatomy skin swap |
| B03 | FormACard916 | pipeline skin swap |
| B04 | FormACard916 | mechanism 1 skin swap |
| B05 | FormACard916 | self-demo skin swap |
| B06 | FormACard916 | mechanism 2 skin swap |
| B07 | FormACard916 | mechanism 3 skin swap |
| B08 | FormACard916 | design tell skin swap |
| B09 | FormACard916 | verdict skin swap |
| B10 | ClaudeComposerAsk916 | Your Turn — HANDOFF LAW (fixed this invocation) |
| B11 | ClaudeTitleOutro916 | Liam sign-off, @HumanitariansAI |

## Compile

```
[art] compiled B00  VIDEO    15.5s  ← B00.mp4
[art] compiled B01  VIDEO    12.7s  ← B01.mp4
[art] compiled B02  VIDEO    19.1s  ← B02.mp4
[art] compiled B03  VIDEO    18.4s  ← B03.mp4
[art] compiled B04  VIDEO    21.0s  ← B04.mp4
[art] compiled B05  VIDEO    21.6s  ← B05.mp4
[art] compiled B06  VIDEO    19.9s  ← B06.mp4
[art] compiled B07  VIDEO    20.6s  ← B07.mp4
[art] compiled B08  VIDEO    26.4s  ← B08.mp4
[art] compiled B09  VIDEO    19.1s  ← B09.mp4
[art] compiled B10  VIDEO    32.2s  ← B10.mp4
[art] compiled B11  VIDEO     8.0s  ← B11.mp4
[art] build stamp → beat_sheet.json (12/12 filled)
[art] wrote exports/vertical/claude-liam-brutalist-skill-riff-vertical.mp4  (234.5s)
[art] slots: 12/12 filled — B00:VIDEO B01:VIDEO B02:VIDEO B03:VIDEO B04:VIDEO B05:VIDEO B06:VIDEO B07:VIDEO B08:VIDEO B09:VIDEO B10:VIDEO B11:VIDEO
```

## Gate V (frame-level QC)

Run (internal to compile.py, then re-run standalone):
```
python3 runtime/qc/final_frame_check.py vertical/ \
  --mp4 exports/vertical/claude-liam-brutalist-skill-riff-vertical.mp4 \
  --sheet vertical/beat_sheet.json
```

```
[gate-v] frames=24 BLOCKER=0 MAJOR=0 → vertical/_qc/REPORT.md
```

12 beats × 2 fractions (50%, 85%) = 24 frames sampled and analyzed. Gate V clean.

Intermediate diagnosis: during repair, Gate V on the review slate (with PIl beat-labels overlaid) showed 24 BLOCKERs — all from the review-mode beat-label PILs extending past BURN_IN_EXCLUDE right boundary. These labels are review-only and not present in the final export. The final candidate Gate V (no labels) confirmed BLOCKER=0, MAJOR=0.

## MP4 verification

`ffprobe` — portrait master:
- width=2160, height=3840, codec=h264
- duration=234.5s
- SHA-256 = `ed2ca4f709268b96450a5db5f11d9c59decc931910283bf1c43a0f0c6aa20959`

Compiler's atomic verification produced `claude-liam-brutalist-skill-riff-vertical.verified.json`.

## Manual visual inspection

Frames extracted from final export and inspected via Read tool:

- B00 ClaudeComposerAsk916: "BRUTALIST · SKILL: RIFF" topic, "The riff Skill" segment, "Bula, Liam" greeting, command box with riff probe question, @HumanitariansAI folder label, output lines (probing artifact, look, judge, record). Clean portrait layout within safe margins.
- B01 BrutalistHesitantWriter916: "riff generates observations." corrected text in serif, centered in portrait. contextTitle "the riff skill" top-left, "@HumanitariansAI" bottom-right.
- B09 FormACard916: verdict with "OUTPUT: RIFF.md / Four design principles" — all 4 numbered principles legible and within portrait safe area.
- B10 ClaudeComposerAsk916 "Your Turn": "BRUTALIST · YOUR TURN" topic, "Apply the riff skill to a scene you own" segment wraps to 2 lines (fixed), "Your Turn" greeting, full riff invocation command, @HumanitariansAI, output lines visible. Gate V: BLOCKER=0.
- B11 ClaudeTitleOutro916: "The riff Skill." title in serif, "@NikBearBrown" per OUTRO-LOCK.md. Dark olive background.

See `_qc/contact_sheet.png` and `_qc/b10_your_turn_50pct.png` and `VISUAL-REVIEW.json`.

## Available checks that ran

- `remotion_scenes.py` render (composition ID resolution + Zod schema validation)
- `beat_lint.py` — clean (beat mix OK)
- `gate_shape.py` — skipped (not a finance reel)
- `compile.py` — Gate F (paperwork), Gate V (frame-level QC internal), atomic verify
- `final_frame_check.py` — standalone re-run; REPORT.md confirmed BLOCKER=0, MAJOR=0

## Available checks that did NOT run

- `scripts/type_check.py` — not present in this isolated toolkit. See `TYPECHECK.md`.
- Kerning-only lint — inspected as part of manual frame-image review.
- YouTube-side transcoding — not applicable pre-upload.
