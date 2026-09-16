# CHECKS-REPORT — landscape

## PROOF GATE (per `skills/make/ai-explainer/SKILL.md` § "PROOF GATE")

- Beats: 12 total.
- Classification (per `skills/make/nopunt` § "SHOW / HOLD / CARD"):
  - 12 SHOW · 0 justified-HOLD · 0 PUNT-flagged
- Teaching arc:
  - FRAMEWORK ✓ (B02 — the case-branch dispatcher, one exec)
  - WORKED EXAMPLE ✓ (B06 `--dry-run` · B07 output artifacts)
  - FALSIFIABILITY ✓ (B08 — four principled drops, each with the rule that dropped it)
  - SCAFFOLDED TASK ✓ (B10 — Your Turn composer, prompt read aloud)
  - BOOKENDS ✓ (B00 `ClaudeComposerAsk` cold open · B09 `ClaudeVerdictArtifact` · B10 HANDOFF · B11 `ClaudeTitleOutro`)
  - NO-SOURCE-NO-VERDICT ✓ (every claim in B09 traces to `art:64-66` or `build_icon_set.py`; see FACTCHECK.md)

## GATE V — `final_frame_check.py`

```
$ python3 runtime/qc/final_frame_check.py <reel> --mp4 <candidate.mp4>
[gate-v] frames=24 BLOCKER=0 MAJOR=0 → <reel>/_qc/REPORT.md
```

- Frames sampled at 50 % and 85 % of every beat (24 total).
- Contact sheet: `_qc/contact_sheet_landscape.png`. Individual PNGs under
  `_qc/frames_landscape/`. Read via the image-capable Read tool — text is
  legible on every beat, no edge-bleed, no clipping, no unresolved slates,
  cream ground consistent, terracotta spark discipline preserved (one accent
  per beat).
- No iterations needed on landscape — the first render passed gate V on the
  first compile. All follow-up work was on vertical portrait layout only.

## Audio decode

```
$ ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,duration,channels,sample_rate -of csv=p=0 <mp4>
aac,48000,2,253.041000
```

- 12 Kokoro `am_onyx` MP3s ledgered as ground truth; per-beat durations sum
  to 253.04 s of narration + 0.00 s outro tail = 253.04 s stream.

## Video

```
$ ffprobe -v error -select_streams v:0 -show_entries stream=width,height,duration,codec_name,r_frame_rate -of csv=p=0 <mp4>
h264,3840,2160,24/1,253.041667
```

- 3840×2160 (native 4K landscape). 24 fps.
- Final SHA-256: `b1af8bf0641cc96b51286f158752f44f726cc4b745f2d1c40752e5c320ea9d62`

## Motion histogram (compiler notice, not a failure)

```
code-cascade:7  type-on:2  hesitant-type:1  artifact-in:1  outro-card:1
WARNING: 'code-cascade' carries 7/12 beats (58%) — over the ~40% pantry cap
```

- WARNING in the current compiler, not a blocker (the compile succeeded and
  the final gate passed). Rationale: this is a command teardown, and command
  teardowns are fundamentally about code — showing the actual dispatcher,
  the raw upstream corpus (`du -sh` table), the four rules verbatim from the
  docstring, the 44-pt math, the `--dry-run` output, the shipped artifacts,
  and the four principled drops. Each of the seven `code-cascade` beats is a
  DIFFERENT code artifact, not a repeated scheme. The reference episodes
  `claude-liam-brutalist-command-help` and `-icons` carry the same warning
  (58% code-cascade) and shipped. Logged as a minor limitation for the human
  reviewer, not a defect to repair.

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

## Conclusion

Landscape gate log: PROOF GATE ✓ · GATE V ✓ (0 BLOCKER / 0 MAJOR) ·
compile ✓ · atomic-verify ✓ · dimensions verified 3840×2160 · audio
verified · every claim traced in FACTCHECK.md. Ready for human review.
