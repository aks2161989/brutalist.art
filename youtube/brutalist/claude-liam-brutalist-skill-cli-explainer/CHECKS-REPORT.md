# Checks — landscape

Run: 2026-09-08 · run_id c1bd87ad4f3a4cbfb9163dca2cd83e44 · attempt 3 (original).
Re-verified: 2026-09-11 · run_id 1685612a4a7c43a99fc9b8f1ce087a15 · source-change re-sign.

## Runtime gates

**Gate V (final_frame_check.py)** — sampled 26 frames (13 beats × 50%/85% steady-state) against the 3840×2160 title-safe area (SAFE w=3456 h=1944). Ink bbox / SAFE-area coverage `FILL_MIN >= 0.55`.
- Command: `runtime/qc/final_frame_check.py <reel> --mp4 <candidate.mp4> --sheet <resolved-sheet.json>`
- Result: **PASS** — BLOCKER 0, MAJOR 0. `_qc/REPORT.md` reads "Clean — no BLOCKER/MAJOR defects. ✓".

**compile.py finish gate (`verify_output`)** — atomic candidate encode + probe verification of duration/frame-count/audio decode.
- Command: `runtime/scripts/compile.py <reel> --height 2160 --out exports/landscape`
- Result: **PASS** — wrote `exports/landscape/claude-liam-brutalist-skill-cli-explainer.mp4` (194.6s master, 3840x2160@24, h264, audio: per-beat timeline preserved from Kokoro). `.verified.json` receipt written next to the master.

**Prior failure and repair.**
- Attempt 2 (05:54): candidate.mp4 gate V failed at B01 `underfill 48%` because `clips/B01.mp4` was audio-mixed from an earlier `media/B01.mp4` render at `fontSize=220`. Attempt 2 subsequently re-rendered `media/B01.mp4` at `fontSize=270` (68% coverage) but did NOT re-run compile.py.
- Attempt 3 (07:57): `compile.py` re-invoked; the manifest's per-clip cache key includes `sha1(media/<bid>.mp4)`, so the change in `media/B01.mp4` invalidated `clips/B01.mp4`, forced a rebuild, and the candidate then passed gate V cleanly.

## Manual visual pass

Extracted 26 steady-state frames (see `_qc/contact_sheet.png`, sha256 6736bc66…) and read them with the image-capable Read tool.
- Beat framing (composer chrome / hesitant writer / anatomy tree / pipeline nodes / code cards / mechanism / verdict / outro): every beat holds INSIDE the title-safe inset, no clip, no bleed, no overlap.
- B00 cold open: greeting `Namaste, Liam` + `@HumanitariansAI` folder label; ask types letter-by-letter; runningText `reading the skill…`; three RESULT lines settle.
- B01 hesitant writer: types `cli-explainer/records/terminals.`, hesitates, corrects to `cli-explainer/commissions/reels.` at fontSize 270; stable seed `cli-explainer-bluf-2026-09-08`; measured coverage 68% (over the 55% floor).
- B12 outro: title restated as `The cli-explainer Skill.`; handle reads `@HumanitariansAI` — the isolated toolkit's ClaudeTitleOutro accepts the handle prop instead of hardcoding `@NikBearBrown`.

## Documented gaps

- No `scripts/type_check.py` in this toolkit; the legacy REL/kerning checker referenced in some docs is not shipped. Visual typography audit performed by reading extracted frames — see `TYPECHECK.md`.
- No `ILLUSTRATIONS.md`, no `reference/type-spec.md`, no kerning skill. Recorded, not fabricated.
- No published contact card or spec sheet checker; verdict rests on gate V + human-read frames.
- `art keys` and `setup --install` were NOT invoked (no external network / credentials in this session, per BUILD-PROMPT restrictions). Demo evidence is recorded from local, source-backed operations only.

## Audio decode

- Master audio: 13 per-beat Kokoro am_onyx MP3s, mixed serially into the candidate; ffprobe confirms audio stream present at 24fps carrier. See `.verified.json` for per-input SHA-256 receipts.

## Re-verification notes (2026-09-11, run_id 1685612a4a7c43a99fc9b8f1ce087a15)

Source change detected: `source_sha256` changed from `e9e2b5b8...` to `050ab021...` because COMMON files changed (runtime/prose/teardown/PROSE.md renamed from voices/; REPOLOOP-PROMPT.md newly tracked). The SKILL.md content is UNCHANGED (SHA f7aab411 in both SOURCE-SNAPSHOT.json and the isolated toolkit copy). The beat_sheet.json was updated to record the current SKILL.md SHA. All rendered clips and exports are identical to the previous pass — no re-render required.

- Landscape export SHA verified unchanged: `ddbb8dcb3e0473d508a91ac63c9bd39e4c7208625750a21b72b96d590280a41a`
- Contact sheet SHA verified unchanged: `6736bc662366a96555641859addd1f32a7309ee93df1e37491ee487bb86e2d5c`
- Gate V REPORT.md: "Clean — no BLOCKER/MAJOR defects. ✓" (unchanged)
- Contact sheet reviewed via image tool — all 13 beats pass visual inspection (no slates, no caption overflows, no safe-area bleed).
