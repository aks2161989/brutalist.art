# CHECKS-REPORT.md — The anthropics Skill — Short

**Aspect:** 9:16 (2160×3840, native portrait)
**Duration:** 121.75 s (container = video = audio)
**Cap:** strictly < 180 s → PASS (58.25 s headroom)
**Run:** `f37e6639e4514e15aeb0321e42e9f17d`
**Source SHA-256:** `68d5048370de87f2e8ecbac251c56173c85d09d1121a720914181ceb12a5040e`
**Final MP4 SHA-256:** `d26c2ffcba8d42cac113bc3fd7caa697e977b7909477313e2b05b0fd22c691cf`
**Final beat_sheet SHA-256:** `13a0a60cb288d53f575eabfbce69bd0f8502167e986cf04594e1b9ae30588c83`

> **Re-verification note (2026-09-11):** source_sha256 changed (other framework skills updated; anthropics SKILL.md is unchanged per vertical beat_sheet note for run 3d80d6c7). Export, beat_sheet, QC frame, and media SHA-256s all match prior verified values. Four frames re-read via image tool (B00-50, B04-50, B07-50, B10-85) — all pass. No re-render required.

## Cut plan — evidence

Parent vertical: 11 beats · 228.9 s. See `CUT-PLAN.json`.

Kept (7): B00 ASK · B01 BLUF · B03 four-mode router · B04 disqualifier · B07 falsifiability · B08 verdict · B10 outro.
Dropped (4): B02 anatomy · B05 behavioural probes · B06 register · B09 paste-ready Your Turn.

`shorts.py` reported: `[short] 7 beats · ~121.8s (2:01.8) OK` and `native portrait reused unchanged` for every kept beat — no ONDA re-render, no center-cut, no outro rewrite, no endcard.

## Commands (actual)

```
python3 runtime/scripts/shorts.py \
  youtube/brutalist/claude-liam-brutalist-skill-anthropics/vertical \
  --output-dir youtube/brutalist/shorts/claude-liam-brutalist-skill-anthropics-short \
  --slug claude-liam-brutalist-skill-anthropics-short \
  --drop B02 B05 B06 B09 --no-endcard --no-outro-rewrite

python3 runtime/scripts/compile.py \
  youtube/brutalist/shorts/claude-liam-brutalist-skill-anthropics-short \
  --height 3840 \
  --out youtube/brutalist/shorts/claude-liam-brutalist-skill-anthropics-short/exports/short
```

Compiler output: `slots: 7/7 filled — B00:VIDEO B01:VIDEO B03:VIDEO B04:VIDEO B07:VIDEO B08:VIDEO B10:VIDEO`; `motion histogram: reveal:4 type-on:2 hold:1`; `drawtext: no — PIL overlays`. Two skin-lint warnings are inherited from the parent's `ClaudeComposerAsk916` cold open and `AntOutro916` outro — these are intentional (documented in the parent's build note: `AntOutro916` is used because the shipped `ClaudeTitleOutro` hardcodes `@NikBearBrown`; the cold open uses `ClaudeComposerAsk916` to fit portrait geometry).

## Probes (final MP4)

```
ffprobe format.duration     121.750000
ffprobe stream v:0 codec    h264
ffprobe stream v:0 wxh      2160x3840
ffprobe stream v:0 fps      24
ffprobe stream v:0 duration 121.750000
ffprobe stream a:0 codec    aac
ffprobe stream a:0 sr/ch    48000 / 2
ffprobe stream a:0 duration 121.750000
```

Audio decode check: `ffmpeg -i <mp4> -vn -ac 1 -ar 16000 -f wav` produced a 121.77 s pcm_s16le stream — no decode errors.

## Frame evidence

For every kept beat, sampled 15% / 50% / 85% relative to that beat's own duration inside the assembled timeline (absolute offsets recorded in the extraction log). All 21 stills plus a 2 fps contact sheet are under `_qc/` and hashed in `VISUAL-REVIEW.json`.

Read frames (Read tool, image mode):

| Beat | Frames read | Observation |
|------|-------------|-------------|
| B00 | 15, 50, 85 | Cold open composer: greeting "Hej, Liam", topic "BRUTALIST · SKILL TEARDOWN", title "The anthropics Skill", composer command legible, result bullets fade in at 50%. Handle chip: @HumanitariansAI. Safe area respected. |
| B01 | 85 | Hesitant-writer serif stack fills the vertical safe area with the corrected line ("The anthropics is a beat reads the artifact"). No clipping; cursor visible. |
| B03 | 50 | SKILL · PIPELINE eyebrow, "Four modes, one router." heading, five phase nodes reveal left-to-right with `--capability` accented terracotta. Footer "Read the artifact. Not the paragraph about it." |
| B04 | 50 | MECHANISM · ACT 1 eyebrow, "If it could be read off the docs — it isn't this." heading, verbatim SKILL.md quote block, verdict pill "KILLS THE DOWNSTREAM-OF-DOCS 90%", spark line "Not the docs." |
| B07 | 50 | DESIGN · TELL eyebrow, "Where it bites." heading, body names the missing siblings AND the no-generated-evidence law, quote block verbatim, verdict pill "HARD CEILING · HIGH COST", spark line "Trades pop for credibility." |
| B08 | 50 | ClaudeVerdictArtifact card with title "The anthropics Skill" and heading "The anthropics beat." Five numbered lines all rendered in-card, no bleed. |
| B10 | 15, 50, 85 | AntOutro916: "BRUTALIST · EPISODE 05" eyebrow, terracotta rule, "The anthropics Skill." poster serif with terracotta period, @HumanitariansAI handle, "LIAM, IN FOR BEAR." subline. |

Full frame paths + SHA-256s in `VISUAL-REVIEW.json`.

## Narration coherence

Post-cut narration was reread against `beat_sheet.json`:

- B00 introduces Liam ("Hej, this is Liam, in for Bear") and names the skill's purpose. IN-FOR-BEAR LAW satisfied.
- B01 sets up the misconception cleanly ("a beat, journalism sense — that reads the artifact").
- B03 delivers the four-mode router, and B04 the disqualifier — no dangling backreference to B02's anatomy.
- B07's "here is where the skill bites" reads as its own turn even without B05/B06 preceding.
- B08's verdict recaps five lines. Two on-screen bullets ("Behaviour is the thesis; defaults are the tell" · "Independence stated once. Situated. Honest about matches.") come from dropped B05/B06. In the narration these are compressed into "It reads the artifact rather than the artifact's press release, and it says so out loud." The bullets on the card read as capsule teasers rather than callbacks to explained material — noted as a minor coherence remark, not a blocker.
- B10 signs off cleanly: "That was the anthropics skill. Liam, in for Bear."

## Result

- Compiler final: OK (no `--review` flag)
- Container/video/audio each < 180 s: **PASS**
- Native 2160×3840 preserved: **PASS**
- Frame evidence extracted and read: **PASS**
- No burned-in captions, no external network use, no publishing: **PASS**
- Blockers: 0 · Majors: 0 · Minors: 1 (see coherence note above)

**Conclusion:** the Short is ready for Bear's viewing/editing. Human review pending.
