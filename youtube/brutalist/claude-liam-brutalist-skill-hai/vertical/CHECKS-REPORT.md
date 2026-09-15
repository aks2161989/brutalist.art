# CHECKS-REPORT.md — The hai Skill (portrait 2160×3840)

Run id: `06dfe1bb8b9e4743882466aa3294a5dd` (resumed; original build under `d660d0c9949a427980931d1c010c2f47`)
Final master: `exports/vertical/claude-liam-brutalist-skill-hai-vertical.mp4`
Master SHA-256: `7a92bdb465492063ced20ba2a4091ad7ce5b0de20f144a187ab3cbc9d8527a31` (unchanged from the atomic-verified build; matches disk).

## Whole-sheet teaching-arc classification

Same twelve-beat structure as the landscape master. Every beat is SHOW. 12 SHOW / 0 justified-HOLD / 0 PUNT.

- FRAMEWORK ✓, WORKED EXAMPLE ✓, FALSIFIABILITY ✓, SCAFFOLDED TASK ✓, BOOKENDS ✓, NO-SOURCE-NO-VERDICT ✓.
- Portrait-specific: three SkillTeardown-family scenes render through their 916 wrappers (native reflow, not center-crop); B01 hesitant writer uses the portrait-aware scale patch.
- `metadata.channel_title` is deliberately omitted from this sheet per `feedback_channel_title_portrait_bleed` — the compile.py overlay bleeds past portrait `safe.b`. The channel identity still lands in the composer's `folderLabel` on every ClaudeComposerAsk916 beat.

## Gate V — visual QC

Final `_qc/REPORT.md`:
```
Frames sampled: 24  ·  BLOCKER: 0  ·  MAJOR: 0
Clean — no BLOCKER/MAJOR defects. ✓
```

Iteration log (portrait-only fixes, all authored inside the vertical beat sheet):

- Attempt 1 (B01 fontSize=130, 5 lines matching landscape recipe): underfill 45%.
- Attempt 2 (B01 fontSize=142, 5 short lines): edge-bleed left/right — text too wide for portrait safe.
- Attempt 3 (B01 fontSize=156, 4 lines): back to underfill 35%.
- Attempt 4 (B01 fontSize=138, 5 lines, lineSpacing 1.4): underfill 38%.
- Attempt 5 (B01 fontSize=130, 5 lines, lineSpacing 2.4 — matches guests recipe): underfill 51%.
- **Attempt 6 (B01 fontSize=130, 5 lines, lineSpacing 2.65): CLEAN.** The extra vertical spacing pushes the content bbox above the 55% coverage floor.

B03 needed two structural passes:

- Original 6-phase pipeline + INPUT/OUTPUT + footer: bottom edge-bleed.
- Reduced to 4 phases (`SCAFFOLD · REWRITE (Plain) · CLI EXERCISE · HAI OUTRO`) with the input/output boxes at the ends and a shorter footer note: CLEAN. The narration still names all six flow steps; the portrait diagram compresses them to the four that define the shape while the tangent + verify stay in the voice.

B10 needed one prose pass:

- Original landscape command text (very long) overflowed the composer card bottom.
- Rewrote the portrait command to the same intent in ~60% of the length. Kept the mandatory five-part-schema check callouts intact. CLEAN.

## Skin lint (expected warnings)

```
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk
[art] SKIN LINT: B11: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro
```

These are the standard portrait-companion warnings — the 916 suffix is the correct native portrait variant of the required cold-open and outro components. Same warnings appear on every portrait companion in this playlist. No action needed.

## Motion histogram (compile.py)

Same distribution as landscape (`reveal:8 type-on:3 hold:1`). The reveal warning is a coarse-label limitation of the histogram — the actual motion per beat differs across the four SkillTeardown-family scenes and ClaudeVerdictArtifact. Same analysis as `../CHECKS-REPORT.md`.

## Narration alignment

Portrait re-uses the landscape Kokoro audio (byte-identical `mp3/` directory copied into `vertical/mp3/`). Every beat's `actual_duration_s` matches the landscape sheet within rounding. Total portrait duration = 280.125s = landscape duration.

## ffprobe

```
codec_name=h264
width=2160
height=3840
r_frame_rate=24/1
duration=280.125000

codec_name=aac
duration=280.125000
```

Native 4K portrait (2160×3840), 24fps, H264+AAC decoded — both streams verified.

## Frame audit (Read PNGs directly)

- `vertical/_qc/contact_sheet.png` — Gate V's 12-tile contact sheet. Read and inspected. Every beat legible on 9:16; type sizes and columns are portrait-native (not letterboxed landscape).
- `vertical/_qc/b01_v5.png` — targeted single-frame read on the final B01 render. Poem-like BLUF spacing; matches the guests-episode B01 aesthetic.
- `vertical/_qc/portrait-defects2.png` — the 3×2 grid extracted before the final fixes, retained as evidence of the underfill/edge-bleed defects that iteration eliminated.

## Fresh proof frames for run 06dfe1bb (this invocation)

Because the prior review file was rejected as "frame evidence missing/stale", I re-extracted five frames directly from the current portrait MP4 with `ffmpeg -ss <t> -frames:v 1`. Each frame was hashed and read with the image-capable Read tool. Combined strip at `vertical/_qc/proof-run-06dfe1bb.png`.

| t (s) | Beat expected | What I observed |
| --- | --- | --- |
| 5   | B00 ClaudeComposerAsk916 cold open | "The hai Skill" title band, "Hello, Liam" composer, hai-skill README ask; @HumanitariansAI folder label. |
| 60  | B03 SkillTeardownPipeline916 | "Six steps. One shape." — vertical stack of the four defining phases with input/output nodes at the ends (portrait compression documented above). |
| 140 | B06 SkillTeardownMechanism916 (CLI exercise) | "The CLI exercise." heading with the five-part-schema quote card. |
| 220 | B09 ClaudeVerdictArtifact916 | "A fork. Not a re-skin." verdict card with sub-line bullets. |
| 275 | B10/B11 handoff (Your Turn composer → outro) | "Fork one of your reels" composer / "Your Turn" greeting; paste-ready portrait prompt. |

Video hash (`7a92bdb4…`) unchanged from the compiler receipt, so the same content the earlier reviewer certified is still on disk; the fresh proof frames confirm the content matches the portrait beat sheet.

## Approvals / gates

Same as landscape: `approvals: {}`, no third-party subject, no GATE G/N in scope for a claude-liam Teardown.

## Conclusion

Portrait companion (2160×3840, 280.125s, H264+AAC, atomic-verified) is complete. Gate V clean after six B01 iterations and two structural B03/B10 iterations — all authored inside the portrait sheet, no changes to the landscape or shared scene source. Human viewing/editing is next.
