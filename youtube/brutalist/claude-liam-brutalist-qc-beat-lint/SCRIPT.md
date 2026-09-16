# Script — Brutalist Utility: beat_lint.py
Persona: Liam, in for Bear | Voice: Kokoro am_onyx | Playlist: Brutalist / @HumanitariansAI

---

## B00 — ClaudeComposerAsk (cold open)

Annyeong. I'm Liam, in for Bear. Your beat sheet is a JSON file — the blueprint for every scene, every narration line, and every rendering lane in your Brutalist reel. Before audio is cut and before Remotion touches a frame, beat_lint.py reads that file and enforces two hardening rules. Exit zero means clean. Exit two means there are defects — and the build does not continue.

---

## B01 — BrutalistHesitantWriter (BLUF)

*Written text:* "beat_lint.py checks your beat sheet before the render starts, catching placeholder beats that could slip past unnoticed."

*Corrected text:* "beat_lint.py checks your beat sheet before the render starts, catching text-card beats wearing illustration clothes."

Narration: Here's what beat_lint actually does, and it matters to get this right. The tool is not a general placeholder hunter. It targets one specific failure: a Remotion content beat whose rendering pattern is a generic text card — a SlateCard, a TextCard, a TitleCard — when it should be a real illustration. That is an explainer wearing a slideshow's bones. The second thing it catches is an illegal placeholder type. Everything else in your sheet is your responsibility.

---

## B02 — BeatLintPipeline (framework diagram)

Narration: Beat_lint is a plan-time check, not a render-time check. That distinction is the point. Run it before you generate audio, before you touch Remotion. It reads your beat_sheet.json, loops through every beat, and applies three rules. A beat that passes all three is clean. A beat that trips any one gets reported with its beat ID, the rule it broke, and a fix instruction. The whole sheet exits two — blocks the build — if any defect exists.

---

## B03 — ClaudeCodeBeat (exempt classes — the rules in code)

Narration: The exemption list is as important as the rule. Bookend beats, ask beats, card beats, and Manim graphics are all exempt — they're either structural or already proved themselves as real rendered graphics. The rule only fires on lane-colon-remotion beats — current-generation sheets that explicitly declare their lane. Older sheets that predate the lane field are not re-litigated. The amnesty is deliberate: it prevents retroactive failures on reels you shipped before this rule existed.

---

## B04 — ClaudeCodeBeat (RULE 3 — the defect condition)

Narration: Rule three fires when lane is remotion AND the pattern is in the text-card set: SlateCard, TextCard, TitleCard, CardText, or QuoteCard. The message is precise: it names the beat ID, calls it a talking slide, and gives you two exits. Give the beat a real illustration pattern — a ShellSession, a BarChart, a custom Remotion scene — or convert it to a vox-anim placeholder, which is the legal way to hold a slot for pantry media. Both fixes pass the lint.

---

## B05 — FormBCard (RULE 4 — two legal placeholder types)

Narration: Rule four defines the only two legal placeholder types. A STILL placeholder: lane vox, type STILL or COMPOSITE — you're reserving a slot for a photograph or a generated clip you'll drop into the pantry. A VOX-ANIM placeholder: lane vox, placeholder vox-anim — pantry media that Remotion will animate vox-style. A SlateCard is legal ONLY in these two cases, or as an act card or a bookend. Everywhere else it is a defect.

---

## B06 — ShellSession (clean run demo)

Narration: Run it from the toolkit root. Point it at a reel directory or directly at a beat_sheet.json file. A clean sheet prints one line: beat-lint, clean, beat mix OK, and the filename. Exit zero. The build continues. That is all you want to see.

---

## B07 — ShellSession (defect run demo)

Narration: A defective sheet prints the count, then one line per defect: beat ID, rule name in brackets, and the full message. The message tells you exactly which pattern tripped the rule and gives you the fix. Exit two. The build stops here. Nothing renders until you fix the beat sheet. This is the whole value of running it early: a five-second check before you spend any time on audio or scenes.

---

## B08 — ClaudeVerdictArtifact (verdict — what it doesn't catch)

Narration: Here's the design tell. Beat_lint has a deliberate scope: it enforces the minimum structural contract, not the quality of your illustrations. It doesn't check whether your ShellSession actually shows something meaningful, whether your BarChart data is correct, or whether any vox-anim placeholder ever gets filled. It also doesn't know about patterns not in its text-card set — a custom scene with a nonsensical name passes clean. The linter is an author-time sanity check, not a substitute for visual review.

---

## B09 — FormBCard (RULE 7 — branding contract via brand_labels.json)

Narration: There's a third rule that runs before the beat loop: Rule seven checks branding. A JSON file next to the script — brand_labels.json — maps channel identifiers to a fixed series kicker and a folder chip. If your beat sheet's brand field matches a channel in that file, and your topic or folderLabel doesn't match what's registered, you get a branding defect. Unknown channels pass silently. Edit brand_labels.json to add or change channels — no code change required.

---

## B10 — ClaudeComposerAsk (Your Turn)

Your turn. Open the beat sheet for your current reel and paste this prompt into Claude Code:

"Run python3 runtime/qc/beat_lint.py on my reel directory. Report every defect with its beat ID and the fix. If any beat trips rule three, show me what a corrected lane:remotion beat with a real illustration pattern looks like for that beat's content. If any beat trips rule four, show me the exact vox-anim placeholder syntax. Exit the session only after beat_lint exits zero."

Narration: Take this prompt. Point it at your own reel. What you're looking for: beat_lint exits zero and every lane-colon-remotion beat in your sheet has a real illustration scene registered against it. If it exits two, the message tells you exactly what to change. That five-second check at the start of your session saves you from discovering the problem at compile time.

---

## B11 — ClaudeTitleOutroHAI (outro)

*Title:* Brutalist Utility: beat_lint.py
*Handle:* @HumanitariansAI
*Narration (in outro):* Liam, in for Bear.
