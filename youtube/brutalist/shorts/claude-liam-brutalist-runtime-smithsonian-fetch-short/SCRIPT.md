# Script — Brutalist Utility: smithsonian_fetch.py — Short

6 beats retained from the 12-beat vertical companion. Total: 110.25s.

---

**B00 — COLD OPEN (20.5s)**  
*ClaudeComposerAsk916 — command: python3 runtime/scripts/smithsonian_fetch.py "UNIVAC computer console"*

Hi, this is Liam, in for Bear. smithsonian_fetch.py brings CC0 images from the Smithsonian Institution into your Brutalist reel — one at a time, with provenance. It searches a local index, resolves the full-resolution URL through the SI API, downloads, optionally upscales with Topaz Photo AI, and shelves the result. Let me show you what it actually does.

---

**B01 — BLUF (19.0s)**  
*BrutalistHesitantWriter916 — "downloader" → "provenance-pipeline"; "manually" → "automatically"*

The framing that sticks wrong is that this is just a download tool. It's not. It's a provenance pipeline: CC0-only by design, an upscale step through Topaz Photo AI when that tool is present, and a source sidecar — SI object id, credit, license, URL — written automatically next to every image. You don't track attribution; the script does it for you.

---

**B03 — WORKED EXAMPLE: TEXT SEARCH (17.875s)**  
*FormACard916 — tokenized query, candidate list, --yes flag*

Here is a text search. The script tokenizes your query — dropping stop words, short words, and domain noise like smithsonian, collection, national — then scores every record in the local index. Candidates display with their SI unit, object type, and thumbnail URL. You pick a number, or pass --yes to auto-accept the top hit.

---

**B07 — PROVENANCE SIDECAR (19.291s)**  
*FormACard916 — .source.txt fields: CC0, SI_ID, title, unit, credit, license*

Every shelved image gets a .source.txt sidecar. It records: CC0, the SI object id, the title, the institutional unit, the credit line, the source URL, and the Smithsonian Open Access license statement. When you use this image a year from now, the provenance is sitting in the same folder. The pantry intake reads it. You don't have to remember anything.

---

**B09 — VERDICT (25.583s)**  
*ClaudeVerdictArtifact916 — gets right + bites*

What smithsonian_fetch.py gets right: strictly CC0, provenance travels with every image, index-first design means fast local search without hammering the SI API, and Topaz upscale degrades gracefully when the tool isn't there. Where it bites: the index must be pre-built — that's a separate smithsonian_index.py step. And --yes auto-accepts the top search hit — use it carefully on ambiguous queries, because the ranker gets hardware right but isn't infallible.

---

**B11 — OUTRO (8.0s)**  
*ClaudeTitleOutroHAI916 — silent branded outro*

Brutalist Utility: smithsonian_fetch.py. Liam, in for Bear.

---

## Dropped beats

B02 (6-stage pipeline anatomy), B04 (scoring formula internals), B05 (CC0 URL JSON path), B06 (Topaz gate details), B08 (--copy pantry workflow), B10 (Your Turn exercise). Full detail in the 16:9 long.
