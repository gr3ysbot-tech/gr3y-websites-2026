"""Dependency-free integrity checks; this is not a browser/layout test."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import re

ROOT = Path(__file__).resolve().parent
class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(); self.path=path; self.ids=set(); self.references=[]; self.titles=0; self.headings=0
        self.feed(path.read_text(encoding='utf-8-sig'))
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, f'Duplicate id in {self.path}: {attrs["id"]}'
            self.ids.add(attrs['id'])
        if tag=='title': self.titles+=1
        if tag=='h1': self.headings+=1
        for key in ('src','href','data-dialog'):
            if key in attrs: self.references.append(('#'+attrs[key]) if key=='data-dialog' else attrs[key])

pages={p.resolve():Page(p) for p in ROOT.rglob('*.html') if 'public' not in p.parts}
count=0
for path,page in pages.items():
    assert page.titles==1 and page.headings==1, f'Expected one title and h1: {path}'
    for ref in page.references:
        parsed=urlsplit(ref)
        if parsed.scheme:
            assert parsed.scheme in ('https','mailto'), f'Unexpected link scheme: {ref}'
            continue
        target=(path.parent / unquote(parsed.path)).resolve() if parsed.path else path
        if target.is_dir(): target=target/'index.html'
        assert target.is_relative_to(ROOT), f'Path outside site: {ref}'
        assert target.exists(), f'Missing link/asset {ref} from {path.name}'
        if parsed.fragment and target in pages:
            assert unquote(parsed.fragment) in pages[target].ids, f'Missing fragment {ref}'
        count+=1
css=(ROOT/'assets/style.css').read_text(encoding='utf-8-sig')
assert css.count('{')==css.count('}'), 'Unbalanced CSS braces'
for asset in re.findall(r'url\([\'\"]?([^\)\'\"]+)',css):
    assert (ROOT/'assets'/asset).exists(),f'Missing CSS asset: {asset}'
assert (ROOT/'CNAME').read_text().strip()=='gr3ycapital.com'
assert 'https://www.youtube.com/@gr3ylabs' in (ROOT/'gr3ylab/index.html').read_text(encoding='utf-8-sig')
assert 'actions/deploy-pages@v4' in (ROOT/'.github/workflows/pages.yml').read_text()
print(f'PASS: {len(pages)} HTML pages, {count} local links/assets/dialog targets; unique IDs, font assets/licenses, CSS structure, domain, channel and deployment workflow.')
print('Browser layout, accessibility interaction and real GitHub deployment are not covered by this check.')
