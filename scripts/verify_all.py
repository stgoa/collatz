#!/usr/bin/env python3
"""Reproduce the finite audits in temporary storage; no universal theorem check."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "collatz_research_20261017"
BUNDLE = RESEARCH / "collatz_packet_currents"
ARCHIVE_SHA = "025c8fafe25940951fe408b32b1ec806259725a6b4f8855d9f2b022911fe5447"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def run(command, cwd):
    result = subprocess.run(command, cwd=cwd, text=True, capture_output=True,
                            timeout=180, check=False)
    require(result.returncode == 0,
            f"Command failed: {command!r}\n{result.stdout}\n{result.stderr}")
    return result.stdout


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cpp", action="store_true", help="require the independent C++17 checks")
    args = parser.parse_args()
    require(not sys.flags.optimize, "Run without -O or PYTHONOPTIMIZE; checks use assertions.")
    archive = ROOT / "collatz_packet_currents_bundle.zip"
    require(hashlib.sha256(archive.read_bytes()).hexdigest() == ARCHIVE_SHA,
            "Original archive checksum mismatch")
    entries = (BUNDLE / "SHA256SUMS.txt").read_text().splitlines()
    for line in entries:
        expected, name = line.split(maxsplit=1)
        path = (BUNDLE / name.lstrip("*")).resolve()
        require(path.is_relative_to(BUNDLE.resolve()), "Manifest path escapes snapshot")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == expected,
                f"Snapshot checksum mismatch: {name}")
    require(len(entries) == 31, "Unexpected original manifest entry count")

    with tempfile.TemporaryDirectory(prefix="collatz-verify-") as temporary:
        work = Path(temporary)
        snapshot = work / "snapshot"
        shutil.copytree(BUNDLE, snapshot,
                        ignore=shutil.ignore_patterns("__pycache__", "independent_verifier"))
        run([sys.executable, "-B", "verify_stored_currents.py"], snapshot)
        stored = json.loads((snapshot / "stored_verification.json").read_text())
        require(stored["status"] == "PASS", "Stored certificate audit failed")

        shutil.copy2(RESEARCH / "right_aligned_packets.py", work)
        run([sys.executable, "-B", "right_aligned_packets.py"], work)
        right = json.loads((work / "right_aligned_audit.json").read_text())
        receipt = json.loads((RESEARCH / "right_aligned_audit.json").read_text())
        require(right == receipt, "Right-aligned audit differs from persisted receipt")
        controls = work / "research" / "negative_controls"
        shutil.copytree(RESEARCH / "negative_controls", controls,
                        ignore=shutil.ignore_patterns("__pycache__"))
        shutil.copy2(RESEARCH / "right_aligned_packets.py", controls.parent)
        shutil.copytree(BUNDLE / "data", controls.parent / "collatz_packet_currents" / "data")
        for script, name in (("affine_controls.py", "negative_controls_audit.json"),
                             ("reduction_audit.py", "reduction_audit.json"),
                             ("main_claims_audit.py", "main_claims_audit.json"),
                             ("progress_measures_audit.py", "progress_measures_audit.json")):
            run([sys.executable, "-B", script], controls)
            fresh = json.loads((controls / name).read_text())
            persisted = json.loads((RESEARCH / "negative_controls" / name).read_text())
            require(fresh == persisted, f"{name} differs from persisted receipt")

        cpp = "not requested"
        if args.cpp:
            compiler = shutil.which(os.environ.get("CXX", "c++"))
            require(compiler is not None, "C++17 compiler unavailable; install one or omit --cpp")
            executable = work / "independent_verifier"
            run([compiler, "-O2", "-std=c++17", "-Wall", "-Wextra",
                 str(snapshot / "independent_verifier.cpp"), "-o", str(executable)], work)
            for N, depth in ((4096, 2), (262144, 4)):
                actual = json.loads(run([str(executable), str(N), str(depth),
                                         str(snapshot / "data")], work))
                expected = json.loads((snapshot / f"independent_{N}.json").read_text())
                require(actual == expected, f"Independent receipt mismatch at N={N}")
            cpp = "PASS: 4096 and 262144"
    print(json.dumps(dict(status="PASS", archive_sha256=ARCHIVE_SHA,
                         manifest_entries=len(entries), stored_python="PASS",
                         right_aligned="PASS: matches persisted receipt",
                         negative_controls_and_audit="PASS: four receipts reproduced",
                         independent_cpp=cpp,
                         scope="Finite audits only; universal current existence remains open."), indent=2))


if __name__ == "__main__":
    main()
