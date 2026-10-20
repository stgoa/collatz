"""Replay this node's unmodified legacy checks in a temporary copy of the legacy layout.

Written at the B11-residual-R40-R60 migration. The legacy scripts in this folder
load sibling modules by their pre-migration folder names
(HERE.parent/'<legacy_folder>/...', repository-relative paths under experiments/),
so they no longer run at their node paths. This certificate rebuilds, in a fresh
temporary directory, the legacy tree they expect: every legacy folder listed in
LAYOUT is filled with the .py, .json and .csv files of the node folders that hold
its migrated files (extra files are harmless). It then runs each script in RUNS
from its legacy folder, without -O, exactly as scripts/verify_all.py did at
be73a66, and requires:
  - exit status 0 (the legacy checkers compare their full recomputation with the
    committed receipt and fail on any difference);
  - every copied file byte-identical afterwards (no receipt was rewritten; for the
    side-lane probes, which always rewrite their receipt, this is a byte-for-byte
    reproduction of the committed receipt).
Nothing in the repository is written. Standard library. Run from the repository
root: python3 <this file>. Exits 1 on any failure.

What this node replays:
  - experiments/residual_progress/joint_frontier/check_joint_frontier.py: two-arrow interface, 3 mod 32 block, expanding and required-ray families, the stored r = 27 currents, against joint_frontier_audit.json;
"""

import filecmp
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
AREA = HERE.parents[1]  # areas/convergence
SOURCE_DIRS = ("results", "attempts")

# legacy folder (relative to the legacy repository root) -> node folders holding its migrated files
# (nodes of those legacy folders that are single .md files hold no files and are not listed)
LAYOUT = {
    "experiments/packet_currents/negative_controls": ["locally-collatz-like-control-barrier"],
    "experiments/annular_construction/arithmetic": ["universal-annular-partial-current"],
    "experiments/annular_construction/components": ["affine-common-tail-tree-lifting"],
    "experiments/current_construction/recursive": ["disjoint-annular-recursion"],
    "experiments/current_construction/obstructions": ["orbit-component-current-criterion", "whole-packet-historical-certificates"],
    "experiments/residual_progress/duality": ["finite-rational-cone-integer-certificate"],
    "experiments/residual_progress/forcing": ["actual-graph-current-compiler"],
    "experiments/residual_progress/transport": ["root-transport-normal-form"],
    "experiments/residual_progress/templates": ["unbounded-exposure-depth-necessary"],
    "experiments/residual_progress/closure": ["local-packet-calibration-extension"],
    "experiments/residual_progress/auxiliary": ["auxiliary-normalisation-remainder"],
    "experiments/residual_progress/release": ["delayed-release-cancellation"],
    "experiments/residual_progress/release_packing": ["release-source-packing"],
    "experiments/residual_progress/complement": ["retained-graph-complement-constructor"],
    "experiments/residual_progress/alternating": ["signed-path-collapse-capacity"],
    "experiments/residual_progress/release_coverage": ["short-delay-all-phase-obstruction"],
    "experiments/residual_progress/complement_recursion": ["annular-complement-outer-descent"],
    "experiments/residual_progress/window_components": ["bounded-source-cluster-local-bound"],
    "experiments/residual_progress/phase_depth": ["fixed-ternary-order-unbounded-depth"],
    "experiments/residual_progress/residual_return": ["halving-coalescence-return"],
    "experiments/residual_progress/sufficient_sets": ["five-ray-profile-completion-suffices", "ansari-sieve-step-counterexample"],
    "experiments/residual_progress/bridge_normal_form": ["elementary-bridge-quotient-normal-form"],
    "experiments/residual_progress/complementary_bridge": ["complementary-run-bridges"],
    "experiments/residual_progress/absorbed_fibers": ["absorbed-fibre-uniform-counts"],
    "experiments/residual_progress/cylinder_barrier": ["prefix-rule-cylinder-rate-barrier"],
    "experiments/residual_progress/known_saturation": ["supplied-path-saturation-core"],
    "experiments/residual_progress/second_return": ["shrinking-paired-return-recursion"],
    "experiments/residual_progress/bounded_run_cycles": ["bounded-runs-exclude-finite-label-potentials"],
    "experiments/residual_progress/merger_scope": ["merger-catalogue-scope"],
    "experiments/residual_progress/paired_completion": ["mixed-shrinking-pair-rules"],
    "experiments/residual_progress/inverse_ancestry": ["decreasing-inverse-ancestry"],
    "experiments/residual_progress/pair_scope": ["tripling-doubling-pair-decomposition"],
    "experiments/residual_progress/pair_one": ["missing-one-mod-8-pair-domain"],
    "experiments/residual_progress/tripling_equivalence": ["critical-tripling-domain-equivalence"],
    "experiments/residual_progress/odd_pair_closure": ["odd-h-pair-interface-compiler"],
    "experiments/residual_progress/even_pair_closure": ["coupled-even-pair-recursion"],
    "experiments/residual_progress/w9_closure": ["critical-nine-elimination"],
    "experiments/residual_progress/critical_inverse": ["decreasing-w5-phase-inverse-barrier"],
    "experiments/residual_progress/joint_frontier": ["joint-source-unbounded-frontier"],
    "experiments/residual_progress/critical_rank": ["critical-image-rank-composition"],
    "experiments/residual_progress/returning_phase": ["returning-forward-interface"],
    "experiments/residual_progress/nonselected_inverse": ["base-inverse-phases-increasing-pairs"],
    "experiments/residual_progress/inverse_escape": ["variable-depth-inverse-escape-barrier"],
    "experiments/residual_progress/nonselected_multiples": ["nonselected-multiples-inverse-interface"],
    "experiments/residual_progress/nonselected_forward": ["forward-blocks-low-exponent-tests"],
    "experiments/residual_progress/inverse_scope": ["inverse-only-exclusions-short-forward"],
    "experiments/residual_progress/double_inverse": ["two-inverse-phases-intermediate-increase"],
    "experiments/residual_progress/phase_rank": ["sigma-rank-removes-absorption-overhead"],
    "experiments/residual_progress/returning_continuation": ["returning-second-forward-interface"],
    "experiments/residual_progress/forward_continuation": ["low-block-continuation-prescribed-growth"],
    "experiments/residual_progress/continued_rules": ["low-block-continuation-prescribed-growth"],
    "experiments/residual_progress/rule_avoidance": ["growing-prefix-unhandled-leading-input"],
    "experiments/residual_progress/selected_forward": ["selected-critical-five-forward-tables"],
    "experiments/residual_progress/selected_inverse": ["two-selected-inverse-choices"],
    "experiments/residual_progress/selected_cycle_exit": ["guarded-cycle-exit-phases"],
    "experiments/residual_progress/selected_rules": ["twelve-family-rho-dispatcher"],
    "experiments/residual_progress/rank_mixing": ["rho-sigma-rank-mixing"],
    "experiments/residual_progress/exact_absorption_bound": ["rank-excess-absorption-classification"],
    "experiments/residual_progress/deferred_rank": ["deferred-original-rank-testing"],
    "experiments/residual_progress/cycle_inverse": ["maximal-inverse-cycle-continuation"],
}
# single legacy files: legacy path -> (node folder, file name)
SINGLE_FILES = {
    "experiments/packet_currents/right_aligned_packets.py": ("right-aligned-fixed-core-remainder", "right_aligned_packets.py"),
    "reviews/side_lane/fibre_count_check.py": ("absorbed-fibre-uniform-counts", "fibre_count_check.py"),
}
# (legacy folder, script, side-lane files to place in that folder from this node)
RUNS = [
    ('experiments/residual_progress/joint_frontier', 'check_joint_frontier.py', []),
]
TIMEOUT = 1500


