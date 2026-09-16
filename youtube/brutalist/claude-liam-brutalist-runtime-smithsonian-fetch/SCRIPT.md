# SCRIPT — Brutalist Utility: smithsonian_fetch.py
# run_id: 742a1549e73142e4b6d655986b0ae560  |  2026-09-14

---

## B00 — Cold Open (ClaudeComposerAsk)

**ON SCREEN:** Claude composer. Greeting "Annyeong, Liam" in serif above. Command
types: `python3 runtime/scripts/smithsonian_fetch.py "UNIVAC computer console"`.
Running indicator. Output lines stagger in.

**NARRATION:**
"Hi, this is Liam, in for Bear. smithsonian_fetch.py brings CC0 images from the
Smithsonian Institution into your Brutalist reel — one at a time, with provenance.
It searches a local index, resolves the full-resolution URL through the SI API,
downloads, optionally upscales with Topaz Photo AI, and shelves the result.
Let me show you what it actually does."

---

## B01 — BLUF (BrutalistHesitantWriter)

**ON SCREEN:** Text types on cream ground. "smithsonian_fetch.py is a downloader
for CC0 museum images." then hesitates — "downloader" struck, "provenance-pipeline"
typed. Continues: "... Attribution and provenance are handled manually." — "manually"
struck, "automatically" typed.

**NARRATION:**
"The framing that sticks wrong is that this is just a download tool. It's not.
It's a provenance pipeline: CC0-only by design, an upscale step through Topaz
Photo AI when that tool is present, and a source sidecar — SI object id, credit,
license, URL — written automatically next to every image. You don't track
attribution; the script does it for you."

---

## B02 — Pipeline Framework (SkillTeardownPipeline)

**ON SCREEN:** Six-node horizontal flow animates in: INDEX → LOOKUP → RESOLVE →
DOWNLOAD → UPSCALE → SHELVE. Nodes drop in one by one with terracotta arrows.
RESOLVE node is terracotta-accented (the interesting gate).

**NARRATION:**
"The pipeline is metadata-first. The index must already exist — built by
smithsonian_index.py — before you fetch anything. A lookup finds the record
by id or text search. Resolve calls the SI content-detail endpoint for the
full-resolution CC0 URL. Download, upscale with Topaz if available, and shelve
with the provenance sidecar."

---

## B03 — Worked Example: Text Search (ClaudeCodeBeat)

**ON SCREEN:** Dark code card. Title: "Text search + interactive pick".
Code shows the search command and annotated output — ranked candidates with
object type tags and thumbnail notes.

**NARRATION:**
"Here is a text search. The script tokenizes your query — dropping stop words,
short words, and domain noise like 'smithsonian', 'collection', 'national' —
then scores every record in the local index. Candidates display with their
SI unit, object type, and thumbnail URL. You pick a number, or pass --yes to
auto-accept the top hit."

---

## B04 — Scoring Mechanism (SkillTeardownMechanism)

**ON SCREEN:** Cream stage. Heading: "The ranking is intentional." Body shows the
four-tier score table: title match +4, token match +2, apparatus bonus +1.5,
ephemera penalty -1.0. Quote from source: "APPARATUS_TYPES / EPHEMERA_TYPES".

**NARRATION:**
"The ranking isn't alphabetical — it's designed. A word in the title scores four
points; a token match scores two. Hardware types — computer, terminal, instrument —
get a 1.5 bonus. Ephemera types — pamphlet, photograph, report — get a one-point
penalty. When you search for a computer, you want the machine, not the manual.
That preference is baked in."

---

## B05 — CC0 URL Resolution (ClaudeCodeBeat)

**ON SCREEN:** Code card showing the content-detail endpoint and the JSON path
the script navigates: response → content → descriptiveNonRepeating → online_media
→ media[]. Highlights the CC0 access gate in terracotta.

