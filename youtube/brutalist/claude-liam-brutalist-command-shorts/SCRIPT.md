# SCRIPT — Brutalist Command: art shorts

Twelve beats. Kokoro `am_onyx`. Liam, in for Bear. No captions.
All narration below is what actually stamped into the mp3s (durations in `beat_sheet.json`).

## B00 — ASK (Cold open · ClaudeComposerAsk)
Salam, this is Liam, in for Bear. Art shorts turns a finished sixteen-nine reel into its nine-sixteen sibling. One editorial rule drives everything: the file must be strictly under three minutes, including the endcard, including encoder rounding. The script prints a plan first, then rewires the visuals — it never truncates speech and it never speeds anything up.

## B01 — BLUF (BrutalistHesitantWriter)
Watch the writer walk this back. Art shorts does not shrink your reel by speeding it up. It cuts whole beats out — first the longest unprotected ones — until the remainder plus a four-and-a-half-second endcard fits under three minutes. And when a Remotion beat has a nine-sixteen composition already registered, the script rewires the beat to that composition and re-renders it portrait. It never crops the frame.

## B02 — FRAMEWORK (art:81-86 case)
The dispatcher is two adjacent cases in the art file. Art shorts execs python on shorts dot py. Art vertical execs the same script with dash dash vertical appended. Same code path, opposite editorial rules: shorts caps at three minutes and can drop beats. Vertical caps at nothing and drops nothing.

## B03 — MECHANISM (THE SHORTS LAW)
The law lives at the top of shorts dot py, and it is worth reading. Every Short is strictly under three minutes, endcard and encoder rounding included — a three-minute-zero file fails and never publishes. Shorten by cutting whole beats first. Reuse the retained narration and native portrait visuals as independent copies. Never truncate speech. Never speed anything up. Publishing is a separate step. And dash dash vertical is not a Short — it is the full-length companion, exempt from the cap.

## B04 — MECHANISM (plan_drops greedy algorithm)
Here is how the auto-planner actually chooses. It computes the parent reel's total duration. It subtracts the endcard length. It subtracts a five-second headroom against encoder rounding. That is the budget. Then it walks the beats sorted by duration, longest first, skipping the protected ones — the first beat, the last beat, anything in an INTRO or OUTRO act, any source-report beat, anything marked hero, and everything you named with dash dash keep. It drops from the top of that list until the running total fits.

## B05 — MECHANISM (THE ONDA CHECK)
The reformat rule for Remotion beats is a separate check with its own name — the ONDA check. Captured user media in the reel gets a center cut, biased by shot dot focus, written into short slash media as beat dash nine sixteen. But Remotion renders are detected by shot dot type equals REMOTION on the beat sheet — never by which folder the file sits in. For each Remotion beat, the script looks up the composition's pattern in Root dot tsx, appends nine sixteen, and if that portrait composition exists, rewires the beat and re-renders it. If the nine sixteen composition is missing, the beat is BLOCKED — you either add the composition to Root dot tsx or drop a pantry override.

## B06 — MECHANISM (precedence)
The precedence for every kept beat is fixed. First, pantry — a file named pantry slash beat dash nine sixteen dot mp4 or png always wins, even over a Remotion render. That is the human's manual replacement slot. Second, for Remotion beats, the ONDA check rewire. Third, for captured media, a hand-made beat dash nine sixteen file next to the source. And only if none of the above exist does the script produce an auto center cut. If your auto cut chops a word or misses the subject, you add the file to pantry and re-run — the auto path steps aside.

## B07 — WORKED EXAMPLE (fixture invocation)
Here is a real invocation. Seven beats, two hundred fourteen seconds, thirty-four seconds over cap. The script prints the plan. It picks B02, the longest unprotected middle beat, fifty-five seconds. It rewires the six remaining Remotion beats to their nine sixteen compositions. Total kept: one sixty three point five seconds, comfortably under three minutes. Two commands to run next: portrait render, then compile. This is verbatim from the log — nothing was invented for the video.

## B08 — FALSIFIABILITY (failure + recovery)
And here is a real failure. The command combines dash dash vertical with dash dash drop. Vertical asks for the full film. Drop asks to shorten. The script refuses on the spot — REFUSED, dash dash vertical preserves the full film, dash dash drop is not allowed. No directory written. Exit one. Recovery is pick one intent. If you want a shorter cut with specific beats gone, that is dash dash drop, no dash dash vertical. If you want the full length nine sixteen sibling, that is dash dash vertical, no dash dash drop. Two verbs, two contracts, no overlap.

## B09 — VERDICT (ClaudeVerdictArtifact)
So the surface. Art shorts derives a short cut. It checks the cap first, plans drops greedily from the longest unprotected middle beats, and prints the plan before touching a file. It rewires every Remotion beat to its nine sixteen composition — it never crops the frame. Captured media does get a center cut, biased by focus, but a pantry override always wins. Art vertical is the same script with dash dash vertical — no cap, no drops, no endcard, no rewritten outro. Publishing is separate. Nothing here uploads.

## B10 — YOUR TURN (paste-ready Claude Code prompt)
Your turn. Paste this into Claude Code from your reel folder. Run art shorts and read the plan before compiling. If the auto plan drops a beat you consider essential, add dash dash keep and re-run — the planner will walk to the next longest unprotected beat and drop that instead. If the ONDA check reports BLOCKED, either register the missing nine sixteen composition in Root dot tsx or drop a pantry override. Only after the plan reads as intended do you run the two printed next-steps: remotion scenes on the short folder, then compile with dash dash review.

## B11 — OUTRO (ClaudeTitleOutro)
Brutalist Command: art shorts. Liam, in for Bear, for at Humanitarians A I.
