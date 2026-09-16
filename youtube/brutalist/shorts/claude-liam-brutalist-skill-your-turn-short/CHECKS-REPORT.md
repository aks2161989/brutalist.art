# CHECKS-REPORT — The your-turn Skill (Short)

Run ID: `bfb6c15f19af454ab8a8e43c589e1cbf` · 2026-09-12

## Context

Source SHA-256 changed since previous Short build (episode.source_sha256
`5ddb70b3a0be6567c05a8cdc88d70794aa59b99341cc8626c2615ae94c7e36e9`). The
parent vertical was re-verified under run_id `1ddecabfca38480996c56171bce09bb7`
with the note "beat content verified accurate to current SKILL.md; renders
preserved (no beat changes required)." All 8 Short media clips and mp3 files
were confirmed byte-identical to the parent vertical — no re-render required.

## 1. Cut plan

Original cut (unchanged from initial build 2026-09-09):

```
python3 runtime/scripts/shorts.py \
  youtube/brutalist/claude-liam-brutalist-skill-your-turn/vertical \
  --output-dir youtube/brutalist/shorts/claude-liam-brutalist-skill-your-turn-short \
  --slug claude-liam-brutalist-skill-your-turn-short \
  --drop B02 B04 B05 B06 B07 B08 \
  --no-endcard --no-outro-rewrite
```

8 retained beats: B00 B01 B03 B09 B10 B11 B12 B13.
All 8 confirmed native 9:16 (2160×3840), byte-copied unchanged from parent.

Media verification (SHA-256 diff vs parent vertical):
- All 8 media/*.mp4: MATCH (byte-identical to parent vertical/media/)
- All 8 mp3/beat-*.mp3: MATCH (byte-identical to parent vertical/mp3/)

## 2. Compile

```
python3 runtime/scripts/compile.py \
  /path/to/youtube/brutalist/shorts/claude-liam-brutalist-skill-your-turn-short \
  --height 3840 \
  --out .../exports/short
```

Result (2026-09-12): 8/8 slots filled (VIDEO), no slates, no drawtext overlays,
per-beat timeline with source audio preserved. Compiled at native 2160×3840
without `--review`. Beat sheet stamped `build.at: 2026-09-12T07:20:41`.

Skin-lint carry-overs from parent (cosmetic, not blockers):

- `SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk`
- `SKIN LINT: B13: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro`
- Motion histogram: reveal:4 type-on:3 hold:1 (reveal at 50%, just over the 40% cap)

These are intentional portrait variants per parent skin_warnings. The reveal tilt
is carried from the four retained mechanism/verdict beats — not correctable without
rewriting a retained beat. Noted for human reviewer.

## 3. Duration cap

```
ffprobe -v error -show_entries format=duration,size:stream=codec_type,codec_name,width,height,duration \
  exports/short/claude-liam-brutalist-skill-your-turn-short.mp4
```

```
video   h264  2160×3840  duration 131.750000
audio   aac   48000 Hz   duration 131.750000
format              size=9641320  duration 131.750000
```

All three durations equal 131.750 s ≪ 180.000 s. Cap satisfied with 48.25 s
of headroom.

## 4. File integrity

| File | SHA-256 |
|------|---------|
| exports/short/claude-liam-brutalist-skill-your-turn-short.mp4 | `4f2f38ce424a51ac73f3cf1cec91f2b0e1e7b93f681ee087cc235353a5660274` |
| beat_sheet.json | `170fc44a9727c838d7c59b0b27ba8fcc5441abb316e5d7a5a668d26b8561dbdc` |

Video SHA-256 unchanged from initial build — all inputs byte-identical.

## 5. Audio joins

All 7 internal seam RMS values carried forward from initial build (mp3 files
byte-identical; no regeneration):

| join    | pre-200ms RMS | post-200ms RMS |
|---------|---------------|----------------|
| B00→B01 | 11            | 3993           |
| B01→B03 | 22            | 3836           |
| B03→B09 | 12            | 4053           |
| B09→B10 | 12            | 3895           |
| B10→B11 | 8             | 2341           |
| B11→B12 | 11            | 1485           |
| B12→B13 | 11            | 2433           |

Natural silent tails before each next beat's speech — no clipped joins, no clicks.

## 6. Visual frame check

24 beat-relative JPEGs at 15/50/85% of each retained beat — all hashes verified
byte-identical to initial build (frames unchanged, media unchanged). See
VISUAL-REVIEW.json for full hash table. Representative check:

- B01 p85: resolves to corrected 'your-turn is / not a / closing-block / skill.'
- B03 p50: Mechanism card — eyebrow SKILL·BLOCK, heading, body, quote, verdict pill
- B09 p50: Worked-example — heading 'One fixture. Zero errors.', report body visible
- B10 p50: Limitation card — heading 'What your-turn does NOT do.', three limits
- B11 p50: Verdict artifact — six recap lines all visible
- B12 p50: YOUR TURN composer — 'Your turn.' greeting + paste-ready prompt
- B13 p50: Outro — 'The your-turn Skill.' + @NikBearBrown handle

Portrait framing safe on all cards; no left/right/top/bottom bleed.

## 7. Ownership / safety checks

- No mp3 or media file regenerated; all slots are byte-copies from parent vertical
- No API spend. Kokoro am_onyx audio already resident in parent reel
- No uploads, no Git push, no publication
- beat_sheet.json validates: short_validation.status = "ready", errors = []
- Parent 16:9 film untouched

## 8. Final artifact

- `exports/short/claude-liam-brutalist-skill-your-turn-short.mp4`
- SHA-256 `4f2f38ce424a51ac73f3cf1cec91f2b0e1e7b93f681ee087cc235353a5660274`
- 9.64 MB · 131.75 s · 2160×3840 · 24 fps · aac 48 kHz stereo

## Blockers / majors

**0 blockers · 0 majors.** Human review of the film is next; publication is a
separate human workflow.
