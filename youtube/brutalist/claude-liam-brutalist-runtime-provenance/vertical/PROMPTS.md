# Prompts — Brutalist Utility: provenance.py
# Episode 52 · run_id: 9acc8c13d5d443968a1aed379ed68b66

## Handoff prompt (B10 — Your Turn)

The viewer is prompted to paste this into Claude Code:

```
Open my reel's beat_sheet.json. Run:
  python3 runtime/scripts/provenance.py <reel>/
For each Capture? beat, read its shot block.
Add: build.filled_by = 'remotion:|manim:|capture:|human:' + one note.
Save beat_sheet.json and commit the change.
```

**Why this prompt is worth running:** Most reels have Capture? beats where the sheet doesn't record who filled the slot. This prompt forces you to read the beat sheet and make that attribution explicit, one beat at a time. After running it, re-running provenance.py should show a shorter Capture? list — that's the testable outcome.

**Expected artifact:** Updated beat_sheet.json with `build.filled_by` fields on previously ambiguous beats. Narration reads the prompt aloud at B10.

---

## Scene queries run before authoring (GATE L compliance)

```bash
./art scenes "audio fingerprint classification provenance tracking"
# → 8 candidates, none specific to provenance. Confirmed no existing component.

./art scenes "file classification pipeline flow beat"
# → 8 candidates. SkillTeardownPipeline (score 6.0) confirmed usable for 3-layer flow.

./art scenes --check ClaudeComposerAsk        # RENDERABLE ✓
./art scenes --check ClaudeComposerAsk916      # RENDERABLE ✓
./art scenes --check BrutalistHesitantWriter   # RENDERABLE ✓
./art scenes --check BrutalistHesitantWriter916 # RENDERABLE ✓
./art scenes --check SkillTeardownPipeline     # RENDERABLE ✓
./art scenes --check ClaudeCodeBeat            # RENDERABLE ✓
./art scenes --check SkillTeardownMechanism    # RENDERABLE ✓
./art scenes --check SkillTeardownAnatomy      # RENDERABLE ✓
./art scenes --check FormBCard                 # RENDERABLE ✓
./art scenes --check FormACard                 # RENDERABLE ✓
./art scenes --check ClaudeVerdictArtifact     # RENDERABLE ✓
./art scenes --check ClaudeVerdictArtifact916  # RENDERABLE ✓
./art scenes --check ClaudeTitleOutro          # RENDERABLE (locked @NikBearBrown — not used)
./art scenes --check HaiTitleOutro             # NOT RENDERABLE → created in this build
./art scenes --check HaiTitleOutro916          # NOT RENDERABLE → created in this build
```

Both HaiTitleOutro and HaiTitleOutro916 created as new Remotion scenes in the isolated toolkit (runtime/remotion/src/scenes/) and registered in Root.tsx. `./art scene-index` run after registration. Both confirmed RENDERABLE.

---

## Template misses (PUNT log)
None. All beats classified as SHOW or CARD. No unresolved slates.
