# PROMPTS — The explainer Skill

## Composer prompts SEEN ON SCREEN

### B00 — cold-open ASK (what the ask is)

```
What is the `explainer` skill? Read skills/make/explainer/SKILL.md and tell
me what it actually is and what its two hard rules are.
```

Running text: `reading skills/make/explainer/SKILL.md…`

Output lines that land after send:
- it is a compositing PIPELINE, not a style
- two-axis shot system: type × source
- the still must be evidence, not texture

### B09 — YOUR TURN (paste-ready, viewer runs)

```
Run `slate cut` on the following concept: [your one-line topic]. Write a
short script, plan beats, generate Kokoro audio, and produce a watchable
review cut with slates in every human-media slot. Do not run any paid API.
Keep every still under VOX LAW.
```

Running text: `paste this into Claude Code…`

Output rubric lines (what the viewer should check afterwards):
- check: does every body beat have ONE specific job only it can do?
- check: is every planned still evidence — the record the beat proves?
- check: apply the swap test. If any still fails it, cut the still.

Both prompts stay on screen long enough for the viewer to pause and read.
Liam reads B09 aloud verbatim (HANDOFF LAW's read-and-discuss requirement).

## Prompts NOT shown on screen but used to build the reel (internal only)

None of these appear inside the film; recorded here for build reproducibility.

- Author beat sheet — followed the ai-explainer skill-teardown structure
  (cold open · hesitant writer · anatomy · pipeline · three mechanism acts ·
  falsifiability · verdict artifact · your turn · title outro). The five
  design decisions covered in the teardown match what SKILL.md structures its
  own doctrine around.
- Trigger word swap — single-token per BrutalistHesitantWriter contract:
  `style → pipeline`. The corrected sentence stands alone as the reel's
  claim ("The explainer skill is a pipeline. Sources never match. The
  treatment does.").
- Chrome wrapper — created `runtime/scripts/chrome_wrap.sh` to survive the
  Apple App Sandbox Mach-port block on `chrome-headless-shell`. Not a prompt,
  but recorded here so the reproduction path is complete.
