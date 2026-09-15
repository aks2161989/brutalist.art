# SCRIPT — Brutalist Utility: image_fetch.py
## Episode 45 · claude-liam-brutalist-runtime-image-fetch
### Voice: Liam (Kokoro am_onyx) · Channel: @HumanitariansAI

---

## B00 — Cold open (ClaudeComposerAsk)

**ON SCREEN:** Claude composer window. Greeting: "Selam, Liam." Topic: "Brutalist Utility." Segment: "image_fetch.py." Command types in. Running indicator. Output lines land.

**NARRATION:**
Every reel needs archival images, and Smithsonian alone stopped being enough. This is image_fetch.py — the multi-source fetch tool for the Brutalist pipeline. This is Liam, in for Bear.

---

## B01 — BLUF (BrutalistHesitantWriter)

**ON SCREEN:** Writer types "image_fetch.py is a download helper." Hesitates. Replaces "download helper" with "fetch-shelf pipeline." Final text holds.

**NARRATION:**
image_fetch.py fetches, optionally upscales with Topaz Photo AI, shelves with a provenance sidecar, and copies to your reel pantry in one call. Not a download helper — a pipeline. Four archives, one interface, license tracked to the file.

---

## B02 — The pipeline (SkillTeardownPipeline)

**ON SCREEN:** Horizontal phase diagram: `--source --id [--url]` → Resolve → Download → Upscale → Shelve → Sidecar → Pantry → `library/.jpg + .source.json`. Each node springs in. Footer note: "--url skips Resolve."

**NARRATION:**
The pipeline runs six phases. Resolve finds the full-res URL through the adapter. Download streams it to a temp directory. Topaz upscales it if installed. Shelve copies the file to the library. The sidecar writes the provenance record — source, license, credit, URL. An optional pantry step copies the shelved image straight into your reel. And if the record was already shelved, the tool returns the cached path and stops.

---

## B03 — The two paths (BinaryBranch)

**ON SCREEN:** Binary branch question: "Does --url skip the resolve step?" Left branch: "No --url — adapter lookup." Right branch: "--url supplied — bypass resolver." Resolver lands at bottom: "Smithsonian has an index. NASA, Wellcome, NLM require --url."

**NARRATION:**
The tool forks at one flag. Without --url, the adapter walks its own index to find the record, then resolves the full-res URL. Smithsonian has that index locally. NASA, Wellcome, and NLM do not. For those three, you supply the URL you already found, and the tool shelves it. --url also lets you override any adapter when you know the URL exactly.

---

## B04 — CLI flags (ClaudeCodeBeat)

**ON SCREEN:** Code block with the full Smithsonian invocation and then a NASA invocation showing --url. Spark line: "Smithsonian: index lookup. NASA: bring your URL."

**NARRATION:**
The Smithsonian adapter uses a local index — pass the record ID and it resolves the full-res URL itself. For NASA, Wellcome, or NLM, you supply the URL directly. Either way, --copy routes the shelved image into your reel's pantry folder, tagged by --beat. The slug comes from the title by default, or you set it with --slug.

---

## B05 — The four adapters (ClaudeScienceChipGrid)

**ON SCREEN:** 2×2 grid of adapter chips staggering in. smithsonian · nasa · wellcome · nlm_ihm. Caption: "Smithsonian's index is the only one that supports adapter.resolve() without --url."

**NARRATION:**
Four adapters, one interface. Smithsonian is the only one with a local search index — its resolve() implementation walks index.jsonl to find the full-res URL. NASA, Wellcome, and NLM implement the adapter interface without a local index, so they require --url. The registry is extensible: a new adapter adds one file to sources/ without touching image_fetch.py.

---

## B06 — Design tell (SkillTeardownMechanism)

**ON SCREEN:** Mechanism card. Heading: "Topaz is a peer, not a requirement." Body explains the tpai probe. Quote from source_core.py: the `if not Path(TPAI).exists()` block. Verdict: gets right.

**NARRATION:**
The Topaz step is the most interesting design decision. The upscaler is not configured, not required, and not an error path — it is simply probed by PATH. If tpai is on the system it runs; if it is not, the function returns None and the caller shelves the original. No flag, no fallback configuration, no error message that stops the pipeline. Availability is the contract.

---

## B07 — Verdict (ClaudeVerdictArtifact)

**ON SCREEN:** Artifact page. Title: "image_fetch.py." Heading: "The archival shelf, in one call." Four lines stagger in.

**NARRATION:**
The verdict. Four adapters, one registry. Topaz when present, original when not. Provenance sidecar for every image, automatic. And on every failure path, a specific message before the exit. The design gets extensibility right, and it gets graceful degradation right. The thing it relies on you to know: for three of the four adapters, you need to find the URL yourself.

---

## B08 — Your Turn (ClaudeComposerAsk)

**ON SCREEN:** Claude composer. Greeting: "Your turn." Command types in — a real paste-ready prompt. Running indicator. No output lines (viewer supplies them).

**NARRATION:**
Your turn. Take the reel you are building and run image_fetch.py on a real Smithsonian record. The prompt asks Claude to find the record ID, show you the exact command, and explain what the provenance sidecar will contain. Run it, open the sidecar, check the license field. If it reads CC0 or public-domain, that image earned its slot.

---

## B09 — Outro (ClaudeTitleOutro)

**ON SCREEN:** Title card: "Brutalist Utility: image_fetch.py." Handle: "@HumanitariansAI." Subline: "fetch · upscale · shelf · provenance."

**NARRATION:**
Brutalist Utility: image_fetch.py. Fetch an archival image, upscale it if you can, and shelve it with provenance. Liam, in for Bear.
