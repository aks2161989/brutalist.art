# brutalist

The pared-down Brutalist video toolkit: builders, personas, and shared production
doctrine, with local Kokoro voices (Onyx `am_onyx`, Bella `af_bella`).

**Free by default** — Kokoro, Manim, Remotion, no account required.
**Optional:** a Higgsfield CLI login (`higgsfield auth login`) unlocks AI video
beats. Absent = the free path (Ken Burns stills) runs silently. No ElevenLabs,
ever.

**Read [`HOW-TO.md`](HOW-TO.md)** — what Brutalist is, install, the three
core builders, and the worked examples. `CLAUDE.md` has the session rules for
agents.

```bash
./setup --install     # deps + Remotion node modules + the Kokoro model (~340MB, auto-downloaded)
./art --list          # the skills
./art keys            # check optional Higgsfield login + SI key
```

## Builders

| Skill | What it makes |
|---|---|
| `ai-explainer` | Claude-branded explainer reel — the tight cut |
| `cli-explainer` | Prompt → real code → moving output (the build reel) |
| [`godot-waikthrough`](skills/make/godot-waikthrough/SKILL.md) | Play a Godot game, cover its implemented features with Liam riffs, render in 4K; optional `walker` Claude/GDD bookends |
| [`godot-gamedev`](skills/make/godot-gamedev/SKILL.md) | Detailed game-development film: actual code, scenes, resources, assets and art in source-backed Godot teaching views; optional `walker` bookends |
| [`godot-gdd`](skills/make/godot-gdd/SKILL.md) | Explain a complete GDD using existing game evidence; separate proposals, implementation, tests and human decisions; optional `walker` bookends |
| `deep-explainer` | 5–10 min documentary episode with vox pantry beats |
| `anthropics` | Reads an Anthropic artifact (repo/paper/content) against its own claims; practitioner-report register |
| `fashionista` | AI fashion-call experiment — sports-announcer call with stated confidence + correction ask |
| `fellows` | Wraps a HAI fellow's video report in Claude bookends for @HumanitariansAI |
| `finance` | Templatized SEC EDGAR filings reel — 11 beats, 5 charts, fully deterministic, two audits |
| `guests` | Wraps a board-member or invited-speaker video in Claude bookends for @HumanitariansAI |

## Personas

| Skill | Register | Voice |
|---|---|---|
| `nbb` | Teardown — take it apart, judge the design | Kokoro `am_onyx` |
| `hai` | Plain — simple and direct; method, when to use it, when NOT to | Kokoro `af_bella` |

## Doctrine (not entry points — inherited by builders)

| Skill | What it governs |
|---|---|
| `explainer` | Parent compositing chassis all builders inherit |
| `your-turn` | The closing three-beat standard |
| `duration-planner` | Duration is an output of the content, never a target |
| `nopunt` | Maps every animatable beat-type to the right Brutalist primitive |
| `screen-clean` | Prepares screen recordings (Zoom/Teams/Meet) for use as a reel beat |
| [`riff`](skills/make/riff/SKILL.md) | Inspect/render an artifact; explain the visible event, mechanism, trade-offs, and educational use |

### Game walkthroughs

Ask your agent: `godot-waikthrough walker /path/to/walker-jumpman` (or use the
alias `godot-walkthrough`). Without `walker`, it opens on gameplay; with it, the
Claude prompt asks Walker to convert the game's GDD, and beat two summarizes
what was actually built. Both use real gameplay, Liam's on-screen riffs, and the
regular outro—not a game-themed sound/voice ending. The skill renders locally
for review; it does not publish.

`./art godot-waikthrough --help` and `./art riff --help` show the agent workflows.
`./art godot-waikthrough --check /path/to/reel` runs the read-only coverage gate.
As with the other builders, invoking `./art <skill>` alone shows the skill to
follow; it is not an autonomous film-render command.

Note: the Kokoro voice model is not in this repo (GitHub's 100MB file limit)
— `./setup --install` fetches it once from the kokoro-onnx releases.

### Godot development films

Ask your agent: `godot-gamedev walker /path/to/walker-jumpman`. This is the
component-by-component companion to the gameplay walkthrough: code, saved and
runtime scenes, resources, assets, procedural art, tests, and export status.
The `walker` modifier adds the Claude/GDD opening, built-result summary, verdict,
Your Turn, and regular stock-only outro. Without it, open directly on the game.

`./art godot-gamedev --help` shows the workflow. The read-only source gate is:

```bash
./art godot-gamedev --check /path/to/reel --game /path/to/project-containing-project.godot
```

The reusable `GodotDevWorkbench` scene has code, tree, asset, and trace views,
including native portrait layout. Its editor chrome is explicitly reconstructed;
source excerpts, runtime observations and art previews must come from the actual
game. It does not modify game code, pretend to export a game, or publish a film.
