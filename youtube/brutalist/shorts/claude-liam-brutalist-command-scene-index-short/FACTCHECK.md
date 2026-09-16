# FACTCHECK — Short (9:16) — Brutalist Command: art scene-index

Every on-screen claim in this Short is retained verbatim from beats in the
parent's vertical companion (`../../claude-liam-brutalist-command-scene-index/vertical/beat_sheet.json`)
whose evidence is documented in the landscape master's FACTCHECK
(`../../claude-liam-brutalist-command-scene-index/FACTCHECK.md`). No new
claims are introduced by cutting. Nothing was regenerated.

## Retained claims

- **620 renderable · 118 undocumented · 0 unresolved.** From the verbatim
  `./art scene-index` run on the isolated toolkit as of the 2026-09-12
  vertical rebuild (parent FACTCHECK). Named in B00, B05 and B09. (Count
  updated from 619 to 620 when ClaudeCodeBeat916 was added to Root.tsx
  in the parent's Sep-12 rebuild.)
- **THE LAW: a scene is renderable only if `Root.tsx` declares a
  `<Composition>` for it.** Verbatim from the top-of-file comment in
  `runtime/scripts/build_scene_index.py`. Displayed in B03 and paraphrased
  in B09.
- **Two files written to disk: `runtime/remotion/src/scenes.json` and
  `SCENE-DOC-TODO.md`.** Verified by the verbatim `ls -l` output in B05.
  Both filenames also appear in the B09 verdict.
- **No aliases — dispatcher case at `art:92-95` matches only the exact
  string `scene-index`.** Named in B09 line 5 (the B02 dispatcher-listing
  detail was cut but the claim is preserved as a one-liner in the verdict).
- **Documented vs derived scenes.json entries.** Named in B09 line 6 (the
  B06 side-by-side detail was cut but the summary line remains).
- **Outro handle `@NikBearBrown`** — hard-coded per `OUTRO-LOCK.md`
  (parent FACTCHECK). Retained via the unchanged B11 native render.

## Beats dropped, and what that removes from the on-screen claim set

- B02 (dispatcher case listing), B04 (three-pass internal walk), B07
  (ledger head sample) and B08 (orphan-scene demo) were the parent's
  fine-grained code cards. The high-level claims those beats justified —
  the LAW, the two-file surface, no aliases, documented vs derived — are
  all still on screen in B03/B05/B09.

## Nothing else changes

B00, B05 and B09 narration MP3s are updated copies from the parent's
Sep-12 vertical rebuild (Kokoro `am_onyx`, Liam in for Bear). B01, B03
and B11 MP3s are byte-identical to the Sep-09 build. No captions, no
subtitle track. No regenerated outro. No pantry overrides.
