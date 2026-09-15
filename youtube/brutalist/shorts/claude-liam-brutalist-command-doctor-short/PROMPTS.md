# PROMPTS — Brutalist Command: art doctor — Short

The Short uses no generative image / video prompts. Every kept beat is a
Remotion `*916` scene whose props were rendered by the parent vertical
companion and are reused unchanged. Kokoro TTS is deterministic given the
same voice + text, and no audio was regenerated for this Short.

## Kokoro TTS

- Engine: `kokoro` (local ONNX, free).
- Voice: `am_onyx` for every retained beat.
- Model: `runtime/models/kokoro/kokoro-v1.0.onnx` +
  `voices-v1.0.bin` (symlinked into the isolated toolkit).
- No text substitutions; the retained narration is the parent's ground truth,
  copied byte-for-byte.

## Remotion scene props reused (kept beats only, portrait 1080×1920 canvas)

| Beat | Component | Key props |
|---|---|---|
| B00 | ClaudeComposerAsk916 | `greeting: "Jambo, Liam"`, `folderLabel: "@HumanitariansAI"`, Do-not-install ask + `running ./setup…` + 3 output lines |
| B01 | BrutalistHesitantWriter916 | `seed: "doctor-b01"`, `text: "art doctor\ninstalls deps."`, `triggerWords: "installs, deps"`, `replacementWords: "verifies, live"`, `fontSize: 210`, `lineSpacing: 4.5` (portrait scale patch applied in the isolated toolkit) |
| B03 | ClaudeCodeBeat916 | title `art doctor — two modes, one table`, code = FEATURES array + surface; spark "Two modes. One table. Seven features." |
| B04 | ClaudeCodeBeat916 | title `$ ./art doctor    (verbatim)`, code = verbatim green table; spark "Seven rows green. Cost $0.00. Exit 0." |
| B06 | ClaudeCodeBeat916 | title `live verification, not receipts`, code = kokoro_synth row + smoke summary + top-of-file rationale; spark "Kokoro must actually speak. Silence fails." |
| B08 | ClaudeCodeBeat916 | title `recovery   (verbatim; one file hidden, one gate refuses)`, code = 3-section verbatim from RUN-LOG.txt; spark "One file missing. Row red. Exit 1. Fix printed." |
| B09 | ClaudeVerdictArtifact916 | 6-line surface recap; heading "art doctor — the whole surface, in the order you use it" |
| B11 | ClaudeTitleOutro916 | title `Brutalist Command: art doctor.`, `slug: claude-liam-brutalist-command-doctor` — mascot + polarity + jingle seeded from slug per `OUTRO-LOCK.md`. |

## What's NOT here

- No text-to-image prompts (no Higgsfield, no Midjourney, no DALL·E).
- No AI-generated stills.
- No sponsored inserts, no ads, no upload, no third-party asset.
- The parent film's "Your Turn" composer (B10, 21.7 s) was dropped from
  the Short. Its paste-ready prompt is preserved verbatim in the parent
  reel's `PROMPTS.md` — the 16:9 long is where that exercise belongs.
