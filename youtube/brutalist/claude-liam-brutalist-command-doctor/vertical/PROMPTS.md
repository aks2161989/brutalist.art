# PROMPTS — Brutalist Command: art doctor

The reel uses no generative image / video prompts. Every beat is a
Remotion scene with props read off `beat_sheet.json`. Kokoro TTS is
deterministic given the same voice + text.

## Kokoro TTS

- Engine: `kokoro` (local ONNX, free).
- Voice: `am_onyx` for every beat.
- Model: `runtime/models/kokoro/kokoro-v1.0.onnx` +
  `voices-v1.0.bin` (symlinked into the isolated toolkit).
- No text substitutions; narration lines are the ground truth.

## Remotion scene props (deterministic given props)

| Beat | Component | Key props |
|---|---|---|
| B00 | ClaudeComposerAsk | `greeting: "Jambo, Liam"`, `folderLabel: "@HumanitariansAI"`, ask + runningText + 3 output lines |
| B01 | BrutalistHesitantWriter | `seed: "doctor-b01"`, `text: "art doctor\ninstalls deps."`, `triggerWords: "installs, deps"`, `replacementWords: "verifies, live"`, `fontSize: 240`, `lineSpacing: 2.6` |
| B02 | ClaudeCodeBeat | title `art:96-99 — one branch, no aliases`, code = dispatcher case; spark "One case. No aliases. One script." |
| B03 | ClaudeCodeBeat | title `art doctor — two modes, one table`, code = FEATURES array + surface; spark "Two modes. One table. Seven features." |
| B04 | ClaudeCodeBeat | title `$ ./art doctor    (verbatim)`, code = verbatim green table; spark "Seven rows green. Cost $0.00. Exit 0." |
| B05 | ClaudeCodeBeat | title `setup:117-140 — check() and dynamic OK_<id>/MISS_<id>`, code = check() body + two example rows; spark "Bash 3.2 safe. OK_id / MISS_id via eval." |
| B06 | ClaudeCodeBeat | title `live verification, not receipts`, code = kokoro_synth row + smoke summary + top-of-file rationale; spark "Kokoro must actually speak. Silence fails." |
| B07 | ClaudeCodeBeat | title `the aggregation loop — setup:156-172`, code = loop body; spark "13 atomic checks → 7 features. One red → exit 1." |
| B08 | ClaudeCodeBeat | title `recovery   (verbatim; one file hidden, one gate refuses)`, code = 3-section verbatim from RUN-LOG.txt; spark "One file missing. Row red. Exit 1. Fix printed." |
| B09 | ClaudeVerdictArtifact | 6-line surface recap; heading "art doctor — the whole surface, in the order you use it" |
| B10 | ClaudeComposerAsk | `greeting: "Your Turn"`, paste-ready prompt reading art doctor output without installing |
| B11 | ClaudeTitleOutro | title `Brutalist Command: art doctor.`, `slug: claude-liam-brutalist-command-doctor` — mascot + polarity + jingle seeded from slug per `OUTRO-LOCK.md`. |

## "Your Turn" prompt (B10, viewer-facing — Liam reads verbatim)

> From my brutalist.art toolkit root: (1) run `./art doctor` and save the whole
> stdout+stderr to `/tmp/doctor.txt`. (2) Do NOT install anything. (3) For every
> row that says `❌ blocked`, write one line naming the atomic check ID that
> failed (the id passed to `check()` in `setup`) and quoting the exact fix hint
> that printed beneath it. (4) If every row is `✅ ready`, tell me the exit code
> and quote the one sentence the script prints under the table about what green
> does NOT prove. (5) Tell me whether you were tempted to run
> `./art doctor --install`, and why you did not.

## What's NOT here

- No text-to-image prompts (no Higgsfield, no Midjourney, no DALL·E).
- No AI-generated stills.
- No sponsored inserts, no ads, no upload, no third-party asset.
