# SCRIPT — The guests Skill

Voice: Liam (in for Bear), Kokoro `am_onyx`, free, local. 12 beats. No
captions. Every beat's `narration_text` and `role_note` is authored below;
the beat-sheet is the executable version. The misconception the hesitant
writer fixes (B01) is `copies` → `prunes` — a fellow is mentored, a board
member is not.

## B00 — COLD OPEN

> Hallo, this is Liam, in for Bear. Today we tear down the guests skill.
> It is the sibling of fellows — same Claude-branded bookends, same contract
> that a person's recording plays untouched. One structural difference.
> Here is the mental model.

Cold open composer names Liam-in-for-Bear (IN-FOR-BEAR LAW) and previews the
teardown's one-sentence thesis. Folder chip: `@HumanitariansAI`.

## B01 — BLUF (hesitant writer)

> The easy read — the one the sibling relationship invites — is that guests
> copies the fellows spine and swaps the name. It does not. Guests
> deliberately prunes one beat. A fellow is mentored; a board member is not.
> Professor Bear's notes are absent by design, not disabled by flag.

The writer types `copies`, corrects to `prunes`, then completes the sentence.
Root-cause fix in the sheet, not the check, when Gate V flagged 54 % coverage
at fontSize 148: bumped to 162 / lineSpacing 1.25 for the landscape, and to a
five-line split at 130 / 2.4 for the portrait.

## B02 — Anatomy

> First, the anatomy. On the toolkit side there is SKILL.md — the doctrine,
> the six-beat spine, GATE G, and the rules that make this a separate skill.
> On the guest's side there is a per-episode folder: a first name or the
> topic, then a dated slug. Inside it: the faster-whisper transcript, the
> source recording sitting in media, a REVIEW markdown the guest must sign
> before the summary and recap render, and a build log. Small on disk. Human
> where it matters.

The folder tree is a legible reference of what a guests episode looks like on
disk — same convention the SKILL.md names. `REVIEW.md` is highlighted with a
callout as a THIRD-PARTY gate (guest-signed, not Bear-signed).

## B03 — Pipeline

> The spine is fixed. Six beats. Not nine. The composer cold open names the
> guest's standing and the video's subject — never a progress report. A
> summary beat written from the faster-whisper transcript. Then the guest's
> video plays as is — that is beat three. A recap, descriptive only, no
> evaluation. A Your Turn prompt. And the standard Humanitarians AI outro.
> Same shape every episode. Only the middle is the guest's own material.

Five phase nodes with `THE VIDEO` accented terracotta — the beat that inverts
audio-first (per the fellows SKILL.md's `THE REPORT IS THE CLOCK`, inherited
here by the `plays AS IS, unmodified` clause).

## B04 — MECHANISM Act 1 — Absence, not a toggle

> First design decision, and it is the sharpest. Fellows has a feedback beat
> — Professor Bear's notes, human-signed, GATE N. Guests does not. Not
> disabled, not opt-out — absent. There is no flag to forget and no default
> to get wrong. The rationale is one sentence from the SKILL.md, and it is
> worth reading verbatim. A board member is not evaluated by staff. Running
> the fellows chassis with a board member's name in it ships an episode
> where Professor Bear assesses a board member's work and assigns him next
> steps — an org-chart inversion, on the org's own channel.

Verbatim quote block on-screen matches SKILL.md `## The one rule that makes
this a separate skill`. Verdict pill: `PREVENTS AN ORG-CHART INVERSION`.

## B05 — MECHANISM Act 2 — GATE G

> Second decision. GATE N has no meaning here — its replacement points at the
> right person. GATE G. The guest approves the summary and recap text before
> render. You are paraphrasing someone else's talk in your own words and
> putting their face in a branded episode. Write the summary and recap to a
> review file, print them, and stop. Do not render past it unsigned. Under
> dash-dash silent, GATE G is a third-party gate — the reel is skipped and
> queued, never auto-passed. Auto-passing puts unapproved words in someone's
> mouth.

Verbatim quote block from SKILL.md `## GATE G`. Verdict pill: `NO AUTO-PASS
ON A THIRD PARTY`.

