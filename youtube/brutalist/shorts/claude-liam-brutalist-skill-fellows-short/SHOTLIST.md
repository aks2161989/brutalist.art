# Shotlist — Short (2160×3840, 24 fps, 128.708 s)

Seven whole beats reused from the vertical parent as independent copies
(no cropping, no re-render, no regenerated audio). Every Remotion source
frame is the same portrait composition the long uses at 2160×3840. The
Short's `shorts.py` run printed `native portrait reused unchanged` for
each kept beat.

| Beat | Composition | Motion | Actual (s) | Frame content |
|---|---|---|---|---|
| B00 | `ClaudeComposerAsk916` | type-on | 13.17 | Portrait composer on cream. Greeting **Hallo, Liam**. Ask command types (`What is the fellows skill?`). Terracotta send button arms. Three result lines fade in: `a frame around a fellow's own recording`, `branded bookends · Professor Bear's notes · HAI outro`, `the report plays untouched — audio and timing`. Folder chip `@HumanitariansAI`. |
| B01 | `BrutalistHesitantWriter916` | type-on | 14.42 | Five-line serif reflow: `The fellows skill / re-cuts the / fellows video. / The fellows report / plays untouched.` The word `re-cuts` flashes terracotta and is corrected to `frames` mid-timeline. Portrait fontSize=118, lineSpacing=2.2 (`feedback_hesitant_writer_portrait_bluf_recipe`). Seed `fellows-bluf-vertical-e71dd104-v2`. |
| B03 | `SkillTeardownPipeline916` | reveal | 19.79 | Vertical pipeline stack. INPUT `fellow's raw recording` at top; ASK → SUMMARY×2–3 → **THE REPORT** (lit terracotta, "beat 4 · fellows own video · plays as is") → BEAR'S NOTES×2 → YOUR TURN + HAI OUTRO → OUTPUT `wrapped reel + signed NOTES.md`. Footer: `Only the middle is the fellow's own material.` Sparkline `Bookends around the fellow's file.` |
| B04 | `SkillTeardownMechanism916` | reveal | 23.75 | MECHANISM · ACT 1. Heading **The report is the clock.** Body paragraph on audio-first inversion + transcode-only compiler. Mono quote block from SKILL.md verbatim. Verdict pill `INVERTS AUDIO-FIRST, FOR BEAT 4` (positive polarity). Sparkline `Report drives. Bookends fit.` |
| B06 | `SkillTeardownMechanism916` | reveal | 27.46 | MECHANISM · ACT 3. Heading **GATE N.** Body on the two SHA-256 fingerprints (NOTES.md content + spoken narration) that Kokoro/Remotion/final refuse to run without. Mono quote block from SKILL.md verbatim. Verdict pill `NO BYPASS, NO AI SIGNATURE` (positive polarity). Sparkline `Bear's words. Bear's signature.` |
| B09 | `ClaudeVerdictArtifact916` | reveal | 26.75 | Portrait artifact card. Chip `The fellows Skill`. Heading **A frame. Not a re-edit.** Six numbered verdict lines reveal in order: (1) frame around a fellow's recording; (2) THE REPORT IS THE CLOCK; (3) FELLOW'S-WORK CARVE-OUT of REBUILD LAW; (4) GATE N + no `--no-gate` bypass; (5) one Kokoro voice per fellow + SOUND REPAIR / no retime; (6) HAI outro, not ClaudeTitleOutro; channel `@HumanitariansAI`. |
| B11 | `ClaudeTitleOutro916` | hold | 3.38 | Cream ground (slug-seeded). Title **The fellows Skill.** with terracotta period. Hardcoded `@NikBearBrown` handle beneath (this teardown is a `claude-liam` reel; `OUTRO-LOCK.md`). No subline. |

## Duration budget

Sum of `render_duration_s`: **128.71 s** · encoded MP4: **128.708 s**.
Editorial cap: strictly < 180.0 s. Timeline, video and audio durations all
verified below the cap by ffprobe (see `CHECKS-REPORT.md`).

## Portrait framing checks

- All seven kept beats probe as 2160×3840 (see CHECKS-REPORT.md `probe_wh`
  block). `shorts.py` re-used each native portrait file as-is.
- Text stays inside the 90% safe box on the extracted 15/50/85 % frames for
  every beat (image evidence: `_qc/beat-*-{15,50,85}.png`).
- `channel_title` metadata is deliberately absent from the short's beat
  sheet (`feedback_channel_title_portrait_bleed`).
- The `BrutalistHesitantWriter916` scale uses the portrait BLUF recipe
  (`feedback_hesitant_writer_portrait_bluf_recipe`) inherited from the
  parent — not the shipped landscape formula.

## Dropped beats (long-form only)

`B02` folder anatomy — `SkillTeardownAnatomy916` reveal
`B05` FELLOW'S-WORK carve-out — `SkillTeardownMechanism916` reveal
`B07` persistent voice + SOUND REPAIR — `SkillTeardownMechanism916` reveal
`B08` HAI-outro falsifiability — `SkillTeardownMechanism916` reveal
`B10` Your-Turn dry-run assignment — `ClaudeComposerAsk916` type-on

These frames are still in the parent reel at `vertical/media/B0{2,5,7,8}.mp4`
and `vertical/media/B10.mp4` — the Short does not delete or crop them, it
just does not include them.
