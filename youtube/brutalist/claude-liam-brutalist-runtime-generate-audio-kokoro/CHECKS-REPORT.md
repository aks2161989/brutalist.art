# CHECKS-REPORT — landscape 3840×2160

Run ID: `713f16bacfaa4ed28908ef6a8db68b4c` (re-verified 2026-09-13; previous: `ee4093952a4c4010a7cab3e6729cd376`)
Reel: `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/youtube/brutalist/claude-liam-brutalist-runtime-generate-audio-kokoro/`
Master: `exports/landscape/claude-liam-brutalist-runtime-generate-audio-kokoro.mp4`

## Gate A · schema + approvals (compile.py preflight)

```
$ python3 runtime/scripts/compile.py <reel> --height 2160 --out <reel>/exports/landscape --force
[art] compiled B00  VIDEO    15.5s  ← B00.mp4
[art] compiled B01  VIDEO    10.6s  ← B01.mp4
... (all 12 beats VIDEO, no slates) ...
[art] compiled B11  VIDEO     6.8s  ← B11.mp4
[art] build stamp → beat_sheet.json (12/12 filled)
[art] wrote .../exports/landscape/claude-liam-brutalist-runtime-generate-audio-kokoro.mp4  (319.7s, ...)
[art] slots: 12/12 filled — B00:VIDEO B01:VIDEO ... B11:VIDEO
```

- All 12 slots filled with per-beat mp4s. No slates. Duration 319.7 s (matches sum of measured beat durations).
- `build_safety.validate_project` + `validate_approvals` pass (no fellows profile; no professor-notes approval required).

## Gate V · visual QC (_qc/REPORT.md)

```
# Gate V — visual QC report
Frames sampled: 24  ·  BLOCKER: 0  ·  MAJOR: 0
Clean — no BLOCKER/MAJOR defects. ✓
```

- Sampled 24 frames — first, 50%, 85% of every beat + final frame.
- Two prior BLUF iterations were caught by Gate V before landing (v1: underfill 46%; v2: edge-bleed on the 320 pt bump). Final: `text: "kokoro\nis paid\nand remote."`, `fontSize: 260`, `lineSpacing: 1.2`, 3 lines, seed v3 → PASS.

## Compiler receipts (`_qc/`, `exports/*.verified.json`)

- `_qc/REPORT.md` — Gate V report, above.
- `_qc/contact_sheet.png` — 12-beat contact sheet (visually inspected — see TYPECHECK.md).
- `exports/landscape/claude-liam-brutalist-runtime-generate-audio-kokoro.mp4` — 18,938,085 bytes.
- `exports/landscape/claude-liam-brutalist-runtime-generate-audio-kokoro.verified.json` — compiler's `atomic_verify` receipt.

## ffprobe · master container

```
$ ffprobe -v error -show_entries stream=width,height,codec_name,duration:format=duration,bit_rate \
    exports/landscape/claude-liam-brutalist-runtime-generate-audio-kokoro.mp4
codec_name=h264
width=3840
height=2160
duration=319.666667
codec_name=aac
duration=319.708000
```

- Native 4K UHD (3840×2160), h.264 video + AAC audio, 319.7 s. No upscale, no crop.

## Motion pantry advisory

```
[art] motion histogram: code-cascade:6  type-on:2  hesitant-type:1  phase-flow:1  artifact-in:1  outro-card:1
[art] WARNING: 'code-cascade' carries 6/12 beats (50%) — over the ~40% pantry cap; convert the excess to another language (MOTION.md)
```

- Utility teardowns of a source file legitimately show code at least 5–6 times (CLI surface, model_paths, skip rules, synth loop, worked example, failure modes). Accept as a documented deviation on utility episodes; not a Gate V defect.

## Missing / unshipped checks (honest gaps)

- `runtime/scripts/type_check.py` and `reference/type-spec.md` — referenced in public docs but not shipped. See TYPECHECK.md for the visual typography inspection that stood in.
- `runtime/skills/kerning/SKILL.md` — not shipped in this toolkit copy.
- No fabricated pass. Every check reported is a check that actually ran.

## Conclusion

Landscape master is Gate-V clean, native 4K, 319.7 s, all 12 slots filled by real Remotion renders (no slates). Human review pending — see FEEDBACK.md.
