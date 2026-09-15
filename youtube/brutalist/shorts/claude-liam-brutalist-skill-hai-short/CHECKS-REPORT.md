# CHECKS-REPORT.md — The hai Skill (Short)

Run id: `6b0a5edfa1ee4bd882707ab0e486cdb5`
Supervisor source SHA-256: `81e4ae65bd6363f318dd85d1564dd289c032a8fc988329ded807a8e872e7e12e`
Feedback SHA-256: `6b7b9c7454a60f145d6970b622d74842a5f8184647f32e564038495c22ecd0f5`
Parent master SHA-256: `7a92bdb465492063ced20ba2a4091ad7ce5b0de20f144a187ab3cbc9d8527a31`
Final Short SHA-256: `d11065ee700115b94ba99bf99316202fd30ea6d7836f64a618e6edd9b6ab4a8a`
Final beat_sheet.json SHA-256: `e41b7001bbb4fae74a4d5f0accce20bbd3c87687b5a4d8f71ab4d15a094f44ad`

## Cut plan

Whole-beat cut. Kept: `B00, B01, B03, B04, B05, B08, B09, B11` (8 beats).
Dropped: `B02, B06, B07, B10` (4 beats). No narration rewrite. No audio
regeneration. No re-render — every kept beat's 2160×3840 media and mp3 was
copied from the parent's `vertical/` folder as an independent file. See
`CUT-PLAN.json` for rationale per drop.

## Command trail

```
python3 runtime/scripts/shorts.py \
  /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/youtube/brutalist/claude-liam-brutalist-skill-hai/vertical \
  --output-dir /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/youtube/brutalist/shorts/claude-liam-brutalist-skill-hai-short \
  --slug claude-liam-brutalist-skill-hai-short \
  --drop B02 B06 B07 B10 \
  --no-endcard \
  --no-outro-rewrite
# → parent reel: 12 beats · 280.1s
# → 8 beats · ~166.4s (2:46.4) OK
# → dropped: B02, B06, B07, B10 · ends on the last beat (no endcard)
# → 8 kept beats reused unchanged from parent's native portrait media/*.mp4

python3 runtime/scripts/compile.py \
  /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/youtube/brutalist/shorts/claude-liam-brutalist-skill-hai-short \
  --height 3840 \
  --out /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/youtube/brutalist/shorts/claude-liam-brutalist-skill-hai-short/exports/short
# → wrote exports/short/claude-liam-brutalist-skill-hai-short.mp4 (166.4s)
# → slots: 8/8 filled — every beat = VIDEO
```

## Duration gate (strictly < 180.0 s)

```
ffprobe -show_entries format=duration → 166.375000 s
ffprobe -select_streams v:0 → 2160×3840, 24 fps, duration 166.375000 s
ffprobe -select_streams a:0 → aac, 48000 Hz, stereo, duration 166.375000 s
```

Container 166.375 s < 180.0 s ✓ (headroom 13.625 s)
Video 166.375 s < 180.0 s ✓
Audio 166.375 s < 180.0 s ✓

## Portrait shape gate (2160×3840)

Every source clip and the final export were probed:

```
media/B00.mp4  2160×3840  15.233s
media/B01.mp4  2160×3840  16.067s
media/B03.mp4  2160×3840  23.533s
media/B04.mp4  2160×3840  27.167s
media/B05.mp4  2160×3840  21.033s
media/B08.mp4  2160×3840  34.467s
media/B09.mp4  2160×3840  25.666s
media/B11.mp4  2160×3840   3.200s
exports/short/claude-liam-brutalist-skill-hai-short.mp4  2160×3840  166.375s
```

Sum of kept-beat durations = 166.366 s (matches the compiler's 166.4 s summary
and the container/video/audio duration within ffmpeg rounding).

## Audio gate

`ffmpeg volumedetect` on the final export:

```
Duration: 00:02:46.38
mean_volume: -27.1 dB
max_volume:  -3.3 dB
```

