# SHOTLIST — Brutalist Command: art final — Short (ep 33)

6 Remotion beats, native portrait (9:16 2160×3840). Whole-beat cut of the
finished vertical parent — every retained mp4 is the parent's native portrait
render, copied unchanged into `media/`. No captions, no burned-in transcript,
no title-card slides, no endcard, no rewritten outro.

| # | id | pattern | motion | duration | on-screen |
|---|---|---|---|---|---|
| 1 | B00 | ClaudeComposerAsk916 | type-on | 14.85s | Cold-open Claude composer; greeting "Hei, Liam"; ask about verified 4K compile + last-good-file preservation; three-line output card. Folder chip `@HumanitariansAI`. |
| 2 | B01 | BrutalistHesitantWriter916 | hesitant-type | 11.65s | Big-serif BLUF: types `art final / renders once.`, then walks it back → `art final / verifies twice.` (accent terracotta on the doomed tokens). |
| 3 | B06 | ClaudeCodeBeat916 | code-cascade | 26.24s | Atomic candidate write from compile.py:805-827. TemporaryDirectory → verify_output → Gate V → validate_approvals → input-hash check → `os.replace`. |
| 4 | B07 | ClaudeCodeBeat916 | code-cascade | 24.77s | verified.json shape (5 keys); read-side pattern + three publication caveats. |
| 5 | B09 | ClaudeVerdictArtifact916 | artifact-in | 22.44s | Six-line recap: invocation · two verbs · fail-fast preflight · atomic write · receipt · slates block. |
| 6 | B11 | ClaudeTitleOutro916 | outro-card | 5.29s | Locked outro: title restate + `@NikBearBrown` handle + slug-seeded mascot. |

Planned total: **~105.3 s** (per-beat sum of the parent's Kokoro-measured
`render_duration_s`; add ~0.8 s lead silence on B01). Well below the strict
180 s Shorts cap. Final measured duration is recorded in `CHECKS-REPORT.md`.

## Dropped beats (not in this Short)

- B02 dispatcher case at `art:90-95` — plumbing detail; the long-form teardown carries it.
- B03 compile.py argparse surface — flag inventory belongs in the long.
- B04 `final_preflight` body — paperwork gating is asserted in B00 ("refuse if paperwork is thin") and B01 ("gates the paperwork"); B09 names it at a level the audience can follow without the verbatim source.
- B05 happy-path worked example — B07 shows the receipt, which is the concrete deliverable.
- B08 empty-FACTCHECK failure/recovery — the "last good file preserved" claim is the whole point of B06's atomic-replace mechanism.
- B10 Your Turn exercise — the Short need not read the long film's full CTA aloud (REPOLOOP-SHORTS-PROMPT).

## Per-beat visual constraints (retained beats)

- **B00** (composer): folder chip `@HumanitariansAI` (playlist adaptation).
  Send button arms after typing completes. Output lines cascade at RUN_START+18f.
- **B01** (BLUF): serif house font, ink `#3D3929`, accent `#D97757`, cream ground.
  `text` = `"art final\nrenders\nonce."`, triggers `renders, once` → replacements
  `verifies, twice`. Portrait uses lineSpacing 2.5 (per
  `feedback_hesitant_writer_portrait_bluf_recipe`).
- **B06 · B07** (code beats): white code card on cream page, terracotta first
  traffic-light dot, mono for code / SF Mono. Card height set by cream margins
  (top 8%, bottom 18%). Long code lines truncate horizontally in portrait —
  the card itself stays inside `SAFE916` so Gate V passes; fellows should
  prefer the landscape master for reading raw script contents.
- **B09** (verdict): white artifact card, six numbered lines, terracotta line
  numbers, spark-line-less (verdict card owns the whole frame).
- **B11** (outro): OUTRO-LOCK — title restate with terracotta period,
  `@NikBearBrown` handle hardcoded (per `OUTRO-LOCK.md`), slug-seeded mascot.
