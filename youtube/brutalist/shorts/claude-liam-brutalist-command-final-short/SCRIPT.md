# SCRIPT — Brutalist Command: art final — Short (ep 33)

Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`. Register: Teardown. 6
retained beats. No captions. Whole-beat cut of the finished vertical parent
(B02, B03, B04, B05, B08, B10 dropped — see `CUT-PLAN.json`). No narration
rewritten; every beat plays the parent's mp3 unchanged.

## B00 — ASK  (ClaudeComposerAsk916, cold open)
"Hei, this is Liam, in for Bear. The ask — compile this reel to a verified 4K master. Refuse if the paperwork is thin or a beat is still a slate. If the new export fails any check, keep the last good file in place. Do not print `ready` unless the file on disk really is."

## B01 — BLUF  (BrutalistHesitantWriter916)
"Watch the writer walk this back. Art final does not render once. It gates the paperwork, renders, and then re-verifies the output it just wrote. Two lines of defence, one written next to the other on the receipt."

Hesitant text: `art final\nrenders\nonce.`
Trigger: `renders, once` → replacement: `verifies, twice`
Final corrected: `art final\nverifies twice.`

## B06 — MECHANISM  (ClaudeCodeBeat916)
"The atomic bit. Compile.py encodes into a candidate.mp4 inside a temp folder next to your --out. Only after Gate V passes and the approvals recheck succeeds does the candidate get os.replaced onto the final path. If any check fails — Gate V, an approval turning stale mid-render, a source file changing hash — the temp folder is thrown away, the previous verified export stays in place, and build-state records the failure. There is never a moment when the file on disk is between two versions."

## B07 — MECHANISM  (ClaudeCodeBeat916)
"The receipt is five keys. Status equals ready. Output — the absolute path. SHA-256 of the mp4. Input_sha256 — every media file and every narration mp3 hashed by name. Duration_s from the timeline the audio built. And a timestamp. Ready is a machine claim about the checks that just passed. It is not human approval, and it is not a promise of YouTube 4K processing. Publication is a separate human step."

## B09 — VERDICT  (ClaudeVerdictArtifact916)
"So — art final. One dispatcher branch, one Python script, two verbs. It gates the paperwork, encodes into a temp, gates the pixels, re-checks approvals, and only then swaps the file in. It writes a receipt beside the mp4. Slates and pending signatures block the master unconditionally. Every guarantee — last good file preserved, receipt matches file, sheet did not drift mid-render — falls out of that same atomic pattern."

Artifact lines (unchanged from the parent):
- bare invocation — `./art final <reel> [--out DIR] [--height 2160]`; forwards to `python3 runtime/scripts/compile.py`.
- one script, two verbs — `--review` writes a slate-marked cut beside the reel; no `--review` writes a clean master to `--out`.
- final_preflight fails fast — paperwork triad + beat_lint + gate_shape before the first ffmpeg call.
- atomic candidate write — candidate encodes into a temp, gates run against it, `os.replace` swaps it in; a failure never overwrites the last verified export.
- verified.json is the receipt — SHA-256 of the mp4, SHA-256 of every input, duration, ISO timestamp; ready is a machine claim, not human sign-off.
- slates and approvals block the master — `--allow-slates` is review-only, `--no-gate` cannot bypass approvals; a pending signature never ships.

## B11 — OUTRO  (ClaudeTitleOutro916)
"Brutalist Command: art final. Liam, in for Bear, for at Humanitarians A I."

Title card: **Brutalist Command: art final.** · `@NikBearBrown` · slug-seeded mascot (locked per `OUTRO-LOCK.md`).
