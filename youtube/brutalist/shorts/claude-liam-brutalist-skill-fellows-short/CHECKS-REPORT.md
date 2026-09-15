# Checks report — Short cut

Run ID: `28dd40173c164f0a85bea3d8084e2ee7`
source_sha256 (this invocation): `1b177f008eddeda9424621410b292a3a4459c28f38799a04206f2267c68f535a`
Parent master SHA-256: `03ca7edaa3af9fee6530060c484cdf858cb51e04d2c54aa8fa692f39de6fe5e0`
Reviewer: AI (Claude Sonnet 4.6). Human review pending.

**Re-verification note.** The parent's vertical beat_sheet.json was re-verified
(parent run_id 616bfc2f; note: "SKILL.md content unchanged, toolkit baseline updated").
This caused the episode source_sha256 to change; the actual beat media, narration, and
video content are identical to the prior build. `compile.py` re-ran: all media/mp3
SHA-256s matched `build-state.json`; the output video SHA is unchanged.

## 1. Duration — strictly under 180.0 s

The editorial rule (`SHORTS_CAP_S = 180.0`, `build_safety.py:210`) requires
every measured duration to be **strictly less than 180.0 seconds**. The
compiler enforces this at three separate points; the Short passed all three
without a `--force`:

- `shorts.py` planning: `require_short_duration(total)` on the frame-aligned
  sum of `render_duration_s` → `128.71 s`, `status: ready`, `errors: []`.
- `compile.py:650` measured timeline: `require_short_duration(...,
  'Measured Short timeline')` → `128.708 s`.
- `compile.py:440–443` encoded container + per-stream:
  `require_short_duration(duration, 'Encoded Short container')` → `128.708 s`,
  and each stream (`video`, `audio`) → `128.667 s`, `128.708 s`.

All three strictly below the cap. No exponent, negative, or NaN durations.

## 2. Command trace

Working directory: the isolated toolkit at
`.repoloop/shorts/workspaces/claude-liam-brutalist-skill-fellows-short/toolkit`.
No `--force`, no `--allow-slates`, no `--review`, no bypass flags.

### 2.1 Cut

```
python3 runtime/scripts/shorts.py \
  /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/youtube/brutalist/claude-liam-brutalist-skill-fellows/vertical \
  --output-dir /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/youtube/brutalist/shorts/claude-liam-brutalist-skill-fellows-short \
  --slug claude-liam-brutalist-skill-fellows-short \
  --drop B02 B05 B07 B08 B10 --no-endcard --no-outro-rewrite
```

Output (verbatim):

```
[short] parent reel: 12 beats · 261.9s (4:21.9) · Shorts cap 3:00
[short] manual plan: dropping B02, B05, B07, B08, B10
[short] B00 native portrait reused unchanged
[short] B01 native portrait reused unchanged
[short] B03 native portrait reused unchanged
[short] B04 native portrait reused unchanged
[short] B06 native portrait reused unchanged
[short] B09 native portrait reused unchanged
[short] B11 native portrait reused unchanged
[short] 7 beats · ~128.7s (2:08.7) OK
[short] dropped: B02, B05, B07, B08, B10 · ends on the last beat (no endcard)
```

Every kept beat printed **`native portrait reused unchanged`** — no crop, no
`--recut`, no `-916` re-derivation, no Onda-check rewire.

### 2.2 Compile

```
python3 runtime/scripts/compile.py \
  /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/youtube/brutalist/shorts/claude-liam-brutalist-skill-fellows-short \
  --height 3840 \
  --out /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/youtube/brutalist/shorts/claude-liam-brutalist-skill-fellows-short/exports/short
```

Output (final lines):

```
[art] compiled B00  VIDEO    13.2s  ← B00.mp4
[art] compiled B01  VIDEO    14.4s  ← B01.mp4
[art] compiled B03  VIDEO    19.8s  ← B03.mp4
[art] compiled B04  VIDEO    23.8s  ← B04.mp4
[art] compiled B06  VIDEO    27.5s  ← B06.mp4
[art] compiled B09  VIDEO    26.8s  ← B09.mp4
[art] compiled B11  VIDEO     3.4s  ← B11.mp4
[art] motion histogram: reveal:4  type-on:2  hold:1
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk
[art] SKIN LINT: B11: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro
[art] build stamp → beat_sheet.json (7/7 filled)
[art] wrote /Users/bear/…/exports/short/claude-liam-brutalist-skill-fellows-short.mp4  (128.7s, audio: per-beat timeline (source audio preserved), drawtext: no — PIL overlays)
[art] slots: 7/7 filled — B00:VIDEO B01:VIDEO B03:VIDEO B04:VIDEO B06:VIDEO B09:VIDEO B11:VIDEO
```

