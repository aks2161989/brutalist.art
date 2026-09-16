# SCRIPT — Brutalist Utility: write_review_queue_report.py

Episode 56. Liam, in for Bear. Kokoro am_onyx. @HumanitariansAI. 12 beats.

---

## B00 — Cold open (ClaudeComposerAsk)

**Greeting:** Merhaba, Liam (Turkish — world-language hello)

**Narration:**
Merhaba. This is Liam, in for Bear. write_review_queue_report.py is the last step in the Brutalist audit chain — the moment two JSON files become a human-readable markdown report. It reads machine data from audit.json and your visual findings from review-notes.json, and writes AUDIT.md without touching a single reel.

---

## B01 — BLUF (BrutalistHesitantWriter)

**Writer correction:** "generates" → "formats"; "inspects" → "reads"

**Typed text (before correction):**
write_review_queue_report.py
generates the audit.
It inspects every reel.

**After correction:**
write_review_queue_report.py
formats the audit.
It reads every reel.

**Narration:**
write_review_queue_report.py doesn't audit anything. It takes two JSON files — audit.json with machine-measured data and review-notes.json with your visual findings — and turns them into a readable markdown report. The actual auditing happened earlier. This script is the pen that writes the summary. Read-only by design: the docstring says it plain — never mutate reels.

---

## B02 — Framework (SkillTeardownPipeline)

**Narration:**
The script takes two files in, writes one file out. audit.json carries machine-measured data — reel hashes, durations, slate counts, stale status. review-notes.json carries your human visual findings — what you saw on screen, ranked by priority. write_review_queue_report.py combines them into AUDIT.md, one section per reel. The reels themselves are never touched.

---

## B03 — Mechanism: reading inputs (ClaudeCodeBeat)

**Narration:**
Line one: the output directory is the only argument. The script reads audit.json from that folder and expects an exact schema — reels as a list of rows, each row carrying reel number, reel path, probe data, and stale status. review-notes.json maps reel numbers to priority and finding strings. Miss either file or misname a key and the script crashes. There is no try-except.

---

## B04 — Mechanism: main loop (ClaudeCodeBeat)

**Narration:**
For each reel, the script looks up the human note by number — stored in review-notes.json as a string key. The priority and finding go into a bold markdown header. Below that: the master probe data — width, height, duration, stale flag, declared slate count. Then it reads the reel's beat_sheet.json and scans every beat for pantry references.

---

## B05 — Mechanism: pantry flags (ClaudeCodeBeat)

**Narration:**
The script flags every beat that still has a pantry reference — an image slot waiting on a human to source it. The comment in the code names it plainly: all three legacy spellings occur in this queue — pantry_path, pantry_file, and pantry. This is backward compatibility written as a comment, not hidden in a migration script. The schema evolved; the reader handles all three forms.

---

## B06 — Output structure (SkillTeardownMechanism)

**Narration:**
AUDIT.md has a fixed structure: a scope statement, main findings, rules and tooling changes, repair order, a section for every film — priority, finding, master probe, reel link, and any pantry-requesting beats. That structure is baked into Python string literals. The script author decided which sections matter. You cannot configure it — if the report shape needs to change, change the source.

---

## B07 — Failure modes (ClaudeCodeBeat)

**Narration:**
The script has no error handling. That is intentional. If audit.json is missing you get a FileNotFoundError. If a reel number is in audit.json but not in review-notes.json you get a KeyError. If a reel folder moved since audit_review_queue.py ran, the beat_sheet.json read crashes. These failures tell you exactly what to fix. A silent pass on bad inputs would be worse.

---

## B08 — Limits (SkillTeardownMechanism)

**Narration:**
The report is honest about its own limits. Twelve frames per film at 70% position is a heuristic — it catches settled-state defects but misses mid-animation states. Pantry flags are metadata, not a pixel check. The report explicitly says it is a queue-wide sample audit, not continuous playback, not a full fact-check, and not approval to publish.

---

## B09 — Verdict (ClaudeVerdictArtifact)

**Narration:**
write_review_queue_report.py is small and intentional. Two inputs, one output, no mutation. The three-spelling pantry check is backward compatibility named in the code. The no-try-except policy means failures are diagnostic, not silent. The report quotes its own limitations. Run it at the end of the audit pipeline and AUDIT.md is your deliverable — but it tells you exactly what it is not.

---

## B10 — Your Turn (ClaudeComposerAsk)

**Greeting:** Your Turn

**Paste-ready prompt:**
Read runtime/scripts/write_review_queue_report.py and runtime/scripts/audit_review_queue.py. Pick two delivered reels and run audit_review_queue.py to generate audit.json and review-notes.json. Then run: python3 runtime/scripts/write_review_queue_report.py <out-dir>. Read the AUDIT.md it produces. What does it flag as pantry requests? Are the master probes accurate for your reels? What would you change in the report structure?

**Narration:**
Here's the prompt. Paste this into Claude with your own reel batch in mind. Run audit_review_queue.py first to get audit.json and review-notes.json, then point write_review_queue_report.py at that output directory. Read the AUDIT.md it produces. Look at the pantry flags — are there beats waiting on human images? Check the master probe lines. Then ask: what would you change about the report structure itself? This is Liam, in for Bear.

---

## B11 — Outro (ClaudeTitleOutroHAI)

**Narration:**
Brutalist Utility: write_review_queue_report.py. Liam, in for Bear.

**Visual:** Title card with @HumanitariansAI handle and slug-seeded mascot (bounce animation).
