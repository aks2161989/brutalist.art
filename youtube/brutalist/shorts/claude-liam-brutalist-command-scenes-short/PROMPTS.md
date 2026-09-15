# PROMPTS — Brutalist Command: art scenes — Short

This Short has no LLM-generated content on screen or in narration. Every
visible code line and every printed terminal output was captured by running
the actual `./art scenes` script inside the isolated toolkit — this Short
reuses those captures unchanged from the parent's vertical companion.

## Retained on-screen captures (single reproducible sequence)

Run from the toolkit root
(`.repoloop/shorts/workspaces/claude-liam-brutalist-command-scenes-short/toolkit`):

```bash
./art scenes "sankey flow" --top 5 --no-log        # B05: rare word wins → FinanceSankey 8.5
./art scenes "yak shaving trombone" --reel youtube/my-reel   # B08: a real miss
```

The complete captured output is in the parent's `demo/RUN-LOG.txt`
(§2 and §10). The code cards in B05 and B08 reproduce those lines verbatim
(only cosmetic wrapping — never a made-up number).

The Python source shown on B04 (`scene_search.py` `score()` and `weight()`)
is quoted verbatim from `runtime/scripts/scene_search.py`; SHA-256 tracked in
the parent's SOURCES.md as `8ec4ece5…`.

## Handoff

There is no paste-ready "Your Turn" prompt in this Short. The extended
Your Turn exercise lives in the 16:9 long and the full-length vertical
companion (B10 there); Shorts intentionally do not read the full audit
aloud.

## LLM prompts NOT used

- No LLM was used to author or paraphrase the code on screen.
- No LLM was used to generate the "sankey flow" ranking — the score column is
  what the actual ranker printed.
- No LLM was used to author the miss line — the tool wrote the punt message
  itself.

The `hesitant writer` animation in B01 is a Remotion component
(`BrutalistHesitantWriter916`), not a language model — the trigger/replacement
pair (`writes,new` → `finds,existing`) is data on the beat, not generation.
