# PROMPTS — Brutalist Utility: align.py — Short

The Short retains the cold-open ask (B00) but DROPS the Your Turn beat (B10, 28s)
per the cut-first brief. Only the B00 composer prompt is spoken here; the paste-ready
exercise lives in the 16:9 long film. Do not fabricate a Your Turn in the Short.

## Cold-open ask (B00 — spoken verbatim in the Short)

Composer command shown on screen (portrait):

```
The audio is generated, the beats are timed to it, and I want a per-word clock
I can hang the animations on. Do not re-transcribe. Do not guess. Use what we
already know.
```

Composer runningText + output rows the ask lands with:

- `invoking align.py…`
- reads narration_text + mp3 from beat_sheet.json — no re-typing
- faster-whisper supplies TIMING; SequenceMatcher matches known words onto those seconds
- emits mp3/words.json — three downstream consumers read it

## Dropped prompt (present in the long, cut from the Short)

The full Your Turn exercise (paste-ready grading task, gap-not-a-bug caveat,
"do NOT bump --model" reminder) is preserved in the 16:9 parent film. Fellows who
want the exercise should watch the long — the Short does not read it aloud and
does not truncate it.

## Prompts NOT to paste (still true across both cuts)

- `align.py <reel> --model large-v3` — bumping the model hides real breaths as gaps; it does not close them.
- Any `sed`/`jq` script that smooths words.json gaps — a smoothed clock lies to the animation plane.
- `rm -rf mp3/*.mp3 && regenerate` — discards the audio the alignment measures; the correct rerun is `align.py <reel> --only <BID>`.
