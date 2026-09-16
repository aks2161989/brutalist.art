# Fact check — every narration claim traced to source

Source of truth: **`skills/make/fellows/SKILL.md`** (isolated toolkit snapshot,
SHA-256 `afd14d36428eac3cc954af49af4610206924cbcbbfb969cff339c02de0640131`;
supervisor's episode.source_sha256 `71d2303f780103e8947b7eeb3c55c362829ea0415e2df75b1a58980f48dbd6d3`).

Additional confirming reads: `skills/make/ai-explainer/SKILL.md`, `docs/PIPELINE-SAFETY.md`,
`docs/FELLOWS-SUBMISSION.md`, `OUTRO-LOCK.md`, `CLAUDE.md`.

## Per-beat claim → SKILL.md evidence

### B00 · Cold open
- **Claim:** "The fellows skill wraps a fellow's own recording without editing it."
  → SKILL.md §The shared skeleton: *"Same Claude-branded bookends as the siblings;
  the MIDDLE is the fellow's own video plus commentary around it."*
- **Claim:** "Branded bookends · Professor Bear's notes · HAI outro."
  → SKILL.md §The required beat spine (B00–B08) + §Brand facts.
- **Claim:** "The report plays untouched — audio and timing."
  → SKILL.md §Laws (THE REPORT IS THE CLOCK): *"…its own audio remains on the timeline.
  …but never retime, trim, speed up, or talk over it."*

### B01 · BLUF (hesitant writer)
- **Claim:** "The fellows report is the middle of the reel and it plays untouched."
  → SKILL.md §The required beat spine B04: *"The fellow's video PLAYS AS IS —
  pass-through beat."*
- **Claim:** "What the skill builds is the frame around it."
  → SKILL.md opening: *"The reel is a frame around their own report…"*

### B02 · Anatomy
- **Claim:** "SKILL.md — the doctrine, one required beat spine, five laws of its own."
  → SKILL.md §The required beat spine (B00–B08 named) + §Laws (five bulleted laws:
  THE REPORT IS THE CLOCK, SOUND REPAIR, FELLOW'S-WORK carve-out, GATE N, HONESTY).
- **Claim:** Fellow folder pattern `first-name-last-initial/YYYY-MM-DD-slug/`.
  → SKILL.md §Brand facts / Output + §Naming: *"lowercase `first-name-last-initial`"*
  and *"`YYYY-MM-DD-short-description-of-that-weeks-work`."*
- **Claim:** "transcript/, media/B04.mp4 (source), NOTES.md, BUILD-LOG.md."
  → SKILL.md §The transcript (`transcript/report.txt`) + §Flow step 2
  (draft `NOTES.md`) + §Flow step 5 (report → `media/B04.mp4`) + §Laws (SOUND REPAIR /
  GATE N logged in `BUILD-LOG.md`).
- **Claim:** "NOTES.md is a human gate — Kokoro will not speak them until Bear signs."
  → SKILL.md §Laws GATE N: *"The notes beats never go to audio until Bear has edited
  or signed `NOTES.md`."*

### B03 · Pipeline
- **Claim:** Nine-beat fixed spine.
  → SKILL.md §The required beat spine: B00 INTRO, B01–B03 THE WORK, B04 THE REPORT,
  B05–B06 PROFESSOR BEAR'S NOTES, B07 YOUR TURN, B08 OUTRO = 9 beats.
- **Claim:** "'What has [Name] been working on lately…'"
  → SKILL.md §The shared skeleton: *"the narrator asks Claude 'I wonder what
  Humanitarians AI fellow [name] has been working on lately…'"*
- **Claim:** "Two or three summary beats from the transcript."
  → SKILL.md B01–B03: *"2–3 beats. The selected narrator summarizes what the fellow
  built — from the transcript, one idea per beat."*
- **Claim:** "The standard HAI outro" (not title-restate).
  → SKILL.md B08 OUTRO: *"The STANDARD Humanitarians AI outro (OutroSeries / OutroCTA,
  humanitarians palette…). NOT the @NikBearBrown outro."*

### B04 · Mechanism · THE REPORT IS THE CLOCK
- **Claim:** "Every other Brutalist skill is audio-first; fellows inverts that for exactly one beat."
  → SKILL.md §Laws: *"THE REPORT IS THE CLOCK (the one exception to audio-first).
  Everywhere else narration MP3s are the master clock."*
- **Claim:** "No trim, no speed change, no voiceover, no re-timing."
  → SKILL.md §Laws: *"never retime, trim, speed up, or talk over it."*
- **Claim:** "The compiler transcodes container and resolution, and stops there."
  → SKILL.md §Laws: *"Transcode container/resolution to the reel spec (3840×2160
  landscape or 2160×3840 vertical, h264/AAC, contain/letterbox — never crop or stretch)."*
