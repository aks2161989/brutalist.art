# PROMPTS

No LLM was called to generate audio, script or scene content in this reel.

## Narration synthesis

Every narration beat was synthesised locally by Kokoro `am_onyx` via the very utility this reel teaches:

```
$ export KOKORO_MODEL=<toolkit>/runtime/models/kokoro/kokoro-v1.0.onnx
$ export KOKORO_VOICES=<toolkit>/runtime/models/kokoro/voices-v1.0.bin
$ export ART_HOME=<toolkit>
$ python3 runtime/scripts/generate_audio_kokoro.py \
    youtube/brutalist/claude-liam-brutalist-runtime-generate-audio-kokoro
[kokoro] beat-B00.mp3  15.53s  voice=am_onyx
[kokoro] beat-B01.mp3  10.58s  voice=am_onyx
[kokoro] beat-B02.mp3  29.82s  voice=am_onyx
[kokoro] beat-B03.mp3  25.92s  voice=am_onyx
[kokoro] beat-B04.mp3  39.64s  voice=am_onyx
[kokoro] beat-B05.mp3  29.87s  voice=am_onyx
[kokoro] beat-B06.mp3  38.95s  voice=am_onyx
[kokoro] beat-B07.mp3  27.41s  voice=am_onyx
[kokoro] beat-B08.mp3  35.14s  voice=am_onyx
[kokoro] beat-B09.mp3  31.04s  voice=am_onyx
[kokoro] beat-B10.mp3  28.80s  voice=am_onyx
[kokoro] beat-B11.mp3  6.83s  voice=am_onyx
[kokoro] 12 beat(s) generated · cost $0.00 · durations are GROUND TRUTH,
         same as generate_audio.py
```

Nothing was sent over the network; no API key of any kind was used. Cost: $0.00.

## Scene rendering

Rendered by the isolated toolkit's `runtime/scripts/remotion_scenes.py` — one composition per beat, `--concurrency=1`, `--scale=2`, `--image-format=png`, `--crf=16`, in the sandbox-safe wrapper:

```
$ export ART_CHROME=<toolkit>/runtime/scripts/_chrome_wrap.sh
$ export ART_CHROME_MODE=chrome-for-testing
$ python3 runtime/scripts/remotion_scenes.py <reel>
[remotion] B00: ok: ClaudeComposerAsk -> media/B00.mp4
[remotion] B01: ok: BrutalistHesitantWriter -> media/B01.mp4
[remotion] B02: ok: SkillTeardownPipeline -> media/B02.mp4
[remotion] B03: ok: ClaudeCodeBeat -> media/B03.mp4
[remotion] B04: ok: ClaudeCodeBeat -> media/B04.mp4
[remotion] B05: ok: ClaudeCodeBeat -> media/B05.mp4
[remotion] B06: ok: ClaudeCodeBeat -> media/B06.mp4
[remotion] B07: ok: ClaudeCodeBeat -> media/B07.mp4
[remotion] B08: ok: ClaudeCodeBeat -> media/B08.mp4
[remotion] B09: ok: ClaudeVerdictArtifact -> media/B09.mp4
[remotion] B10: ok: ClaudeComposerAsk -> media/B10.mp4
[remotion] B11: ok: ClaudeTitleOutro -> media/B11.mp4
```

`_chrome_wrap.sh` invokes the already-cached `chrome-headless-shell` with `--single-process --in-process-gpu` per the documented `ART_CHROME` hook (feedback: [[chrome-sandbox-remotion-fix]]).

## Component overrides applied to the isolated toolkit

- `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx` — portrait scale patch: replaced `const scale = Math.min(width / 1920, height / 1080)` with the height>width ternary so 9:16 BLUF coverage clears Gate V (feedback: [[brutalist-hesitant-writer-portrait-scale-patch]]).
- `runtime/remotion/src/scenes/ClaudeCodeBeat.tsx` — adaptive font clamp: replaced fixed `fontSize: height * 0.022` with `Math.min(baseFont, availH/(lines*lineH), availW/(longest*charRatio))` so long code stanzas fit in both aspects (feedback: [[claude-code-beat-adaptive-font]]).
- `runtime/remotion/src/Root.tsx` — added `<Composition id="ClaudeCodeBeat916" width=1080 height=1920>` and `<Composition id="SkillTeardownMechanism916" width=1080 height=1920>` to enable the native portrait swaps for the vertical companion.

These overrides live only in this isolated toolkit; the public toolkit is unchanged.
