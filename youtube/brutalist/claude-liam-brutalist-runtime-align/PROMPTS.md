# PROMPTS — Brutalist Utility: align.py

## Cold-open ask (B00)

```
Before I fill a single beat sheet, I want a per-word clock hung on the audio
I already generated with generate_audio_kokoro.py. Do not re-transcribe. Do
not guess. Use what we already know: the narration_text on each beat, and
the mp3 that came out of Kokoro. Give me one words.json under mp3/ that maps
every narration word onto the frame where the audio actually spoke it.
```

Composer output lines (what the ask lands with):

- reads narration_text + mp3 from beat_sheet.json — no re-typing
- faster-whisper supplies TIMING; SequenceMatcher matches known words to those seconds
- emits mp3/words.json — three consumers read it downstream

## Your-Turn prompt (B10, verbatim)

```
Point Claude Code at any reel folder that already has beat_sheet.json + mp3/
filled: (1) run `python3 runtime/scripts/align.py <that folder>` and save
stdout+stderr to /tmp/align.log; (2) cat mp3/words.json into your context;
(3) for each beat, tell me — the total word count, whether the run line said
`aligned` or `fallback`, and the biggest single gap in seconds between two
adjacent words (end_time_i vs start_time_{i+1}). (4) Do NOT re-run with a
larger --model to try to shrink the gaps. Explain in one line what a gap
actually is when the narration itself paused, and why a bigger model would
hide that pause instead of closing it.
```

## What the fellow should look for

- The `aligned` vs `fallback` count in the tail line (`(aligned N, fallback M)`).
- Any beat whose words.json entries are all evenly spaced — that is the even_spread
  fallback path; something in that beat's audio failed to anchor with SequenceMatcher.
  It is worth investigating (silent MP3? wrong language? missing narration_text?)
  but it is not a bug in align.py.
- The biggest end→start gap: that is a real breath in the narration. A word-keyed
  overlay on that beat should hold the last word until the next word actually starts.

## Prompts NOT to paste

The following are red flags in a fellow's follow-up. If Claude Code offers to run
any of them, hold the fellow back:

- `align.py <reel> --model large-v3` — the base model already anchors most narrations;
  larger models just change which audio frames get bracketed, not whether real breaths
  become real gaps.
- Any `sed`/`jq` script that "smooths" the gaps in words.json — a smoothed clock is
  a lie; the animation will hit before the audio and read as a mistake.
- `rm -rf mp3/*.mp3 && regenerate` — that discards the audio the alignment is
  measuring against. The correct rerun is `align.py <reel> --only <BID>` after
  the specific mp3 changed.
