# TYPECHECK.md — Brutalist Command: art smoke — Short

There is no separate legacy type checker in this toolkit. This file records
the actual **visual typography review** — the equivalent gate that the
compile pipeline and the human reviewer rely on.

## Scope

Six beats × three sampled frames (15 / 50 / 85 %) plus the compiler's own
mid-frame contact sheet. Every frame was extracted from the final compiled
mp4 and opened with the image-capable Read tool.

## Font stack & face

- Body typeface across ClaudeCodeBeat916 and ClaudeVerdictArtifact916:
  system serif (Georgia / DejaVu Serif fallback), rendered by Remotion at
  the parent's landscape defaults.
- BLUF hesitant writer (B01): serif face at the portrait-native sizing
  produced by BrutalistHesitantWriter916 (see the shipped preset in
  `runtime/remotion/src/scenes/`); serif "art smoke" title + terracotta
  hesitation swap to "renders video." — confirmed visually across
  B01_15/50/85.
- OUTRO (B10): the same serif family in white on dark ink polarity,
  slug-seeded per OUTRO-LOCK.

## Legibility (frames sampled)

| Beat | 15 % | 50 % | 85 % | Verdict |
|---|---|---|---|---|
| B00 | 691dab | 35e6d5 | 048a51 | Composer + folder chip + cascade lines all inside SAFE916. Legible. |
| B01 | 4b233f | 30a7d0 | 7830a3 | Trigger swap (`checks` → `renders`, `deps` → `video`) executes correctly; large serif type stays inside SAFE916. |
| B03 | 4526cb | cf9a0b | bb4c12 | Code card 15 lines, ~90 char widest; fits inside card and card fits inside SAFE916. Spark line legible. |
| B07 | 428dea | 2aa7e6 | ac5316 | Longest code beat (BEFORE + WHY + RECOVERY + AFTER, ~28 lines). All four subsections stay inside the card. |
| B08 | 6eff8b | 484bf0 | ec8731 | Verdict artifact with six numbered lines; body copy legible; heading not truncated. |
| B10 | a878ba | 0a0cd6 | 71738d | Title `Brutalist Command: art smoke.` breaks over three lines above `@NikBearBrown`; both fit within the SAFE916 inset. |

(SHA-256 prefixes above are the first 6 hex characters; full digests are
in VISUAL-REVIEW.json.)

## Contract compliance

- **SAFE916 inset (x 40-1040, y 192-1728 at 1080-space):** every sampled
  frame stays inside this rectangle. No text bleeds past the edge.
- **BLUF coverage (FILL_MIN 0.55):** B01 BLUF text ("art smoke / renders
  video.") sits on two lines with generous line-spacing — the portrait
  recipe fills the safe area vertically without dropping below the
  ClaudeCodeBeat portrait fill floor at 50 %.
- **Onda check (never crop generated graphics):** every kept beat is a
  Remotion render already produced at 2160×3840 in the parent's vertical
  build; shorts.py copied them unchanged. No center-cut cropping was
  applied.
- **Portrait sparkLine baseline:** B03 spark line sits comfortably inside
  the SAFE916 y-range with no vertical clipping. (Feedback memory about
  the +60 CSS bump for baseline-aligned SparkLines applies to `CommandTodo`
  patterns; ClaudeCodeBeat916 uses a card-anchored spark line and is not
  affected.)
- **OUTRO polarity:** the slug `claude-liam-brutalist-command-smoke` has a
  char-sum whose parity places this outro on the dark polarity (confirmed
  in B10_50). `@NikBearBrown` handle is hard-coded per OUTRO-LOCK — flagged
  in README.md for @HumanitariansAI human review.

## Regression checks

- No hesitant-writer trigger collision: `checks` and `deps` only appear in
  the target text of B01, not in any preserved title/prefix — the first
  occurrence rule is safe here.
- No portrait scale collapse: shipped portrait-native preset was used
  (parent's vertical build), so the 0.5625 shrink observed on some
  BrutalistHesitantWriter portrait renders (feedback memory) does not
  apply.
- No channel_title portrait bleed: this cut retains the parent's beat
  sheet which has already removed `metadata.channel_title` from the
  compile-overlay path.

## Result

**PASS.** No typography defects observed at any sampled frame. Compile
Gate V confirms 0 BLOCKER and 0 MAJOR at 12 additional samples.
