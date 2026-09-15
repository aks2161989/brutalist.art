# TYPECHECK.md — The explainer Skill (portrait)

## GATE T status

Same as landscape (`../TYPECHECK.md`): the legacy `scripts/type_check.py`
is not shipped in this snapshot. Portrait typography reviewed by hand
against Gate V's 22 steady-state frames.

## What DID run

`runtime/qc/final_frame_check.py` — clean:
```
Frames sampled: 22  ·  BLOCKER: 0  ·  MAJOR: 0
Clean — no BLOCKER/MAJOR defects. ✓
```

## Manual typography audit against the 9-point rubric

1. **Edge bleed / clipping** — none. The `SAFE916` inset (x 54–1026, y
   96–1824 at 1080×1920 design ref) is respected. B01 hesitant writer
   after the portrait-scale patch renders at full design-size (~160 px
   fontSize scaled 1.0) across 8 short lines and the ink bbox sits well
   inside the inset. Anatomy, Pipeline, and Mechanism 916 wrappers reflow
   from `useVideoConfig()` and stay inside `SAFE916`.
2. **Title-safe margins** — respected.
3. **Container overflow** — Pipeline diagram: 4 phases + input + output =
   6 nodes at `boxW = min(200, floor(1080 × 0.78 / 6) − 20) = 120`; total
   width = 6 × 120 + 5 × 42 = 930 px inside a 1080 × 0.86 = 928.8 px
   allowance (verified inside margins with `left/right = w×0.07`). Fits.
4. **Collision** — none.
5. **Offscreen anchors** — none. `channel_title` metadata omitted so the
   compile-overlay wordmark does not bleed past `safe.b` (documented in
   `feedback_channel_title_portrait_bleed`).
6. **Legibility** — serif heading + sans body remains legible at 4K
   portrait output.
7. **Brand bug placement** — @HumanitariansAI folder chip inside
   composer beats; @NikBearBrown on outro card locked via
   `ClaudeTitleOutro916` schema (OUTRO-LOCK.md).
8. **Aspect** — 2160×3840, confirmed via ffprobe.
9. **Canvas fill** — every beat ≥ 55 % of `SAFE916` per Gate V.

## Skin lint warnings — false positives

```
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk
[art] SKIN LINT: B10: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro
```

The 916 variants ARE the portrait-native cold open and outro. Same warnings
appear on every prior portrait episode in this playlist by design.

## Verdict

`TYPECHECK` = PASS by visual review. Portrait typography audited against
CLAUDE-CODE-VISUAL-QC-CHECK.md; no defects. GATE T machine check
unavailable in this snapshot — recorded honestly.
