# SCRIPT — Brutalist Utility: setup_smoke_kokoro.py — Short

Kept beats: B00, B01, B06, B08, B09, B10  
Dropped beats: B02, B03, B04, B05, B07  
Duration: 107.5s  
Voice: Liam (Kokoro am_onyx)

---

**B00 — cold open / ASK** (18.04s)

Selam — this is Liam, in for Bear. When you run dot-slash setup, one check calls setup underscore smoke underscore kokoro dot py — the audio gate. It doesn't just ask whether Kokoro imports. It synthesizes a phrase, measures the decibels, and exits zero only if the audio is real. Here's why that distinction matters.

---

**B01 — BLUF — hesitant writer** (18.0s)

The easy version of this check imports the library and sees if any errors fire. But setup underscore smoke underscore kokoro synthesizes and measures real audio — because a broken install can import cleanly and produce silence. That's the distinction the gate is built on: not whether the code runs, but whether it makes sound.

---

**B06 — failure modes — what breaks and what you read** (23.5s)

Every failure path exits one with a specific note to stderr — the script's only output. 'Kokoro model files missing' means run setup with dash dash install. synthesis raised followed by an exception means the model is corrupted or incompatible. And 'synthesized audio too quiet' with the measured dB means the synthesis ran but produced nothing useful. Setup reads exit code only — its check function discards everything the script prints.

---

**B08 — verdict** (20.46s)

The verdict. Setup underscore smoke underscore kokoro is the gap between 'Kokoro is installed' and 'Kokoro makes sound.' Three guards catch the obvious prerequisites. One synthesis catches the subtle failure — an install that imports cleanly but synthesizes nothing. The minus forty decibel gate is generous enough to ignore a whisper and strict enough to catch silence. That's the whole gate.

---

**B09 — your turn / handoff** (21.79s)

Your turn. Paste this prompt into Claude: read runtime slash scripts slash setup underscore smoke underscore kokoro dot py. If I add a new TTS backend to Brutalist, what would I need to change in this script to smoke-test it? What's the minimum gate that would catch a silent install? The answer is cleaner than you'd expect. The volume gate doesn't know which synth produced the audio — that part doesn't change. Look for what's separated from what's shared.

---

**B10 — outro** (5.71s)

Brutalist Utility: setup underscore smoke underscore kokoro. Liam, in for Bear.

---

## Dropped beats (not in this Short)

- **B02** — framework pipeline overview (ClaudeCodeBeat916)
- **B03** — three prerequisites guard code (ClaudeCodeBeat916)
- **B04** — synthesis step code (ClaudeCodeBeat916)
- **B05** — volume gate code (ClaudeCodeBeat916)
- **B07** — try/finally cleanup design tell (ClaudeCodeBeat916)

These five beats are available in the full 16:9 film and the native portrait companion.
