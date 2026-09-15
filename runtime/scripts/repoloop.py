#!/usr/bin/env python3
"""Resumable, serial film factory. Never publishes, signs human approval, or spends API credits."""
import argparse
import collections
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
import time
import uuid

from build_safety import (BuildError, atomic_json, atomic_text, file_digest, writable_path,
                          require_short_duration)

VERSION = 1
IGNORED = {'.git', '.repoloop', 'node_modules', '__pycache__', 'clips', 'mp3', 'mp4',
           'media', 'audio', '_qc', '_stale', '_previous-build', 'short', 'vertical', '916'}
INTRO = [
    ('what-is-brutalist', 'What Is Brutalist?',
     'Film as code: a beat sheet is the editable recipe, not the MP4. Show one small change becoming a new rendered result. Explain human judgment versus agent execution.'),
    ('download-and-set-up', 'Download Brutalist with Claude Code',
     'All fellows already have Claude Code. Give a paste-ready request to clone the public DOT repo into a new folder, inspect setup, install free dependencies, and verify readiness. Explain that a Claude Code subscription is separate from optional paid APIs. Never pretend an installation ran if you only inspected it.'),
    ('your-first-project', 'Your First Brutalist Project',
     'Start with a tiny research question and evidence. Ask Claude Code for an AI Explainer, watch it, request one visible revision, rebuild and verify. Show native landscape and portrait, then GitHub source / Drive video handoff. A runtime receipt is not publication approval.'),
]
ART_SOURCES = {
    'help': ['art'], 'list': ['art'],
    'scenes': ['runtime/scripts/scene_search.py'], 'scene-index': ['runtime/scripts/build_scene_index.py'],
    'icons': ['runtime/scripts/icon_search.py'], 'icon-build': ['runtime/scripts/build_icon_set.py'],
    'todo': ['runtime/scripts/todo.py'], 'run': ['runtime/scripts/run.sh'],
    'shorts': ['runtime/scripts/shorts.py'], 'vertical': ['runtime/scripts/shorts.py'],
    'approvals': ['runtime/scripts/build_safety.py'], 'final': ['runtime/scripts/compile.py'],
    'doctor': ['setup'], 'smoke': ['runtime/scripts/smoke_test.sh'], 'keys': ['runtime/scripts/check_keys.py'],
}
COMMON = ['skills/make/ai-explainer/SKILL.md', 'skills/make/nopunt/SKILL.md',
          'runtime/prose/teardown/PROSE.md', 'docs/PIPELINE-SAFETY.md', 'docs/FELLOWS-SUBMISSION.md',
          'REPOLOOP-PROMPT.md']


def now():
    return datetime.now(timezone.utc).isoformat()


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def read_json(path, default=None):
    return json.loads(path.read_text()) if path.is_file() else default


def fingerprint(repo, sources):
    return digest({s: file_digest(repo / s) if (repo / s).is_file() else None for s in sources})


def discover(repo):
    """Canonical commands get films; aliases map to that same film, not duplicate films."""
    items = []
    def add(key, title, kind, sources, brief='', aliases=None):
        sources = list(dict.fromkeys(sources))
        items.append({'id': key, 'slug': 'claude-liam-brutalist-' + key,
                      'title': title, 'kind': kind, 'sources': sources,
                      'brief': brief, 'aliases': aliases or [],
                      'source_sha256': fingerprint(repo, sources + COMMON)})
    for key, title, brief in INTRO:
        add(key, title, 'onboarding', ['README.md', 'art', 'setup'] + COMMON, brief)
    for source in sorted((repo / 'skills').glob('*/**/SKILL.md')):
        relative = source.relative_to(repo).as_posix()
        name = source.parent.name
        add('skill-' + name, 'The ' + name + ' Skill', 'skill', [relative],
            'Read the whole skill and its relevant references. Explain its mechanism and show a safe, real demo or a clearly labeled documented limitation.')
    seen = set()
    for line in (repo / 'art').read_text().splitlines():
        match = re.fullmatch(r'  ([^()]+)\)', line)
        if not match:
            continue
        tokens = [s.strip().strip('"') for s in match[1].split('|')]
        names = [s for s in tokens if re.fullmatch(r'[a-z][a-z-]*', s)]
        if not names:
            continue
        name = names[0]
        if name in seen:
            continue
        seen.add(name)
        add('command-' + name, 'Brutalist Command: art ' + ('--list' if name == 'list' else name),
            'command', ['art'] + ART_SOURCES.get(name, []),
            'Show the exact syntax, input, observed output, one failure case and how to recover. Aliases belong to this same episode.', tokens)
    add('command-setup', 'Brutalist Command: setup', 'command', ['setup', 'requirements.txt'])
    add('command-repoloop', 'Brutalist Command: repoloop.sh', 'command',
        ['repoloop.sh', 'runtime/scripts/repoloop.py', 'REPOLOOP-PROMPT.md'])
    covered = {p for sources in ART_SOURCES.values() for p in sources}
    # Include independent executable runtime/QC utilities, not imported helper modules.
    for directory in ('runtime/scripts', 'runtime/qc'):
        for source in sorted((repo / directory).glob('*.py')):
            relative = source.relative_to(repo).as_posix()
            if relative in covered or source.name == 'repoloop.py':
                continue
            text = source.read_text()
            if not re.search(r'if\s+__name__\s*==\s*[\'"]__main__[\'"]', text):
                continue
            key = ('qc-' if directory.endswith('/qc') else 'runtime-') + source.stem.replace('_', '-')
            add(key, 'Brutalist Utility: ' + source.name, 'utility', [relative],
                'Explain this executable utility, including real prerequisites and failure behavior. Use only disposable fixtures. For unavailable services, show source-backed behavior without inventing a successful run.')
    if len({i['id'] for i in items}) != len(items):
        raise BuildError('Duplicate inventory IDs; disambiguate before building')
    for n, item in enumerate(items, 1):
        item['order'] = n
    return items


