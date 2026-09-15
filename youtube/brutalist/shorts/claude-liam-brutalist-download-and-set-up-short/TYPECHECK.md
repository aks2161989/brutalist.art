# TYPECHECK — Download Brutalist with Claude Code — Short

Run: `4b21324d56e84a3ca0cbfee8bc4b2f61`  ·  Date: 2026-09-11

## Scope

This is a visual typography review of the compiled Short at 2160×3840, based on frames sampled at 2 fps and at beat-relative 15% / 50% / 85% of each retained beat. The legacy `scripts/type_check.py` static type checker referenced in `skills/make/ai-explainer/SKILL.md` GATE T is not part of the current shorts.py + compile.py runtime; the check that IS available (frame-level visual QC + Gate V frame audit) was performed and its evidence is recorded here and in `CHECKS-REPORT.md`.

All type comes from independent copies of the parent vertical's per-beat Remotion renders (see `beat_sheet.json` — every kept beat's `filled_by` is a portrait Remotion composition). No text was regenerated or re-typeset in this run; typography is inherited byte-for-byte from renders that already passed the parent film's GATE T.

## §8.1 — min-size (readable body / spark type)

Passes. On every inspected frame:

- The dark-terminal readings in B04 (dependency column, feature column) remain readable at portrait size.
- Sparklines under illustrations (B06 "The tool has a shape. That shape is the honesty.", B07 "That is how you download Brutalist.") read clearly.
- Terracotta accent chips (e.g. `01 · CLONE`, `SETUP COST $0.00`, `● Verdict`) sit above the legibility floor.

## §8.2 — overflow

Passes. Every text element that carries variable-length copy uses the source component's `maxWidth` + wrap, not a fixed-width box. Verified per beat:

- B00 composer text ("Clone the public Brutalist toolkit into this folder and run the free setup doctor for me.") wraps inside the composer card at portrait width.
- B04 feature-column entries (`audio (Kokoro Bella/Onyx)`, `Remotion beats + backends`, `fonts (EB Garamond + Oswald)`) fit their column; dependency column wraps to two visible lines where needed (e.g. `ffmpeg / faster-whisper`).
- B05 lane cards each hold three-line bullet lists inside their card; no overflow.
- B06 subheads (`setup asks for zero credentials.`, `everything lives inside your clone.`, `~340MB Kokoro voice model from a GitHub release, the first --install.`) wrap inside their row.
- B07 verdict lines wrap without touching the safe inset.
- B09 title breaks at natural word boundary (`Download Brutalist\nwith Claude Code.`) inside the safe area.

## §8.3 — contrast

Passes. Every beat renders on the Claude fidelity palette: cream ground `#FAF9F5`, warm ink `#3D3929`, terracotta `#D97757` as the ONE accent. Contrast checks:

- Ink-on-cream body copy: pass.
- Terracotta-on-cream headline / spark / period: pass.
- Green terminal readings on the dark terminal card (B04): pass (the terminal is a dark card by design; readings are bright green on near-black — very high contrast).
- Muted / ghost lane in B05 ("Anthropic API — PAID · OPTIONAL") uses a lighter ink so viewers register it as the not-the-default lane; still passes the readability floor.

No `crispEdges` pixel-art rotation issues arise here (this Short uses no `ClaudeMascotScene` / `ClaudeMascotGrid` / `ClaudeTitleOutro` beats; the reel-local `DbcOutro916` in B09 does not rotate pixel-aligned rects).

## §8.4 — kerning sanity (Pango fallback catch)

Passes. All renders use the toolkit-bundled EB Garamond (serif) and system UI sans, loaded through Remotion — no Pango substitution path. Frame inspection shows no visible letter-spacing collapse in headings ("Green means ready.", "Subscription. Optional key. Free pipeline.", "What setup won't do.", "Download Brutalist, in three lines.", "Download Brutalist with Claude Code.") and no fallback-family bounding-box artifact on any inspected frame.

## §8.5 — no-wordy-card

Passes. Every retained beat's cards carry a headline plus at most three short lines / rows. Body prose sits in the narration, not on the frame (per SHOW-DON'T-TELL LAW). Two beats to spot-check:

- B06 uses three rows of ~3–8 words each — well under the wordy-card cap.
- B07's verdict card has three numbered lines, each a single spoken sentence — that IS the artifact's job (VERDICT act), not a slide.

## §8.6 — golden strings per rendered frame

Golden strings are visible on the expected beats:

- B00: `HUMANITARIANS AI · BRUTALIST`, `Download Brutalist`, `Ciao, Liam`, `@HumanitariansAI`.
- B04: `Green means ready.`, `$ ./setup`, `All core features ready.`, `Cost: $0.00.`
- B05: `Subscription. Optional key. Free pipeline.`, `Claude Code`, `Anthropic API`, `Brutalist pipeline`, `SETUP COST  $0.00`.
- B06: `What setup won't do.`, `No accounts created.`, `No files outside this folder.`, `No upload. One download.`, `~340MB`.
- B07: `Verdict`, `Download Brutalist, in three lines.`, `That is how you download Brutalist.`
- B09: `BRUTALIST · EPISODE 02`, `Download Brutalist with Claude Code.` (with terracotta period), `@HumanitariansAI`, `LIAM, IN FOR BEAR.`

All present.

## FAIL count

**0 FAIL, 0 WARN.** Typography is inherited from parent renders that already carry the parent film's GATE T / GATE V evidence; no new type was authored this run, so no new type defect could have been introduced. Human typography review pending.
