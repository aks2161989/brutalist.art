# Brutalist Playlist — Episode 03: Your First Brutalist Project

**Run ID:** `35a283c44f7e4830a26c6a84abf10319`
**Voice:** Kokoro `am_onyx` (Liam, in for Bear)
**Channel:** `@HumanitariansAI`
**Length:** 148 s landscape / 143 s portrait
**Status:** Renders complete, Gate V clean, **awaiting Bear's review** — not published.

## Deliverables

| Aspect | Master | Beat sheet | Review record |
|---|---|---|---|
| 16:9, 3840x2160 | `exports/landscape/claude-liam-brutalist-your-first-project.mp4` | `beat_sheet.json` | `VISUAL-REVIEW.json` |
| 9:16, 2160x3840 | `exports/vertical/claude-liam-brutalist-your-first-project-vertical.mp4` | `vertical/beat_sheet.json` | `vertical/VISUAL-REVIEW.json` |

Both aspects are **native re-authored layouts**, not crops. The portrait uses portrait-registered compositions (Composer916, HesitantWriter916, CodeBeat916, VerdictArtifact916, TitleOutroHAI916).

## The film in twelve beats

B00 the cold-open ask · B01 the hesitant writer BLUF (demo -> claim) · B02 what a beat sheet IS · B03 the concrete first ask · B04 what Claude actually reads and touches · B05 the review-cut receipt · B06 the one-beat revision ask · B07 the tiny on-disk diff · B08 two ratios, one film · B09 source to GitHub, video to Drive · B10 Your Turn prompt · B11 title restate (Liam, in for Bear — HAI).

## Paperwork per aspect

Landscape and portrait each hold:

- `FACTCHECK.md` · `SOURCES.md` · `SHOTLIST.md` · `PROMPTS.md` · `CHECKS-REPORT.md` · `TYPECHECK.md` · `BUILD-PROMPT.md`
- `VISUAL-REVIEW.json` — run_id-matched review evidence with SHA-256 of the master mp4, beat_sheet.json, and the human-review contact sheet.
- `_qc/REPORT.md` · `_qc/contact_sheet.png` · `_qc/human-review-contact.png` — from Gate V and a 1 fps sampling of the full compiled master.

## What Bear does next

Watch the two masters, note anything that misreads, and (if it lands) approve them for the human YouTube handoff. Runtime green is not publication approval.

## What was NOT done in this build

- No `./setup --install`, no `./art keys`, no live remote clones, no paid API calls. The audio was generated locally with Kokoro `am_onyx`; the visuals were rendered locally with Remotion (chrome-headless-shell in `--single-process` mode to survive the local sandbox).
- No `ClaudeTitleOutro` (locked to `@NikBearBrown`) was modified. A new isolated variant `ClaudeTitleOutroHAI` accepts a `handle` prop and defaults to `@HumanitariansAI`.
- No captions, subtitle track, or burned-in transcript was created; the reel teaches with legible on-screen labels and short code snippets only.

## Known limitations

- `scripts/type_check.py` / `reference/type-spec.md` are absent from this isolated toolkit; typography was reviewed by hand (image-capable Read tool). Documented in each aspect's `TYPECHECK.md`.
- Gate V's motion histogram warns `fade:7/12` — a design note, not a defect. The card content ANIMATES per beat per SHOW-DON'T-TELL LAW.
- `compile.py` skin lint flagged the HAI outro variant and the portrait Composer916 as "not the shipped default" — expected, both switches are the point of this playlist and are documented in `CHECKS-REPORT.md`.
