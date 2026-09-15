# CHECKS-REPORT.md — vertical (2160×3840)

## Build run (this invocation)
run_id: `81d4ac79a3f54016801f0269956c2d7c` · source_sha256: `cf8873d1a540147a49b11feff3dd4ab774fd4f0e0ef9941c52895bd691bb628c`

Source changes vs prior build (run_id 7213a626): B04 narration + code updated with `./art smoke` advice; B05 code block updated to refactored `if !` pipeline; B04 audio independently regenerated for this vertical (20.78s). Total duration: 290.5s (was 285.5s).

```
$ python3 runtime/scripts/generate_audio_kokoro.py <vertical> --only B04
[kokoro] beat-B04.mp3  20.78s  voice=am_onyx

$ remotion_scenes.py <vertical> --only B04 --force
[remotion] B04: ok: ClaudeCodeBeat916 -> media/B04.mp4

$ remotion_scenes.py <vertical> --only B05 --force
[remotion] B05: ok: ClaudeCodeBeat916 -> media/B05.mp4

$ compile.py <vertical> --height 3840 --out <reel>/exports/vertical --force
[art] compiled B00…B12 VIDEO 290.5s  slots: 13/13 filled
```

Gate V: **0 BLOCKER / 0 MAJOR** — `.verified.json` stamped.
ffprobe: 2160x3840 h264 · 290.5s · aac 48kHz; volumedetect: mean -27.0 dB / max -2.9 dB.
Visual QC: `vertical/_qc/contact-sheet.jpg` Read — B04 portrait FEATURE table + `./art smoke` lines visible; B05 portrait `--install` code visible; B12 "Brutalist Command: setup." + @NikBearBrown + olive. All clean.

---

## Portrait derivation (not a crop)

```
$ python3 runtime/scripts/shorts.py <reel> --vertical
[short] B00…B12  ONDA CHECK: <pattern> → <pattern>916 (portrait re-render on short/;
        match the 916 zod schema — rule #4)
[short] 13 beats · ~285.5s (4:45.5) full-length vertical (no Short cap)
[short] dropped: none · ends on the last beat (no endcard)
[short] ONDA CHECK: 13 REMOTION beat(s) rewired to 916 compositions
```

Every one of the thirteen beats was rewired to a native portrait 916 composition, then re-rendered by `remotion_scenes.py` at 1080×1920 logical dimensions and compiled to a 2160×3840 native 4K master via `--height 3840`. No center-cut, no upscale-of-landscape.

## Scenes added / patched in the isolated toolkit's Root.tsx

- `ClaudeCodeBeat916` — added as a portrait Composition (1080×1920) reusing `ClaudeCodeBeat` with the same zod schema.
- `ClaudeCodeBeat.tsx` — adaptive-fontSize patch applied: `fontSize = min(baseFont, availH/(lines*lineH), availW/(longestLine*0.6))` so any URL-bearing or many-line stanza fits both axes. Landscape behaviour unchanged (baseFont still wins on typical stanzas).
- `BrutalistHesitantWriter.tsx` — the portrait scale patch from the isolated-toolkit playbook: `scale = height > width ? min(width/1080, height/1920) : min(width/1920, height/1080)`. Landscape behaviour unchanged; portrait now scales off a 1080×1920 design reference so the BLUF can actually fill the safe area.

Both patches will be exported to `scene-source/` by the supervisor's post-build sweep, per repoloop's `export_scene_changes` pass.

## Portrait-specific beat sheet edits

- **B01** — `text` split to three lines (`setup\ninstalls\neverything.`), `fontSize` 218, `lineSpacing` 3.45. Same triggers/replacements as landscape (`installs, everything` → `verifies, live`). Final on-screen reads "setup / verifies / live." — the same reel claim as the landscape's 2-line variant; the 3-line stack is what clears Gate V's 55 % FILL_MIN floor without edge-bleed on the portrait canvas.
- **B11** — `segment` shortened from "Read ./setup — diagnose without installing" to "Diagnose without installing" (the longer 16:9 segment ran past SAFE916.r). Composer `command` trimmed from 677 to ~525 chars and each `output` line to ≤ 45 chars (from 65+), so the composer body + footer + running + three output lines fit inside SAFE916. The paste-ready prompt remains substantively the same.

Every other beat's props are identical to the landscape sheet.

## Audio (reused from landscape build)

Same Kokoro `am_onyx` per-beat MP3s as the landscape master; symlinked into `vertical/mp3/` by `shorts.py --vertical`. No regeneration; no delta. Duration is identical (285.5 s).

## Compile (vertical 4K)

```
$ python3 runtime/scripts/compile.py <reel>/vertical --height 3840 \
  --out <reel>/exports/vertical
[art] compiled B00…B12 VIDEO 285.5s
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916'
[art] SKIN LINT: B12: palette=claude but the outro is 'ClaudeTitleOutro916'
[art] wrote …/exports/vertical/claude-liam-brutalist-command-setup-vertical.mp4  (285.5s)
[art] slots: 13/13 filled
```

The two SKIN LINT informational messages are expected for a portrait build — the 916 variants ARE the correct choice for this aspect (SHORTS ONDA CHECK rewired the sheet to them). The lint is a landscape-first heuristic, not a gate.

## Final gate (Gate V — final_frame_check.py)

```
[gate-v] frames=26 BLOCKER=0 MAJOR=0
Clean — no BLOCKER/MAJOR defects. ✓
```

The compiler's atomic replace + `.verified.json` stamp succeeded after this pass. The gate ran on the master candidate before atomic replace, exactly as on landscape.

## ffprobe / audio decode

```
$ ffprobe exports/vertical/claude-liam-brutalist-command-setup-vertical.mp4
codec=h264  width=2160  height=3840  duration=285.500000
audio=aac  48000 Hz  channels=2

$ ffmpeg -af volumedetect  →  mean_volume: -27.0 dB   max_volume: -2.9 dB
```

Native portrait 4K. Real audio decoded.

## Visual QC — actually looked at

- `_qc/vertical/beats/` — 39 per-beat frames sampled at 15%, 50%, 85% of every beat.
- `_qc/vertical/contact-sheet.jpg` — 13×3 grid the reviewer Read with the image-capable tool. Independent of the landscape contact sheet.
- Per-beat inspection confirmed: no accidental center-cropping, no clipping past SAFE916, no dead space under top-clustered content.

## Known limitations, honestly recorded

- Same `type_check.py` documentation-drift gap noted on the landscape build applies here; see TYPECHECK.md for the honest split.
- The outro card handle `@NikBearBrown` is locked by OUTRO-LOCK.md and flagged in README.md for the human reviewer's substitution decision, same as landscape.
- Portrait build depended on the isolated toolkit's `node_modules/.cache/` being shadowed with a writable directory (Apple App Sandbox denies writes into the shared symlinked cache). The shadow is a standard workaround, not a bypass — `runtime/remotion/node_modules` is a directory of symlinks + a writable `.cache/`.