def example_index(fellows):
    """Read only beat sheets, not participants' unrelated documents or media."""
    examples = []
    if not fellows.is_dir():
        return examples
    for root, dirs, files in os.walk(fellows, followlinks=False):
        dirs[:] = sorted(d for d in dirs if d not in IGNORED and not d.startswith('.')
                         and not (Path(root) / d).is_symlink())
        if 'beat_sheet.json' not in files:
            continue
        path = Path(root) / 'beat_sheet.json'
        if path.is_symlink() or path.stat().st_size > 2_000_000:
            continue
        try:
            sheet = read_json(path)
            md = sheet.get('metadata', {})
            examples.append({'path': str(path.relative_to(fellows)), 'sha256': file_digest(path),
                             'title': md.get('title', path.parent.name),
                             'patterns': sorted({b.get('shot', {}).get('remotion', {}).get('pattern', '')
                                                 for b in sheet.get('beats', []) if isinstance(b.get('shot'), dict)})})
        except (OSError, ValueError, TypeError, AttributeError):
            continue
    return examples


def discover_shorts(repo):
    """Independent derivative queue: no edits or feedback on landscape parents."""
    parents = read_json(repo / '.repoloop/queue.json', {'items': []})
    inventory = []
    for parent in parents['items']:
        if parent.get('status') != 'review_ready':
            continue
        reel = repo / 'youtube/brutalist' / parent['slug']
        master = reel / 'exports/vertical' / (parent['slug'] + '-vertical.mp4')
        source = reel / 'vertical/beat_sheet.json'
        receipt = read_json(master.with_suffix('.verified.json'), {})
        if not master.is_file() or not source.is_file() or receipt.get('status') != 'ready':
            continue
        if receipt.get('sha256') != file_digest(master):
            continue
        sources = [str(source.relative_to(repo)), 'REPOLOOP-SHORTS-PROMPT.md']
        inventory.append(dict(parent, slug=parent['slug'] + '-short', kind='short',
            title=parent['title'] + ' — Short', sources=sources,
            parent_reel=str(reel), parent_master=str(master),
            parent_master_sha256=receipt['sha256'],
            source_sha256=digest({'source': fingerprint(repo, sources), 'master': receipt['sha256']}),
            brief='Cut complete beats first. Explain what THIS skill/command does at a high level. '
                  'Every Short must be strictly under 180 seconds. Preserve the long unchanged.'))
        # Production state belongs to this derivative, not its completed parent.
        for key in ('status', 'outputs', 'run_id', 'attempts', 'feedback_sha256', 'note',
                    'started_at', 'completed_at', 'retry_at', 'log'):
            inventory[-1].pop(key, None)
    return inventory


def select_examples(item, examples):
    terms = set(re.findall(r'[a-z]{3,}', item['id'] + ' ' + item['title'].lower())) - {'the', 'skill', 'command', 'brutalist'}
    def rank(example):
        haystack = (example['path'] + ' ' + str(example['title']) + ' ' + ' '.join(example['patterns'])).lower()
        return (sum(t in haystack for t in terms) + (4 if 'agent-first-brutalist' in haystack else 0), example['path'])
    return sorted(examples, key=rank, reverse=True)[:2]


def feedback_digest(folder):
    return file_digest(folder / 'FEEDBACK.md') if (folder / 'FEEDBACK.md').is_file() else None


def merge_queue(old, inventory, playlist):
    prior = {i['id']: i for i in (old or {}).get('items', [])}
    result = []
    for definition in inventory:
        item = dict(prior.get(definition['id'], {}))
        changed = item.get('source_sha256') != definition['source_sha256']
        feedback = feedback_digest(playlist / definition['slug'])
        changed = changed or ('feedback_sha256' in item and feedback != item['feedback_sha256'])
        item.update(definition)
        item.setdefault('status', 'pending')
        item.setdefault('attempts', 0)
        if changed and item['status'] != 'building':
            item.update(status='pending', attempts=0, retry_at=0, note='New or changed source/feedback; old renders preserved')
        item['feedback_sha256'] = feedback
        result.append(item)
    for key, item in prior.items():
        if key not in {i['id'] for i in inventory}:
            result.append(dict(item, status='retired', note='No longer discovered; existing film retained'))
    return {'version': VERSION, 'updated_at': now(), 'items': result,
            'factory_sha256': (old or {}).get('factory_sha256'),
            'pause_until': (old or {}).get('pause_until', 0), 'pause_reason': (old or {}).get('pause_reason', '')}


