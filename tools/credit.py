#!/usr/bin/env python3
"""Compute contribution credit from the knowledge graph. The policy is conventions/CREDIT.md.

    python3 tools/credit.py               # contributor table
    python3 tools/credit.py --node <id>   # how one node's value is computed and shared

Credit is computed, never assigned by hand. Each node has a value: a base value for its kind and status,
plus a share of the value of every node that depends on it. The value is split among the node's authors
and independent reviewers. The formula is version 1; change it only by a pull request against this file
and conventions/CREDIT.md.
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import nodes  # noqa: E402

FORMULA_VERSION = 1

# Base value by kind and status. Refuted and withdrawn nodes keep their history but earn nothing;
# whoever refuted them earns through their own node or review.
BASE = {
    "result": {"proposed": 0.25, "written": 1.0, "reviewed": 1.5, "formal": 2.0},
    "attempt": {"proposed": 0.25, "written": 0.5, "reviewed": 0.75, "formal": 1.0},
    "question": {"open": 0.25, "answered": 0.25},
}
FLOW = 0.5            # fraction of a dependent's value that flows back to what it depends on
REVIEW_SHARE = 0.25   # share of a node's value that goes to its independent reviewers, when it has any

# Contributors who were AI agents directed by a person, recorded before the "(directed by …)" convention
# of conventions/CREDIT.md §4 existed. Every lane that worked on this repository before 2026-10-20 was
# directed by the repository owner (archive/HISTORY.md).
LEGACY_DIRECTION = {
    name: "Santiago Armstrong"
    for name in ("ChatGPT main lane", "ChatGPT handoff conversation", "Claude side lane", "Claude Lean lane",
                 "Claude PR1 lane", "Claude audit lane", "Claude explicit-Tao lane")
}

DIRECTED = re.compile(r"directed by ([^;,)]+)", re.I)


def identity(entry) -> str:
    """The contributor named by an authors/reviewed_by entry: the part before any parentheses."""
    return re.sub(r"\s*[(<].*$", "", str(entry)).strip()


def accountable(entry) -> str:
    """The person accountable for an entry: '(…; directed by X)' if given, else the legacy table, else itself."""
    m = DIRECTED.search(str(entry))
    if m:
        return m.group(1).strip()
    name = identity(entry)
    return LEGACY_DIRECTION.get(name, name)


def node_values(g: nodes.Graph) -> dict[str, float]:
    """value(n) = base(n) + FLOW * sum over dependents d of value(d) / (number of nodes d builds on)."""
    by_id = g.by_id()
    builds_on = {n.id: [str(t) for t in n.list_field("depends_on") + n.list_field("assumes")
                        if str(t) in by_id and by_id[str(t)].kind != "source"] for n in g.nodes}
    dependents = defaultdict(list)
    for nid, targets in builds_on.items():
        for t in targets:
            dependents[t].append(nid)
    memo: dict[str, float] = {}

    def value(nid: str, stack: frozenset = frozenset()) -> float:
        if nid in memo:
            return memo[nid]
        n = by_id[nid]
        v = BASE.get(n.kind, {}).get(n.status, 0.0)
        for d in dependents.get(nid, ()):
            if d not in stack:                      # tools/check.py rejects cycles; guard anyway
                v += FLOW * value(d, stack | {nid}) / len(builds_on[d])
        memo[nid] = v
        return v

    for n in g.nodes:
        value(n.id)
    return memo


def shares(n: nodes.Node, value: float) -> dict[str, float]:
    """Split one node's value among its contributors (raw entries, so accountability can be resolved)."""
    authors = n.list_field("authors")
    author_ids = {identity(a) for a in authors}
    reviewers = [r.get("by") for r in n.list_field("reviewed_by")
                 if isinstance(r, dict) and r.get("by") and identity(r.get("by")) not in author_ids]
    # One share per distinct reviewer, however many reviews they wrote.
    seen, unique = set(), []
    for r in reviewers:
        if identity(r) not in seen:
            seen.add(identity(r))
            unique.append(r)
    out: dict[str, float] = defaultdict(float)
    author_part = value * (1 - REVIEW_SHARE) if unique else value
    for a in authors:
        out[str(a)] += author_part / len(authors)
    for r in unique:
        out[str(r)] += value * REVIEW_SHARE / len(unique)
    return out


def table(g: nodes.Graph):
    """Rows (contributor, credit, nodes authored, reviews given) and the accountable-person rollup."""
    values = node_values(g)
    credit, authored, reviews = defaultdict(float), defaultdict(int), defaultdict(int)
    person = defaultdict(float)
    for n in g.nodes:
        for entry, c in shares(n, values[n.id]).items():
            credit[identity(entry)] += c
            person[accountable(entry)] += c
        for a in n.list_field("authors"):
            authored[identity(a)] += 1
        for r in n.list_field("reviewed_by"):
            if isinstance(r, dict) and r.get("by"):
                reviews[identity(r["by"])] += 1
    total = sum(credit.values()) or 1.0
    rows = sorted(((name, c / total, authored[name], reviews[name]) for name, c in credit.items()),
                  key=lambda r: (-r[1], r[0]))
    people = sorted(((name, c / total) for name, c in person.items()), key=lambda r: (-r[1], r[0]))
    return rows, people


def render(g: nodes.Graph) -> str:
    """The Contributors section of MAP.md."""
    rows, people = table(g)
    out = ["## Contributors\n",
           f"Credit computed by [`tools/credit.py`](tools/credit.py) (formula v{FORMULA_VERSION}) under "
           "[`conventions/CREDIT.md`](conventions/CREDIT.md): each node's value (its kind and status, plus a "
           "share of everything built on it) is split among its authors and independent reviewers.\n",
           "| Contributor | Share of credit | Nodes authored | Reviews given |", "|---|---|---|---|"]
    for name, share, a, r in rows:
        out.append(f"| {name} | {100 * share:.1f}% | {a} | {r} |")
    out += ["", "**By accountable person** (agents are credited to the person who directed them; "
            "[`conventions/CREDIT.md`](conventions/CREDIT.md) §4):\n",
            "| Person | Share of credit |", "|---|---|"]
    for name, share in people:
        out.append(f"| {name} | {100 * share:.1f}% |")
    return "\n".join(out) + "\n"


def explain(g: nodes.Graph, nid: str) -> int:
    res = g.resolver()
    if nid not in res:
        print(f"unknown node: {nid}")
        return 2
    n = res[nid]
    values = node_values(g)
    base = BASE.get(n.kind, {}).get(n.status, 0.0)
    print(f"{n.id} ({n.kind}, {n.status}): value {values[n.id]:.3f} = base {base:.2f} "
          f"+ {values[n.id] - base:.3f} flowing back from nodes built on it")
    for entry, c in sorted(shares(n, values[n.id]).items(), key=lambda x: -x[1]):
        print(f"  {c:.3f}  {entry}")
    return 0


def main(argv):
    g = nodes.load()
    if g.errors:
        print("\n".join(g.errors))
        return 1
    if argv[:1] == ["--node"] and len(argv) == 2:
        return explain(g, argv[1])
    print(render(g))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
