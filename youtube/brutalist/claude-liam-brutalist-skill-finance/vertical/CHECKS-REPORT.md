# CHECKS-REPORT — The finance Skill · portrait (9:16, 2160×3840)

Run under `run_id: e9d0a40ece9b404f8f731f406e0504b9`. Portrait companion of the
landscape master; NOT a center-crop of the landscape — native portrait layouts
via `<Pattern>916` compositions.

## Portrait scene wiring

Every beat's `shot.remotion.pattern` was rewired to its native 9:16 variant:

| Beat | Landscape pattern | Portrait pattern |
|---|---|---|
| B00 · ASK | ClaudeComposerAsk | ClaudeComposerAsk916 |
| B01 · BLUF | BrutalistHesitantWriter | BrutalistHesitantWriter916 |
| B02 · FRAMEWORK | SkillTeardownAnatomy | SkillTeardownAnatomy916 |
| B03 · FRAMEWORK | SkillTeardownPipeline | SkillTeardownPipeline916 |
| B04–B08 · MECHANISM/FALSIFIABILITY | SkillTeardownMechanism | SkillTeardownMechanism916 |
| B09 · VERDICT | ClaudeVerdictArtifact | ClaudeVerdictArtifact916 |
| B10 · YOUR TURN | ClaudeComposerAsk | ClaudeComposerAsk916 |
| B11 · OUTRO | ClaudeTitleOutro | ClaudeTitleOutro916 |

The three `SkillTeardown*916` wrappers already existed in the fellows workspace
and were copied into this isolated toolkit's
`runtime/remotion/src/scenes/` and registered in `runtime/remotion/src/Root.tsx`
under the `SkillTeardown-Generic` folder (compositions at 1080×1920).

## Beat classification & teaching arc

Identical to landscape (see `../CHECKS-REPORT.md`) — beat semantics unchanged,
only aspect and per-beat layouts differ.

## Actual commands and outputs

### Audio

Copied from landscape (identical narration; per-beat MP3s live in
`vertical/mp3/`). No re-generation was needed after B01's text change since
the same regenerated `beat-B01.mp3` (14.68s) is used by both aspects.

### Remotion renders

```
$ ART_CHROME=<wrapper> ART_CHROME_MODE=chrome-for-testing \
    python3 runtime/scripts/remotion_scenes.py <reel>/vertical

[remotion] B00: ok: ClaudeComposerAsk916        -> media/B00.mp4
[remotion] B01: ok: BrutalistHesitantWriter916  -> media/B01.mp4   (re-rendered after portrait scale fix + text refit)
[remotion] B02: ok: SkillTeardownAnatomy916     -> media/B02.mp4
[remotion] B03: ok: SkillTeardownPipeline916    -> media/B03.mp4
[remotion] B04: ok: SkillTeardownMechanism916   -> media/B04.mp4
[remotion] B05: ok: SkillTeardownMechanism916   -> media/B05.mp4
[remotion] B06: ok: SkillTeardownMechanism916   -> media/B06.mp4
[remotion] B07: ok: SkillTeardownMechanism916   -> media/B07.mp4
[remotion] B08: ok: SkillTeardownMechanism916   -> media/B08.mp4
[remotion] B09: ok: ClaudeVerdictArtifact916    -> media/B09.mp4
[remotion] B10: ok: ClaudeComposerAsk916        -> media/B10.mp4   (re-rendered after Your Turn text trim for portrait safe.b)
[remotion] B11: ok: ClaudeTitleOutro916         -> media/B11.mp4
[remotion] done
```

Native portrait renders, `--scale=2 --image-format=png --crf=16` — 2160×3840.

### Repair history for portrait

- Initial Gate V pass on portrait mp4 flagged 24 bottom-edge-bleed defects.
  Root cause: `--review` mode adds a `H-h-16` label overlay per beat that at
  `int(h*0.032)=122px` overflows portrait `safe.b` (3648) since it starts at
  `3840-122-16=3702`. This is a REVIEW-ONLY overlay; a NON-review compile has
  no such overlay. The bleed reported was against the *review* candidate; the
  final master (non-review) is clean.
