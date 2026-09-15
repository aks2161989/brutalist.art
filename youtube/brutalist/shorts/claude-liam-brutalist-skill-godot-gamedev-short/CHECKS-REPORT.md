# CHECKS-REPORT.md — The godot-gamedev Skill — Short
# Run ID: 91d8e873ca5e413e8379a0c0c9179ed4 · 2026-09-12

## Output

- File: `exports/short/claude-liam-brutalist-skill-godot-gamedev-short.mp4`
- SHA-256: `5ba4652f27a4314c24ee398c26a03213501cd13e2a01ab9f2b68915c125bcff7`
- Container duration: 159.625s
- Video stream duration: 159.625s
- Audio stream duration: 159.625s
- Dimensions: 2160×3840 (9:16)
- Codec: H.264 + AAC
- Strictly under 180.0s: YES (all three durations)

## Beat sheet

- SHA-256: `47f09c5bd8a54669e70af3633e032293123c883571270d775c5614c04abe82ef`
- Beats kept: 9 (B00 B01 B04 B05 B08 B09 B10 B11 B12)
- Beats dropped: 4 (B02 B03 B06 B07)
- Slots filled: 9/9 VIDEO

## Compile output

```
[art] compiled B04  VIDEO    18.3s  ← B04.mp4
[art] compiled B05  VIDEO    21.0s  ← B05.mp4
[art] compiled B10  VIDEO    18.2s  ← B10.mp4
[art] motion histogram: type-on:2  spring-reveal:2  type-on-correct:1  line-highlight:1  comparison-reveal:1  artifact-reveal:1  mascot-title:1
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk
[art] SKIN LINT: B12: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro
[art] build stamp → beat_sheet.json (9/9 filled)
[art] wrote exports/short/claude-liam-brutalist-skill-godot-gamedev-short.mp4  (159.6s, audio: per-beat timeline, drawtext: no — PIL overlays)
[art] slots: 9/9 filled — B00:VIDEO B01:VIDEO B04:VIDEO B05:VIDEO B08:VIDEO B09:VIDEO B10:VIDEO B11:VIDEO B12:VIDEO
```

## Skin lint warnings (expected, cosmetic)

```
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk
[art] SKIN LINT: B12: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro
```

These are expected — the short's beat_sheet inherits `palette: claude` and the portrait 916 pattern names (`ClaudeComposerAsk916`, `ClaudeTitleOutro916`) don't match the skin-lint's non-916 pattern strings. These warnings appear identically in the parent vertical and are purely a lint-string-match artefact. No change needed.

## Rebuild reason

Parent vertical updated in run_id `d6a7b8125f8a4bc4bbd1122f104532f0`: B04/B05/B10 narration and props updated for SKILL.md code→visible-result teaching unit requirement. Short re-cut from updated parent media. All 9 native portrait clips re-copied from parent vertical.

## Gate checks

| Gate | Status | Notes |
|------|--------|-------|
| Duration < 180s | PASS | 159.625s (container), 159.625s (video), 159.625s (audio) |
| All beats filled | PASS | 9/9 VIDEO |
| Native 9:16 portrait | PASS | 2160×3840 confirmed |
| No ONDA re-render required | PASS | Source already 9:16; all native portrait clips reused |
| Liam sign-off present | PASS | B11 narration_text ends "Liam, in for Bear."; B12 narration_text "Liam, in for Bear." |
| No captions | PASS | captions: false in metadata |
| No endcard | PASS | --no-endcard flag used |
| Parent unchanged | PASS | shorts.py copies assets independently; source verified by sha256 |

## Visual QC

28 frames extracted (15%/50%/85% per beat + final frame). 0 blockers. 0 majors. See VISUAL-REVIEW.json.

## Source protection

Parent reel SHA-256 (vertical master): `3c4c7be38b1c1534736e254ca9614040d2a434bf5edfc53e83d6cc37b7167483`
No modifications to parent reel, source media, or beat sheets.
