# TYPECHECK — vertical (2160×3840)

## Actual typography review

Same principle as landscape TYPECHECK.md — the unshipped legacy `scripts/type_check.py` and `reference/type-spec.md` were not invoked. This document records the actual visual typography inspection performed against the finished 4K portrait master.

## What I actually did

- Ran `runtime/qc/final_frame_check.py` at portrait aspect (SAFE916 = x:54, y:96, r:1026, b:1824) against the 24 frames sampled from the finished portrait master. Result: 0 blockers, 0 majors.
- Read `vertical/_qc/contact_sheet.png` (1920×3412) and a supplemental 12-beat 70%-frame roll-up with the image-capable Read tool. Per-beat inspection:
  - B00 — `ClaudeComposerAsk916` — greeting serif kerning tight, running indicator terracotta spark clean, three output lines evenly spaced beneath the composer, folder chip `@HumanitariansAI` legible.
  - B01 — `BrutalistHesitantWriter916` — four final lines `fill_slates / stamps / empty beats / in a reel.` render at fontSize 175 with lineSpacing 2.2. Caret pipe visible in trailing position. Terracotta correction highlight lands only on the two trigger words during their hesitation windows.
  - B02 — `SkillTeardownMechanism916` — eyebrow + heading + body + quote card + spark line all inside SAFE916; no phase-strip left/right bleed.
  - B03–B08 — `ClaudeCodeBeat916` — monospace scales down cleanly for the tallest code blocks (B08's four failure-mode branches, ~50 lines). No indent collapse; no comment lines cut off; adaptive font clamp is active on both axes.
  - B09 — `ClaudeVerdictArtifact916` — six numbered lines all wrap inside the card's TEXT_MAX_W; heading "fill_slates.py — the whole surface, in order" wraps naturally over two lines; card bottom sits well inside SAFE916.b=1824.
  - B10 — `ClaudeComposerAsk916` — shortened segment "Dry-run + upgrade a card" wraps cleanly; composer input area shows the paste-ready prompt with backtick monospace pill in "fill_slates.py --books"; three grading lines appear underneath in mono.
  - B11 — `ClaudeTitleOutro916` — title serif "Brutalist Utility: fill_slates.py." plus `@NikBearBrown` handle (per hardcoded outro rule — see the beat's role_note) and mascot mark; all inside SAFE916.

## Font stack in use

Same three-family Claude font stack as landscape.

## Notes

- No unshipped `scripts/type_check.py` was invoked. Human typography review pending Bear's playback.
- All three families are shipped with the isolated toolkit's Remotion bundle and render at 4K portrait without any fallback substitution.
