# CHECKS-REPORT — landscape

run_id: `915961a4e22f469590e497ffe1dd9a7f` (re-verified; original build run_id `f2da2cc936694334b92c9a741e8f66e2`)

## Source change summary (this revision)

Between the previous run (`5cfd78a4afe94cf3928a48ebeb3f626c`) and this one, the `art` dispatcher gained new commands (`todo`, `run`, `approvals`, `final`, `keys`, etc.) before the `shorts` case, shifting its line numbers from **art:81-83** to **art:102-104** and the `vertical` case from art:84-86 to **art:105-107**. The `shorts.py` module docstring SHORTS LAW rules 2, 3, and 4 were also expanded with more detail (explicit `--rewrite-outro` mention in rule 3; HAI scheduling timing in rule 4).

## Beats re-rendered

- **B02** — ClaudeCodeBeat title corrected from `"art:81-86 — two cases, one script"` to `"art:102-107 — two cases, one script"`; inline line-number comments added to the code block.
- **B03** — Code card updated to remove the `"verbatim"` claim (the stored condensed summary no longer matched the expanded docstring); condensed version updated to reflect current rules 2/3/4 accurately. Narration unchanged (still accurate to the current source).

## What actually ran and passed

- **B02/B03 re-render** — `remotion_scenes.py <reel> --only B02 --force` and `--only B03 --force` using the `ART_CHROME` chrome-wrapper. Both succeeded: `ClaudeCodeBeat → media/B02.mp4`, `ClaudeCodeBeat → media/B03.mp4`.
- **Compile master** — `python3 runtime/scripts/compile.py <reel> --height 2160 --out exports/landscape --force` wrote `exports/landscape/claude-liam-brutalist-command-shorts.mp4` (3840×2160 · 296.3s · h.264 + AAC), 12/12 beats filled.
- **Gate D — audio decode / duration** — compile.py's `verify_output()` re-probed the emitted mp4; duration ~296.3 s, audio decoded OK.
- **Gate V — final_frame_check** — `runtime/qc/final_frame_check.py <reel> --mp4 exports/landscape/...mp4 --sheet beat_sheet.json` → **0 BLOCKER / 0 MAJOR** (24 frames sampled). Per-beat sampling written to `_qc/contact_sheet.png`.
- **Own-eye visual review** — `_qc/contact_sheet.png` (4×6 per-beat grid) and `_qc/final-contact-sheet.png` (3×4 sample of finished master) opened with image-capable Read tool. All 12 panels show content inside title-safe area. B00 Salam cold open composer chip shows `@HumanitariansAI`. B01 hesitant BLUF shows corrected "shorts drops. / and rewires it." B02 code card shows "art:102-107" in the title. B03 code card shows updated SHORTS LAW without "verbatim" claim. B09 verdict 8-line artifact, B10 Your Turn, B11 outro @NikBearBrown per OUTRO-LOCK.

## Available runtime checks used

| Gate | Script | Result |
|---|---|---|
| F (paperwork) | compile.py precondition | pass — FACTCHECK.md · SHOTLIST.md · PROMPTS.md present |
| L (beat-mix lint) | compile.py | pass — code-cascade histogram is a WARNING (intentional) |
| D (audio decode) | compile.py `verify_output` | pass — 12 audio segments decoded; ~296.3 s |
| V (frame check) | runtime/qc/final_frame_check.py | pass — 0 BLOCKER, 0 MAJOR (24 frames sampled) |

## Absent checks

- `scripts/type_check.py` (not shipped in this toolkit) — replaced by direct visual read of the final contact sheet. See TYPECHECK.md.
- `reference/type-spec.md` — not shipped; brand tokens live in `runtime/remotion/src/tokens/claude.ts` and `runtime/remotion/src/tokens/layout.ts`, which are what Gate V's safe-area constants mirror.

## Blockers repaired during this build

1. **Wrong line numbers in B02** — previous build cited `art:81-86` for the shorts/vertical dispatcher cases. Source changed (new commands added); actual lines are now `art:102-107`. Fixed in beat_sheet.json and re-rendered B02.
2. **Stale "verbatim" claim in B03** — shorts.py SHORTS LAW docstring was expanded between builds; the condensed card version no longer matched. Removed "verbatim" claim; updated condensed code to accurately reflect current rules. Re-rendered B03.

## Retained from previous build (no change)

- All audio (mp3/beat-B00.mp3 … mp3/beat-B11.mp3) — narration unchanged, Kokoro am_onyx.
- B00, B01, B04–B11 media clips — source logic unchanged for these beats.
- Motion histogram: code-cascade 7/12 (58%) — WARNING, intentional for a command teardown. Documented, not a defect.

## Not attempted (out of scope for this invocation)

- Fresh network clone / `setup --install` — the isolated toolkit was already installed.
- The `--rewrite-outro` audio-regeneration path — not exercised end-to-end.
- The captured-media center-cut path — no captured media in this reel.
