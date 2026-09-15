# SCRIPT — Brutalist Utility: audit_review_queue.py — Short

Short cut: 6/12 beats, ~122.0s. Dropped B02/B03/B04/B06/B08/B10.

## Kept beats

### B00 — ASK (cold open) · 25.2s
Bula. This is Liam, in for Bear. audit_review_queue.py is a read-only batch inspector for Brutalist reels. Give it a numbered list of reel paths and it walks every folder: hashing beat sheets, probing master MP4s, sampling per-beat source clips at the 70-percent mark for contact sheets, and flagging anything worth a human look — stale masters, pantry paths that should be code, math layout mismatches. It never approves. It never publishes. It writes evidence and stops.

### B01 — BLUF (hesitant writer) · 19.2s
Before the script reads a single file, fix the first misconception. audit_review_queue.py does not decide if a reel ships. The script's own docstring says it plainly: never approves, never publishes. It reads source structure, samples frames, and writes review leads — flags that point a human where to look, not proof of fabrication. This is Liam. Let's take it apart.

### B05 — DESIGN TELL (stale master) · 20.5s
One design decision worth the Teardown lens: stale master detection. The script compares the master MP4's modification time against the beat sheet's. If the beat sheet is newer than the master, the contact sheet frames you're reviewing may not match what the current sheet describes — the render is stale. The flag is informational. It does not block the audit and does not touch either file. It just names the gap.

### B07 — EVIDENCE (live audit run) · 22.3s
Here's the real output from a live audit run against the nopunt skill episode — a completed reel with all twelve source clips present. Twelve beats found. Twelve frame samples taken at the 70-percent mark of each per-beat clip. Zero review leads. No pantry paths, no math layout errors, no overflow claims in narration. The output line is the contract: beat count, lead count, sample count — nothing else is printed to stdout.

### B09 — VERDICT · 28.7s
The verdict. The stale-master check is the one signal the rest of the pipeline cannot give you — it names when source and render are out of sync. The 70-percent frame position is a deliberate design choice: it skips the slate frame at clip start and freeze artifacts near the end, capturing a settled mid-play state. What it bites on: silent ffmpeg tile failures look identical to healthy tiles unless you count them. And math_layout_check has no fallback — a missing local module crashes the entire batch before the first reel opens.

### B11 — OUTRO · 6.0s
That was Brutalist Utility: audit_review_queue.py. Liam, in for Bear.

---

## Dropped beats (belong in the 16:9 long)

- B02 FRAMEWORK — Invocation flags walkthrough (--list, --root, --out syntax)
- B03 PIPELINE — Four-phase anatomy (Parse/Audit/Sample/Report internals)
- B04 MECHANISM — Finding categories code walkthrough
- B06 PREREQUISITES — Hard dependency list (PIL, math_layout_check, ffmpeg)
- B08 FAILURE — Failure modes code walkthrough
- B10 YOUR_TURN — Detailed two-reel batch exercise with rubric
