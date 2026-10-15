# TEMPLATE-MISSES

A genuine miss is a design card, not a licence to slate. Clear a row by
building the component (then it is in the library forever) or by striking
it if the query was simply badly worded.

## Judged misses (candidates existed but were unusable — logged by hand)

`scene_search.py` returns a hit whenever anything scores ≥2, even if the
candidate is unusable for the new reel (wrong topic, non-parameterized
beyond a sparkLine, wrong token palette, no 9:16 sibling) — it only
auto-logs a TRUE zero-hit. These two rows are genuine misses found by
reading the candidates' actual props/source per GATE L, not by the
zero-hit path, so they're recorded here by hand.

| Date | Query | Reel | Why the top hit didn't work |
|---|---|---|---|
| 2026-08-27 | `RAG retrieval augmented generation flowchart: question, retrieve chunks, context, LLM answer` | what-is-rag | Top hit `CwcMemoryRetrieval` is a different topic (agent memory recall, not document RAG), hardcoded content beyond `sparkLine`, Claude one-terracotta tokens (not the humanitarians palette this reel needs), no 9:16 sibling. Resolved: new parameterized `B02_Flowchart` Manim scene (question → retrieve → context → answer), humanitarians palette, portrait-aware. |
| 2026-08-27 | `embeddings vector space diagram, similar meaning close together, dots clustering` | what-is-rag | No candidate addresses embeddings/vector similarity at all — nearest hits were unrelated (fear-response diagrams, equation reveals). Resolved: new `B03_Embeddings` Manim scene (2D point-cloud, topic clusters, nearest-neighbor highlight), humanitarians palette, portrait-aware. |
| 2026-08-27 | `transformer encoder decoder architecture diagram, input to encoder to decoder to output` | what-are-transformers | No candidate in the Remotion library addresses the transformer encoder/decoder flow at all — nearest hits were unrelated pipeline shapes with hardcoded, non-parameterized content and no 9:16 sibling. Resolved: new `B02_Architecture` Manim scene (input → encoder → representation hand-off → decoder → output, with an autoregressive loop-back arrow), humanitarians palette, portrait-aware. |
| 2026-08-27 | `self-attention mechanism diagram, word looking at other words in a sentence` | what-are-transformers | No candidate addresses self-attention/word-relation visualization — nearest hits were unrelated diagram types. Resolved: new `B00_Title` word-chip + attention-arc motif and `B01_Problem` fading-token-chain Manim scenes, humanitarians palette, portrait-aware. |
| 2026-09-04 | `MCP model context protocol architecture diagram, client server tool call flow` | what-is-mcp | Top hits (`BuildMcpServerPatterns`, `McpBuilderAnatomy`, `McpIntAnatomy`, etc.) are real MCP content but Claude one-terracotta-accent tokens, hardcoded to specific builder-audience skill-teardown detail (Zod schemas, deployment models, tool-naming conventions), no humanitarians-palette/general-audience variant, no 9:16 sibling. Resolved: new `B02_Architecture` Manim scene (host+client → MCP protocol → interchangeable servers → tool/data), humanitarians palette, portrait-aware. |

---

## Auto-logged search misses (scene_search.py)

Written by `scene_search.py` when a search returns nothing. Each row is a
beat that had no component to reach for — the raw material of the next
design card. Clear a row by building the component (then it is in the
library forever) or by striking it if the query was simply badly worded.

| Date | Query | Reel |
|---|---|---|
| 2026-09-10 | `godot` | — |
| 2026-09-13 | `flowdiagram` | — |
| 2026-10-06 | `figma` | — |
| 2026-10-07 | `langchain` | — |
| 2026-10-12 | `claudedesktop` | — |
| 2026-10-13 | `triangle vertices mesh` | — |
| 2026-10-13 | `shader uv vertex fragment` | — |
| 2026-10-13 | `vertex collision displacement` | — |
| 2026-10-13 | `texture sampling` | — |
| 2026-10-13 | `varying interpolation` | — |
| 2026-10-14 | `3d convex concave collider` | — |
| 2026-10-14 | `transform inheritance` | — |
| 2026-10-14 | `velocity or displacement` | — |
| 2026-10-14 | `stomp or hurt` | — |
| 2026-10-14 | `teleport deliberately` | — |
| 2026-10-14 | `choose the backend` | — |
