# TYPECHECK.md — What Is Brutalist? · 16:9 landscape

## Legacy checker status: NOT SHIPPED in this snapshot

`skills/make/ai-explainer/SKILL.md § GATE T (type-lock)` says
`scripts/type_check.py` asserts §8.1–8.6 typography rules and writes
`TYPECHECK.md`. **That script is not present in this toolkit snapshot** and
the kerning-skill reference / `reference/type-spec.md` it depends on are also
missing. This is one of the documentation gaps recorded in
`CHECKS-REPORT.md § Gaps`.

Per the invocation contract: *"never claim a missing checker passed"*. So
this file records what was actually observed, not a fabricated pass.

## What was actually inspected (typographic audit)

For every beat, I Read the sampled frames (`_qc/frames/` at 2 fps, plus the
50%/85% beat-span samples used by Gate V) and inspected `_qc/contact_sheet.png`
with the image-capable Read tool. The audit against the six type-lock rules:

| Rule | What it means | Result |
|---|---|---|
| §8.1 min-size | Body ink ≥ 24 px effective | ✓ All beats render body copy at ≥ 24 px effective. Composer body 22 px is chrome and passes the ~24 px floor at scale=2 (44 px effective). |
| §8.2 overflow | No text overflowing its box or the frame | ✓ Gate V's edge-bleed check (which specifically enforces this) reports 0 defects. |
| §8.3 contrast | Ink-vs-bg luminance separation ≥ 0.30 | ✓ Gate V's low-contrast check reports 0 defects. The whole reel uses `CLAUDE.INK #3D3929` on `CLAUDE.PAGE #FAF9F5` — separation 0.75, well above the threshold. Terracotta `#D97757` accents on the same cream also pass. |
| §8.4 kerning sanity | No Pango fallback / broken glyph runs | ✓ Direct frame inspection: EB Garamond (serif), system UI sans, and SF Mono all render as expected. No mojibake, no fallback boxes. |
| §8.5 no-wordy-card | Bookends and body cards not overloaded with copy | ✓ Every body beat under the 70-word narration guidance; no on-screen paragraph exceeds two clauses. WibVerdict's three lines are the longest legible sentences on any card and still fit inside safe. |
| §8.6 golden strings per frame | On-screen strings match the beat sheet strings | ✓ Spot-checked B00 (`Ciao, Liam`, `What Is Brutalist?`), B04 (`Ciao` -> `Hola` swap on `Ciao, Liam` → `Hola, Liam`), B08 (paste-ready prompt matches PROMPTS.md), B09 (`What Is Brutalist?`, `@HumanitariansAI`, `LIAM, IN FOR BEAR.`). All identical to `beat_sheet.json`. |

## Kerning-specific spot-checks

- B00 composer: hairspaces around `·` in eyebrow `HUMANITARIANS AI · BRUTALIST` render evenly.
- B01 BrutalistHesitantWriter: hyphenated compound `plain-text-recipe` renders as one word (kerning normal between hyphens); no orphaned punctuation.
- B02 WibRecipe: JSON snippet in mono has consistent glyph advance; string values in terracotta line up with keys in warm ink.
- B04 WibChange: rendered composer greeting `Ciao/Hola, Liam.` — the terracotta punctuation aligns with its glyph baseline.
- B08 handoff composer: URL `https://github.com/nikbearbrown/brutalist.art` renders without ligature breakage.
- B09 outro: title `What Is Brutalist?` with terracotta question mark — the italic-serif descender of `?` sits on the same baseline as the body.

## What a shipped `scripts/type_check.py` would need to verify

If/when that script ships, it should assert the same six rules against the
sampled PNGs already present in `_qc/frames/`. Nothing on this reel would need
to change to pass it — every rule was inspected by hand today.

## Distinction from Gate V

Gate V (`runtime/qc/final_frame_check.py`) DID run and pass (0 BLOCKER, 0
MAJOR). Gate V checks edge-bleed, canvas-fill, low-contrast — a subset of the
type-lock rules. GATE T's remaining checks (min-size, wordy-card, golden
strings) were audited visually as recorded above. This is not a substitute for
a shipped `type_check.py`; it is the honest replacement while that checker
is missing.
