# SCRIPT — Brutalist Utility: align.py

**Episode:** claude-liam-brutalist-runtime-align
**Voice:** Kokoro `am_onyx` (Liam, in for Bear)
**Register:** Teardown
**Channel adaptation:** composer chip reads `@HumanitariansAI`; outro card stays the locked `ClaudeTitleOutro` (hardcoded `@NikBearBrown` per `OUTRO-LOCK.md`) and is flagged in `README.md` for the human reviewer before publish.

The word count target is the audio-first budget in `ai-explainer/SKILL.md` — body beats 45–70 words; the ask, the BLUF, the handoff and the verdict are exempt where they earn it.

---

## B00 — ASK (cold open, `ClaudeComposerAsk`)
Greeting: `Shalom, Liam` (Hebrew, one word, fresh — see the greeting_note in `beat_sheet.json`).

> Shalom, this is Liam, in for Bear. The ask — the audio is generated, the beats are timed to it, and I want a per-word clock I can hang the animations on. Do not re-transcribe. Do not guess. Use what we already know.

## B01 — BLUF (hesitant writer, `BrutalistHesitantWriter`)
Correction is the reel's actual misconception. Text starts `align.py / transcribes audio.` and settles on `align.py / times the words.` — because that is what the whole file is arguing: Whisper supplies the seconds; the narration_text supplies the letters.

> Watch the writer walk this back. Align.py does not transcribe. Whisper listens for TIMING, the beat sheet already holds the WORDS, and the two are stitched together — the known text lands on the moments the audio actually spoke.

## B02 — FRAMEWORK (concept illustration, `SkillTeardownPipeline`)
INPUT `beat_sheet.json + mp3/*.mp3` → phases `WHISPER → SEQUENCEMATCHER → INTERPOLATE → EMIT` → OUTPUT `mp3/words.json`.

> Here is the pipeline. Take the beat sheet, which already carries the narration text. Take the mp3 files that came out of Kokoro. Feed each mp3 to faster-whisper for word-level timestamps. Match the recognised words to the known words with SequenceMatcher. Fill any gaps by interpolating between anchors. Emit a single words dot json for the whole reel.

## B03 — MECHANISM 1 (code, `ClaudeCodeBeat`)
The CLI surface, verbatim from `--help`, plus what the folder must contain.

> The command surface is small. One required positional: the reel folder. Two optional flags. Dash dash model picks the faster-whisper size — base is the default. Dash dash only takes beat ids so a rerun only touches those. Under the folder align.py expects a beat sheet dot json and an mp3 directory that generate audio kokoro already filled.

## B04 — WORKED EXAMPLE (code, `ClaudeCodeBeat`)
Verbatim from demo/RUN-LOG.txt section 2 — the one-beat happy path.

> One beat, one line of narration, one mp3. Run align.py. It writes words dot json under mp3 slash. Each word carries the exact narration text — including the trailing period on words dot — and a start frame and end frame at the film fps. Frames are beat local. Start frame zero is the first frame of THIS beat's clip, not the reel.

## B05 — MECHANISM 2 (code, `ClaudeCodeBeat`)
`whisper_words()` — what Whisper actually returns.

> Inside align.py, one function talks to Whisper. Whisper words returns a flat list of triples: the word, its start second, its end second. It runs on CPU with int8 quantisation — no GPU required, small enough to ship on a laptop. If faster whisper is not installed, the process exits with the pip line printed in place. That is the only remote dependency in this whole script.

## B06 — MECHANISM 3 (code, `ClaudeCodeBeat`)
`align_words()` — SequenceMatcher + interpolation, THE clever bit.

> Here is the clever bit. Normalise both sides — the known narration and the whisper output — to lowercase alphanumeric. Feed them to SequenceMatcher and take the matching blocks. Each block anchors a run of known words directly onto whisper timestamps. Words outside the matches — the interior gaps — interpolate linearly between the surrounding anchors. Words before the first anchor pin to that first anchor. Words after the last anchor pin to that last anchor. Nothing is left floating.

## B07 — MECHANISM 4 (code, `ClaudeCodeBeat`)
`even_spread()` fallback + the "unreliable" warning.

> When Whisper anchors nothing — silent audio, non speech, the wrong language — align dot py does not fail the reel. It calls even spread. Words divide the beat duration evenly. It also prints a warning: word keyed tracks on this beat are unreliable. That warning is the point. The clock still exists; the timings on that one beat are averages, not observations. The reel keeps rendering.

## B08 — WORKED EXAMPLE 2 (code, `ClaudeCodeBeat`)
The drift case. Numbers vs respelling; the invisibility to downstream consumers.

> The drift case. Narration says the digits nineteen twenty six. Kokoro speaks nineteen twenty six as three words. Whisper timestamps three words. SequenceMatcher does not anchor the digit token, so it interpolates the digit over the whole span of the audio those three spoken words occupy. Downstream, the karaoke overlay renders the digits — not the respelling. The audio and the on screen text finally agree.

## B09 — VERDICT (`ClaudeVerdictArtifact`)
The whole file, in the order it does its job. Six lines.

> So — align dot py. The word clock. It ingests known text and measured audio, produces a per word timeline in frames at the film fps, and refuses to guess when the audio disagrees. It runs at audio lock, between generate audio and render. Rerun it whenever a beat's mp3 changes. One narration, three consumers: the Remotion plane, the SRT publisher, the karaoke overlay. Exact text. No drift.

## B10 — YOUR TURN (`ClaudeComposerAsk`, greeting `Your Turn`)
Prompt is read aloud verbatim then discussed.

> Your turn. Paste this into Claude Code, pointed at any reel that already has audio: run align dot py on the reel, cat the resulting words dot json, and tell me — for each beat — the total word count, whether the run said aligned or fallback, and the biggest single gap in seconds between two adjacent end frame and start frame values. Watch for whether Claude is tempted to smooth those gaps by re running with a larger dash dash model. That is not the fix. The gap is a real breath in the narration; the model change would hide it, not close it.

## B11 — OUTRO (`ClaudeTitleOutro`, slug-seeded mascot, hardcoded `@NikBearBrown`)

> Brutalist Utility: align dot py. Liam, in for Bear, for at Humanitarians A I.
