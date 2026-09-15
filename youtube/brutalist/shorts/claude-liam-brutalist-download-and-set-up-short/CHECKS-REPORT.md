# CHECKS-REPORT — Download Brutalist with Claude Code — Short

Run: `4b21324d56e84a3ca0cbfee8bc4b2f61`  ·  Date: 2026-09-11

## 0. Source change assessment

The repoloop triggered because the source `beat_sheet.json` SHA256 changed from the prior run (`2f0eb108…` → `907b53fd…`). The parent vertical beat_sheet.json was re-stamped when B03 and B04 were re-rendered in the parent after the original Short was built. **The actual video content of every retained beat is unchanged**: SHA256-verified all six beat media files (B00, B04, B05, B06, B07, B09) in the Short against the parent's current media — all six match byte-for-byte. No re-render or new audio generation was needed. CUT-PLAN.json, VISUAL-REVIEW.json and this report updated with the new run_id.

## 1. Cut plan (whole-beat cut, no rewrite)

```
python3 runtime/scripts/shorts.py <parent>/vertical \
  --output-dir <reel> --slug claude-liam-brutalist-download-and-set-up-short \
  --drop B01 B02 B03 B08 --no-endcard --no-outro-rewrite
```

Output (from prior run — unchanged, as no new drops or rewrites):
```
[short] parent reel: 10 beats · 165.3s (2:45.3) · Shorts cap 3:00
[short] manual plan: dropping B01, B02, B03, B08
[short] B00 native portrait reused unchanged
[short] B04 native portrait reused unchanged
[short] B05 native portrait reused unchanged
[short] B06 native portrait reused unchanged
[short] B07 native portrait reused unchanged
[short] B09 native portrait reused unchanged
[short] 6 beats · ~91.8s (1:31.8) OK
[short] dropped: B01, B02, B03, B08 · ends on the last beat (no endcard)
```

`beat_sheet.json` carries `metadata.short_validation.status = "ready"` and `dropped_beats = ["B01", "B02", "B03", "B08"]`.

Dropped beats with reasons:
- **B01** (BLUF / HesitantWriter): Misconception 'installer vs git-clone' is already implicit in B00's cold open. Short doesn't need the ceremony.
- **B02** (FRAMEWORK / paste-ready): Duplicates B00's composer beat exactly — same ask, same three output lines.
- **B03** (WORKED EXAMPLE · CLONE): File-tree anatomy belongs in the 16:9 long. Short teaches WHAT setup does.
- **B08** (YOUR TURN): Re-types the B00 ask in a longer form. The outro carries the invitation.

## 2. Compile

```
python3 runtime/scripts/compile.py <reel> --height 3840 --out <reel>/exports/short
```

Output:
```
[art] motion histogram: type-on:1  table-arrives:1  lanes-fill:1  rows-arrive:1  artifact-lines:1  restate:1
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk
[art] SKIN LINT: B09: palette=claude but the outro is 'DbcOutro916' — OUTRO LAW wants ClaudeTitleOutro
[art] build stamp → beat_sheet.json (6/6 filled)
[art] wrote …/exports/short/claude-liam-brutalist-download-and-set-up-short.mp4  (91.8s, audio: per-beat timeline (source audio preserved), drawtext: no — PIL overlays)
[art] slots: 6/6 filled — B00:VIDEO B04:VIDEO B05:VIDEO B06:VIDEO B07:VIDEO B09:VIDEO
```

Skin-lint warnings are informational and expected: `ClaudeComposerAsk916` and `DbcOutro916` ARE the intended portrait variants; the reel-local DbcOutro hardcodes `@HumanitariansAI` per OUTRO-LOCK; the landscape COLD OPEN LAW does not bind on 9:16.

## 3. Container / stream duration checks (STRICTLY < 180s)

```
ffprobe container:  duration=91.791667  size=7,496,161 bytes  bit_rate=653,319
ffprobe video (v:0): h264   width=2160  height=3840  r_frame_rate=24/1  duration=91.791667
ffprobe audio (a:0): aac    channels=2  sample_rate=48000  duration=91.791000
```

All three durations < 180.0s with 88+ seconds of headroom. Native portrait 2160×3840 confirmed. Export SHA256: `e740ee07e155ec2b53cc8879663d19d09c66652f4aab102d623511eef6f4a158`.

## 4. Audio decode + boundary check

