# PROMPTS — Brutalist Utility: build_cli_d3_reels.py — Short

Only one composer beat appears in the Short (B00). The parent's B10 Your-Turn
composer with the paste-ready dry-run prompt was dropped per the shorts
cut-first guidance — a detailed CTA belongs in the 16:9 long.

## B00 — Cold-open ask (`ClaudeComposerAsk916`)

```
I have a folder of D3 sims already built (one HTML each). Wrap every one in
a Claude-skin explainer reel. Unattended, overnight, one config.json in.
```

**RunningText:** `invoking build_cli_d3_reels.py…`
**Output lines** (three, cascading under the composer):
- reads sims[] from config.json — each row: slug · book · html · note
- stamps beat_sheet.json (ClaudeComposerAsk / ClaudeCodeBeat / ClaudeTitleOutro; 10 beats)
- captures the sim → audio → Remotion → compile.py --review; appends one row per sim to the log

**Folder chip:** `@HumanitariansAI` · **Model:** Claude · **Effort:** Sonnet
