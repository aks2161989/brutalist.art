# TYPECHECK — Brutalist Command: art icon-build — Short (9:16)

## The legacy type checker

`runtime/scripts/type_check.py` and the shipped kerning skill referenced in `ai-explainer/SKILL.md` are **not present** in this toolkit snapshot. As on the parent vertical, this file distinguishes the absent legacy checker (unavailable, would fail equivalently on the parent) from the actual visual typography review below, which was done.

## Actual visual typography review

Nine-point rubric per `CLAUDE-CODE-VISUAL-QC-CHECK.md`, applied to the extracted 15 % / 50 % / 85 % frames listed in `CHECKS-REPORT.md § 6`:

| # | Check | Result |
|---|---|---|
| 1 | **Serif consistency (EB Garamond)** — greetings, verdict headings, outro title | Pass. Same weight and rendering as parent 9:16. |
| 2 | **Mono consistency (SF Mono)** — code cards on B04, B06 | Pass. Character grid intact; no anti-alias smear at 2160×3840. |
| 3 | **Cream ground `#FAF9F5`** | Pass in every retained frame. |
| 4 | **Warm ink `#3D3929`** | Pass. |
| 5 | **Terracotta spark `#D97757`** — B00 upload button, B01 trigger words, B04 rule digits, B06 header dot, B09 numbered digits, B11 accent period | Pass on every beat. |
| 6 | **Safe-area coverage ≥ 55 %** — measured by visible ink bbox on each 50 % frame | Pass. B01 BLUF fills the vertical safe area at ~65 %+ thanks to the portrait-scale patch baked into the parent render. |
| 7 | **No burned-in captions / subtitles** | Pass. The compiler ran without `--review`; nothing overlays the clips. |
| 8 | **Portrait framing (no cropping seam, no letterbox)** | Pass. All six retained clips are native 2160×3840 renders, copied byte-identical from the parent. |
| 9 | **Outro contract** — `@NikBearBrown` hardcoded, slug-seeded mascot | Pass. B11 frame at 108.570 s shows title, handle, mascot region. |

## Minor observation

- **B06 header wraps `--dry-run   (verbatim from this workspace)`** — the trailing `)` clips at the right composition edge. This is identical to the parent 9:16 render (same source clip, byte-identical). No regression introduced by the Short cut. Logged as a minor in `VISUAL-REVIEW.json` for the parent's next revision, not this Short's.

## Slate / skin-lint

- No slate placeholders — 6 / 6 beats filled with real video.
- `SKIN LINT` for `ClaudeComposerAsk916` / `ClaudeTitleOutro916` in the compile log are expected false positives (see `SHOTLIST.md § Compiler SKIN-LINT expected notice`).

## Conclusion

Typography and colour contract holds across every retained beat. No majors, no blockers. Human typography review of the parent vertical (already done) is unchanged in the Short because every clip is byte-identical.
