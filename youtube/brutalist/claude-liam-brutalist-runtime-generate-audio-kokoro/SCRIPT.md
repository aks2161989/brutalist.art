# SCRIPT — Brutalist Utility: generate_audio_kokoro.py

Voice: Kokoro `am_onyx`. Persona: Liam, in for Bear. Channel: @HumanitariansAI.
Twelve beats. All narration read verbatim by Kokoro; no human voice.

## B00 · ASK · ClaudeComposerAsk

> Ahoj, this is Liam, in for Bear. The ask — a new beat sheet needs narration
> for two beats. No API key. No metered service. Just generate the audio
> locally, on this laptop, with the free engine. And skip the fellows report
> beat and the intentional silence beat while you're at it.

## B01 · BLUF · BrutalistHesitantWriter

> Watch the writer walk this back. Kokoro is not paid and remote. It is a
> free, local ONNX model that runs on this laptop's CPU. No key. No meter.
> No account. Just voices.

Screen: `kokoro is / paid and remote.` → `kokoro is / free and local.`

## B02 · FRAMEWORK · SkillTeardownPipeline

> The pipeline. One invocation. Parse the arguments — a reel folder and some
> optional flags. Load the Kokoro engine from the on-disk model files. Walk the
> beats and filter — source reports and silent beats out, sentinels out, non
> kokoro engines out, empty narration out. For every survivor: normalize
> symbols to spoken form, synth samples with Kokoro dot create, write a wave
> file, transcode to MP3 with ffmpeg, measure duration with ffprobe. Then
> atomically write the actual duration and audio file path back into the beat
> sheet.

## B03 · MECHANISM 1 · ClaudeCodeBeat — CLI surface (verbatim)

> The command surface. One optional positional — the reel folder. Five flags.
> Dash dash only takes a list of beat IDs to regenerate. Dash dash speed
> adjusts playback rate. Dash dash dry run prints the plan and exits without
> touching the disk. Dash dash list voices prints all fifty four Kokoro
> preset voice codes and exits. Dash dash sheet lets you point at a different
> filename than beat sheet dot json. Dash dash no gate is deprecated — it
> cannot bypass human approvals.

## B04 · MECHANISM 2 · ClaudeCodeBeat — model_paths + load_engine + lang_for

> Where Kokoro lives. Model paths returns two paths — the ONNX model and the
> voices bundle — resolving in order from the Kokoro model and Kokoro voices
> environment variables, then from ART home slash runtime slash models slash
> kokoro. Load engine checks both files exist. If they don't, it prints the
> exact curl commands to fetch them — three hundred and thirty megabytes, one
> time, no account — and exits. If the kokoro dash onnx package is missing,
> it prints pip install kokoro dash onnx and exits. Then lang for maps the
> voice code's first letter to a G2P language. A is American English. B is
> British. J is Japanese. Z is Mandarin. And narration for a non English
> voice must actually be written in that language.

## B05 · MECHANISM 3 · ClaudeCodeBeat — the five skip rules

> The filter. Five skip rules. One — is source report or intentional silence:
> the beat has an existing source audio or a silent flag. Two — empty
> narration text. Three — narration text starts with a warning glyph, or the
> string LOST in square brackets, or PLACEHOLDER in square brackets.
> Sentinels are notes to humans, not scripts. Voicing one ships narration
> lost as narration. Real incident, twenty twenty six, August. Four — dash
> dash only was passed and this beat ID isn't on the list. Five — engine is
> not kokoro. That beat needs its own generator.

## B06 · MECHANISM 4 · ClaudeCodeBeat — normalize_for_tts + write_mp3 + measure

> The synth loop. For each survivor: normalize for TTS runs a small symbol
> table — psi, integral, delta x, times, squared, all the physics glyphs —
> and turns them into spoken English. Kokoro dot create returns raw samples
> at a sample rate. Write MP3 wraps the samples in a temporary wave file
> inside a copy on write scratch directory — never following a Short's legacy
> symlink — then calls ffmpeg with libmp3lame quality two to encode the final
> MP3. Measure calls ffprobe with format equals duration and returns the
> number in seconds. That number becomes the beat's actual duration s. Every
> downstream step reads that field. The engine name is never checked again.

## B07 · WORKED_EXAMPLE · ClaudeCodeBeat — demo/fixture-reel dry-run

> Worked example. Disposable fixture — one beat sheet with six beats. B zero
> and B one have plain narration. B two is marked as a source report —
> preserve the fellow's audio. B three has silent equals true. B four's
> narration starts with LOST in square brackets. B five's engine field is set
> to nbb. Run dash dash dry run against the fixture. Two beats would
> generate. Two source or silent skips. One sentinel skip. One engine skip.
> Cost: zero dollars. No mp3 written. No sheet mutated.

## B08 · MECHANISM 5 · ClaudeCodeBeat — failure modes

> Failure modes. Three loud, one quiet. Loud one — the model files aren't on
> disk. Load engine prints the exact three commands to curl them from the
> kokoro dash onnx release, then sys exits. No stack trace. Loud two — the
> kokoro dash onnx pip package isn't installed. It prints pip install kokoro
> dash onnx and sys exits. Loud three — a beat asks for a voice code Kokoro
> doesn't ship. The tool sys exits with unknown voice colon that code, see
> dash dash list voices. Observed on the badvoice fixture with am underscore
> nonexistent. Quiet one — a sentinel narration. It prints SKIPPED and moves
> on. The sheet is never mutated for a sentinel. Ever.

## B09 · VERDICT · ClaudeVerdictArtifact

> So — generate audio kokoro dot py. The free voice engine. One optional
> positional and five flags. One Kokoro ONNX model on disk — three hundred
> and thirty megabytes, one time, no account. One symbol table normalizes
> physics glyphs before synth. Five skip rules keep source reports, silences,
> sentinels, filtered beats and non kokoro beats out of the loop. Every
> survivor becomes one MP3 whose measured duration is written back into the
> beat sheet. Ground truth. Same interface as the paid engine — downstream
> never knows which engine spoke.

## B10 · YOUR_TURN · ClaudeComposerAsk

> Your turn. Paste this into Claude Code, pointed at a reel folder of your
> own that has a beat sheet with at least two speaking beats and one silent
> beat. Ask Claude to run generate audio kokoro against that folder in dash
> dash dry run first, and paste back the printed plan. Then have Claude run
> it for real on just the two speaking beats with dash dash only. Verify the
> sheet was updated — audio file and actual duration s stamped on both beats
> — and that no MP3 was written for the silent beat. Local, free, ground
> truth durations. That's the deal.

## B11 · OUTRO · ClaudeTitleOutro

> Brutalist Utility: generate audio kokoro dot py. Liam, in for Bear, for at
> Humanitarians A I.
