# CHECKS-REPORT — The logo Skill — Short (9:16 derivative)

Run ID `738dc432a7ab423fae14aaca169b73fd` (re-verified 2026-09-12; originally
built under `83cff665286b4cab94e34c143b4dbf0b` on 2026-09-08). All commands
were run from the isolated toolkit at
`.repoloop/shorts/workspaces/claude-liam-brutalist-skill-logo-short/toolkit`.

## Cut (whole-beat, no rewrite)

```
python3 runtime/scripts/shorts.py \
  /Users/bear/…/brutalist/claude-liam-brutalist-skill-logo/vertical \
  --output-dir /Users/bear/…/brutalist/shorts/claude-liam-brutalist-skill-logo-short \
  --slug claude-liam-brutalist-skill-logo-short \
  --drop B02 B03 B06 B07 B10 --no-endcard --no-outro-rewrite
```

Output (excerpt):

```
[short] parent reel: 12 beats · 317.2s (5:17.2) · Shorts cap 3:00
[short] manual plan: dropping B02, B03, B06, B07, B10
[short] B00 native portrait reused unchanged
[short] B01 native portrait reused unchanged
[short] B04 native portrait reused unchanged
[short] B05 native portrait reused unchanged
[short] B08 native portrait reused unchanged
[short] B09 native portrait reused unchanged
[short] B11 native portrait reused unchanged
[short] 7 beats · ~155.4s (2:35.4) OK
[short] dropped: B02, B03, B06, B07, B10 · ends on the last beat (no endcard)
```

Every retained beat's parent `media/<bid>.mp4` was verified 2160×3840 by
`shorts.py`'s aspect check (`width*16 == height*9`) and copied unchanged into
`short/media/`. No re-render, no crop, no regenerated audio.

## Compile

```
python3 runtime/scripts/compile.py \
  /Users/bear/…/brutalist/shorts/claude-liam-brutalist-skill-logo-short \
  --height 3840 --out …/exports/short
```

Output:

```
[art] compiled B00  VIDEO    15.2s  ← B00.mp4
[art] compiled B01  VIDEO    18.2s  ← B01.mp4
[art] compiled B04  VIDEO    28.8s  ← B04.mp4
[art] compiled B05  VIDEO    27.3s  ← B05.mp4
[art] compiled B08  VIDEO    33.5s  ← B08.mp4
[art] compiled B09  VIDEO    29.0s  ← B09.mp4
[art] compiled B11  VIDEO     3.3s  ← B11.mp4
[art] motion histogram: reveal:4  type-on:2  hold:1
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916'
                 — COLD OPEN LAW wants ClaudeComposerAsk
[art] SKIN LINT: B11: palette=claude but the outro is 'ClaudeTitleOutro916'
                 — OUTRO LAW wants ClaudeTitleOutro
[art] build stamp → beat_sheet.json (7/7 filled)
[art] wrote …/exports/short/claude-liam-brutalist-skill-logo-short.mp4
       (155.4s, audio: per-beat timeline (source audio preserved),
        drawtext: no — PIL overlays)
[art] slots: 7/7 filled — B00:VIDEO B01:VIDEO B04:VIDEO B05:VIDEO
       B08:VIDEO B09:VIDEO B11:VIDEO
```

The two SKIN LINT warnings are the parent vertical's known portrait trade-off
(the `*916` compositions rewire `ClaudeComposerAsk`/`ClaudeTitleOutro`); they
are inherited from the vertical parent and not defects for this derivative.

## Duration gates (strictly under 180 s)

```
$ ffprobe -v error -show_entries \
    format=duration,size:stream=codec_type,codec_name,duration,width,height \
    -of default=noprint_wrappers=1 \
    exports/short/claude-liam-brutalist-skill-logo-short.mp4
codec_name=h264
codec_type=video
width=2160
height=3840
duration=155.375000
codec_name=aac
codec_type=audio
duration=155.375000
duration=155.375000
size=11480409
```

- Timeline sum (sheet `render_duration_s`): **155.375 s** — `require_short_duration`
  passed inside both `shorts.py` (planning) and `compile.py` (post-mux).
- Container duration: **155.375 s** — strictly under 180 s.
- Video stream duration: **155.375 s** — strictly under 180 s.
- Audio stream duration: **155.375 s** — strictly under 180 s.
- Dimensions: **2160×3840** (native portrait 4K, no upscale).

## Audio decode

```
$ ffmpeg -v error -i exports/short/…mp4 -vn -f null - && echo AUDIO_DECODE_OK
AUDIO_DECODE_OK
```

Full AAC stream decoded without error. Per-beat mp3 concat preserved. No
speech is clipped, sped up or truncated — every retained beat is the parent's
original Kokoro `am_onyx` render, byte-for-byte.

## Visual review

