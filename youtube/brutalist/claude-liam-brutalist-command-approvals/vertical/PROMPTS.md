# PROMPTS — Brutalist Command: art approvals

This reel does not call any generative image or video models. All beats are
Remotion scenes rendered from source props. The two visible prompts are:

## B00 — the cold-open ASK typed into the composer

> Before I sign anything on a fellows reel, show me exactly what I would be
> signing. Do not sign it for me. Just print the fingerprints.

Runs on top of `ClaudeComposerAsk` (16:9) / `ClaudeComposerAsk916` (9:16).
Segment label reads `art approvals`. Output lines under the composer:

- prints subjects (voice + professor_notes) — one SHA-256 each
- validates pasted metadata.approvals against those SHAs
- writes zero files — audit only, never signs

## B10 — the YOUR TURN prompt for the viewer

> Point Claude Code at a fellows reel of yours. Run `./art approvals <reel>
> --fingerprints` and copy the JSON. Paste it into `metadata.approvals` in
> `beat_sheet.json` as human review records with `status: "approved"`,
> `reviewer_type: "human"`, your name in `reviewed_by`, and a full ISO-8601
> `reviewed_at` (with a timezone offset). Then re-run `./art approvals <reel>`
> with no flag. Read me the exit code and the last log line. Do NOT fill in
> `reviewed_by` for me — that is the field an agent must never write.

Rendered by `ClaudeComposerAsk` / `ClaudeComposerAsk916`, greeting `Your Turn`,
runningText `paste this into Claude Code…`. Three grading lines follow:

- step 1 — `--fingerprints` returns two subject blocks with SHA-256s
- step 2 — pasted record fields must be human-authored and dated
- step 3 — the follow-up validate returns exit 0 with no output

Narration reads the prompt aloud verbatim, then discusses the grading rubric.

## Beat-prefixed instruction cards

None. This reel's visuals are pure Remotion compositions; no image/video
generators are called. Code cards are typed strings; hesitant-writer trigger
words are literal.
