# SCRIPT.md — The your-turn Skill (ep 21)

Narrator: **Liam, in for Bear**. Voice: Kokoro `am_onyx`. No captions.

## B00 · ASK · 17.2s

Hallo, this is Liam, in for Bear. There is a skill called your-turn that most fellows will look at and think it is a whole workflow. It is not. It is a closing-block skill that standardizes the last three beats of every claude-explainer reel, then hands off. So I asked Claude to read the SKILL dot m-d and tell me what it actually rewrites.

## B01 · BLUF · 10.2s  *(0.8s lead pause)*

Watch the writer walk this back. Your-turn is not a whole-reel skill. It is a closing-block skill — the last three Liam beats at the end of every claude-explainer reel, standardized.

## B02 · FRAMEWORK · Anatomy · 15.7s

Every skill on this toolkit is a folder Claude reads before working. Your-turn is one SKILL dot m-d plus one Python script — apply underscore your underscore turn dot p-y. The doctrine lives in the SKILL file. The script is the deterministic transformer that applies it.

## B03 · FRAMEWORK · Block · 18.9s

Here is the block, in fixed order. Beat one — VERDICT, on the artifact card, opens with the handoff line then the full recap. Beat two — YOUR TURN, on the composer, shows a prompt relevant to this specific video and Liam reads the whole thing aloud. Beat three — the title outro, poster serif, Liam re-reads the reel's own title. Three beats, one voice, always closing.

## B04 · MECHANISM 1 · Handoff · 18.8s

First decision. The handoff line changes based on who narrated the body. If the previous beat was Bear, the recap opens with — Thanks Bear, let's recap with Claude. If the previous beat was already Liam, it just opens — Let's recap with Claude. There is a half-second lead pause so the handoff breathes. The script reads the prior beat's engine to decide which line to write.

## B05 · MECHANISM 2 · Drafts gate · 20.0s

Second decision, and this is the one non-deterministic step. The YOUR TURN prompt must be relevant to the specific reel — so it is drafted per slug into a drafts dot j-son file. One entry per slug — a prompt, and optionally a recap for reels that don't have a verdict card yet. The human reviews drafts dot j-son BEFORE any audio spend or render. This is the one phase gate.

## B06 · MECHANISM 3 · Verdict fixes · 25.7s

Third decision, and it fixes two defects in one edit. The verdict card was hard-pinned to eight hundred sixty pixels on a nineteen twenty frame — small, floating, indefensible. It now fills eighty-four percent of the width with legible type. One component edit — every reel bigger on re-render. And the double-numbered recap lines — where authors typed one dot, two dot, and the card also numbered them — those are stripped from artifactLines both when writing and defensively at render.

## B07 · MECHANISM 4 · Your Turn contract · 18.7s

Fourth decision, and it is what makes YOUR TURN feel like a real handoff. Liam reads the prompt out loud — the full thing. The narration text and the composer's command field are the same string. Greeting slot reads — Your turn. Full stop. The composer types the prompt while Liam speaks it. No 'here is your prompt' filler. No paraphrase. The prompt IS the narration.

## B08 · MECHANISM 5 · Outro contract · 20.2s

Fifth decision. The outro beat re-reads the title. Not a channel plug, not a subline. The narration text field on the outro is literally the reel's title, spoken in Liam's voice with the terracotta period landing under the poster serif. The transformer copies metadata dot title into both the narration and props dot title. Re-run the skill tomorrow — same output. Idempotent.

## B09 · WORKED EXAMPLE · Dry-run demo · 20.1s

Now watch it run — on a synthetic fixture in this reel's demo folder. Dry-run only, no real reel is touched. The script scans the sheet, finds the closing YOUR TURN and OUTRO, cleans the verdict, rewrites the three beats, and writes a report. Changed, skipped, needs prompt, errors. Look at the report — one fixture changed, zero errors, and the notes name every edit the transformer made.

## B10 · FALSIFIABILITY · Documented limitation · 20.4s

Now what your-turn does NOT do. It never touches the body. It never publishes. Applying the block and even re-rendering the reel is safe — going public is a separate manual step in YouTube Studio. And the re-render itself is human-triggered per reel, because re-uploading replaces the video file via a NEW ID and the old URL and its views are lost. That is why the SKILL says — batch deliberately.

## B11 · VERDICT · 17.4s

So the split. Bookends up to the body — INHERITED from ai-explainer. The closing three beats — OWNED. The handoff line is persona-aware. Drafts dot j-son is the human gate before any spend. The verdict card is fixed once, every reel bigger. And reach elsewhere if the sheet has no your-turn or Liam outro — this skill skips it.

## B12 · YOUR TURN · 22.6s

Your turn. Paste this into Claude Code. Read the your-turn SKILL and its apply script. Then pick one of your own reels — or a synthetic beat sheet fixture — and ask Claude to draft a drafts dot j-son entry for it. First surface the reel's own material — the source chapter, the body beats' narration text — and draft one prompt a curious viewer would paste after watching. Then dry-run apply your turn against that draft and read the report before touching a real reel.

## B13 · OUTRO · 4.8s

The your dash turn Skill. Liam, in for Bear, for at Humanitarians A I.
