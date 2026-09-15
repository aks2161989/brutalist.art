# PROMPTS — Brutalist Utility: audit_review_queue.py

## B10 — Your Turn prompt (paste-ready)

```
Read runtime/scripts/audit_review_queue.py in full.

Pick two reels you have already delivered — completed episodes at
<book>/youtube/brutalist/<slug>/ with beat_sheet.json present.

Write a batch file: each line must have a number, a label, and the
reel's relative path from your books root. Example:
  1. Ep 22 art help command youtube/brutalist/claude-liam-brutalist-command-art-help
  2. Ep 23 art list command  youtube/brutalist/claude-liam-brutalist-command-art-list

Run:
  python3 runtime/scripts/audit_review_queue.py \
    --list  /path/to/batch.txt  \
    --root  /path/to/books/     \
    --out   /path/to/audit-out/

Open the audit.json it writes. For each reel check three things:
1. Is stale true or null? (true = master older than beat_sheet.json)
2. How many findings landed? (0 = clean; > 0 = read the finding categories)
3. Are all sample statuses "sampled" rather than "error"?
   (error = ffmpeg couldn't read a per-beat clip — check that clip path)

Report: the stale state of each reel, any findings, and whether all
samples are healthy. If stale is true, explain what the gap means.
```

## Demo run command (B07 evidence)

Real execution that produced the numbers shown in the film:

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/.repoloop/workspaces/claude-liam-brutalist-runtime-audit-review-queue/toolkit/runtime/scripts

echo "  1. The nopunt Skill youtube/brutalist/claude-liam-brutalist-skill-nopunt" \
  > "$TMPDIR/batch_demo.txt"

python3 audit_review_queue.py \
  --list "$TMPDIR/batch_demo.txt" \
  --root /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art \
  --out  "$TMPDIR/audit_out_demo"
```

**Actual output:**
```
01: 12 beats; 0 leads; 12 frame samples
```

This is the source for the numbers shown in B07 (ExecutedData). Command is reproducible; same numbers expected on re-run against the same unmodified reel.
