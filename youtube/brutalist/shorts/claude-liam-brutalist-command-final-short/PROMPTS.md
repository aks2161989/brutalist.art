# PROMPTS — Brutalist Command: art final — Short (ep 33)

## On-screen prompts (1)

### B00 — the ask, in the Claude composer

> Compile this reel to a verified 4K master. Refuse on thin paperwork or an
> unfilled slate. If the new export fails any check, keep the last good file
> in place. Do not print ready unless the file on disk really is.

The Your Turn composer (B10) was dropped from this Short; the paste-ready
verification prompt remains available in the parent
`claude-liam-brutalist-command-final/vertical/PROMPTS.md`.

No AI image/video generators were called during this build. No paid API. No
uploads. The only external process is `chrome-headless-shell` (installed
locally, offline) used by the parent's Remotion beats; no re-render was needed
for this Short.

## Reproducible command sequence — Short build

```bash
export TOOLKIT=/Users/bear/…/toolkit
export PARENT=/Users/bear/…/claude-liam-brutalist-command-final
export SHORT=/Users/bear/…/shorts/claude-liam-brutalist-command-final-short

# 1. Whole-beat cut from the finished native portrait companion. Copies each
#    kept beat's native 2160×3840 mp4 and Kokoro mp3 into $SHORT independently
#    (no symlinks). No re-render, no re-narration.
python3 "$TOOLKIT/runtime/scripts/shorts.py" "$PARENT/vertical" \
  --output-dir "$SHORT" \
  --slug claude-liam-brutalist-command-final-short \
  --drop B02 B03 B04 B05 B08 B10 \
  --no-endcard --no-outro-rewrite

# 2. Compile the Short at native 4K height (2160×3840).
python3 "$TOOLKIT/runtime/scripts/compile.py" "$SHORT" \
  --height 3840 --out "$SHORT/exports/short"
```

The kept beats (B00, B01, B06, B07, B09, B11) inherit the parent's approvals
and Kokoro voice. Nothing about the source `art final` command changes.
