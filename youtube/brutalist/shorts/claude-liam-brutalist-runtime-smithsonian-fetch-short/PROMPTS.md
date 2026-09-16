# PROMPTS — Brutalist Utility: smithsonian_fetch.py — Short
# Short run_id: 7d5225769ced4a06a72051a66def374b  |  2026-09-14
# B10 (Your Turn) was dropped in this Short. Cold open command (B00) retained.

## B00 — Cold open command (shown in ClaudeComposerAsk)

```
python3 runtime/scripts/smithsonian_fetch.py "UNIVAC computer console"
```

Topic: BRUTALIST · UTILITIES
Segment: smithsonian_fetch.py
Running text: fetching from Smithsonian Open Access...

## B10 — Handoff prompt (paste-ready for the viewer)

```
Read runtime/scripts/smithsonian_fetch.py and runtime/scripts/smithsonian_index.py.
I want to add a CC0 image from the Smithsonian Open Access collection to beat B07
of my reel at <path/to/my-reel>.

First tell me:
1. Whether the library/smithsonian/index.jsonl exists (and how to build it if not).
2. The top 3 search candidates for "<my topic>" using the scoring logic in the script.
3. Which one you recommend and why (object_type bonus, title match score).

Then fetch the recommended image, shelve it with the provenance sidecar, and drop
it into my-reel/pantry/ as B07-<slug>.png. After the copy, print the contents of
the .source.txt sidecar so I can verify the CC0 attribution is complete.
```

Expected output / test of success:
- library/smithsonian/images/si-<id>-<slug>.jpg created
- library/smithsonian/images/si-<id>-<slug>.source.txt contains CC0 + correct SI id
- reel/pantry/B07-<slug>.png created
- .source.txt sidecar shows CC0, SI_ID, Title, Unit, Credit, Source URL, License
