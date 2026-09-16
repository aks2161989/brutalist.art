# PROMPTS — Brutalist Utility: image_fetch.py

## B00 — Cold open composer prompt

```
Every reel needs archival images, and Smithsonian alone stopped being enough. I need one
tool that fetches from NASA, Wellcome, and NLM too — upscales with Topaz if it's installed,
and shelves every image with a provenance record I can actually trust in the reel.
```

Expected output lines:
- "four adapters: smithsonian · nasa · wellcome · nlm_ihm"
- "optional Topaz upscale — graceful when absent"
- "library shelf + sidecar + pantry copy in one call"

## B08 — Your Turn handoff prompt (paste-ready for viewers)

```
I'm building a Brutalist reel about climate science. Find me a relevant CC0 image from the
Smithsonian Open Access collection. Show me the image_fetch.py command that fetches it and
places it in my reel's pantry for beat B03. Then explain what the .source.json sidecar will
contain — specifically what the license and credit fields will say.
```

Expected Claude behavior:
1. Search Smithsonian Open Access for climate science imagery
2. Return a record ID (e.g. `nmah_1234567` or `nasm_SIL-...`)
3. Produce the exact command: `python3 runtime/scripts/image_fetch.py --source smithsonian --id <id> --copy <reel_path> --beat B03`
4. Describe the sidecar: source: smithsonian, license: CC0, credit: Smithsonian Institution, id: <id>, title: ..., url: <full_res_url>, source_url: https://si.edu/object/<id>

Test of success: open `<reel>/pantry/B03-<slug>.jpg` — image is there; open `library/smithsonian/images/<stem>.source.json` — license reads CC0.

## Narration prompts used to generate Kokoro audio (am_onyx)

These are the exact narration_text strings passed to generate_audio_kokoro.py per beat:

- B00: "Every reel needs archival images, and Smithsonian alone stopped being enough. This is image_fetch.py — the multi-source fetch tool for the Brutalist pipeline. This is Liam, in for Bear."
- B01: "image_fetch.py fetches, optionally upscales with Topaz Photo AI, shelves with a provenance sidecar, and copies to your reel pantry in one call. Not a download helper — a pipeline. Four archives, one interface, license tracked to the file."
- B02: "The pipeline runs six phases. Resolve finds the full-res URL through the adapter. Download streams it to a temp directory. Topaz upscales it if installed. Shelve copies the file to the library. The sidecar writes the provenance record — source, license, credit, URL. An optional pantry step copies the shelved image straight into your reel. And if the record was already shelved, the tool returns the cached path and stops."
- B03: "The tool forks at one flag. Without --url, the adapter walks its own index to find the record, then resolves the full-res URL. Smithsonian has that index locally. NASA, Wellcome, and NLM do not. For those three, you supply the URL you already found, and the tool shelves it. --url also lets you override any adapter when you know the URL exactly."
- B04: "The Smithsonian adapter uses a local index — pass the record ID and it resolves the full-res URL itself. For NASA, Wellcome, or NLM, you supply the URL directly. Either way, --copy routes the shelved image into your reel's pantry folder, tagged by --beat. The slug comes from the title by default, or you set it with --slug."
- B05: "Four adapters, one interface. Smithsonian is the only one with a local search index — its resolve() implementation walks index.jsonl to find the full-res URL. NASA, Wellcome, and NLM implement the adapter interface without a local index, so they require --url. The registry is extensible: a new adapter adds one file to sources/ without touching image_fetch.py."
- B06: "The Topaz step is the most interesting design decision. The upscaler is not configured, not required, and not an error path — it is simply probed by PATH. If tpai is on the system it runs; if it is not, the function returns None and the caller shelves the original. No flag, no fallback configuration, no error message that stops the pipeline. Availability is the contract."
- B07: "The verdict. Four adapters, one registry. Topaz when present, original when not. Provenance sidecar for every image, automatic. And on every failure path, a specific message before the exit. The design gets extensibility right, and it gets graceful degradation right. The thing it relies on you to know: for three of the four adapters, you need to find the URL yourself."
- B08: "Your turn. Take the reel you are building and run image_fetch.py on a real Smithsonian record. The prompt asks Claude to find the record ID, show you the exact command, and explain what the provenance sidecar will contain. Run it, open the sidecar, check the license field. If it reads CC0 or public-domain, that image earned its slot."
- B09: "Brutalist Utility: image_fetch.py. Fetch an archival image, upscale it if you can, and shelve it with provenance. Liam, in for Bear."
