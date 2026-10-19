#!/usr/bin/env python3
"""Check the Lean sources against their receipts, without building them.

For every lean/receipts/<File>.sha256.txt, each line "<sha256>  <path>" must match the current hash of
lean/<basename of path>. Receipts written before the 2026-10-19 restructure name the old directory
(experiments/lean_lane/), so only the file name is used.

Every lean/*.lean source is also scanned, outside comments, for constructs that would weaken a proof:
sorry, admit, native_decide, axiom declarations, unsafe, implemented_by, extern and opaque.

    python3 scripts/check_lean_receipts.py
"""
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEAN = ROOT / "lean"
FORBIDDEN = re.compile(r"\bsorry\b|\badmit\b|\bnative_decide\b|^\s*(?:private\s+|protected\s+)?axiom\b|"
                       r"\bunsafe\b|\bimplemented_by\b|@\[\s*extern\b|^\s*opaque\b", re.M)


def strip_comments(src):
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


def main():
    problems, checked = [], 0
    for receipt in sorted((LEAN / "receipts").glob("*.sha256.txt")):
        for line in receipt.read_text().splitlines():
            if not line.strip():
                continue
            expected, path = line.split(maxsplit=1)
            source = LEAN / Path(path.strip().lstrip("*")).name
            checked += 1
            if not source.exists():
                problems.append(f"{receipt.name}: {source.name} missing")
            elif hashlib.sha256(source.read_bytes()).hexdigest() != expected:
                problems.append(f"{receipt.name}: {source.name} differs from its receipt")
    for source in sorted(LEAN.glob("*.lean")):
        for m in FORBIDDEN.finditer(strip_comments(source.read_text(encoding="utf-8"))):
            problems.append(f"{source.name}: forbidden construct '{m.group(0).strip()}'")
    for p in problems:
        print(p)
    print(f"{checked} receipt hashes checked, {len(list(LEAN.glob('*.lean')))} sources scanned, "
          f"{len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