- **Claim:** "A trimmed cut is only legal when a human explicitly asks for it in the build log."
  → SKILL.md §Laws: *"If the human wants a trimmed cut, that is an explicit request
  logged in BUILD-LOG.md — never the skill's own call."*

### B05 · Mechanism · FELLOW'S-WORK CARVE-OUT
- **Claim:** "Every claude explainer has a REBUILD law…" (context).
  → ai-explainer/SKILL.md §Hard rules · REBUILD LAW.
- **Claim:** "Fellows carves out one exception; frames pulled from the fellow's own report
  play as themselves."
  → SKILL.md §Laws: *"FELLOW'S-WORK carve-out (of REBUILD LAW). Frames and clips from
  the fellow's own report play as THEMSELVES."*
- **Claim:** "Ken Burns on a still, or the clip untouched."
  → SKILL.md B01–B03: *"Visuals: frames pulled from the report (Ken Burns; FELLOW'S-WORK carve-out)…"*
- **Claim:** "Their receipt is the point; rebuilding it would falsify it."
  → SKILL.md §Laws: *"the fellow's artifact is the receipt; rebuilding it would
  falsify it."*
- **Claim:** "Everything else — context diagrams, notes cards — stays under REBUILD law,
  in the humanitarians palette."
  → SKILL.md §Laws: *"Everything that is NOT the fellow's own material (context
  diagrams, comparison charts, the notes cards) is rebuilt native, REBUILD LAW unchanged."*
  + §Brand facts Skin: *"RESULT/notes graphics render in the humanitarians palette."*

### B06 · Mechanism · GATE N
- **Claim:** "Professor Bear's notes are Bear's words."
  → SKILL.md §Laws heading: *"GATE N — Professor Bear's notes are BEAR'S words."*
- **Claim:** "The skill drafts them from the transcript, in plain register, as a starting point."
  → SKILL.md §Laws: *"The skill DRAFTS `NOTES.md` (feedback + next steps) from the
  transcript, in Bear's plain register, as a starting point."*
- **Claim:** "Nothing goes to Kokoro until Bear has edited or signed NOTES markdown."
  → SKILL.md §Laws: *"but the notes beats never go to audio until Bear has edited
  or signed `NOTES.md`."*
- **Claim:** "The runtime hashes the notes and the exact spoken wording."
  → SKILL.md §Laws: *"GATE N is logged in BUILD-LOG.md and bound to the notes
  and exact spoken text in `metadata.approvals.professor_notes`."*
  + PIPELINE-SAFETY.md §Human approval: *"`notes_sha256` … `narration_sha256`."*
- **Claim:** "Pending, stale, or missing signature blocks Kokoro, Remotion, and any final;
  --no-gate does not bypass."
  → SKILL.md §Laws: *"The runtime blocks pending or stale records; `--no-gate` is
  not a bypass."*
  + PIPELINE-SAFETY.md: *"Pending, missing or stale records block Kokoro generation,
  Remotion rendering, review assembly and direct final export."*
- **Claim:** "Never have an AI sign a human's approval."
  → SKILL.md §Laws: *"Never have an AI sign a human's approval record."*

### B07 · Mechanism · Persistent voice + SOUND REPAIR
- **Claim:** "Each fellow picks one Kokoro voice, once, and every episode uses that voice."
  → SKILL.md §Persistent fellow voice: *"Each fellow chooses one Kokoro voice
  before the first report is generated and keeps it across the whole report series."*
