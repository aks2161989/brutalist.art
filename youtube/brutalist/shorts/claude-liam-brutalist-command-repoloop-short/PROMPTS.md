# PROMPTS — Brutalist Command: repoloop.sh — Short

Registered scenes only; no LLM-generated visuals; no Higgsfield calls; no
image prompts. No new authoring prompts were sent for this Short: every
kept beat's `props` and `code` are inherited unchanged from the parent
vertical reel's beat sheet.

## Derivative build steps (this Short)

```bash
python3 runtime/scripts/shorts.py \
    youtube/brutalist/claude-liam-brutalist-command-repoloop/vertical \
    --output-dir youtube/brutalist/shorts/claude-liam-brutalist-command-repoloop-short \
    --slug claude-liam-brutalist-command-repoloop-short \
    --drop B02 B03 B04 B06 B07 B08 \
    --no-endcard --no-outro-rewrite

python3 runtime/scripts/compile.py \
    youtube/brutalist/shorts/claude-liam-brutalist-command-repoloop-short \
    --height 3840 \
    --out youtube/brutalist/shorts/claude-liam-brutalist-command-repoloop-short/exports/short
```

`shorts.py` copied each kept beat's native 2160×3840 mp4 and per-beat mp3
into this reel's `media/` and `mp3/` directories as independent files
(no symlinks, no hardlinks). The parent reel is untouched.

## Kept beat props (inherited verbatim from the parent vertical beat sheet)

### B00 — ClaudeComposerAsk916
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

### B01 — BrutalistHesitantWriter916
```json
{
  "text": "repoloop.sh\nis not a\nrender loop.\nIt spawns\nfellows.",
  "triggerWords": "fellows",
  "replacementWords": "workers",
  "seed": "repoloop-b01-vertical-v3",
  "face": "serif",
  "fontSize": 155,
  "lineSpacing": 2.2,
  "align": "center",
  "charMs": 16,
  "jitter": 6,
  "mistakeRate": 0,
  "hesitateWithin": 0,
  "hesitateBetween": 0
}
```
- Single-token trigger `fellows` → `workers`; no trailing punctuation, no
  collision with the preserved prefix `repoloop.sh / is not a / render loop.`
  (memory: hesitant-writer triggerWords match FIRST occurrence).
- Portrait-tuned per feedback_brutalist_hesitant_writer_portrait_scale_patch
  memory: `fontSize 155 + lineSpacing 2.2` fills the SAFE916 area without
  bleeding past its top/bottom.
- Final corrected sentence renders as `repoloop.sh is not a render loop. It
  spawns workers.` — coherent standalone claim per §Beat 2 rendering rules.

### B05 — ClaudeCodeBeat916
Verbatim abridged excerpt of `./repoloop.sh --dry` output; identical to
`beats[5].shot.remotion.props` in the parent vertical `beat_sheet.json`.

### B09 — ClaudeVerdictArtifact916
Six-line whole-surface artifact; identical to `beats[9].shot.remotion.props`
in the parent vertical `beat_sheet.json`. This one beat carries the
`verify_film` fail-closed refusal as the Short's essential caveat.

### B10 — ClaudeComposerAsk916 (Your Turn)
The `command` prop IS the viewer's paste-ready prompt and is read aloud
verbatim in the narration (HANDOFF LAW). Explicit no-go verbs
(`--once/--forever/--start/--stop`) are named in the prompt so the viewer's
Claude session cannot accidentally start the loop.

### B11 — ClaudeTitleOutro916
```json
{
  "title": "Brutalist Command: repoloop.sh.",
  "slug": "claude-liam-brutalist-command-repoloop"
}
```
Handle hardcoded `@NikBearBrown` inside the component per OUTRO-LOCK.md.
Mascot is slug-seeded → deterministic per render. This Short targets the
HAI channel; the mismatch is flagged in README.md for Bear's review.

## What was NOT prompted for this Short

- No image generation of any kind.
- No audio regeneration: every kept beat's mp3 was copied bit-identical
  from the parent vertical reel (`--no-outro-rewrite`, no Kokoro invocation).
- No Remotion re-render: every kept beat's mp4 was copied bit-identical
  from the parent vertical reel (all six kept beats already had native
  2160×3840 renders under `<pattern>916` compositions).
- No web searches, no MCP servers, no paid API calls.
- No endcard PNG or endcard mp3 (`--no-endcard`); the Short ends on B11's
  locked outro card.
