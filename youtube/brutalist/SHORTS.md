# Brutalist Shorts: less than three minutes

Every 9:16 **Short** must be **strictly under 3:00**. Exactly 3:00.000 fails.
Plan at most 2:55 so frame rounding, audio tails and endcards have headroom.
The compiler checks both the measured timeline and encoded container/streams;
the playlist supervisor independently probes the final file before accepting it.

Cut complete beats first. Explain what **this** skill does, when to use it and
the useful result; keep an essential caveat. Generic skill explanations,
repository anatomy and detailed walkthroughs stay in the 16:9 long. Reuse
retained narration and native portrait footage. Rewrite only if cuts cannot
produce a coherent, self-contained Short under the limit. Never cut mid-sentence
at a timestamp or speed up narration to squeeze it in.

`art vertical` remains a full-length portrait companion, not a Short. Its files
must not be submitted to the Shorts playlist merely because they are 9:16.
The long and full-length portrait masters are preserved; Short-only feedback
and artifacts live in their own queue.

From the Brutalist repository root:

```bash
./repoloop.sh --shorts-only --dry
./repoloop.sh --shorts-only --prepare
./repoloop.sh --shorts-only --start
./repoloop.sh --shorts-only --status
./repoloop.sh --shorts-only --stop
```

The independent queue discovers completed, hash-verified native portrait
parents, attempts one Short at a time, and picks up later completed episodes.
Progress: [Shorts watch list](shorts/WATCH.md). State/logs:
`.repoloop/shorts/`. It uses the existing Claude Code subscription and local
Kokoro/rendering, never paid API fallback. Both queues need the Mac awake.

Each Short keeps `CUT-PLAN.json`: retained/dropped beats with reasons, parent
hash, timing, coherence review and justification for any rewrite. A new edit
requires its own frame/audio review and compiler receipt. Ready for review is
not approval to publish; Shorts still require Bear's review. Landscape approval
does not approve a newly cut Short. Nothing in this queue uploads or publishes.
