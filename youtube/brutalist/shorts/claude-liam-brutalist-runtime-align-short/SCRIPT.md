# SCRIPT — Brutalist Utility: align.py — Short

Native 2160×3840. 6 beats. 90.25s. Voice: Kokoro `am_onyx` (Liam, in for Bear).
Captions off. Every retained mp3 is the parent's independent copy — nothing regenerated.

## B00 — ASK (11.79s) — `ClaudeComposerAsk916`

> Shalom, this is Liam, in for Bear. The ask — the audio is generated, the beats are
> timed to it, and I want a per-word clock I can hang the animations on. Do not
> re-transcribe. Do not guess. Use what we already know.

## B01 — BLUF (12.63s) — `BrutalistHesitantWriter916`

> Watch the writer walk this back. Align dot py does not transcribe. Whisper listens
> for TIMING, the beat sheet already holds the WORDS, and the two are stitched together —
> the known text lands on the moments the audio actually spoke.

## B02 — FRAMEWORK (19.00s) — `SkillTeardownMechanism916`

> Here is the pipeline. Take the beat sheet, which already carries the narration text.
> Take the mp3 files that came out of Kokoro. Feed each mp3 to faster whisper for word
> level timestamps. Match the recognised words to the known words with SequenceMatcher.
> Fill any gaps by interpolating between anchors. Emit a single words dot json for
> the whole reel.

## B07 — MECHANISM (fallback) (19.42s) — `ClaudeCodeBeat916`

> When Whisper anchors nothing — silent audio, non speech, the wrong language — align
> dot py does not fail the reel. It calls even spread. Words divide the beat duration
> evenly. It also prints a warning: word keyed tracks on this beat are unreliable.
> That warning is the point. The clock still exists; the timings on that one beat are
> averages, not observations. The reel keeps rendering.

## B09 — VERDICT (21.67s) — `ClaudeVerdictArtifact916`

> So — align dot py. The word clock. It ingests known text and measured audio, produces
> a per word timeline in frames at the film fps, and refuses to guess when the audio
> disagrees. It runs at audio lock, between generate audio and render. Rerun it whenever
> a beat's mp3 changes. One narration, three consumers: the Remotion plane, the SRT
> publisher, the karaoke overlay. Exact text. No drift.

## B11 — OUTRO (5.75s) — `ClaudeTitleOutro916`

> Brutalist Utility: align dot py. Liam, in for Bear, for at Humanitarians A I.

## Cut notes

- Order preserved (B00 → B01 → B02 → B07 → B09 → B11); no beats rewritten.
- B07 references `even_spread` without a prior code beat showing it — the narration
  itself explains what even_spread does ("Words divide the beat duration evenly"),
  so the transition works without B03-B06.
- B09 opens with "So —" which lands naturally as a summary after the safety beat.
- Outro preserves the Liam-in-for-Bear disclosure and the `@NikBearBrown` handle
  (per OUTRO-LOCK). The composer folder chip in B00 remains `@HumanitariansAI`.
- No endcard appended, no outro rewrite.

## Dropped beats (in the parent long, not the Short)

B03 CLI `--help`, B04 `words.json` layout, B05 `whisper_words()`, B06 `align_words()`,
B08 1926 drift case, B10 Your Turn exercise. Total dropped duration ≈ 133.13s.
