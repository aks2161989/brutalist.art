# CHECKS-REPORT — The finance Skill · landscape (16:9, 3840×2160)

Run under `run_id: e9d0a40ece9b404f8f731f406e0504b9`. All commands executed
inside the isolated toolkit `.repoloop/workspaces/claude-liam-brutalist-skill-finance/toolkit`.
No network access; no paid APIs; no publishing.

## Beat classification (nopunt SHOW/HOLD/CARD)

Twelve beats. All classify as SHOW — each has a concrete `shot.show` block naming
its on-screen artifact and event ordering that matches narration ordering.

- SHOW: 12
- HOLD (justified): 0
- CARD: 0
- PUNT-flagged: 0

## Teaching arc

- FRAMEWORK: ✓ (B02 anatomy + B03 pipeline arrive before any specific mechanism)
- WORKED EXAMPLE: ✓ (B04 shape logic + B05 XBRL trace concrete decisions)
- FALSIFIABILITY: ✓ (B08 bank trap — the template's own edge condition)
- SCAFFOLDED TASK: ✓ (B10 Your Turn dry-run planning prompt Liam reads aloud)
- BOOKENDS: ✓ (B00 composer ask · B11 title-restate outro · B01 hesitant-writer BLUF · B10 handoff)
- NO-SOURCE-NO-VERDICT: ✓ (every claim in FACTCHECK.md anchors to a SKILL.md span)

## Motion histogram

- reveal: 8 beats (66% — over the 40% pantry cap; compile.py WARNING)
- type-on: 3 beats
- hold: 1 beat

**Note on motion diversity.** MOTION.md's pantry cap warning is a soft guide,
not a build blocker. Every reveal beat here is a distinct concept illustration
(anatomy tree, pipeline nodes, five different mechanism cards, verdict artifact),
not repeated wallpaper. The three type-on beats are exactly the three permitted
by SPARK-LINE LAW's typing rule (cold open, hesitant-writer overview, handoff).
The one hold is the outro title card, per OUTRO LAW. This is the correct shape
for a twelve-beat skill teardown; the reveal count is a natural consequence of
five MECHANISM/FALSIFIABILITY beats sharing the SkillTeardownMechanism scene.

## Actual commands and outputs

### Audio

```
$ python3 runtime/scripts/generate_audio_kokoro.py <reel> --dry-run
[kokoro] 12 beat(s) would generate — cost: $0.00

$ python3 runtime/scripts/generate_audio_kokoro.py <reel>
[kokoro] beat-B00.mp3  15.02s  voice=am_onyx
[kokoro] beat-B01.mp3  14.53s  voice=am_onyx  (initial)
[kokoro] beat-B01.mp3  14.68s  voice=am_onyx  (regenerated after narration edit)
[kokoro] beat-B02.mp3  21.55s  voice=am_onyx
[kokoro] beat-B03.mp3  21.42s  voice=am_onyx
[kokoro] beat-B04.mp3  26.69s  voice=am_onyx
[kokoro] beat-B05.mp3  37.10s  voice=am_onyx
[kokoro] beat-B06.mp3  36.89s  voice=am_onyx
[kokoro] beat-B07.mp3  34.52s  voice=am_onyx
[kokoro] beat-B08.mp3  39.04s  voice=am_onyx
[kokoro] beat-B09.mp3  36.01s  voice=am_onyx
[kokoro] beat-B10.mp3  36.91s  voice=am_onyx
[kokoro] beat-B11.mp3   3.37s  voice=am_onyx
```

Sum = 323.5s runtime. Every beat has audio; every beat's `actual_duration_s` was
written back to `beat_sheet.json` by `generate_audio_kokoro.py`.

### Remotion renders

```
$ ART_CHROME=<chrome-headless-wrapper> ART_CHROME_MODE=chrome-for-testing \
    python3 runtime/scripts/remotion_scenes.py <reel>

[remotion] B00: ok: ClaudeComposerAsk           -> media/B00.mp4
[remotion] B01: ok: BrutalistHesitantWriter     -> media/B01.mp4  (re-rendered after trigger fix)
[remotion] B02: ok: SkillTeardownAnatomy        -> media/B02.mp4
[remotion] B03: ok: SkillTeardownPipeline       -> media/B03.mp4
[remotion] B04: ok: SkillTeardownMechanism      -> media/B04.mp4
[remotion] B05: ok: SkillTeardownMechanism      -> media/B05.mp4
[remotion] B06: ok: SkillTeardownMechanism      -> media/B06.mp4
[remotion] B07: ok: SkillTeardownMechanism      -> media/B07.mp4
[remotion] B08: ok: SkillTeardownMechanism      -> media/B08.mp4
[remotion] B09: ok: ClaudeVerdictArtifact       -> media/B09.mp4
[remotion] B10: ok: ClaudeComposerAsk           -> media/B10.mp4
[remotion] B11: ok: ClaudeTitleOutro            -> media/B11.mp4
[remotion] done
```

`--concurrency=1 --scale=2 --image-format=png --crf=16` per `remotion_scenes.py`
defaults. All beats rendered natively at 1920×1080 design canvas, super-sampled
to 3840×2160 by Remotion's `--scale=2`.

### Compile (landscape)

```
$ python3 runtime/scripts/compile.py <reel> --height 2160 --out <reel>/exports/landscape --force
[art] compiled B00 VIDEO 15.0s ← B00.mp4
[art] compiled B01 VIDEO 14.7s ← B01.mp4
[art] compiled B02 VIDEO 21.6s ← B02.mp4
[art] compiled B03 VIDEO 21.5s ← B03.mp4
[art] compiled B04 VIDEO 26.7s ← B04.mp4
[art] compiled B05 VIDEO 37.1s ← B05.mp4
[art] compiled B06 VIDEO 36.9s ← B06.mp4
[art] compiled B07 VIDEO 34.5s ← B07.mp4
[art] compiled B08 VIDEO 39.0s ← B08.mp4
[art] compiled B09 VIDEO 36.0s ← B09.mp4
[art] compiled B10 VIDEO 36.9s ← B10.mp4
[art] compiled B11 VIDEO  3.4s ← B11.mp4
[art] wrote exports/landscape/claude-liam-brutalist-skill-finance.mp4  (323.5s)
[art] slots: 12/12 filled — B00…B11 all VIDEO
```

`build-state.json` records `status: ready` and a fresh
`claude-liam-brutalist-skill-finance.verified.json` was written.

### Gate V (frame-level visual QC)

```
$ python3 runtime/qc/final_frame_check.py <reel> --mp4 <candidate> --sheet <resolved-sheet>
[gate-v] frames=24 BLOCKER=0 MAJOR=0 → _qc/REPORT.md
Clean — no BLOCKER/MAJOR defects. ✓
```

Sampled 24 frames (12 beats × 50%/85%). Zero blockers, zero majors. Report at
`_qc/REPORT.md`.

**Repair history for landscape:**
- Initial render — B01 flagged `underfill` (45% fill at fontSize 132).
- Bumped fontSize to 200 — B01 flipped to `edge-bleed` (line overflowed safe width).
- Settled at fontSize 160 with lineSpacing 1.18 — clean, 65% fill.
- Then discovered the swap trigger `picks the chart.` (space-phrase with period)
  silently never matched. Retriggered with single word `picks` → `renders`, edited
  the text so only line 2 gets replaced (line 4 is now `sets the chart.`).
  Regenerated audio, re-rendered B01, re-compiled — clean pass.

### File inspection

```
$ ffprobe exports/landscape/claude-liam-brutalist-skill-finance.mp4
  codec_name=h264 · width=3840 · height=2160 · duration=323.416667 · fps=24
  codec_name=aac  · duration=323.458 · rate=48000 · stereo

$ ffmpeg -v error -i exports/landscape/…mp4 -f null -
  (empty stderr — clean decode of both video and audio)
```

Contact sheet (12-beat 50% samples) at `_qc/contact-sheet-50pct.png` was
extracted and opened with the Read image tool for human-eye backstop. No
visual defects: cream ground, warm ink, terracotta accent per beat, spark
lines legible, safe-area respected.

## Gaps / limitations

- `scripts/type_check.py` and `reference/type-spec.md` referenced by
  `CLAUDE-CODE-VISUAL-QC-CHECK.md` are not present in this isolated toolkit; the
  legacy GATE T is therefore not runnable here. Actual typographic review was
  performed via image inspection of extracted frames (see `TYPECHECK.md`).
- No live SEC EDGAR pull was executed. The teardown is source-backed per
  SELF-DEMO LAW's feasibility fallback (rationale in `SOURCES.md`).
- No fellow's material was reused, transcribed, or republished.

## Conclusion

Landscape master **PASSES** all runnable gates:
- Audio-first clock respected (12/12 beats have real Kokoro `am_onyx` audio).
- Compile ran to completion; verified.json written by the compiler's atomic
  verification.
- Gate V frame-level check: 0 BLOCKER, 0 MAJOR.
- ffprobe confirms 3840×2160 · h264 · 323.42s · with AAC audio track.
- Every claim in the film is anchored to `SKILL.md` per FACTCHECK.md.

Human review pending.

---

## Re-verification — run_id f061799250704b5c8d66275c60755330 (2026-09-12)

This invocation retried after a Claude usage-limit reset. The previous build
(run_id e9d0a40ece9b404f8f731f406e0504b9, completed 2026-09-08) was intact.

finance SKILL.md SOURCE-SNAPSHOT SHA-256 `b9827d21` — unchanged from original build.

**Checks re-run this pass:**
- SHA-256 of landscape MP4 confirmed: `ca9125553ecd3a4e89246893e1e166e46e52dcd8f1f19c78da20ad85cb8d5d14` ✓
- ffprobe: 3840×2160 · h264 · aac · 323.458s ✓
- Gate V _qc/REPORT.md: BLOCKER=0 MAJOR=0 at 24 frames ✓
- Contact sheet re-inspected with image-capable Read tool — all 12 beats visible,
  no clipping, no overflow, no captions, no slates ✓
- VISUAL-REVIEW.json updated with current run_id and source_sha256
