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
                             ("progress_measures_audit.py", "progress_measures_audit.json"),
                             ("attempt_probes.py", "attempt_probes.json")):
            run([sys.executable, "-B", script], controls)
            fresh = json.loads((controls / name).read_text())
            persisted = json.loads((RESEARCH / "negative_controls" / name).read_text())
            require(fresh == persisted, f"{name} differs from persisted receipt")


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
            ("templates", "check_symbolic_lift.py"),
            ("templates", "check_unbounded_exposure.py"),
            ("closure", "check_local_extension.py"),
            ("auxiliary", "check_auxiliary_normal_form.py"),
            ("release", "check_release.py"),
            ("release_packing", "release_packing.py"),
            ("complement", "check_complement.py"),
            ("alternating", "check_alternating_paths.py"),
            ("release_coverage", "check_coverage.py"),
            ("complement_recursion", "check_transfer.py"),
            ("window_components", "check_window_components.py"),
            ("phase_depth", "check_fixed_h.py"),
            ("residual_return", "check_halving_return.py"),
            ("bridge_normal_form", "check_normal_form.py"),
            ("complementary_bridge", "check_run_bridge.py"),
            ("absorbed_fibers", "check_fibers.py"),
            ("cylinder_barrier", "check_cylinder_barrier.py"),
            ("known_saturation", "check_saturation.py"),
            ("second_return", "check_paired_return.py"),
            ("bounded_run_cycles", "check_bounded_runs.py"),
            ("merger_scope", "check_merger_scope.py"),
            ("paired_completion", "check_mixed_pairs.py"),
            ("inverse_ancestry", "check_inverse_ancestry.py"),
            ("pair_scope", "check_pair_scope.py"),
            ("pair_one", "check_pair_one.py"),
            ("tripling_equivalence", "check_tripling.py"),
            ("odd_pair_closure", "check_odd_interface.py"),
            ("even_pair_closure", "check_even_pairs.py"),
            ("w9_closure", "check_w9_closure.py"),
            ("critical_inverse", "check_critical_inverse.py"),
            ("joint_frontier", "check_joint_frontier.py"),
            ("critical_rank", "check_rank_closure.py"),
            ("returning_phase", "check_returning_phase.py"),
            ("nonselected_inverse", "check_inverse_phases.py"),
            ("inverse_escape", "check_inverse_escape.py"),
            ("nonselected_multiples", "check_multiple_escape.py"),
            ("nonselected_forward", "check_nonselected_forward.py"),
            ("inverse_scope", "check_inverse_scope.py"),
            ("double_inverse", "check_double_inverse.py"),
            ("double_inverse", "check_expanded_union.py"),
            ("phase_rank", "check_sigma_rank.py"),
            ("returning_continuation", "check_returning_continuation.py"),
            ("forward_continuation", "check_forward_continuation.py"),
            ("rule_avoidance", "check_rule_avoidance.py"),
            ("continued_rules", "check_continued_rules.py"),
            ("selected_forward", "check_selected_forward.py"),
            ("selected_inverse", "check_selected_inverse.py"),
            ("selected_cycle_exit", "check_selected_exit.py"),
            ("rank_mixing", "probe_rank_mixing.py"),
            ("selected_rules", "check_selected_rules.py"),
            ("exact_absorption_bound", "check_exact_bound.py"),
            ("deferred_rank", "check_deferred_rank.py"),
            ("cycle_inverse", "check_cycle_inverse.py"),
            ("exit_continuation", "check_exit_continuation.py"),
            ("refined_rules", "check_refined_rules.py"),
            ("sufficient_sets", "check_recursive_sieve.py"),
            (".", "check_pair_domain_external.py"),
        ):
            run([sys.executable, "-B", script], residual_work / directory)
        # The review checker imports the annular arithmetic implementation;
        # its temporary copy and dependencies now exist at their usual paths.
        run([sys.executable, "-B", "check_review_scope.py"], controls)
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
                         negative_controls_and_audit="PASS: five receipts reproduced",
                         review_scope="PASS: alternative minimum-cost one-sided certificates",
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
                         symbolic_component_lift="PASS: 9171 decisions and 42487 exact inequalities",
                         unbounded_exposure="PASS: inverse invariants and complete CRT/ray components",
                         local_extension="PASS: 64 identities, 16640 coefficients, stored outer current",
                         auxiliary_normalization="PASS: 66 annuli, order independence, residual lower bound",
                         delayed_release="PASS: 69 currents, refined complete components, neutral and resolving witnesses",
                         extended_packing="PASS: 129 annuli, disjoint source capacity and floor counts",
                         retained_graph_extension="PASS: 131 cutoff graphs, 36 phases, supplied-input conversions",
                         signed_path_collapse="PASS: exact currents, intermediate capacity, retained frontiers and exits",
                         release_phase_coverage="PASS: symbolic phase isolation and fixed-h required-ladder obstruction",
                         annular_complement_transfer="PASS: smaller ancestors, exact outer currents and delayed descents",
                         bounded_source_clusters="PASS: complete local clusters, sharp63 span and forbidden-exit scope",
                         fixed_ternary_depth="PASS: finite barrier and complete obstructions at fixed h=2",
                         shrinking_coalescence="PASS: full binary family, exact residual counts and supplied-current conversion",
                         elementary_bridge_normal_form="PASS: complete components, quotient map, all inverse branches and exact counts",
                         complementary_run_bridges="PASS: full run branches, normalized counts, signed conversion and remaining obstructions",
                         infinite_absorbed_fibers="PASS: exact high-band counts and finite supplied-current conversions",
                         prefix_cylinder_rates="PASS: direct residues, four exact DPs, rotation bounds and high common states",
                         supplied_path_saturation="PASS: exact finite core, least origins, signed counts and additional weight2 certificate",
                         shrinking_paired_returns="PASS: signed recursion, arbitrary-depth cylinders, exact merger clocks and supplied-current conversion",
                         bounded_run_growth="PASS: repeated words, fixed run labels, required-ray witnesses and exact currents",
                         merger_scope="PASS: exact successor bound, scoped escapes, early cancellation and external peak tables",
                         mixed_pair_recursion="PASS: three shrinking branches, mixed cylinders, clocks and supplied-current conversion",
                         decreasing_inverse_ancestry="PASS: complete chains, exact counts and unbounded-return lower-seed families",
                         general_pair_scope="PASS: half-seed comparison, formal pair types and complete static catalogue components",
                         missing_pair_domain="PASS: two 1-mod-8 entry rules, mixed cylinders and actual Mersenne conversions",
                         critical_tripling_domain="PASS: exact critical bijection, conditional plans, supplied-input boundaries and finite compilations",
                         complete_odd_pair_interface="PASS: all odd-h boundaries, high-h shrinkage, critical input compilation and scoped ternary delay",
                         coupled_even_pairs="PASS: split-catalogue scope, joint cylinders, exact half-seed clocks and full source weights",
                         critical_nine_elimination="PASS: complete local interfaces, signed W5-only plans, input bounds and finite substitutions",
                         critical_inverse_phase="PASS: whole shrinking phase, exact self-dependency and complete inverse-branch arithmetic",
                         joint_positive_frontier="PASS: complete interfaces, growing prefixes and full-weight actual required-ray roots",
                         critical_image_rank="PASS: W9 and absorption bounds, mixed signed closure and supplied input checks",
                         returning_forward_phase="PASS: complete interface, scoped undo loops, decreasing subdomains and unbounded-run families",
                         nonselected_inverse_phases="PASS: both base rays, exact rank thresholds, self-returns and increasing-index descent",
                         variable_inverse_escape="PASS: two-block slope criterion, full depth4 classification and fixed-precision all-ray barriers",
                         nonselected_multiple_escape="PASS: complete two-block phases, exact failure vectors and supplied currents",
                         complete_nonselected_forward="PASS: full blocks, exact low-exponent tests, CRT families and undo identities",
                         permanent_inverse_scope="PASS: finite closed exclusion certificates, all-ray lifts and short forward resolutions",
                         double_inverse_phases="PASS: exact endpoint thresholds through intermediate growth and signed substitutions",
                         seven_rule_composition="PASS: preserved earlier rules, strict common rank, mixed closure and supplied inputs",
                         phase_rank="PASS: uniform sigma absorption bound, complete forward class and explicit rank incompatibility",
                         second_returning_block="PASS: full signed interface, exact low-run table, long CRT families and actual substitutions",
                         forward_continuation="PASS: complete two-block table, maximal low runs, unbounded delayed descents and supplied currents",
                         rule_avoidance="PASS: positive growing prefixes, complete W9 accounting and separately ranked leading-leaf obstructions",
                         continued_rule_composition="PASS: preserved seven-rule priority plus both rho continuations; sigma kept separate",
                         selected_forward="PASS: complete first/second block tables, new CRT domains, corrected phase and actual substitutions",
                         selected_inverse="PASS: both inverse choices, exhaustive failed vectors, exact thresholds and arbitrary forward-depth intersections",
                         selected_cycle_exit="PASS: maximal guarded cycles, eleven exit phases, new unbounded progressions and supplied currents",
                         finite_rank_mixing="PASS: two completed finite dependency graphs; no universal compatibility claim",
                         selected_rule_composition="PASS: old nine-rule priority preserved; three selected families share rho and retain missing inputs",
                         exact_absorption_excess="PASS: complete above-minimum request classification, fifth-family rho test and supplied currents",
                         deferred_rank_expansion="PASS: protected-source signed rewriting, complete new domains and higher-request cancellation",
                         maximal_cycle_inverse="PASS: complete cycle/point thresholds, failed frontiers, all-depth CRT escape and supplied currents",
                         eleven_exit_continuation="PASS: whole exit interface, sharp original-rank threshold and exact scoped continuation undo",
                         refined_rule_composition="PASS: old twelve-rule priority preserved; fifteen families share rho with explicit missing leaves",
                         external_sieve_gap="PASS: exact counterexample to the displayed set equality; no theorem refutation",
                         external_pair_controls="PASS: seven exact cycle witnesses, including three W5 pairs, and invariant-pairing obstructions",
                         scope="Finite audits only; universal current existence remains open."), indent=2))


if __name__ == "__main__":
    main()
