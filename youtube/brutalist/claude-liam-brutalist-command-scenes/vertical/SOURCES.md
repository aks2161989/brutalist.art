# Sources — Brutalist Command: art scenes

## Primary sources under test (this invocation)

| Repo-relative path | SHA-256 (this run) |
|---|---|
| `art` | `9bb77a7c84701d23ab6e73f0a4f48592f17748ffad2c7114b62687bb7f97d0e9` |
| `runtime/scripts/scene_search.py` | `8ec4ece59d47d2a9dba83821aa88882a8a8c87612ffa28d1bb4148288b15c079` |

`episode.source_sha256` for the invocation: `4759b441d3d6c9faee523870e99fa26482fb28ecaa7cbf9a19b43c1680651a56`.

Both files were read in full before the beat sheet was authored. Every claim on
screen or in narration is traceable to a line in one of the two files. The
verbatim demo output that populates the WORKED_EXAMPLE beats (B05-B07) and the
FALSIFIABILITY beat (B08) was captured against these exact hashes on
2026-09-09.

## Doctrine references consulted

| Path | SHA-256 (from SOURCE-SNAPSHOT.json) |
|---|---|
| `skills/make/ai-explainer/SKILL.md` | `a7421d4d861b44a983a31e9fcd7451cd32312a139366e74acc2123dfdefbd3c0` |
| `skills/make/nopunt/SKILL.md` | `ef38a574fe22f2fca1dfa0774bc51681252776f8ef2bd6f2b1e52d6478cab505` |
| `runtime/prose/teardown/PROSE.md` | `6accc1a576ca9b52713abd31507f5deece6dc2612ca90967b25b661e59111786` |
| `docs/PIPELINE-SAFETY.md` | `4619f0d4702317d654cd6498cadc8c277691e4c7565920ef851dbb628aa6298d` |
| `docs/FELLOWS-SUBMISSION.md` | `7825c728f040b0f7a49bbd950a5a2bef70c8a59ff2fbe0538716c8d3381f5223` |
| `CLAUDE-BRAND.md`, `OUTRO-LOCK.md`, `CLAUDE-CODE-VISUAL-QC-CHECK.md` | consulted from toolkit root |

The public repository these files live in (for setup guidance in the reel):
<https://github.com/nikbearbrown/brutalist.art>.

## Read-only example leads (reference DATA, not this run's output)

Both example beat sheets in `example-sources.json` were read in full for staging
and framing cues. Their content, human signatures, and Drive URLs remain the
property of their original authors; nothing from them was republished.

| Example | Original repo-relative path | SHA-256 |
|---|---|---|
| Your Weekly Video, Handled. | `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` | `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22` |
| This Week, Gordy. | `yatra-r/2026-09-03-this-week-gordy/beat_sheet.json` | `7e3ea1f61c421e605e583be9b2a7b5f554aa8cadfb6e14dabaee66f471856083` |

What was ported over from them: the general staging of the composer cold open,
the placement of a hesitant-writer BLUF in beat 2, and the shape of the verdict
artifact. No text, name, signature, or Drive URL from either example appears in
this episode.

## Local demo capture

- `demo/RUN-LOG.txt` — every command shown on screen was run against the
  isolated toolkit at build time. The `demo/` folder is the receipt.
- The `TEMPLATE-MISSES.md` ledger row shown in B08 was produced by an actual
  `--reel youtube/my-reel` miss during the run; the ledger file itself lives at
  `toolkit/TEMPLATE-MISSES.md` (auto-appended by `scene_search.py`).

## Voice, media and audio

- Narration: Kokoro `am_onyx` (Liam, in for Bear), generated locally via
  `runtime/scripts/generate_audio_kokoro.py`. No paid TTS.
- Rendering: Remotion inside the isolated toolkit's Node/Chromium runtime,
  driven by `runtime/scripts/remotion_scenes.py`. No paid renderer.
- The wrap script for the sandbox's headless-shell workaround
  (`ART_CHROME=/tmp/claude/chrome-wrap.sh`) exists only to let Remotion spawn a
  browser inside the isolated environment; it is not a bypass of any check.