- Extracted 2 fps sample frames (311 PNGs at `_qc/frames/f001.png` …
  `f311.png`).
- Extracted beat-relative 15% / 50% / 85% frames per kept beat (21 PNGs
  named `_qc/frames/{B00,B01,B04,B05,B08,B09,B11}-{p15,p50,p85}.png`).
- Built a 3×7 contact sheet at `_qc/contact-sheet.png` (SHA-256 recorded in
  `VISUAL-REVIEW.json`).
- Directly viewed the p50 frame for each of the 7 retained beats and the
  edge (p15 / p85) frames for B00, B01, B11.

Findings — no blockers, no majors. Details:

- **B00 (composer ask):** eyebrow "BRUTALIST · SKILL TEARDOWN" and title
  "The logo Skill" sit inside the top portrait safe area; "Hola, Liam"
  greeting scaled for portrait; composer card with the three-line ask
  ("mental model, not the README summary") legible; result lines "appends
  ONE brand sting…" appear under the folder chip "@HumanitariansAI".
- **B01 (BLUF hesitant writer):** five-line serif fills the portrait safe
  area — "The logo skill / plays a random / brand sting. / The MP3 / is the
  clock." — showing the resolved state after the "fixed → random" swap.
  Trigger-word deletion visible at p15.
- **B04 (MECHANISM ACT 1):** eyebrow "MECHANISM · ACT 1" and heading "The
  MP3 is the clock." on cream; body paragraph, verbatim quote block
  ("The MP3 is the clock — and the jingle is NEVER cut."), verdict pill
  "TRIM SILENCE, NEVER SOUND", spark "Silence lives IN the clock." All
  inside portrait safe area.
- **B05 (MECHANISM ACT 2):** eyebrow "MECHANISM · ACT 2" and heading
  "Random once, then locked." on cream; body paragraph mentioning
  SystemRandom and `shot.remotion.picked`; verbatim quote block; verdict
  pill "-REROLL TO RE-SPIN"; spark "Random across reels. Locked within
  one."
- **B08 (FALSIFIABILITY ACT 5):** eyebrow "FALSIFIABILITY · ACT 5" and
  heading "No nik-bear-brown pool." on cream; body paragraph naming the
  four brand pools; verbatim quote block from SKILL.md; verdict pill
  "NBB → CLAUDETITLEOUTRO · EVERYONE ELSE → LOGOOUTRO"; spark "One skill
  does not fit all channels."
- **B09 (verdict artifact):** artifact card "The logo Skill" with heading
  "A locked lottery. Silence at the end." and all six verdict lines
  numbered in terracotta, each legible at portrait scale.
- **B11 (title outro):** dark cream-on-ink ground with title "The logo
  Skill." and hardcoded "@NikBearBrown" beneath. Pixel mascot animates
  from the slug seed; last frame holds cleanly.

Audio joins between beats are clean (per-beat mp3 concat, no truncation, no
click on the boundaries). No captions burned in. Two carry-over palette lint
warnings (B00/B11 on the `*916` compositions) are known portrait-native
trade-offs, not defects.

## Provenance

- Supervisor `episode.source_sha256` (2026-09-12 invocation):
  `cd91c7629215668fc384f7ede73832e62d91423c676f62711f3a3cfa17cc9da7`.
- Parent vertical beat sheet SHA-256 (current, 2026-09-12):
  `07b56335795af257554a8e1fdd8908c9a3a2d4039c293a210da739d661b3f109`.
  (Original build source: `b1aa8e364f7353c33919b2f5d3d55e3f463b27480c40077071cc1fe287660784`.)
  Retained beats B00/B01/B04/B05/B08/B09/B11 content is unchanged in both versions.
- Parent vertical master SHA-256 (`episode.parent_master_sha256`):
  `c9a9fb393e384ec024b1f9b3afbb375343e89aae23848ba0558786e6a0361a71`.
- This Short's beat sheet SHA-256:
  `8f9b44579415fc5cec38aae839d43adabfc5e604f4b064f613cceb169c1c4896`.
- This Short's export SHA-256:
  `bc8acd5074866633ae8626c11e0ef134c2fbe527121049bca060bedd9af57f46`.

## Human approvals

`metadata.approvals = {}`. `runtime/scripts/build_safety.py::validate_approvals`
runs inside `compile.py` and did not raise — this Short is neither a fellows
profile nor does any retained beat carry a `professor_notes` / GATE-N
requirement. No signature was fabricated; no human review is claimed.

## Conclusion

The Short is 155.375 s of native portrait 4K, strictly under 3:00, using only
the vertical parent's native renders and Kokoro `am_onyx` audio, unchanged.
Written at
`exports/short/claude-liam-brutalist-skill-logo-short.mp4`.
Human review by Bear is pending.