Non-silent, no clipping, no per-beat silence.

## Visual review evidence

- `_qc/contact-2fps.png` — 2 frames/second contact sheet across the full 166 s
  timeline. Progression visible: cold-open composer (Claude UI, cream/ink,
  terracotta send) → hesitant-writer BLUF → SkillTeardownPipeline916 →
  Mechanism Act 1 → Mechanism Act 2 → Falsifiability Act 5 → Verdict
  artifact → ClaudeTitleOutro916.
- `_qc/beat-frames/` — 24 beat-relative frames at 15%/50%/85% of each kept
  beat. Each was inspected in-tool. Findings:
  - B00 (15/50/85): cold open lands "Hallo, Liam", the paste-ready ask, and
    the three-line output. `@HumanitariansAI` folder chip is inside the safe
    area. No `channel_title` compile overlay (deliberately omitted — see the
    parent build's note; `feedback_channel_title_portrait_bleed`).
  - B01 (15/50/85): hesitant-writer serif type fills the safe area at portrait
    scale; the terminal state shows "The hai skill / forks a / source reel /
    The source stays intact." — the "reformats" → "forks" flip has landed.
  - B03 (15/50/85): SkillTeardownPipeline916 with six phase nodes, "CLI
    EXERCISE" highlighted terracotta, INPUT/OUTPUT bars legible.
  - B04, B05, B08 (15/50/85): SkillTeardownMechanism916 — eyebrow, heading,
    body, quote, verdict pill, sparkLine — all rendered with no clipping,
    no bleed past safe.b. Terracotta pill uses positive/negative variants
    consistently.
  - B09 (15/50/85): ClaudeVerdictArtifact916 — six numbered lines with
    terracotta numbers, "The hai Skill" chip and "A fork. Not a re-skin."
    heading. All six lines fit inside the artifact card.
  - B11 (15/50/85): ClaudeTitleOutro916 — "The hai Skill." with terracotta
    period, `@NikBearBrown` handle underneath (OUTRO-LOCK compliance).

No burned-in captions detected. No landscape center-crop artifacts (native
portrait source throughout). No stale review label overlay (compile ran
without `--review`).

## Warnings recorded (non-blockers)

- `motion histogram: reveal:5 type-on:2 hold:1` — 62% reveal exceeds the
  ~40% pantry cap. This is inherited from the parent's design; the Short
  cannot fix it without authoring new visual language, which the cut-first
  brief forbids for whole-beat cuts.
- `SKIN LINT: B00: palette=claude but cold open is 'ClaudeComposerAsk916'`
  and `B11: outro is 'ClaudeTitleOutro916'` — expected; these are the
  portrait-companion variants that Root.tsx already registers. The linter is
  reading a `claude` palette + `*916` pattern name as a mismatch, but the
  916 patterns are the correct portrait renders on the Claude palette. Same
  warning shipped in the parent build.

## Preserved paperwork

- `BUILD-PROMPT.md`, `BRIEF.md`, `FEEDBACK.md`, `SOURCE-SNAPSHOT.json` — the
  supervisor's inputs, untouched.
- `beat_sheet.json` — 8 kept beats, metadata updated (`kind=short`,
  `aspect_ratio=9:16`, `slug=claude-liam-brutalist-skill-hai-short`,
  `derived_from=claude-liam-brutalist-skill-hai-vertical`).
- `CUT-PLAN.json`, `SCRIPT.md`, `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`,
  `SOURCES.md` — regenerated for the retained cut.

## Conclusion

Every current gate passes: duration strictly under 180.0 s on all three
tracks (container, video, audio); native portrait 2160×3840; audio audible
with no clipping; on-brand Claude palette; @NikBearBrown OUTRO-LOCK handle
present; Liam sign-off intact; no captions; no invented approvals; no
network. The Short is ready for Bear's viewing/editing. Publish is a
separate authorized workflow.
