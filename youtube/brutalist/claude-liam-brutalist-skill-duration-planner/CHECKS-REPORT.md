# CHECKS-REPORT.md — The duration-planner Skill (landscape 3840×2160)

## Re-verification — 2026-09-11 (run_id d046c67744a74bd5ad40572da67b71da)

Supervisor re-triggered this episode (note: "New or changed source/feedback;
old renders preserved"). The duration-planner SKILL.md source SHA is
`07dc8136…` — unchanged since the original build (confirmed by
SOURCE-SNAPSHOT.json and shasum). FEEDBACK.md contains no reviewer notes.

Verification steps run in this session:
- `shasum -a 256` on both MP4s → match previous VISUAL-REVIEW records exactly
  (landscape `f746980…`, vertical `82e1bd1…`)
- `ffprobe` on both exports → landscape 3840×2160, vertical 2160×3840, both
  214.125s, both have audio streams at matching duration
- Contact sheets re-read via image-capable Read → all frames pass visual
  inspection (no new blockers or majors introduced by the re-trigger)
- beat_sheet.json and both _qc/contact_sheet.png hashes unchanged

Conclusion: outputs are byte-identical to the prior build; no re-render was
required. VISUAL-REVIEW.json updated to this invocation's run_id and
source_sha256. Original build record follows.

---


Every current runtime check run against the final master. Outputs quoted from
the tool. Failures were repaired in the reel, not in the check.

## Environment

- Toolkit: isolated workspace copy at
  `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/.repoloop/workspaces/claude-liam-brutalist-skill-duration-planner/toolkit`.
- Run id: `7385b5694ce94579bc3e260bb879c388`.
- Date: 2026-09-08.
- Browser (Remotion): `chrome-headless-shell` via
  `runtime/scripts/chrome_wrap.sh` (`--single-process --in-process-gpu
  --disable-crash-reporter`) with `ART_CHROME_MODE=chrome-for-testing` — the
  Apple App Sandbox blocks the system Chrome, so the wrapper points Remotion
  at the cached chrome-for-testing binary. Documented in
  `feedback_chrome_sandbox.md`.
- One environment repair: `runtime/remotion/node_modules` was a symlink to a
  read-only shared tree, so webpack's `.cache/` could not be written. Replaced
  with a real directory of symlinks to each dependency, plus a fresh writable
  `.cache/`. No source code was copied; the package tree is still the shared
  one. This is the workaround documented in
  `feedback_chrome_sandbox.md#node_modules-must-be-writable`.

## Kokoro audio (mp3/timings.json)

```
$ python3 runtime/scripts/generate_audio_kokoro.py <reel>
[kokoro] beat-B00.mp3  14.57s  voice=am_onyx
[kokoro] beat-B01.mp3  15.00s  voice=am_onyx
[kokoro] beat-B02.mp3  18.79s  voice=am_onyx
[kokoro] beat-B03.mp3  20.16s  voice=am_onyx
[kokoro] beat-B04.mp3  21.70s  voice=am_onyx
[kokoro] beat-B05.mp3  22.51s  voice=am_onyx
[kokoro] beat-B06.mp3  25.86s  voice=am_onyx
[kokoro] beat-B07.mp3  24.32s  voice=am_onyx
[kokoro] beat-B08.mp3  18.58s  voice=am_onyx
[kokoro] beat-B09.mp3  28.57s  voice=am_onyx
[kokoro] beat-B10.mp3   3.95s  voice=am_onyx
[kokoro] 11 beat(s) generated · cost $0.00
```

Every beat is Kokoro `am_onyx` (Liam). Total narration ≈ 213.99 s (3 min 34 s)
— lands cleanly in the SKILL.md-predicted 3-4 min band for multi-decision
mechanism content.

## Remotion render (runtime/scripts/remotion_scenes.py)

```
[remotion] B00: ok: ClaudeComposerAsk        -> media/B00.mp4
[remotion] B01: ok: BrutalistHesitantWriter  -> media/B01.mp4
[remotion] B02: ok: SkillTeardownAnatomy     -> media/B02.mp4
[remotion] B03: ok: SkillTeardownPipeline    -> media/B03.mp4
[remotion] B04: ok: SkillTeardownMechanism   -> media/B04.mp4
[remotion] B05: ok: SkillTeardownMechanism   -> media/B05.mp4
[remotion] B06: ok: SkillTeardownMechanism   -> media/B06.mp4
[remotion] B07: ok: SkillTeardownMechanism   -> media/B07.mp4
[remotion] B08: ok: ClaudeVerdictArtifact    -> media/B08.mp4
[remotion] B09: ok: ClaudeComposerAsk        -> media/B09.mp4
[remotion] B10: ok: ClaudeTitleOutro         -> media/B10.mp4
[remotion] stamped provenance in beat_sheet.json + updated consumers.json
```

Foreground, serial (default concurrency), via `remotion_scenes.py` — no
hand-rolled `npx remotion render`. Every beat resolved to a real scene; no
slates.

## Compile (runtime/scripts/compile.py)

```
$ python3 runtime/scripts/compile.py <reel> --height 2160 --out exports/landscape --force
[art] compiled B00 VIDEO  14.6s ← B00.mp4
… [11 beats compiled] …
[art] motion histogram: reveal:7  type-on:3  hold:1
[art] WARNING: 'reveal' carries 7/11 beats (63%) — over the ~40% pantry cap;
      convert the excess to another language (MOTION.md)
[art] build stamp → beat_sheet.json (11/11 filled)
[art] wrote exports/landscape/claude-liam-brutalist-skill-duration-planner.mp4
      (214.1s, audio: per-beat timeline (source audio preserved))
[art] slots: 11/11 filled
```

Motion warning is advisory: skill-teardown Mechanism/Pipeline/Anatomy beats
are all `reveal`-motion by design. It is a house pantry-cap warning, not a
gate failure.

## Gate V — final_frame_check.py (frame-level visual QC)

```
$ python3 runtime/qc/final_frame_check.py <reel>
      --mp4 exports/landscape/claude-liam-brutalist-skill-duration-planner.mp4
      --sheet clips/_work/resolved-sheet.json
[gate-v] frames=22 BLOCKER=0 MAJOR=0 → _qc/REPORT.md
```

`_qc/REPORT.md`:

```
# Gate V — visual QC report
Frames sampled: 22  ·  BLOCKER: 0  ·  MAJOR: 0
Clean — no BLOCKER/MAJOR defects. ✓
```

22 frames = 11 beats × (50 %, 85 %) steady-state samples. `_qc/contact_sheet.png`
covers the reel at a glance. Frames were Read via the image-capable tool during
authoring iteration (details in FACTCHECK.md and BUILD-LOG timeline below).

### Repairs made during Gate V iteration

- B01 hesitant writer underfilled 45 % (fontSize 200, 4 lines, mid-typing
  showed only 1 line). Repaired by tightening `lineSpacing` to 1.15, splitting
  into 4 shorter lines (`Video duration / is your output. / Size the script. /
  Hold every beat.`), and setting `charMs: 22` with reduced hesitation. Also
  reworded so the single-token `target → output` swap yields a grammatical
  sentence (avoiding the "a output" bug of an earlier iteration). Final 55 %+
  coverage at both 50 % and 85 %.
- B08 verdict card 53 % coverage. Repaired by expanding to 6 verdict lines with
  slightly longer copy so the ClaudeVerdictArtifact card sizes taller. Final
  55 %+ coverage.

Both repairs were made in the reel's beat sheet — never by loosening Gate V or
running with `--lenient`.

## Compiler final gate — atomic verified.json

The compiler writes an atomic receipt beside the master:

```
$ ls exports/landscape/
claude-liam-brutalist-skill-duration-planner.mp4
claude-liam-brutalist-skill-duration-planner.verified.json
```

`verified.json` pins the master's SHA-256 and every input (`media/B00.mp4 …
B10.mp4`, `mp3/beat-B00.mp3 … B10.mp3`) that fed it. `ready` means the
automated export checks passed — human review is separate.

## FFprobe dimensions and audio decode

```
$ ffprobe -v error -show_entries stream=width,height,codec_type,duration \
      -of default=nw=1 exports/landscape/claude-liam-brutalist-skill-duration-planner.mp4
codec_type=video
width=3840
height=2160
duration=214.125000
codec_type=audio
duration=214.125000
```

Native 4K UHD (16:9). Audio stream present, decoded, same duration as video.

## Motion histogram observation

`reveal` at 7/11 beats (63 %) exceeds the pantry cap (~40 %). This is expected
for a skill-teardown reel: the ILLUSTRATE LAW body beats
(SkillTeardownAnatomy · Pipeline · four Mechanism cards) all use "reveal"
motion (staged element-in animation). Not a gate failure, just a house
pantry-cap warning. Watching the film, the motion reads as varied because the
Anatomy tree, Pipeline flow, and Mechanism quote-blocks reveal in different
ways.

## No captions / subtitles

`captions: false` in metadata. No SRT/VTT/CC track authored, no
transcript slide substituted for a demonstration.

## No paid calls, no publishing

Kokoro is local, free. Remotion is local, free. No API calls. No upload, no
YouTube handoff, no GitHub push. The mp4 lives in
`youtube/brutalist/claude-liam-brutalist-skill-duration-planner/exports/landscape/`
for Bear's viewing.

## What did NOT run (recorded honestly)

- No `pace_check.py` demo. The duration-planner skill's own `pace_check.py`
  would flag below-floor beats in a reel. Running it on the teardown reel
  itself would be circular — the reel *explains* the tool, it isn't a
  reel that *uses* the tool. The B03 pipeline diagram is a hand-drawn
  illustration of the flow the script implements, not a screenshot of its
  output; SOURCES.md is explicit about this.
- No `scripts/type_check.py` GATE T run. That checker is referenced in the
  toolkit's `CLAUDE.md` but not shipped in this snapshot. Instead, visual
  typography was verified by reading frames — see TYPECHECK.md.
- No `art keys`, no `setup --install`, no external clones. Setup is
  demonstrated by reference (github.com/nikbearbrown/brutalist.art) but not
  actually run.

## Files that exist

Landscape master: `exports/landscape/claude-liam-brutalist-skill-duration-planner.mp4`
Landscape receipt: `exports/landscape/claude-liam-brutalist-skill-duration-planner.verified.json`
QC frame audit: `_qc/REPORT.md`, `_qc/contact_sheet.png`
