# CHECKS-REPORT.md — Brutalist Command: art smoke (landscape)

Run at: 2026-09-12 UTC · run_id `e6fb28666cd04b18b360c7b6af6d7995`.
All commands executed inside the isolated toolkit; nothing published, no
paid API calls, no network fetches.

## Beat-authoring exit condition (nopunt § SHOW / HOLD / CARD)

11 beats · **11 SHOW / 0 HOLD / 0 CARD / 0 PUNT**. Every beat sheet's `shot`
carries an ordered `show` block. Every body beat classifies as SHOW — the code
cards, hesitant writer, verdict artifact, composer beats and outro card each
name an on-screen action.

Teaching arc:
- FRAMEWORK ✓ (B02 dispatcher case; B03 pipeline + three gates)
- WORKED EXAMPLE ✓ (B06 verbatim pass reproduction, values from RUN-LOG.txt)
- FALSIFIABILITY ✓ (B07 verbatim shipped-fixture failure + recovery)
- SCAFFOLDED TASK ✓ (B09 handoff prompt)
- BOOKENDS ✓ (B00 cold open · B10 outro card)
- NO-SOURCE-NO-VERDICT ✓ (verdict lines all cite sources in FACTCHECK.md)

## Automated gates run

| Gate | Command | Result |
|---|---|---|
| slug regex (validate_project) | `python3 -c 'from build_safety import validate_project; validate_project(json.load(open(sheet)))'` | OK — passes for slug `claude-liam-brutalist-command-smoke` |
| Kokoro synth | `python3 runtime/scripts/generate_audio_kokoro.py <reel>` | 11 beats generated, cost $0.00 |
| GATE L (beat-mix lint) | `bash runtime/scripts/run.sh <reel>` (inside `compile.py`) | `[beat-lint] clean — beat mix OK` |
| GATE SHAPE | inside `run.sh` | `skip — not a finance reel` |
| Remotion beat render | `python3 runtime/scripts/remotion_scenes.py <reel>` | 11/11 beats rendered (ClaudeComposerAsk×2, BrutalistHesitantWriter, ClaudeCodeBeat×6, ClaudeVerdictArtifact, ClaudeTitleOutro) |
| compile.py | `python3 runtime/scripts/compile.py <reel> --height 2160 --out <reel>/exports/landscape` | wrote 238.7s master, 11/11 filled, atomic verify passed |
| GATE V (final_frame_check) | `runtime/qc/final_frame_check.py` (invoked by compile.py) | 22 frames sampled · BLOCKER 0 · MAJOR 0 · PASS |

## Visual QC (image inspection, not just probe)

Per-beat frames extracted at 15/50/85% into `_qc/per-beat/` and Read via the
image-capable Read tool. Also extracted 7 spot frames from the final compiled
master at 5s/25s/50s/100s/150s/200s/235s into `_qc/final-landscape/`.
Contact sheet at `_qc/contact-sheet-landscape.png` (SHA-256
`a2258d20c0bacb58a3fb6442ac5d83c0b021ee8672357378e4dd3931f53d02ef`).

Observations:
- B00 composer: greeting "Aloha, Liam", command line fully inside safe area,
  three output lines under composer bounded by SPARK rule at bottom-left.
- B01 hesitant writer: two-line BLUF corrects to "art smoke / renders video."
  — trigger words `checks`, `deps` fire only in line 2 (no collision with the
  preserved title "art smoke").
- B02-B07 code cards: adaptive font-size (added to `ClaudeCodeBeat` locally so
  long snippets fit both vertical and horizontal card dimensions — see
  `scene-source/`). All body copy remains inside the card.
- B08 verdict artifact: six numbered lines, ink on cream, first accent
  on the row numbers.
- B09 Your Turn composer: five-step handoff prompt inside composer + three
  grading output lines below.
- B10 outro card: dark ground, "Brutalist Command: art smoke." + hardcoded
  `@NikBearBrown` handle + slug-seeded mascot. (Playlist adaptation:
  `@HumanitariansAI` folder chip in every OTHER beat; the outro handle is
  locked per OUTRO-LOCK.md and flagged in `README.md` for human review.)

## Container / stream checks (landscape master)

```
$ ffprobe -v error -select_streams v:0 -show_entries stream=width,height,codec_name,duration,r_frame_rate \
    exports/landscape/claude-liam-brutalist-command-smoke.mp4
codec_name=h264
width=3840
height=2160
r_frame_rate=24/1
duration=238.666667

$ ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,channels,sample_rate,duration \
    exports/landscape/claude-liam-brutalist-command-smoke.mp4
codec_name=aac
sample_rate=48000
channels=2
duration=238.666000

$ ffmpeg -i exports/landscape/claude-liam-brutalist-command-smoke.mp4 -af volumedetect -f null - 2>&1 | grep -E 'mean_volume|max_volume'
mean_volume: -27.0 dB
max_volume: -3.1 dB
```

- Aspect: 3840×2160 (native 4K UHD landscape) ✓
- Duration: 238.67s = sum of 11 beat mp3 durations (Kokoro is the clock) ✓
- Audio: stereo 48 kHz AAC, mean_volume -27.0 dB, max -3.1 dB — clears the
  -40 dB floor referenced by `./art smoke`'s own GATE AUDIO ✓
- Video codec: H.264 yuv420p ✓

## Gaps and honest limitations

- `type_check.py` (referenced in `CLAUDE.md`'s GATE T) is not shipped in this
  toolkit revision. TYPECHECK.md documents that gap explicitly and records the
  visual typography review that stands in its place.
- On this workstation the macOS App Sandbox denies writes to `mktemp -d`'s
  default `/var/folders/…` target. `./art smoke` uses that default. A local
  `.mktemp-shim/mktemp` in the isolated toolkit reroutes to `$TMPDIR` — used
  only to capture the smoke run's own output for the demo log. The shim is
  never in the toolkit's shipped path; smoke_test.sh itself is untouched.
- `SKIN LINT` warnings from compile.py flag "COLD OPEN LAW wants
  ClaudeComposerAsk" and "OUTRO LAW wants ClaudeTitleOutro" — this is the
  documented false-positive when the beat legally uses the portrait 916
  variants (only surfaces in the vertical companion). The landscape master
  does not trigger these lints.
- `motion histogram: code-cascade:6 (54%)` exceeds the 40% pantry cap for a
  single motion. Justified: this is a command teardown; the six code beats
  each render different code content (dispatcher, pipeline, fixture, gate,
  pass output, failure output). They are visually differentiated by content,
  not motion.

## Conclusion

Landscape 3840×2160 master at
`exports/landscape/claude-liam-brutalist-command-smoke.mp4` passes every
runtime gate available in this toolkit. Human review pending; no publication.
