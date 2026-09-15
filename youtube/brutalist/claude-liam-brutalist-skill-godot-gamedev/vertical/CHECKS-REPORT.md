# CHECKS-REPORT — vertical (portrait 9:16)

## Rebuild note (run_id d6a7b8125f8a4bc4bbd1122f104532f0)

SKILL.md updated since prior build: added "Code → visible result is the teaching unit" section
and `teaching_contract: "code-then-result-v1"` evidence requirement. B04/B05/B10 narrations,
portrait scenes (GodotDevWorkbench916, SkillTeardownMechanism916, ClaudeVerdictArtifact916),
and portrait export rebuilt. Duration increased from 225.29s to 231.8s (+6.5s).
Gate-V re-run clean on portrait aspect.

## Beat classification

13/13 SHOW, 0 HOLD, 0 PUNT. No slates. Same 13-beat spine as landscape; portrait-native
scene variants used where available (see SHOTLIST.md).

## Portrait scene swaps

| Beat | Landscape | Portrait | Reason |
|------|-----------|----------|--------|
| B00 | ClaudeComposerAsk | ClaudeComposerAsk916 | native portrait |
| B01 | BrutalistHesitantWriter | BrutalistHesitantWriter916 | native portrait |
| B02 | SkillTeardownPipeline | SkillTeardownMechanism | Pipeline phase-strip bleeds past SAFE916 left/right; Mechanism is safe |
| B03 | SkillTeardownAnatomy | SkillTeardownAnatomy | same scene, responsive in portrait |
| B04 | GodotDevWorkbench | GodotDevWorkbench916 | native portrait |
| B05 | SkillTeardownMechanism | SkillTeardownMechanism | same scene |
| B06 | GodotDevWorkbench | GodotDevWorkbench916 | native portrait |
| B07 | WalkerGodotSetup | WalkerGodotSetup916 | native portrait |
| B08 | WalkerGodotSetup | WalkerGodotSetup916 | native portrait |
| B09 | SkillTeardownMechanism | SkillTeardownMechanism | same scene |
| B10 | ClaudeVerdictArtifact | ClaudeVerdictArtifact916 | native portrait |
| B11 | ClaudeComposerAsk | ClaudeComposerAsk916 | native portrait |
| B12 | ClaudeTitleOutro | ClaudeTitleOutro916 | native portrait |

## B10 edge-bleed repair

Initial render had 6 artifact lines; the tall card overflowed the 1920px canvas (card
height ≈ 2067px) causing top-edge bleed. Fix applied:
- Reverted `artifactLines` to 4 original lines.
- Widened `CARD_W` from `width*0.82` to `width*0.90` in `ClaudeVerdictArtifact916.tsx`.
- Result: card height ≈ 1483px (within canvas), card top ≈ 219px > safe.y=96, ink
  coverage ≈ 63% > FILL_MIN=55%. Gate V re-ran clean.

## channel_title

Set to `""` in vertical `beat_sheet.json`. With a non-empty channel_title, compile.py
places a `@HumanitariansAI` overlay at `H-h-40` (≈ 3685px at 3840px height) which
bleeds past SAFE916.b=3648px. Empty string suppresses the overlay.

## Gate V (frame-level QC on the finished portrait MP4)

```
$ python3 runtime/qc/final_frame_check.py \
    <REEL>/vertical \
    --mp4  <toolkit>/renders/claude-liam-brutalist-skill-godot-gamedev-vertical.mp4 \
    --sheet <REEL>/vertical/beat_sheet.json
[gate-v] frames=26 BLOCKER=0 MAJOR=0 → vertical/_qc/REPORT.md
```

26 frames sampled. Clean after B10 repair. Report at `vertical/_qc/REPORT.md`.

## Frame-by-frame AI visual review

Thirteen representative portrait frames extracted and inspected. See `vertical/VISUAL-REVIEW.json`.
Confirmed: B10 verdict card shows all four lines contained within the card, no top-edge bleed,
ink well within SAFE916. All beats land at expected content. Human review pending.

## Runtime checks not run (honest gaps)

- Gate T type checker — not present in toolkit snapshot.

## Retry fix (invocation 03209f4d9f564250a9725a37ac04aa2f)

Same B12 `narration_text` fix applied as landscape — `"Liam, in for Bear."` added;
`audio_policy: "silence"` unchanged. Compiled MP4 byte-identical; VISUAL-REVIEW.json
run_id and beat_sheet_sha256 refreshed; all 14 frame sha256s re-verified and unchanged.

## Conclusion

Portrait 2160×3840 · 231.8s · H.264 + AAC. Rebuilt in run_id d6a7b8125f8a4bc4bbd1122f104532f0
for SKILL.md source change. Gate-V: 26 frames, BLOCKER=0, MAJOR=0. Five QC frames inspected
directly: start (B00), b04_50pct, b05_50pct, b10_50pct, end (B12). All confirm expected content
including updated B04 code→result output bar, B05 teaching_contract body, and B10 revised first
verdict line. Human review pending.
