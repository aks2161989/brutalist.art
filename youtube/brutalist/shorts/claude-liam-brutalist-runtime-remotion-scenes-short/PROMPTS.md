# PROMPTS — Brutalist Utility: remotion_scenes.py

## B10 Handoff prompt (Your Turn)

```
I have a reel at ~/my-reel/ with some beats already filled and some slate.
Run remotion_scenes.py to fill only the empty beats, then show me the
consumer index to confirm the pattern was logged.

Here is what I want to know:
1. What exact command do I run?
2. What does the output tell me for each beat (SLATE vs filled)?
3. Where is consumers.json and what does a logged entry look like?
4. What flags do I add to re-render just one beat if it fails?
```

### What the viewer should check in Claude's answer

- The command: `python3 runtime/scripts/remotion_scenes.py ~/my-reel/`
- Per-beat status lines showing SLATE or "filled already (skip)"
- The consumers.json path: `runtime/remotion/_bench/consumers.json`
- An entry like `{"ClaudeComposerAsk": [{"video": "my-reel", "beat": "B00"}]}`
- Re-render flag: `--force --only B00` for a single failed beat

### Why this prompt is interesting

It threads three outputs together — the status lines, the consumer index, and
the re-render path — which makes the viewer verify they understand all three
parts of the script's contract, not just that it ran.
