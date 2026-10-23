from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1 = 0
        self.main = 0
        self.redirect = False
        self.refs = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.h1 += tag == 'h1'
        self.main += tag == 'main'
        if tag == 'meta' and attrs.get('http-equiv', '').lower() == 'refresh':
            self.redirect = True
        for key in ('href', 'src'):
            if attrs.get(key):
                self.refs.append((tag, key, attrs[key]))


def check():
    failures = []
    pages = 0
    for site in sorted((ROOT / 'sites').iterdir()):
        if not site.is_dir():
            continue
        for path in sorted(site.rglob('*.html')):
            page = Page()
            page.feed(path.read_text(encoding='utf-8'))
            pages += 1
            relative = path.relative_to(ROOT)
            if page.redirect:
                continue
            if page.h1 != 1 or page.main != 1:
                failures.append(f'{relative}: expected one h1 and main; got {page.h1}, {page.main}')
            for tag, key, ref in page.refs:
                url = urlsplit(ref)
                if tag == 'img' and ref == '#':
                    failures.append(f'{relative}: image source is a placeholder')
                if url.scheme or url.netloc or not url.path:
                    continue
                target = site / unquote(url.path.lstrip('/')) if url.path.startswith('/') else path.parent / unquote(url.path)
                if target.is_dir():
                    target /= 'index.html'
                if not target.exists():
                    failures.append(f'{relative}: missing {key}={ref}')
    for failure in failures:
        print(failure)
    print(f'{pages} HTML files checked; {len(failures)} failures. External destinations are not checked.')
    return bool(failures)

if __name__ == '__main__':
    raise SystemExit(check())
