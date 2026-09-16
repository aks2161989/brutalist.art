# CHECKS-REPORT — Brutalist Command: art --list (9:16 vertical companion)

Invocation `run_id = c619fb86bdcd40079fc05e9378e8bbeb` — 2026-09-12.
Prior run: `8350d76b75754d93a802dcfb825c4478` — 2026-09-09.

Rebuilt after source `art` grew from 16 to 20 skills: godot-waikthrough,
godot-gamedev, godot-gdd and riff added; branch lines moved to art:58-80,
catch-all to art:127-136. Seven beats regenerated (B00 B01 B03 B04 B06
B09 B10); three re-rendered only (B02 B07 B08); B05 B11 unchanged.

This is the full-length `art vertical` companion (native portrait
compositions, not a cropped landscape). Slug
`claude-liam-brutalist-command-list-vertical`. Duration 196.9s at
2160 × 3840.

## Beat classification

12 / 12 SHOW · 0 HOLD · 0 PUNT — same acts as the landscape sheet,
with a longer B01 narration to accommodate the portrait BLUF recipe and
one extra HesitantWriter line-break for the 5-line stack.

## Teaching-arc checklist

- FRAMEWORK: ✓ (B02 — dispatcher `case` block)
- WORKED EXAMPLE: ✓ (B04 — verbatim 21-line output, 20 skills)
- FALSIFIABILITY: ✓ (B07 — `./art -list` exit 2 on stdout)
- SCAFFOLDED TASK: ✓ (B10 — Your Turn: diff the aliases)
- BOOKENDS: ✓ (B00 ASK, B01 BLUF, B10 YOUR_TURN, B11 OUTRO restate title)
- NO-SOURCE-NO-VERDICT: ✓ (every claim traces to `art:58-80`,
  `art:127-136`, or `../demo/RUN-LOG.md`)

## Runtime gates

- **Kokoro audio** — 12 / 12 beats generated locally with `am_onyx`.
  B01 lengthened to 16.26s so the portrait 5-line hesitant writer's
  50% and 85% samples both catch the settled state (still ≥ 9s BLUF
  minimum). Other beats reuse the landscape narration and mp3s.
- **Remotion render** — 12 / 12 beats rendered via `remotion_scenes.py`,
  foreground, serial concurrency one, `--scale=2` (native 4K portrait
  output = 2160 × 3840). Every beat uses a portrait `-916` composition:
  - B00, B10 → `ClaudeComposerAsk916`
  - B01 → `BrutalistHesitantWriter916` (portrait recipe: fontSize 130,
    lineSpacing 2.4, 5-line stack, `command-list-b01-v` seed)
  - B02–B08 → `ClaudeCodeBeat916` (added to Root.tsx in the isolated
    toolkit — the shipped Root.tsx ships only the landscape variant)
  - B09 → `ClaudeVerdictArtifact916` (7 artifact lines to fill the
    portrait card's vertical span above the 55% Gate V floor)
  - B11 → `ClaudeTitleOutro916`
  Chrome-headless-shell + `--single-process` wrapper via `ART_CHROME`.
- **compile.py final gates** — encoded a candidate mp4 into a temp
  directory, ran Gate V BEFORE promoting the candidate. Only replaced
  any previous verified master after Gate V passed clean AND the beat
  sheet / input hashes were re-verified.
- **Gate V (visual QC)** — final report (`_qc/REPORT.md`):
  ```
  Frames sampled: 24  ·  BLOCKER: 0  ·  MAJOR: 0
  Clean — no BLOCKER/MAJOR defects. ✓
  ```
- **Motion histogram** — code-cascade 7/12 (58%). WARNING flagged.
  Same rationale as landscape (command teardown; source and observed
  output are the point).
- **Skin lint** — compile.py emits two WARN lines that are **expected**
  for this playlist's portrait build (they say COLD OPEN LAW and OUTRO
  LAW want the landscape composition names on a `claude` palette; the
  vertical companion explicitly uses `-916` variants):
  - `B00: palette=claude but the cold open is 'ClaudeComposerAsk916'`
  - `B11: palette=claude but the outro is 'ClaudeTitleOutro916'`

## Local scene overrides applied in the isolated toolkit

- `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx` — portrait
  scale patch (memory `feedback_brutalist_hesitant_writer_portrait_scale_patch`):
  `const scale = height > width ? min(w/1080, h/1920) : min(w/1920, h/1080)`.
  Without this patch a 1080×1920 composition collapses to 0.5625× and
  every font drops with it, guaranteeing an underfill on Gate V.
  Landscape behaviour unchanged.
- `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx` — the two
  hard-coded correction pauses (1000+500ms and 300ms) reduced to
  (500+250ms and 200ms) so B01's mid/late samples both hit the settled
  state on a portrait beat with 5 lines.
- `runtime/remotion/src/scenes/ClaudeVerdictArtifact.tsx` — cardW cap
  raised (see landscape CHECKS-REPORT.md).
- `runtime/remotion/src/Root.tsx` — added `ClaudeCodeBeat916` composition
  at 1080×1920, component is the shared aspect-adaptive
  `ClaudeCodeBeat`.

None of these changes touch the shared public toolkit.

## Actual commands run

```bash
export ART_CHROME=<toolkit>/runtime/scripts/chrome_wrap.sh
export ART_CHROME_MODE=chrome-for-testing

# audio (only regenerated B01 differently)
python3 runtime/scripts/generate_audio_kokoro.py <REEL>/vertical

# remotion (foreground, one at a time, --scale=2 → native 4K portrait)
python3 runtime/scripts/remotion_scenes.py <REEL>/vertical

# assemble + Gate V
python3 runtime/scripts/compile.py <REEL>/vertical --height 3840 \
  --out <REEL>/exports/vertical --force
```

## Gates that did NOT run

Same as landscape — `scripts/type_check.py` and `reference/type-spec.md`
are not present in this workspace. See TYPECHECK.md.

## Frame evidence

- `_qc/contact_sheet.png` — Gate V's 24-frame sample, 16-tile contact.
- `_qc/REPORT.md` — the machine-readable Gate V report.
- Per-beat raw frames sampled during authoring for B00, B01, B04, B07,
  B09, B10, B11 (kept out of tree).

Human review remains required.