@contextmanager
def exclusive_lock(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a+') as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise BuildError('Another repoloop owns this playlist; no second worker started')
        lock.seek(0); lock.truncate(); lock.write(str(os.getpid())); lock.flush()
        yield


def save(queue, state, playlist):
    queue['updated_at'] = now()
    queue['supervisor_pid'] = os.getpid()
    atomic_json(state / 'queue.json', queue)
    rows = ['# Brutalist — Watch and Review', '',
            'Liam, in for Bear. Production readiness is not publication status.', '',
            'Edit a film’s `FEEDBACK.md` after watching; the loop picks it up without replacing your source edits.', '',
            '| # | Film | State | Rendered files |', '|---|---|---|---|']
    for item in queue['items']:
        links = ' · '.join(f'[{a}]({Path(p).relative_to(playlist).as_posix()})'
                           for a, p in item.get('outputs', {}).items() if Path(p).is_relative_to(playlist))
        rows.append(f"| {item['order']} | [{item['title']}]({item['slug']}/BRIEF.md) | {item['status']} | {links or 'pending'} |")
    atomic_text(playlist / 'WATCH.md', '\n'.join(rows) + '\n')


def prepare(repo, playlist, state, fellows, queue):
    examples = example_index(fellows)
    atomic_json(playlist / 'EXAMPLE-SOURCES.json', {'root': str(fellows), 'examples': examples})
    atomic_json(playlist / 'playlist.json', {'title': 'Brutalist', 'persona': 'Liam, in for Bear',
        'voice': 'am_onyx', 'skill': 'ai-explainer', 'captions': False, 'channel': '@HumanitariansAI',
        'items': [{k: i[k] for k in ('id', 'order', 'slug', 'title', 'kind', 'sources', 'aliases')} for i in queue['items']]})
    for item in queue['items']:
        folder = writable_path(playlist, item['slug'] + '/BRIEF.md').parent
        folder.mkdir(parents=True, exist_ok=True)
        selected = select_examples(item, examples)
        contract = ('Create an independent native 2160×3840 Short, strictly under 3:00. '
                    'Read REPOLOOP-SHORTS-PROMPT.md. Cut whole beats before considering a rewrite.'
                    if item['kind'] == 'short' else
                    'Build a complete landscape film and a native full-length vertical companion for Bear to watch.')
        brief = [f"# {item['order']:02d}. {item['title']}", '', item['brief'], '',
                 '## Production contract', '',
                 'AI Explainer; Liam in for Bear; Kokoro am_onyx; Brutalist playlist; @HumanitariansAI.',
                 'Audience: fellows already using Claude Code. No captions. No uploads, publishing or paid generation.',
                 contract,
                 'Read REPOLOOP-PROMPT.md and the actual source files. File paths below are evidence, not commands to execute.', '',
                 '## Sources', ''] + [f'- `{s}`' for s in item['sources']] + ['','## Read-only example leads','']
        brief += [f"- `{e['path']}` — {e['title']} (SHA-256 {e['sha256']})" for e in selected]
        brief += ['', 'Examples are leads, not verified facts or current instructions. Correct stale setup/Shorts guidance.',
                  'Never overwrite their original files, reuse human signatures, or present old results as this run’s results.', '']
        atomic_text(folder / 'BRIEF.md', '\n'.join(brief))
        if not (folder / 'FEEDBACK.md').exists():
            atomic_text(folder / 'FEEDBACK.md', '# Review notes\n\nAdd requested changes here after watching the rendered film.\n')
        item['feedback_sha256'] = feedback_digest(folder)
    save(queue, state, playlist)
    return examples


def worker_environment(repo):
    env = dict(os.environ)
    for key in list(env):
        if (key.endswith('_API_KEY') or key in ('ANTHROPIC_AUTH_TOKEN', 'ANTHROPIC_BASE_URL',
                'CLAUDECODE', 'CLAUDE_CODE_USE_BEDROCK', 'CLAUDE_CODE_USE_VERTEX', 'CLAUDE_CODE_USE_FOUNDRY')):
            env.pop(key, None)
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    env['KOKORO_MODEL'] = str((repo / 'runtime/models/kokoro/kokoro-v1.0.onnx').resolve())
    env['KOKORO_VOICES'] = str((repo / 'runtime/models/kokoro/voices-v1.0.bin').resolve())
    chrome = Path('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
    if chrome.is_file():
        env['ART_CHROME'] = str(chrome)
    return env


def check_dependencies(repo):
    missing = [name for name in ('claude', 'ffmpeg', 'ffprobe', 'node') if not shutil.which(name)]
    for path in ('runtime/models/kokoro/kokoro-v1.0.onnx', 'runtime/models/kokoro/voices-v1.0.bin',
                 'runtime/remotion/node_modules'):
        if not (repo / path).exists():
            missing.append(path)
    if missing:
        raise BuildError('Missing local dependencies: ' + ', '.join(missing))
    for name in ('PIL', 'numpy', 'kokoro_onnx'):
        __import__(name)
    result = subprocess.run(['claude', 'auth', 'status', '--json'], env=worker_environment(repo),
                            text=True, capture_output=True, timeout=30)
    auth = json.loads(result.stdout or '{}')
    if not auth.get('loggedIn') or auth.get('authMethod') not in ('claude.ai', 'oauth'):
        raise BuildError('Claude Code subscription login unavailable; no API-key fallback is allowed')


def snapshot_toolkit(repo, workspace):
    toolkit = workspace / 'toolkit'
    if not (workspace / 'toolkit-baseline.json').is_file():
        toolkit.mkdir(parents=True, exist_ok=True)
        def skip_generated(directory, names):
            return [name for name in names if name in ('__pycache__', 'node_modules', '.env')
                    or name.endswith('.pyc') or (Path(directory) / name).is_symlink()]
        for name in ('runtime/scripts', 'runtime/qc', 'runtime/schema', 'runtime/manim', 'runtime/fonts',
                     'runtime/prose', 'runtime/design', 'runtime/remotion/src', 'runtime/remotion/public',
                     'skills', 'brands', 'docs'):
            source = repo / name
            if source.is_dir():
                shutil.copytree(source, toolkit / name, dirs_exist_ok=True, ignore=skip_generated)
        for source in list(repo.glob('*.md')) + [repo / 'art', repo / 'setup', repo / 'requirements.txt']:
            if source.is_file():
                shutil.copy2(source, toolkit / source.name)
        for source in (repo / 'runtime/remotion').iterdir():
            if source.is_file() and source.suffix in ('.json', '.ts', '.js', '.mjs'):
                shutil.copy2(source, toolkit / 'runtime/remotion' / source.name)
        if not (toolkit / 'runtime/remotion/node_modules').is_symlink():
            (toolkit / 'runtime/remotion/node_modules').symlink_to((repo / 'runtime/remotion/node_modules').resolve(), target_is_directory=True)
        baseline = {str(p.relative_to(toolkit)): file_digest(p) for p in toolkit.rglob('*')
                    if p.is_file() and not p.is_symlink() and 'node_modules' not in p.parts}
        commit = subprocess.run(['git', '-C', str(repo), 'rev-parse', 'HEAD'], capture_output=True, text=True)
        overrides = subprocess.run(['git', '-C', str(repo), 'diff', '--name-only', 'HEAD', '--', 'runtime/remotion/src'], capture_output=True, text=True)
        untracked = subprocess.run(['git', '-C', str(repo), 'ls-files', '--others', '--exclude-standard', '--', 'runtime/remotion/src'], capture_output=True, text=True)
        atomic_json(workspace / 'toolkit-revision.json', {'commit': commit.stdout.strip(),
            'local_overrides': sorted(set(overrides.stdout.splitlines() + untracked.stdout.splitlines())),
            'skipped': 'Symlinked render/audio assets are not toolkit source and are not copied.'})
        atomic_json(workspace / 'toolkit-baseline.json', baseline)
    return toolkit


def worker_settings(repo, workspace, folder, fellows):
    # Sandboxed subprocesses may write only their scratch workspace and this film.
    # Runtime dependencies are shared read-only; no skip-permissions escape hatch.
    return {'disableAllHooks': True,
        'permissions': {'defaultMode': 'dontAsk',
            'allow': ['Read', 'Glob', 'Grep', 'Bash', f'Edit(/{workspace}/**)', f'Edit(/{folder}/**)'],
            'deny': ['Read(**/.env)', 'Read(~/.ssh/**)', 'Read(~/.aws/**)', 'Read(~/.config/gcloud/**)',
                     'Bash(git push *)', 'Bash(gh *)', 'Bash(curl *)', 'Bash(wget *)', 'Bash(ssh *)']},
        'sandbox': {'enabled': True, 'failIfUnavailable': True, 'autoAllowBashIfSandboxed': True,
            'allowUnsandboxedCommands': False,
            'filesystem': {'allowWrite': [str(workspace), str(folder)],
                'denyWrite': [str(repo / 'runtime'), str(repo / 'skills'), str(repo / '.git'), str(fellows)],
                'denyRead': ['~/.ssh', '~/.aws', '~/.config/gcloud', str(repo / '.env')]},
            'network': {'allowedDomains': ['localhost', '127.0.0.1'], 'allowLocalBinding': True}}}


def run_process(command, cwd, env, log, timeout, stop):
    with log.open('w') as output:
        process = subprocess.Popen(command, cwd=cwd, env=env, stdout=output, stderr=subprocess.STDOUT,
                                   stdin=subprocess.DEVNULL, start_new_session=True)
        started = time.monotonic()
        try:
            while process.poll() is None:
                if stop.exists() or time.monotonic() - started > timeout:
                    os.killpg(process.pid, signal.SIGTERM)
                    try:
                        process.wait(timeout=15)
                    except subprocess.TimeoutExpired:
                        os.killpg(process.pid, signal.SIGKILL); process.wait()
                    return 130 if stop.exists() else 124
                time.sleep(2)
            return process.returncode
        finally:
            if process.poll() is None:
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=15)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL); process.wait()


