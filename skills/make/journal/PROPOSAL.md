# journal — a proposed skill: one film per substantive change to a project

**What this is.** A structure for a new brutalist.art skill, `journal`, proposed 2026-10-07 at Bear's request and revised the same day on his correction. The original ask: "a new skill called journal … make a film every day of that update to that project … it should read like a journal, like a running session." The correction: "we don't necessarily have to be bound by day. We need to have a log per event. If something was done which is a real change, there's a description of one thing. If a day had three substantive changes, it would get three films. The journal entries are not by date, they're by date-time. And they're about a substantive change, not a trivial change: some improvement, the results of that improvement, and then the next steps." Nothing is built; this is the design to confirm. **Why.** The series *Professor Bear Does His Assignments* needs a repeatable, cheap, honest small form between the big films, one per real change. **Found.** Nearly every part exists in the toolkit. Two small Remotion scenes and one collector script are new; everything else is reused from show-tell, lecture, cc-explainer and tldr.

---

## The one idea

**One film = one substantive change, timestamped.** An entry is not a day; it is an event: a real change to the project, logged in the project's FRICTIONAL.md with a date, and given a time by the commit or the log line that recorded it. Each film says three things about that one change: what was changed and why, what the result was, and what comes next. Three real changes in a day are three films, morning, afternoon, night. A trivial change (wording, formatting, a re-run with the same result) is not an entry, by the same rule the FRICTIONAL logs already use for "substantive".

**The log is the script.** The film is built from that entry's own text, the commit that carried it, the files it touched, and the counters the change moved. The builder reads what was written; it never narrates from memory.

## The through-line in every entry (Bear, 2026-10-07: "conducting AI, Frictional, irreducibly human, written through it")

Three of his course ideas run through every film, not as a slogan at the end but as the shape of the beats:

| Idea | Where it lives in the spine | How it shows |
|---|---|---|
| **Frictional** (the dated process log) | the whole film | Every beat is a field of the FRICTIONAL entry read aloud and shown: tried/expected, happened, did, who contributed, understand/don't, evidence and next step. The entry's heading is written on screen; the film never says more than the log recorded. |
| **Conducting AI** (the person directs and supervises) | THE CHANGE and THE RESULT | When the entry records a supervisory act, the beat names which of the five capacities it was: plausibility auditing, problem formulation, tool orchestration, interpretive judgment, executive integration. Named only when the log shows the act; never pinned on for completeness. |
| **Irreducibly human** (what stayed with the person) | BLEDGER | The human column is the irreducibly-human ledger for this entry: the decision, the understanding, the relationship, the permission that stayed with Bear. Assigned by task, never as a claim that people are better. Where Claude Code did something on his behalf, the AI column says so and the human column says "not yet reviewed" when that is true. |

The rule across all three: name who did what, in the log's words, and let the viewer see the split.

## Unit, cadence, numbering

