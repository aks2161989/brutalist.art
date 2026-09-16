# PROMPTS — Brutalist Utility: pantry.py
## run_id: 1df027e6acef4cf1ad6843ed3815ffb7

## Your Turn prompt (B10)

Paste this into Claude Code, run from your reel folder:

```
Read my beat_sheet.json and list every file in my pantry/ folder. For each file pantry.py would reject — missing beat prefix, beat not in the sheet, or wrong extension — explain why and rewrite the filename so it passes the intake check.
```

**Expected artifact:** A table of every pantry/ file, its current name, the reason it would be rejected (if any), and the corrected filename. Files that already pass get a ✓.

**Test of success:** After renaming per the output, run `python3 runtime/scripts/pantry.py reels/<slug>` — zero SKIP lines should appear in the console output.

**What to look for in Claude's answer:**
1. Did Claude read the actual beat IDs from beat_sheet.json, not invent them?
2. Does the renamed list match the BID_RE pattern `^[A-Z]{1,3}\d{2}`?
3. Are portrait clips (taller-than-wide) named `<BID>-916.*` if they belong to Short slots?

## AI generation prompts used in production

None. All beats are deterministic Remotion compositions. No image-generation,
video-generation, or AI-clip prompts were used. No pantry/ assets required.

## Demo commands (source-backed, run in toolkit)

```bash
# Verify pantry.py is present and readable
python3 -c "import ast; ast.parse(open('runtime/scripts/pantry.py').read()); print('pantry.py: valid Python')"

# Show the Pantry Law docstring
python3 -c "
import pantry  # run from runtime/scripts/ with sys.path manipulation
" 2>&1 || python3 -c "
with open('runtime/scripts/pantry.py') as f:
    src = f.read()
# Print the opening docstring (lines 2-18)
import ast
tree = ast.parse(src)
print(ast.get_docstring(tree.body[0]))  # module docstring
"

# Verify BID_RE pattern
python3 -c "
import re
BID_RE = re.compile(r'^([A-Z]{1,3}\d{2})')
tests = [
    ('B04_restoration.mov', True),
    ('B12_landscape.png', True),
    ('B04-916.mp4', True),
    ('broll.mp4', False),
    ('thumbnail.jpg', False),
]
for name, expected in tests:
    m = BID_RE.match(name)
    status = 'PASS' if bool(m) == expected else 'FAIL'
    print(f'{status}: {name!r} -> {m.group(1) if m else \"no match\"}')"
```