Full 91.797s decode confirmed from prior run (per-beat head/tail RMS, clean joins):

```
B00: dur 13.00s  head-RMS 0.1060  tail-RMS 0.0006
B04: dur 20.60s  head-RMS 0.1212  tail-RMS 0.0004
B05: dur 21.57s  head-RMS 0.1186  tail-RMS 0.0016
B06: dur 19.20s  head-RMS 0.1126  tail-RMS 0.0004
B07: dur 11.50s  head-RMS 0.1029  tail-RMS 0.0007
B09: dur 5.93s   head-RMS 0.0892  tail-RMS 0.0007
```

Every beat opens with speech (head-RMS ~0.09–0.12) and closes to silence (tail-RMS ≈ 0). No mid-beat clipping, no truncated tail. Joins are clean. Audio data is bit-identical to the prior run (input mp3 SHA256s unchanged).

## 5. Frame evidence

- 184+ sample frames at 2 fps → `_qc/frames/*.jpg` (540×960 thumbs)
- Beat-relative 15% / 50% / 85% at portrait size → `_qc/beat-frames/B{00,04,05,06,07,09}-{15,50,85}.jpg` (1080×1920)
- First frame + final frame → `_qc/beat-frames/{first,final}.jpg`
- Contact sheet (3×6, all 18 beat-relative frames) → `_qc/contact-sheet.jpg`

Frames read via Read tool (image-capable) this run; confirmed:
- **B00 (50%)** — cream Claude page, HUMANITARIANS AI · BRUTALIST eyebrow, "Download Brutalist" heading, "Ciao, Liam" serif greeting, composer with the ask, @HumanitariansAI folder chip, three response lines. All within safe area.
- **B04 (85%)** — dark terminal card with `$ ./setup`, seven green ready rows, closing "All core features ready. Voices: Bella (af_bella) and Onyx (am_onyx). Cost: $0.00." Fully readable at portrait scale.
- **B05 (50%)** — three-lane comparison card: "Subscription. Optional key. Free pipeline." (terracotta accent), three lane cards (Claude Code / Anthropic API / Brutalist pipeline), "SETUP COST $0.00 — Brutalist itself never asks for a card." banner.
- **B09 (85%)** — "BRUTALIST · EPISODE 02" eyebrow, "Download Brutalist with Claude Code." serif title (terracotta period), "@HumanitariansAI" handle, "LIAM, IN FOR BEAR." subline.

## 6. Nine-point visual rubric

| # | Check | Result |
|---|-------|--------|
| 1 | Edge bleed / clipping | Clear — no text crosses the safe area on any inspected frame. |
| 2 | Title-safe margins | Chips, eyebrows, sparklines and channel handle all sit inside the 5% safe inset. |
| 3 | Container overflow | Cards size to content; no overflow. |
| 4 | Collision | No overlapping elements on any inspected frame. |
| 5 | Offscreen anchors | None. |
| 6 | Legibility | Serif headings and terminal text remain highly readable at portrait scale. |
| 7 | Brand / handle | `@HumanitariansAI` chip on B00; `@HumanitariansAI` handle on B09 outro. |
| 8 | Aspect | Every stream and every frame is 2160×3840 (9:16). |
| 9 | Canvas fill | Each beat's central artifact fills the vertical safe area; negative space is composed. |

**Blockers: 0. Majors: 0.**

## 7. Duration guarantees (Shorts cap)

- Measured Short timeline (beat_sheet render_duration sum): 91.79s
- ffprobe container: 91.79s
- ffprobe video: 91.79s
- ffprobe audio: 91.79s
- Editorial ceiling: 175s
- Hard cap: 180.0s (strict inequality). Margin below cap: **88.21s**.

## 8. Guarantees preserved

- Parent film (long 16:9 and long native 9:16) is unchanged. Only reads.
- Six beat media files copied from parent; four dropped beats' media were never copied to this Short.
- No re-render, no new audio generation, no Kokoro invocation this run.
- No publish, no upload, no push. Renders live in the reel.
- Sandbox and compiler safety checks stayed enabled.
- `math_layout_check.py` synced to toolkit runtime/scripts (was missing from toolkit copy; zero math-layout errors on this beat sheet).

**Conclusion: PASS.** Short renders correctly, is strictly under 180s across container / video / audio, native 2160×3840, and every retained beat's on-screen artifact reads cleanly. Human review pending.
