#!/usr/bin/env python3
"""Check that every relative link in the repository's Markdown files resolves to an existing path.

Usage:
    python3 scripts/check_links.py            # report broken links, exit 1 if any
    python3 scripts/check_links.py --quiet    # only the summary line

External links (http, https, mailto) and pure in-page anchors (#...) are not checked.
Code spans and fenced code blocks are skipped, so example links inside them are ignored.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)|!\[[^\]]*\]\(([^)\s]+)\)")
FENCE = re.compile(r"^\s*(```|~~~)")
SKIP_DIRS = {".git", ".lake", "node_modules", "__pycache__"}


def md_files():
    for p in ROOT.rglob("*.md"):
        if not any(part in SKIP_DIRS for part in p.parts):
            yield p


def links(path):
    in_fence = False
    for lineno, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        stripped = re.sub(r"`[^`]*`", "", line)
        for m in LINK.finditer(stripped):
            target = m.group(1) or m.group(2)
            yield lineno, target


def is_external(t):
    return t.startswith(("http://", "https://", "mailto:", "#")) or "://" in t


def main():
    quiet = "--quiet" in sys.argv
    broken, total = [], 0
    for f in sorted(md_files()):
        for lineno, t in links(f):
            if is_external(t):
                continue
            total += 1
            rel = t.split("#", 1)[0]
            if not rel:
                continue
            target = (f.parent / rel).resolve()
            if not target.exists():
                broken.append((f.relative_to(ROOT), lineno, t))
    if not quiet:
        for f, ln, t in broken:
            print(f"{f}:{ln}: {t}")
    print(f"{total} relative links checked, {len(broken)} broken")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