def is_rate_limit(text):
    return bool(re.search(r"hit your (?:session |usage )?limit|rate.limit(?:ed| exceeded| reached)|usage limit reached|out of extra usage", text, re.I))


def is_auth_failure(text):
    return bool(re.search(r'OAuth access token has been revoked|authentication_failed|Failed to authenticate|not logged in', text, re.I))


def worker_failed(log):
    """Claude may exit zero with an error result. Never accept that as a build."""
    result = None
    with log.open() as stream:
        for line in stream:
            try:
                event = json.loads(line)
                if event.get('type') == 'result':
                    result = event
            except (ValueError, AttributeError):
                continue
    return result is None or result.get('is_error', False) or result.get('subtype') != 'success'


def verify_film(folder, item, dimensions):
    outputs = {}
    for aspect, size in dimensions.items():
        reel = folder if aspect in ('landscape', 'short') else folder / 'vertical'
        sheet = read_json(reel / 'beat_sheet.json', {})
        md, beats = sheet.get('metadata', {}), sheet.get('beats', [])
        minimum_beats = 3 if aspect == 'short' else 8
        if len(beats) < minimum_beats or md.get('playlist') != 'Brutalist' or md.get('voice_kokoro', md.get('voice')) != 'am_onyx':
            raise BuildError(f'{aspect}: missing film, Brutalist playlist or Liam voice')
        if any(b.get('voice', 'am_onyx') != 'am_onyx' or b.get('engine', 'kokoro') != 'kokoro' for b in beats):
            raise BuildError(f'{aspect}: non-Liam narration')
        patterns = [b.get('shot', {}).get('remotion', {}).get('pattern', '') for b in beats]
        if aspect != 'short' and (not patterns[0].startswith('ClaudeComposerAsk') or 'HesitantWriter' not in patterns[1]):
            raise BuildError(f'{aspect}: required cold open / hesitant-writer overview missing')
        if aspect != 'short' and (not patterns[-2].startswith('ClaudeComposerAsk') or
                beats[-2]['shot']['remotion'].get('props', {}).get('greeting', '').lower().strip() not in ('your turn', 'your turn.')):
            raise BuildError(f'{aspect}: missing scaffolded Your Turn')
        if 'liam' not in beats[0].get('narration_text', '').lower() or 'in for bear' not in beats[0].get('narration_text', '').lower():
            raise BuildError(f'{aspect}: narrator disclosure missing')
        if 'liam' not in beats[-1].get('narration_text', '').lower() or 'in for bear' not in beats[-1].get('narration_text', '').lower():
            raise BuildError(f'{aspect}: Liam sign-off missing')
        expected = item['slug'] + ('-vertical' if aspect == 'vertical' else '')
        output = writable_path(folder, f'exports/{aspect}/{expected}.mp4')
        receipt = read_json(output.with_suffix('.verified.json'), {})
        state = read_json(reel / 'build-state.json', {})
        if not output.is_file() or state.get('status') != 'ready' or receipt.get('status') != 'ready':
            raise BuildError(f'{aspect}: no successful verified export')
        sha = file_digest(output)
        if receipt.get('sha256') != sha or state.get('sha256') != sha:
            raise BuildError(f'{aspect}: export hash does not match verification')
        probe = subprocess.run(['ffprobe', '-v', 'error', '-show_streams', '-show_format', '-of', 'json', str(output)],
                               capture_output=True, text=True, check=True, timeout=60)
        streams = json.loads(probe.stdout).get('streams', [])
        video = next((s for s in streams if s.get('codec_type') == 'video'), {})
        if (video.get('width'), video.get('height')) != tuple(size):
            raise BuildError(f'{aspect}: expected native {size[0]}×{size[1]} export')
        if aspect == 'short':
            if md.get('kind') != 'short' or md.get('aspect_ratio') != '9:16':
                raise BuildError('Short must be explicitly marked kind=short and aspect_ratio=9:16')
            measured = json.loads(probe.stdout)
            require_short_duration(measured.get('format', {}).get('duration'), 'Short export')
            for stream in streams:
                if stream.get('codec_type') in ('video', 'audio') and stream.get('duration') is not None:
                    require_short_duration(stream['duration'], 'Short ' + stream['codec_type'])
            plan = read_json(reel / 'CUT-PLAN.json', {})
            if (plan.get('strategy') not in ('whole-beat-cut', 'rewrite-after-cut')
                    or not plan.get('focus') or not plan.get('kept_beats')
                    or not plan.get('cut_first_review')
                    or plan.get('parent_master_sha256') != item.get('parent_master_sha256')):
                raise BuildError('Short needs a source-bound, cut-first editorial plan')
            if plan['strategy'] == 'rewrite-after-cut' and not plan.get('rewrite_reason'):
                raise BuildError('Short rewrite needs evidence that a coherent beat cut was insufficient')
            if plan['kept_beats'] != [b['beat_id'] for b in beats]:
                raise BuildError('Short cut plan must name the actual final beats in order')
            if plan['strategy'] == 'whole-beat-cut':
                parent = read_json(Path(item['parent_reel']) / 'vertical/beat_sheet.json', {})
                retained = [b for b in parent.get('beats', []) if b['beat_id'] in plan['kept_beats']]
                if ([b['beat_id'] for b in retained] != plan['kept_beats'] or
                        any(a.get('narration_text') != b.get('narration_text') for a, b in zip(retained, beats))):
                    raise BuildError('Whole-beat cut changed narration/order; record and justify a rewrite instead')
        if not any(s.get('codec_type') == 'audio' for s in streams):
            raise BuildError(f'{aspect}: audio stream missing')
        sound = subprocess.run(['ffmpeg', '-nostdin', '-v', 'info', '-xerror', '-i', str(output),
                                '-af', 'volumedetect', '-f', 'null', '-'], capture_output=True, text=True, check=True, timeout=300)
        mean = re.search(r'mean_volume:\s*(-?[\d.]+) dB', sound.stderr)
        if not mean or float(mean[1]) <= -40:
            raise BuildError(f'{aspect}: narration is missing or too quiet')
        review = read_json(reel / 'VISUAL-REVIEW.json', {})
        if (not item.get('run_id') or review.get('run_id') != item['run_id'] or
                review.get('source_sha256') != item['source_sha256'] or
                review.get('beat_sheet_sha256') != file_digest(reel / 'beat_sheet.json') or
                review.get('status') != 'pass' or review.get('reviewer_type') != 'ai' or review.get('video_sha256') != sha):
            raise BuildError(f'{aspect}: missing current AI frame-review record (not a human sign-off)')
        if review.get('blockers') != 0 or review.get('majors') != 0 or not review.get('frames'):
            raise BuildError(f'{aspect}: incomplete or failing visual review')
        for frame in review['frames']:
            path = writable_path(reel, frame['path'])
            if not path.is_file() or frame.get('sha256') != file_digest(path):
                raise BuildError(f'{aspect}: visual-review frame evidence missing/stale')
        for name in ('FACTCHECK.md', 'SOURCES.md', 'SHOTLIST.md', 'PROMPTS.md', 'CHECKS-REPORT.md', 'BUILD-PROMPT.md', 'TYPECHECK.md'):
            if not (reel / name).is_file() or not (reel / name).read_text().strip():
                raise BuildError(f'{aspect}: missing {name}')
        if sheet.get('metadata', {}).get('build', {}).get('slates'):
            raise BuildError(f'{aspect}: unfinished visual slots')
        if any(reel.glob('*.srt')) or any(reel.glob('*.vtt')) or md.get('captions') not in (None, False):
            raise BuildError(f'{aspect}: this playlist requested no captions')
        outputs[aspect] = str(output)
    return outputs


