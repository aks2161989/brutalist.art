# PROMPTS — Brutalist Command: art todo

## Kokoro (voice) prompts

Every beat runs through `runtime/scripts/generate_audio_kokoro.py`. No API. No
paid voice. Voice: `am_onyx` per beat and in metadata. Text is the exact
`narration_text` from `beat_sheet.json`.

## Composer / Ask beat prompts (ASK → RESULT — what types on screen)

### B00 — cold open ask (result lines pre-answered)

```
$ art todo my-reel/ --open
```

Result lines (populated in `ClaudeComposerAsk.output`):

- `reads beat_sheet.json — no other input`
- `writes todo.json + STATUS.md + ToDo.md`
- `--open filter → only beats still needing a clip`

### B10 — Your Turn (the paste-ready Claude Code prompt)

```
Run `./art todo` on this reel folder, then walk the `--method remotion --open`
list and render each one via `./art run <reel>`. When only human-owed beats are
left, stop and tell me which slot filenames still need media dropped in, and
which archive I should try first for each.
```

Look-for rubric lines (three, staggered as `output`):

- grade it: does it name the exact slot filenames (`media/<BID>.mp4`)?
- grade it: does it stop at the human-owed beats instead of guessing?
- grade it: does it reread the receipt after each render?

## Live demonstration commands (all run local on this workstation)

Captured in `demo/RUN-LOG.md` and used on B04, B07, B08:

```
./art todo demo/example-reel                        # baseline table
./art todo demo/example-reel --method manim --open  # agent-lane filter
./art todo demo/example-reel --json                 # machine-readable output
./art todo demo/empty-reel                          # failure case (exit 1)
```

No network calls. No API keys. No spending. Kokoro TTS + local Remotion +
local `todo.py` — the free path.
