#!/usr/bin/env python3
"""Validate the repository: node schema, ids, references, status rules, links, Lean hygiene, MAP.md.

    python3 tools/check.py            # run every check; exit 1 on any error
    python3 tools/check.py --fix-map  # also rewrite MAP.md if it is stale

This is the check every pull request must pass. It is fast (seconds) and runs no research code.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_map  # noqa: E402
import nodes  # noqa: E402
import schema as S  # noqa: E402

ROOT = nodes.ROOT
# Trees whose contents are not held to the conventions: frozen history and the migration holding area.
EXEMPT = ("archive/", "_triage/", ".lake/", "lean/.lake/")
ROOT_FILES = {"README.md", "AGENTS.md", "CLAUDE.md", "CONTRIBUTING.md", "LICENSE", "MAP.md",
              ".gitignore", ".gitattributes"}
ROOT_DIRS = {"areas", "sources", "lean", "papers", "conventions", "tools", "archive", ".github", "_triage"}


def exempt(rel: str) -> bool:
    return rel.startswith(EXEMPT)


def check_nodes(g: nodes.Graph, errors: list, warnings: list):
    errors.extend(g.errors)
    seen_ids: dict[str, str] = {}
    seen_alias: dict[str, str] = {}
    for n in g.nodes:
        m, rel = n.meta, n.rel
        kind = m.get("kind")
        if kind not in S.KINDS:
            errors.append(f"{rel}: kind must be one of {', '.join(S.KINDS)}, got {kind!r}")
            continue
        if kind != n.dir_kind:
            errors.append(f"{rel}: kind `{kind}` but the file is in a `{n.dir_kind}` folder")
        for k in S.REQUIRED[kind]:
            if m.get(k) in (None, "", []):
                errors.append(f"{rel}: missing required field `{k}`")
        for k in m:
            if k not in S.ALLOWED:
                errors.append(f"{rel}: unknown field `{k}` (allowed: see conventions/SCHEMA.md)")
        for k in S.LIST_FIELDS:
            if k in m and not isinstance(m[k], list):
                errors.append(f"{rel}: `{k}` must be a list")
        nid = m.get("id", "")
        if not isinstance(nid, str) or not re.match(S.ID_RE, nid) or len(nid) > S.ID_MAX:
            errors.append(f"{rel}: id {nid!r} must be a lowercase kebab-case slug of at most {S.ID_MAX} chars")
        expected = n.path.parent.name if n.path.name == "README.md" else n.path.stem
        if nid != expected:
            errors.append(f"{rel}: id `{nid}` must equal the file or folder name `{expected}`")
        if nid in seen_ids:
            errors.append(f"{rel}: id `{nid}` already used by {seen_ids[nid]}")
        seen_ids[nid] = rel
        st = m.get("status")
        if st not in S.STATUSES[kind]:
            errors.append(f"{rel}: status for a {kind} must be one of {', '.join(S.STATUSES[kind])}, got {st!r}")
        if m.get("created") is not None and not re.match(S.DATE_RE, str(m.get("created"))):
            errors.append(f"{rel}: created must be YYYY-MM-DD")
        for a in n.list_field("aliases"):
            if not re.match(S.ALIAS_RE, str(a)):
                errors.append(f"{rel}: bad alias {a!r}")
            if str(a) in seen_alias:
                errors.append(f"{rel}: alias `{a}` already used by {seen_alias[str(a)]}")
            seen_alias[str(a)] = rel
        for r in n.list_field("reviewed_by"):
            if not isinstance(r, dict):
                errors.append(f"{rel}: each reviewed_by entry is a mapping with `by` and `date`")
                continue
            for k in S.REVIEW_KEYS_REQUIRED:
                if not r.get(k):
                    errors.append(f"{rel}: reviewed_by entry lacks `{k}`")
            for k in r:
                if k not in S.REVIEW_KEYS_ALLOWED:
                    errors.append(f"{rel}: reviewed_by entry has unknown key `{k}`")
        for c in n.list_field("certificates"):
            if n.path.name != "README.md":
                errors.append(f"{rel}: a node with certificates must be a folder `{nid}/README.md`")
                break
            p = n.folder / str(c)
            if not p.is_file() or p.suffix != ".py":
                errors.append(f"{rel}: certificate `{c}` is not a .py file in the node folder")
        if n.path.name == "README.md":
            for p in n.folder.rglob("*"):
                if p.is_dir() and (p / "README.md").exists() and p != n.folder:
                    errors.append(f"{rel}: nested node folder {p.relative_to(ROOT)} is not allowed")
    for a, rel in seen_alias.items():
        if a in seen_ids:
            errors.append(f"{rel}: alias `{a}` collides with a node id")
    for area in sorted((ROOT / "areas").glob("*/")) if (ROOT / "areas").is_dir() else []:
        if not (area / "OVERVIEW.md").is_file():
            errors.append(f"areas/{area.name}: missing OVERVIEW.md")


def check_references(g: nodes.Graph, errors: list, warnings: list):
    res = g.resolver()
    for n in g.nodes:
        for field, kinds in S.TARGETS.items():
            for t in n.list_field(field):
                tgt = res.get(str(t))
                if tgt is None:
                    errors.append(f"{n.rel}: `{field}` names unknown node `{t}`")
                elif tgt.kind not in kinds:
                    errors.append(f"{n.rel}: `{field}` may only name {'/'.join(kinds)} nodes; `{t}` is a {tgt.kind}")
                elif str(t) != tgt.id:
                    errors.append(f"{n.rel}: `{field}` uses alias `{t}`; write the id `{tgt.id}`")
        st, kind = n.status, n.kind
        authors = {_who(a) for a in n.list_field("authors")}
        if st in ("reviewed", "formal") and kind in ("result", "attempt"):
            others = [r for r in n.list_field("reviewed_by") if isinstance(r, dict) and _who(r.get("by", "")) not in authors]
            if st == "reviewed" and not others:
                errors.append(f"{n.rel}: status `reviewed` needs a reviewed_by entry by someone other than the authors")
        if st == "formal":
            if not n.list_field("lean"):
                errors.append(f"{n.rel}: status `formal` needs the `lean` field (fully qualified declarations)")
            if not re.search(r"^## Lean\b", n.body, re.M):
                errors.append(f"{n.rel}: status `formal` needs a `## Lean` section explaining how the Lean statement matches the claim")
        if st == "answered" and not n.list_field("answered_by"):
            errors.append(f"{n.rel}: status `answered` needs `answered_by`")
        if st == "refuted" and not n.meta.get("refuted_by"):
            errors.append(f"{n.rel}: status `refuted` needs `refuted_by` (a node id or a link to the counterexample)")
        if st == "withdrawn" and not n.meta.get("withdrawn_reason"):
            errors.append(f"{n.rel}: status `withdrawn` needs `withdrawn_reason`")
        for t in n.list_field("depends_on") + n.list_field("assumes"):
            tgt = res.get(str(t))
            if tgt and tgt.status in ("refuted", "withdrawn") and st not in ("refuted", "withdrawn"):
                warnings.append(f"{n.rel}: depends on `{tgt.id}`, which is {tgt.status}")
    # Acyclicity of depends_on + assumes.
    edges = {n.id: [res[str(t)].id for t in n.list_field("depends_on") + n.list_field("assumes") if str(t) in res]
             for n in g.nodes}
    color: dict[str, int] = {}

    def visit(u, stack):
        color[u] = 1
        for v in edges.get(u, []):
            if color.get(v) == 1:
                errors.append("dependency cycle: " + " -> ".join(stack[stack.index(v):] + [v]) if v in stack else f"dependency cycle at {v}")
            elif not color.get(v):
                visit(v, stack + [v])
        color[u] = 2

    for u in edges:
        if not color.get(u):
            visit(u, [u])
    # Lean declarations named by nodes must exist.
    decls = lean_declarations()
    for n in g.nodes:
        for d in n.list_field("lean"):
            short = str(d).split(".")[-1]
            if str(d) not in decls and short not in decls:
                errors.append(f"{n.rel}: Lean declaration `{d}` not found under lean/")


def _who(s) -> str:
    """Normalise an author or reviewer string to its name part: 'Claude Fable (Lean lane)' -> 'claude fable'."""
    return re.sub(r"\s*[(<].*$", "", str(s)).strip().lower()


def lean_files():
    lean = ROOT / "lean"
    if not lean.is_dir():
        return []
    return [p for p in lean.rglob("*.lean") if ".lake" not in p.parts]


DECL = re.compile(r"^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+)*"
                  r"(?:theorem|lemma|def|abbrev|structure|inductive|instance|class)\s+([^\s:({\[]+)", re.M)


def lean_declarations() -> set:
    out = set()
    for p in lean_files():
        for m in DECL.finditer(p.read_text(encoding="utf-8", errors="replace")):
            out.add(m.group(1))
            out.add(m.group(1).split(".")[-1])
    return out


def strip_lean_comments(src: str) -> str:
    out, i, depth, n = [], 0, 0, len(src)
    while i < n:
        if src.startswith("/-", i):
            depth += 1
            i += 2
        elif depth and src.startswith("-/", i):
            depth -= 1
            i += 2
        elif depth:
            out.append("\n" if src[i] == "\n" else " ")
            i += 1
        elif src.startswith("--", i):
            j = src.find("\n", i)
            i = n if j < 0 else j
        else:
            out.append(src[i])
            i += 1
    return "".join(out)


def check_lean(errors: list):
    for p in lean_files():
        code = strip_lean_comments(p.read_text(encoding="utf-8", errors="replace"))
        for pat in S.LEAN_FORBIDDEN:
            for m in re.finditer(pat, code, re.M):
                line = code.count("\n", 0, m.start()) + 1
                errors.append(f"{p.relative_to(ROOT)}:{line}: forbidden Lean construct `{m.group(0).strip()}`")


LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def check_links(errors: list):
    for p in sorted(ROOT.rglob("*.md")):
        rel = p.relative_to(ROOT).as_posix()
        if exempt(rel) or "/.lake/" in rel or rel.startswith(".git/"):
            continue
        text = re.sub(r"```.*?```", "", p.read_text(encoding="utf-8"), flags=re.S)
        text = re.sub(r"`[^`\n]*`", "", text)
        for m in LINK.finditer(text):
            target = m.group(1)
            if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                continue
            path = target.split("#", 1)[0]
            if path.startswith("/"):
                errors.append(f"{rel}: absolute link `{target}`; use a relative path")
                continue
            resolved = (p.parent / path).resolve()
            if not resolved.exists():
                errors.append(f"{rel}: broken link `{target}`")
            elif resolved.is_relative_to(ROOT / "_triage"):
                errors.append(f"{rel}: link into the temporary `_triage/` folder: `{target}`")


def top_level_entries() -> list[tuple[str, bool]]:
    """Tracked top-level entries as (name, is_dir); falls back to the filesystem outside git."""
    import subprocess
    try:
        out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True).stdout
        names = {}
        for f in out.splitlines():
            head, sep, _ = f.partition("/")
            names[head] = names.get(head, False) or bool(sep)
        return sorted(names.items())
    except (OSError, subprocess.CalledProcessError):
        return [(p.name, p.is_dir()) for p in ROOT.iterdir() if p.name != ".git"]


def check_root(errors: list):
    for name, is_dir in top_level_entries():
        if not is_dir and name not in ROOT_FILES:
            errors.append(f"{name}: no files at the repository root beyond {', '.join(sorted(ROOT_FILES))}")
        if is_dir and name not in ROOT_DIRS:
            errors.append(f"{name}/: unexpected top-level folder (allowed: {', '.join(sorted(ROOT_DIRS))})")


def main(argv):
    errors: list[str] = []
    warnings: list[str] = []
    g = nodes.load()
    check_nodes(g, errors, warnings)
    check_references(g, errors, warnings)
    check_lean(errors)
    check_links(errors)
    check_root(errors)
    if not errors:
        fresh = build_map.render(g)
        current = (ROOT / "MAP.md").read_text(encoding="utf-8") if (ROOT / "MAP.md").exists() else ""
        if fresh != current:
            if "--fix-map" in argv:
                (ROOT / "MAP.md").write_text(fresh, encoding="utf-8")
                print("MAP.md rewritten")
            else:
                errors.append("MAP.md is stale: run `python3 tools/build_map.py`")
    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    print(f"{len(g.nodes)} nodes, {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
