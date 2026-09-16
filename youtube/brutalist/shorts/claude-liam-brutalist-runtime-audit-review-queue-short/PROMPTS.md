# PROMPTS — Brutalist Utility: audit_review_queue.py — Short

Short cut: 6/12 beats. B10 (Your Turn) was dropped — the paste-ready prompt belongs in the 16:9 long.

## Demo run command (B07 evidence source)

Real execution that produced the numbers shown in B07 (ExecutedData916):

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

This is the source for the numbers shown in B07 (ExecutedData916). Command is reproducible; same numbers expected on re-run against the same unmodified reel.

## Your Turn prompt (B10 — not in this Short)

The full Your Turn exercise is in the 16:9 long film. Paste-ready prompt preserved in the parent vertical's PROMPTS.md.
