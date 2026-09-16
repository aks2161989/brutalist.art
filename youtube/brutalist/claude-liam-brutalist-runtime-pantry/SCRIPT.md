# SCRIPT — Brutalist Utility: pantry.py
## run_id: 1df027e6acef4cf1ad6843ed3815ffb7

### B00 — Cold Open (ClaudeComposerAsk)
**On screen:** Composer with greeting "Bula, Liam"; command types in; output lines stagger.
**Narration:** Hi, this is Liam, in for Bear. pantry.py is the step between your raw media finds and your Remotion slots — it normalizes assets, names them by beat, and flags anything that will cause a rendering problem. Let's look at how it works.

---

### B01 — BLUF: Executive Summary (BrutalistHesitantWriter)
**On screen:** Writer types "Drop your b-roll in media — pantry.py slots it. / Any filename works. / Beat IDs are optional." Hesitates at "media" → replaces with "pantry". Hesitates at "optional" → replaces with "mandatory". Final text holds.
**Narration:** pantry.py stands between your raw media and the film. Every asset must enter through pantry-slash, renamed with its beat. This episode walks that contract and shows where it fails.

---

### B02 — Framework: The Pantry Law (SkillTeardownMechanism)
**On screen:** Eyebrow "UTILITY · DESIGN LAW"; heading "Raw finds never go straight to media/."; body text; verbatim quote card from pantry.py docstring; verdict pill "IDEMPOTENT".
**Narration:** The Pantry Law is the first constraint the script states. Raw media goes into pantry-slash first — not straight into media. It gets restored and upscaled before it arrives, but pantry.py handles the mechanical rest: classify, normalize, slot. The contract is idempotent — run it again and it reprocesses whatever is in pantry.

---

### B03 — Mechanism: Beat-Prefix Rule (ClaudeCodeBeat)
**On screen:** Code card showing BID_RE regex, valid prefix examples (B04_, B12_, B04-916), and SKIP examples.
**Narration:** The prefix is the key. BID_RE — uppercase letters then two digits — must be the first thing in the filename. B04 underscore anything. B12 dash anything. Skip the prefix and the file is silently ignored. The regex is the gate the Pantry Law describes.

---

### B04 — Worked Example: The Pipeline (SkillTeardownPipeline)
**On screen:** Pipeline diagram: INPUT (pantry/) → Detect type → Normalize (terracotta accent) → Slot → OUTPUT (media/<BID>). Footer: "Idempotent — reruns reprocess pantry/".
**Narration:** The intake runs three steps: detect what type of asset it is — image or video, portrait or landscape; normalize it — crop documents, strip audio from b-roll, convert to RGB; and slot it into media with the beat ID as the filename. That is the whole machine.

---

### B05 — Worked Example: Image Path (ClaudeCodeBeat)
**On screen:** Code from pantry.py lines 111-127: DOCUMENT crop logic, RGB conversion, width warning.
**Narration:** For images, the script checks the beat's shot type. A DOCUMENT — a scanned page, a poster — gets cropped to 16:9, anchored at the top so the title survives. Everything gets converted to RGB. Anything under 1920 pixels wide gets a warning — Ken Burns zoom will soften the edges.

---

### B06 — Worked Example: Video Path (ClaudeCodeBeat)
**On screen:** Code from pantry.py lines 74-109: portrait detection (suffix = "-916"), source-report audio logic, slow-mo duration warning.
**Narration:** For video, two checks run immediately. Is it portrait? Height greater than width means it routes to B04-916.mp4 — the Short override slot. Is it a source report? Then the audio stays. Ordinary b-roll gets the sound stripped. The compiler adds the narration MP3; the b-roll is just picture.

---

### B07 — Mechanism: Provenance Stubs (SkillTeardownMechanism)
**On screen:** Eyebrow "UTILITY · PROVENANCE"; heading "Every asset gets a sidecar."; body; verbatim quote about AI disclosure; spark line "Fill the sidecar. Ship the receipt."
**Narration:** After each asset lands in media, pantry.py writes a .source.txt sidecar. If the file looks AI-generated — Higgsfield filename patterns trigger the detection — it prefills a disclosure template. Everything else gets placeholder fields: URL, license, credit. The human fills them in. The sidecar is what makes the reel auditable.

---

### B08 — Edge Case: What Stops It (ClaudeCodeBeat)
**On screen:** Code showing hard stops (sys.exit on missing pantry/, validate_project) and silent skips (no prefix logged, bad beat ID logged).
**Narration:** Two conditions stop the run outright: a missing pantry directory and an invalid beat sheet. Beyond those, the script is permissive — wrong prefix, unknown beat ID, unrecognized extension all get a logged skip, not an abort. The contract is strict on naming; it is lenient on what you leave in pantry while you work.

---

### B09 — Verdict (ClaudeVerdictArtifact)
**On screen:** Artifact card "pantry.py · Verdict" / "The naming law works." / Four lines: idempotency, provenance, and two "where it bites" items.
**Narration:** The verdict: the naming law works. The idempotency is real — rerun it and only hash-changed files get reprocessed. The provenance stubs are the right idea, gating disclosure at intake. Where it bites: no dry-run flag. You learn about skipped files from the console after the fact, not before.

---

### B10 — Your Turn (ClaudeComposerAsk)
**On screen:** Greeting "Your turn." above composer; audit prompt types in; output lines: renamed list, warnings flagged.
**Narration:** This prompt hands the intake audit to Claude. Paste it into your project — Claude reads your sheet, walks through every file in pantry-slash, and tells you which ones would be silently skipped and why. Then it gives you the corrected filenames. Run it before your first pantry.py invocation and you will not see a column of SKIP warnings after the fact.

---

### B11 — Outro (ClaudeTitleOutro)
**On screen:** Title card "Brutalist Utility: pantry.py" with slug-seeded mascot and @NikBearBrown handle (per OUTRO-LOCK.md).
**Narration:** Brutalist Utility: pantry.py. Liam, in for Bear.
