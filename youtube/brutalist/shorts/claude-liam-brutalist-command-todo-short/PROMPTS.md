# PROMPTS — Brutalist Command: art todo — Short (9:16)

Derivative of the 16:9 long / native-portrait companion. This Short reuses the
parent's already-generated Kokoro `am_onyx` MP3s beat-by-beat, unchanged. No
audio is regenerated for this Short (no `--rewrite-outro`).

## Kokoro (voice) prompts

Every retained beat's `mp3/beat-<BID>.mp3` is the parent file, copied as an
independent file, hashes recorded in `VISUAL-REVIEW.json`. Voice `am_onyx`
per beat and in metadata. Text is the exact `narration_text` from the parent
`beat_sheet.json`, preserved in the derivative sheet.

## Composer / Ask beat prompts on-screen

### B00 — cold open ask (result lines pre-answered)

```
$ art todo my-reel/ --open
```

Result lines (populated in `ClaudeComposerAsk916.output`):

- `reads beat_sheet.json — no other input`
- `writes todo.json + STATUS.md + ToDo.md`
- `--open filter → only beats still needing a clip`

The parent's B10 "Your Turn" ClaudeComposerAsk916 was DROPPED in this Short;
its full paste-ready Claude Code prompt is not shown here. Fellows can view
the full long-form Your Turn in the 16:9 parent film / vertical companion.

## Live demonstration commands (executed local on this workstation)

Captured in the parent's `demo/RUN-LOG.md` and used on B04, B07, B08:

```
./art todo demo/example-reel                        # baseline table (B04)
./art todo demo/example-reel --method manim --open  # agent-lane filter (B07)
./art todo demo/empty-reel                          # failure case, exit 1 (B08)
```

No network calls. No API keys. No spending. Kokoro TTS + local Remotion +
local `todo.py` — the free path throughout.

## Short-specific outputs

- No endcard (`--no-endcard`) — Short ends on `ClaudeTitleOutro916` (B11).
- No outro rewrite (`--no-outro-rewrite`) — the parent outro's four-second
  title-restate holds.
- No captions burned in (contract requirement).