def export_scene_changes(workspace, folder):
    toolkit = workspace / 'toolkit'
    baseline = read_json(workspace / 'toolkit-baseline.json', {})
    overrides = read_json(workspace / 'toolkit-revision.json', {}).get('local_overrides', [])
    changed = []
    for source in (toolkit / 'runtime/remotion/src').rglob('*'):
        if source.is_file() and not source.is_symlink():
            relative = str(source.relative_to(toolkit))
            if relative in overrides or baseline.get(relative) != file_digest(source):
                destination = folder / 'scene-source' / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, destination)
                changed.append(relative)
    atomic_json(folder / 'scene-source-manifest.json', {'files': changed,
        'baseline_sha256': file_digest(workspace / 'toolkit-baseline.json'),
        'note': 'Overlay on the local toolkit snapshot recorded in SOURCE-SNAPSHOT.json, not blindly on another revision.'})


def build_one(repo, playlist, state, fellows, item, examples, args):
    folder = playlist / item['slug']
    workspace = state / 'workspaces' / item['slug']
    toolkit = snapshot_toolkit(repo, workspace)
    # Only copies go into the agent's workspace; originals are never writable.
    copied = []
    for example in select_examples(item, examples):
        source = fellows / example['path']
        if source.is_file() and file_digest(source) == example['sha256']:
            destination = workspace / 'examples' / (example['sha256'][:12] + '.json')
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
            copied.append(dict(example, local_copy=str(destination)))
    atomic_json(workspace / 'example-sources.json', copied)
    atomic_json(workspace / 'settings.json', worker_settings(repo, workspace, folder, fellows))
    references = item['sources'] + COMMON
    if args.shorts_only:
        references += ['runtime/scripts/build_safety.py', 'runtime/scripts/compile.py', 'runtime/scripts/shorts.py']
    source_snapshot = {s: file_digest(repo / s) if (repo / s).is_file() else None for s in references}
    atomic_json(folder / 'SOURCE-SNAPSHOT.json', {'captured_at': now(), 'files': source_snapshot,
                'revision': read_json(workspace / 'toolkit-revision.json', {}),
                'toolkit_baseline_sha256': file_digest(workspace / 'toolkit-baseline.json'),
                'runtime_note': 'Isolated copy of the local working toolkit, including any existing uncommitted scenes.'})
    # New source docs refresh in the isolated copy; scene edits remain until reviewed.
    for relative in references:
        source, dest = repo / relative, toolkit / relative
        if source.is_file():
            dest.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(source, dest)
    prompt_file = 'REPOLOOP-SHORTS-PROMPT.md' if args.shorts_only else 'REPOLOOP-PROMPT.md'
    prompt = (repo / prompt_file).read_text() + '\n\nTHIS INVOCATION\n' + json.dumps({
        'episode': item, 'toolkit': str(toolkit), 'reel': str(folder),
        'examples': str(workspace / 'example-sources.json'),
        'dimensions': args.dimensions, 'previous_error': item.get('note', '')}, indent=2)
    atomic_text(folder / 'BUILD-PROMPT.md', prompt)
    command = ['claude', '-p', prompt, '--permission-mode', 'dontAsk', '--setting-sources', '',
               '--settings', str(workspace / 'settings.json'), '--tools', 'Read,Glob,Grep,Edit,Write,Bash',
               '--add-dir', str(folder), '--strict-mcp-config', '--mcp-config', '{"mcpServers":{}}',
               '--no-chrome', '--no-session-persistence', '--output-format', 'stream-json', '--verbose']
    if args.model:
        command += ['--model', args.model]
    log = state / 'logs' / f"{item['slug']}-{int(time.time())}.jsonl"
    log.parent.mkdir(parents=True, exist_ok=True)
    item['log'] = str(log)
    atomic_json(state / 'active.json', {'id': item['id'], 'run_id': item['run_id'], 'log': str(log), 'started_at': now()})
    env = worker_environment(repo); env['ART_HOME'] = str(toolkit)
    code = run_process(command, toolkit, env, log, args.timeout, state / 'STOP')
    with log.open('rb') as f:
        f.seek(max(0, log.stat().st_size - 16000)); tail = f.read().decode(errors='replace')
    if is_rate_limit(tail):
        return 'limited', 'Claude usage limit; retain job and wait for reset', {}
    if is_auth_failure(tail):
        return 'auth_required', 'Claude login rejected; run claude auth login. The queue will retry automatically in 30 minutes.', {}
    if code != 0:
        return 'failed', f'Claude worker exited {code}; inspect {log.name}', {}
    if worker_failed(log):
        return 'failed', f'Claude did not return a successful result; inspect {log.name}', {}
    try:
        if args.shorts_only and (file_digest(Path(item['parent_master'])) != item['parent_master_sha256']
                or any(file_digest(repo / s) != source_snapshot[s] for s in item['sources'])):
            raise BuildError('Short parent/policy changed during this cut; preserve output and retry new source')
        outputs = verify_film(folder, item, args.dimensions)
        export_scene_changes(workspace, folder)
        return 'review_ready', 'Rendered and machine-checked; awaiting Bear’s viewing and edits', outputs
    except (BuildError, OSError, ValueError, KeyError, IndexError, subprocess.SubprocessError) as exc:
        return 'failed', str(exc), {}


