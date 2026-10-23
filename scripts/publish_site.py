"""Review or publish one static site to its existing GitHub Pages repository.

Uses the operator's existing gh sign-in. Never stores a token or copies Git history.
Default is a read-only diff; --publish makes one non-forced, atomic branch update.
"""
import argparse
import base64
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
EXTENSIONS = {'.html', '.htm', '.css', '.js', '.json', '.svg', '.png', '.jpg', '.jpeg',
              '.gif', '.webp', '.ico', '.ttf', '.woff', '.woff2', '.eot', '.otf',
              '.md', '.txt', '.xml', '.py', '.yml', '.yaml'}
SECRET = re.compile(rb'(?:-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|AKIA[0-9A-Z]{16}|gh[pousr]_[A-Za-z0-9]{30,})')


def api(path, method='GET', body=None):
    args = ['gh', 'api', path, '--method', method]
    payload = None
    if body is not None:
        args += ['--input', '-']
        payload = json.dumps(body).encode()
    process = subprocess.run(args, input=payload, capture_output=True, timeout=60)
    if process.returncode:
        raise ValueError('GitHub operation failed; check gh authentication, permissions and target repository.')
    return json.loads(process.stdout) if process.stdout.strip() else None


def permitted(name):
    path = Path(name)
    return (not path.is_absolute() and '..' not in path.parts and
            not any(part in {'.git', '.env', 'node_modules', '.venv'} for part in path.parts) and
            (path.suffix.lower() in EXTENSIONS or path.name in {'CNAME', '.nojekyll', '.gitignore'}))


def publish(site, write=False):
    manifest = json.loads((ROOT / 'sites.json').read_text(encoding='utf-8'))
    item = manifest['sites'][site]
    folder = (ROOT / item['folder']).resolve()
    if not folder.is_relative_to(ROOT / 'sites') or not (folder / 'index.html').is_file():
        raise ValueError('Site must be a static folder under sites/ with index.html.')
    target = item['deployment_repository']
    if not re.fullmatch(r'gr3ysbot-tech/[A-Za-z0-9_.-]+', target):
        raise ValueError('Unexpected deployment repository owner or name.')
    meta = api('repos/' + target)
    if meta['private'] or meta['default_branch'] != 'main':
        raise ValueError('Publishing requires an existing public website-only repository on main.')
    prefix = 'repos/' + target + '/git/'
    head = api(prefix + 'ref/heads/main')['object']['sha']
    base_tree = api(prefix + 'commits/' + head)['tree']['sha']
    tree = api(prefix + 'trees/' + base_tree + '?recursive=1')
    if tree.get('truncated'):
        raise ValueError('Refusing an incomplete target tree.')
    remote = {}
    for row in tree['tree']:
        if row['type'] == 'tree':
            continue
        if row['type'] != 'blob' or row['mode'] not in ('100644', '100755') or not permitted(row['path']):
            raise ValueError('Target includes a non-static or unsupported file; review it before publishing.')
        remote[row['path']] = row
    local = {}
    for path in folder.rglob('*'):
        if path.is_symlink():
            raise ValueError('Symlinks are not permitted in public site sources.')
        if not path.is_file():
            continue
        name = path.relative_to(folder).as_posix()
        if not permitted(name) or not path.resolve().is_relative_to(folder):
            raise ValueError('Source includes a non-static or unsupported file.')
        content = path.read_bytes()
        if SECRET.search(content):
            raise ValueError('A possible credential was found; source must be reviewed before publication.')
        sha = hashlib.sha1(b'blob ' + str(len(content)).encode() + b'\0' + content).hexdigest()
        local[name] = {'content': content, 'sha': sha}
    if 'CNAME' in local and local['CNAME']['content'].decode().strip() != (item.get('cname_file') or item['domain']):
        raise ValueError('CNAME does not match the declared custom domain.')
    changes = [name for name in sorted(local) if name not in remote or local[name]['sha'] != remote[name]['sha']]
    removed = sorted(set(remote) - set(local))
    result = {'site': site, 'target': target, 'files': len(local), 'changed': changes, 'removed': removed, 'published': False}
    if not write or not (changes or removed):
        return result
    git = ['git', '-c', 'safe.directory=' + ROOT.as_posix(), '-C', str(ROOT)]
    status = subprocess.run(git + ['status', '--porcelain'], capture_output=True, text=True, timeout=20)
    if status.returncode or status.stdout.strip():
        raise ValueError('Commit and push the central source before publishing a deployment target.')
    revision = subprocess.check_output(git + ['rev-parse', 'HEAD'], text=True, timeout=20).strip()
    published_revision = api('repos/gr3ysbot-tech/gr3y-websites-2026/commits/main')['sha']
    if revision != published_revision:
        raise ValueError('Local source must match the pushed central main branch.')
    updates = []
    for name in changes:
        blob = api(prefix + 'blobs', 'POST', {'content': base64.b64encode(local[name]['content']).decode(), 'encoding': 'base64'})
        updates.append({'path': name, 'mode': remote.get(name, {}).get('mode', '100644'), 'type': 'blob', 'sha': blob['sha']})
    updates += [{'path': name, 'mode': remote[name]['mode'], 'type': 'blob', 'sha': None} for name in removed]
    new_tree = api(prefix + 'trees', 'POST', {'base_tree': base_tree, 'tree': updates})
    commit = api(prefix + 'commits', 'POST', {'message': f'Publish {site} from central websites {revision[:12]}',
                 'tree': new_tree['sha'], 'parents': [head]})
    api(prefix + 'refs/heads/main', 'PATCH', {'sha': commit['sha'], 'force': False})
    result.update(published=True, commit=commit['sha'], source_revision=revision)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('site')
    parser.add_argument('--publish', action='store_true')
    args = parser.parse_args()
    try:
        print(json.dumps(publish(args.site, args.publish), indent=2))
    except (ValueError, KeyError, OSError, subprocess.SubprocessError, UnicodeError):
        print(json.dumps({'error': 'website_publish_failed', 'detail': 'Check the site manifest, clean pushed source, public target, file types and gh access.'}), file=sys.stderr)
        raise SystemExit(1)
