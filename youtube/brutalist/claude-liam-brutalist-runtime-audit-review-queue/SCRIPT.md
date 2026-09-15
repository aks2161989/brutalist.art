# SCRIPT — Brutalist Utility: audit_review_queue.py

**Slug:** claude-liam-brutalist-runtime-audit-review-queue
**Run ID:** edb2d009ee804ed2a476f5bc953eb4cb
**Voice:** Liam, in for Bear · Kokoro am_onyx
**Channel:** @HumanitariansAI · Playlist: Brutalist
**Register:** Teardown
**Beats:** 12 (B00–B11)

---

## B00 — Cold open (ClaudeComposerAsk)

**Act:** ASK
**Pattern:** ClaudeComposerAsk
**Greeting:** Bula, Liam
**Topic:** BRUTALIST UTILITY · audit_review_queue.py
**Segment:** Source Audit, Not Approval

**Command typed:**
> I need to inspect a batch of Brutalist reels before review. What does audit_review_queue.py check, and what can it tell me that probing the rendered video cannot?

**Output lines:**
- reads every reel's beat_sheet.json and probes its master MP4
- samples source-beat clips at 70% position for contact sheets
- flags review leads — never approves, never publishes

**Narration:** Bula. This is Liam, in for Bear. audit_review_queue.py is a read-only batch inspector for Brutalist reels. Give it a numbered list of reel paths and it walks every folder: hashing beat sheets, probing master MP4s, sampling per-beat source clips at the 70-percent mark for contact sheets, and flagging anything worth a human look — stale masters, pantry paths that should be code, math layout mismatches. It never approves. It never publishes. It writes evidence and stops.

---

## B01 — BLUF (BrutalistHesitantWriter)

**Act:** BLUF
**Pattern:** BrutalistHesitantWriter
**Text typed (with correction):**
```
audit_review_queue.py
approves reels
for human review.
```
**Trigger:** `approves` → `documents`
**Final text:** audit_review_queue.py documents reels for human review.

**Narration:** Before the script reads a single file, fix the first misconception. audit_review_queue.py does not decide if a reel ships. The script's own docstring says it plainly: never approves, never publishes. It reads source structure, samples frames, and writes review leads — flags that point a human where to look, not proof of fabrication. This is Liam. Let's take it apart.

---

## B02 — Invocation syntax (ClaudeCodeBeat)

**Act:** FRAMEWORK
**Pattern:** ClaudeCodeBeat
**Title:** audit_review_queue.py — invocation
**Code:** three required flags + batch.txt format + example batch.txt
**Spark line:** Three flags. No defaults.

**Narration:** Three required flags, all mandatory. --list points at a text file of numbered reel entries. --root is the books directory the script resolves relative paths against. --out is where the evidence lands: numbered source JSON files, contact sheets, and a rolled-up audit.json. The batch file format is human-readable: a number, a dot, a description label, then the path. The parser extracts the last slash-containing token from each line.

---

## B03 — Pipeline phases (FormBCard)

**Act:** PIPELINE
**Pattern:** FormBCard
**Title:** Per-reel audit pipeline
**Items:** Parse → Audit → Sample → Report

**Narration:** Per reel, four phases. Parse the list with a strict regex — empty or duplicate entries throw before any reel is touched. Audit opens the beat sheet, probes the master MP4 if one exists, and runs the math layout check. Sample takes source-beat clips — the individual per-beat MP4s — and grabs one frame at 70 percent of each clip's duration. Report writes a numbered JSON per reel plus a rolled-up audit.json with the batch scope and limitations clause.

---

## B04 — Findings categories (ClaudeCodeBeat)

**Act:** MECHANISM
**Pattern:** ClaudeCodeBeat
**Title:** audit_review_queue.py — findings
**Code:** the four finding types from the script
**Spark line:** Four categories. All review leads.

**Narration:** Four finding categories. Math layout errors come from the math_layout_check import — it flags flat notation like sigma-over-slash in FormACard props where structured rendering is required. Pantry paths split two ways: if the visual intent suggests terminal output or notebook rows, it's a replace-with-code lead; otherwise it's a source-artifact-review. Overflow-to-infinity narration patterns get their own flag. Every finding carries confidence: source-confirmed, routing-review, or review.

---

## B05 — Stale master detection (ClaudeCodeBeat)

