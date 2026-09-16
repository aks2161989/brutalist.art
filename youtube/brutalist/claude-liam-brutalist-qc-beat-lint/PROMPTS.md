# Prompts — Brutalist Utility: beat_lint.py

## Handoff prompt (B10 — Your Turn)

```
Run python3 runtime/qc/beat_lint.py on my reel directory. Report every defect with its beat ID and the fix. If any beat trips rule three, show me what a corrected lane:remotion beat with a real illustration pattern looks like for that beat's content. If any beat trips rule four, show me the exact vox-anim placeholder syntax. Exit the session only after beat_lint exits zero.
```

**What to look for in Claude's response:**
- Beat_lint exits 0 (confirmed clean) or lists specific defect IDs
- For each RULE 3 defect: Claude proposes a real illustration scene (not another text card)
- For each RULE 4 defect: Claude shows `"lane": "vox", "placeholder": "vox-anim"` syntax
- After fixes: a second lint run confirms exit 0

## Why this prompt is interesting (read aloud in narration)

This prompt turns beat_lint into a collaborative authoring tool. You're not just running the linter — you're asking Claude to interpret each defect and propose the fix that fits the beat's content. The model reads what the beat is about, picks a real illustration pattern from the registered scene library, and shows you the corrected shot block. That is a meaningful extension: from five-second check to five-minute improvement loop.

## Cold open command (B00)

```
I'm about to write a beat sheet for my explainer reel. How do I know if the beat mix is correct before I spend any time rendering?
```

Expected result lines (shown in composer output):
- "→ beat_lint.py checks your mix at author time"
- "→ flags text-card beats wearing illustration clothes"
- "→ exits 0 if clean, exits 2 with defects"
