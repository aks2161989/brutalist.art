# SCRIPT — Brutalist Command: art help (9:16 Short)

Slug: `claude-liam-brutalist-command-help-short` · run_id `d72074096c874f4582fbb787fcb1a7ba` · 2026-09-09.
Derived from `claude-liam-brutalist-command-help-vertical` (parent master SHA-256 `e3fb4d442ddabb32cf3370c44c0ee783c753b2f745e0578405388644304800d9`).
Focus of the Short: **what `./art help` actually does, at a high level — and where it stops.**

Kokoro `am_onyx` (Liam, in for Bear). Native 2160×3840. No captions.
Whole-beat cut of the parent vertical companion. No narration rewrites.
Every retained beat's audio and video is copied from the parent unchanged.

## Retained beats (in order)

| ID | Act | Pattern | Dur (s) | On-screen |
|---|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk916` | 17.13 | Composer: "What does ./art help actually do — and what does it not do?" · greeting "Namaste, Liam" · folder chip `@HumanitariansAI` · output list (17-line sheet, four aliases, different from `--list`) |
| B01 | BLUF | `BrutalistHesitantWriter916` | 9.75 | 4-line stack `art help / lists / every / skill.` → single trigger swap `skill` → `command` |
| B03 | MECHANISM | `ClaudeCodeBeat916` | 14.79 | `art:39` — two-sed pipeline extracts the file's own header, minus the hashes |
| B04 | WORKED_EXAMPLE | `ClaudeCodeBeat916` | 12.50 | Verbatim `$ ./art help` output — 17 lines, exits 0 |
| B05 | MECHANISM | `ClaudeCodeBeat916` | 15.71 | Four aliases (`empty`, `-h`, `--help`, `help`) → the one case pattern `""|-h|--help|help)` at `art:38` |
| B06 | CONTRAST | `ClaudeCodeBeat916` | 15.04 | `$ ./art --list` — the skills catalog (16 rows). `help = commands · --list = skills` |
| B09 | VERDICT | `ClaudeVerdictArtifact916` | 17.33 | Four scopes: `art help`, `art --list`, `art <skill> --help`, unknown-token exit 2 |
| B11 | OUTRO | `ClaudeTitleOutro916` | 5.13 | Locked title restate: "Brutalist Command: art help." · `@NikBearBrown` · slug-seeded mascot |

Total: **107.375 s** (measured on the final `.mp4` container, video and audio streams — all three equal).

## Dropped beats (recorded in `CUT-PLAN.json`)

- **B02 FRAMEWORK** — the whole-`case` walkthrough. The Short only needs the help body; B03 shows the actual sed pipe and B05 shows the four aliases hitting that body, so the wider tour was redundant.
- **B07 FALSIFIABILITY** — `./art bogus` failure worked example. The verdict at B09 already summarises the fall-through: *unknown token — exit 2, one line to stderr, points to `--list`*.
- **B08 RECOVERY** — `--list` then `<skill> --help`. B06 already contrasts help vs `--list`; B09 already states `art <skill> --help` opens the skill's SKILL.md in `$PAGER`.
- **B10 YOUR_TURN** — the long paste-into-Claude-Code diff-the-aliases prompt. Cut-first override permits dropping the extended exercise from a Short; the long film retains it.

## Coherence of the retained arc

1. **B00** sets both claims: four aliases share one branch, the help text is not stored — it is the file's own header extracted by sed at run time.
2. **B01** BLUF correction — "art help lists every **command**", not skill.
3. **B03** shows the actual sed body that produces the help (mechanism).
4. **B04** shows the verbatim output that mechanism produces (evidence).
5. **B05** shows the four aliases and the case pattern that ties them to that body.
6. **B06** contrasts with `--list` — the near-miss the audience is most likely to make.
7. **B09** verdict enumerates the four scopes as a wrap.
8. **B11** locked outro sign-off.

The verdict references `art <skill> --help` (SKILL.md via `$PAGER`) and the exit-2 fall-through without a prior worked example, but the audience is Brutalist fellows already using Claude Code and Unix conventions; the verdict lands as a summary line. See `CUT-PLAN.json` for the editorial record.
