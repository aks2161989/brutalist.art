# PROMPTS — Brutalist Utility: setup_smoke_kokoro.py

## B09 — Your Turn handoff prompt (paste-ready)

```
Read runtime/scripts/setup_smoke_kokoro.py. If I add a new TTS backend to Brutalist, what would I need to change in this script to smoke-test it? What's the minimum gate that would catch a silent install?
```

**What this prompt does:** Asks Claude to reason about the script's architecture — specifically which parts are Kokoro-specific and which are backend-agnostic. The volume gate (ffmpeg volumedetect → mean_db > -40 dB) is generic; the synthesis block (Kokoro instantiation + k.create()) is the only part that needs swapping.

**What to look for in Claude's answer:** Claude should identify the synthesis block (lines 41–56) as the only Kokoro-specific section, and correctly note that the WAV-write, volumedetect, and -40 dB threshold stay unchanged. If it suggests changing the threshold, push back — the threshold is backend-agnostic.

**Why this prompt is interesting:** It turns the episode's core lesson into an open-ended design question. The answer reveals the separation of concerns the script was designed around: the gate (what counts as real audio) is separated from the synthesizer (how to produce audio). That's an architectural choice, not just code style.
