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

        # Preserve the repository-relative imports used by the new experiments.
        revised = work / "collatz_research_20261017"
        revised.mkdir()
        shutil.copy2(RESEARCH / "right_aligned_packets.py", revised)
        source_experiments = ROOT / "experiments" / "current_construction"
        experiments = work / "experiments" / "current_construction"
        shutil.copytree(source_experiments, experiments,
                        ignore=shutil.ignore_patterns("__pycache__"))
        new_audits = (
            ("frontier", "check_sparse_criteria.py", "sparse_criteria_audit.json"),
            ("recursive", "check_annular_recursion.py", "annular_audit.json"),
            ("obstructions", "verify_obstructions.py", "audit.json"),
        )
        for directory, script, receipt_name in new_audits:
            actual = json.loads(run([sys.executable, "-B", script], experiments / directory))
            expected = json.loads((source_experiments / directory / receipt_name).read_text())
            require(actual == expected, f"New audit receipt differs: {script}")
        run([sys.executable, "-B", "check_five_rays_independent.py"],
            experiments / "obstructions")
        # The demo independently checks stored table rows and its full receipt.
        run([sys.executable, "-B", "whole_packet_demo.py"], experiments / "obstructions")
        # The constructive-annulus checks compare their own persisted receipts
        # and tables. Keep both experiment trees for repository-relative imports.
        annular_source = ROOT / "experiments" / "annular_construction"
        annular_work = work / "experiments" / "annular_construction"
        shutil.copytree(annular_source, annular_work,
                        ignore=shutil.ignore_patterns("__pycache__"))
        for directory, script in (
            ("components", "affine_template_compiler.py"),
            ("components", "check_annular_components.py"),
            ("arithmetic", "check_arithmetic_reductions.py"),
            ("arithmetic", "combined_partial_current.py"),
            ("duality", "check_duality.py"),
        ):
            run([sys.executable, "-B", script], annular_work / directory)
        residual_source = ROOT / "experiments" / "residual_progress"
        residual_work = work / "experiments" / "residual_progress"
        shutil.copytree(residual_source, residual_work,
                        ignore=shutil.ignore_patterns("__pycache__"))
        for directory, script in (
            ("transport", "check_root_transport.py"),
            ("duality", "check_finite_cone.py"),
            ("forcing", "actual_graph_compiler.py"),
            ("templates", "check_inverse_exposure.py"),
        ):
            run([sys.executable, "-B", script], residual_work / directory)
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
                         right_aligned="PASS: matches persisted receipt", independent_cpp=cpp,
                         sparse_rays="PASS: five-ray proof arithmetic and finite bases",
                         annular_recursion="PASS: 66 finite full-measure cases",
                         current_obstructions="PASS: finite graphs and delayed separation",
                         revised_currents="PASS: 10 samples and both stored new tables",
                         affine_packing="PASS: exact lifts, capacity, cutoffs 8..4096 by 8",
                         annular_currents="PASS: 6 diagnostics and stored A_96/A_168 tables",
                         arithmetic_reductions="PASS: 66 cases, norm and outer profiles",
                         combined_partial_current="PASS: 8 cases through 6144",
                         component_duality="PASS: potentials, boundary flux, projections, reflected certificate",
                         residual_transport="PASS: normal form, surviving atoms, exact plateaus",
                         finite_cone="PASS: rational identities and 216000 integer-gap cases",
                         finite_forcing="PASS: 30 actual packet inputs and stored U_112 current",
                         inverse_exposure="PASS: 48 full-graph comparisons and complete depth-32 obstruction",
                         scope="Finite audits only; universal current existence remains open."), indent=2))


if __name__ == "__main__":
    main()
