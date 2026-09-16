# SCRIPT — Brutalist Utility: pantry.py — Short
## run_id: 517c4dadd53d490386ecb25993a16740
## Kept beats: B00, B01, B03, B04, B06, B08, B09, B11
## Dropped: B02 (Pantry Law abstract), B05 (image path detail), B07 (provenance detail), B10 (Your Turn CTA)

---

### B00 — Cold Open (ClaudeComposerAsk916)
**On screen:** Composer with greeting "Bula, Liam"; command types in; output lines stagger.
**Narration:** Hi, this is Liam, in for Bear. pantry.py is the step between your raw media finds and your Remotion slots — it normalizes assets, names them by beat, and flags anything that will cause a rendering problem. Let's look at how it works.

---

### B01 — BLUF: Executive Summary (BrutalistHesitantWriter916)
**On screen:** Writer types lines about pantry intake. Hesitates at "media" → replaces with "pantry". Hesitates at "optional" → replaces with "mandatory". Final corrected text holds.
**Narration:** pantry.py stands between your raw media and the film. Every asset must enter through pantry-slash, renamed with its beat. This episode walks that contract and shows where it fails.

---

### B03 — Mechanism: Beat-Prefix Rule (ClaudeCodeBeat916)
**On screen:** Code card showing BID_RE regex, valid prefix examples (B04_, B12_, B04-916), and SKIP examples.
**Narration:** The prefix is the key. BID_RE — uppercase letters then two digits — must be the first thing in the filename. B04 underscore anything. B12 dash anything. Skip the prefix and the file is silently ignored. The regex is the gate the Pantry Law describes.

---

### B04 — Worked Example: The Pipeline (SkillTeardownMechanism916)
**On screen:** Mechanism card "Three steps. One slot." — detect type → normalize → slot to media/<BID>. Verdict pill "IDEMPOTENT".
**Narration:** The intake runs three steps: detect what type of asset it is — image or video, portrait or landscape; normalize it — crop documents, strip audio from b-roll, convert to RGB; and slot it into media with the beat ID as the filename. That is the whole machine.

---

### B06 — Worked Example: Video Path (ClaudeCodeBeat916)
**On screen:** Code from pantry.py lines 74-109: portrait detection (suffix = "-916"), source-report audio logic, slow-mo duration warning.
**Narration:** For video, two checks run immediately. Is it portrait? Height greater than width means it routes to B04-916.mp4 — the Short override slot. Is it a source report? Then the audio stays. Ordinary b-roll gets the sound stripped. The compiler adds the narration MP3; the b-roll is just picture.

---

### B08 — Edge Case: What Stops It (ClaudeCodeBeat916)
**On screen:** Code showing hard stops (sys.exit on missing pantry/, validate_project) and silent skips (no prefix logged, bad beat ID logged).
**Narration:** Two conditions stop the run outright: a missing pantry directory and an invalid beat sheet. Beyond those, the script is permissive — wrong prefix, unknown beat ID, unrecognized extension all get a logged skip, not an abort. The contract is strict on naming; it is lenient on what you leave in pantry while you work.

---

### B09 — Verdict (ClaudeVerdictArtifact916)
**On screen:** Artifact card "pantry.py - Verdict" / "The naming law works." / Six lines covering idempotency, provenance, two "where it bites" items, invocation, and SKIP guidance.
**Narration:** The verdict: the naming law works. The idempotency is real — rerun it and only hash-changed files get reprocessed. The provenance stubs are the right idea, gating disclosure at intake. Where it bites: no dry-run flag. You learn about skipped files from the console after the fact, not before.

---

### B11 — Outro (ClaudeTitleOutro916)
**On screen:** Title card "Brutalist Utility: pantry.py" with @NikBearBrown handle (OUTRO-LOCK).
**Narration (silent):** Brutalist Utility: pantry.py. Liam, in for Bear.
