# CHECKS-REPORT — The logo Skill (portrait companion)

Run ID: `f971dbe48eef4a7c82cd58515b018d69` · (re-verified from `19539b2db46647a796f0f26e66bb6e76`) · commit-baseline: `ba2d0e0f`.

## Beat-authoring gate (PROOF GATE)

Same twelve beats as the landscape master, adapted to 9:16 native. Every beat
carries a `shot.show` block. No slates, no punts.

## Portrait-specific decisions

- `metadata.channel_title` deliberately omitted (per
  `feedback_channel_title_portrait_bleed`) — the compile.py overlay bleeds past
  the portrait `safe.b` even at ~3% font height. Channel identity still lives
  in every `ClaudeComposerAsk916.folderLabel` (`@HumanitariansAI`).
- Three `SkillTeardown*916.tsx` portrait wrappers copied from the guests /
  hai episode's `scene-source/` into this toolkit's isolated
  `runtime/remotion/src/scenes/` and registered in `Root.tsx` at compile time.
  Credited in `SOURCES.md`.
- `BrutalistHesitantWriter` was patched in the isolated toolkit only, per
  `feedback_hesitant_writer_portrait_scale`: the shipped
  `Math.min(width/1920, height/1080)` collapses to 0.5625 on 9:16;
  the patch uses `Math.min(width/1080, height/1920)` when the canvas is
  portrait so the serif fills the safe area instead of shrinking.

## Audio (regenerated per aspect)

```
$ python3 runtime/scripts/generate_audio_kokoro.py vertical
[kokoro] beat-B00.mp3  15.25s  voice=am_onyx
[kokoro] beat-B01.mp3  18.13s  voice=am_onyx
[kokoro] beat-B02.mp3  32.94s  voice=am_onyx
[kokoro] beat-B03.mp3  31.94s  voice=am_onyx
…
[kokoro] beat-B11.mp3  3.33s   voice=am_onyx
[kokoro] 12 beat(s) generated · cost $0.00
```

Kokoro `am_onyx` (local, free). Same narration texts as landscape (audio-first
rule; a portrait version does NOT change what the voice says).

## Remotion renders

All 12 beats rendered natively at 1080x1920 comp, super-sampled to 2160x3840
by `--scale=2`:

```
[remotion] B00: ok: ClaudeComposerAsk916       -> media/B00.mp4
[remotion] B01: ok: BrutalistHesitantWriter916 -> media/B01.mp4
[remotion] B02: ok: SkillTeardownAnatomy916    -> media/B02.mp4
[remotion] B03: ok: SkillTeardownPipeline916   -> media/B03.mp4
[remotion] B04: ok: SkillTeardownMechanism916  -> media/B04.mp4
[remotion] B05: ok: SkillTeardownMechanism916  -> media/B05.mp4
[remotion] B06: ok: SkillTeardownMechanism916  -> media/B06.mp4
[remotion] B07: ok: SkillTeardownMechanism916  -> media/B07.mp4
[remotion] B08: ok: SkillTeardownMechanism916  -> media/B08.mp4
[remotion] B09: ok: ClaudeVerdictArtifact916   -> media/B09.mp4
[remotion] B10: ok: ClaudeComposerAsk916       -> media/B10.mp4
[remotion] B11: ok: ClaudeTitleOutro916        -> media/B11.mp4
```

Chrome + node symlink patches identical to landscape (see landscape
CHECKS-REPORT.md for details).

## Portrait iteration log (Gate V feedback)

Portrait requires more room-aware sizing than landscape. Fixes applied
per-beat inside `vertical/beat_sheet.json` only:

- **B01 hesitant writer** — attempt 1 used the landscape recipe (fontSize 148,
  3 lines, lineSpacing 1.25). Gate V flagged underfill AND bottom edge-bleed.
  Fix: fontSize 130, 5 lines, lineSpacing 2.5 (per
  `feedback_hesitant_writer_portrait_bluf_recipe`). Content bbox now fills
  ~65% of the portrait safe area and last line lands above `safe.b`. CLEAN.
