# PROMPTS — Brutalist Command: art scenes

This reel has no LLM-generated content on screen or in narration. Every visible
line of code and every printed terminal output was captured by running the
actual `./art scenes` script inside the isolated toolkit.

## The single reproducible command sequence

Run from the toolkit root (`.repoloop/workspaces/claude-liam-brutalist-command-scenes/toolkit`):

```bash
./art scenes                                       # bare — prints the doctrine
./art scenes "sankey flow" --top 5 --no-log        # rare word wins
./art scenes "bar chart" --top 5 --no-log          # common terms, id-hit still wins
./art scenes --check ClaudeComposerAsk BarChart NotAScene
./art scenes "the and for with that this"          # all stop words — rejected
./art scenes --undocumented | head -15             # the backfill list
./art scenes "quantum entanglement particle" --no-log
./art scenes --check ClaudeComposerAsk             # via three aliases
./art scene  --check ClaudeComposerAsk
./art scene-search --check ClaudeComposerAsk
./art scenes "yak shaving trombone" --reel youtube/my-reel   # a real miss
```

The complete captured output is in `demo/RUN-LOG.txt`. Every code card in the
film reproduces those lines verbatim (with cosmetic wrapping/truncation only —
never a made-up number).

## Handoff prompt (B10, read aloud verbatim)

The viewer's paste-ready audit script — this is the one prompt this reel puts
into the viewer's hands:

```
From the brutalist.art toolkit root, run:

  ./art scenes;
  ./art scenes "bar chart";
  ./art scenes "sankey flow";
  ./art scenes "three-part funnel" --top 12 --no-log;
  ./art scenes --check ClaudeComposerAsk BarChart FormBCard NotAScene;
  ./art scenes --undocumented | head;
  ./art scenes "purely-made-up-thing" --reel youtube/your-reel.

Then diff ./art scenes "BarChart" against ./art scene "BarChart" and
./art scene-search "BarChart" — all three must be identical. Finally, run
the search on ONE beat you are authoring right now and record the top hit —
or the miss.
```

Expected outcomes (shown as composer output on B10):

- top hits are relevant on common queries (bar chart, funnel)
- rare word beats common word: `sankey flow` finds `FinanceSankey` first
- checks: three names IN SET, `NotAScene` is a punt
- aliases scenes/scene/scene-search return byte-identical output
- one honest miss on the made-up query — appears in `TEMPLATE-MISSES.md`
