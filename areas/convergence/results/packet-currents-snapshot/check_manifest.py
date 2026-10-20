#!/usr/bin/env python3
"""Certificate: the inherited snapshot is byte-identical to its upload manifest.

Recomputes the SHA-256 of every file listed in collatz_packet_currents/SHA256SUMS.txt
and compares it with the listed hash. Exits non-zero on any mismatch, missing file,
path escaping the snapshot, or an entry count other than the original 31.

    python3 areas/convergence/results/packet-currents-snapshot/check_manifest.py

Standard library only; reads files, writes nothing.
"""
import hashlib
import sys
from pathlib import Path

SNAPSHOT = Path(__file__).resolve().parent / "collatz_packet_currents"
EXPECTED_ENTRIES = 31


def main() -> int:
    lines = (SNAPSHOT / "SHA256SUMS.txt").read_bytes().decode("ascii").splitlines()
    entries = [line for line in lines if line.strip()]
    failures = []
    for line in entries:
        expected, name = line.split(maxsplit=1)
        path = (SNAPSHOT / name.lstrip("*")).resolve()
        if not path.is_relative_to(SNAPSHOT):
            failures.append(f"path escapes snapshot: {name}")
        elif not path.is_file():
            failures.append(f"missing: {name}")
        elif hashlib.sha256(path.read_bytes()).hexdigest() != expected.lower():
            failures.append(f"hash mismatch: {name}")
    if len(entries) != EXPECTED_ENTRIES:
        failures.append(f"manifest has {len(entries)} entries, expected {EXPECTED_ENTRIES}")
    for failure in failures:
        print(f"FAIL {failure}")
    if failures:
        return 1
    print(f"PASS: all {len(entries)} manifest entries of collatz_packet_currents match SHA256SUMS.txt")
    return 0


if __name__ == "__main__":
    sys.exit(main())
