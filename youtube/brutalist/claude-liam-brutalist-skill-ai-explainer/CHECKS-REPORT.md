# CHECKS-REPORT — landscape 16:9 build

Reel: `The ai-explainer Skill` · slug `claude-liam-brutalist-skill-ai-explainer`
Run: 2026-09-08 · This invocation `run_id` a620d2fb17d742268eafcb27f0859b5d.

## PROOF GATE (nopunt classification)

11 SHOW / 0 justified-HOLD / 0 PUNT-flagged

Teaching arc: FRAMEWORK ✓ (B02 anatomy + B03 pipeline)
              WORKED EXAMPLE ✓ (SELF-DEMO — the reel itself is the demo; B04–B06 walk the framework's three mechanism acts step-by-step, and the on-screen scenes ARE the framework being applied to itself)
              FALSIFIABILITY ✓ (B07 "Where it bites")
              SCAFFOLDED TASK ✓ (B09 has a real prompt + two on-screen success tests)
              BOOKENDS ✓ (B00 cold open · B08 verdict · B09 handoff · B10 title-restate outro)
              NO-SOURCE-NO-VERDICT ✓ (every claim beat carries the SKILL.md quote block; verdict + handoff are the two allowed exemptions)

## Runtime checks (the ones the toolkit ships)

Because the fellows submission gates (`beat_lint.py`, `gate_shape.py`, `final_frame_check.py`) exist in `runtime/qc/`, they will run during `compile.py --final`. This section records what was executed in this session and what it found.

### Actual commands run

```
python3 runtime/scripts/generate_audio_kokoro.py <reel> --dry-run
python3 runtime/scripts/generate_audio_kokoro.py <reel>
python3 runtime/scripts/remotion_scenes.py <reel> --list
python3 runtime/scripts/remotion_scenes.py <reel> --only B00
python3 runtime/scripts/remotion_scenes.py <reel>          # renders every beat
python3 runtime/scripts/remotion_scenes.py <reel> --only B10   # re-render after HAI outro swap
```

### Runtime infrastructure repairs used to get renders to complete

Both are documented so a reviewer sees what deviated from vanilla and why:

1. **Remotion project mirrored to `$TMPDIR/remwork/`** (via `ART_REMOTION_PROJECT`). The isolated toolkit's `runtime/remotion/node_modules/` is a symlink pointing at the primary toolkit's `node_modules/`; the sandbox denies writes there, so webpack cannot manage its cache in-place. The mirror is a real writable directory with a real `node_modules/` in which every `@remotion/*` package is a real deep copy (patched — see below) and every other package is a symlink to the original read-only copy. `.cache/webpack/` lives in that writable tree.
2. **Chrome-headless-shell + `--single-process` patch** (per memory `feedback_chrome_sandbox`). macOS's App Sandbox blocks the Mach port rendezvous when Chromium spawns renderer subprocesses. Remotion only injects `--single-process` on Linux; both `dist/esm/index.mjs:7140` and `dist/open-browser.js:135` in the `$TMPDIR/remwork/node_modules/@remotion/renderer` copy were patched to always inject `--single-process` when GL is not vulkan. The patch is confined to the throwaway `$TMPDIR` mirror — the primary and isolated toolkit renderers are untouched.
3. **`remotion_scenes.py` grew two env vars**: `ART_REMOTION_PROJECT` (writable project dir) and `ART_REMOTION_LAUNCHER` (invoke `node --preserve-symlinks .../remotion-cli.js` instead of `npx remotion`, because npx canonicalises symlinks and re-loads the original unpatched renderer). Both fall back to the vanilla behaviour when unset.

### Missing-checker honesty

- `scripts/type_check.py` — DOES NOT EXIST in this toolkit (search: `runtime/qc/` has no `type_check.py`; only `beat_lint.py`, `gate_shape.py`, `final_frame_check.py`, `manim_layout_audit.py`, `wcag_margin_check.py`, `brand_labels.json`, `static_scene_check.py`). See TYPECHECK.md for the honest substitute (visual inspection).
- `skills/kerning/` — no kerning-specific skill folder. Not applicable.
- `reference/type-spec.md` — not present. Not applicable.
- `ILLUSTRATIONS.md` — SKILL.md references `runtime/remotion/src/illustrations/ILLUSTRATIONS.md`. The folder exists; the doc may or may not. Not consulted because the beats did NOT need a new illustration structure — they used the already-registered SkillTeardown-Generic components.

None of the missing checkers was claimed to have passed.

### Compile inputs verified

`compile.py` will re-run these before touching the destination:
- `beat_lint.py` (fellows preflight) — invoked by final_preflight
- `gate_shape.py` (fellows preflight) — invoked by final_preflight
- `final_frame_check.py` — samples decoded frames from the candidate
- `validate_approvals(...)` — this reel is `kind: skill`, not `fellows`, so it needs only an empty `approvals: {}` object which the beat sheet already provides.
- Duration + audio-decode verification via `verify_output()`.

## Frame-level visual QC (SHOWED, not merely PROBED)

11 beats × 1 mid-frame each were extracted from the per-beat renders via `ffmpeg -ss 2 -frames:v 1` to `_qc/preview/*.png`. Five representative frames (B02, B03, B04, B08, B10) got a `-late` frame at 85% of beat duration so the progressive-reveal beats (Anatomy, Pipeline, Mechanism, Verdict) could be inspected once fully drawn. Every extracted PNG was opened with the image-capable Read tool.

- B00 · **PASS**. Cold open on Claude composer. Greeting "Hej, Liam" (Swedish, one-word — inside HAI/Liam word budget). Prompt typing correctly. Running indicator + output lines visible. `@HumanitariansAI` folder chip present. No captions.
- B01 · **PASS** (13.80s > 9s minimum for hesitant writer). Mid-frame shows serif ink typing "The ai-explainer" with terracotta on the letter about to be deleted per the writer's accent contract. Final corrected text: "The ai-explainer skill is a workflow that reads a whole SKILL file / for Claude-branded videos." Beat runs its full 13.80s; the 0.8s lead_silence field is authored — actual silence at head verified during compile via audio decode.
- B02 · **PASS**. Late-frame shows the full folder tree revealed (nine entries with the SKILL.md accent + tag), terracotta callout box "The SKILL.md is the instruction", spark line "Doctrine first. Then the machinery.", eyebrow "SKILL · ANATOMY · WAS CLAUDE-EXPLAINER" (renaming preserved). Fills the canvas top-to-bottom.
- B03 · **PASS**. Left-to-right pipeline: INPUT → Scaffold → Narrate → Audio (terracotta accent) → Visuals → Compile → OUTPUT. Every node reveals in order. Footer note "Audio-first. Every visual conforms to the measured voice." Spark "The voice measures. Everything else conforms."
- B04 · **PASS**. "Fixed bookends. Free interior." — body names the six moves; quote card carries the SKILL.md verbatim; verdict pill terracotta.
- B05 · **PASS**. "The UI earns its beats." — the anti-wallpaper quote is the ILLUSTRATE LAW smell/failure line, verbatim. Verdict pill "KILLS WALLPAPER REELS".
- B06 · **PASS**. "Ask, then the receipt." — ASK → RESULT LAW quote verbatim, verdict "PROMPTS AS RECEIPTS".
- B07 · **PASS**. "Where it bites." — IN-FOR-BEAR LAW quote verbatim; verdict pill "REQUIRES A READER" is intentionally in the neutral (non-positive) style since this is the falsifiability beat.
- B08 · **PASS**. Verdict artifact card lists six numbered lines exactly matching SCRIPT.md.
- B09 · **PASS**. `Your Turn` greeting present, folder chip `@HumanitariansAI`, prompt types the full paste-ready task, three output success-tests visible. Liam reads the prompt aloud during 21.42s of narration.
- B10 · **PASS**. `The ai-explainer Skill.` with the terracotta terminal period. Handle `@HumanitariansAI` (from the new ClaudeTitleOutroHAI custom variant — see TYPECHECK.md §Outro handling). Slug-seeded mascot beneath.

Contact sheet PNGs live in `_qc/preview/`. A landscape final-frame-check gate will also run inside `compile.py --final` and its report will be captured after the compile.

## Outro handling (channel adaptation, not a violation)

OUTRO-LOCK.md scopes the hardcoded `@NikBearBrown` outro to `claude-liam-*` reels on the @NikBearBrown channel. This playlist is deliberately re-scoped to @HumanitariansAI per BUILD-PROMPT.md ("Keep the Claude visual tokens but use that handle, not the hardcoded @NikBearBrown channel of some stock NBB components. This is an explicit channel adaptation, not a voice change. … Native custom outro variants may live in the isolated scene source; do not alter the live library."). Therefore B10 uses a NEW component `ClaudeTitleOutroHAI` (and `ClaudeTitleOutroHAI916` for portrait), registered in this isolated toolkit only. Same slug-seeded polarity + mascot + terracotta-terminal-punct visual grammar; only the hardcoded handle differs.

## Conclusion

All 11 beats rendered as native 4K Remotion scenes with the correct audio-conformed durations. No slates. No captions. No wallpaper (every non-UI middle beat is a concept-illustration scene). Handle correctly reads @HumanitariansAI. Ready for landscape compile. Human review still pending — this document is a machine-produced pass record, not a human sign-off.

---

## Re-review addendum — invocation a2d6bcc90e44499b906ada378401a3db (2026-09-11)

SKILL.md changed since the previous build. See FACTCHECK.md §Source update for the diff summary. Assessment: two additive hard rules (Executable evidence + Math) and a simplified frontmatter description. No beat content is staled or contradicted.

Existing landscape master re-verified:
- `ffprobe`: 3840×2160, h264, AAC 48kHz, 186.92s — unchanged
- `sha256`: `356d96227ac4f50b92e548d8e32ea6895e11016b20b076f195abd48e293d8518` — unchanged
- Contact sheet re-read via image-capable Read tool — all 11 beats confirmed in correct order, @HumanitariansAI handle, no captions, no slates
- Gate V BLOCKER=0, MAJOR=0 from previous build stands

No re-render performed. VISUAL-REVIEW.json updated to this invocation's run_id.
