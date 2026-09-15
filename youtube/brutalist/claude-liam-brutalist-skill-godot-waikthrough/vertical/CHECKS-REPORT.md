# CHECKS-REPORT — Portrait 9:16 Vertical
# slug: claude-liam-brutalist-skill-godot-waikthrough-vertical
# run_id: 4d4269b669dd4b84a92a266e5bff804f
# Re-verified 2026-09-12: SKILL.md §4 changed; §1–§3 unchanged; no beat rebuild required.

## Compile

```
python3 runtime/scripts/compile.py <reel>/vertical --height 3840 --out <reel>/exports/vertical --force
```

Result: PASS — 13/13 slots filled, 269.3s, exports/vertical/claude-liam-brutalist-skill-godot-waikthrough-vertical.mp4

## Gate V — visual QC

Portrait safe area SAFE916 scaled by 2160/1080=2: x=[108,2052], y=[192,3648].
FILL_MIN 0.55 applies to portrait bounding box vs portrait safe area.

```
# Gate V re-run 2026-09-12:
python3 runtime/qc/final_frame_check.py <reel>/vertical --mp4 exports/vertical/…-vertical.mp4
[gate-v] frames=26 BLOCKER=0 MAJOR=0 → vertical/_qc/REPORT.md
```

Five portrait fixes applied before Gate V pass:
1. BrutalistHesitantWriter.tsx: portrait-aware scale patch (height>width ? min(w/1080,h/1920) : min(w/1920,h/1080))
2. GodotDesignBoard.tsx: portrait title top→5.5%h; brand bottom→5.5%h
3. GodotDevWorkbench.tsx: portrait title top→5.5%h; brand bottom→5.5%h
4. B07: WalkerGodotSetup916 → SkillTeardownMechanism916 (flow-mode column overflow in portrait)
5. B10: ClaudeVerdictArtifact916 → SkillTeardownMechanism916 (cream-on-cream underfill ~40%)
B01: fontSize 130→110, charMs:8 added (animation completes before 50% QC sample at 7.78s)

## Scene-level checks

All portrait scenes use native 9:16 variants:
- B00: ClaudeComposerAsk916 — portrait composer layout
- B01: BrutalistHesitantWriter916 — portrait text stack (5 short lines, fontSize:130, lineSpacing:2.6)
- B02: SkillTeardownMechanism916 — portrait mechanism reveal (pipeline swap per feedback)
- B03–B11: Scene variants with 916 suffix or Mechanism916 swaps
- B12: ClaudeTitleOutro916 — portrait outro with slug-seeded mascot

## Gaps and limitations

- `scripts/type_check.py` not present in toolkit; replaced by visual typography review (see TYPECHECK.md)
- Portrait audit is AI visual review only; human viewing/editing required before publication