**NARRATION:**
"Resolving the full-resolution image URL is a two-stage lookup. S3-indexed records
already have the URL stored directly. API-indexed records call the SI content-detail
endpoint. The script navigates the nested JSON — descriptiveNonRepeating, online_media,
media array — looking for type Images and access CC0. First hit wins. Fallback: any
CC0 media. If nothing is CC0, the record is skipped."

---

## B06 — Topaz Upscale: the Optional Gate (SkillTeardownMechanism)

**ON SCREEN:** Cream stage. Heading: "Topaz upscale: optional, graceful." Body
describes the two paths: tpai found → upscale and compare dimensions; tpai missing
→ shelve original, print warning. Verdict pill: "DEGRADES GRACEFULLY".

**NARRATION:**
"Upscaling is optional. The script checks whether tpai — the Topaz Photo AI CLI —
exists at its expected path. Found: it runs the upscale, then compares source and
output dimensions and logs the scale ratio. If the output isn't actually larger,
you see WARN. Not found: the script says so, shelves the original, and moves on.
No silent failure; no hard dependency."

---

## B07 — Provenance Sidecar (ClaudeCodeBeat)

**ON SCREEN:** Code card showing the sidecar file contents:
CC0 / SI_ID / Title / Unit / Credit / Source URL / License. Title: "The sidecar
travels with the image."

**NARRATION:**
"Every shelved image gets a .source.txt sidecar. It records: CC0, the SI object
id, the title, the institutional unit, the credit line, the source URL, and the
Smithsonian Open Access license statement. When you use this image a year from now,
the provenance is sitting in the same folder. The pantry intake reads it. You
don't have to remember anything."

---

## B08 — Pantry Integration: --copy (ClaudeCodeBeat)

**ON SCREEN:** Code card. Title: "From library to reel". Command:
`python3 runtime/scripts/smithsonian_fetch.py --id nmah_12345 --copy ./my-reel --beat B07`
Output shows pantry path and next step prompt.

**NARRATION:**
"Pass --copy with a reel path and --beat B07 to move the shelved image into your
reel's pantry folder. The script converts JPEG to PNG for pantry intake — pantry.py
expects PNGs. After the copy it prints the next step: open the image, inspect the
framing, then run pantry.py. Note: --copy requires --beat; omit the beat id and the
script exits immediately with a clear message."

---

## B09 — Verdict (ClaudeVerdictArtifact)

**ON SCREEN:** Artifact-style verdict card. Lines stagger in. Gets right column
vs bites column.

**NARRATION:**
"What smithsonian_fetch.py gets right: strictly CC0, provenance travels with every
image, index-first design means fast local search without hammering the SI API,
and Topaz upscale degrades gracefully when the tool isn't there. Where it bites:
the index must be pre-built — that's a separate smithsonian_index.py step. And
--yes auto-accepts the top search hit — use it carefully on ambiguous queries,
because the ranker gets hardware right but isn't infallible."

---

## B10 — Handoff: Your Turn (ClaudeComposerAsk)

**ON SCREEN:** Claude composer. Greeting: "Your turn." Prompt types in.
Running indicator.

**NARRATION:**
"Here's your prompt. Paste this into Claude with your reel folder and topic in mind.
Claude reads both scripts — the indexer and the fetcher — then searches for a CC0
image relevant to your topic, fetches and shelves it, and drops it into pantry with
the right beat prefix. The test of success: open the .source.txt next to the
shelved image and confirm it shows CC0, the correct SI object id, and a credit line
that matches the Smithsonian record. If the sidecar is right, the provenance
chain is intact."

---

## B11 — Outro (ClaudeTitleOutroHAI)

**ON SCREEN:** Cream or dark outro card. Title: "Brutalist Utility: smithsonian_fetch.py."
Handle: "@HumanitariansAI". Mascot slug-seeded.

**NARRATION (audio_policy: silence — silent under jingle):**
"Brutalist Utility: smithsonian_fetch.py. Liam, in for Bear."
