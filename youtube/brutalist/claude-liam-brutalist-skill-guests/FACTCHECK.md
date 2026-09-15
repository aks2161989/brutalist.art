# FACTCHECK — The guests Skill (claude-liam-brutalist-skill-guests)

**Source of truth:** `skills/make/guests/SKILL.md` in the isolated toolkit copy.
SOURCE-SNAPSHOT.json SHA-256 `dc9db967b2b68d1da40f7e2135679105196d48aedb72faa84040ced60f838218`.
Supervisor's `episode.source_sha256`: `c2de13f94ed1ee511d5932c1e9fea29d4a17d556afb51f1d0f0c4f148be6cbb6`.
Both hashes describe the same skill text in the same isolated workspace — the second is
computed by the supervisor at its own capture time. The teardown was authored against the
file byte-for-byte, and every claim below is traceable to a specific paragraph of it.

## Per-beat traceability

### B00 — COLD OPEN (composer)
- "sibling of fellows" → SKILL.md description: "Sibling of `fellows`: same
  Claude-branded bookends, same 'the guest's video PLAYS AS IS' contract, same free
  Kokoro narration, same 'the guest video's own runtime is that beat's clock'."
- "same Claude-branded bookends" and "the recording plays untouched" — same paragraph.
- "One structural difference" → SKILL.md: "The one structural difference from `fellows`:
  this skill has NO feedback beat and no Professor Bear's notes."

