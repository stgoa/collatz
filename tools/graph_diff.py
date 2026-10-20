#!/usr/bin/env python3
"""Summarise how a pull request changes the knowledge graph, as Markdown (posted as a PR comment).

    python3 tools/graph_diff.py origin/main

Lists added and removed nodes, status changes, and, for every changed node, the nodes that depend on
it, directly or transitively. Reviewers start from this summary.
"""
from __future__ import annotations

import io
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import nodes  # noqa: E402

ROOT = nodes.ROOT


def load_at(ref: str) -> nodes.Graph:
    paths = [p for p in ("areas", "sources") if subprocess.run(
        ["git", "cat-file", "-e", f"{ref}:{p}"], cwd=ROOT, capture_output=True).returncode == 0]
    tmp = Path(tempfile.mkdtemp())
    if paths:
        blob = subprocess.run(["git", "archive", ref, *paths], cwd=ROOT, capture_output=True, check=True).stdout
        with tarfile.open(fileobj=io.BytesIO(blob)) as tar:
            try:
                tar.extractall(tmp, filter="data")
            except TypeError:            # Python without extraction filters
                tar.extractall(tmp)
    g = nodes.load(tmp)
    for n in g.nodes:
        n.path = ROOT / n.path.relative_to(tmp)
    return g


def dependents(g: nodes.Graph, ids: set) -> dict[str, set]:
    rev: dict[str, set] = {}
    for n in g.nodes:
        for t in n.list_field("depends_on") + n.list_field("assumes"):
            rev.setdefault(str(t), set()).add(n.id)
    out = {}
    for i in ids:
        seen, todo = set(), [i]
        while todo:
            for d in rev.get(todo.pop(), ()):
                if d not in seen:
                    seen.add(d)
                    todo.append(d)
        out[i] = seen
    return out


def main(base: str) -> int:
    old, new = load_at(base), nodes.load()
    o, n = old.by_id(), new.by_id()
    added = sorted(set(n) - set(o))
    removed = sorted(set(o) - set(n))
    status = sorted(i for i in set(o) & set(n) if o[i].status != n[i].status)
    edited = sorted(i for i in set(o) & set(n)
                    if (o[i].meta, o[i].body) != (n[i].meta, n[i].body) and i not in status)
    lines = ["### Knowledge-graph changes", ""]
    if not (added or removed or status or edited):
        lines.append("No node changed.")
    for i in added:
        lines.append(f"- **added** `{i}` ({n[i].kind}, {n[i].status}): {n[i].meta.get('title', '')}")
    for i in removed:
        lines.append(f"- **removed** `{i}` ({o[i].kind}). Nodes are normally refuted or withdrawn, not deleted.")
    for i in status:
        lines.append(f"- **status** `{i}`: {o[i].status} → **{n[i].status}**")
    for i in edited:
        lines.append(f"- **edited** `{i}` ({n[i].status})")
    deps = dependents(new, set(status) | set(edited) | set(removed))
    affected = {k: v for k, v in deps.items() if v}
    if affected:
        lines += ["", "**Dependents to re-check:**"]
        for k, v in sorted(affected.items()):
            lines.append(f"- `{k}` → {', '.join(f'`{d}`' for d in sorted(v))}")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "origin/main"))