**Act:** DESIGN TELL
**Pattern:** ClaudeCodeBeat
**Title:** audit_review_queue.py — stale master
**Code:** stale detection logic from the script
**Spark line:** Timestamp delta. The design tell.

**Narration:** One design decision worth the Teardown lens: stale master detection. The script compares the master MP4's modification time against the beat sheet's. If the beat sheet is newer than the master, the contact sheet frames you're reviewing may not match what the current sheet describes — the render is stale. The flag is informational. It does not block the audit and does not touch either file. It just names the gap.

---

## B06 — Prerequisites (ClaudeCodeBeat)

**Act:** PREREQUISITES
**Pattern:** ClaudeCodeBeat
**Title:** audit_review_queue.py — dependencies
**Code:** import section annotated
**Spark line:** Three hard deps. No fallback.

**Narration:** Three hard dependencies at import time. PIL — the script calls Image.new and ImageDraw.Draw to build contact sheets; no Pillow, no contact sheets, no run. math_layout_check — a local module in runtime/scripts; if it's missing, the import fails before argument parsing. ffmpeg and ffprobe — called via subprocess for probing and frame extraction; absent binaries produce empty contact tiles and zero-byte probes, with no warning unless ffmpeg itself is absent from PATH.

---

## B07 — Real demo output (ExecutedData)

**Act:** EVIDENCE
**Pattern:** ExecutedData
**Mode:** table
**Rows:** real numbers from the demo run on claude-liam-brutalist-skill-nopunt
**Note:** Audit of claude-liam-brutalist-skill-nopunt · all source clips present

**Narration:** Here's the real output from a live audit run against the nopunt skill episode — a completed reel with all twelve source clips present. Twelve beats found. Twelve frame samples taken at the 70-percent mark of each per-beat clip. Zero review leads. No pantry paths, no math layout errors, no overflow claims in narration. The output line is the contract: beat count, lead count, sample count — nothing else is printed to stdout.

---

## B08 — Failure modes (ClaudeCodeBeat)

**Act:** FAILURE
**Pattern:** ClaudeCodeBeat
**Title:** audit_review_queue.py — failure modes
**Code:** the three failure scenarios
**Spark line:** Two hard stops. One silent tile.

**Narration:** Three failure modes. The first two are hard stops before any reel is touched: an empty list and a list with duplicate paths both raise ValueError immediately. The third is silent: if ffmpeg cannot extract a frame — wrong path format, corrupt clip, codec gap — the contact sheet tile stays blank and the sample record carries status error. The audit continues for all other beats. You find out in the contact sheet image, not in stderr.

---

## B09 — Verdict (ClaudeVerdictArtifact)

**Act:** VERDICT
**Pattern:** ClaudeVerdictArtifact
**Title:** audit_review_queue.py
**Heading:** Source evidence, not approval

**Narration:** The verdict. What it gets right: the stale-master check is the one signal that tells you source and render are out of sync, and it is absent from every other pipeline tool. The 70-percent frame position is a deliberate design choice — it avoids both the slate frame at clip start and freeze artifacts at the end, so the contact sheet captures a settled mid-play state. What it bites on: the ffmpeg tile failure is silent; contact sheets with blank tiles look the same as contact sheets with healthy tiles unless you count them. And math_layout_check has no fallback — a missing local module crashes the entire run before the first reel is opened.

---

## B10 — Your Turn (ClaudeComposerAsk)

**Act:** YOUR_TURN
**Pattern:** ClaudeComposerAsk
**Greeting:** Your Turn
**Topic:** BRUTALIST UTILITY · audit_review_queue.py
**Segment:** Run it on your own reel batch

**Narration:** Your turn. Paste this into Claude Code. Pick two reels you have already delivered — complete episodes, not in-progress builds. Write a two-line batch file: each line has a number, a label, and the reel's relative path from your books root. Run audit_review_queue.py with --list, --root, and --out pointing at a scratch directory. Open the audit.json it writes. For each reel, check three things: is stale true or null, how many findings landed, and are all sample statuses sampled rather than error. If stale is true, the master predates the sheet. If a sample is error, check the per-beat clip path.

---

## B11 — Outro (ClaudeTitleOutro)

**Act:** OUTRO
**Pattern:** ClaudeTitleOutro
**Title:** Brutalist Utility: audit_review_queue.py
**Slug:** claude-liam-brutalist-runtime-audit-review-queue

**Narration:** That was Brutalist Utility: audit_review_queue.py. Liam, in for Bear.