def lock_held(path):
    if not path.is_file():
        return False
    with path.open() as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            return False
        except BlockingIOError:
            return True


def start_background(repo, state, args):
    if lock_held(state / 'worker.lock'):
        print('A repoloop worker already owns this playlist; no duplicate started.')
        return 0
    state.mkdir(parents=True, exist_ok=True)
    command = [sys.executable, str(Path(__file__).resolve()), '--repo', str(repo), '--forever',
               '--timeout', str(args.timeout), '--min-free-gb', str(args.min_free_gb)]
    for key in ('fellows', 'only', 'model'):
        if getattr(args, key):
            command += ['--' + key, str(getattr(args, key))]
    if args.landscape_only:
        command += ['--landscape-only']
    if args.shorts_only:
        command += ['--shorts-only']
    with (state / 'supervisor.log').open('a') as log:
        process = subprocess.Popen(command, cwd=repo, env=worker_environment(repo), stdin=subprocess.DEVNULL,
                                   stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
    time.sleep(3)
    if process.poll() is not None:
        raise BuildError(f'Supervisor exited {process.returncode}; inspect .repoloop/supervisor.log')
    watch_path = 'youtube/brutalist/' + ('shorts/' if args.shorts_only else '') + 'WATCH.md'
    status_flags = '--shorts-only --status' if args.shorts_only else '--status'
    print(f'Started supervisor PID {process.pid}; inspect {status_flags} and {watch_path}.')
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--fellows', type=Path)
    mode = parser.add_mutually_exclusive_group()
    for flag in ('dry', 'prepare', 'status', 'stop', 'once', 'start'):
        mode.add_argument('--' + flag, action='store_true')
    parser.add_argument('--forever', action='store_true')
    parser.add_argument('--n', type=int, default=0)
    parser.add_argument('--only', help='exact inventory ID')
    parser.add_argument('--timeout', type=int, default=9000)
    parser.add_argument('--min-free-gb', type=float, default=12)
    parser.add_argument('--model', default=os.environ.get('REPOLOOP_MODEL'))
    parser.add_argument('--landscape-only', action='store_true')
    parser.add_argument('--shorts-only', action='store_true',
                        help='independent cut-first queue from completed native portraits; never rebuilds longs')
    args = parser.parse_args()
    if args.n < 0 or args.timeout < 1 or args.min_free_gb < 1:
        parser.error('n must be nonnegative; timeout and minimum free GB must be positive')
    if args.shorts_only and args.landscape_only:
        parser.error('--shorts-only and --landscape-only are mutually exclusive')
    repo = args.repo.resolve()
    playlist = writable_path(repo, 'youtube/brutalist/' + ('shorts/' if args.shorts_only else '') + 'WATCH.md').parent
    state = writable_path(repo, '.repoloop/' + ('shorts/' if args.shorts_only else '') + 'queue.json').parent
    scan = discover_shorts if args.shorts_only else discover
    fellows = (args.fellows or repo.parent / 'humanitarians-youtube/fellows').resolve()
    args.dimensions = {'landscape': [3840, 2160]}
    if not args.landscape_only:
        args.dimensions['vertical'] = [2160, 3840]
    if args.shorts_only:
        args.dimensions = {'short': [2160, 3840]}
    if args.status:
        queue = read_json(state / 'queue.json', {'items': []})
        active = [i for i in queue['items'] if i['status'] == 'building']
        print(json.dumps({'updated_at': queue.get('updated_at'), 'counts': dict(collections.Counter(i['status'] for i in queue['items'])),
                          'running': lock_held(state / 'worker.lock'), 'pause_reason': queue.get('pause_reason'),
                          'pause_until': queue.get('pause_until'),
                          'active_log': read_json(state / 'active.json') if active else None,
                          'active': active}, indent=2))
        return 0
    if args.stop:
        state.mkdir(parents=True, exist_ok=True); atomic_text(state / 'STOP', now() + '\n')
        print('Stop requested; the current worker will be terminated and its files retained.'); return 0
    inventory = scan(repo)
    if args.only and args.only not in {i['id'] for i in inventory}:
        raise BuildError('Unknown --only ID; inspect --dry')
    if args.dry:
        for item in inventory:
            print(f"{item['order']:02d} {item['id']}: {item['title']} [{item['kind']}]")
        print(f'{len(inventory)} films; fresh Claude context per film; Liam; no captions; no publication.')
        return 0
    if args.start:
        return start_background(repo, state, args)
    playlist.mkdir(parents=True, exist_ok=True)
    with exclusive_lock(state / 'worker.lock'):
        previous = read_json(state / 'queue.json')
        queue = merge_queue(previous, inventory, playlist)
        factory_sha = file_digest(Path(__file__).resolve())
        if (previous or {}).get('factory_sha256') != factory_sha:
            for item in queue['items']:
                if item['status'] == 'retrying':
                    item.update(status='pending', retry_at=0, attempts=0,
                                note='Factory updated; retry with repaired infrastructure')
        queue['factory_sha256'] = factory_sha
        for item in queue['items']:
            if item['status'] == 'building':
                item.update(status='pending', note='Recovered interrupted worker; output files retained')
        examples = prepare(repo, playlist, state, fellows, queue)
        if args.prepare:
            print(f"Prepared {len(inventory)} briefs and indexed {len(examples)} read-only fellows examples."); return 0
        check_dependencies(repo)
        if (state / 'STOP').exists():
            # A deliberate new run acknowledges the previous stop; never deletes films.
            (state / 'STOP').unlink()
        def stop_signal(signum, frame):
            atomic_text(state / 'STOP', f'Signal {signum} at {now()}\n')
        signal.signal(signal.SIGTERM, stop_signal)
        signal.signal(signal.SIGINT, stop_signal)
        count = 0
        last_scan = time.monotonic()
        while not (state / 'STOP').exists():
            if time.monotonic() - last_scan >= 600:
                queue = merge_queue(queue, scan(repo), playlist)
                examples = prepare(repo, playlist, state, fellows, queue)
                last_scan = time.monotonic()
            ready = [i for i in queue['items'] if i['status'] in ('pending', 'retrying')
                     and i.get('retry_at', 0) <= time.time() and (not args.only or i['id'] == args.only)]
            free = shutil.disk_usage(repo).free / 1_000_000_000
            if free < args.min_free_gb:
                queue.update(pause_until=time.time() + 600, pause_reason=f'Low disk: {free:.1f} GB free')
            if queue.get('pause_until', 0) > time.time() or not ready:
                save(queue, state, playlist)
                pending = any(i['status'] in ('pending', 'retrying') and (not args.only or i['id'] == args.only) for i in queue['items'])
                if not args.forever:
                    return 3 if pending else 0
                time.sleep(30)
                continue
            queue.update(pause_until=0, pause_reason='')
            item = ready[0]
            item.update(status='building', started_at=now(), run_id=uuid.uuid4().hex)
            save(queue, state, playlist)
            print(f"{now()} Building {item['order']}: {item['title']}", flush=True)
            try:
                status, note, outputs = build_one(repo, playlist, state, fellows, item, examples, args)
            except (BuildError, OSError, ValueError, subprocess.SubprocessError) as exc:
                status, note, outputs = 'failed', str(exc), {}
            if status in ('limited', 'auth_required'):
                item.update(status='pending', note=note)
                queue.update(pause_until=time.time() + 1800, pause_reason=note)
            elif status == 'failed':
                item['attempts'] += 1
                # Bounded backoff, not a hot retry loop; other films proceed meanwhile.
                item.update(status='retrying', note=note, retry_at=time.time() + min(21600, 300 * 2 ** min(item['attempts'] - 1, 7)))
            else:
                item.update(status=status, note=note, outputs=outputs, completed_at=now(), attempts=0)
            save(queue, state, playlist)
            print(f"{now()} {item['id']}: {item['status']} — {note}", flush=True)
            count += 1
            if args.once or (args.n and count >= args.n):
                return 0 if item['status'] == 'review_ready' else 3
        return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (BuildError, OSError, ValueError, ImportError, subprocess.SubprocessError) as exc:
        print(f'[repoloop] {exc}', file=sys.stderr)
        raise SystemExit(2)
