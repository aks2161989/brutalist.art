# FACTCHECK — Brutalist Utility: align.py — Short

This is the derivative Short. The parent's full FACTCHECK covers every claim on
screen in the 16:9 long. Here we verify only the claims the Short RETAINS after
the whole-beat cut (B00, B01, B02, B07, B09, B11). All claims verify against
`runtime/scripts/align.py`
(SHA-256 `89e0f38ded269908fab42362723f9dab3d87f449bf08e70cad05a4e4efb3c33e`)
and the parent reel's live demo output in `demo/RUN-LOG.txt`.

| # | Claim on screen / in narration (Short) | Source line(s) | Verified? |
|---|---------------------------------------|----------------|-----------|
| 1 | "align.py is the word clock" (B00, B09) | `align.py:2` docstring | ✅ verbatim |
| 2 | "The narration TEXT is already known — the beat sheet holds it" (B00, B01, B02) | `align.py:4-7` docstring; `main()` reads `narration_text` first | ✅ |
| 3 | "faster-whisper supplies word-level TIMING only" (B00, B02, B09) | `align.py:59` `word_timestamps=True` | ✅ |
| 4 | "SequenceMatcher aligns known words onto whisper timestamps" (B02, B09) | `align.py:72-81` `align_words()` | ✅ |
| 5 | "Interpolate the gaps between anchors" (B02, B09) | `align.py:91-101` gap-fill loop | ✅ |
| 6 | "Emits `mp3/words.json`" (B00, B02, B09) | `align.py:17-18` + `main()` write path | ✅ |
| 7 | "Three downstream consumers" (B00, B02, B09) | `align.py:24-27` docstring | ✅ named |
| 8 | "align.py does NOT transcribe; it TIMES known words" (B01 BLUF misconception) | `align.py:3-8` + `align_words()` intent | ✅ verified by design; `words.json` writes `narration_text` verbatim |
| 9 | "even_spread fallback when no anchors + known duration" (B07, B09) | `align.py:104-109` + `main():158-162` | ✅ |
| 10 | "Prints `[warn] {bid}: NO anchors — even spread over {dur}s (word-keyed tracks on this beat are unreliable)`" (B07) | `align.py:164-165` | ✅ verbatim |
| 11 | "No anchors + no duration → `[skip]`" (B09) | `align.py:158-160` | ✅ |
| 12 | "Beat-local startFrame/endFrame at `metadata.fps` (default 24)" (B09) | `align.py:22-24`, `169-173` | ✅ |
| 13 | `norm()` lowers punctuation/case (B09) | `align.py:43-46` | ✅ |

## Retained live-demo verifications

| # | Demo assertion (retained in Short) | Source of truth |
|---|-------------------------------------|-----------------|
| D1 | `align.py` treats the narration text as the truth and only asks whisper for timing | RUN-LOG section 2 + `demo/single-beat/mp3/words.json` |
| D2 | Fallback path prints the exact `[warn]` message with the beat id and duration | RUN-LOG section 5 + `align.py:164-165` |

## Claims deliberately NOT in the Short (present in the long)

The Short does not repeat the CLI `--help` walkthrough (B03), the concrete
`words.json` layout dump (B04), the `whisper_words()` implementation (B05), the
`align_words()` SequenceMatcher listing (B06), the 1926 number-drift worked example
(B08) or the Your Turn exercise (B10). Every one of those beats is preserved
unaltered in the 16:9 long. Do not present the Short as fact-checking claims it
never makes; do not present the long's dropped-beat coverage as if it appeared here.

## Nothing else claimed

The Short does not claim `align.py` publishes anywhere, hits any network beyond the
first-run faster-whisper model fetch, or writes any file besides `mp3/words.json`.
The outro `@NikBearBrown` handle is the locked OUTRO-LOCK identity per the parent's
adaptation note; the composer folder chip reads `@HumanitariansAI`.
