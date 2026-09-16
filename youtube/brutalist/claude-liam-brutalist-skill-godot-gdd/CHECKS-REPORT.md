# CHECKS-REPORT — landscape

## Beat classification (per PROOF GATE, nopunt SKILL)

12/12 SHOW, 0 HOLD, 0 PUNT. No slates.

Every beat's `shot.show` block names the visual events that land against the narration.
No beat invents a visual absent from the source. All GodotDesignBoard / WalkerGodotSetup
quotes are verbatim from `skills/make/godot-gdd/SKILL.md`.

## Teaching arc checklist

- PIPELINE ✓ — B02 (four-stage pipeline: Read → Map → Visualize → Assemble).
- ANATOMY ✓ — B03 (GodotDesignBoard cards: SKILL.md excerpt + four coverage cards).
- MECHANISM ✓ — B05 (GodotDesignBoard flow: causal chain cards with arrows).
- MECHANISM ✓ — B06 (ClaudeCodeBeat: checker command, VERIFIES block, CANNOT VERIFY block).
- FALSIFIABILITY ✓ — B08 ("A proposal is not a passing test" stress-tests the framework).
- BOOKENDS ✓ — B00 cold-open ClaudeComposerAsk, B01 BLUF, B09 verdict, B10 handoff, B11 outro.
- NO SOURCE, NO VERDICT ✓ — every verdict line at B09 maps to a source line in FACTCHECK.md.

## Gate F (paperwork triad)

- FACTCHECK.md · every claim mapped to a source line in `skills/make/godot-gdd/SKILL.md`.
- SHOTLIST.md · beat table + per-beat visual constraints.
- PROMPTS.md · visible prompts (B00 ask + B10 handoff) documented; no image/video generators called.

## Gate V (frame-level QC on the finished MP4)

Re-run for run_id `0084792391494bda81c23c7b93a0404a` (source_sha256 changed; SKILL.md content unchanged):

```
$ python3 runtime/qc/final_frame_check.py \
    <REEL> \
    --mp4  exports/landscape/claude-liam-brutalist-skill-godot-gdd.mp4
[gate-v] frames=24 BLOCKER=0 MAJOR=0 → _qc/REPORT.md
```

24 frames sampled. Clean. Report at `_qc/REPORT.md`.
Contact sheet SHA-256: `6c0b0785ca426d2de68000ea33a59d816756ee1f6485197035cce4d28cc25ebe`.

## Frame-by-frame AI visual review

See `VISUAL-REVIEW.json`. All 12 beats reviewed. 0 defects.

## SKIN LINT warnings (expected)

```
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916'...
[art] SKIN LINT: B11: palette=claude but the outro is 'ClaudeTitleOutro916'...
```

Both warnings are expected behavior — the `*916` suffix components are the portrait-aware
variants registered in Root.tsx. Landscape compilation correctly uses the base variants.
The SKIN LINT fires because the beat_sheet carries the `916` component name from the
vertical sheet; this is a false-positive the linter emits whenever the pattern name
differs from the skin's expected cold-open/outro component. No action needed.
