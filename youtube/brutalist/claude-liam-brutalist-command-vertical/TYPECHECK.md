# TYPECHECK.md — landscape (16:9)

## Scope

The historical `scripts/type_check.py` / `reference/type-spec.md` /
kerning skill referenced in some ai-explainer docs are NOT shipped in
this toolkit revision (`toolkit_baseline_sha256`
`92432609980c8ffc03bc1f00a1300fe1ac78bd7363b5b8ba9f2d389407d72b9d`).
This file does not claim that check passed — the check does not exist
in this workspace.

What DID run:

1. The compiler's Gate V (`runtime/qc/final_frame_check.py`) — pixel-
   level checks against the title-safe area on the actual compiled
   MP4. Passed with 0 BLOCKER / 0 MAJOR (see `CHECKS-REPORT.md`).
2. Manual visual typography review — 36 frames extracted at 15 %,
   50 %, 85 % of each of 12 beats and read with the image-capable Read
   tool.

## Manual visual typography audit (landscape)

Ground: cream (`#FAF9F5`). Ink: warm near-black (`#3D3929`). Accent:
one terracotta moment per beat (`#D97757`). Serif: EB Garamond
(bundled). UI sans + mono: system fallbacks. Palette matches
CLAUDE-BRAND.md.

| Beat | Pattern | Typography check |
|---|---|---|
| B00 | ClaudeComposerAsk | greeting "Hola, Liam" in serif; composer body in UI sans; output lines in mono; folder chip in soft ink; all inside SAFE. |
| B01 | BrutalistHesitantWriter | corrected sentence "vertical preserves. / and rewires it." in EB Garamond at 240 pt; two lines fill the safe area vertically; no bleed at 15/50/85. |
| B02–B08 | ClaudeCodeBeat | code card centered on cream; mono code inside white card; comments in soft ink; terracotta on active traffic-light dot; sparkLine in serif at bottom. Every code line fits inside the card's width at 16:9. |
| B09 | ClaudeVerdictArtifact | "Verdict" label + heading in serif; 8 numbered lines in UI sans; terracotta numerals; all inside SAFE. |
| B10 | ClaudeComposerAsk | greeting "Your Turn" in serif; composer body carries the paste-ready prompt (readable at 4K); output lines in mono. |
| B11 | ClaudeTitleOutro | poster serif "Brutalist Command: art vertical." with terracotta full-stop; @NikBearBrown handle beneath; slug-seeded pixel-art mascot; brand rule bands top/bottom. Matches OUTRO-LOCK. |

## Legibility

Every beat's text is legible at 4K playback and readable when the
video is scaled to 480p width. No font falls below the 24 px effective
floor. No text touches the 5 % title-safe inset (x 96–1824,
y 54–1026).

## Contrast

Warm ink on cream (#FAF9F5) hits ~11:1 luminance ratio at body sizes;
terracotta accents are used for one focal moment per beat, never as
body text (per Accent Law). No low-contrast defects observed.
