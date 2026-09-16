# CHECKS-REPORT — Brutalist Command: art keys · landscape (3840×2160)

**Episode**: 36 · `command-keys` · Brutalist playlist · @HumanitariansAI
**Run ID**: `b7896f5b2d2a441186ff1451881c0a5b` (re-verified 2026-09-13; previous run abdef8f04e1246deaf8cf7ab26ae350b interrupted by Claude usage limit — exports unchanged)
**Master**: `exports/landscape/claude-liam-brutalist-command-keys.mp4`
**Duration**: 218.583 s · **Beats**: 12 · **Slates**: 0
**Master SHA-256**: `6c86395efba7a96cafd4ee6d99a8b22fcf9951c502bdde9e46d18ce521e3fadf` (unchanged — re-verified 2026-09-12)

## Beat classification (proof gate, per skills/make/nopunt/SKILL.md)

12 SHOW · 0 HOLD · 0 CARD · 0 PUNT · 0 slates · 0 skin warnings on the landscape master.

| Teaching-arc item | Status | Where it lands |
|---|---|---|
| FRAMEWORK before EXAMPLE | ✓ | B02 dispatcher + B03 four-status taxonomy precede B04/B05 verbatim runs. |
| WORKED EXAMPLE (real, not synthesised) | ✓ | B04 (invalid, higgsfield offline) + B05 (unset, higgsfield removed from PATH), both verbatim from `demo/RUN-LOG.txt`. |
| FALSIFIABILITY | ✓ | B08 shows the docstring's exit-1-on-invalid promise vs the actual code (`any_invalid = False` never reassigned) — the reel is falsifiable by re-running the script on any box and inspecting `echo $?`. |
| SCAFFOLDED VIEWER TASK | ✓ | B10 handoff: audit the script (do NOT fix it) and write one pytest that would fail today and pass if the promise were kept. |
| BOOKENDS (ask → verdict → handoff → title) | ✓ | B00 ClaudeComposerAsk cold open · B09 ClaudeVerdictArtifact · B10 Your-Turn composer · B11 title outro. |
| NO-SOURCE-NO-VERDICT | ✓ | Every code beat cites either a line range in `check_keys.py` / `art` or a section of `demo/RUN-LOG.txt`. FACTCHECK.md tracks each claim. |

## Command log (verbatim, in build order)

```
$ python3 runtime/scripts/generate_audio_kokoro.py \
    <reel>
  → 12 beat mp3s at $0.00, kokoro am_onyx, durations 5.4–32.0 s

$ python3 runtime/scripts/remotion_scenes.py <reel>
  → 12 media/B*.mp4 rendered via chrome-headless-shell --single-process
    (ART_CHROME wrapper), foreground, serial concurrency 1.
  → After B06 was inspected and shortened (top 3 lines removed so all
    four exception branches fit inside the code card), B06 was re-rendered
    with `--only B06 --force`.

$ python3 runtime/scripts/compile.py <reel> \
    --height 2160 --out <reel>/exports/landscape [--force]
  → wrote exports/landscape/claude-liam-brutalist-command-keys.mp4
    (218.583 s, 3840×2160, h264 yuv420p, aac audio, PIL overlays)
  → wrote exports/landscape/claude-liam-brutalist-command-keys.verified.json
```

## GATE V — final frame check (landscape)

- Sampler: `runtime/qc/final_frame_check.py` (SAFE inset x96-1824 y54-1026,
  scaled to 3840×2160; FILL_MIN 0.55).
- **frames=24 · BLOCKER=0 · MAJOR=0**.
- Report: `_qc/REPORT.md`.
- Extended proof frames (36 total) at `_qc/proof-landscape/{B00…B11}-{15,50,85}.png`
  — 15%, 50%, 85% of each beat's on-screen span from the beat sheet.
- Contact sheet: `_qc/contact-sheet-landscape.png` (SHA-256
  `416d33bcfa75090200fb2cf58554ea2626fbc1d2d9d888791124d1da8b5df241`).
- Every proof frame in `_qc/proof-landscape` was `Read` with the
  image-capable Read tool; spot checks below.

## Frames actually viewed (image-capable Read, not just probed)

| Frame | What it establishes |
|---|---|
| B00-50 | Cold open composer with "Habari, Liam" greeting typed; ask lands answered with three output lines under runningText. |
| B01-85 | Corrected BLUF settles as "art keys / audits upgrades." Two-line composition covers the safe area. |
| B02-85 | Dispatcher case `art:103-104` — code card shows the two-line `keys)` branch. |
| B03-85 | Four-status taxonomy: valid / invalid / unset / warn, mapped to the emoji marks the table prints. |
| B04-85 | Verbatim `./art keys` invocation with higgsfield offline — red `❌ invalid` row followed by green "All present keys validated." + `[exit 0]`. |
| B05-85 | Verbatim `./art keys` invocation with higgsfield removed from PATH — yellow `· unset` row + `[exit 0]`. |
| B06-85 | The full 17-line probe body (`check_keys.py:44-58`) — try/except FileNotFoundError/except Exception, all four branches visible. |
| B07-85 | `load_env` body + the `grep -c 'this-should-never-print' → 0` redaction proof. |
| B08-85 | Side-by-side of docstring promise vs `any_invalid = False` reality + the `SI key` help drift. |
| B09-85 | Verdict artifact — six lines summarising the whole surface. |
| B10-85 | Your Turn composer with the audit prompt and three grading lines. |
| B11-50 | Outro title restate + `@NikBearBrown` handle + slug-seeded mascot. |

## Skin lint

`code-cascade` carries 7/12 beats (58%) — over the ~40% MOTION.md pantry
cap. Justification: this is a command teardown of a Python script; the code
IS the subject. The alternative would be to substitute Manim illustrations
for code beats, which would violate ILLUSTRATE LAW (the interface is the
subject). Documented in BUILD-LOG rationale rather than corrected.

## Landscape-specific portrait fixes NOT applied here

- `channel_title: "@HumanitariansAI"` IS included in landscape metadata —
  compile.py's PIL overlay fits inside the burn-in exclude at 3840-wide.
  (Removed only from the vertical sheet; see vertical CHECKS-REPORT.md.)

## Outstanding limitations

- **OUTRO-LOCK**: the outro card's handle is hardcoded `@NikBearBrown`
  even though this episode belongs to @HumanitariansAI. This is
  intentional per `OUTRO-LOCK.md` (locked component; changing it would
  require altering the shared component in the isolated toolkit, which
  the BUILD-PROMPT forbids). Flagged in `README.md` for the human
  reviewer.
- No shipped `scripts/type_check.py` in this toolkit — see `TYPECHECK.md`
  for the visual typography audit that stood in.
- Human review pending.
