# CHECKS-REPORT — vertical 9:16 build

Reel: `The ai-explainer Skill` (portrait companion) · slug `claude-liam-brutalist-skill-ai-explainer-vertical`
Run: 2026-09-08 · This invocation `run_id` `5d2d09528cd0403dac54ed33498aef23`.

The portrait companion is a NATIVE 9:16 build, NOT an upscaled crop of the landscape master. Every scene is a purpose-built portrait composition registered in the isolated toolkit's Remotion project (see the `*916` compositions in `Root.tsx`).

## What was compiled

- Composition: registered 9:16 comps, rendered at `--scale=2` → true `2160 × 3840` (4K portrait).
- Frame rate: 24 fps · Video: h264 `yuv420p` crf 16 · Audio: AAC stereo, per-beat MP3 preserved (source audio never re-generated during compile).
- Duration: 186.916s master (matches landscape — same script, same audio).
- 11/11 beats filled from `media/<BID>.mp4` — 0 slates.

## Runtime checks that ran on THIS aspect

- `runtime/qc/beat_lint.py` and `runtime/qc/gate_shape.py` — invoked by `compile.py` as the fellows preflight (both required, no bypass).
- `runtime/qc/final_frame_check.py` (Gate V) — invoked against the compiled candidate before the atomic move to `exports/vertical/`. Uses `SAFE916 = {x:54, y:96, r:1026, b:1824, w:972, h:1728}` scaled to the actual 2160-wide frame.
- `runtime/scripts/compile.py::verify_output` — decodes video + audio streams, checks duration matches `sum(beat.render_duration_s)` within tolerance, and writes the atomic `.verified.json`.

## Actual commands run (portrait re-render sequence)

The previous attempt left `media/B00.mp4`…`media/B10.mp4` in place; this attempt regenerated the eight beats whose scene components changed.

```
export ART_HOME=<toolkit>
export ART_CHROME=$ART_HOME/runtime/scripts/chrome-wrap.sh
export ART_CHROME_MODE=chrome-for-testing
python3 runtime/scripts/remotion_scenes.py <reel>/vertical --only B01 --force
python3 runtime/scripts/remotion_scenes.py <reel>/vertical --only B02 --force
python3 runtime/scripts/remotion_scenes.py <reel>/vertical --only B03 --force
python3 runtime/scripts/remotion_scenes.py <reel>/vertical --only B04 --force
python3 runtime/scripts/remotion_scenes.py <reel>/vertical --only B05 --force
python3 runtime/scripts/remotion_scenes.py <reel>/vertical --only B06 --force
python3 runtime/scripts/remotion_scenes.py <reel>/vertical --only B07 --force
python3 runtime/scripts/remotion_scenes.py <reel>/vertical --only B08 --force
python3 runtime/scripts/compile.py <reel>/vertical --height 3840 \
        --out <reel>/exports/vertical --force
```

B00 (composer cold open), B09 (composer handoff), B10 (outro) were unchanged — their scene components did not need portrait-specific edits and their rendered `media/*.mp4` remained valid.

## Portrait-specific scene fixes made in the isolated toolkit

The previous attempt's Gate V failed with 14 BLOCKER edge-bleeds and 2 MAJOR underfills. Every failure was traced to a scene decoration sitting outside `SAFE916` when the same component is rendered at 1080 wide instead of 1920 wide. Fixes were confined to the isolated toolkit:

1. `runtime/remotion/src/scenes/HesitantWriterFramed.tsx` — the top/bottom framing rules and the eyebrow / spark line moved from `4.5–7%` insets to `6.5–9%` insets in portrait mode. The landscape branch is unchanged (still `5–7.5%`). Fixes B01 top/bottom edge-bleed.
2. `runtime/remotion/src/scenes/SkillTeardownAnatomy916.tsx` — spark line moved from `bottom: height*0.04` to `bottom: height*0.075`. Fixes B02 edge-bleed.
3. `runtime/remotion/src/scenes/SkillTeardownPipeline916.tsx` — footer note raised from `bottom: height*0.09` to `bottom: height*0.115`; spark line from `0.04` → `0.075`. Fixes B03 edge-bleed.
4. `runtime/remotion/src/scenes/SkillTeardownMechanism916.tsx` — spark line raised from `bottom: height*0.04` to `bottom: height*0.075`. Fixes B04, B05, B06, B07 edge-bleeds.
5. `runtime/remotion/src/scenes/ClaudeVerdictArtifact916.tsx` — card width `0.90→0.92`, padding + font sizes bumped (`FONT_HEADING 0.024→0.036`, `FONT_LINE 0.017→0.026`). Verdict card coverage rose from 43% to 73% of the safe area — clears the 55% FILL_MIN. Fixes B08 underfill.

