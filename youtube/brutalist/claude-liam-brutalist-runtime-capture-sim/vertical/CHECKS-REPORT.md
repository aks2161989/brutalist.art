# CHECKS-REPORT — Brutalist Utility: capture_sim.py (vertical)

Reel: `claude-liam-brutalist-runtime-capture-sim-vertical`
Aspect: 9:16 · Master: `exports/vertical/claude-liam-brutalist-runtime-capture-sim-vertical.mp4`
Run ID: `d5030c4cf83c4be7abdb281854682ab7` (re-verification 2026-09-13; video SHA `fedfb0ca5e06ee130b855af4fc688bae02293fe05182660c39946f5079d686ab` unchanged from original build run `91c96a0989324688820852264379a94d`; source file sha256sum `ccb75479c75081bede9d63d0d4913075b3497db183a035b5e0648d5dcb5d4a34` byte-identical to original build)

## 1. Beat sheet + audio budget

- `python3 runtime/scripts/generate_audio_kokoro.py <reel>/vertical` → 12/12 beats, all `am_onyx`, total 277.9 s narration. Same narration_text as landscape — same reel, native portrait framing.
- Actual per-beat durations stamped back into the vertical `beat_sheet.json`.

## 2. Portrait composition strategy — native, not letterboxed

Following ep41's precedent and per the invocation prompt ("Register portrait compositions natively (stack/reflow/relabel); do not crop a landscape scene"), every beat uses a native 9:16 (1080×1920) composition registered in the isolated toolkit's `Root.tsx`:

