# BUILD-PROMPT — vertical 9:16

Same build prompt as the landscape aspect. See `../BUILD-PROMPT.md` for the full
Brutalist playlist production brief.

## Vertical-specific invocation parameters

```json
{
  "slug": "claude-liam-brutalist-skill-godot-gdd",
  "run_id": "e2eff5f858424f279a41a85a015e0a15",
  "aspect": "vertical",
  "dimensions": [2160, 3840],
  "persona": "Liam",
  "voice": "am_onyx",
  "channel": "@HumanitariansAI"
}
```

## Portrait build command

```bash
python3 runtime/scripts/compile.py "$REEL" \
  --height 3840 \
  --out "$REEL/../exports/vertical" \
  --force
```

## Portrait-specific component fixes applied

1. **GodotDesignBoard.tsx** — footer `bottom:height*.04` → `bottom:height*.045+(portrait?45:0)`
   to keep @NikBearBrown below safe.b=3648 in 2160×3840.
2. **WalkerGodotSetup.tsx** — added `overflow:'hidden'` to flow content div to prevent
   4-panel stack from bleeding past shell bottom boundary.
3. **ClaudeCodeBeat.tsx** — portrait detection + adaptive `codeFontSize` so long bash
   lines don't bleed past portrait card edges.
4. **Root.tsx** — registered `ClaudeCodeBeat916` composition at 1080×1920 so B06 renders
   natively in portrait rather than being center-cropped from landscape.
5. **ClaudeVerdictArtifact916.tsx** — added `brandLabel` to destructured props and
   rendered at `bottom:height*0.065` to push ink y1 to ~3578 (fill 69.4%).
6. **vertical/beat_sheet.json** B01 `lineSpacing` → 3.4; B06 `pattern` → `ClaudeCodeBeat916`.
