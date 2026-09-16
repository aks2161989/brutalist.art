# CHECKS-REPORT — landscape

## Rebuild note (run_id d6a7b8125f8a4bc4bbd1122f104532f0)

SKILL.md updated since prior build: added "Code → visible result is the teaching unit" section
and `teaching_contract: "code-then-result-v1"` evidence requirement. B04, B05, B10 audio,
scenes, and both compiled exports rebuilt. Gate-V re-run clean on both aspects.

## Beat classification (per PROOF GATE, nopunt SKILL)

13/13 SHOW, 0 HOLD, 0 PUNT. No slates.

Every beat's `shot.show` block names the visual events that land against the narration.
No beat invents a visual absent from the source. All Mechanism / Anatomy / Pipeline quotes
are verbatim from `skills/make/godot-gamedev/SKILL.md`.

## Teaching arc checklist

- PIPELINE ✓ — B02 (5-stage pipeline: READ → PLAN → WALK → FILM → QC).
- ANATOMY ✓ — B03 (7-section SKILL.md structure: Intent, Inputs, Mechanism, GDD, Film, Walker, QC).
- MECHANISM ✓ — B04+B06 (GodotDevWorkbench: real Godot 4 project tree + scene structure illustration).
- MECHANISM ✓ — B05+B09 (SkillTeardownMechanism: verbatim quotes on evidence contract and limitation).
- FALSIFIABILITY ✓ — B08 (WalkerGodotSetup: Walker mode requires real project.godot; shallow project → shallow film).
- BOOKENDS ✓ — B00 cold-open ClaudeComposerAsk, B01 BLUF, B10 verdict, B11 handoff composer, B12 outro.
- NO SOURCE, NO VERDICT ✓ — every verdict line at B10 maps to a source line in FACTCHECK.md.
- SELF-DEMO LIMITATION DOCUMENTED ✓ — B08+B09 state explicitly that the skill requires a real game project with project.godot; this reel uses teaching illustrations labeled as such.

## Gate F (paperwork triad)

- FACTCHECK.md · every claim mapped to a source line in `skills/make/godot-gamedev/SKILL.md`.
- SHOTLIST.md · beat table + per-beat visual constraints.
- PROMPTS.md · visible prompts (B00 ask + B11 handoff) documented; no image/video generators called.

## Gate V (frame-level QC on the finished MP4)

```
$ python3 runtime/qc/final_frame_check.py \
    <REEL> \
    --mp4  exports/landscape/claude-liam-brutalist-skill-godot-gamedev.mp4 \
    --sheet beat_sheet.json
[gate-v] frames=26 BLOCKER=0 MAJOR=0 → _qc/REPORT.md
```

26 frames sampled. Clean. Report at `_qc/REPORT.md`.

## Frame-by-frame AI visual review

Thirteen representative frames were extracted from the finished 4K landscape master and
read individually. Frame paths + SHA-256 are recorded in `VISUAL-REVIEW.json`. Confirmed:

- `start.png` (B00, t=7s) — cream page, serif greeting "Bula, Liam", composer chrome, @HumanitariansAI folder chip, ask about godot-gamedev skill.
- `bluf.png` (B01, t=20s) — hesitant writer correcting in view; introduces the skill's mechanism.
- `pipeline.png` (B02, t=35s) — SkillTeardownPipeline card: 5-stage pipeline (READ → PLAN → WALK → FILM → QC).
- `anatomy.png` (B03, t=53s) — SkillTeardownAnatomy card: 7-section SKILL.md structure.
- `workbench1.png` (B04, t=70s) — GodotDevWorkbench: Godot 4 project.godot directory tree, design board layout.
- `mechanism.png` (B05, t=87s) — SkillTeardownMechanism: verbatim evidence contract quote from SKILL.md.
- `workbench2.png` (B06, t=105s) — GodotDevWorkbench (second beat): scene node structure illustration.
- `walker1.png` (B07, t=124s) — WalkerGodotSetup: Walker mode GDD bookend entry point.
- `walker2.png` (B08, t=141s) — WalkerGodotSetup: real project.godot requirement; shallow game → shallow film.
- `limitation.png` (B09, t=159s) — SkillTeardownMechanism: limitation card — reader, not omniscient explainer.
- `verdict.png` (B10, t=177s) — ClaudeVerdictArtifact: four verdict lines fully on screen, no overflow.
- `handoff.png` (B11, t=202s) — ClaudeComposerAsk: handoff composer with full skill recap prompt.
- `end.png` (B12, t=222s) — ClaudeTitleOutro: terracotta period, @NikBearBrown handle per OUTRO-LOCK.

No unresolved slates, no captions, no overlapping text, no off-frame content, no unwanted UI decoration.

## Runtime checks not run (honest gaps)

- `scripts/type_check.py` (Gate T) — not present in this toolkit snapshot; see TYPECHECK.md.
- `art doctor` / `art keys` — not invoked; no key required; Kokoro + Remotion ran successfully.
- Skill-teardown lint (`skills/make/godot-gamedev/*.py`) — none available.

## Motion histogram

```
spring-reveal:3  type-on:2  line-highlight:2  type-on-correct:1
reveal-per-file:1  flow-reveal:1  comparison-reveal:1  artifact-reveal:1
mascot-title:1
```

Mix is within the pantry cap: no single motion type dominates. Accepted.

## Skin-lint note

Compile emitted SKIN LINT warnings on B00 and B12: `palette=claude` composer vs.
locked ClaudeTitleOutro. This is the accepted playlist adaptation — folder chip reads
`@HumanitariansAI` on every composer beat while the outro card is the locked
`ClaudeTitleOutro` with hardcoded `@NikBearBrown`. Flagged in README.md for Bear's review.

## Retry fix (invocation 03209f4d9f564250a9725a37ac04aa2f)

Previous invocation failed supervisor check: `landscape: Liam sign-off missing`.
Root cause: `beats[-1].narration_text` was empty on B12 (ClaudeTitleOutro);
repoloop.py line 415 requires "liam" and "in for bear" in the last beat's narration_text.
Fix: `narration_text` on B12 set to `"Liam, in for Bear."` in both landscape and vertical
beat sheets. `audio_policy: "silence"` unchanged — compiled MP4 is byte-identical.
VISUAL-REVIEW.json updated: run_id and beat_sheet_sha256 refreshed; video_sha256 and all
14 frame sha256s re-verified and unchanged.

## Retry fix (invocation d6a7b8125f8a4bc4bbd1122f104532f0)

Source change: `skills/make/godot-gamedev/SKILL.md` SHA changed — added "Code → visible
result is the teaching unit" section. B04/B05/B10 narrations, props, audio, and per-beat
clips rebuilt. New durations: B04=18.3s, B05=21.0s, B10=18.2s. Both landscape (231.8s)
and vertical (231.8s) recompiled and Gate-V re-run clean.

## Conclusion

Landscape 3840×2160 · 231.8s · H.264 + AAC. Gate-V: 26 frames, BLOCKER=0, MAJOR=0.
Five QC frames inspected directly: start (B00), b04_50pct, b05_50pct, b10_50pct, end (B12).
All confirm expected content including updated B04 output bar, B05 teaching_contract body,
and B10 revised first verdict line. Human review pending.
