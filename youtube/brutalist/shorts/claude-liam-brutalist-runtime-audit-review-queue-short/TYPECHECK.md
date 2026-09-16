# TYPECHECK — Brutalist Utility: audit_review_queue.py — Short

run_id: 51f5933e39e74631bacd3698e3be0613  
Short cut: 6/12 beats (B00, B01, B05, B07, B09, B11). All beats reuse native portrait renders from parent vertical.

## Beat schema checks

All retained beats use Remotion 916 compositions. No Remotion re-renders were needed (native portrait reused).

| Beat | Pattern | Props used | Schema match |
|---|---|---|---|
| B00 | ClaudeComposerAsk916 | greeting, topic, segment, command, runningText, output[], folderLabel, modelLabel, effortLabel | ✓ |
| B01 | BrutalistHesitantWriter916 | text, triggerWords, replacementWords, seed, face, fontSize, lineSpacing, align, charMs, jitter, mistakeRate, hesitateWithin, hesitateBetween, banner, brandLabel | ✓ |
| B05 | ClaudeCodeBeat916 | title, code, sparkLine, language, brandLabel | ✓ |
| B07 | ExecutedData916 | title, mode, columnLabels[], rows[], note | ✓ |
| B09 | ClaudeVerdictArtifact916 | artifactTitle, artifactHeading, artifactLines[], brandLabel | ✓ |
| B11 | ClaudeTitleOutro916 | title, slug | ✓ |

## Metadata checks

| Field | Value | Expected | Status |
|---|---|---|---|
| kind | short | short | ✓ |
| aspect_ratio | 9:16 | 9:16 | ✓ |
| voice | am_onyx | am_onyx | ✓ |
| voice_kokoro | am_onyx | am_onyx | ✓ |
| captions | false | false | ✓ |
| playlist | Brutalist | Brutalist | ✓ |
| short_validation.status | ready | ready | ✓ |
| total_estimated_duration_seconds | 121.96 | < 175.0 | ✓ |

## Audio policy

- B11: audio_policy: silence (expected for outro beat; 6.0s silent gap ✓)
- All other beats: kokoro am_onyx MP3s present

## No type errors found.
