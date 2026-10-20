#!/usr/bin/env python3
"""Run legacy scripts at their new paths from the repository root, with a timeout (migration helper).

    python3 _triage/try_script.py path/to/check_a.py [path/to/check_b.py ...] [--timeout 600]

Prints PASS/FAIL/TIMEOUT per script with the last output lines; exit code is the number of non-passes.
"""
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
args = sys.argv[1:]
timeout = 600
if "--timeout" in args:
    i = args.index("--timeout")
    timeout = int(args[i + 1])
    del args[i:i + 2]
bad = 0
for s in args:
    t0 = time.time()
    try:
        p = subprocess.run([sys.executable, s], cwd=ROOT, capture_output=True, text=True, timeout=timeout)
        verdict = "PASS" if p.returncode == 0 else f"FAIL(rc={p.returncode})"
        tail = (p.stdout + p.stderr).strip().splitlines()[-3:]
    except subprocess.TimeoutExpired:
        verdict, tail = "TIMEOUT", []
    bad += verdict != "PASS"
    print(f"{verdict} {s} ({time.time() - t0:.0f}s)")
    for line in tail:
        print(f"    {line[:200]}")
sys.exit(bad)
