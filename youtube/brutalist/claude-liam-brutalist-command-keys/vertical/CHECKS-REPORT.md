# CHECKS-REPORT — Brutalist Command: art keys · vertical (2160×3840)

**Episode**: 36 · `command-keys` · Brutalist playlist · @HumanitariansAI
**Run ID**: `b7896f5b2d2a441186ff1451881c0a5b` (re-verified 2026-09-13; previous run abdef8f04e1246deaf8cf7ab26ae350b interrupted by Claude usage limit — exports unchanged)
**Master**: `exports/vertical/claude-liam-brutalist-command-keys-vertical.mp4`
**Duration**: 218.583 s · **Beats**: 12 · **Slates**: 0
**Master SHA-256**: `acf2b0c143be0498d0ed56f59ddc97b5b720f8b68dafac733716c37dbbc629c1` (unchanged — re-verified 2026-09-12)

## Beat classification

12 SHOW · 0 HOLD · 0 CARD · 0 PUNT · 0 slates.

The vertical variant is a native 1080×1920 render per beat (Root.tsx 916
compositions), scaled to 2160×3840 at compile time. It is NOT a
center-crop of the landscape master.

## Command log (verbatim, in build order)

```
$ python3 <<< 'derive vertical/beat_sheet.json from landscape sheet:
    - slug += "-vertical"; aspect_ratio "9:16"; kind "vertical"; fit "pad"
    - REMOVE metadata.channel_title (portrait bleed — see
      feedback_channel_title_portrait_bleed)
    - rename every beat.shot.remotion.pattern → append 916
    - copy landscape mp3/*.mp3 → vertical/mp3/*.mp3 (same clock)'

$ python3 runtime/scripts/remotion_scenes.py <reel>/vertical
  → 12 vertical/media/B*.mp4 rendered at native 1080×1920.

$ python3 runtime/scripts/compile.py <reel>/vertical \
    --height 3840 --out <reel>/exports/vertical --force
  → wrote exports/vertical/claude-liam-brutalist-command-keys-vertical.mp4
    (218.583 s, 2160×3840, h264 yuv420p, aac audio)
  → wrote exports/vertical/claude-liam-brutalist-command-keys-vertical.verified.json
```

## B01 portrait iteration history (Gate V tuning)

The portrait BLUF (BrutalistHesitantWriter916) needed three passes to
clear Gate V for coverage without edge-bleed. Recipe reference:
`feedback_hesitant_writer_portrait_bluf_recipe` (fontSize small, then
push lineSpacing until the ≥55% floor is met).

| Attempt | fontSize | lineSpacing | Gate V verdict |
|---|---|---|---|
| 1 | 260 | 2.5 | BLOCKER `edge-bleed` on B01_50 + B01_85 — the widest line "audits upgrades." was ~2 000 px wide at 3840×2160 scale, past SAFE916 (x 108–3732). |
| 2 | 145 | 2.6 | Cleared edge-bleed. But MAJOR `underfill` — content bbox covered only 49% of SAFE916 (below the 55% floor). |
| 3 | **145** | **6.5** | ✅ Cleared. Content bbox spans enough vertical height to pass FILL_MIN. Widest line fits comfortably inside the safe width. |

Fixed props for the shipped B01 portrait beat:
```
"fontSize": 145,  "lineSpacing": 6.5
"align": "center",  "seed": "keys-b01",
"text": "art keys\nblocks renders."
"triggerWords": "blocks, renders"  →  "audits, upgrades"
```

## GATE V — final frame check (vertical)

- Sampler: `runtime/qc/final_frame_check.py`, portrait `SAFE916` inset
  (x 54-1026 y 96-1824), scaled to 2160×3840; `FILL_MIN 0.55`.
- **frames=24 · BLOCKER=0 · MAJOR=0**.
- Report: `_qc/REPORT.md`.
- Extended proof frames at `_qc/proof-portrait/{B00…B11}-{15,50,85}.png`
  (36 total).
- Contact sheet: `_qc/contact-sheet-portrait.png` (SHA-256
  `e0d90d266b3686c62adc98d94b25c14ae90ee63be088833c324f5c37adc052bc`).
- Every proof frame was Read with the image-capable Read tool.

## Frames actually viewed (spot check)

| Frame | What it establishes |
|---|---|
| B00-85 | Portrait composer with "Habari, Liam" greeting; three output lines fit under the @HumanitariansAI folder chip. |
| B01-85 | Corrected BLUF "art keys / audits upgrades." — fontSize 145 / lineSpacing 6.5. Both lines centered, no edge-bleed. |
| B04-85 | Verbatim `./art keys` (invalid) run — the red `❌ invalid` row and green footer both visible; wide "Cannot reach https://…" line wraps. |
| B06-85 | Full probe body inside the portrait card. Long code lines truncate at the card's right edge — see LIMITATIONS below. |
| B08-85 | Design-tell card — both drifts visible; grep line's `sit'` closing quote crops as `sit` (right-edge truncation, same known portrait limitation). |
| B09-85 | Verdict artifact — all six lines visible with room. |
| B10-85 | Portrait Your-Turn composer — command text wraps but readable; grading lines visible. |
| B11-50 | Outro title stacks vertically: "Brutalist" / "Command: art" / "keys." with terracotta period + `@NikBearBrown` handle. |

## LIMITATIONS carried forward from ep 32 (documented, not resolved)

**Portrait `ClaudeCodeBeat916` right-edge truncation.** Long code lines
that fit inside a 1920-wide landscape card overflow the 1080-wide portrait
card. The code stays inside the white container so Gate V passes as
"clean" (no ink outside SAFE916), but any character beyond column ~40 is
clipped by the container's right edge. Affected beats: B02, B03, B04,
B05, B06, B07, B08. The salient part of every line is visible within the
first ~40 columns; the FULL text of every code beat is preserved in the
landscape master and `demo/RUN-LOG.txt`. The vertical companion is
intended as a preview-and-flip-to-landscape reel, not a
standalone-in-9:16 replacement.

**OUTRO-LOCK on portrait too.** `ClaudeTitleOutro916` uses the same
locked `@NikBearBrown` handle as the landscape variant. Flagged for the
human reviewer.

## Skin warnings (informational)

`build.skin_warnings` records that B00 and B11 use `ClaudeComposerAsk916`
and `ClaudeTitleOutro916` (not the exact strings COLD OPEN LAW / OUTRO
LAW's linter recognises). These are the intentional portrait variants
of the required scenes and satisfy the actual laws.

## Outstanding limitations

- No shipped `scripts/type_check.py` — see `TYPECHECK.md` for the visual
  audit that stood in.
- Human review pending.
