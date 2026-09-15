# FACTCHECK — Brutalist Utility: align.py

Every claim the film makes about `align.py` is verified against the source file at
`runtime/scripts/align.py` (SHA-256 `89e0f38ded269908fab42362723f9dab3d87f449bf08e70cad05a4e4efb3c33e`)
and the live demo output in `demo/RUN-LOG.txt`.

| # | Claim on screen / in narration | Source line(s) | Verified? |
|---|--------------------------------|----------------|-----------|
| 1 | "align.py is the word clock, REMOTION.md build-order step 1" | `align.py:2` | ✅ verbatim in docstring |
| 2 | "The narration TEXT is already known — the beat sheet holds it" | `align.py:4-7` docstring; `main():143` reads `narration_text` first | ✅ |
| 3 | "faster-whisper supplies word-level TIMING from each beat's mp3" | `align.py:59` `word_timestamps=True` | ✅ |
| 4 | "SequenceMatcher aligns known words onto whisper timestamps" | `align.py:72-81` `align_words()` | ✅ |
| 5 | "Missed words interpolate between anchors" | `align.py:91-101` gap-fill loop | ✅ |
| 6 | "Runs at audio lock (workflow step 3), right after generate_audio_kokoro.py" | `align.py:14-15` | ✅ verbatim |
| 7 | "Rerun with `--only` for changed beats" | `align.py:15` docstring; `main():138-139` | ✅ |
| 8 | "Reads `beat_sheet.json`, writes `mp3/words.json`" | `align.py:17-18`; `main():121, 129, 177` | ✅ |
| 9 | "Frames are BEAT-LOCAL at the film fps (default 24; metadata.fps overrides)" | `align.py:22-24`, `main():122` | ✅ |
| 10 | "Three consumers: Remotion plane, stage_publish.py, karaoke derivative" | `align.py:24-27` (docstring) | ✅ named in docstring |
| 11 | "faster-whisper required: `pip install faster-whisper`; CPU fine" | `align.py:31, 53-57` | ✅ exit message printed |
| 12 | "Runs on CPU with int8 quantisation" | `align.py:58` `device="cpu", compute_type="int8"` | ✅ |
| 13 | "CLI: `python3 scripts/align.py reels/<slug> [--model base] [--only B05 T01]`" | `align.py:29-30` docstring; `main():115-118` | ✅ verbatim |
| 14 | "Default model size is `base`" | `align.py:115` `default="base"` | ✅ |
| 15 | "Default language is `en`" | `align.py:116` `default="en"` | ✅ |
| 16 | "Normalises to lowercase alphanumeric before matching" | `align.py:43-46` `norm()` | ✅ |
| 17 | "Uses SequenceMatcher with `autojunk=False`" | `align.py:77` | ✅ |
| 18 | "Anchors from matching blocks; interpolates gaps; pins pre/post" | `align.py:78-101` | ✅ |
| 19 | "Falls back to even spread if nothing anchors AND duration exists" | `align.py:158-162` | ✅ |
| 20 | "Prints `[warn] {bid}: NO anchors — even spread over {dur}s (word-keyed tracks on this beat are unreliable)`" | `align.py:164-165` | ✅ verbatim |
| 21 | "words.json carries the correctly-spelled narration text, never the respelled tts text" | `align.py:141-142` (comment) | ✅ verbatim intent; `main():143` reads narration_text first |
| 22 | "Uses `actual_duration_s` OR `timings.json` OR 0.0 for duration" | `align.py:153` `dur = beat.get("actual_duration_s") or timings.get(bid) or 0.0` | ✅ |
| 23 | "Word entries in words.json: `{text, startFrame, endFrame}`, rounded from seconds×fps" | `align.py:169-173` | ✅ |
| 24 | "Both frames clamped to ≥ 0" | `align.py:171-172` `max(0, round(...))` | ✅ |
| 25 | "Skip messages for missing narration/audio and missing files" | `align.py:146, 150` | ✅ verbatim |

## Live-demo verifications

| # | Demo assertion | Source of truth |
|---|----------------|-----------------|
| D1 | `python3 runtime/scripts/align.py -h` prints the usage block used on screen | RUN-LOG section 1 (captured this workstation) |
| D2 | Happy path emits `[ok] B00: 10 words @ 24fps` for narration "Whisper hears the words. The known text tells the writer." | RUN-LOG section 2; `demo/single-beat/mp3/words.json` |
| D3 | Number-drift keeps `"1926,"` verbatim in words.json despite spoken "nineteen twenty six" | RUN-LOG section 3; `demo/number-drift/mp3/words.json` |
| D4 | `--only B02` re-writes only B02 and preserves the other two beats in `words.json` | RUN-LOG section 4; compare pre/post `demo/only-flag/mp3/words.json` |
| D5 | Three separate skip messages print for no-duration / no-audio / missing-file | RUN-LOG section 5; `demo/skip-cases/` |

## Known limitation, honestly labelled

- On a fresh box behind the sandbox's SOCKS proxy, `WhisperModel()` fails with a traceback ending in either the `socksio` import error or a plain connection error to `huggingface.co` — because the CTranslate2 loader inside faster-whisper still hits huggingface.co for the model manifest. The failure is not in `align.py`; it is in the model-fetch it delegates to. On this workstation the model was already cached under `~/.cache/huggingface/hub`, and `HF_HUB_OFFLINE=1` prevents even the metadata round-trip. That's the recipe used for every demo in RUN-LOG. The film's B03 narration flags this honestly as the "only remote dependency in this whole script."

## Nothing else claimed

The film does not claim `align.py` publishes anywhere, or that it changes any file besides `mp3/words.json`. It does not claim SRT is generated here — that's `stage_publish.py`, and `align.py` only writes the `words.json` those consumers read. Both facts are consistent with `align.py:24-27`.
