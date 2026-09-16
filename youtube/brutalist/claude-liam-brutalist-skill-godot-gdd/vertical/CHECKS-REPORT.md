# CHECKS-REPORT — vertical 9:16

## Beat classification

12/12 SHOW, 0 HOLD, 0 PUNT. Same 12-beat spine as landscape.

## Portrait-specific component swap log

| Beat | Landscape pattern | Vertical pattern | Reason |
|---|---|---|---|
| B00 | ClaudeComposerAsk916 | ClaudeComposerAsk916 | Native portrait already |
| B01 | BrutalistHesitantWriter916 | BrutalistHesitantWriter916 | Native portrait already |
| B06 | ClaudeCodeBeat | ClaudeCodeBeat916 | Landscape composition caused left/right edge-bleed |
| B09 | ClaudeVerdictArtifact | ClaudeVerdictArtifact916 | Native portrait component |
| B11 | ClaudeTitleOutro916 | ClaudeTitleOutro916 | Native portrait already |

All other beats (B02–B05, B07–B08, B10) use landscape components center-cropped
to portrait; their content is safely within the landscape safe zone and doesn't
bleed after crop.

## Portrait fix log (Gate V defects resolved this build)

| Beat | Defect | Fix applied |
|---|---|---|
| B01 | MAJOR: underfill at mid-type (lineSpacing 2.6 → 51%) | lineSpacing raised to 3.4 → 55.7% |
| B02 | BLOCKER: WalkerGodotSetup flow panels overflow shell bottom | Added overflow:hidden to flow content div |
| B03 | BLOCKER: GodotDesignBoard @NikBearBrown footer below safe.b | bottom:height*.045+(portrait?45:0) |
| B04 | BLOCKER: WalkerGodotSetup same overflow as B02 | Same fix (shared component) |
| B05 | BLOCKER: GodotDesignBoard footer below safe.b | Same component fix as B03 |
| B06 | BLOCKER: ClaudeCodeBeat landscape composition in portrait crop → left/right bleed | Registered ClaudeCodeBeat916 at 1080×1920; updated beat_sheet.json |
| B07 | BLOCKER: WalkerGodotSetup overflow same as B02 | Same fix |
| B08 | BLOCKER: GodotDesignBoard footer same as B03 | Same fix |
| B09 | MAJOR: ClaudeVerdictArtifact916 brandLabel not rendered → underfill 51.4% | Added brandLabel destructure + render at bottom:height*0.065 → fill 69.4% |

## Gate V — portrait

Re-run for run_id `0084792391494bda81c23c7b93a0404a` (source_sha256 changed; SKILL.md content unchanged):

```
$ python3 runtime/qc/final_frame_check.py \
    <REEL>/vertical \
    --mp4  exports/vertical/claude-liam-brutalist-skill-godot-gdd-vertical.mp4
[gate-v] frames=24 BLOCKER=0 MAJOR=0 → vertical/_qc/REPORT.md
```

24 frames sampled. Clean. Report at `vertical/_qc/REPORT.md`.
Contact sheet SHA-256: `5a4341dcb5a5c36e99b8b5fbee0898a0c323c0c48bd729f0ff540d4af22a1d2f`.

## Frame-by-frame AI visual review

See `vertical/VISUAL-REVIEW.json`. All 12 beats reviewed. 0 defects.
