#!/usr/bin/env python3
"""Check the Lean receipts in lean/receipts/ against the current sources, without building anything.

    python3 tools/check_lean_receipts.py

Checks:
1. every line "<sha256>  <path>" of lean/receipts/<File>.sha256.txt matches the current hash of
   lean/<basename of path> (receipts written before the 2026-10-19 restructure name the old directory
   experiments/lean_lane/, so only the file name is used);
2. every "source sha256: <hash>" header in lean/receipts/<File>.build.txt and <File>.axioms.txt
   matches the current hash of lean/<File>.lean;
3. every `#print axioms` line in lean/receipts/*.axioms.txt names only the standard axioms
   propext, Classical.choice and Quot.sound (or "does not depend on any axioms").

Lean hygiene (sorry, admit, axiom declarations, ...) is scanned by tools/check.py, not here.
Ported from the legacy scripts/check_lean_receipts.py. Standard library only; exits 1 on any problem.
"""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEAN = ROOT / "lean"
RECEIPTS = LEAN / "receipts"
STANDARD = {"propext", "Classical.choice", "Quot.sound"}
DEPENDS = re.compile(r"depends on axioms: \[([^\]]*)\]")
HEADER = re.compile(r"^source sha256: ([0-9a-f]{64})\s*$", re.M)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    problems: list[str] = []
    hashes = headers = axiom_lines = 0
    for receipt in sorted(RECEIPTS.glob("*.sha256.txt")):
        for line in receipt.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            expected, path = line.split(maxsplit=1)
            source = LEAN / Path(path.strip().lstrip("*")).name
            hashes += 1
            if not source.exists():
                problems.append(f"{receipt.name}: {source.name} missing")
            elif sha(source) != expected:
                problems.append(f"{receipt.name}: {source.name} differs from its receipt")
    for receipt in sorted(list(RECEIPTS.glob("*.build.txt")) + list(RECEIPTS.glob("*.axioms.txt"))):
        stem = receipt.name.split(".")[0]
        text = receipt.read_text(encoding="utf-8")
        for m in HEADER.finditer(text):
            source = LEAN / f"{stem}.lean"
            headers += 1
            if not source.exists():
                problems.append(f"{receipt.name}: {source.name} missing")
            elif sha(source) != m.group(1):
                problems.append(f"{receipt.name}: header hash differs from {source.name}")
        if receipt.name.endswith(".axioms.txt"):
            if "sorryAx" in text:
                problems.append(f"{receipt.name}: mentions sorryAx")
            for m in DEPENDS.finditer(text):
                axiom_lines += 1
                extra = {a.strip() for a in m.group(1).split(",") if a.strip()} - STANDARD
                if extra:
                    problems.append(f"{receipt.name}: non-standard axioms {sorted(extra)}")
    if hashes == 0:
        problems.append("no lean/receipts/*.sha256.txt found")
    for p in problems:
        print(p)
    print(f"lean receipts: {hashes} source hashes, {headers} header hashes, "
          f"{axiom_lines} axiom lines checked, {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
