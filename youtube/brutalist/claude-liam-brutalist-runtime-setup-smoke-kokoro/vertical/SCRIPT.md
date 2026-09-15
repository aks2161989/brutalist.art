# SCRIPT — Brutalist Utility: setup_smoke_kokoro.py

**Persona:** Liam, in for Bear  
**Voice:** Kokoro am_onyx  
**Channel:** @HumanitariansAI  
**Register:** Teardown (Feynman × MKBHD)

---

## B00 — Cold Open (ClaudeComposerAsk)

*Greeting: "Selam, Liam"*

Selam — this is Liam, in for Bear. When you run dot-slash setup, one check calls setup underscore smoke underscore kokoro dot py — the audio gate. It doesn't just ask whether Kokoro imports. It synthesizes a phrase, measures the decibels, and exits zero only if the audio is real. Here's why that distinction matters.

---

## B01 — BLUF / Hesitant Writer Overview (BrutalistHesitantWriter)

*lead_silence_s: 0.8*

The easy version of this check imports the library and sees if any errors fire. But setup underscore smoke underscore kokoro synthesizes and measures real audio — because a broken install can import cleanly and produce silence. That's the distinction the gate is built on: not whether the code runs, but whether it makes sound.

*On screen: writer types "setup checks Kokoro by / verifying the import works. / Loading the model is enough." — then corrects "import" → "synthesis" and "enough" → "insufficient".*

---

## B02 — Framework: What Is This Script (SkillTeardownPipeline)

The script is setup's audio gate. Setup calls it in its check function, discards everything it prints to stderr, and reports its own MISS message if it fails. The gate runs five checks in sequence: three prerequisites, then one synthesis, then one decibel measurement. Every step can fail independently, and each failure path exits one with a one-liner naming the exact problem.

---

## B03 — Mechanism: The Three Prerequisites (ClaudeCodeBeat)

The first three checks are strict. The model file and voices binary must exist at their exact paths under runtime slash models. If ffmpeg isn't on the PATH, fail. If kokoro underscore onnx won't import, fail. Each fails with a specific one-line message to stderr. No ambiguity about what's missing.

---

## B04 — Mechanism: The Synthesis Step (ClaudeCodeBeat)

Then it actually synthesizes. One throwaway phrase via the same Kokoro class narration beats use. The float samples convert to signed sixteen-bit integers, then write into a real WAV file in the system temp directory. A module that loads but synthesizes silence gets no free pass here — this is the moment that separates a broken silent install from a working one.

---

## B05 — Mechanism: The Volume Gate (ClaudeCodeBeat)

Then ffmpeg's volumedetect filter reads the WAV and prints mean underscore volume — the average decibel level. The script parses that from stderr and checks it against negative forty decibels. Real speech sits around negative twelve to negative twenty. Silence or a corrupt output comes in below negative forty. That's the gate. If the synthesized audio doesn't cross it, exit one.

---

## B06 — Failure Modes: What Breaks and What You Read (ClaudeCodeBeat)

Every failure path exits one with a specific note to stderr — the script's only output. 'Kokoro model files missing' means run setup with dash dash install. synthesis raised followed by an exception means the model is corrupted or incompatible. And 'synthesized audio too quiet' with the measured dB means the synthesis ran but produced nothing useful. Setup reads exit code only — its check function discards everything the script prints.

---

## B07 — Design Tell: The try/finally Cleanup (ClaudeCodeBeat)

The design tell is the try-finally block. The temp WAV is created before the volume check, and the finally clause deletes it unconditionally — whether the check passed or failed, whether ffmpeg threw an error, whether mean underscore volume was None. The docstring calls it 'one throwaway phrase.' This is the script's contract with itself: no temp files left behind, no manual cleanup needed.

---

## B08 — Verdict (ClaudeVerdictArtifact)

The verdict. Setup underscore smoke underscore kokoro is the gap between 'Kokoro is installed' and 'Kokoro makes sound.' Three guards catch the obvious prerequisites. One synthesis catches the subtle failure — an install that imports cleanly but synthesizes nothing. The minus forty decibel gate is generous enough to ignore a whisper and strict enough to catch silence. That's the whole gate.

---

## B09 — Your Turn (ClaudeComposerAsk)

*Greeting: "Your turn."*

Your turn. Paste this prompt into Claude: read runtime slash scripts slash setup underscore smoke underscore kokoro dot py. If I add a new TTS backend to Brutalist, what would I need to change in this script to smoke-test it? What's the minimum gate that would catch a silent install? The answer is cleaner than you'd expect. The volume gate doesn't know which synth produced the audio — that part doesn't change. Look for what's separated from what's shared.

---

## B10 — Outro (ClaudeTitleOutro)

Brutalist Utility: setup underscore smoke underscore kokoro. Liam, in for Bear.
