# CHECKS-REPORT — vertical 2160×3840

Run ID: `713f16bacfaa4ed28908ef6a8db68b4c` (re-verified 2026-09-13; previous: `ee4093952a4c4010a7cab3e6729cd376`)
Reel: `.../claude-liam-brutalist-runtime-generate-audio-kokoro/vertical/`
Master: `exports/vertical/claude-liam-brutalist-runtime-generate-audio-kokoro-vertical.mp4`

## Gate A · schema + approvals (compile.py preflight)

```
$ python3 runtime/scripts/compile.py <reel>/vertical --height 3840 \
    --out <reel>/exports/vertical --force
[art] compiled B00  VIDEO    15.5s  ← B00.mp4
[art] compiled B01  VIDEO    10.6s  ← B01.mp4
... (all 12 beats VIDEO, no slates) ...
[art] compiled B11  VIDEO     6.8s  ← B11.mp4
[art] build stamp → beat_sheet.json (12/12 filled)
[art] wrote .../exports/vertical/claude-liam-brutalist-runtime-generate-audio-kokoro-vertical.mp4  (319.7s, ...)
[art] slots: 12/12 filled — B00:VIDEO B01:VIDEO ... B11:VIDEO
```

- All 12 slots filled with per-beat native 9:16 mp4s. No slates.
- `build_safety.validate_project` + `validate_approvals` pass.

## Gate V · visual QC (`_qc/REPORT.md`)

```
# Gate V — visual QC report
Frames sampled: 24  ·  BLOCKER: 0  ·  MAJOR: 0
Clean — no BLOCKER/MAJOR defects. ✓
```

Iteration history (portrait):
- v1: B00/B10/B11 edge-bleed (right); B01 underfill 26 %. Root causes were long single-line topic strings (`BRUTALIST · UTILITY: GENERATE_AUDIO_KOKORO.PY` = 45 chars) that overflow the portrait-safe 972 px inner width, plus a BLUF stanza too small (fontSize 130 with a widest line of 8 chars).
- v2: shortened `topic` to `BRUTALIST · UTILITY`, `segment` on B10 to `Dry-run + generate two`; bumped B01 to fontSize 175 / lineSpacing 2.2. Cleared all edge-bleeds; B01 still underfill 42 %.
- v3 (final): B01 to fontSize 220 / lineSpacing 1.9 with 4-line text `kokoro\nis\npaid and\nremote.` — Gate V clean.
- Outro (B11): the shipped `ClaudeTitleOutro916.tsx` did not word-break single-word filenames. Patched locally to add `overflowWrap: 'anywhere', wordBreak: 'break-word'` so the 45-char title wraps inside the 936 px maxWidth.

## Compiler receipts (`_qc/`, `exports/*.verified.json`)

- `_qc/REPORT.md` — Gate V report, above.
- `_qc/contact_sheet.png` — 12-beat portrait contact sheet (visually inspected — see TYPECHECK.md).
- `exports/vertical/claude-liam-brutalist-runtime-generate-audio-kokoro-vertical.mp4` — 18,145,339 bytes.
- `exports/vertical/claude-liam-brutalist-runtime-generate-audio-kokoro-vertical.verified.json` — compiler's `atomic_verify` receipt.

## ffprobe · master container

```
$ ffprobe -v error -show_entries stream=width,height,codec_name,duration:format=duration \
    exports/vertical/claude-liam-brutalist-runtime-generate-audio-kokoro-vertical.mp4
codec_name=h264
width=2160
height=3840
duration=319.666667
codec_name=aac
duration=319.708000
```

- Native 4K portrait (2160×3840), h.264 video + AAC audio, 319.7 s. No upscale, no crop from the landscape master; every beat rendered natively at 1080×1920 (Remotion `--scale=2` producing 2160×3840).

## SKIN LINT (informational)

```
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk
[art] SKIN LINT: B11: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro
```

These are the intentional native-portrait swaps per the production brief (portrait companion must not crop the landscape master). Not defects.

## Missing / unshipped checks (same as landscape)

- `runtime/scripts/type_check.py` and `reference/type-spec.md` — not shipped. See `TYPECHECK.md`.
- `runtime/skills/kerning/SKILL.md` — not shipped.

## Conclusion

Vertical master is Gate-V clean, native 4K portrait, 319.7 s, all 12 slots filled by real native 9:16 Remotion renders. Human review pending.
