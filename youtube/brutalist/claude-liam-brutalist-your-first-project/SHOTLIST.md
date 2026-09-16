# SHOTLIST.md — Your First Brutalist Project (landscape 16:9)

Twelve beats. Native 3840 × 2160. Kokoro `am_onyx`. `@HumanitariansAI`.

| # | Act | Pattern | What appears on screen | Duration (s) |
|---|---|---|---|---|
| B00 | COLD OPEN | `ClaudeComposerAsk` | Claude composer with first-project ask; four-line plan below (reads SKILL.md → drafts beat sheet → generates audio → renders/compiles). Introduces Liam. | 10.15 |
| B01 | BLUF (BrutalistHesitantWriter LAW) | `BrutalistHesitantWriter` | Serif text types: "Your first Brutalist project is a demo. Evidence, in a one-minute film." Then "demo" is deleted (terracotta) and typed back as "claim". `lead_silence_s: 0.8` in metadata. | 11.41 |
| B02 | FRAMEWORK | `ClaudeCodeBeat` | White code card, cream page. A JSON fragment showing what one beat_sheet.json record looks like (beat_id, act, narration_text, engine, voice, shot.remotion.pattern). Spark line: "The video IS the file. One beat, one record." | 12.71 |
| B03 | ASK 1 | `ClaudeComposerAsk` | Composer with a concrete first-project ask on ribosomes reading mRNA. Greeting: "The ask,". Output shows target beat count, voice, hard stop at review cut. | 10.07 |
| B04 | WHAT CLAUDE READS | `ClaudeVerdictArtifact` | Artifact card, 7 numbered lines describing the concrete files/actions the pipeline performs. Heading: "Seven files. One review cut." | 13.50 |
| B05 | PREVIEW | `ClaudeVerdictArtifact` | Artifact card titled `review-cut.mp4`. 4 numbered lines about what the file actually is; heading: "The pipeline finished. Now you judge it." | 12.93 |
| B06 | REVISION | `ClaudeComposerAsk` | Composer with a one-beat revision ask. Greeting: "The change,". Output shows which files are re-touched (audio, media, clip, review cut). | 12.27 |
| B07 | REBUILD | `ClaudeCodeBeat` | Code card titled "diff — after the one-beat revision" — 5 modified files listed, comment: "Audio is the clock; a beat is a slot." Spark line: "One beat changed. Nothing else." | 13.37 |
| B08 | TWO RATIOS | `ClaudeVerdictArtifact` | Artifact heading "9:16 is a separate sheet, never a crop." 5 numbered lines: dimensions and the `art vertical` role (plans, not reframes). | 15.67 |
| B09 | SUBMISSION LANES | `ClaudeVerdictArtifact` | Artifact heading "Source to GitHub. Video to Drive." 5 lines: what goes where, and the receipt≠publication rule. | 14.77 |
| B10 | YOUR TURN (HANDOFF LAW) | `ClaudeComposerAsk` | Composer with the paste-ready first-project prompt, `greeting: "Your Turn"`. Output: "GOOD: one question, a length, a hard stop / BAD: 'make me a video' / watch the review cut — request ONE revision." | 13.30 |
| B11 | OUTRO (title restate) | `ClaudeTitleOutroHAI` | Poster-style serif title: "Your First Brutalist Project." (terracotta period), `@HumanitariansAI` beneath, playlist sub-mark. Narration signs off: "Liam, in for Bear — for Humanitarians AI." | 5.07 |

Total measured audio: ~145 s (2:25). Compile conforms visuals to these durations.

## Type / ratio / brand guarantees per beat

- **All beats native at 3840 × 2160** — no cropping, no upscaling. Verified via
  `ffprobe` on each `media/<BID>.mp4` (see `_qc/probe.json`).
- **One terracotta moment per beat** — the composer send button, one accent
  on a heading numeral, the code card's active traffic-light dot, or the
  final period in the outro. Two orange things per beat is a defect.
- **No captions / subtitle track / burned-in transcript.** Only text is
  instructional labels, prompts, and short code fragments — the material
  the beat is teaching.
- **Corner brand bug:** the folder chip `@HumanitariansAI` sits inside the
  composer in B00, B03, B06, B10. B11 carries the wordmark full-size.