**SKIN LINT interpretation.** The two warnings (B00, B11) are advisory
warnings from the compiler's SKIN LINT: at portrait aspect the composition
IDs end with `916` (e.g. `ClaudeComposerAsk916`, `ClaudeTitleOutro916`),
and COLD OPEN LAW / OUTRO LAW are worded against the base landscape IDs
(`ClaudeComposerAsk`, `ClaudeTitleOutro`). The 916 variants share source
with their landscape siblings and reflow via `useVideoConfig()`
(documented in the parent beat sheet's `skin_warnings`). Same warning
issued and accepted on the parent 9:16 build; not a blocker.

## 3. ffprobe — dimensions and durations

Every kept beat probes native portrait 2160×3840 and each mp3 is Kokoro
`am_onyx` at 24 kHz mono (the parent's originals):

| Beat | Video (w×h · dur) | Audio (Hz · ch · dur) |
|---|---|---|
| B00 | 2160×3840 · 13.167 s | 24000 · 1 · 13.163 s |
| B01 | 2160×3840 · 14.400 s | 24000 · 1 · 14.379 s |
| B03 | 2160×3840 · 19.800 s | 24000 · 1 · 19.776 s |
| B04 | 2160×3840 · 23.733 s | 24000 · 1 · 23.723 s |
| B06 | 2160×3840 · 27.433 s | 24000 · 1 · 27.435 s |
| B09 | 2160×3840 · 26.733 s | 24000 · 1 · 26.731 s |
| B11 | 2160×3840 · 3.400 s  | 24000 · 1 ·  3.371 s |

Final container:

- Container `mov,mp4,m4a,3gp,3g2,mj2` · size 9.98 MB · duration **128.708 s**
- Video: `h264` · 2160×3840 · **128.667 s** · 3088 frames (24 fps × 128.667 s)
- Audio: `aac` · 48000 Hz stereo · **128.708 s**

All three strictly < 180.0 s (see §1).

## 4. Audio decode

`ffmpeg -i final.mp4 -af astats=metadata=1:reset=0 -f null -` decoded the
audio track end-to-end. Overall peak −3.13 dB, overall RMS −27.02 dB.
Real narration is present (Liam / Kokoro `am_onyx`), consistent throughout
without dropouts. Not silence, not clipping.

## 5. Visual review — per-beat frames

Extracted with `ffmpeg -ss <t> -i final.mp4 -frames:v 1 -vf scale=540:960
_qc/beat-<bid>-<pct>.png`, plus first/final and a 2 fps contact sheet.
Opened with the image-capable Read tool. Full hashes in `VISUAL-REVIEW.json`.

- **B00** (0 s → 13.17 s). 15% shows the composer mid-ask with the
  greeting `Hallo, Liam` above; the ask reads
  `What is the fellows skill? Read skills/make/fellows/SKILL.md…` and the
  folder chip `@HumanitariansAI` is visible. 50% shows the full three
  result lines below the composer. Cream palette; terracotta send-button
  and result-line asterisk correct. Legible; text inside the safe box.
- **B01** (13.17 s → 27.58 s). 15% shows `The fellows skill / re-cuts`
  (mid-mistake, `re-cuts` still terracotta). 50% shows the corrected
  five-line reflow `The fellows skill / frames the / fellows video. /
  The fellows report / plays untouched.` — the hesitant-writer correction
  landed. Serif face, portrait BLUF recipe (fontSize=118, lineSpacing=2.2)
  clearly applied; the text does not underfill (`feedback_gate_v_underfill`
  compliant).
- **B03** (27.58 s → 47.38 s). Pipeline stack fully revealed at 50%.
  INPUT `fellow's raw recording`, ASK, SUMMARY×2–3, **THE REPORT** (lit
  terracotta), BEAR'S NOTES×2, YOUR TURN + HAI OUTRO, OUTPUT
  `wrapped reel + signed NOTES.md`. Footer note visible. Sparkline
  `Bookends around the fellow's file.` at bottom-left safe.
- **B04** (47.38 s → 71.11 s). MECHANISM · ACT 1. Heading
  **The report is the clock.** Full body paragraph, mono quote block
  citing `fellows SKILL.md · THE REPORT IS THE CLOCK`. Verdict pill
  `INVERTS AUDIO-FIRST, FOR BEAT 4` (positive polarity, terracotta ring).
- **B06** (71.11 s → 98.55 s). MECHANISM · ACT 3. Heading **GATE N.**
  Full body paragraph on approval fingerprints. Mono quote block citing
  `fellows SKILL.md · GATE N`. Verdict pill `NO BYPASS, NO AI SIGNATURE`.
- **B09** (98.55 s → 125.28 s). Artifact card chip `The fellows Skill`.
  Heading **A frame. Not a re-edit.** All six numbered lines visible and
  legible at 50%. Verdict line 4 explicitly says
  `GATE N: NOTES.md is human-signed before Kokoro speaks it — no --no-gate bypass.`
- **B11** (125.28 s → 128.67 s). Title outro **The fellows Skill.** with
  terracotta period; `@NikBearBrown` beneath. Slug-seeded mascot slot
  present (cream-polarity variant). Final frame identical.

**Contact sheet** (`_qc/contact-2fps.png`, 2 fps × 128.7 s = 257 tiles at
8 columns × 33 rows). Reads cream-palette throughout; no black frames, no
frame-order regression, no unwanted subtitle burn, no unresolved visual
stalls at beat joins.

## 6. Verdict coherence — dropped beats vs. verdict lines

B09's six verdict lines cover both retained laws (THE REPORT IS THE CLOCK,
GATE N) and three laws whose mechanism beats were dropped (FELLOW'S-WORK
carve-out, persistent voice + SOUND REPAIR, HAI outro deviation). These
appear as single verdict lines and the viewer hears them for the first
time in the recap. That is the point of a verdict at Short length; each
line is directly traced to SKILL.md in `FACTCHECK.md` (see §"Claims verdict
lines make about beats not shown in the Short").

## 7. Numbered transitions

- B04 opens `First design decision, and it is the sharpest.`
- B06 opens `Third decision, and it is where the skill earns its trust.`

`Third` reads as a minor stumble because `Second` and `Fourth` (B05, B07)
were cut whole. Kept as-is rather than regenerate B06's Kokoro audio and
Remotion render for a one-word rewrite (`Third` → `Next`); documented in
`CUT-PLAN.json` `coherence_notes` and `SCRIPT.md` §Editorial notes.

## 8. Gates and paperwork

- `beat_sheet.json` — validated by `validate_project()` (safe beat IDs,
  non-empty beats list, well-formed metadata slug).
- `short_validation` in metadata: `status: ready`, `errors: []`.
- `metadata.approvals` = `{}` — this teardown is source-backed
  (SELF-DEMO LAW feasibility fallback); no `professor_notes` approval
  applies because no fellow's `NOTES.md` was drafted or read this run.
- Paperwork present in this reel: `FACTCHECK.md`, `SHOTLIST.md`,
  `PROMPTS.md`, `SOURCES.md`, `SCRIPT.md`, `CUT-PLAN.json`,
  `CHECKS-REPORT.md`, `TYPECHECK.md`, `VISUAL-REVIEW.json`,
  `BUILD-PROMPT.md` (supervisor's, preserved), `BRIEF.md`, `FEEDBACK.md`,
  `SOURCE-SNAPSHOT.json`, `README.md`.

## 9. Not done

- Not published, not uploaded, not pushed to git, no paid generation.
- No fellow's report was transcribed, embedded, or referenced by name.
- Human review pending (Bear). `reviewer_type: ai`.

## 10. Ready receipt

- Compiler wrote:
  `youtube/brutalist/shorts/claude-liam-brutalist-skill-fellows-short/exports/short/claude-liam-brutalist-skill-fellows-short.mp4`
  (128.708 s, 9.98 MB).
- SHA-256: `2c596d7352f473d5f67ebad341d5e5a13294737cea180c794b5745810d26f3b7`.
- Beat sheet SHA-256: `0f4d105a55f74a3f0c58202da5763a7de4967c4535e733b5c07f8a6969f483bd` (updated build.at stamp from this compile run).
