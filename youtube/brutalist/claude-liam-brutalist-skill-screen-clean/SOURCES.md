# SOURCES — The screen-clean Skill (Brutalist episode 19)

## Primary source

- Repository path: `skills/make/screen-clean/SKILL.md`
- Upstream repo: https://github.com/nikbearbrown/brutalist.art
- `episode.source_sha256`: `df40ee6226bb543052625f6549ccf753a83f1c7f7a318c748ec10e52d80b2fc7`
- Isolated-toolkit capture SHA-256 (per `SOURCE-SNAPSHOT.json`): `c50640bff9f4de41030672d6c4de48cfb110aa398d302b1ba8d11f4ddb7c6efb`
- Toolkit commit: `ba2d0e0f043f5b3b35a50d336e0fc66fbfecfc0c` (with local overrides listed in the snapshot)
- Read verbatim in full for this teardown.

## Verbatim quotes displayed on screen

All quotes on `SkillTeardownMechanism` cards are lifted directly from the
SKILL.md above, cited as `screen-clean SKILL.md · <section>`:

- Mechanism 1 (shared, ignorant): "**Format is orthogonal to relationship.**
  Anything that ingests a recording calls this." — § "Why it is shared, not
  built into one skill".
- Mechanism 2 (audio gate): "**If mean_volume is below -40 dB, STOP.** The
  recording is silent and every downstream stage will happily build a dead
  episode around it. Never infer audio from the presence of an audio stream —
  decode it." — § "Pass 1 — probe and audio gate".
- Mechanism 3 (aspect fit): "**Measure the taskbar. Do not assume it.**" and
  "**Bars are Claude cream `#FAF9F5`, never black.**" — § "Pass 2 — aspect fit".
- Mechanism 4 (privacy): "Print the list, mark which items **survive the crop**
  and which the crop removes, and **wait for a human**. Never auto-blur and
  never decide on someone's behalf — 'is this embarrassing' is judgment, not
  arithmetic, so this pass flags rather than loops to a fix." — § "Pass 4 —
  privacy scan (flag, never decide)".
- Falsifiability (contact sheet): "**The proof is the review artifact, not the
  numbers**" and "Four frames, not one — the shared screen changes." —
  § "Pass 2 — aspect fit / The proof is the review artifact".
- Verdict: quotes are the source's own output-contract lines, § "Output
  contract".

## Aspect-fit numeric table

The A / B / C table used in beats B03 and B06 is quoted verbatim from
`SKILL.md` § "Pass 2 — aspect fit" (2560×1600 source, ~72 px taskbar). No
numbers are invented; the table is redrawn in the fidelity palette per
REBUILD LAW and labelled "Redrawn from screen-clean SKILL.md" on screen.

## Read-only example leads

Per BRIEF.md the following two beat sheets were provided as reference DATA:

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — SHA-256
  `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`
  (local study copy: `.repoloop/workspaces/.../examples/746409a8715e.json`).
- `shivpriya-mane/2026-08-11-marley-tools/beat_sheet.json` — SHA-256
  `4213b45a19fff41e89b892941de181be03d1056ae9bb00d8f8e1e51d2f4420bc`
  (local study copy: `.repoloop/workspaces/.../examples/4213b45a19ff.json`).

Both were read for staging patterns only. Their audio, human signatures,
research findings, Drive URLs and outputs were NOT reused. No claim in this
film is sourced to them; every claim is sourced to `screen-clean/SKILL.md`.

## Local safe demo (Pass 1)

- Two synthetic fixtures generated in `demo/` with `ffmpeg -f lavfi` — one
  silent (`anullsrc`), one voiced (440 Hz sine at ~-21 dB). Both are 6-second
  2560×1600 fills in a dark-desktop grey.
- Real `ffprobe` + `ffmpeg -af volumedetect` output captured in
  `demo/screen-clean-run.log`. The silent fixture measures `mean_volume =
  -91.0 dB` (STOP verdict); the voiced fixture measures `-21.1 dB` (proceed
  verdict).
- No real personal screen recording was ingested. Nothing external was
  contacted; nothing was published.

## What did NOT run

- `screen-clean` is a shared preprocessor called by `fellows` and `guests`;
  its `SKILL.md` documents behaviours (list of privacy items, contact-sheet
  render, dead-air trim, --silent mode). This film does not exercise those end
  to end on a real recording — the film's demo covers Pass 1 only. Passes 2–5
  are illustrated per REBUILD LAW from the SKILL.md and clearly labelled as
  redrawn.
- No paid TTS, no API keys, no publishing, no upload. Kokoro `am_onyx`
  narrated every beat locally.
