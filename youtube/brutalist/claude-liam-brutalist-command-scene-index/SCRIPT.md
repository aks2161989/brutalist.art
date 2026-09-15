# SCRIPT — Brutalist Command: art scene-index

Voice: Kokoro `am_onyx` (Liam, in for Bear). Register: Teardown.
All beats narrated locally; no captions.

Total narrated length: **268.0 s** (measured MP3 durations).
Master duration after conform: **268.5 s**.

---

## B00 · ASK · 15.85 s · `ClaudeComposerAsk`

> Bonjour, this is Liam, in for Bear. Six hundred and nineteen
> renderable compositions live in Brutalist. Art scenes searches that
> index. Art scene-index writes it. When you add a component to Root
> dot tsx, the search cannot see it until you re-index. This is the
> tool that closes that loop.

## B01 · BLUF · 13.80 s · `BrutalistHesitantWriter`

> Watch the writer walk this back. Art scene-index does not read the
> scenes for you. It reads Root dot tsx and rewrites the index that
> art scenes searches. Search reads the index. Scene-index writes it.
> That is the whole distinction this reel turns on.

`lead_silence_s: 0.8`. Correction: `reads → rewrites`, `scenes → index`.

## B02 · FRAMEWORK · 20.03 s · `ClaudeCodeBeat`

> The dispatcher is one case in the art file. The pattern matches only
> the exact string scene-index — there are no aliases. It execs the
> python builder against runtime slash remotion slash src, with the
> todo flag baked in so SCENE-DOC-TODO markdown is always regenerated
> alongside scenes dot json. Every argument you add lands after the
> flag.

## B03 · MECHANISM · 21.74 s · `ClaudeCodeBeat`

> Here is the law the tool exists to enforce. A scene is usable only
> if Root dot tsx declares a Composition for it. A dot tsx file
> sitting in scenes slash is not enough — several exist that no
> Composition references, and they are invisible to the pipeline. So
> the index is generated from Root dot tsx for that exact reason.
> Registered is the only truth. Everything else in the folder is a
> draft.

## B04 · MECHANISM · 29.78 s · `ClaudeCodeBeat`

> Three passes over Root dot tsx. Pass one builds the import map —
> local name to module path and exported name — so a Composition tag
> can be resolved to its backing file. Pass two walks the file
> linearly, tracking banner comments, folder open and close tags, and
> every Composition span. Pass three opens each backing file and reads
> the component's own header comment. If there is no header, the
> entry is derived — from the id, the folder, the props, and the
> strings the component ships with — and the tool marks it derived so
> search knows to trust it less.

## B05 · WORKED_EXAMPLE · 22.04 s · `ClaudeCodeBeat`

> So the bare invocation. Dot slash art scene-index. It runs, it
> prints two lines and exits zero. Six hundred and nineteen
> renderable compositions. One hundred and eighteen of them are
> running on derived search text. Zero unresolved — every registered
> id has a backing file on disk. Two files change on disk: scenes dot
> json under runtime slash remotion slash src, and SCENE-DOC-TODO
> markdown at the repo root.

## B06 · WORKED_EXAMPLE · 29.40 s · `ClaudeCodeBeat`

> Two records from the same file. On the left, a documented entry —
> ClaudeComposerAsk. Its desc is the opening of its own header, its
> props are read from its zod schema, its synonyms are mined from the
> header body. Documented is true. On the right, a derived entry —
> CodexComposerAsk. No header in the component, so the desc is
> assembled from evidence: the id, the folder it was registered
> under, keywords, on-screen strings, and the props. Documented is
> false. The two are equal citizens for search — but the derived one
> is worth reading the file before you trust it.

## B07 · WORKED_EXAMPLE · 22.21 s · `ClaudeCodeBeat`

> The second file the tool writes is SCENE-DOC-TODO markdown. That is
> the backfill ledger — every scene running on derived text, one row
> apiece, with the file path and the folder it lives under. One
> hundred and eighteen rows, nineteen percent of the six hundred and
> nineteen. Each row is a small chore: open the file, add one honest
> sentence at the top, re-run scene-index. The pile shrinks by one,
> the search text sharpens by one component.

## B08 · FALSIFIABILITY · 28.71 s · `ClaudeCodeBeat`

> And here is the law in flight. A scratch toolkit with two files in
> scenes slash: ClaudeComposerAsk and OrphanNewScene. Only one
> Composition tag in Root dot tsx. Scene-index runs, reports one
> renderable, and puts only the registered id in scenes dot json. The
> orphan is invisible. Now add the missing Composition to Root dot
> tsx and re-run. Count jumps to two. Both ids present. The tool did
> not silently accept the disk file — it accepted the registered
> Composition. Recovery is one edit and one re-run.

## B09 · VERDICT · 26.65 s · `ClaudeVerdictArtifact`

> So the surface. Bare art scene-index re-reads Root dot tsx and
> writes two files. Scenes dot json — the six hundred and nineteen
> entry index that art scenes searches. SCENE-DOC-TODO markdown — the
> one hundred and eighteen entry backfill list from the todo flag
> baked into the wrapper. There are no aliases; the dispatcher
> matches only scene-index. And the law under all of it: a scene is
> renderable only if Root dot tsx declares a Composition for it. A
> file on disk is a draft. Root dot tsx is the truth.

## B10 · YOUR_TURN · 32.45 s · `ClaudeComposerAsk`

> Your turn. Paste this into Claude Code from the brutalist toolkit
> root. It exercises the full loop: run scene-index once as a
> baseline, count what you have, add a fresh Composition to Root dot
> tsx for a component you are about to author, re-run, and confirm
> the count went up by exactly one. Then open SCENE-DOC-TODO
> markdown, pick one row, add a one-sentence header to that file,
> re-run, and confirm the undocumented number went down by one. If
> either move surprises you — the count did not change, a name went
> missing — that is a lead: either Root dot tsx did not save, or the
> import path does not match.

## B11 · OUTRO · 5.59 s · `ClaudeTitleOutro`

> Brutalist Command: art scene-index. Liam, in for Bear, for at
> Humanitarians A I.
