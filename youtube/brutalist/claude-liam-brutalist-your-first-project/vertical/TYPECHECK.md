# TYPECHECK.md — Your First Brutalist Project (portrait 9:16)

## The legacy checker is missing from this cut

Same gap as the landscape reel: `scripts/type_check.py` and `reference/type-spec.md` are referenced by the public docs but are NOT in this isolated toolkit. Per the invocation brief, that is recorded honestly here rather than papered over.

## What DID run — Gate V

`runtime/qc/final_frame_check.py` with portrait-aware `SAFE916 = {x:54, y:96, w:972, h:1728}` (scaled to 2160x3840 in the actual samples). Result: `Frames sampled: 24  ·  BLOCKER: 0  ·  MAJOR: 0`.

## Manual visual typography review

Every beat's 50 % steady-state and 85 % steady-state frames were extracted at portrait 4K and read via the image-capable Read tool. Font sizes reflect the isolated portrait tuning:

| Beat | Typeface | Sizes (in 1080x1920 canvas, scaled up 2x on render) | Result |
|---|---|---|---|
| B00 | Serif greeting + mono command | Greeting ~72px, command ~54px | Fits portrait, no overflow. |
| B01 | Serif hesitant writer | fontSize 340px (in props) × portrait scale 0.5625 = 191px effective | 6 stacked lines fill safe height at 85 %. |
| B02 | Mono code | h*0.022 = 42px effective | Narrow-wrapped JSON fits card body. |
| B03 | Composer | Same as B00 | Portrait-tight command wraps once inside card. |
| B04 | Artifact card (tuned) | FONT_TITLE h*0.024, FONT_HEADING h*0.034, FONT_LINE h*0.023 | 7 lines fill card. |
| B05 | Artifact card | Same class | 6 lines fill card. |
| B06 | Composer | Same as B00 | 4 output lines resolve. |
| B07 | Mono code | Same as B02 | 5 modified files + 2 comment lines fit. |
| B08 | Artifact card | Same class as B04 | 7 lines fill card. |
| B09 | Artifact card | Same class | 7 lines fill card. |
| B10 | Composer | Same as B00 | GOOD/BAD lines terracotta on cue. |
| B11 | Serif poster outro | Title h*0.058 = 111px, handle h*0.032 = 61px, sub h*0.018 = 34px | Poster fills; dark polarity. |

**Findings.** No sub-24px effective text found. No overflow. No overlap. Terracotta appears on exactly one focal element per beat.

## Portrait-specific decisions

Portrait scaling in the toolkit's `BrutalistHesitantWriter` uses `scale = min(width/1920, height/1080)` = 0.5625 for 9:16. That means a fontSize authored for landscape reads at ~56 % of its nominal size in portrait, so the portrait beat sheet passes a much LARGER `fontSize` (340 vs. 132) to end up at a comparable rendered pixel size.

The `ClaudeVerdictArtifact916` component's default text sizes proved too small to reach FILL_MIN = 0.55 at portrait. It was retuned in the isolated toolkit (card width 90 % -> 94 %, FONT_TITLE 0.018 -> 0.024, FONT_HEADING 0.024 -> 0.034, FONT_LINE 0.017 -> 0.023, padding proportionally larger). Only this reel consumes the 916 variant (verified in `runtime/remotion/_bench/consumers.json`), so the change is isolated.

## Golden-string audit (manual)

Same handles/labels as the landscape reel:

- "@HumanitariansAI" — playlist channel.
- "Kokoro am_onyx" — matches SKILL.md and generate_audio_kokoro.py.
- "2160 x 3840" — matches ffprobe on the compiled portrait master.
- "art vertical PLANS the portrait sheet" — matches `./art` dispatcher.

## Conclusion

Legacy checker gap disclosed. Gate V clean. Manual audit found zero typographic blockers. Portrait review is independent of landscape; both aspects pass. Bear's viewing is next.