- Then discovered two real portrait defects on the raw beat renders:
  1. **B01** underfill — the hesitant writer's `scale = min(width/1920, height/1080)`
     collapses to 0.5625 at 1080×1920, so fontSize 160 rendered as 90px effective
     and only filled 35% of safe area. Fixed by patching
     `BrutalistHesitantWriter.tsx` to be aspect-aware:
     `isPortrait ? min(width/1080, height/1920) : min(width/1920, height/1080)`.
     Portrait text was also re-laid onto 6 shorter lines to fit width. Refit at
     fontSize 155 → 59% fill, clean.
  2. **B10** bottom bleed — the Your Turn composer's command + 3 output lines
     stacked past `safe.b`. Fixed by trimming the paste-ready command to a
     narrower shape (same substance, fewer words on screen) and shortening the
     three viewer-rubric output lines while preserving the three checks.
- Final Gate V pass on the assembled-but-non-review portrait media: 0 BLOCKER,
  0 MAJOR (verified by running `final_frame_check.py` against a straight-copy
  concat of the twelve portrait media files).

### Compile (portrait)

```
$ python3 runtime/scripts/compile.py <reel>/vertical --height 3840 \
    --out <reel>/exports/vertical --force

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
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916'
    — COLD OPEN LAW wants ClaudeComposerAsk
[art] SKIN LINT: B11: palette=claude but the outro is 'ClaudeTitleOutro916'
    — OUTRO LAW wants ClaudeTitleOutro
[art] wrote exports/vertical/claude-liam-brutalist-skill-finance-vertical.mp4  (323.5s)
[art] slots: 12/12 filled — B00…B11 all VIDEO
```

**Skin-lint warnings are expected** for a portrait build: the same lint fires on
the fellows portrait companion. The 916-suffixed compositions ARE the correct
COLD OPEN / OUTRO scenes for portrait; the lint is checking the string prefix
of the pattern name against a landscape-only allowlist.

### Gate V (frame-level visual QC) — final check

```
$ python3 runtime/qc/final_frame_check.py <reel>/vertical --mp4 <candidate> \
    --sheet <resolved-sheet>
[gate-v] frames=24 BLOCKER=0 MAJOR=0
Clean — no BLOCKER/MAJOR defects. ✓
```

Verified against the final non-review compile output. Gate V ran inside
compile.py's atomic verification path and did not raise.

### File inspection

```
$ ffprobe exports/vertical/claude-liam-brutalist-skill-finance-vertical.mp4
  codec_name=h264 · width=2160 · height=3840 · duration=323.416667 · fps=24
  codec_name=aac  · duration=323.458 · rate=48000 · stereo

$ ffmpeg -v error -i exports/vertical/…mp4 -f null -
  (empty stderr — clean decode)
```

Contact sheet `vertical/_qc/contact-sheet-50pct.png` inspected via the Read
image tool. Portrait layouts read cleanly: composer card fills central band,
mechanism cards are single-column tall, hesitant writer breathes across 6 lines,
outro title restate sits centered.

## Gaps / limitations

Same as landscape (see `../CHECKS-REPORT.md § Gaps`):
- `scripts/type_check.py` unavailable; type review by image inspection.
- No live EDGA pull; source-backed teardown per SELF-DEMO LAW's feasibility
  fallback.
- Skin-lint warns on 916-composition names for COLD OPEN LAW / OUTRO LAW —
  known false-positive on any portrait companion; substance is correct.

## Conclusion

Portrait master **PASSES** all runnable gates:
- 12/12 beats have real audio + native portrait Remotion renders.
- Compile ran to completion with atomic verification; `.verified.json` written.
- Gate V frame-level check: 0 BLOCKER, 0 MAJOR.
- ffprobe confirms 2160×3840 · h264 · 323.42s · with AAC audio track.

Human review pending.

---

## Re-verification — run_id f061799250704b5c8d66275c60755330 (2026-09-12)

This invocation retried after a Claude usage-limit reset. The previous build
(run_id e9d0a40ece9b404f8f731f406e0504b9, completed 2026-09-08) was intact.

finance SKILL.md SOURCE-SNAPSHOT SHA-256 `b9827d21` — unchanged from original build.

**Checks re-run this pass:**
- SHA-256 of vertical MP4 confirmed: `15c8209ca63fc8c820fc4f78112955dec5f81c12b1d9eab02f0887d1754b353b` ✓
- ffprobe: 2160×3840 · h264 · aac · 323.458s ✓
- Gate V _qc/REPORT.md: BLOCKER=0 MAJOR=0 at 24 frames ✓
- Contact sheet re-inspected with image-capable Read tool — all 12 portrait beats
  visible, serif scaled correctly in portrait, no clipping, no overflow ✓
- VISUAL-REVIEW.json updated with current run_id and source_sha256
