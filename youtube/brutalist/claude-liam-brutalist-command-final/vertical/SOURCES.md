# SOURCES — Brutalist Command: art final (ep 33)

## Primary sources (from `SOURCE-SNAPSHOT.json`)

| File | SHA-256 | Role |
|---|---|---|
| `art` | `9bb77a7c84701d23ab6e73f0a4f48592f17748ffad2c7114b62687bb7f97d0e9` | Top-level dispatcher; case `final)` at art:90-95 is the subject. |
| `runtime/scripts/compile.py` | `047e9fa6d0944f54c284ed16df8b4d847f62737a0e263a0f4bf0bad2b11f446c` | The compiler + assembler + final_preflight + atomic replace + verified.json writer. |

Combined source_sha256 for the two named files (per `episode.source_sha256`):
`15dc70372375121fb4a194daa1bac7042ceb4f232345e27a08a353cd14129a10`.

## Supporting doctrine

| File | SHA-256 | Role |
|---|---|---|
| `skills/make/ai-explainer/SKILL.md` | `a7421d4d861b44a983a31e9fcd7451cd32312a139366e74acc2123dfdefbd3c0` | Register, bookend law, house laws (COLD-OPEN, EXECUTIVE-SUMMARY, OUTRO, HANDOFF). |
| `skills/make/nopunt/SKILL.md` | `ef38a574fe22f2fca1dfa0774bc51681252776f8ef2bd6f2b1e52d6478cab505` | PROOF GATE — SHOW/HOLD/CARD classification for every beat. |
| `runtime/prose/teardown/PROSE.md` | `6accc1a576ca9b52713abd31507f5deece6dc2612ca90967b25b661e59111786` | Teardown register (Feynman × MKBHD) — explain the machinery, judge the design. |
| `docs/PIPELINE-SAFETY.md` | `4619f0d4702317d654cd6498cadc8c277691e4c7565920ef851dbb628aa6298d` | The runtime contract this episode teaches — atomic replace, receipt semantics, "reviews are not finals". |
| `docs/FELLOWS-SUBMISSION.md` | `7825c728f040b0f7a49bbd950a5a2bef70c8a59ff2fbe0538716c8d3381f5223` | YouTube 4K processing caveat, README template, publication is separate. |
| `CLAUDE-BRAND.md` | (in the toolkit; unchanged this session) | Claude palette (`CLAUDE.PAGE / INK / SPARK`), spark-line law, illustrate law. |
| `OUTRO-LOCK.md` | (in the toolkit; unchanged) | Locked outro card: title restate + hardcoded @NikBearBrown handle + slug-seeded mascot. |
| `CLAUDE-CODE-VISUAL-QC-CHECK.md` | (in the toolkit; unchanged) | Frame-level VISUAL QC LAW procedure that Gate V implements. |
| `REPOLOOP-PROMPT.md` | `abf55bdc729a9c30216e4375dff0c62b4bf5af4c717ad28be69709de64d5bc97` | Supervisor prompt — read for boundary rules (no publication, no paid API, isolated toolkit). |

## Demo evidence

- `demo/RUN-LOG.txt` — verbatim `./art final` output captured from this
  workstation on 2026-09-09, run against:
  - `/tmp/claude-501/art-final-demo/` (success + failure/recovery on empty FACTCHECK.md)
  - `/tmp/claude-501/art-final-slate-demo/` (final rejects an unfilled slate)
- The SHA-256s in the on-screen verified.json card at B05 are the actual values
  written to `/tmp/claude-501/art-final-demo/exports/art-final-demo.verified.json`
  during this session, elided for card width. Full values in RUN-LOG.txt.

## Human signatures

None. This build has zero `metadata.approvals` entries because the reel is a
plain command teardown (`kind: command`) — it does not arm the fellows voice
gate or a professor-notes gate. The `build_safety.py` auditor was covered
independently in ep 32 (`command-approvals`).

The final export's `verified.json.status = "ready"` is a machine claim about
the automated checks; **human review is pending**. Bear watches both aspects
and either signs off in `FEEDBACK.md` or requests targeted per-beat rebuilds.

## What is NOT a source

- No screenshots. Every beat is a native Remotion render at the fidelity
  palette (per REBUILD LAW). The only "screenshot"-shaped image in this reel
  is the `_qc/previews/*.png` sampled from the actual Remotion mp4s during
  visual review.
- No AI image/video generation. Zero Higgsfield calls, zero image APIs.
- No captions/SRT/VTT. Legible on-screen code and labels only.
