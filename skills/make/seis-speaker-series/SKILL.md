---
name: seis-speaker-series
description: >
  Turn one SEIS guest-speaker recording (a 1–4 hour Teams meeting) into a finished speaker-series
  film: SEIS logo reveal → "Speaker Series N / <speaker>" card → the talk and Q&A, uncut →
  SEIS logo, with word-level mutes for profanity and an optional music bed on the bookends.
  Input is a plan.json; output is one mp4 review cut, or a 4K H.264 .mov YouTube master. Use
  when the user types `seis speaker series`, `speaker series video`, or points at a Teams
  speaker-event recording. Never publishes.
---

# seis-speaker-series — event recording → speaker-series film

Engine: `runtime/scripts/seis_speaker_series.py`. Bookends render through Remotion `SeisFilm`
(the alumni film's `logo` + `card` items, nothing new to slate). The talk is cut, muted and
conformed by ffmpeg, because an 80-minute Remotion render buys nothing.

## The plan
```json
{"series": 2, "speaker": "<Speaker Name>",
 "source": "<Teams recording>.mp4",
 "segments": [{"label": "talk-and-qa", "in": 65.2, "out": 5108.0}],
 "bleep":    [[4840.66, 4840.98], {"phrase": "~stupidest fucking idea", "word": "fuck"}],
 "open":  {"light": true},
 "close": {"logo_only": true, "light": true},
 "music": {"file": "music/bed.mp3", "gain": 1.0, "under": 0},
 "logo_seconds": 4.5, "loudnorm": true}
```
```
python3 runtime/scripts/seis_speaker_series.py plan.json --out render/speaker-series-2.mp4 --dry   # print the timeline
python3 runtime/scripts/seis_speaker_series.py plan.json --out render/speaker-series-2.mp4         # 1080p review cut
python3 runtime/scripts/seis_speaker_series.py plan.json --out render/speaker-series-2.mov --master  # 4K YouTube master
```
- **in/out**: seconds, `m:ss`, `h:mm:ss` (the recording's clock; the Teams .docx clock is within about 2 s),
  or `"~a phrase"` resolved against `<source>.transcript.json` (`seis_extract.py transcribe`).
- **bleep**: `[t0, t1]` in the source clock, or `{"phrase", "word"}`, which mutes every word matching
  `word` inside the phrase, padded 60 ms each side. These are mutes, not beeps.
- **open / close**: `{}` gives the default card (`Speaker Series N / <speaker>` at the open, `Thank you, <speaker>.`
  at the close); fields merge over it. `"light": true` uses the white-ground logo reveal.
  `"logo_only": true` drops the card. `false` removes the bookend. `{"image": "<approved PNG>"}`
  makes a still slate (for an approved lockup the brand group supplies; never composed here).
- **music**: a bed mixed after the cut, with the video stream copied. Plays at `gain` under the bookends,
  eases to `under` about 1 s before the recording starts, and lifts back under the closing bookend.
  Set `under: 0` for silence under the talk. It gets one static gain to −16 LUFS (the talk's
  loudnorm target).
- **--master**: 3840×2160 H.264 .mov, 2-pass VBR (`--bitrate`, default 40M), 48 kHz, encoded once
  from the source (cut, mutes, lanczos upscale), never an upscale of the review cut. Expect about 34 GB and
  about 4 h on an M1 for a 2-hour film; wrap the run in `caffeinate -i` (a sleeping Mac stalls ffmpeg).

## Editing laws
- **No internal cuts.** Keep the whole talk, side conversations, host reframes and Q&A. Trim only the
  dead air at the ends: start on the host's first line of the intro (skip the Teams splash and
  "one more minute"), end on the speaker's last word before the host's break or next-class
  announcement. Make 20 s end-option clips when the stopping point is a judgment call.
- **Find the words, then cut.** Transcribe (the `base.en` model is fast enough for structure; re-check
  cut points and every bleep with `small` on short windows). Never place a mute from the Teams
  transcript's starred text alone, because its clock drifts.
- **Verify by listening data, not the probe.** After a render, measure RMS across each mute (silence),
  transcribe the first and last 8 s (correct in/out), and look at frames of both bookends.
- **Names come from the user.** Whisper mangles surnames, and so do hosts. Never put a guessed
  name on the card.

## Brand notes (NEU videography guideline)
"Include no opening title slide; simply start the video." End on the "Wordmark + Motto lockup,
preferably against a white background." A SEIS title card at the open is a deliberate
exception. Get it cleared by brand review (brand@northeastern.edu). There is no NEU audio
mnemonic; don't invent one without brand approval.

## What it refuses
Guessed speaker names, an unapproved lockup or tagline, a crop for 9:16, and any publish step.