## B06 — MECHANISM Act 3 — The recording

> Third decision, and it protects the recording itself. Always call
> screen-clean on the source before assembling. It handles the probe and the
> audio gate, the aspect fit — crop the taskbar, pad in Claude cream, never
> crop from the top where the webcam sits — the legibility check, the
> privacy scan, and the dead-air trim. Show its full report before building
> beats. And the harder rule underneath. Never crop or excerpt the guest's
> talk to fit a runtime. If a recording is long enough that a cut would
> help, surface the runtime at GATE G and let the guest decide. Generate
> YouTube chapters from the transcript instead. Cutting a board member's
> talk on your own editorial judgment is precisely what GATE G exists to
> prevent.

Verbatim quote block from SKILL.md `## The recording`. Verdict pill:
`CHAPTERS, NOT CUTS`.

## B07 — MECHANISM Act 4 — Naming and voice

> Fourth decision. Naming and voice. The slug is guest-firstname or
> guest-topic — follow the channel's privacy posture, first names by default.
> Standing gets named when the guest's full name and standing are the point
> of the episode — for a board member, they usually are. And the voice
> belongs to the channel, not to the guest — one persistent narrator voice
> per channel, free Kokoro, no spend. The guest does not pick a voice the
> way a fellow does, because a guest is not on a weekly cadence — the
> narrator is the channel's consistent framing around a rotating cast of
> visitors.

Contrast with the sibling `fellows` skill (per-fellow persistent voice) is
documented in `FACTCHECK.md`. Verdict pill: `CHANNEL VOICE · NOT A PER-GUEST
SWAP`.

## B08 — FALSIFIABILITY — The outro follows the channel

> Falsifiability. This is a claude-liam teardown, so its own outro is the
> title-restate — you will see it in ten seconds. But the skill we are
> tearing down does not use that outro. Guests is a HAI-channel reel. Its
> last beat is the standard Humanitarians AI outro, in the humanitarians
> palette, on the same channel as its folder chip. If someone ships a guests
> reel with the title-restate outro locked to at-NikBearBrown, that is a
> defect — not a style choice. The outro follows the channel, and the
> channel is HAI.

Negative-polarity verdict pill: `WRONG OUTRO = DEFECT`. Verbatim quote:
SKILL.md `## Never`.

## B09 — VERDICT (artifact card)

> The verdict. Guests is a frame around a guest's own recording — nothing
> more, nothing less. Six beats, not nine. Professor Bear's notes are absent
> by design — a board member is not evaluated by staff. GATE G moves the
> signature from Bear to the guest, and dash-dash silent will queue the
> reel, never auto-pass it. Screen-clean cleans the recording, but the talk
> itself is never trimmed to fit a runtime. The narrator voice belongs to
> the channel, not the guest. And the outro is the standard HAI outro —
> because the channel is HAI.

Six-line artifact card `A frame. Not a re-edit.` recapitulates the skill.

## B10 — YOUR TURN

> Your turn. Paste this into Claude Code: read the guests skill, then plan —
> do not run — a dry-run guests episode. Assume a hypothetical board member
> with a three-minute talk. Draft the cold-open composer that names their
> standing and the subject, a summary beat written from a fabricated
> transcript labeled clearly as a fixture, a recap that is purely
> descriptive with no grading language, a paste-ready Your Turn prompt, and
> the metadata approvals block for GATE G with status pending. Read the plan
> and check three things. Are there exactly six beats — no feedback beat
> between the video and the recap. Is the recap descriptive only, with no
> evaluative words. And does the outro name the standard HAI outro, never
> ClaudeTitleOutro.

Dry-run per SELF-DEMO LAW's feasibility fallback (a real run requires a
guest's video and their signature on REVIEW.md via GATE G — neither is
available in this free unattended pipeline). Each of the three rubric checks
maps to a specific SKILL.md rule.

## B11 — OUTRO

> That was the guests Skill. Liam, in for Bear.

`ClaudeTitleOutro` per OUTRO-LOCK.md — the handle `@NikBearBrown` here is
correct because THIS TEARDOWN is a claude-liam reel; the skill it explains
uses the HAI outro instead (that deviation is B08's argument).
