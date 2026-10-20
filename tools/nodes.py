#!/usr/bin/env python3
"""Load the repository's knowledge graph: every node file and its frontmatter.

A node is one Markdown file that starts with a YAML frontmatter block. The schema is in
conventions/SCHEMA.md. Nodes live in:

    areas/<area>/results/    kind: result
    areas/<area>/attempts/   kind: attempt
    areas/<area>/questions/  kind: question
    sources/                 kind: source

A node is either `<id>.md` or, when it has attached files, `<id>/README.md`.

Standard library only. The frontmatter parser accepts a deliberately small YAML subset
(documented in conventions/SCHEMA.md §5) so that every tool and every agent reads it the same way.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

KIND_DIRS = {"results": "result", "attempts": "attempt", "questions": "question"}


class FrontmatterError(ValueError):
    pass


# ---------------------------------------------------------------- YAML subset parser

def _scalar(text: str, where: str):
    t = text.strip()
    if t == "":
        return None
    if t[0] in "\"'":
        if len(t) < 2 or t[-1] != t[0]:
            raise FrontmatterError(f"{where}: unterminated quoted string: {t}")
        body = t[1:-1]
        return body.replace('\\"', '"') if t[0] == '"' else body.replace("''", "'")
    if t.startswith("["):
        if not t.endswith("]"):
            raise FrontmatterError(f"{where}: unterminated inline list: {t}")
        inner = t[1:-1].strip()
        if not inner:
            return []
        return [_scalar(p, where) for p in _split_commas(inner, where)]
    if t.startswith("{"):
        raise FrontmatterError(f"{where}: inline mappings are not allowed; use a block list of mappings")
    if t in ("true", "false"):
        return t == "true"
    if re.fullmatch(r"-?\d+", t):
        return int(t)
    if " #" in t:
        t = t.split(" #", 1)[0].rstrip()
    return t


def _split_commas(s: str, where: str):
    out, cur, q = [], "", None
    for ch in s:
        if q:
            cur += ch
            if ch == q:
                q = None
        elif ch in "\"'":
            q = ch
            cur += ch
        elif ch == ",":
            out.append(cur)
            cur = ""
        else:
            cur += ch
    if q:
        raise FrontmatterError(f"{where}: unterminated quote in list")
    out.append(cur)
    return [p for p in (x.strip() for x in out)]


KEY = re.compile(r"^([a-z_][a-z0-9_]*):(?:\s+(.*))?$")


def parse_frontmatter(text: str, where: str = "<frontmatter>") -> dict:
    """Parse the supported YAML subset into a dict.

    Supported: `key: scalar`, `key: "quoted"`, `key: [a, b]`, folded/literal blocks (`key: >` or
    `key: |` followed by lines indented by two spaces), and block lists (`key:` followed by
    `  - item` lines), whose items are scalars or flat mappings (`  - a: 1` / `    b: 2`).
    """
    lines = text.split("\n")
    data: dict = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        if line.startswith(" "):
            raise FrontmatterError(f"{where}: line {i + 1}: unexpected indentation: {line!r}")
        m = KEY.match(line.rstrip())
        if not m:
            raise FrontmatterError(f"{where}: line {i + 1}: expected `key: value`: {line!r}")
        key, rest = m.group(1), (m.group(2) or "").strip()
        if key in data:
            raise FrontmatterError(f"{where}: duplicate key `{key}`")
        i += 1
        if rest in (">", "|"):
            block = []
            while i < len(lines) and (lines[i].startswith("  ") or not lines[i].strip()):
                block.append(lines[i][2:] if lines[i].strip() else "")
                i += 1
            while block and not block[-1]:
                block.pop()
            if rest == "|":
                data[key] = "\n".join(block)
            else:
                paras, cur = [], []
                for b in block:
                    if b:
                        cur.append(b.strip())
                    elif cur:
                        paras.append(" ".join(cur))
                        cur = []
                if cur:
                    paras.append(" ".join(cur))
                data[key] = "\n\n".join(paras)
        elif rest == "":
            items = []
            while i < len(lines) and (lines[i].startswith("  ") or not lines[i].strip()):
                ln = lines[i]
                i += 1
                if not ln.strip():
                    continue
                if ln.startswith("  - "):
                    body = ln[4:]
                    km = KEY.match(body.rstrip())
                    if km and not body.lstrip().startswith(("\"", "'")):
                        item = {km.group(1): _scalar(km.group(2) or "", where)}
                        while i < len(lines) and lines[i].startswith("    ") and not lines[i].startswith("    - "):
                            km2 = KEY.match(lines[i][4:].rstrip())
                            if not km2:
                                raise FrontmatterError(f"{where}: line {i + 1}: bad mapping line {lines[i]!r}")
                            if km2.group(1) in item:
                                raise FrontmatterError(f"{where}: duplicate key `{km2.group(1)}` in list item")
                            item[km2.group(1)] = _scalar(km2.group(2) or "", where)
                            i += 1
                        items.append(item)
                    else:
                        items.append(_scalar(body, where))
                else:
                    raise FrontmatterError(f"{where}: line {i}: expected `  - item` under `{key}:`")
            data[key] = items
        else:
            data[key] = _scalar(rest, where)
    return data


def split_node(text: str, where: str):
    """Return (frontmatter dict, body) of a node file."""
    if not text.startswith("---\n"):
        raise FrontmatterError(f"{where}: a node must start with a `---` frontmatter line")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise FrontmatterError(f"{where}: frontmatter is not closed by a `---` line")
    return parse_frontmatter(text[4:end], where), text[end + 5:]


# ---------------------------------------------------------------- graph

@dataclass
class Node:
    path: Path            # the node file, absolute
    meta: dict
    body: str
    area: str | None      # None for sources
    dir_kind: str         # kind implied by the folder

    @property
    def id(self) -> str:
        return self.meta.get("id", "")

    @property
    def kind(self) -> str:
        return self.meta.get("kind", "")

    @property
    def status(self) -> str:
        return self.meta.get("status", "")

    @property
    def rel(self) -> str:
        return self.path.relative_to(ROOT).as_posix()

    @property
    def folder(self) -> Path:
        """Folder holding the node's attached files (the node's own folder, or its parent)."""
        return self.path.parent

    def list_field(self, name: str) -> list:
        v = self.meta.get(name)
        if v is None:
            return []
        return v if isinstance(v, list) else [v]


@dataclass
class Graph:
    nodes: list[Node] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    def by_id(self) -> dict[str, Node]:
        return {n.id: n for n in self.nodes if n.id}

    def resolver(self) -> dict[str, Node]:
        """Map ids and aliases to nodes."""
        r = self.by_id()
        for n in self.nodes:
            for a in n.list_field("aliases"):
                r.setdefault(str(a), n)
        return r


def node_files(root: Path = ROOT):
    """Yield (path, area, dir_kind) for every node file in the tree."""
    areas = root / "areas"
    if areas.is_dir():
        for area in sorted(p for p in areas.iterdir() if p.is_dir()):
            for dname, kind in KIND_DIRS.items():
                d = area / dname
                if not d.is_dir():
                    continue
                for p in sorted(d.iterdir()):
                    if p.is_file() and p.suffix == ".md" and p.name != "README.md":
                        yield p, area.name, kind
                    elif p.is_dir():
                        yield p / "README.md", area.name, kind
    src = root / "sources"
    if src.is_dir():
        for p in sorted(src.iterdir()):
            if p.is_file() and p.suffix == ".md" and p.name != "README.md":
                yield p, None, "source"
            elif p.is_dir():
                yield p / "README.md", None, "source"


def load(root: Path = ROOT) -> Graph:
    g = Graph()
    for path, area, kind in node_files(root):
        rel = path.relative_to(root).as_posix()
        if not path.is_file():
            g.errors.append(f"{rel}: node folder has no README.md")
            continue
        try:
            meta, body = split_node(path.read_text(encoding="utf-8"), rel)
        except FrontmatterError as e:
            g.errors.append(str(e))
            continue
        g.nodes.append(Node(path, meta, body, area, kind))
    return g
