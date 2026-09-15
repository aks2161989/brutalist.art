# PROMPTS — Brutalist Utility: write_review_queue_report.py

run_id: aef36acf6a354924acd1af29d9d319cf

## B00 — Cold open command (shown in ClaudeComposerAsk)

```
I ran audit_review_queue.py and got audit.json and review-notes.json in my output directory. How do I turn those into a readable markdown report?
```

Expected artifact: AUDIT.md in the output directory.
Test of success: open AUDIT.md and verify it contains per-film sections with priority/finding/probe data.

## B10 — Your Turn prompt (paste-ready for viewers)

```
Read runtime/scripts/write_review_queue_report.py and runtime/scripts/audit_review_queue.py. Pick two delivered reels and run audit_review_queue.py to generate audit.json and review-notes.json. Then run: python3 runtime/scripts/write_review_queue_report.py <out-dir>. Read the AUDIT.md it produces. What does it flag as pantry requests? Are the master probes accurate for your reels? What would you change in the report structure?
```

Rubric: check pantry flags against beat_sheet.json pantry fields; verify probe dimensions match ffprobe; propose one change to hardcoded section order or content.

## Demo command (captured in demo/)

```bash
python3 runtime/scripts/write_review_queue_report.py demo/
```

Output: demo/AUDIT.md — observed and saved.