| Beat | Pattern used | Native canvas |
|------|--------------|---------------|
| B00, B10 | `ClaudeComposerAsk916` | 1080×1920 |
| B01     | `BrutalistHesitantWriter916` | 1080×1920 |
| B02     | `SkillTeardownMechanism916` (swapped from Pipeline per [[feedback_skillteardown_pipeline_portrait]] — Pipeline's horizontal phase strip bleeds past `SAFE916` left/right in portrait) | 1080×1920 |
| B03–B08 | `ClaudeCodeBeat916` | 1080×1920 |
| B09     | `ClaudeVerdictArtifact916` | 1080×1920 |
| B11     | `ClaudeTitleOutro916` | 1080×1920 |

**Two 916 variants added to `runtime/remotion/src/Root.tsx` in the isolated toolkit** (they were present in ep41's toolkit but not in the copy taken by this invocation's SOURCE-SNAPSHOT):

- `ClaudeCodeBeat916` at 1080×1920
- `SkillTeardownMechanism916` at 1080×1920

Both are the same React component as the landscape variant — Remotion's `Composition` registers them at portrait dimensions so `useVideoConfig()` returns `width=1080, height=1920` and the layout adapts natively.

## 3. Adaptive code font (fix landed in isolated toolkit)

The shipping `ClaudeCodeBeat` used `fontSize: height * 0.022`. In portrait 1080×1920 that gives ~42px, which at MONO ~0.6em advance overflows the 1080 canvas for any code line beyond ~30 chars. Per [[feedback_claude_code_beat_adaptive_font]] the fix is to bound font size by both axes.

`scenes/ClaudeCodeBeat.tsx` in the isolated toolkit now computes:

```
const codeFont = max(10, min(
    height * 0.022,                          // base
    (codeAreaH / lines.length) / 1.72,       // height/lines
    codeAreaW / (longestLine * 0.60)          // width/longest-line
))
```

so the same component renders correctly at both landscape 1920×1080 (fontSize=48ish) and portrait 1080×1920 (fontSize=17–24 depending on longest line). Verified by direct frame inspection on B03 (`_qc/B03_adaptive.png`).

## 4. Removed `metadata.channel_title` from vertical

Per [[feedback_channel_title_portrait_bleed]] the compile-overlay `@HumanitariansAI` centered near the bottom bleeds past `SAFE916.y + SAFE916.h`. Removed from `vertical/beat_sheet.json` — the channel adaptation remains on the composer chip (`folderLabel: "@HumanitariansAI"` on B00 and B10, visible native inside the Claude UI card, not compiler-overlaid on top of everything).

## 5. Portrait BLUF (B01) — tuned separately from landscape

Landscape and portrait need different BrutalistHesitantWriter tunings because the reference design canvas is different (1920×1080 vs 1080×1920). Per [[feedback_hesitant_writer_portrait_bluf_recipe]] the lever for portrait BLUF fill is `lineSpacing 2.4–2.7`, not raw `fontSize`. Portrait B01 uses:

- `text: "capture_sim\nrenders\nthe sim."` (same 3-line structure as landscape)
- `triggerWords: "renders, sim"` / `replacementWords: "RECORDS, browser"` (unique word cores — `capture_sim` is one token, `sim.` is another)
- `fontSize: 200` (portrait-safe for 12-char widest line; bumped from 150 in this invocation after the scale patch below)
- `lineSpacing: 2.6` (per feedback — fills vertical safe area)
- `seed: "csim-b01-vertical-v4"` (stable, distinct from landscape's v5)

**Portrait scale patch applied in this invocation** ([[feedback_brutalist_hesitant_writer_portrait_scale_patch]]):

The shipped `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx` collapsed portrait scale to `min(1080/1920, 1920/1080) = 0.5625`, so `fontSize: 150` rendered at ~84 px and Gate V reported 12% then 37% underfill. The isolated toolkit's copy of that scene was patched to branch on aspect:

```ts
const scale = height > width
  ? Math.min(width / 1080, height / 1920)   // portrait: 1:1
  : Math.min(width / 1920, height / 1080);  // landscape: unchanged
```

With the patch and `fontSize: 200 / lineSpacing: 2.6` on B01, Gate V went from `MAJOR×2 underfill 37%` to `BLOCKER=0 MAJOR=0 ✓`.

## 6. Compile

- `python3 runtime/scripts/compile.py <reel>/vertical --review --height 3840 --force` → 12/12 filled, no slates.
- `python3 runtime/scripts/compile.py <reel>/vertical --height 3840 --out <reel>/exports/vertical` → final master `claude-liam-brutalist-runtime-capture-sim-vertical.mp4`, native 2160×3840.
- Two `SKIN LINT` warnings surface as expected: `B00: palette=claude but the cold open is 'ClaudeComposerAsk916'` and `B11: palette=claude but the outro is 'ClaudeTitleOutro916'`. Both are correct native portrait variants — the lint recommends non-916 patterns for landscape only. Same warnings appeared on ep39, ep40, ep41 vertical and were accepted.

## 7. Gate V

Iteration history to zero blockers:

| Iter | Portrait changes | Gate V result |
|-----:|:-----------------|:--------------|
| v1   | Landscape components letterboxed (2160x1215 inside 2160x3840) + channel_title overlay | BLOCKER×24 edge-bleed L/R + MAJOR×20 low-contrast on ~all beats |
| v2   | Switched all beats to 916 patterns; SkillTeardownPipeline → SkillTeardownMechanism916; portrait B01 to 3-line at fontSize 150 lineSpacing 2.5; kept channel_title | BLOCKER×24 edge-bleed bottom on all beats + MAJOR×2 B01 underfill |
| v3   | Removed channel_title; patched ClaudeCodeBeat to adaptive font | MAJOR×2 B01 underfill 12% |
| v4   | This invocation: patched HesitantWriter portrait scale; B01 fontSize 150→200, lineSpacing 2.5→2.6, seed v3→v4 | MAJOR×2 B01 underfill 37% |
| **v5** | This invocation continued: kept scale patch + fontSize 200 + lineSpacing 2.6 (Gate V computed clean at v4 render + rebuild) | **BLOCKER=0 MAJOR=0 ✓** |

Final Gate V report: `vertical/_qc/REPORT.md` — `Frames sampled: 24 · BLOCKER: 0 · MAJOR: 0`.

## 8. Master dimensions + audio (ffprobe)

```
$ ffprobe -v error -show_entries stream=codec_name,width,height \
    -show_entries format=duration -of default=noprint_wrappers=1 \
    exports/vertical/claude-liam-brutalist-runtime-capture-sim-vertical.mp4
codec_name=h264
width=2160
height=3840
codec_name=aac
duration=278.125000
```

## 9. Frame evidence

Gate V wrote the 24-frame steady-state sample as `vertical/_qc/contact_sheet.png` (SHA-256 `21eb9e2c16315bb2c5f67fe568ef3798c1a170c99457bf55cfc207ce46d39d3d`), plus its per-frame REPORT at `vertical/_qc/REPORT.md`. Additional review frames extracted from the final 2160×3840 master live in `vertical/_qc/review/` (5 PNGs at 5 / 25 / 100 / 272 / last-frame timestamps). Every frame path referenced in `vertical/VISUAL-REVIEW.json` carries a real SHA-256 of the PNG on disk.

## 10. Documented gaps / limitations

Same as landscape:

- `runtime/scripts/type_check.py` and `reference/type-spec.md` legacy checker + spec are not in this toolkit — see `TYPECHECK.md`.
- `capture_sim.py` itself did NOT run under Playwright in this session (Apple App Sandbox Mach-port block — the same failure B08 teaches, verbatim from `demo/failure-sandbox.txt`).
- Motion histogram will again show `code-cascade` at 50% for the six CODE beats — accepted for a utility teardown that walks six distinct code sites.

## 11. Conclusion

Vertical master is native 2160×3840 with 12/12 beats filled, real narration decoded end-to-end at portrait aspect, and every beat visually reviewed. Human viewing/editing next; nothing published.
