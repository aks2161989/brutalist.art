# SHOTLIST — Brutalist Command: art final (ep 33)

12 Remotion beats · one landscape build (16:9 3840×2160) + one native portrait
companion (9:16 2160×3840, `vertical/`). No captions, no burned-in transcript,
no title-card slides — every code beat carries a real code artifact from the
`art` dispatcher or `compile.py`.

| # | id | pattern | motion | duration | on-screen |
|---|---|---|---|---|---|
| 1 | B00 | ClaudeComposerAsk | type-on | 14.85s | Cold-open Claude composer; greeting "Hei, Liam"; ask about verified 4K compile + last-good-file preservation; three-line output card. Folder chip `@HumanitariansAI`. |
| 2 | B01 | BrutalistHesitantWriter | hesitant-type | 11.65s | Big-serif BLUF: types `art final / renders once.`, then walks it back → `art final / verifies twice.` (accent terracotta on the doomed tokens). |
| 3 | B02 | ClaudeCodeBeat | code-cascade | 18.67s | Dispatcher case at `art:90-95`. Two-branch `case " $* " in` for `--height`. |
| 4 | B03 | ClaudeCodeBeat | code-cascade | 22.19s | compile.py argparse surface: `folder`, `--review`, `--fps`, `--height`, `--audio`, `--force`, `--allow-slates`, `--out`, `--sheet`. |
| 5 | B04 | ClaudeCodeBeat | code-cascade | 19.97s | `final_preflight()` body (compile.py:451-463) + call site (compile.py:629). |
| 6 | B05 | ClaudeCodeBeat | code-cascade | 25.43s | Verbatim `$ ./art final /tmp/…-demo …` stdout + verified.json body (elided SHA-256s). |
| 7 | B06 | ClaudeCodeBeat | code-cascade | 26.24s | Atomic candidate write from compile.py:805-827. TemporaryDirectory → verify_output → Gate V → validate_approvals → input-hash check → `os.replace`. |
| 8 | B07 | ClaudeCodeBeat | code-cascade | 24.77s | verified.json shape (5 keys); read-side pattern + three publication caveats. |
| 9 | B08 | ClaudeCodeBeat | code-cascade | 25.37s | Verbatim BEFORE/EDIT/AFTER/RECOVERY. Refusal → `GATE F: missing or empty FACTCHECK.md`. SHA-256 unchanged. |
| 10 | B09 | ClaudeVerdictArtifact | artifact-in | 22.44s | Six-line recap: invocation · two verbs · fail-fast preflight · atomic write · receipt · slates block. |
| 11 | B10 | ClaudeComposerAsk | type-on | 22.14s | Your Turn composer; 5-step paste-ready prompt (art final → cat verified.json → shasum → compare → investigate on drift). |
| 12 | B11 | ClaudeTitleOutro | outro-card | 5.29s | Locked outro: title restate + `@NikBearBrown` handle + slug-seeded mascot. |

Total measured duration: **239.44 s** (per-beat sum of Kokoro-measured
`actual_duration_s`). Frame padding to next frame boundary happens in
`prepare_timeline`.

## Per-beat visual constraints

- **B00 · B10** (composers): folder chip `@HumanitariansAI` (playlist adaptation).
  Send button arms after typing completes. Output lines cascade at RUN_START+18f.
- **B01** (BLUF): serif house font, ink `#3D3929`, accent `#D97757`, cream ground.
  `text` = `"art final\nrenders once."`, triggers `renders, once` → replacements
  `verifies, twice`. Portrait variant uses lineSpacing 2.6 not fontSize bump (see
  `feedback_hesitant_writer_portrait_bluf_recipe`).
- **B02–B08** (code beats): white code card on cream page, terracotta first
  traffic-light dot, mono for code / SF Mono, ~24-26px lines. Card height set
  by cream margins (top 8%, bottom 18%).
- **B09** (verdict): white artifact card, six numbered lines, terracotta line
  numbers, spark-line-less (verdict card owns the whole frame).
- **B11** (outro): OUTRO-LOCK — title restate with terracotta period,
  `@NikBearBrown` handle hardcoded (per `OUTRO-LOCK.md`), slug-seeded mascot.

## Portrait companion (`vertical/`)

Same 12 beats, `*916` scene ids. `ClaudeCodeBeat916` was registered in this
build (see PROMPTS.md § patches). Long code lines truncate horizontally in
portrait — the card itself stays inside `SAFE916` so Gate V passes; fellows
should prefer the landscape master for reading raw script contents. This
matches the ep-29/32 behaviour, documented in each aspect's `CHECKS-REPORT.md`.
