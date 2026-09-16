# SCRIPT — Brutalist Command: art final (ep 33)

Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`. Register: Teardown. 12 beats. No captions.

## B00 — ASK  (ClaudeComposerAsk, cold open)
"Hei, this is Liam, in for Bear. The ask — compile this reel to a verified 4K master. Refuse if the paperwork is thin or a beat is still a slate. If the new export fails any check, keep the last good file in place. Do not print `ready` unless the file on disk really is."

## B01 — BLUF  (BrutalistHesitantWriter)
"Watch the writer walk this back. Art final does not render once. It gates the paperwork, renders, and then re-verifies the output it just wrote. Two lines of defence, one written next to the other on the receipt."

Hesitant text: `art final\nrenders once.`
Trigger: `renders,once.` → replacement: `verifies,twice.`
Final corrected: `art final\nverifies twice.`

## B02 — FRAMEWORK  (ClaudeCodeBeat)
"The dispatcher is one case in the art file. It matches the exact string final, checks whether you already passed a --height, and forwards everything to compile.py. If you did not name a height, it hardcodes 2160 — the native 4K master. There are no aliases. Every rule the command enforces lives inside compile.py."

## B03 — FRAMEWORK  (ClaudeCodeBeat)
"Compile.py's argparse surface is small on purpose. A reel folder. Optional --review, which is the reason art run and art final are the same script — the review path draws beat labels and stays beside the reel. Then --fps, --height, --audio, --force, --allow-slates, and --out. --allow-slates is review-only; a final refuses slates unconditionally. --out picks the destination — a local folder, a mounted drive, anywhere."

## B04 — FRAMEWORK  (ClaudeCodeBeat)
"When --review is off, final_preflight runs before a single frame renders. It calls require_paperwork — a FACTCHECK, a SHOTLIST, and a PROMPTS file, each nonempty. Then it runs beat_lint and gate_shape as executable Python. If either gate exits non-zero, final refuses. The lint runs on the sheet, not the mp4 — you fail fast, before you spend the render."

## B05 — WORKED_EXAMPLE  (ClaudeCodeBeat)
"Here is a tiny reel with one still, three seconds of narration, and the three paperwork files. Art final prints a single line per beat, a motion histogram, a build stamp, then the mp4 path. Next to the mp4 is a verified.json file the compiler wrote itself — the SHA-256 of the export, and the SHA-256 of every input that fed it. This receipt is what downstream tools use to match the file to its recipe."

## B06 — MECHANISM  (ClaudeCodeBeat)
"The atomic bit. Compile.py encodes into a candidate.mp4 inside a temp folder next to your --out. Only after Gate V passes and the approvals recheck succeeds does the candidate get os.replaced onto the final path. If any check fails — Gate V, an approval turning stale mid-render, a source file changing hash — the temp folder is thrown away, the previous verified export stays in place, and build-state records the failure. There is never a moment when the file on disk is between two versions."

## B07 — MECHANISM  (ClaudeCodeBeat)
"The receipt is five keys. Status equals ready. Output — the absolute path. SHA-256 of the mp4. Input_sha256 — every media file and every narration mp3 hashed by name. Duration_s from the timeline the audio built. And a timestamp. Ready is a machine claim about the checks that just passed. It is not human approval, and it is not a promise of YouTube 4K processing. Publication is a separate human step."

## B08 — FAILURE_RECOVERY  (ClaudeCodeBeat)
"One failure worth showing. Same reel. Truncate FACTCHECK.md to zero bytes — mimicking the accidental commit that empties a paperwork file. Re-run. Art final refuses immediately: gate F, missing or empty. The mp4 in exports is unchanged; the SHA-256 you had before is the SHA-256 you have now. The recovery is one line — put a real sentence back in FACTCHECK.md — and the next art final exits zero."

## B09 — VERDICT  (ClaudeVerdictArtifact)
"Art final — the whole surface, in the order you use it."

Artifact lines:
- bare invocation — `./art final <reel> [--out DIR] [--height 2160]`; forwards to `python3 runtime/scripts/compile.py`.
- one script, two verbs — `--review` writes a slate-marked cut beside the reel; no `--review` writes a clean master to `--out`.
- final_preflight fails fast — paperwork triad + beat_lint + gate_shape before the first ffmpeg call.
- atomic candidate write — candidate encodes into a temp, gates run against it, `os.replace` swaps it in; a failure never overwrites the last verified export.
- verified.json is the receipt — SHA-256 of the mp4, SHA-256 of every input, duration, ISO timestamp; ready is a machine claim, not human sign-off.
- slates and approvals block the master — `--allow-slates` is review-only, `--no-gate` cannot bypass approvals; a pending signature never ships.

## B10 — YOUR_TURN  (ClaudeComposerAsk, greeting "Your Turn")
"Your turn. Paste this into Claude Code, pointed at a reel folder you finished this week. Run art final with a --out flag pointed at a fresh directory. Copy the printed SHA-256 out of exports and hash the file yourself with shasum minus a two-five-six. If those two strings match, the receipt describes the file. If they do not, something wrote to your export after the compile — investigate before you share the video."

## B11 — OUTRO  (ClaudeTitleOutro)
"Brutalist Command: art final. Liam, in for Bear, for at Humanitarians A I."