- **Claim:** "A name-based suggestion is a heuristic, never an identity claim."
  → SKILL.md §Persistent fellow voice: *"When the fellow has not supplied a
  preference, use the name only as a starting heuristic… This is not an identity claim."*
- **Claim:** "The fellow's explicit choice overrides it; a later change is a documented re-voice."
  → SKILL.md §Persistent fellow voice: *"The fellow's explicit preference always
  overrides the heuristic. A later voice change is a documented re-voice decision
  for the series, never a silent per-episode choice."*
- **Claim:** "If the report's audio is bad — quiet, hummy, clipped — normalize, denoise, high-pass."
  → SKILL.md §Laws SOUND REPAIR: *"quiet, clipped, hummy, roomy, wildly uneven — FIX IT…
  loudness-normalize… denoise (`afftdn`, or `arnndn`…), high-pass the rumble/hum
  (`highpass=f=80`…), and de-ess/limit clipping peaks."*
- **Claim:** "Timing stays. Voice stays."
  → SKILL.md §Laws SOUND REPAIR: *"timing untouched… Never pitch-shift, never
  time-stretch, never re-voice."*
- **Claim:** "Every filter applied is logged in the build log."
  → SKILL.md §Laws SOUND REPAIR: *"Every filter applied is logged in BUILD-LOG.md."*

### B08 · Falsifiability · sibling outro break
- **Claim:** "Every other claude explainer closes on the title-restate outro locked to @NikBearBrown."
  → ai-explainer/SKILL.md §Frame laws · OUTRO LAW: *"the terracotta period, handle
  beneath (`ClaudeTitleOutro` pattern…)"* + OUTRO-LOCK.md: *"HANDLE — `@NikBearBrown`,
  HARDCODED."*
- **Claim:** "Fellows does not. The last beat is the standard Humanitarians AI outro, in
  the humanitarians palette."
  → SKILL.md B08 OUTRO: *"The STANDARD Humanitarians AI outro (OutroSeries / OutroCTA,
  humanitarians palette, content from AUTHOR.MD's Humanitarians AI section)."*
- **Claim:** "If someone ships a fellows reel with the title-restate outro, that is a defect."
  → SKILL.md B08 OUTRO: *"**NOT** the @NikBearBrown outro — fellows is a HAI channel
  reel; `ClaudeTitleOutro` and its lock (OUTRO-LOCK.md) do NOT apply here."*

### B09 · Verdict artifact
- All six lines paraphrase or quote SKILL.md sections cited above; no new claims introduced.

### B10 · Your Turn
- The paste-ready prompt asks the viewer to PLAN (not execute) a dry-run and validate
  three properties. The rubric properties are direct SKILL.md/PIPELINE-SAFETY.md/OUTRO-LOCK
  checks:
  - `kind: source_report` + `audio_policy: preserve` → PIPELINE-SAFETY.md §"The source report
    owns its clock and sound" (JSON example).
  - `approvals` records PENDING with real fingerprints → PIPELINE-SAFETY.md §Human approval
    (JSON example) + build_safety.py's requirement that approvals include real subject SHA-256.
  - Standard HAI outro, not `ClaudeTitleOutro` → SKILL.md B08 OUTRO (as above).

### B11 · Outro (this teardown's own)
- **Claim in narration:** none about fellows itself — just "That was the fellows Skill.
  Liam, in for Bear." — IN-FOR-BEAR LAW (ai-explainer §Liam).

## Claims deliberately NOT made

- No specific fellow's name appears on screen or in narration.
- No production numbers (episodes shipped, watch time, review turnaround) — none are in SKILL.md.
- No claim about YouTube 4K certification or channel size — those are separate PM/publishing
  processes and not part of the fellows skill itself.
- No claim of running the fellows skill in this session. See SCRIPT.md §"What this reel does NOT do".

## Corrections applied vs. source

None. The source is current (SHA-256 matches supervisor snapshot). No stale model versions,
count promises, or drift-prone metrics appear in the reel.
