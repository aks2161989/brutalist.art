# Script — Brutalist Utility: provenance.py
# Episode 52 · run_id: 9acc8c13d5d443968a1aed379ed68b66

## B00 — ClaudeComposerAsk (cold open)
**On screen:** Composer. Greeting "Selam, Liam". Command types: `python3 provenance.py claude-liam-brutalist-runtime-provenance/`. Running indicator. Output lines reveal.

**Narration:** Selam — this is Liam, in for Bear. Every Brutalist reel is a mix: the pipeline makes some of the media, you make the rest. Provenance dot py runs one command and tells you which is which — audio fingerprint, output directory, and per-beat slot, all at once.

---

## B01 — BrutalistHesitantWriter (BLUF / executive summary)
**On screen:** Writer types: "provenance.py lists / your reel's files and counts them. / It's a **completeness** check." Word "completeness" highlights terracotta → struck through → replaced with "provenance". Final: "It's a **provenance** check."

**Narration:** Provenance dot py lists your reel's files and counts them — it's a provenance check, not a completeness check. Each file gets a label: Brutalist, meaning the pipeline rendered it; or YOU, meaning a human or gen-AI filled that slot; or Capture-question-mark, when the sheet is ambiguous.

*lead_silence_s: 0.8 — typing needs the head start*

---

## B02 — SkillTeardownPipeline (framework)
**On screen:** Three-phase horizontal flow: reel/ → [Audio | Outputs (terracotta) | Slots] → report. Phases reveal with narration. Spark line: "Audio. Outputs. Slots."

**Narration:** Provenance dot py reads three layers. First, audio: it fingerprints each MP3 by sample rate — 24 kilohertz means Kokoro, 44 kilohertz means something older. Second, video outputs: your slug dot mp4, clips, and Manim renders are always machine-made, so they're labeled Brutalist automatically. Third, per-beat slots in your media folder: that classification comes from the beat sheet itself.

---

## B03 — ClaudeCodeBeat (audio_engine source)
**On screen:** Code card — `audio_engine()` function, 12 lines. Lines reveal staggered. Spark line: "Sample rate is the fingerprint."

**Narration:** The audio fingerprint is four lines. It calls ffprobe on each MP3 and reads the sample rate. Twenty-four thousand? Kokoro — free local TTS, the pipeline's own voice. Forty-four thousand or higher? Legacy — something pre-Kokoro. No rate returned means ffprobe couldn't read the file, so it reports a question mark. The beat sheet's declared engine is printed alongside for comparison.

---

## B04 — SkillTeardownMechanism (slot_provenance design)
**On screen:** Heading "The beat sheet is the provenance record." Body text: three fields the classifier reads. Verbatim quote from source lines 47–51. Verdict: "The sheet encodes the maker."

**Narration:** The slot classifier reads the beat sheet, not the file itself. It looks at three fields: shot dot remotion dot pattern, build dot filled-by, and shot dot type. If any of those says 'remotion' or 'manim', the slot is Brutalist — the pipeline rendered it. If shot dot type says AI-VIDEO, archival, or historical image, the slot is YOU — you or a gen-AI tool supplied it. The design insight here is that the beat sheet is the provenance record. It encodes not just what plays but who made it.

---

## B05 — ClaudeCodeBeat (real demo output)
**On screen:** Code card showing actual `python3 provenance.py provenance-fixture/` output. AUDIO mismatch line highlighted. Three SLOTS lists visible.

**Narration:** Here's the command on a real fixture. Audio shows Kokoro colon one and legacy-44k colon one — there's a mismatch. The beat sheet says kokoro, but one MP3 came in at 44 kilohertz. Provenance dot py surfaces that immediately. The video line counts nine machine-made outputs. Slots: four Brutalist — B00 through B03 all have shot dot remotion set. B04 is YOU because its shot type is archival. B05 is Capture-question-mark because shot type is screen, which the classifier can't resolve.

---

## B06 — FormBCard (the three labels)
**On screen:** Three items with icons: 🤖 Brutalist / 👤 YOU / ❓ Capture? with descriptions. Items reveal on narration cues.

**Narration:** Capture-question-mark is the honest label for ambiguity. Brutalist means the pipeline rendered the slot — you can trace it back to a scene file or a Manim script. YOU means a human or gen-AI tool explicitly provided the media — the beat sheet says so. Capture-question-mark means a media file exists in the slot but the beat sheet doesn't record whether it came from capture-sim dot py or from you dropping a clip in. Older beat sheets almost always have Capture-question-marks. Newer ones with a build dot filled-by field have fewer.

---

## B07 — SkillTeardownAnatomy (prerequisites)
**On screen:** Folder tree: reel/ → beat_sheet.json (accent, required) / mp3/ / B**.mp3 / media/ / B**.mp4. Callout: "ffprobe must be on your PATH."

**Narration:** Three things must be in place for provenance dot py to give a useful report. First: ffprobe on your PATH — it's the audio fingerprinter, and without it, every MP3 returns a question mark. Second: beat-sheet dot json in the reel folder — without it the script runs but reports no beats, giving you only the audio and output counts. Third: the media folder with per-beat dot mp4 files — if those are absent, the slot map is empty. Beat-plan dot py is optional: if it's importable, the script uses fill-plan data; if the import fails, it silently continues.

---

## B08 — FormACard (failure modes)
**On screen:** Five text lines: "Failure modes." + four arrow lines, each a failure scenario.

**Narration:** Four failure modes are worth knowing. No reel directory argument: the script prints usage and exits with a nonzero code. No beat-sheet dot json: it constructs an empty beats list, so the slot map stays empty — you still get audio and output counts. Ffprobe missing from PATH: subprocess fails silently, sr() returns None, and every audio file shows a question mark engine. Beat-plan import fails: fill-plan is set to None and skipped — provenance dot py continues without it, no error raised.

---

## B09 — ClaudeVerdictArtifact (verdict)
**On screen:** Artifact card "provenance.py — What it actually gives you." Three numbered lines reveal.

**Narration:** Here's what provenance dot py actually gives you. An audio engine check: the fingerprint versus what the beat sheet declared — if those disagree, you have a stale or foreign MP3 in your audio folder. A video count: how many machine-made outputs exist, so you know if any expected files are missing. And the slot map: a Brutalist, YOU, and Capture-question-mark list per beat, so you can see exactly what you made and what the pipeline made, and chase down the ambiguous ones.

---

## B10 — ClaudeComposerAsk (Your Turn / handoff)
**On screen:** Composer with "Your turn." Prompt types. Output lines show the five steps of the prompt.

**Narration:** Your turn. Here's a paste-ready prompt: open your reel's beat-sheet dot json, run provenance dot py on the reel folder, and for each Capture-question-mark beat, read its shot block and add a build dot filled-by field — remotion colon, manim colon, capture colon, or human colon — plus a one-line note. Commit the result. This turns ambiguous slots into legible records, and the next time you run provenance dot py, the Capture-question-mark list should be shorter.

---

## B11 — HaiTitleOutro (outro)
**On screen:** Poster-style. Title "Brutalist Utility: provenance.py." @HumanitariansAI handle.

**Narration:** Brutalist Utility — provenance dot py. Liam, in for Bear.
