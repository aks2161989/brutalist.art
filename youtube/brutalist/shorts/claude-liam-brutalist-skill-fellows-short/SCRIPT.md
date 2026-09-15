# Script — The fellows Skill (Short cut)

Slug: `claude-liam-brutalist-skill-fellows-short`
Aspect: 9:16 · 2160×3840 · 24 fps · Kokoro `am_onyx` · captions off
Playlist: Brutalist · Channel: `@HumanitariansAI`
Derived from: `claude-liam-brutalist-skill-fellows-vertical`
Cut strategy: whole-beat cut (see `CUT-PLAN.json`)

## Kept beats — narration exactly as it plays

**B00 · ASK (13.17 s) — Claude composer cold open**

> Hallo, this is Liam, in for Bear. Today we tear down the fellows skill.
> Every Humanitarians AI fellow ships weekly research videos — this is the
> skill that wraps their own recording without editing it. Here is the
> mental model.

**B01 · BLUF (14.42 s) — hesitant writer: `re-cuts` → `frames`**

> The easy read — the one the name invites — is that fellows re-cuts the
> fellow's video into something Claude approves of. It does not. The
> fellow's report is the middle of the reel and it plays untouched. What
> the skill builds is the frame around it — bookends, notes, and a handoff.

**B03 · FRAMEWORK (19.79 s) — nine-beat spine**

> The spine is fixed. Nine beats. The composer asks what the fellow has
> been working on. Two or three summary beats read from the transcript.
> Then the fellow's video plays as is — that is beat four. Two beats of
> Professor Bear's notes — feedback, then next steps. A Your Turn prompt,
> and the standard Humanitarians AI outro. Same shape every episode. Only
> the middle is the fellow's own material.

**B04 · MECHANISM · ACT 1 (23.75 s) — THE REPORT IS THE CLOCK**

> First design decision, and it is the sharpest. Every other Brutalist
> skill is audio-first — Kokoro generates the narration and the visuals
> conform to that clock. Fellows inverts that for exactly one beat. Beat
> four's clock is the report's own runtime. No trim, no speed change, no
> voiceover, no re-timing. The compiler transcodes container and
> resolution, and stops there. A trimmed cut is only legal when a human
> explicitly asks for it in the build log.

**B06 · MECHANISM · ACT 3 (27.46 s) — GATE N**

> Third decision, and it is where the skill earns its trust. Professor
> Bear's notes are Bear's words. The skill drafts them from the
> transcript, in plain register, as a starting point — but nothing goes
> to Kokoro until Bear has edited or signed NOTES markdown. The runtime
> hashes the notes and the exact spoken wording; a pending record, a
> stale hash, or a missing signature blocks Kokoro, Remotion, and any
> final. The dash-dash no-gate flag exists but it does not bypass this.
> Never have an AI sign a human's approval.

**B09 · VERDICT (26.75 s) — artifact card, six lines**

> The verdict. Fellows is a frame around a fellow's own recording —
> nothing more, nothing less. The report is the clock, so the fellow's
> runtime rules beat four. The fellow's frames play as themselves.
> Professor Bear's notes require Bear's actual signature. The fellow
> picks a Kokoro voice once and keeps it across the whole series, and
> the audio can be repaired but never retimed. And the outro is the HAI
> outro — because fellows is a HAI reel. Skip any of these, and the
> frame breaks the very thing it exists to protect.

**B11 · OUTRO (3.38 s) — title restate + Liam sign-off**

> That was the fellows Skill. Liam, in for Bear.

## Total measured

- Timeline: **128.708 s** (frame-aligned per-beat sum)
- Encoded MP4 container: 128.708 s · video: 128.667 s · audio: 128.708 s
- SHORTS_CAP_S = 180.0 s. All three durations strictly less than the cap.

## Editorial notes on the whole-beat cut

- **B06 opens "Third decision"** — B04 announces "First design decision" and
  B05/B07 were cut, so the numbering is a small artifact. B06 was retained
  because GATE N (human signature of Professor Bear's notes) is the safety
  hinge the whole skill turns on; dropping it would strip the Short of the
  single most important human-decision that remains. A one-word rewrite
  ("Third" → "Next") was considered and rejected because it crosses the
  regenerate-audio threshold; the number "Third" reads as a minor stumble,
  not a broken reference.
- **B09 verdict recaps six laws** — three of them (FELLOW'S-WORK carve-out,
  persistent Kokoro voice / SOUND REPAIR, HAI outro deviation) were
  covered by B05, B07, B08 in the long. In the Short they appear only as
  single verdict lines. That is the point of a verdict — one useful line
  per law is enough at Short length; the full mechanism belongs in the 16:9.
- **B11 is the parent outro, unchanged.** No funnel outro was regenerated
  (`--no-outro-rewrite`); no silent endcard was appended (`--no-endcard`).
  The Short ends on Liam's title sign-off, mirroring the long.
- **Reference to the 16:9 long** — not included as an on-screen URL or
  narration line, since the long is not published. The parent title
  restate ("The fellows Skill.") is the only reference the viewer sees.

## Dropped beats — narration NOT in this cut

`B02` (folder anatomy · 21.65 s) · `B05` (FELLOW'S-WORK carve-out · 22.55 s)
· `B07` (persistent voice + SOUND REPAIR · 26.84 s) · `B08` (HAI-outro
falsifiability · 26.26 s) · `B10` (Your Turn dry-run assignment · 35.73 s).
Full narration and evidence for each is preserved in the parent reel's
`vertical/SCRIPT.md`, `vertical/FACTCHECK.md` and `vertical/SHOTLIST.md`.
