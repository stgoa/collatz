#!/usr/bin/env python3
"""Run the certificate scripts of nodes, only where something changed.

A certificate is a script listed in a node's `certificates:` field. It proves a finite step of the
node's argument, so it must exit 0 when run from the repository root. It is re-run only when the
node's folder changes: the inputs of a frozen certificate do not change, so neither does its result.

    python3 tools/run_certificates.py --changed origin/main   # nodes touched since that ref (CI)
    python3 tools/run_certificates.py --node <id> [<id> ...]  # named nodes
    python3 tools/run_certificates.py --all                   # every certificate (slow; manual only)

Exploration scripts (anything not listed under `certificates:`) are never run by this tool.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import nodes  # noqa: E402

ROOT = nodes.ROOT


def changed_files(base: str) -> list[str]:
    out = subprocess.run(["git", "diff", "--name-only", f"{base}...HEAD"], cwd=ROOT,
                         capture_output=True, text=True, check=True).stdout
    return [l for l in out.splitlines() if l]


def main():
    ap = argparse.ArgumentParser()
    g_ = ap.add_mutually_exclusive_group(required=True)
    g_.add_argument("--changed", metavar="BASE_REF")
    g_.add_argument("--node", nargs="+")
    g_.add_argument("--all", action="store_true")
    ap.add_argument("--timeout", type=int, default=1800, help="seconds per script")
    a = ap.parse_args()

    g = nodes.load()
    with_certs = [n for n in g.nodes if n.list_field("certificates")]
    if a.all:
        todo = with_certs
    elif a.node:
        res = g.resolver()
        missing = [x for x in a.node if x not in res]
        if missing:
            print(f"unknown node(s): {', '.join(missing)}")
            return 2
        todo = [res[x] for x in a.node]
    else:
        files = changed_files(a.changed)
        todo = [n for n in with_certs
                if any(f.startswith(n.folder.relative_to(ROOT).as_posix() + "/") for f in files)]
    failures = 0
    for n in todo:
        for c in n.list_field("certificates"):
            script = (n.folder / str(c)).relative_to(ROOT).as_posix()
            t0 = time.time()
            try:
                p = subprocess.run([sys.executable, script], cwd=ROOT, capture_output=True, text=True,
                                   timeout=a.timeout)
                ok, tail = p.returncode == 0, (p.stdout + p.stderr).strip().splitlines()[-3:]
            except subprocess.TimeoutExpired:
                ok, tail = False, [f"timed out after {a.timeout}s"]
            failures += not ok
            print(f"{'PASS' if ok else 'FAIL'} {n.id}: {script} ({time.time() - t0:.0f}s)")
            if not ok:
                for line in tail:
                    print(f"    {line}")
    print(f"{len(todo)} node(s) checked, {failures} certificate failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
