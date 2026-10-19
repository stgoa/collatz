#!/usr/bin/env python3
"""Run the standalone checkers of the repository's research lines and reviews, in place, from the repo root.

    python3 scripts/run_checks.py                       # every line below
    python3 scripts/run_checks.py --line cycle_spectrum # one line (repeatable)
    python3 scripts/run_checks.py --fast -j 4           # skip checks slower than ~1 minute

Lines handled here: cycle_spectrum, viewpoints, explicit_tao, and reviews (reviews/side_lane).
The frozen lines (collatz_research_20261017, current_construction, annular_construction, residual_progress,
phase6) are verified by scripts/verify_all.py, which runs them in a temporary copy, because some of
their scripts rewrite committed receipts when run in place.

Side-lane probes write their JSON receipt next to themselves on every run. Three of those receipts
record timing, environment or path details and may change on re-run (NONDETERMINISTIC below); a
diff in them alone is not a failure.
Exit status: 0 if every selected check passed, 1 otherwise.
"""
import argparse
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Delivery checks pinned to the commits that produced them; they compare documents byte-for-byte with
# those commits and are expected to fail at HEAD. Kept as historical records.
PINNED = {f"experiments/cycle_spectrum/C0{n}/check_delivery.py" for n in range(8, 14)}

# Scripts that need command-line arguments (see their docstrings); not run automatically.
NEEDS_ARGS = {
    "reviews/side_lane/c004_narrow_check.py",
    "reviews/side_lane/c005_c006_order_check.py",
    "reviews/side_lane/c007_height_check.py",
    "reviews/side_lane/c008_residue_check.py",
    "reviews/side_lane/s7_stress_rational.py",
}

# Checks that took more than about a minute on a laptop (skipped with --fast).
SLOW = {
    "experiments/cycle_spectrum/C012/check_coupled_system.py",
    "reviews/side_lane/c012_candidate_check.py",
    "reviews/side_lane/closure_frontier_meter.py",
    "reviews/side_lane/complete_core_classes.py",
    "reviews/side_lane/q2_end_depth.py",
    "reviews/side_lane/r58_excess_check.py",
    "reviews/side_lane/s10_more_mismatches.py",
    "reviews/side_lane/s10_multirotation_lp.py",
    "reviews/side_lane/s10_v2nev4_killers.py",
    "reviews/side_lane/s10_v2nev4_twelve_rotations.py",
    "reviews/side_lane/s13_rise_lemma.py",
    "reviews/side_lane/s4_band1_gcd.py",
    "reviews/side_lane/slow_cluster_probe.py",
}

NONDETERMINISTIC = {
    "reviews/side_lane/c001_spectrum_check.json",
    "reviews/side_lane/q1_giant_component.json",
    "reviews/side_lane/selected_rules_meter.json",
}

LINES = {
    "cycle_spectrum": lambda: sorted(ROOT.glob("experiments/cycle_spectrum/**/check_*.py")),
    "viewpoints": lambda: sorted(ROOT.glob("experiments/viewpoints/**/verify_examples.py")),
    "explicit_tao": lambda: sorted(ROOT.glob("experiments/explicit_tao/check_*.py")),
    "reviews": lambda: sorted(ROOT.glob("reviews/side_lane/*.py")),
}


def run(rel, timeout):
    t0 = time.time()
    try:
        r = subprocess.run([sys.executable, "-B", rel], cwd=ROOT, capture_output=True, text=True, timeout=timeout)
        ok, tail = r.returncode == 0, (r.stdout + r.stderr).strip().splitlines()[-1:] or [""]
    except subprocess.TimeoutExpired:
        ok, tail = False, [f"timeout after {timeout}s"]
    return rel, ok, round(time.time() - t0, 1), tail[0][:160]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--line", action="append", choices=sorted(LINES), help="line to check (repeatable)")
    ap.add_argument("--fast", action="store_true", help="skip checks that take more than about a minute")
    ap.add_argument("-j", "--jobs", type=int, default=4)
    ap.add_argument("--timeout", type=int, default=1200)
    args = ap.parse_args()
    lines = args.line or sorted(LINES)
    todo, skipped = [], []
    for line in lines:
        for p in LINES[line]():
            rel = p.relative_to(ROOT).as_posix()
            if rel in PINNED or rel in NEEDS_ARGS or (args.fast and rel in SLOW):
                skipped.append(rel)
            else:
                todo.append(rel)
    with ThreadPoolExecutor(max_workers=args.jobs) as ex:
        results = list(ex.map(lambda rel: run(rel, args.timeout), todo))
    failed = [r for r in results if not r[1]]
    for rel, ok, secs, tail in results:
        print(f"{'PASS' if ok else 'FAIL'}  {secs:7.1f}s  {rel}" + ("" if ok else f"   {tail}"))
    print(f"\n{len(results) - len(failed)} passed, {len(failed)} failed, {len(skipped)} skipped "
          f"(pinned historical, needs arguments{', slow' if args.fast else ''})")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