Also patched (needed for portrait channel-title overlay to sit inside safe area):

6. `runtime/scripts/compile.py` — channel title overlay Y offset moved from a fixed `H-h-40` to `H-h-max(40, int(h*0.06))`. In landscape (`h=2160`) this evaluates to `H-h-129` (still safely below the previous 40 was outside safe area but happened to be masked by the QC burn-in exclusion zone that covers the centered landscape title). In portrait (`h=3840`) this evaluates to `H-h-230`, keeping the "@HumanitariansAI" title inside SAFE916 whose bottom is at y=1824·(2160/1080)=3648. Previously the right ~225px of the title bled outside the burn-in exclusion (which only covers x=0..60%) and Gate V correctly flagged it as B00 bottom edge-bleed.

None of these changes touched the primary/live library — they are confined to the isolated per-invocation toolkit copy.

## Frame-level visual QC (Gate V, actual)

```
[gate-v] frames=22 BLOCKER=0 MAJOR=0 → vertical/_qc/REPORT.md
```

Gate V samples 22 frames total (11 beats × 50% + 85% of each beat's `render_duration_s`) from the compiled 4K portrait master, decodes them, and audits each against `SAFE916` for edge-bleed, canvas-fill (min 55%), and low-contrast (min 0.30 luminance separation). Every frame passed all three checks. The 4-column contact sheet lives at `vertical/_qc/contact_sheet.png` and was reviewed with the image-capable Read tool: content column-centered, safe insets honoured on every beat, the eight fixed beats visibly correct.

Per-beat coverage measured on the sampled 50% frames after the fix (all `defects=[]`):

| Beat | Component | Coverage of SAFE916 |
|---|---|---|
| B00 | ClaudeComposerAsk916 | 86% |
| B01 | HesitantWriterFramed916 | 95% |
| B02 | SkillTeardownAnatomy916 | 91% |
| B03 | SkillTeardownPipeline916 | 83% |
| B04 | SkillTeardownMechanism916 | 94% |
| B05 | SkillTeardownMechanism916 | 94% |
| B06 | SkillTeardownMechanism916 | 94% |
| B07 | SkillTeardownMechanism916 | 94% |
| B08 | ClaudeVerdictArtifact916 | 73% |

## Missing-checker honesty (same as landscape)

- `scripts/type_check.py` — still absent. See `TYPECHECK.md` for the visual substitute.
- `skills/kerning/`, `reference/type-spec.md`, top-level `ILLUSTRATIONS.md` — not present; not applicable to this build.

None of the absent checkers is claimed to have passed.

## Compile artifacts

- `exports/vertical/claude-liam-brutalist-skill-ai-explainer-vertical.mp4` — 4K portrait master.
- `exports/vertical/claude-liam-brutalist-skill-ai-explainer-vertical.verified.json` — sha256 + input-hash record atomically written by compile.py after Gate V passed.
- `vertical/build-state.json` — status `ready`.
- `vertical/_qc/REPORT.md` and `vertical/_qc/contact_sheet.png` — Gate V receipts.

## Conclusion

Portrait companion compiled as a NATIVE 4K 2160×3840 build with per-beat audio preserved, Gate V clean (0/0), no slates, no captions, no wallpaper (every non-UI middle beat is a purpose-built portrait illustration). Handle reads `@HumanitariansAI`. Human review by Bear is pending — this document records the machine passes; publication and YouTube's own 4K transcoding are downstream steps that this build does not attempt.

---

## Re-review addendum — invocation a2d6bcc90e44499b906ada378401a3db (2026-09-11)

SKILL.md changed since the previous build. See FACTCHECK.md §Source update for the diff summary. Assessment: two additive hard rules (Executable evidence + Math) and a simplified frontmatter description. No beat content is staled or contradicted.

Existing portrait master re-verified:
- `ffprobe`: 2160×3840, h264, AAC 48kHz, 186.9s — unchanged
- `sha256`: `d8dca0f414440a0816284375159ce89da59284b549735f26aaa9dc7bf46e9cb5` — unchanged
- Portrait contact sheet re-read via image-capable Read tool — all 11 beats confirmed in native 9:16 portrait reflow, @HumanitariansAI handle, content inside SAFE916
- Gate V BLOCKER=0, MAJOR=0 from previous build stands

No re-render performed. VISUAL-REVIEW.json updated to this invocation's run_id.
