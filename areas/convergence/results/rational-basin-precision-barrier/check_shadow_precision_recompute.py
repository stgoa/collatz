"""Recompute this node's legacy receipt, apart from the hashes of edited notes. It reruns the exact Python classification of all 1,732,883 canonical origins -u/7153 with 7153 < u < 7277133 (19 hits on c0, every first-hit score at least 1, no cap), the c0 cycle, the inverse-ray checks, the 306 positive inverse words and the 14 rejections. The C++ cross-check is not run (it needs a compiler).

Written at the B13-residual-R78-R94 migration (on tools/legacy_replay.py), because no legacy check of
this node passes any more. The legacy checker check_shadow_precision.py pins the SHA-256 of shadow_precision/SHADOW_PRECISION.md, phi_exit_control/PHI_EXIT_CONTROL.md, which the
migration edited into node READMEs, so the unmodified checker can no longer reproduce its receipt.
This certificate rebuilds the pre-migration layout in a temporary directory from
tools/legacy_paths.json, puts a placeholder at each of those note paths, imports the unmodified
legacy checker there and runs its audit, and requires the result to equal the committed receipt
shadow_precision_audit.json after removing only the hash entries of those notes (dictionary keys ending in .md).
Every other recorded value, including the hashes of all pinned code and data files, must match, and
every copied file must be unchanged afterwards. Nothing in the repository is written.
Run from the repository root: python3 <this file>. Exits 1 on any failure.
"""
import filecmp
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import legacy_replay  # noqa: E402

CHECKER = 'experiments/residual_progress/shadow_precision/check_shadow_precision.py'
RECEIPT = 'experiments/residual_progress/shadow_precision/shadow_precision_audit.json'
NOTES = ['experiments/residual_progress/shadow_precision/SHADOW_PRECISION.md', 'experiments/residual_progress/phi_exit_control/PHI_EXIT_CONTROL.md']
AUDIT_ARGS = 'none'  # "none": audit(); "stored": audit(stored receipt)

DRIVER = r'''
import json, sys
sys.path.insert(0, ".")
import importlib
checker = importlib.import_module(sys.argv[1])
stored = json.loads(open(sys.argv[2], encoding="utf-8").read())
result = checker.audit(stored) if sys.argv[3] == "stored" else checker.audit()
result = json.loads(json.dumps(result))
def strip(x):
    if isinstance(x, dict):
        return {k: strip(v) for k, v in x.items() if not (isinstance(k, str) and k.endswith(".md"))}
    if isinstance(x, list):
        return [strip(v) for v in x]
    return x
removed = []
def count(x):
    if isinstance(x, dict):
        for k, v in x.items():
            if isinstance(k, str) and k.endswith(".md"):
                removed.append(k)
            count(v)
    elif isinstance(x, list):
        for v in x:
            count(v)
count(stored)
if strip(result) != strip(stored):
    keys = sorted(k for k in set(result) | set(stored) if strip(result.get(k)) != strip(stored.get(k)))
    print("FAIL: recomputed audit differs from the receipt in", keys)
    sys.exit(1)
print("PASS: receipt reproduced apart from", len(removed), "note hash(es):", ", ".join(sorted(removed)))
'''


def main() -> int:
    mapping = legacy_replay.load_map()
    for path in [CHECKER, RECEIPT]:
        if path not in mapping:
            print(f"FAIL {path}: not in tools/legacy_paths.json")
            return 1
    env = {k: v for k, v in os.environ.items() if k not in ("PYTHONOPTIMIZE", "PYTHONPATH")}
    with tempfile.TemporaryDirectory() as name:
        tmp = Path(name)
        copied = legacy_replay.build(tmp, mapping)
        for note in NOTES:
            dest = tmp / note
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text("placeholder for a legacy note edited at the migration\n", encoding="utf-8")
            copied.pop(dest, None)
        folder = (tmp / CHECKER).parent
        proc = subprocess.run([sys.executable, "-B", "-c", DRIVER, Path(CHECKER).stem,
                               str(tmp / RECEIPT), AUDIT_ARGS], cwd=folder, env=env,
                              capture_output=True, text=True, timeout=1800)
        out = (proc.stdout + proc.stderr).strip().splitlines()
        changed = [str(d.relative_to(tmp)) for d, s in copied.items()
                   if not d.is_file() or not filecmp.cmp(s, d, shallow=False)]
    for line in out[-3:]:
        print(line)
    if changed:
        print("FAIL: files changed during the run:", ", ".join(changed))
        return 1
    return proc.returncode


if __name__ == "__main__":
    sys.exit(main())