def node_dir(name):
    for kind in SOURCE_DIRS:
        path = AREA / kind / name
        if path.is_dir():
            return path
    raise FileNotFoundError("node folder not found: " + name)


def build(tmp):
    copied = []
    for legacy, nodes in LAYOUT.items():
        dest = tmp / legacy
        dest.mkdir(parents=True, exist_ok=True)
        for name in nodes:
            for src in sorted(node_dir(name).iterdir()):
                if src.is_file() and src.suffix in (".py", ".json", ".csv"):
                    shutil.copy2(src, dest / src.name)
                    copied.append((src, dest / src.name))
    for legacy, (name, file_name) in SINGLE_FILES.items():
        src, dest = node_dir(name) / file_name, tmp / legacy
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        copied.append((src, dest))
    for legacy, _script, extra in RUNS:
        for file_name in extra:
            src, dest = HERE / file_name, tmp / legacy / file_name
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)
            copied.append((src, dest))
    # A later copy may replace an earlier one of the same name; compare with the last source.
    final = {}
    for src, dest in copied:
        final[dest] = src
    return final


def main():
    failures = []
    env = {k: v for k, v in os.environ.items() if k not in ("PYTHONOPTIMIZE", "PYTHONPATH")}
    with tempfile.TemporaryDirectory() as name:
        tmp = Path(name)
        copied = build(tmp)
        for legacy, script, _extra in RUNS:
            try:
                proc = subprocess.run([sys.executable, "-B", script], cwd=tmp / legacy, env=env,
                                      capture_output=True, text=True, timeout=TIMEOUT)
            except subprocess.TimeoutExpired:
                failures.append(f"{legacy}/{script}: timed out")
                continue
            if proc.returncode != 0:
                tail = (proc.stdout + proc.stderr).strip().splitlines()[-3:]
                failures.append(f"{legacy}/{script}: exit {proc.returncode}: " + " | ".join(tail))
        for dest, src in copied.items():
            if not dest.is_file() or not filecmp.cmp(src, dest, shallow=False):
                failures.append(f"{dest.relative_to(tmp)} differs after the replay")
    if failures:
        for line in failures:
            print("FAIL", line)
        sys.exit(1)
    print(f"PASS: {len(RUNS)} legacy check(s) replayed in the legacy layout; receipts unchanged")


if __name__ == "__main__":
    main()
