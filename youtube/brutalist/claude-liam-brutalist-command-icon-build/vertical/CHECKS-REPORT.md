# CHECKS-REPORT — vertical

## PROOF GATE (per `skills/make/ai-explainer/SKILL.md` § "PROOF GATE")

- Beats: 12 total (identical spine to landscape).
- Classification: 12 SHOW · 0 justified-HOLD · 0 PUNT-flagged.
- Teaching arc: same as landscape (see landscape CHECKS-REPORT.md).

## GATE V — `final_frame_check.py`

```
$ python3 runtime/qc/final_frame_check.py <reel/vertical> --mp4 <candidate.mp4>
[gate-v] frames=24 BLOCKER=0 MAJOR=0 → <reel/vertical>/_qc/REPORT.md
```

- Frames sampled at 50 % and 85 % of every beat (24 total).
- Contact sheet: `_qc/contact_sheet_vertical.png`. Individual PNGs under
  `_qc/frames_vertical/`. Text legible on every beat, no edge-bleed, no
  clipping, no unresolved slates.

## Iterations before the pass

- **B10 composer overflow.** First vertical build failed gate V with 2
  BLOCKER "edge-bleed" defects on B10 (the HANDOFF composer) at 50 % and
  85 %. Cause: the composer's `command` string plus 4-item `output` array
  exceeded the portrait safe area; the folder-chip/composer bottom edge
  crossed the title-safe inset. **Fix:** shortened the composer prompt from
  4 numbered steps to 3, reduced `output` from 4 lines to 3, and slightly
  shortened the narration to match. Re-rendered B10 and re-compiled. Gate
  V clean.
- **Portrait ClaudeCodeBeat overflow.** Same shipped `ClaudeCodeBeat`
  component was reused at 1080×1920 (as `ClaudeCodeBeat916`). Its font size
  `height * 0.022` = ~42 px at 1920 tall, combined with a card `width * 0.86`
  = ~929 px wide, fits only ~37 monospace characters per line. Landscape
  code text (~70 chars/line) overflowed horizontally in portrait AND rows
  beyond the card's inner height were clipped by `overflow: hidden`. **Fix:**
  authored a portrait-specific `code` string for each of the seven
  `ClaudeCodeBeat916` beats (B02–B08) — shorter lines (~35 chars max),
  fewer rows (~16 max), same meaning. Landscape beats keep the original
  wider layout. GATE V is not sensitive to text-inside-card clipping (it
  audits frame-edge bleed and title-safe margins), but the visual
  inspection caught it and the fix improves legibility on 9:16 devices.

Every scene was re-rendered from scratch via `remotion_scenes.py --force`
(never a stale cached clip) after each content change.

## Audio decode

```
$ ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,duration -of csv=p=0 <mp4>
aac,248.333000
```

- 12 Kokoro `am_onyx` MP3s ledgered as ground truth; per-beat durations
  sum to 248.33 s. Portrait cut is 4.7 s shorter than landscape because B10
  narration was condensed to match the 3-step portrait prompt.

## Video

```
$ ffprobe -v error -select_streams v:0 -show_entries stream=width,height,duration,codec_name,r_frame_rate -of csv=p=0 <mp4>
h264,2160,3840,24/1,248.291667
```

- 2160×3840 (native 4K portrait). 24 fps. NOT an upscaled crop of the
  landscape master — every scene rendered at native 1080×1920 first, then
  compile.py upsampled the assembled master to 4K.
- Final SHA-256: `3566906b923fb2b0ef211f5ed1dcb434109b2ad68144d389d43edeeecf4a86a2`

## Motion histogram (compiler notice, not a failure)

Same as landscape (`code-cascade:7 (58%)`). Same rationale — command
teardowns are code-first. Not a defect to repair.

## Compiler SKIN-LINT notices (false positives — expected)

```
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk
[art] SKIN LINT: B11: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro
```

- The `*916` variants ARE the correct portrait wrappers around the
  underlying `ClaudeComposerAsk` and `ClaudeTitleOutro` scenes. The linter
  matches the pattern name literally; it does not know that `*916` binds
  the same component to a 1080×1920 canvas. Same false positive appears on
  every vertical cut in the playlist (see ep-24 `command-icons`, ep-23
  `command-list`, ep-22 `command-help`). Logged, not repaired.

## Motion / captions

- No captions, no karaoke, no burned-in transcript (per playlist contract).
- Every beat is a Remotion scene registered in Root.tsx (see
  `PROMPTS.md § Rendering` for the render command); no hand-rolled
  `npx remotion render`.

## Runtime checks not run

Same as landscape. See TYPECHECK.md.

## Conclusion

Vertical gate log: PROOF GATE ✓ · GATE V ✓ (0 BLOCKER / 0 MAJOR) ·
compile ✓ · atomic-verify ✓ · dimensions verified 2160×3840 · audio
verified · every claim traced in FACTCHECK.md. Ready for human review.