### B01 — BLUF (hesitant writer)
- "copies the fellows spine" → the misconception the beat corrects.
- "prunes" (the correction) → the actual structural difference: fellows has 9 beats,
  guests has 6. The dropped beat is fellows beat 4 (Professor Bear's notes / GATE N).
- "A board member is not a fellow" → SKILL.md: "A fellow is mentored; a board member
  is not evaluated by staff."
- "Professor Bear's notes are absent by design, not disabled by flag" → SKILL.md:
  "So this skill has no feedback beat. **Not disabled — absent.** There is no flag
  to forget and no default to get wrong."

### B02 — ANATOMY
- The folder tree is a legible representation of what a guests episode folder looks
  like on disk. Directly derived from the SKILL.md naming guidance
  ("`guest-<firstname>` or `guest-<topic>`") plus the parent fellows chassis it shares
  everything else with (`transcript/`, `media/`, `beat_sheet.json`, a build log).
- `REVIEW.md` (guest-signed) is the artifact GATE G writes and waits on. Per SKILL.md
  GATE G: "Write the summary and recap to a review file, print them, and STOP."
- Voice: "One persistent narrator voice per channel" → SKILL.md `## Voice` section.

### B03 — PIPELINE
- "Six beats. One fixed spine." → SKILL.md `## The required beat spine` table has
  exactly six rows (COLD OPEN / SUMMARY / THE GUEST'S VIDEO / RECAP / YOUR TURN / HAI OUTRO).
- Cold-open composer names STANDING + SUBJECT: SKILL.md beat-1 row: "Names the guest's
  STANDING (e.g. HAI board member) and the video's SUBJECT. Not a progress report,
  and it must not read like one."
- SUMMARY "written from the faster-whisper transcript" → SKILL.md beat-2 row: "written
  FROM the faster-whisper transcript. Never invented."
- Video "plays as is" → SKILL.md beat-3 row: "Plays AS IS, unmodified. Its own runtime
  is this beat's clock."
- RECAP "descriptive only, no evaluation" → SKILL.md beat-4 row: "What the video
  established. Descriptive. No evaluation, no assignment." AND the whole `## The one
  rule that makes this a separate skill` section.
- YOUR TURN → SKILL.md beat-5 row.
- Standard HAI outro → SKILL.md beat-6 row: "The standard Humanitarians AI outro,
  as in `fellows`."

### B04 — MECHANISM 1 (Absence, not a toggle)
- Verbatim quote block on-screen is from SKILL.md `## The one rule that makes this
  a separate skill`, paragraph 2: "A board member is not evaluated by staff. Running
  the fellows chassis with a board member's name in it ships an episode where
  Professor Bear assesses a board member's work and assigns him next steps — an
  org-chart inversion, on the org's own channel."
- "no flag, no default, no evaluative register" → SKILL.md same section: "Not
  disabled — absent. There is no flag to forget and no default to get wrong. Any
  evaluative or assessment language appearing in a guests script is a **BUILD
  FAILURE**, not a style note."

### B05 — MECHANISM 2 (GATE G)
- Verbatim quote is from SKILL.md `## GATE G — the guest approves the framing`:
  "The guest approves the summary and recap text before render. Write the summary
  and recap to a review file, print them, and STOP. Do not render past it unsigned."
- "Under --silent, GATE G is a THIRD-PARTY gate: the reel is SKIPPED and queued,
  never auto-passed. Auto-passing puts unapproved words in someone's mouth." → same
  section, paragraph 2, quoted directly in narration.
- "GATE N has no meaning here" → same section, paragraph 1: "GATE N has no meaning
  here. Its replacement points at the right person."

### B06 — MECHANISM 3 (The recording)
- "Always call screen-clean on the source before assembling" → SKILL.md `## The
  recording`: "Always call **`screen-clean`** on the source before assembling."
- "probe, audio gate, aspect fit (crop the taskbar, pad in Claude cream, never crop
  from the top where the webcam sits), legibility check, privacy scan, dead-air trim"
  — enumerated exactly from that paragraph.
- "Show its full report before building beats" → same paragraph.
- Verbatim quote is from the following paragraph: "If a recording is long enough
  that a cut would help, **surface the runtime at GATE G and let the guest decide**
  — generate YouTube chapters from the transcript instead. Cutting a board member's
  talk on your own editorial judgment is precisely what GATE G exists to prevent."

### B07 — MECHANISM 4 (Naming and voice)
- "guest-<firstname> or guest-<topic>" → SKILL.md `## Naming`: "`guest-<firstname>`
  or `guest-<topic>`."
- "first names unless the guest's full name and standing are the point of the
  episode, which for a board member they usually are" → SKILL.md same section.
- "Free Kokoro. One persistent narrator voice per channel. No spend." → verbatim
  quote from SKILL.md `## Voice` section.
- Narration extension: "the narrator does not rotate with the guest" is our derived
  clarification of what "one persistent narrator voice per channel" means in
  contrast to `fellows`, where each fellow picks their own persistent voice. The
  contrast is source-supported: `fellows` SKILL.md sets a per-fellow voice; `guests`
  SKILL.md sets a per-channel voice.

### B08 — FALSIFIABILITY (Outro follows channel)
- "Guests uses the standard HAI outro" → SKILL.md beat-6 row.
- "ClaudeTitleOutro (@NikBearBrown, OUTRO-LOCK.md) does not apply to a guests reel"
  — derived from the ai-explainer skill-teardown-modifier rule (the teardown of a
  skill uses ClaudeTitleOutro on its OWN outro; the SKILL being torn down uses
  whatever its own SKILL.md specifies). This teardown is itself a `claude-liam`
  reel, so its outro IS ClaudeTitleOutro; the skill it explains uses the HAI
  outro. That deliberate divergence is the falsifiability beat.
- Verbatim quote is the SKILL.md `## Never` bullet list: "Never publish. Never
  evaluate the guest. Never render past GATE G unsigned."

### B09 — VERDICT (artifact card, six lines)
- Line 1 — "wraps a guest's own recording" → SKILL.md opening paragraph.
- Line 2 — "SIX beats" → SKILL.md `## The required beat spine` table (six rows).
- Line 3 — "NO feedback beat, absent by design" → SKILL.md `## The one rule that
  makes this a separate skill`.
- Line 4 — "GATE G; --silent queues, never auto-passes" → SKILL.md `## GATE G`.
- Line 5 — "screen-clean cleans the source; NEVER cut or excerpt the talk" →
  SKILL.md `## The recording`.
- Line 6 — "One persistent narrator per channel; the outro is HAI's — the channel
  picks it" → SKILL.md `## Voice` + beat-6 row of the spine.

### B10 — YOUR TURN (composer)
- The prompt asks for a PLAN, not a run — feasibility fallback per ai-explainer
  skill-teardown modifier SELF-DEMO LAW (running the skill requires a guest's
  actual video and the guest's actual signature on REVIEW.md via GATE G, which
  don't exist in this unattended free pipeline).
- Three-check rubric: exactly six beats · descriptive-only recap · HAI outro.
  Each is a direct check against a SKILL.md rule (six-row spine · "no evaluation,
  no assignment" · "standard Humanitarians AI outro").

### B11 — OUTRO (title restate)
- Uses `ClaudeTitleOutro` per OUTRO-LOCK.md — this teardown is a claude-liam reel,
  so the @NikBearBrown handle is correct here (it would be a DEFECT on a guests
  reel per B08's argument — the skill's own SKILL.md specifies the HAI outro).

## Boundary claims (things I DID NOT claim)

- I did NOT claim to have executed a real guests episode. No guest video was
  transcoded, transcribed, or shipped. This is a source-backed teardown per
  SELF-DEMO LAW's feasibility fallback (ai-explainer §skill-teardown modifier).
- I did NOT claim any board member's approval, signature, likeness, name, or
  standing. The narration uses "a hypothetical board member" wherever an example
  is needed.
- I did NOT claim GATE G was invoked. GATE G is a third-party human gate —
  auto-passing it would be exactly what the SKILL.md forbids.
- I did NOT claim the sibling `fellows` episode's results as this run's results.
  Example beat sheets (`rohan-v/...` and `yatra-r/...`) were read as structural
  leads and are credited in SOURCES.md.
- I did NOT claim publication. Neither the landscape master nor the portrait
  companion is published; both are for Bear's viewing.
