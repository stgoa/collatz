"""Recompute the legacy uniform fixed-word pair receipt with the unmodified legacy code.

Written at the B12-residual-R61-R77 migration. The legacy checker check_uniform_pair.py pins the
SHA-256 of its own note under the legacy name UNIFORM_PAIR_SCOPE.md, which became this node's edited
README.md, so it can no longer pass unchanged. This certificate copies the unmodified uniform_pair.py
and check_uniform_pair.py into a temporary directory with a placeholder note, runs the legacy audit()
there (the 1110-node constructor search, the independent 3401-node enumeration, the 43 candidates
with their lower witnesses and complete upper words, 215 direct instances, 256 small affine paths,
12 domain boundaries and 20 rejections), replaces only the note's hash entry by the one recorded in
the receipt, and requires the result to equal uniform_pair_audit.json exactly. It also requires the
receipt's hashes of the two scripts to match the files in this folder. Nothing is written here.
Standard library. Run from the repository root: python3 <this file>. Exits 1 on any failure.
"""
import hashlib
import importlib
import json
import shutil
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPTS = ("uniform_pair.py", "check_uniform_pair.py")
NOTE = "UNIFORM_PAIR_SCOPE.md"


def fail(message: str) -> int:
    print(f"FAIL: {message}")
    return 1


def main() -> int:
    if sys.flags.optimize:
        return fail("the legacy audit relies on assert statements; run without -O")
    receipt = json.loads((HERE / "uniform_pair_audit.json").read_text(encoding="utf-8"))
    recorded = receipt.get("source_hashes", {})
    for name in SCRIPTS:
        actual = hashlib.sha256((HERE / name).read_bytes()).hexdigest()
        if recorded.get(name) != actual:
            return fail(f"receipt hash of {name} does not match the file in this folder")
    if NOTE not in recorded:
        return fail(f"receipt has no hash entry for {NOTE}")
    with tempfile.TemporaryDirectory() as tmp:
        for name in SCRIPTS:
            shutil.copyfile(HERE / name, Path(tmp) / name)
        (Path(tmp) / NOTE).write_text("placeholder\n", encoding="utf-8")
        sys.path.insert(0, tmp)
        try:
            for mod in ("uniform_pair", "check_uniform_pair"):
                sys.modules.pop(mod, None)
            legacy = importlib.import_module("check_uniform_pair")
            try:
                result = legacy.audit()
            except AssertionError as exc:
                return fail(f"legacy audit assertion failed: {exc}")
        finally:
            sys.path.remove(tmp)
    if set(result.get("source_hashes", {})) != set(recorded):
        return fail("source-hash entries differ from the receipt")
    result["source_hashes"][NOTE] = recorded[NOTE]
    if result != receipt:
        return fail("recomputed audit differs from uniform_pair_audit.json")
    print(f"PASS: legacy uniform-pair audit recomputed; {len(result['constructor']['candidates'])} candidates, "
          "receipt identical apart from the pinned legacy note hash")
    return 0


if __name__ == "__main__":
    sys.exit(main())
