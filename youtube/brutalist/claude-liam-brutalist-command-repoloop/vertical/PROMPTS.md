# PROMPTS — Brutalist Command: repoloop.sh

Registered scenes only; no LLM-generated visuals; no Higgsfield calls; no
image prompts. What follows is the fixed set of authored prompts / props /
demo commands that produced this reel.

## Authoring prompts sent to the reel's Claude session (this build)

The entire session ran under `.repoloop/workspaces/…/toolkit/` sandboxed
per `worker_settings()` in `runtime/scripts/repoloop.py` — the settings
JSON is captured verbatim in `../settings.json` inside the workspace, and
the beat text of B04 quotes the relevant clauses. No user-facing prompts
were emitted; the whole build was steered by the BUILD-PROMPT.md file
that ships with this reel (`REPOLOOP-PROMPT.md` + `THIS INVOCATION` JSON).

## Demo commands (all recorded verbatim in demo/RUN-LOG.txt)

```bash
$ ./repoloop.sh --help
$ ./repoloop.sh --dry
$ ./repoloop.sh --status
$ ./repoloop.sh --shorts-only --dry            # (tail)
$ ./repoloop.sh --only totally-fake-id --dry   # error demo
$ ./repoloop.sh --shorts-only --landscape-only # mutually-exclusive demo
$ ./repoloop.sh --n -1                         # nonnegative-guard demo
```

All commands are read-only. None spawns a worker. None writes to the queue.

## Beat-by-beat scene inputs (what actually reaches Remotion)

### B00 — ClaudeComposerAsk (landscape)
```json
{
  "greeting": "Vanakkam, Liam",
  "topic": "BRUTALIST · COMMAND: REPOLOOP.SH",
  "segment": "repoloop.sh",
  "command": "How do I build the whole Brutalist playlist without babysitting every film? Show me the loop that runs one fresh Claude worker per episode, on repeat.",
  "runningText": "planning the queue…",
  "output": [
    "one fresh Claude subprocess per film, serial",
    "sandboxed writes; ANTHROPIC_* env vars stripped",
    "resumable queue; verify_film() is the fail-closed gate"
  ],
  "folderLabel": "@HumanitariansAI",
  "modelLabel": "Claude",
  "effortLabel": "Sonnet"
}
```

### B01 — BrutalistHesitantWriter (landscape)
```json
{
  "text": "repoloop.sh\nbuilds videos.",
  "triggerWords": "builds, videos",
  "replacementWords": "orchestrates, workers",
  "seed": "repoloop-b01",
  "face": "serif",
  "fontSize": 240,
  "lineSpacing": 2.6,
  "align": "center",
  "charMs": 26,
  "jitter": 18,
  "mistakeRate": 0,
  "hesitateWithin": 0,
  "hesitateBetween": 0
}
```
Author-time verification (see feedback_hesitant_writer_triggers memory):
- `triggerWords` and `replacementWords` are comma-separated single tokens,
  no trailing punctuation, positionally matched.
- Neither `builds` nor `videos` appears in the preserved title/prefix
  `repoloop.sh` (memory: hesitant-writer triggerWords match FIRST
  occurrence, so collisions in the prefix would swap the wrong token).
- Final sentence, after replacement: `repoloop.sh orchestrates workers.` —
  a coherent, standalone claim (per §Beat 2 rendering rules).

### B02..B08 — ClaudeCodeBeat (landscape)
Every beat's `code` prop is a small verbatim (or lightly-abridged VERBATIM)
excerpt from the sources in FACTCHECK.md. No paraphrasing of code lines.
`title` names the source file range or command. `sparkLine` is ≤ 6 words
and states the beat's judgment.

### B09 — ClaudeVerdictArtifact (landscape)
Six-line artifact enumerating repoloop.sh's whole surface in the order a
user touches it. See beat_sheet.json `beats[9].shot.remotion.props`.

### B10 — ClaudeComposerAsk (landscape) — "Your Turn" prompt
The `command` prop IS the viewer's paste-ready prompt. It is also read
aloud verbatim in the narration (HANDOFF LAW). Explicit no-go verbs are
named in the prompt itself so the viewer's Claude session cannot
accidentally start the loop.

### B11 — ClaudeTitleOutro (landscape)
```json
{
  "title": "Brutalist Command: repoloop.sh.",
  "slug": "claude-liam-brutalist-command-repoloop"
}
```
Handle hardcoded `@NikBearBrown` inside the component per OUTRO-LOCK.md.
Mascot is slug-seeded → deterministic per render. This reel targets the
HAI channel; the mismatch is flagged in README.md for Bear's review.

## What was NOT prompted

- No image generation (Manim, higgsfield, dall-e, sora, midjourney, etc.).
- No audio generation other than Kokoro `am_onyx` for narration beats.
- No web searches. Every source line came from files inside the isolated
  workspace toolkit (baseline hashed in `toolkit-baseline.json`).
- No fresh network install. `chrome-headless-shell` was already present
  under `~/node_modules/.remotion/` from a prior session; the wrapper
  script at `$TMPDIR/claude-repoloop-chrome/chrome-wrap.sh` invokes it
  with `--single-process --in-process-gpu` per the chrome-sandbox
  workaround memory. No fresh download attempted.
