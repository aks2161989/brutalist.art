# SCRIPT.md — Brutalist Command: art vertical

Persona: **Liam, in for Bear** · Voice: Kokoro `am_onyx` (free/local) ·
Register: Teardown · Channel: `@HumanitariansAI` · Playlist: Brutalist.

The narration below is the master clock. All timings are measurements taken
from the rendered Kokoro MP3s, not authored targets.

## B00 — ASK (cold open)

> Hola, this is Liam, in for Bear. Art vertical takes a finished sixteen-nine
> reel and produces its full-length nine-sixteen twin. No cropping. No cut
> beats. No shortened outro. Same script that powers art shorts, opposite
> editorial contract: shorts caps at three minutes and drops beats to fit;
> vertical preserves every beat and every second.

## B01 — BLUF (hesitant writer, ≥9 s window with 0.8 s lead silence)

> Watch the writer walk this back. Art vertical is not a Short. It does not
> shorten anything, and it never crops the frame. What it does do — every
> time — is rewire each Remotion beat to its nine-sixteen composition, so
> the portrait render is a native layout, not a chopped landscape. That is
> the whole difference from a bad screen-crop.

Hesitant text: `vertical shrinks.\nand crops it.` → `vertical preserves.\nand rewires it.`
(the correction changes both nouns — the reel's actual misconception.)

## B02 — FRAMEWORK (dispatcher, two adjacent cases)

> The dispatcher lives in a single bash file. Art vertical is one case. Art
> shorts is the case above it. Both exec the same python script — shorts dot
> py — but vertical appends dash dash vertical to the argument list. Same
> code path, opposite editorial contract, chosen by which verb you typed.

## B03 — MECHANISM (THE VERTICAL CONTRACT)

> The contract for vertical is rule five of the module's own docstring, and
> it is worth reading verbatim. Dash dash vertical creates a full-length
> companion, not a Short. No drops. No duration cap. No rewritten outro. No
> added endcard. Every beat that landscape had, vertical has. Same running
> time. Same words. Just a portrait layout for every generated visual.

## B04 — MECHANISM (the guardrails inside main)

> The guardrails are three lines of python. If vertical is on and dash dash
> drop was passed, the script refuses on the spot. If vertical is on, the
> endcard is forced off and the outro-rewrite is forced off — both flags
> auto-set to true. There is no way to sneak a drop, an endcard, or a
> reworded outro into a vertical build. The refusal is by construction.

## B05 — MECHANISM (ONDA CHECK still fires)

> Then the ONDA check runs, exactly the way it runs for shorts. Every
> Remotion beat is detected by its beat sheet — shot dot type equals
> Remotion. The script appends nine sixteen to each beat's composition
> pattern, looks it up in Root dot tsx, and rewires the beat when a portrait
> composition exists. If it does not, the beat is BLOCKED — you register the
> nine sixteen composition or drop a pantry override. Vertical does not
> soften this check. It is the same check.

## B06 — MECHANISM (the cap check is skipped)

> The one thing vertical skips is the cap check. Right at the end of main,
> the script asks — was this a vertical build? If yes, require underscore
> short underscore duration is not called. That is the entire delta on the
> duration side. Every other check — validate project, atomic write, invalidate
> stale renders — runs the same. Vertical is not a lenient shorts. It is a
> different contract with one guardrail flipped and one measurement removed.

## B07 — WORKED_EXAMPLE (verbatim invocation)

> Here is a real run against the fixture reel. Seven beats. Two hundred
> fourteen seconds. Three minutes thirty-four. The script prints the parent
> reel's total, prints the vertical banner, walks the seven Remotion beats
> through the ONDA check — every one of them has a nine sixteen composition
> already registered — and reports seven beats at two hundred fourteen
> seconds, full-length vertical, no Short cap. The dropped column reads
> none. The endcard line reads ends on the last beat. That is exactly the
> shape vertical promises.

## B08 — FALSIFIABILITY (the vertical-plus-drop refusal)

> And here is the refusal that makes the contract real. Art vertical on the
> fixture, dash dash drop B zero two. The script prints one line to stderr —
> REFUSED, dash dash vertical preserves the full film, dash dash drop is not
> allowed. Exit one. No directory written. Recovery is to pick one intent.
> Shorts if you want a cut, vertical if you want the twin. The same refusal
> fires from the shorts dispatch too — because both spellings hit the same
> guardrail in the same python source.

## B09 — VERDICT (the whole surface)

> So the surface. Art vertical wraps art shorts with dash dash vertical.
> Same script. Same ONDA check. Full length. No cap. No drops. No endcard.
> No rewritten outro. Every Remotion beat rewires to its portrait sibling
> and re-renders. Captured media in a native portrait reel is reused
> untouched. The two commands the script prints — remotion scenes, then
> compile — are what actually build the vertical mp4. Publishing is
> separate. Nothing here uploads.

## B10 — YOUR TURN (composer, prompt read aloud)

> Your turn. Paste this into Claude Code from a finished sixteen-nine reel
> of yours. Run art vertical, read the plan, then run the two printed
> next-steps. If ONDA check reports BLOCKED for any Remotion beat, either
> register the nine sixteen composition in Root dot tsx or drop a pantry
> override. This prompt is the discipline: read the plan, resolve BLOCKED,
> render portrait, compile at four K. Look for a full-length vertical mp4
> that plays end to end with no cropped text.

## B11 — OUTRO (title restate + sign-off)

> Brutalist Command: art vertical. Liam, in for Bear, for at Humanitarians A I.