| Rule | What it means |
|---|---|
| Unit | One substantive change. Source: one FRICTIONAL entry (or one dated bullet under a day's entry, where the log extended the day), plus its commit. |
| Timestamp | Date **and hour**, taken from the commit that carried the change; if the change was never committed, from the log's own time note; failing both, the date alone and the film says "time not recorded". **Format (Bear, 2026-10-07): day, month, year, then the hour on a 24-hour clock, no minutes.** On screen `7 October 2026 · 14:00`; spoken "the seventh of October, twenty twenty-six, fourteen hundred"; in folder names the sortable form `2026-10-07T14`. Minutes are dropped on purpose: no film is made every minute. Two entries in the same hour keep the same stamp and differ by entry number. |
| Numbering | Entry N, counted from the project's first substantive entry, in timestamp order. Never typed; computed by the collector. |
| Several in a day | Each gets its own film. The slate shows the time, and the running strip shows which entry of the day it is ("2nd change today"). |
| None in a day | Nothing is built, nothing is said. The next entry's "since last entry" strip shows the elapsed time ("3 days since entry 13"). |
| Trivial change | Not an entry. If it was committed, it appears only as a line in the next entry's strip ("2 small commits since"). |
| Length | No cap, no target (show-tell's Law 9). One change, told completely: typically 60 to 180 seconds. |

## The spine

```
BOPEN    portrait/title       lecture-title-slide-16x9      narrated: series name, entry title, one or two sentences on what this entry covers
BSLATE   the stamp            JournalSlate (new)            Entry N · date · time · project · "since last entry" strip
BHOOK    where it stood       BrutalistHesitantWriter       the state before this change, one phrase corrected into the change
  THE CHANGE                  one block: what was changed, and why
  THE RESULT                  one block: what it produced, measured, shown as the thing
BLEDGER  who did what         JournalLedger (new)           two columns, THE AI DID / THE HUMAN DID, plus the doubt line, from this entry
BNEXT    next steps           ClaudeVerdictArtifact         the entry's own "next step" lines, verbatim
BOUT     outro                ClaudeTitleOutro (OUTRO-LOCK) "<series title>, Entry N. At Nik Bear Brown."
```

No key-terms card: a term new to the project in this entry is defined on screen where it first appears (lecture's rule for a seventh term). No recap: the who-did-what card is the recap. No Your Turn by default; on only when the change is a move the viewer could make on their own project, and the log's own words are the prompt.

### BOPEN, the narrated opening (Bear, 2026-10-07: the journal follows the lecture skill's intro)
Every entry opens exactly as a lecture does. Use the lecture skill's approved first-beat template (`../lecture/templates/title-slide-16x9/`, read its README for the build contract): a seeded Professor Bear portrait on the left; the **entry's title** (for example "Entry 14: The First Real Sync") on the right; the series title and entry position across the top; "Liam, in for Bear · Narration". The first thing the viewer hears, in Liam's voice, is: **the series name, then the exact entry title, then a very short statement of what this entry covers** (one or two sentences, never more than a short paragraph). Example: "Professor Bear Does His Assignments. Entry fourteen: the first real sync. Three copies of the job-search tool were brought back into step, and one file the sync had missed was found." The card holds for the measured narration, then cuts to BSLATE. The narration is written from the entry's own heading and "What happened" line, never from memory, and is stored in `narration_text` with `shot.narration_contract: "playlist-title-summary-v1"`.

Two consequences. BSLATE no longer introduces the entry, so it keeps only the date, the hour and the since-last-entry strip. And the card's "Video NN / TT" field needs a total, which an open-ended journal does not have; see the open question below.

### BSLATE, the stamp (new scene `JournalSlate`)
A cream Claude stage. Top left, the project name in serif. Centre, the date in large serif (`7 October 2026`), the hour beneath it (`14:00`), and "Entry N" beneath that. Along the bottom, the **since-last-entry strip**: elapsed time since entry N−1, and the project's three to five standing counters with their change since that entry, read from files by the collector (for the job-search project: boards read, postings, kept, runs, films published). Unchanged counters in grey; changed ones in terracotta with the delta. Liam's greeting over it: "Hola. This is Liam, in for Bear. Entry fourteen. The seventh of October, twenty twenty-six, fourteen hundred."

### BHOOK, where it stood (`BrutalistHesitantWriter`, reused)
The writer types the state before the change, as the previous entry's "next step" or this entry's "I tried / expected" put it, and corrects one phrase into what this change did. Example: "the sync script reports all three in sync" → the trigger "all three in sync" becomes "in sync on the files it was told to check". The tldr/lecture hesitant-writer contract unchanged; only the source of the text is new: the log.

### THE CHANGE (one block, from "I tried / expected" and "What happened")
What was changed, in the entry's words, and why it was needed. Visual by the lecture's SHOW-THE-THING LAW first: the real diff (`CCDiff` / `GitHubCodeDiff` cut from the commit), the real page (`BrowserCapture`), the real session (`CCSession`), the real file. Where the change is an idea rather than an artifact, one drawn isometric image on the project's standing cast, advanced from where the last entry left it. A `ShowTellCard` only where it passes the card test. The entry's heading is written on screen by `QuillWriter` as the block's label.

### THE RESULT (one block, from "What happened" and "Evidence")
What the change produced, measured, with the check shown: counts read from files (`ExecutedData` or `LectureEvidenceTable` with the source note), the gate output, the test run, the contact sheet, the before-and-after of a number. If the result was a failure, the failure is the result and stays on screen. If the result cannot be measured yet, the film says "not yet measured" and BNEXT carries the measurement.

### BLEDGER, who did what (new scene `JournalLedger`, a variant of `CCHumanLedger`)
The closing summary Bear asked for (2026-10-07): "something at the end summarizing what the AI did and what the human did." Two columns on one card, filled from this entry's own "What Claude or another person contributed" field and nothing else:

| THE AI DID | THE HUMAN DID |
|---|---|
| the specific work it produced: fetched, drafted, ran, compared, typed | the specific calls a person made: set the target, chose, rejected, approved, reviewed, or has not yet reviewed |

The AI column lands first and the human column second and holds; that order is the argument, as in the cc-explainer's ledger. The human column carries the terracotta rule. Beneath the columns, one line: **Doubt caught:** what looked right and was not, or the check that confirmed it; "nothing caught in this entry" when that is the truth, said aloud. Every row cites the entry it came from in small type. Rows name work, never capability: the card never says what AI cannot do, only what it did not do here and who did it instead.

### BNEXT, next steps (`ClaudeVerdictArtifact`, reused)
The entry's own "Evidence and next step" lines, verbatim, as the artifact's numbered lines. Nothing new is asserted. Liam reads them as the entry's last words; they become the next entry's BHOOK.

### BOUT (`ClaudeTitleOutro`, OUTRO-LOCK)
Title "<series title>, Entry N" with the entry's heading as the film's own title in the description, hardcoded @NikBearBrown, slug-seeded mascot, no subline.

## Laws (this skill's own; the parents' laws all still bind)

1. **ONE-CHANGE LAW.** One film, one substantive change. Two changes in one entry are two films; the collector splits on the log's own bullets and commits, and the builder never merges.
2. **RECORD LAW.** Every beat traces to the entry, its commit, a publish-log line, or a file the collector read. If it is not in the record, it is not in the film.
3. **TIMESTAMP LAW.** Date and hour are said and shown, in the one format (day month year · HH:00, 24-hour clock); a number carries the hour it was read.
4. **RESULT LAW.** Every film shows the result of its change with the check that measured it, or says "not yet measured". No change is shown as done without its effect.
5. **SAME-CAST LAW.** One standing drawn cast per project, declared in `JOURNAL.md`. Every drawn beat uses it, so entry 14 looks like entry 13 with one thing moved. New objects join the cast when the project gains them.
6. **DELTA LAW.** Counters are change since the last entry, read by script, never typed.
7. **WHO-DID-WHAT LAW.** Claude Code's work and Bear's decisions are labelled apart in every film; "typed on his behalf, not yet reviewed" is said when the log says it.
8. **NO-FLUENCY LAW.** A polished number, chart or summary never stands alone: the beat shows the file it came from or the check that was run.
9. **SELF-CONTAINED BUT SERIAL.** Any one entry can be followed cold (BHOOK gives the state before); a regular viewer gets the running thread (cast, counters, entry number, the next-step lines carried forward).

## What is reused, what is new

| Part | From | Status |
|---|---|---|
| Hesitant-writer open, card test, Law 9, drawing cast, Claude palette, Kokoro Liam, all gates | show-tell | reuse |
| SHOW-THE-THING LAW, BEST-BEAT audition, `BrowserCapture`, `LectureEvidenceTable`, outro table by channel | lecture | reuse |
| Real-session law, `CCSession`, `CCDiff`, `GitHubCodeDiff`, the AI/human ledger idea (`CCHumanLedger`) | cc-explainer | reuse |
| `QuillWriter` (built 2026-10-07 for writing and log beats), `ExecutedData`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro` | runtime scenes | reuse |
| `JournalSlate` (date, time, entry N, since-last-entry strip) | — | **new, small** |
| `JournalLedger` (two columns, AI did / human did, plus the doubt line, with citations) | — | **new, small; a variant of CCHumanLedger** |
| `collect_entries.py`: splits the project's logs and commits into timestamped substantive entries, writes one `ENTRY.md` + `COUNTERS.json` per entry, numbers them | — | **new script; the heart of the skill** |

## Workflow

```
./brutalist.art/art journal <project.json> --list                 # every substantive entry, numbered, with timestamps; which have films
./brutalist.art/art journal <project.json> --entry 14             # build entry 14
./brutalist.art/art journal <project.json> --since 2026-10-07     # build every unfilmed entry from that date, one film each
```

1. **Collect** (`collect_entries.py`): read the project file (folders, counters, cast, series title, channel, playlist); walk every FRICTIONAL.md the project names and split it into entries (a `### date — heading` block, or a dated bullet that extends a day); pair each with the commit that carried it (time from the commit; the log's time note if uncommitted); drop anything the log itself marks as not substantive; number them in timestamp order; write `ENTRY.md` (the entry's text, verbatim, with its commit and changed files) and `COUNTERS.json` (counters at that time, with deltas from the previous entry). Prints the list and stops if nothing is new.
2. **Beat the record** (the builder, per entry): BHOOK from the previous entry's next-step lines or this entry's expectation; THE CHANGE, THE RESULT, WHO DID WHAT from the entry's fields; the ledger; BNEXT from the entry's next-step lines. Write `beat_sheet.json`, `SHOTLIST.md` (why each visual), `FACTCHECK.md` (every number against its file; a status report is a pointer, the log entry and the files are the sources).
3. **Voice, draw, render, gate**: as show-tell, with `JournalSlate` and `JournalLedger` through `remotion_scenes.py`. No approval gate on any free step; all machine gates to PASS; cut the master; STOP.
4. **Index**: append the entry to `<project>/youtube/journal/JOURNAL.md` (entry N, timestamp, heading, the three ledger lines, master path, published link when it exists). Publishing stays on Bear's word, into the playlist named exactly in the project file.

## Output contract

```
<project>/youtube/journal/
  JOURNAL.md                                     series index + the standing cast
  project.json                                   folders, counters, cast, series title, channel, playlist
  entry-014-2026-10-07T14-the-first-real-sync/   one reel per entry, the usual files (stamp in sortable form, to the hour)
    ENTRY.md  COUNTERS.json  beat_sheet.json  SHOTLIST.md  FACTCHECK.md  BUILD-LOG.md  README.md
```

## Worked example from today's log (2026-10-07)

The collector would find three substantive entries in the job-search project's logs for this date, each its own film:

| Entry | Time | Heading (from the log) | The change → the result → next |
|---|---|---|---|
| 14 | the hour of commit `e88a0c4` | The first real sync, and the file the sync list had missed | `demand_report.py` added to the shared list; sync run for real for the first time → `--check` reports all three in sync; three pushes → add a new shared file to the list in the same change |
| 15 | the hour the file was written | A status report for the job-search project | `STATUS-2026-10-07.md` written from the files → exec summary, counts, gaps, next steps; not yet read by Bear → read it; decide on scheduling and the five unreadable boards |
| 16 | the hour the plan was pasted | The series plan and the journal skill | plan verified against the logs; journal proposed → this file → Bear's answers to the open questions |

The three pushes themselves are not entries; they are lines in entry 14's result.

## Open for Bear

1. Title form: "Entry N: <the entry's own heading>" (proposed), or the timestamp alone.
2. First person or third: the log is in Bear's first person; Liam reads it "in for Bear" in third person (proposed, matching the series), or reads Bear's lines as written.
3. Your Turn: off by default (proposed), or on every entry.
4. The hour source: the commit (proposed); for uncommitted work, the log line's own stamp, which means log entries should start carrying the hour in the same format (`7 October 2026 · 14:00`).
5. Whether journal entries earn standing publish approval after the first three have been watched, or stay one by one.
6. The opening card shows "Video NN / TT". A journal has no fixed total. Options: set a provisional total and revise it, make the builder accept an open-ended count ("Entry 14"), or drop the position field for journal entries. Film 1 of the Professor Bear Does His Assignments series uses a provisional "01 / 08" so the card builds.
