# CHECKS-REPORT.md — The hai Skill (landscape 3840×2160)

Run id: `06dfe1bb8b9e4743882466aa3294a5dd` (resumed; original build under `d660d0c9949a427980931d1c010c2f47`)
Final master: `exports/landscape/claude-liam-brutalist-skill-hai.mp4`
Master SHA-256: `d223bbd36847cd86ca8c0b64fcfdd77d609d7240f48c48804d05455d5d016a76` (unchanged from the atomic-verified build; matches `exports/landscape/*.verified.json` and current disk).

## Whole-sheet teaching-arc classification

12 SHOW / 0 justified-HOLD / 0 PUNT-flagged.

- FRAMEWORK ✓ (B02 SkillTeardownAnatomy · B03 SkillTeardownPipeline before any mechanism/example beat)
- WORKED EXAMPLE ✓ (B02 folder tree derived from actual `hai-example-reel` scaffold output in `demo/`; B06 CLI exercise beat cites the five-part schema evidence in FACTCHECK)
- FALSIFIABILITY ✓ (B08 — real voice-field disagreement across three source files, verified verbatim in `FACTCHECK.md`)
- SCAFFOLDED TASK ✓ (B10 — paste-ready prompt + three-line rubric)
- BOOKENDS ✓ (B00 ClaudeComposerAsk cold open · B09 ClaudeVerdictArtifact · B10 Your Turn composer · B11 ClaudeTitleOutro title restate)
- NO-SOURCE-NO-VERDICT ✓ (every mechanism beat carries the SKILL.md quote it's judging; B08 cites brands/hai.md)

## Gate V — visual QC (final_frame_check.py)

Command:
```
python3 runtime/qc/final_frame_check.py \
  <reel> --mp4 <candidate> --sheet <resolved-sheet>
```

Final result (from `_qc/REPORT.md`):
```
Frames sampled: 24  ·  BLOCKER: 0  ·  MAJOR: 0
Clean — no BLOCKER/MAJOR defects. ✓
```

Iteration log (root cause: hesitant writer type size on 16:9 canvas):

- Attempt 1 (fontSize=162, 3 lines): B01 underfill 45% (min 55%) → MAJOR ×2. Fix: added a line + bumped fontSize.
- Attempt 2 (fontSize=190, 4 lines): B01 underfill 48% → MAJOR ×2. Fix: added a fifth line and reduced fontSize.
- Attempt 3 (fontSize=175, 5 lines): B01 top/bottom edge-bleed → BLOCKER ×2. Fix: reduced fontSize to keep 5 lines inside safe.b.
- Attempt 4 (fontSize=148, 4 lines, longer per-line phrasing): CLEAN.

Root cause: this text is shorter than the guests episode's baseline text, so the 162 default under-fills at 16:9 unless line count + per-line width both increase. Fix belongs in the beat sheet's props, not in the checker.

## Motion histogram (compile.py)

```
reveal: 8/12 (66%)  — over the ~40% pantry cap
type-on: 3/12
hold:    1/12
```

**Analysis of the warning.** The 8 `reveal` beats are the 4-beat MECHANISM run (B04–B07) plus the FALSIFIABILITY (B08), the two FRAMEWORK beats (B02, B03) and the VERDICT (B09). Every one of them uses a *different* SkillTeardown-family composition or ClaudeVerdictArtifact — not the same visual scheme repeated. The `motion` field in the sheet is coarse-grained (reveal/type-on/hold/…); the actual on-screen action varies by component (SkillTeardownAnatomy stagger-in on folder rows; SkillTeardownPipeline INPUT→phases→OUTPUT node stagger; SkillTeardownMechanism eyebrow→heading→body→quote→verdict pill; ClaudeVerdictArtifact heading→lines). Diversifying the coarse motion label without rebuilding six scenes would only trade an honest label for a false one. Documented as a warning, not resolved by relabeling — a future scene refactor should split `reveal` into finer verbs.

## Type/scene sanity — narration alignment

Every beat's `actual_duration_s` (from Kokoro) is written back into `beat_sheet.json`. compile.py then holds each source clip to the audio's duration by `extend_clip_to_duration` (last frame held). Verified:

- B00 audio 15.21s → clip padded to 15.25s (0.04s tail hold — inaudible).
- B01 audio 16.04s → clip padded to 16.04s (native match; hesitant writer's timeline runs long enough).
- All other beats match audio to within ±0.05s (frame-quantized at 24fps).

Total master duration: 280.125s (ffprobe). Sum of `actual_duration_s`: 279.94s. Delta: 0.19s across 12 tail holds. Acceptable.

## ffprobe (post-compile)

```
codec_name=h264
width=3840
height=2160
r_frame_rate=24/1
duration=280.125000

codec_name=aac
duration=280.125000
```

Native 4K, 24fps, H264 video + AAC audio decoded — both streams verified.

## Frame audit (Read PNGs directly)

- `_qc/contact_sheet.png` — Gate V-generated 12-tile contact sheet. Read and inspected. Every beat legible; palette consistent; no unwanted captions; outro shows `The hai Skill.` with slug-seeded mascot. The outro handle overlay is `@NikBearBrown` (hardcoded in the shared `ClaudeTitleOutro` scene per `OUTRO-LOCK.md`); channel identity is carried via the composer `folderLabel` on B00/B10 (`@HumanitariansAI`) and the beat sheet `metadata.channel` field. Same handling as every other Brutalist playlist episode.
- `_qc/verify-tile.png` — additional 12-tile at 1/24Hz sampling. Read and inspected. Confirms no title-safe bleed on any beat, no overlap, no orphaned artifacts.
- `_qc/b01-pair.png` — targeted pair of B01 at t=20s and t=29s (mid + late). Read and inspected. Correction landed (both frames show `forks`, not `reformats`); serif type well inside SAFE; caret visible at line end.

## Fresh proof frames for run 06dfe1bb (this invocation)

Because the prior review file was rejected as "frame evidence missing/stale", I re-extracted five frames directly from the current landscape MP4 with `ffmpeg -ss <t> -frames:v 1`. Each frame was hashed and read with the image-capable Read tool. Combined strip at `_qc/proof-run-06dfe1bb.png`.

| t (s) | Beat expected | What I observed |
| --- | --- | --- |
| 5   | B00 ClaudeComposerAsk cold open | "The hai Skill" title, "Hello, Liam" greeting, README hai-skill ask; @HumanitariansAI folder label. |
| 60  | B03 SkillTeardownPipeline | "Six steps. One shape." heading over the pipeline diagram. |
| 140 | B06 SkillTeardownMechanism (CLI exercise) | "The CLI exercise." with the five-part-schema quote block. |
| 220 | B09 ClaudeVerdictArtifact | "A fork. Not a re-skin." verdict card with sub-line bullets. |
| 275 | B10/B11 handoff (Your Turn composer → outro) | "Fork one of your reels without shipping it" composer / "Your Turn" greeting, paste-ready prompt. |

Video hash (`d223bbd3…`) unchanged from the compiler receipt, so the same content the earlier reviewer certified is still on disk; the fresh proof frames confirm the content matches the beat sheet.

## Static gates NOT run for this cut

- `scripts/type_check.py` (GATE T) — not present in this snapshot of the isolated toolkit. See `TYPECHECK.md` for the actual typography inspection substituted here (image-level review of every rendered frame).
- `runtime/qc/beat_lint.py` / static-scene checks — the compile.py pipeline invokes the shape/skin lints internally and emits `skin_warnings` in `metadata.build` (empty for this cut). No additional standalone lint script is required by the current compile.py control flow.

## Approvals / gates

`approvals: {}`. This is a claude-liam Teardown, no third-party subject and no human-signed review file required. No `GATE G` / `GATE N` in scope.

## Conclusion

Landscape master (3840×2160, 280.125s, H264+AAC, atomic-verified) is complete. Gate V clean after four iterations on B01 hesitant-writer sizing. Every teaching-arc item is satisfied. Human viewing/editing is next.