- **B03 pipeline** — attempt 1 kept all six phases + long labels + long
  desc lines; bottom edge-bleed. Fix: compressed to four representative phases
  (`PICK & LOCK`, `COPY + PAD`, `STAGE SVG`, `APPEND BEAT`) with tighter labels
  and a shorter footer. The **narration still names all six** flow steps —
  the diagram simply shows the four that carry the mental model in portrait.
  CLEAN.
- **B10 Your Turn** — attempt 1 pasted the landscape prompt verbatim; the
  composer input overflowed. Fix: shortened the command text by ~40% while
  preserving the three-check rubric. Same intent, tighter prose. CLEAN.

Every other beat (B00, B02, B04–B09, B11) passed on the first render — they
use the same source props as landscape because the SkillTeardown/Verdict/Outro
916 scenes are natively responsive.

## Compile (vertical)

```
$ python3 runtime/scripts/compile.py <reel>/vertical --height 3840 \
      --out <reel>/exports/vertical --force

[art] compiled B00  VIDEO    15.2s  ← B00.mp4
[art] compiled B01  VIDEO    18.2s  ← B01.mp4  (post-fix render)
[art] compiled B02  VIDEO    33.0s  ← B02.mp4
[art] compiled B03  VIDEO    32.0s  ← B03.mp4  (post-fix render)
[art] compiled B04  VIDEO    28.8s  ← B04.mp4
[art] compiled B05  VIDEO    27.3s  ← B05.mp4
[art] compiled B06  VIDEO    33.1s  ← B06.mp4
[art] compiled B07  VIDEO    29.5s  ← B07.mp4
[art] compiled B08  VIDEO    33.5s  ← B08.mp4
[art] compiled B09  VIDEO    29.0s  ← B09.mp4
[art] compiled B10  VIDEO    34.4s  ← B10.mp4  (post-fix render)
[art] compiled B11  VIDEO     3.3s  ← B11.mp4
[art] SKIN LINT: B00 palette=claude but the cold open is 'ClaudeComposerAsk916'
[art] SKIN LINT: B11 palette=claude but the outro is 'ClaudeTitleOutro916'
[art] build stamp → beat_sheet.json (12/12 filled)
[art] wrote .../exports/vertical/claude-liam-brutalist-skill-logo-vertical.mp4
      (317.2s)
```

Two SKIN LINT warnings are **expected**: for the portrait cut the 916 variants
ARE the correct compositions, and this is exactly how the hai episode logged
them too. Not a defect.

## Gate V — visual QC

```
[gate-v] frames=24 BLOCKER=0 MAJOR=0 → _qc/REPORT.md
[gate-v] clean.
```

`_qc/REPORT.md`: "Frames sampled: 24 · BLOCKER: 0 · MAJOR: 0"

## Frame inspection

Per-beat frames sampled at 50/85% and Read as images
(`vertical/_qc/samples/`). Selected reads:

- `B00_85.png` — cold-open composer, greeting + ask + three-line answer,
  @HumanitariansAI folder chip. Native portrait reflow (composer centered).
- `B01_85.png` — hesitant BLUF final: "The logo skill / plays a random / brand
  sting. / The MP3 / is the clock." — the correction from `fixed` → `random`
  landed; content fills safe area.
- `B02_85.png` — folder tree stacked, callout at bottom.
- `B03_85.png` — 4-phase compressed pipeline diagram with PICK & LOCK
  highlighted terracotta.
- `B08_85.png` — Falsifiability card with the `logos/nik-bear-brown/` quote.
- `B10_50.png` — Your Turn composer with the shortened dry-run prompt visible;
  three-check rubric visible below.
- `B11_50.png` — outro title card, hardcoded @NikBearBrown handle, seeded
  pixel mascot.

## Verified atomic output

Output: `exports/vertical/claude-liam-brutalist-skill-logo-vertical.mp4`
- 2160x3840, 317.25s, h264 + aac
- `.verified.json` written by compile.py after Gate V passed

## No captions, no unauthorized actions

Same standing rules as landscape. Never published, never uploaded, no API-key
fallback.

Bear's editing pass is next.
