# The sri-explainer Skill — Brutalist playlist episode 20

> **Re-verified 2026-09-12** (run_id `a960d8bf6f6e4238996f9688a426dab9`).
> Source `SKILL.md` updated: Notebook look camera rule corrected (static camera
> on ordinary 2D beats; orbit on 3D only). No beat content affected; films
> unchanged. Both aspects recompiled and Gate V re-run: BLOCKER=0 MAJOR=0.


Skill teardown of `skills/make/sri-explainer/SKILL.md`. AI-Explainer
visual treatment, Teardown register, narrated by **Liam, in for Bear**
(Kokoro `am_onyx`, local, free). Playlist adaptation for
**@HumanitariansAI**. 14 beats, 281.75 s, no captions.

Bear's viewing / editing is the next step — nothing here has been
published or uploaded.

## Deliverables

| Aspect | File | Size | Duration | SHA-256 |
|---|---|---|---|---|
| Landscape 16:9 | [`exports/landscape/claude-liam-brutalist-skill-sri-explainer.mp4`](exports/landscape/claude-liam-brutalist-skill-sri-explainer.mp4) | 3840×2160 | 281.75 s | `b0d0e60a03bda0e896525f74fe7bdb433cda8fd96403e8c1f51196edcfb8235a` |
| Portrait 9:16 | [`exports/vertical/claude-liam-brutalist-skill-sri-explainer-vertical.mp4`](exports/vertical/claude-liam-brutalist-skill-sri-explainer-vertical.mp4) | 2160×3840 | 281.75 s | `b11d283cfb7cea11ba354adae17c6962f9e569775aca2329261ffaa7744d4b49` |

The portrait is a **native 9:16 build**, not a cropped landscape master.
Every beat uses its `<Pattern>916` composition; three SkillTeardown
portrait variants were registered in the isolated toolkit's `Root.tsx`
for this reel.

Compiler receipts sit beside each master
(`*.verified.json`).

## Paperwork

Landscape:
`SCRIPT.md` · `SOURCES.md` · `FACTCHECK.md` · `SHOTLIST.md` ·
`PROMPTS.md` · `CHECKS-REPORT.md` · `TYPECHECK.md` ·
`VISUAL-REVIEW.json` · `BUILD-PROMPT.md` · `beat_sheet.json`.

Portrait (in `vertical/`): the same paperwork copied over unchanged
where it still applies, plus a portrait-specific `CHECKS-REPORT.md`,
`TYPECHECK.md`, `VISUAL-REVIEW.json`, and `beat_sheet.json`.

Frame QC evidence:
- Landscape contact sheet: [`_qc/contact_sheet.png`](_qc/contact_sheet.png)
- Portrait contact sheet: [`vertical/_qc/contact_sheet.png`](vertical/_qc/contact_sheet.png)
- Gate V reports: `_qc/REPORT.md` (both aspects, 0 blocker / 0 major).

## Honest limitations (documented on screen at B10)

- **No live end-to-end sri-explainer run.** A real chapter-to-video
  build would need a Prof Sridhar chapter file (e.g.
  `quantum-mechanics-vol1/chapters/*.md`), and none was ingested for
  this run.
- **`claude-sri` channel not wired in.** The skill file records that
  the new `claude-sri` channel needs to be added to
  `generate_audio_kokoro.py`'s `ALLOWED_VOICES` and
  `brand_variant.py`'s channel table before the first real build. That
  is not done in this toolkit snapshot — the reel uses `am_onyx`, which
  is already allowed.
- **No factcheck of a chapter's own numbers.** GOLDEN-TEST-ON-SCREEN
  LAW applies to a live run against a real chapter; this reel only
  describes the law from the SKILL.md.

## Next step

Bear watches both files, marks feedback in `FEEDBACK.md`, and either
approves for publication (out of this pipeline's scope — no upload
machinery here) or the next automatic attempt resumes with the
feedback in view.
