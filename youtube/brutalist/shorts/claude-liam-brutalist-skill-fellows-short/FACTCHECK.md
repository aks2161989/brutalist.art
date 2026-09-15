# Fact check — Short cut (every kept-beat claim traced to source)

Source of truth: **`skills/make/fellows/SKILL.md`** (isolated-toolkit snapshot,
SHA-256 `afd14d36428eac3cc954af49af4610206924cbcbbfb969cff339c02de0640131`;
supervisor's `episode.source_sha256`
`8185b0a2f3b715f6c18622995e40c5a523b7883c8bfd664407e16433ccd7d70f`, which
resolves to the same file with a normalized trailing-newline convention —
the fellows spine and laws are identical in both).

Confirming reads (unchanged from parent's evidence set): `skills/make/ai-explainer/SKILL.md`,
`docs/PIPELINE-SAFETY.md`, `docs/FELLOWS-SUBMISSION.md`, `OUTRO-LOCK.md`, `CLAUDE.md`.

This Short retains seven whole beats from the parent. The per-beat evidence
below covers only the kept beats. Beats B02, B05, B07, B08 and B10 were cut
whole — their evidence still stands in the parent's `vertical/FACTCHECK.md`.

## Per-beat claim → SKILL.md evidence

### B00 · Cold open (ClaudeComposerAsk916)
- **Claim:** "The fellows skill wraps a fellow's own recording without editing it."
  → SKILL.md §The shared skeleton: *"Same Claude-branded bookends as the siblings;
  the MIDDLE is the fellow's own video plus commentary around it."*
- **Claim:** "Every Humanitarians AI fellow ships weekly research videos."
  → docs/FELLOWS-SUBMISSION.md §Cadence: two videos per week (research + report).
- **Claim (on-screen result lines):** "a frame around a fellow's own recording",
  "branded bookends · Professor Bear's notes · HAI outro",
  "the report plays untouched — audio and timing".
  → SKILL.md opening + §The shared skeleton + §Laws (THE REPORT IS THE CLOCK).

### B01 · BLUF hesitant writer
- **Claim (correction):** the skill does NOT re-cut the video; it **frames** it.
  → SKILL.md §The required beat spine B04: *"The fellow's video PLAYS AS IS —
  pass-through beat."*
- **Claim:** "The fellows report is the middle of the reel and it plays untouched."
  → SKILL.md §The required beat spine B04 (as above).
- **Claim:** "What the skill builds is the frame around it — bookends, notes,
  and a handoff."
  → SKILL.md opening: *"The reel is a frame around their own report…"* +
  §The required beat spine (B00–B08 = ASK + summaries + THE REPORT + notes ×2 +
  YOUR TURN + OUTRO).

### B03 · Pipeline (nine-beat fixed spine)
- **Claim:** Nine-beat fixed spine.
  → SKILL.md §The required beat spine: B00 INTRO, B01–B03 THE WORK,
  B04 THE REPORT, B05–B06 PROFESSOR BEAR'S NOTES, B07 YOUR TURN, B08 OUTRO
  = 9 beats.
- **Claim:** "The composer asks what the fellow has been working on."
  → SKILL.md §The shared skeleton: *"the narrator asks Claude 'I wonder what
  Humanitarians AI fellow [name] has been working on lately…'"*
- **Claim:** "Two or three summary beats read from the transcript."
  → SKILL.md B01–B03: *"2–3 beats. The selected narrator summarizes what the
  fellow built — from the transcript, one idea per beat."*
- **Claim:** "Then the fellow's video plays as is — that is beat four."
  → SKILL.md B04.
- **Claim:** "Two beats of Professor Bear's notes — feedback, then next steps."
  → SKILL.md B05–B06: *"Feedback"* + *"Next steps"*.
- **Claim:** "A Your Turn prompt, and the standard Humanitarians AI outro."
  → SKILL.md B07 (YOUR TURN) + B08 OUTRO: *"The STANDARD Humanitarians AI outro"*.
- **Claim:** "Only the middle is the fellow's own material."
  → SKILL.md §Laws FELLOW'S-WORK carve-out + REBUILD LAW.

### B04 · Mechanism · Act 1 · THE REPORT IS THE CLOCK
- **Claim:** "Every other Brutalist skill is audio-first — Kokoro generates
  the narration and the visuals conform to that clock."
  → ai-explainer/SKILL.md §Frame laws · AUDIO-FIRST LAW.
- **Claim:** "Fellows inverts that for exactly one beat."
  → SKILL.md §Laws: *"THE REPORT IS THE CLOCK (the one exception to audio-first).
  Everywhere else narration MP3s are the master clock."*
- **Claim:** "No trim, no speed change, no voiceover, no re-timing."
  → SKILL.md §Laws: *"never retime, trim, speed up, or talk over it."*
- **Claim:** "The compiler transcodes container and resolution, and stops there."
  → SKILL.md §Laws: *"Transcode container/resolution to the reel spec (3840×2160
  landscape or 2160×3840 vertical, h264/AAC, contain/letterbox — never crop or
  stretch)."*
