# PROMPTS — Brutalist Command: art shorts

No Manim beats. All Remotion beats fill from their zod schemas via
`runtime/scripts/remotion_scenes.py` — the beat sheet's `shot.remotion.props`
is the entire prompt surface. Reproduced here for review.

## B00 — ClaudeComposerAsk (cold open)
```json
{
  "greeting": "Salam, Liam",
  "topic": "BRUTALIST · COMMAND: ART SHORTS",
  "segment": "art shorts",
  "command": "Turn my finished 16:9 reel into its 9:16 sibling. Check the length first, drop whole beats if the cap needs it, rewire every Remotion beat to a portrait composition instead of cropping it, and print the plan before you touch a file.",
  "runningText": "checking cap; planning drops; rewiring…",
  "output": [
    "wraps: python3 runtime/scripts/shorts.py <reel> [--drop --keep --vertical …]",
    "writes: <reel>/short/beat_sheet.json (or vertical/ for --vertical)",
    "editorial law: Short = strictly < 3:00; --vertical drops the cap entirely"
  ],
  "folderLabel": "@HumanitariansAI",
  "modelLabel": "Claude",
  "effortLabel": "Sonnet"
}
```

## B01 — BrutalistHesitantWriter (BLUF)
```json
{
  "text": "art shorts speeds up\nand crops the frame.",
  "triggerWords": "speeds, crops",
  "replacementWords": "drops, rewires",
  "seed": "command-shorts-b01",
  "face": "serif",
  "fontSize": 240,
  "lineSpacing": 2.5,
  "align": "center",
  "charMs": 26,
  "jitter": 18,
  "mistakeRate": 0,
  "hesitateWithin": 0,
  "hesitateBetween": 0
}
```

## B02..B08 — ClaudeCodeBeat props
Each has `title` (filename in the traffic-light bar), `code` (newline-joined
string), and `sparkLine`. Reproduced in the beat_sheet.json under
`beats[i].shot.remotion.props`. Verbatim excerpts are the direct source of the
narration in each beat.

## B09 — ClaudeVerdictArtifact
```json
{
  "artifactTitle": "Verdict",
  "artifactHeading": "art shorts — the whole surface, in the order you use it",
  "artifactLines": [
    "bare invocation — ./art shorts <reel>; wraps python3 runtime/scripts/shorts.py.",
    "cap first — Short = strictly < 3:00 including endcard + encoder rounding.",
    "auto-plan drops — longest unprotected middle beats until the total fits; --keep/--drop override.",
    "protected always — first beat, last beat, INTRO/OUTRO acts, source_reports, 'hero' beats, --keep ids.",
    "ONDA CHECK — every REMOTION beat rewired to <pattern>916; missing composition = BLOCKED.",
    "pantry wins — pantry/<bid>-916.* overrides the auto cut, the rewire and the hand-made -916.",
    "art vertical — same script, --vertical; no cap, no drops, no endcard, no rewritten outro.",
    "render only — no upload, no scheduling; publishing is a separate authorized human workflow."
  ]
}
```

## B10 — ClaudeComposerAsk (Your Turn)
The `command` field is the paste-ready Claude Code prompt Liam reads aloud in
its entirety. Present in `beat_sheet.json` `beats[10].shot.remotion.props.command`.

## B11 — ClaudeTitleOutro
`{ "title": "Brutalist Command: art shorts.", "slug": "claude-liam-brutalist-command-shorts" }`
plus every default the schema stamps in (handle `@NikBearBrown`, byline).
