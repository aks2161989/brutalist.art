# CHECKS-REPORT — landscape

## PROOF GATE (per skills/make/ai-explainer/SKILL.md § "PROOF GATE")

- Beats: 12 total.
- Classification (per skills/make/nopunt § "SHOW / HOLD / CARD"):
  - 12 SHOW  ·  0 justified-HOLD  ·  0 PUNT-flagged
- Teaching arc:
  - FRAMEWORK ✓ (B02 — the case-branch dispatcher, one exec)
  - WORKED EXAMPLE ✓ (B05 "money" · B06 --check/--show · B07 --brands)
  - FALSIFIABILITY ✓ (B08 — "quantum entanglement" miss, exit 0)
  - SCAFFOLDED TASK ✓ (B10 — Your Turn composer, prompt read aloud)
  - BOOKENDS ✓ (B00 ClaudeComposerAsk cold open · B09 ClaudeVerdictArtifact · B10 HANDOFF · B11 ClaudeTitleOutro)
  - NO-SOURCE-NO-VERDICT ✓ (every claim in B09 traces to art:60-63 or icon_search.py; see FACTCHECK.md)

## GATE V — final_frame_check.py

```
$ python3 runtime/qc/final_frame_check.py <reel> --mp4 <candidate.mp4>
Frames sampled: 24  ·  BLOCKER: 0  ·  MAJOR: 0
Clean — no BLOCKER/MAJOR defects. ✓
```

- Frames sampled at 50% and 85% of every beat (24 total per aspect).
- Contact sheet: `_qc/contact_sheet.png`. Read via the image-capable Read
  tool — text is legible on every beat, no edge-bleed, no clipping, no
  unresolved slates, cream ground consistent, terracotta spark discipline
  preserved (one accent per beat).
- Iterations: B01 fontSize tuned from 250 → 340 (bleed) → 280 (clean, 55%
  cover); B09 artifactHeading widened + artifactLines extended from 5 → 7
  lines to clear the underfill threshold. Every change re-rendered from
  scratch via `remotion_scenes.py --force`.

## Audio decode

```
$ ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,duration,channels,sample_rate -of csv=p=0 <mp4>
aac,48000,2,199.333000
```

- 12 Kokoro `am_onyx` MP3s ledgered as ground truth; per-beat durations sum
  to 199.14s of narration + 0.19s outro tail = 199.33s stream.

## Video

```
$ ffprobe -v error -select_streams v:0 -show_entries stream=width,height,duration,codec_name,r_frame_rate -of csv=p=0 <mp4>
h264,3840,2160,24/1,199.291667
```

- 3840×2160 (native 4K landscape). 24 fps.

## Motion histogram (compiler notice, not a failure)

```
code-cascade:7  type-on:2  hesitant-type:1  artifact-in:1  outro-card:1
WARNING: 'code-cascade' carries 7/12 beats (58%) — over the ~40% pantry cap
```

- This is a WARNING in the current compiler, not a blocker (the compile
  succeeded and the final gates passed). Rationale: this is a command
  teardown, and command teardowns are fundamentally about code — showing
  the actual case branch, the JSON index, the ranker, five worked outputs
  (money, --check/--show, --brands, and the miss). Each of the seven
  `code-cascade` beats is a DIFFERENT code artifact, not a repeated
  scheme. The reference episode `claude-liam-brutalist-command-help`
  carried the same warning (58% code-cascade) and shipped. Logged as a
  minor limitation for the human reviewer, not a defect to repair.

## Motion / captions

- No captions, no karaoke, no burned-in transcript (per playlist contract).
- Every beat is a Remotion scene registered in Root.tsx; no hand-rolled
  `npx remotion render`; no bypass of fit/QC gates.

## Runtime checks not run

- `scripts/type_check.py` — not present in this toolkit snapshot. See
  TYPECHECK.md.
- `scripts/kerning/*` — the kerning skill referenced in
  `ai-explainer/SKILL.md` is not shipped in this cut. TYPECHECK.md
  distinguishes actual visual typography review (done) from the absent
  legacy checker.

## Re-verification — 2026-09-12 (run_id 9c6d30d53da2466ea7266f53a51cf4ef)

Source SHA changed from `a83e2aa2…` to `0959b926…`; changes were to
SKILL.md files and unrelated Remotion components (BarChart, RequireReport,
Root). No beat content, scene components, audio, or compiled clips changed.
Gate V re-run: frames=24 BLOCKER=0 MAJOR=0. Contact sheet re-inspected
visually — all 12 beats clean, same conclusions as original review.
Video sha256 `e96e46dd…` unchanged; build-state.json still valid.

## Conclusion

Landscape gate log: PROOF GATE ✓ · GATE V ✓ (0 BLOCKER / 0 MAJOR) ·
compile ✓ · atomic-verify ✓ · dimensions verified 3840×2160 · audio
verified · every claim traced in FACTCHECK.md. Ready for human review.