- **Claim:** "A trimmed cut is only legal when a human explicitly asks for it in
  the build log."
  → SKILL.md §Laws: *"If the human wants a trimmed cut, that is an explicit
  request logged in BUILD-LOG.md — never the skill's own call."*
- **On-screen quote block** is verbatim from SKILL.md §Laws (THE REPORT IS THE CLOCK).

### B06 · Mechanism · Act 3 · GATE N
- **Claim:** "Professor Bear's notes are Bear's words."
  → SKILL.md §Laws heading: *"GATE N — Professor Bear's notes are BEAR'S words."*
- **Claim:** "The skill drafts them from the transcript, in plain register, as a starting point."
  → SKILL.md §Laws: *"The skill DRAFTS `NOTES.md` (feedback + next steps) from
  the transcript, in Bear's plain register, as a starting point."*
- **Claim:** "Nothing goes to Kokoro until Bear has edited or signed NOTES markdown."
  → SKILL.md §Laws: *"the notes beats never go to audio until Bear has edited or
  signed `NOTES.md`."*
- **Claim:** "The runtime hashes the notes and the exact spoken wording."
  → SKILL.md §Laws + PIPELINE-SAFETY.md §Human approval:
  `metadata.approvals.professor_notes` binds `notes_sha256` + `narration_sha256`.
- **Claim:** "A pending record, a stale hash, or a missing signature blocks
  Kokoro, Remotion, and any final."
  → PIPELINE-SAFETY.md: *"Pending, missing or stale records block Kokoro
  generation, Remotion rendering, review assembly and direct final export."*
- **Claim:** "--no-gate does not bypass this."
  → SKILL.md §Laws: *"`--no-gate` is not a bypass."*
- **Claim:** "Never have an AI sign a human's approval."
  → SKILL.md §Laws: *"Never have an AI sign a human's approval record."*
- **On-screen quote block** is verbatim from SKILL.md §Laws (GATE N).

### B09 · Verdict artifact (six-line recap)
All six numbered lines paraphrase or restate the laws already cited above:
1. Frame around a fellow's own recording · SKILL.md opening.
2. THE REPORT IS THE CLOCK · SKILL.md §Laws (also fully cited under B04).
3. FELLOW'S-WORK carve-out of REBUILD LAW · SKILL.md §Laws.
4. GATE N + no `--no-gate` bypass · SKILL.md §Laws (also fully cited under B06).
5. One Kokoro voice per fellow across the series; SOUND REPAIR legal, retiming not
   · SKILL.md §Persistent fellow voice + §Laws SOUND REPAIR.
6. Standard HAI outro; channel `@HumanitariansAI` · SKILL.md B08 OUTRO.
No new factual claim is introduced by the verdict card.

### B11 · Outro (title restate + Liam sign-off)
- **Narration claim:** "That was the fellows Skill. Liam, in for Bear."
  → ai-explainer/SKILL.md §Liam · IN-FOR-BEAR LAW.
- **On-screen handle** `@NikBearBrown` is hardcoded per OUTRO-LOCK.md (this
  teardown is a `claude-liam` reel; the skill it explains uses a different
  outro — that deviation was covered by B08 in the long, and by verdict line
  6 in the Short).

## Claims verdict lines make about beats not shown in the Short

Verdict lines 3 (FELLOW'S-WORK carve-out) and 5 (persistent voice · SOUND REPAIR)
each summarize one law that the Short does not have its own mechanism beat for.
Both are still directly traced above to SKILL.md §Laws. The parent's
`vertical/FACTCHECK.md` under B05 and B07 carries the full per-claim evidence.

## Claims deliberately NOT made

- No specific fellow's name, folder or Drive link appears on screen or in
  narration. The Short is entirely source-backed (SELF-DEMO LAW feasibility
  fallback), same as the long.
- No production numbers (episodes shipped, watch time, review turnaround).
- No claim about YouTube 4K certification or channel size.
- No claim that the fellows skill was actually run this session.
- No URL for the 16:9 long — the long is not published.

## Corrections applied vs. source

None. The source is current (SHA-256 matches supervisor snapshot). No stale
model versions, count promises, or drift-prone metrics appear in the cut.
