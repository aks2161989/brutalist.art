# GDD evidence ledger

`gdd-evidence.json` has `schema_version: 1`, `document` with `sha256`, `sections`,
`excerpts`, and `evidence` arrays. Hash the actual UTF-8 GDD bytes before and after
the work; do not normalize the source just to make a hash pass.

Each section has `heading` (the exact Markdown `## ` heading without its prefix),
`beat_ids`, or an explicit `exclusion` reason instead. Every top-level section
must appear once. Coverage means the narration actually explains the section,
not that a title was flashed on screen. Human review still checks that claim.

Each excerpt has `beat_id`, one-based `start_line` and `end_line`, and `text`
extracted verbatim. Put that text in the beat's `shot.remotion.props.excerpt`;
line wrapping is presentation, not permission to rewrite a quote. Short prose
paraphrases belong in the explanation/cards and are labeled as explanation.

Each evidence item has `path` relative to the reel, `sha256`, `method` and
`supports`. Copy small records/screenshots or link them in the source prose.
The checker forbids escaping the reel or symlinking out of it. Keep media hashes
even though media stays out of Git. Record the source game's build ID separately
in FACTCHECK/SOURCES and its build manifest. Do not count a file's presence as
proof that the claimed assertion passed; read the result and its method.

Every body beat includes `design_status` chosen from `proposed`, `implemented`,
`observed`, `pending`, or `comparison`. Comparison beats explicitly separate the
states in their visible labels and narration. In particular, a test suite passing
34 assertions does not close 22 differently defined acceptance cases or four
human design gates. Future features get proposed diagrams, never fake gameplay.

Keep machine evidence separate from human judgments. Approval records are never
fabricated, copied from another film, or inferred from a render succeeding.
