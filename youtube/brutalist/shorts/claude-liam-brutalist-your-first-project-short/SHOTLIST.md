# SHOTLIST.md — Your First Brutalist Project (Short, 9:16)

Seven beats retained from the parent portrait companion (12 → 7). Native 2160 × 3840. Kokoro `am_onyx`. `@HumanitariansAI`. No burned-in captions. Every retained beat's media and audio was copied unchanged from the parent; nothing was re-rendered or re-cropped.

| # | Beat | Act | Pattern (portrait) | What appears on screen | Duration (s) |
|---|---|---|---|---|---|
| 1 | B00 | COLD OPEN | `ClaudeComposerAsk916` | Claude composer with the first-project ask; folder chip `@HumanitariansAI`; four-line answer resolves (reads skill → drafts beat sheet → generates Kokoro am_onyx → renders + compiles). Liam introduces himself. | 8.54 |
| 2 | B01 | BLUF | `BrutalistHesitantWriter916` | Six stacked serif lines type on: "Your first / Brutalist / project / is a demo / Evidence in / a short film." The word `demo` is overwritten in terracotta by `claim`. | 12.50 |
| 3 | B03 | ASK | `ClaudeComposerAsk916` | Composer with the specific first-project ask ("use ai-explainer to make a 60s reel on how ribosomes read mRNA. 12 beats, am_onyx, review cut only."). Three-line output resolves. | 9.83 |
| 4 | B04 | WHAT CLAUDE READS | `ClaudeVerdictArtifact916` | Verdict card, heading "Seven files. One review cut." Seven terracotta-numbered lines: reads SKILL.md → drafts beat_sheet.json → generates mp3/beat-*.mp3 → renders media/*.mp4 → compiles review-cut.mp4 at 4K → writes CHECKS-REPORT.md and _qc/ → stops. | 13.58 |
| 5 | B05 | PREVIEW | `ClaudeVerdictArtifact916` | Verdict card titled `review-cut.mp4`, heading "The pipeline finished. Now you judge it." Six numbered lines including the honest limitation ("not a Short, not a published master, a receipt"; "human review is a separate step — you watch it"). | 12.92 |
| 6 | B10 | YOUR TURN | `ClaudeComposerAsk916` | Composer, greeting "Your Turn". Paste-ready prompt with `[my tiny question]` placeholder. Output lines contrast GOOD ("one question, length, hard stop") vs BAD ("'make me a video' with no shape") and remind: watch the review cut — request ONE revision. | 13.29 |
| 7 | B11 | OUTRO | `ClaudeTitleOutroHAI916` | Dark polarity poster: "Your First Brutalist Project." (terracotta period), `@HumanitariansAI`, "BRUTALIST — 03" sub-mark. Liam signs off in narration. | 5.08 |

**Total planned duration:** 75.75 s (1:15.75). **Final container / video / audio measured:** each 75.750 s. Well under the 180 s Short cap.

## Type / ratio / brand guarantees

- **All beats native at 2160 × 3840** — no cropping, no upscaling. `ffprobe` on each `media/<BID>.mp4` reports `2160,3840`. The compile receipt in `exports/short/*.verified.json` lists per-input SHA-256s.
- **One terracotta moment per beat** — send button (B00, B03, B10), the correction sweep (B01), the numeral column (B04, B05), the final period (B11).
- **No captions / subtitle track / burned-in transcript.** Only on-screen text is prompts, artifact lines and the title.
- **Corner brand bug:** `@HumanitariansAI` folder chip in every composer beat; B11 carries the wordmark full-size.

## What was dropped from the parent (and why)

| Beat | Dropped act | Why cut |
|---|---|---|
| B02 | FRAMEWORK — beat_sheet.json anatomy | Repository anatomy belongs in the 16:9 long; a Short does not need the schema on screen. |
| B06 | ONE REVISION — revision ask | A second worked example. The first ask in B03 covers "what does the skill accept". |
| B07 | REBUILD — diff on disk | Long-form code walkthrough; the receipt message stands without it. |
| B08 | TWO RATIOS — 9:16 vs 16:9 | Format discipline for fellows; not the high-level answer to "what does this skill do". |
| B09 | SUBMISSION LANES — GitHub vs Drive | Handoff plumbing; the Short's honest limitation is already carried by B05 (receipt ≠ publication). |

Nothing else was altered. The parent portrait companion at `youtube/brutalist/claude-liam-brutalist-your-first-project/vertical/` is unchanged.
