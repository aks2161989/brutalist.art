# SOURCES — The screen-clean Skill — Short

Derivative of `youtube/brutalist/claude-liam-brutalist-skill-screen-clean`
(the 16:9 long / full-length native vertical). This Short does not
re-execute the demo — it reuses parent narration + native portrait renders
unchanged.

## Primary source (doctrine)

- Repository path: `skills/make/screen-clean/SKILL.md`
- Upstream repo: https://github.com/nikbearbrown/brutalist.art
- `episode.source_sha256`
  (parent): `df40ee6226bb543052625f6549ccf753a83f1c7f7a318c748ec10e52d80b2fc7`
- Isolated-toolkit snapshot SHA-256 (per `SOURCE-SNAPSHOT.json`):
  `c50640bff9f4de41030672d6c4de48cfb110aa398d302b1ba8d11f4ddb7c6efb`

## Derivative source (this Short)

- Parent reel: `youtube/brutalist/claude-liam-brutalist-skill-screen-clean`
- Parent vertical beat sheet:
  `youtube/brutalist/claude-liam-brutalist-skill-screen-clean/vertical/beat_sheet.json`
- Parent vertical master SHA-256 (per invocation record):
  `1d655dc3c4ae8ceb319d0136b056756aa3fac7a628cac47413d20c1ca858c357`
- Short episode `source_sha256`:
  `b06aceaebc9e3aa40ac124e867b04393f7c261b4d7e8a4773b14a71a96909717`
- Short run_id: `8e015bf97ef640ad913e13304e87da91`

## Verbatim quotes displayed in this Short

Only one Mechanism card is retained, so only one on-screen quote is shown:

- **B07** (Pass 4, flag never decide): "Never auto-blur and never decide on
  someone's behalf — 'is this embarrassing' is judgment, not arithmetic."
  Cited as `screen-clean SKILL.md · Pass 4`.

## Reused parent assets

- `vertical/media/{B00,B01,B03,B07,B09,B11}.mp4` copied independently to
  `media/`. Each is 2160×3840 h264. No re-render, no re-crop, no ONDA rewire.
- `vertical/mp3/beat-{B00,B01,B03,B07,B09,B11}.mp3` copied independently to
  `mp3/`. Kokoro `am_onyx` narration; parent's timings preserved.

## Not carried into this Short

- Parent demo folder `demo/screen-clean-run.log` (Pass 1 fixtures) — belongs
  to B05.
- Parent `scene-source/` overlay assets — no visual scene was rewritten in
  this cut.
- Parent SOURCES.md's list of mechanism-card quotes for Acts 1/2/3/5 — those
  quotes belong to dropped beats B04/B05/B06/B08.
