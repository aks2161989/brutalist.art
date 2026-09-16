import os, pathlib

ISOPATH = '/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/.repoloop/workspaces/claude-liam-brutalist-command-smoke/toolkit/runtime/remotion/node_modules/@remotion/renderer/dist/open-browser.js'
PUBPATH = '/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/node_modules/@remotion/renderer/dist/open-browser.js'

content = pathlib.Path(ISOPATH).read_text()
iso_inode = os.stat(ISOPATH).st_ino
pub_inode = os.stat(PUBPATH).st_ino
print(f'Before: iso inode={iso_inode}, pub inode={pub_inode}, same={iso_inode==pub_inode}')

# Replace the Linux-only single-process condition to also cover macOS
OLD = "process.platform === 'linux'"
NEW = "(process.platform === 'linux' || process.platform === 'darwin')"
patched = content.replace(OLD, NEW)
changed = (patched != content)
print(f'Pattern matched and replaced: {changed}')

if changed:
    os.unlink(ISOPATH)
    pathlib.Path(ISOPATH).write_text(patched)
    iso_inode2 = os.stat(ISOPATH).st_ino
    pub_inode2 = os.stat(PUBPATH).st_ino
    print(f'After: iso inode={iso_inode2}, pub inode={pub_inode2}, same={iso_inode2==pub_inode2}')
    print('OK: hardlink broken, open-browser.js patched in isolated toolkit only')
else:
    print('ERROR: pattern not found in file')
    # Print context around the expected location
    idx = content.find("'linux'")
    print(repr(content[max(0,idx-50):idx+100]))
