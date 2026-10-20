# Migration manifest

One row per migration unit (a legacy folder, a file, or a script with its receipts). Each batch fills in **Fate** for its rows, in the same commit as the move:
- `node <id>` (or several ids): the content became that node, or is attached to it;
- `archive <path>`: kept as frozen history;
- `dropped: <reason>`.

Batches run in order, one commit each. The batch letter in the first column says which batch owns the row.

| Batch | Legacy unit | Files | Fate |
|---|---|---|---|
| B01-sources | `docs/LITERATURE.md` | 1 | node adamczewski-2013-mahler-functions, barina-2025-convergence-2-71, berg-1994-analytic-encoding, bugeaud-2022-two-logarithms, cobham-recognizability-theorem, corvaja-2005-s-unit-height, eilenberg-finite-kernel, eliahou-1993-cycle-length, everett-1977-stopping-time, halbeisen-1997-rational-cycles, hercher-2023-cycle-length, knight-2026-high-cycles, krasikov-2003-predecessors, lagarias-1985-survey, languasco-2025-two-primes, lau-2026-positive-density, matveev-2000-linear-forms, mazur-2026-predecessor-density, monks-2006-sufficiency, monks-2013-strongly-sufficient, musson-collatz-gap-all, rhin-1987-irrationality-measure, simons-2005-m-cycles, steiner-1977-one-cycles, tao-2019-almost-all, terras-1976-stopping-time |
| B02-lean | `lean/audit` | 18 | restored to `lean/audit` |
| B02-lean | `lean/CycleSpectrum.lean` | 1 | restored to `lean/CycleSpectrum.lean` |
| B02-lean | `lean/Dichotomy.lean` | 1 | restored to `lean/Dichotomy.lean` |
| B02-lean | `lean/GeneralPeriodic.lean` | 1 | restored to `lean/GeneralPeriodic.lean` |
| B02-lean | `lean/KernelClosure.lean` | 1 | restored to `lean/KernelClosure.lean` |
| B17-leftovers | `lean/LOG.md` | 1 | pending |
| B02-lean | `lean/OddEventuallyPeriodic.lean` | 1 | restored to `lean/OddEventuallyPeriodic.lean` |
| B02-lean | `lean/PairObligation.lean` | 1 | restored to `lean/PairObligation.lean` |
| B02-lean | `lean/PeriodicRigidity.lean` | 1 | restored to `lean/PeriodicRigidity.lean` |
| B02-lean | `lean/QuadraticSeparation.lean` | 1 | restored to `lean/QuadraticSeparation.lean` |
| B02-lean | `lean/README.md` | 1 | restored to `lean/README.md` |
| B02-lean | `lean/ReverseClosure_Assembly.lean` | 1 | restored to `lean/ReverseClosure_Assembly.lean` |
| B02-lean | `lean/ReverseClosure_Final.lean` | 1 | restored to `lean/ReverseClosure_Final.lean` |
| B17-leftovers | `lean/STATE.md` | 1 | pending |
| B02-lean | `lean/ScalarInterface.lean` | 1 | restored to `lean/ScalarInterface.lean` |
| B02-lean | `lean/V004_Assembly.lean` | 1 | restored to `lean/V004_Assembly.lean` |
| B02-lean | `lean/V004_Final.lean` | 1 | restored to `lean/V004_Final.lean` |
| B02-lean | `lean/build_assembly.sh` | 1 | restored to `lean/build_assembly.sh` |
| B02-lean | `lean/build_reverse_assembly.sh` | 1 | restored to `lean/build_reverse_assembly.sh` |
| B02-lean | `lean/lakefile.toml` | 1 | restored to `lean/lakefile.toml` |
| B02-lean | `lean/lean-toolchain` | 1 | restored to `lean/lean-toolchain` |
| B02-lean | `lean/receipts` | 35 | restored to `lean/receipts` |
| B03-cycles-C001-C007 | `experiments/cycle_spectrum/C001` | 12 | node repeated-block-cancellation-bound, perturbed-mechanical-block-family, actual-cycles-3x-d-corpus |
| B03-cycles-C001-C007 | `experiments/cycle_spectrum/C002` | 10 | node equal-total-two-block-exclusion, proportional-slope-two-block-bound, unequal-slope-two-block-growth, rotating-mechanical-two-block-family, constant-cancellation-two-growing-blocks |
| B03-cycles-C001-C007 | `experiments/cycle_spectrum/C003` | 10 | node two-block-uniform-denominator-growth, contracting-two-block-effective-exclusion, interval-trapping-expanding-blocks |
| B03-cycles-C001-C007 | `experiments/cycle_spectrum/C004` | 10 | node narrow-cycles-are-mechanical, narrow-cycle-spectrum-law, rotation-lattice-single-divisibility, close-pair-lattice-criterion |
| B03-cycles-C001-C007 | `experiments/cycle_spectrum/C005` | 14 | node rotation-block-exclusion, dyadic-order-lemma, three-band-collatz-cycles-are-ordered, mechanical-normalized-word-transfer, ordered-cycle-denominator-one |
| B03-cycles-C001-C007 | `experiments/cycle_spectrum/C006` | 12 | node ordered-cycle-sparse-forcing, ordered-cycle-height-change-growth, generic-cycle-minimum-baselines, ordered-cycle-shortcuts, mechanical-normalized-word-transfer, one-height-defect-ordered-cycles |
| B03-cycles-C001-C007 | `experiments/cycle_spectrum/C007` | 13 | node height-denominator-candidate, ordered-cycle-residue-law, ordered-cycle-height-census, height-bound-via-residues-or-relaxation |
| B03-cycles-C001-C007 | `reviews/side_lane/c001_spectrum_check.*` | 2 | node repeated-block-cancellation-bound |
| B03-cycles-C001-C007 | `reviews/side_lane/c002_two_block_check.*` | 2 | node equal-total-two-block-exclusion |
| B03-cycles-C001-C007 | `reviews/side_lane/c003_variable_blocks_check.*` | 2 | node contracting-two-block-effective-exclusion |
| B03-cycles-C001-C007 | `reviews/side_lane/c004_narrow_check.*` | 2 | node narrow-cycles-are-mechanical |
| B03-cycles-C001-C007 | `reviews/side_lane/c004c_bridge_check.*` | 2 | node narrow-cycles-are-mechanical |
| B03-cycles-C001-C007 | `reviews/side_lane/c005_c006_order_check.*` | 2 | node rotation-block-exclusion |
| B03-cycles-C001-C007 | `reviews/side_lane/c005d_ofword_check.*` | 2 | node rotation-block-exclusion |
| B03-cycles-C001-C007 | `reviews/side_lane/c005e_rep_check.*` | 2 | node rotation-block-exclusion |
| B03-cycles-C001-C007 | `reviews/side_lane/c005f_bookkeeping_check.*` | 2 | node rotation-block-exclusion |
| B03-cycles-C001-C007 | `reviews/side_lane/c005g_rotation_block_check.*` | 2 | node rotation-block-exclusion |
| B03-cycles-C001-C007 | `reviews/side_lane/c005h_ratio_bound_check.*` | 2 | node rotation-block-exclusion |
| B03-cycles-C001-C007 | `reviews/side_lane/c006b_erun_check.*` | 2 | node ordered-cycle-sparse-forcing |
| B03-cycles-C001-C007 | `reviews/side_lane/c006c_g4_check.*` | 2 | node ordered-cycle-sparse-forcing |
| B03-cycles-C001-C007 | `reviews/side_lane/c006d_g2_check.*` | 2 | node ordered-cycle-sparse-forcing |
| B03-cycles-C001-C007 | `reviews/side_lane/c006e_cc_check.*` | 2 | node ordered-cycle-sparse-forcing |
| B03-cycles-C001-C007 | `reviews/side_lane/c006f_order_word_check.*` | 2 | node ordered-cycle-sparse-forcing |
| B03-cycles-C001-C007 | `reviews/side_lane/c007_height_check.*` | 2 | node height-denominator-candidate |
| B04-cycles-C008-C014 | `experiments/cycle_spectrum/C008` | 15 | node ordered-cycle-sorted-rank-residues, small-band-height-residue-matching, primewise-height-residue-matching, height-residue-hall-matching |
| B04-cycles-C008-C014 | `experiments/cycle_spectrum/C009` | 16 | node excursion-compression, excursion-cut-lemma, one-point-deletion-rank-shift |
| B04-cycles-C008-C014 | `experiments/cycle_spectrum/C010` | 15 | node local-odd-rounding-exclusion, complete-gap-lattice-equivalence, odd-spacing-rounding-bound |
| B04-cycles-C008-C014 | `experiments/cycle_spectrum/C011` | 20 | node two-defect-rotation-exclusion, two-defect-cancellation-bound, two-defect-bounded-denominator-finiteness, two-defect-marker-family, fixed-defect-unbounded-cancellation, termwise-plateau-divisibility |
| B04-cycles-C008-C014 | `experiments/cycle_spectrum/C012` | 16 | node coupled-defect-matrix-smith-form, three-defect-arbitrary-background, rotation-defect-denominator-candidate, rotation-distance-growth |
| B04-cycles-C008-C014 | `experiments/cycle_spectrum/C013` | 15 | node shared-background-denominator-law, paired-state-run-law, distance-three-height-family |
| B04-cycles-C008-C014 | `experiments/cycle_spectrum/C014` | 7 | node compatible-arcs-common-partition-limits, rotated-residual-resultant-invariance |
| B04-cycles-C008-C014 | `reviews/side_lane/c008_residue_check.*` | 2 | node ordered-cycle-sorted-rank-residues |
| B04-cycles-C008-C014 | `reviews/side_lane/c009_excursion_check.*` | 2 | node excursion-compression |
| B04-cycles-C008-C014 | `reviews/side_lane/c010_gap_check.*` | 2 | node local-odd-rounding-exclusion |
| B04-cycles-C008-C014 | `reviews/side_lane/c010b_gap_lattice_check.*` | 2 | node local-odd-rounding-exclusion |
| B04-cycles-C008-C014 | `reviews/side_lane/c010c_any_arrangement_check.*` | 2 | node local-odd-rounding-exclusion |
| B04-cycles-C008-C014 | `reviews/side_lane/c011_two_defect_check.*` | 2 | node two-defect-rotation-exclusion |
| B04-cycles-C008-C014 | `reviews/side_lane/c012_candidate_check.*` | 2 | node coupled-defect-matrix-smith-form |
| B04-cycles-C008-C014 | `reviews/side_lane/c013_background_check.*` | 2 | node shared-background-denominator-law |
| B04-cycles-C008-C014 | `reviews/side_lane/c013b_run_law_check.*` | 2 | node shared-background-denominator-law |
| B05-cycles-S02-S08 | `experiments/cycle_spectrum/S02` | 1 | node ordered-cycle-run-renormalisation, run-start-gap-recursion, orbit-exponent-density |
| B05-cycles-S02-S08 | `experiments/cycle_spectrum/S03` | 1 | node band-three-ordering-extension, q-one-inversion-pair-reduction |
| B05-cycles-S02-S08 | `experiments/cycle_spectrum/S04` | 1 | node band-one-gcd-law-search |
| B05-cycles-S02-S08 | `experiments/cycle_spectrum/S05` | 1 | node mismatch-height-tradeoff, cycle-height-ceiling, cycle-height-bound |
| B05-cycles-S02-S08 | `experiments/cycle_spectrum/S06` | 1 | node two-mismatch-exclusion-via-gap, cycle-height-ceiling |
| B05-cycles-S02-S08 | `experiments/cycle_spectrum/S07` | 1 | node three-mismatch-exclusion |
| B05-cycles-S02-S08 | `experiments/cycle_spectrum/S08` | 1 | node four-mismatch-size-method-limit, ones-run-divisibility, one-cycle-exclusion-via-gap |
| B05-cycles-S02-S08 | `reviews/side_lane/s1a_integer_cycle_check.*` | 2 | node ordered-gap-closed-form (with single-forced-position-denominator, band-one-three-forced-positions from the S1 feed entry) |
| B05-cycles-S02-S08 | `reviews/side_lane/s1b_run_start_gcd_check.*` | 2 | node ordered-gap-closed-form |
| B05-cycles-S02-S08 | `reviews/side_lane/s1cd_gap_coprime_check.*` | 2 | node ordered-gap-closed-form (also evidence for single-forced-position-denominator) |
| B05-cycles-S02-S08 | `reviews/side_lane/s2_ucycle_explore.*` | 2 | node ordered-cycle-run-renormalisation |
| B05-cycles-S02-S08 | `reviews/side_lane/s2c_density_check.*` | 2 | node orbit-exponent-density |
| B05-cycles-S02-S08 | `reviews/side_lane/s3_inversion_pairs.*` | 2 | node band-three-ordering-extension |
| B05-cycles-S02-S08 | `reviews/side_lane/s3a_inversion_iff_check.*` | 2 | node q-one-inversion-pair-reduction |
| B05-cycles-S02-S08 | `reviews/side_lane/s4_band1_gcd.*` | 2 | node band-one-gcd-law-search |
| B05-cycles-S02-S08 | `reviews/side_lane/s4b_block_divisor_test.*` | 2 | node band-one-gcd-law-search |
| B05-cycles-S02-S08 | `reviews/side_lane/s5_cycle_heights.*` | 1 | node mismatch-height-tradeoff |
| B05-cycles-S02-S08 | `reviews/side_lane/s5_mismatch_height.*` | 2 | node mismatch-height-tradeoff |
| B05-cycles-S02-S08 | `reviews/side_lane/s6_c011_via_s5.*` | 2 | node two-mismatch-exclusion-via-gap |
| B05-cycles-S02-S08 | `reviews/side_lane/s7_stress_rational.*` | 1 | node three-mismatch-exclusion |
| B05-cycles-S02-S08 | `reviews/side_lane/s7_three_mismatch.*` | 2 | node three-mismatch-exclusion |
| B05-cycles-S02-S08 | `reviews/side_lane/s8_four_mismatch_map.*` | 2 | node four-mismatch-size-method-limit |
| B05-cycles-S02-S08 | `reviews/side_lane/s8_multiple_rotations.*` | 1 | node four-mismatch-size-method-limit |
| B05-cycles-S02-S08 | `reviews/side_lane/s8_multirotation_check.*` | 1 | node four-mismatch-size-method-limit |
| B06-cycles-S09-S13 | `experiments/cycle_spectrum/BRIEF.md` | 1 | archive archive/cycle-spectrum/BRIEF.md |
| B06-cycles-S09-S13 | `experiments/cycle_spectrum/LOG.md` | 1 | archive archive/cycle-spectrum/LOG.md |
| B06-cycles-S09-S13 | `experiments/cycle_spectrum/README.md` | 1 | dropped: content summarised in areas/cycles/OVERVIEW.md (index superseded by MAP.md); git rm |
| B06-cycles-S09-S13 | `experiments/cycle_spectrum/S09` | 1 | node two-three-mismatch-denominator-laws, global-drift-ceiling, cycle-word-repeat-bound |
| B06-cycles-S09-S13 | `experiments/cycle_spectrum/S10` | 1 | node multi-rotation-four-mismatch-exclusion, four-mismatch-sign-dichotomy (from Lean S10-a) |
| B06-cycles-S09-S13 | `experiments/cycle_spectrum/S11` | 1 | node shared-background-copies-via-gap |
| B06-cycles-S09-S13 | `experiments/cycle_spectrum/S12` | 1 | node denjoy-koksma-height-bound, denjoy-koksma-denominator-law |
| B06-cycles-S09-S13 | `experiments/cycle_spectrum/S13` | 1 | node rise-lemma, short-rotation-mismatch-growth, rise-lemma-denominator-law, largest-letter-rho-reduction; questions largest-letter-sublinear, rotation-distance-at-least-5 |
| B13-residual-R78-R94 | `reviews/side_lane/c0_basin_classify.*` | 1 | pending |
| B13-residual-R78-R94 | `reviews/side_lane/c0_basin_receipt.*` | 2 | pending |
| B09-residual-R11-R24 | `reviews/side_lane/fixed_h_check.*` | 2 | pending |
| B11-residual-R40-R60 | `reviews/side_lane/negative_cycle_shadows.*` | 2 | pending |
| B12-residual-R61-R77 | `reviews/side_lane/rho_prefix_plans.*` | 2 | pending |
| B06-cycles-S09-S13 | `reviews/side_lane/s10_more_mismatches.*` | 1 | node multi-rotation-four-mismatch-exclusion |
| B06-cycles-S09-S13 | `reviews/side_lane/s10_multirotation_lp.*` | 2 | node multi-rotation-four-mismatch-exclusion |
| B06-cycles-S09-S13 | `reviews/side_lane/s10_repeat_complexity.*` | 2 | node cycle-word-repeat-bound |
| B06-cycles-S09-S13 | `reviews/side_lane/s10_v2nev4_discrete.*` | 1 | node multi-rotation-four-mismatch-exclusion |
| B06-cycles-S09-S13 | `reviews/side_lane/s10_v2nev4_killers.*` | 1 | node multi-rotation-four-mismatch-exclusion |
| B06-cycles-S09-S13 | `reviews/side_lane/s10_v2nev4_twelve_rotations.*` | 1 | node multi-rotation-four-mismatch-exclusion |
| B06-cycles-S09-S13 | `reviews/side_lane/s11_c013_gap.*` | 2 | node shared-background-copies-via-gap |
| B06-cycles-S09-S13 | `reviews/side_lane/s12_denjoy_koksma.*` | 2 | node denjoy-koksma-height-bound |
| B06-cycles-S09-S13 | `reviews/side_lane/s12_dk_denominator_law.*` | 2 | node denjoy-koksma-denominator-law |
| B06-cycles-S09-S13 | `reviews/side_lane/s13_corollaries.*` | 2 | node short-rotation-mismatch-growth (also evidence for largest-letter-rho-reduction) |
| B06-cycles-S09-S13 | `reviews/side_lane/s13_rise_lemma.*` | 2 | node rise-lemma |
| B06-cycles-S09-S13 | `reviews/side_lane/s13_short_rotations.*` | 2 | node short-rotation-mismatch-growth |
| B06-cycles-S09-S13 | `reviews/side_lane/s9_denominator_law.*` | 2 | node two-three-mismatch-denominator-laws |
| B12-residual-R61-R77 | `reviews/side_lane/transfer_3xd.*` | 2 | pending |
| B07-convergence-packet-currents | `experiments/packet_currents/README.md` | 1 | node packet-currents-snapshot (became its README) |
| B07-convergence-packet-currents | `experiments/packet_currents/collatz_packet_currents` | 32 | node packet-currents-snapshot (snapshot kept whole and byte-identical in its folder; also cited by finite-current-certificate-identity, uniform-current-cost) |
| B07-convergence-packet-currents | `experiments/packet_currents/negative_controls` | 15 | node locally-collatz-like-control-barrier (whole folder, scripts import each other); also supports right-aligned-reduction-independent-checks, exact-current-minimality, progress-measures-control-3x-61, class-wise-obligation-equivalence, annular-bottom-cancellation-attempt |
| B07-convergence-packet-currents | `experiments/packet_currents/right_aligned_audit.json` | 1 | node right-aligned-fixed-core-remainder (also cited by qualitative-current-criterion, dyadic-cutoff-core-remainder) |
| B07-convergence-packet-currents | `experiments/packet_currents/right_aligned_packets.py` | 1 | node right-aligned-fixed-core-remainder (certificate; also cited by qualitative-current-criterion, dyadic-cutoff-core-remainder) |
| B07-convergence-packet-currents | `papers/README.md` | 1 | dropped: merged into `papers/README.md` (its build hint and paper row); the legacy file was removed |
| B07-convergence-packet-currents | `papers/right_aligned_reduction` | 1 | paper `papers/right-aligned-reduction/right-aligned-reduction.tex` (renamed, byte-identical); presents finite-current-certificate-identity, right-aligned-fixed-core-remainder, qualitative-current-criterion, dyadic-cutoff-core-remainder |
| B08-convergence-current-annular | `experiments/annular_construction/README.md` | 1 | archive archive/convergence-annular-construction/README.md |
| B08-convergence-current-annular | `experiments/annular_construction/REPORT.md` | 1 | archive archive/convergence-annular-construction/REPORT.md |
| B08-convergence-current-annular | `experiments/annular_construction/arithmetic` | 5 | node universal-annular-partial-current, annular-root-collapse-contraction, outer-profile-closure-obstruction |
| B08-convergence-current-annular | `experiments/annular_construction/components` | 10 | node affine-common-tail-tree-lifting |
| B08-convergence-current-annular | `experiments/annular_construction/duality` | 5 | node exposure-potential-boundary-flux, binary-residue-projection-information-loss, reflected-negative-annulus-control, annular-component-progress-lemma |
| B08-convergence-current-annular | `experiments/current_construction/README.md` | 1 | archive archive/convergence-current-construction/README.md |
| B08-convergence-current-annular | `experiments/current_construction/REPORT.md` | 1 | archive archive/convergence-current-construction/REPORT.md; its open obligation became node five-ray-annular-current-supply |
| B08-convergence-current-annular | `experiments/current_construction/frontier` | 3 | node five-ray-current-criterion, mesh-maximum-principle-alternative-grids, sparse-paired-exact-current-criterion |
| B08-convergence-current-annular | `experiments/current_construction/obstructions` | 12 | node orbit-component-current-criterion, bounded-packet-certificate-obstruction, whole-packet-historical-certificates, uniform-aggregate-exposure-depth, five-ray-current-criterion (sparse_ray_independent_audit.md, check_five_rays_independent.py) |
| B08-convergence-current-annular | `experiments/current_construction/recursive` | 4 | node disjoint-annular-recursion, exact-current-prefix-criterion |
| B10-residual-R25-R39 | `experiments/residual_progress/PAIR_DOMAIN_REVIEW.md` | 1 | pending |
| B09-residual-R11-R24 | `experiments/residual_progress/README.md` | 1 | pending |
| B09-residual-R11-R24 | `experiments/residual_progress/REPORT.md` | 1 | pending |
| B10-residual-R25-R39 | `experiments/residual_progress/absorbed_fibers` | 4 | pending |
| B12-residual-R61-R77 | `experiments/residual_progress/adjacent_history` | 1 | pending |
| B12-residual-R61-R77 | `experiments/residual_progress/adjacent_recursion` | 4 | pending |
| B12-residual-R61-R77 | `experiments/residual_progress/all_ray_continuation` | 4 | pending |
| B09-residual-R11-R24 | `experiments/residual_progress/alternating` | 3 | pending |
| B12-residual-R61-R77 | `experiments/residual_progress/arithmetic_progress` | 4 | pending |
| B09-residual-R11-R24 | `experiments/residual_progress/auxiliary` | 3 | pending |
| B10-residual-R25-R39 | `experiments/residual_progress/bounded_run_cycles` | 4 | pending |
| B10-residual-R25-R39 | `experiments/residual_progress/bridge_normal_form` | 4 | pending |
| B10-residual-R25-R39 | `experiments/residual_progress/check_pair_domain_external.py` | 1 | pending |
| B13-residual-R78-R94 | `experiments/residual_progress/child_history_scope` | 3 | pending |
| B09-residual-R11-R24 | `experiments/residual_progress/closure` | 5 | pending |
| B09-residual-R11-R24 | `experiments/residual_progress/complement` | 5 | pending |
| B09-residual-R11-R24 | `experiments/residual_progress/complement_recursion` | 5 | pending |
| B10-residual-R25-R39 | `experiments/residual_progress/complementary_bridge` | 5 | pending |
| B11-residual-R40-R60 | `experiments/residual_progress/continued_rules` | 3 | pending |
| B12-residual-R61-R77 | `experiments/residual_progress/critical_basis` | 4 | pending |
| B11-residual-R40-R60 | `experiments/residual_progress/critical_inverse` | 4 | pending |
| B11-residual-R40-R60 | `experiments/residual_progress/critical_rank` | 7 | pending |
| B11-residual-R40-R60 | `experiments/residual_progress/cycle_inverse` | 4 | pending |
| B10-residual-R25-R39 | `experiments/residual_progress/cylinder_barrier` | 4 | pending |
| B13-residual-R78-R94 | `experiments/residual_progress/deeper_window` | 9 | pending |
| B12-residual-R61-R77 | `experiments/residual_progress/defect_normal_form` | 4 | pending |
| B12-residual-R61-R77 | `experiments/residual_progress/defect_resolution` | 4 | pending |
| B11-residual-R40-R60 | `experiments/residual_progress/deferred_rank` | 4 | pending |
| B10-residual-R25-R39 | `experiments/residual_progress/pair_domain_external_review.json` | 1 | pending |
| B09-residual-R11-R24 | `experiments/residual_progress/side_lane_review.json` | 1 | pending |
| B12-residual-R61-R77 | `experiments/residual_progress/side_lane_review_13590c1.json` | 1 | pending |
| B12-residual-R61-R77 | `experiments/residual_progress/side_lane_review_13590c1.md` | 1 | pending |
| B10-residual-R25-R39 | `experiments/residual_progress/side_lane_review_1a2dfc5.json` | 1 | pending |
| B09-residual-R11-R24 | `experiments/residual_progress/side_lane_review_20261017_2005.json` | 1 | pending |
| B09-residual-R11-R24 | `experiments/residual_progress/side_lane_review_20261017_latest.json` | 1 | pending |
| B09-residual-R11-R24 | `experiments/residual_progress/side_lane_review_20261017_latest.md` | 1 | pending |
| B12-residual-R61-R77 | `experiments/residual_progress/side_lane_review_33c3829.json` | 1 | pending |
| B12-residual-R61-R77 | `experiments/residual_progress/side_lane_review_33c3829.md` | 1 | pending |
| B11-residual-R40-R60 | `experiments/residual_progress/side_lane_review_3d69784.json` | 1 | pending |
| B11-residual-R40-R60 | `experiments/residual_progress/side_lane_review_64a5981.json` | 1 | pending |
| B11-residual-R40-R60 | `experiments/residual_progress/side_lane_review_64a5981.md` | 1 | pending |
| B12-residual-R61-R77 | `experiments/residual_progress/side_lane_review_678e565.json` | 1 | pending |
| B12-residual-R61-R77 | `experiments/residual_progress/side_lane_review_678e565.md` | 1 | pending |
| B11-residual-R40-R60 | `experiments/residual_progress/side_lane_review_767af32.md` | 1 | pending |
| B13-residual-R78-R94 | `experiments/residual_progress/side_lane_review_86ead16.json` | 1 | pending |
| B13-residual-R78-R94 | `experiments/residual_progress/side_lane_review_86ead16.md` | 1 | pending |
| B13-residual-R78-R94 | `experiments/residual_progress/side_lane_review_8ed32bc.json` | 1 | pending |
| B13-residual-R78-R94 | `experiments/residual_progress/side_lane_review_8ed32bc.md` | 1 | pending |
| B13-residual-R78-R94 | `experiments/residual_progress/side_lane_review_9849c53.md` | 1 | pending |
| B13-residual-R78-R94 | `experiments/residual_progress/side_lane_review_b9203ff.md` | 1 | pending |
| B11-residual-R40-R60 | `experiments/residual_progress/side_lane_review_bae3969.md` | 1 | pending |
| B11-residual-R40-R60 | `experiments/residual_progress/side_lane_review_c2319c9.json` | 1 | pending |
| B12-residual-R61-R77 | `experiments/residual_progress/side_lane_review_cbe77bc.json` | 1 | pending |
| B12-residual-R61-R77 | `experiments/residual_progress/side_lane_review_cbe77bc.md` | 1 | pending |
| B12-residual-R61-R77 | `experiments/residual_progress/side_lane_review_d3a91fe.md` | 1 | pending |
| B10-residual-R25-R39 | `experiments/residual_progress/side_lane_review_e3111d3.json` | 1 | pending |
| B12-residual-R61-R77 | `experiments/residual_progress/side_lane_review_fcc7e88.md` | 1 | pending |
| B10-residual-R25-R39 | `reviews/side_lane/batch_436f51f_check.*` | 2 | pending |
| B10-residual-R25-R39 | `reviews/side_lane/batch_64fff1d_check.*` | 2 | pending |
| B09-residual-R11-R24 | `reviews/side_lane/batch_r15_r18_r21_r29_check.*` | 2 | pending |
| B10-residual-R25-R39 | `reviews/side_lane/batch_r33_r36_check.*` | 2 | pending |
| B11-residual-R40-R60 | `reviews/side_lane/batch_r40_r41_check.*` | 2 | pending |
| B11-residual-R40-R60 | `reviews/side_lane/batch_r43_r46_check.*` | 2 | pending |
| B11-residual-R40-R60 | `reviews/side_lane/batch_r51_r54_check.*` | 2 | pending |
| B11-residual-R40-R60 | `reviews/side_lane/batch_r53_check.*` | 2 | pending |
| B11-residual-R40-R60 | `reviews/side_lane/batch_r57_check.*` | 2 | pending |
| B12-residual-R61-R77 | `reviews/side_lane/batch_r61_r67_check.*` | 2 | pending |
| B12-residual-R61-R77 | `reviews/side_lane/batch_r68_r70_check.*` | 2 | pending |
| B12-residual-R61-R77 | `reviews/side_lane/batch_r73_r74_check.*` | 2 | pending |
| B12-residual-R61-R77 | `reviews/side_lane/batch_r75_r77_check.*` | 2 | pending |
| B13-residual-R78-R94 | `reviews/side_lane/batch_r78_r80_check.*` | 2 | pending |
| B13-residual-R78-R94 | `reviews/side_lane/batch_r81_r83_check.*` | 2 | pending |
| B13-residual-R78-R94 | `reviews/side_lane/batch_r84_r85_check.*` | 2 | pending |
| B09-residual-R11-R24 | `reviews/side_lane/r24_check.*` | 2 | pending |
| B11-residual-R40-R60 | `reviews/side_lane/r42_joint_frontier_check.*` | 2 | pending |
| B11-residual-R40-R60 | `reviews/side_lane/r49_ancestor_free.*` | 2 | pending |
| B11-residual-R40-R60 | `reviews/side_lane/r56_selected_inverse_check.*` | 2 | pending |
| B11-residual-R40-R60 | `reviews/side_lane/r58_excess_check.*` | 2 | pending |
| B11-residual-R40-R60 | `reviews/side_lane/r60_cycle_inverse_check.*` | 2 | pending |
| B12-residual-R61-R77 | `reviews/side_lane/r62_compatibility_check.*` | 2 | pending |
| B12-residual-R61-R77 | `reviews/side_lane/r64_lifted_cycle_check.*` | 2 | pending |
| B12-residual-R61-R77 | `reviews/side_lane/r71_mechanical_check.*` | 2 | pending |
| B12-residual-R61-R77 | `reviews/side_lane/r71a_mech_gcd_check.*` | 2 | pending |
| B12-residual-R61-R77 | `reviews/side_lane/r71b_den_mech_check.*` | 2 | pending |
| B12-residual-R61-R77 | `reviews/side_lane/r71c_state_bound_check.*` | 2 | pending |
| B13-residual-R78-R94 | `reviews/side_lane/r82_anchor_lift_check.*` | 2 | pending |
| B13-residual-R78-R94 | `reviews/side_lane/r86_even_exit_check.*` | 2 | pending |
| B13-residual-R78-R94 | `reviews/side_lane/r88_anchor_exhaustive.*` | 1 | pending |
| B13-residual-R78-R94 | `reviews/side_lane/r89_retained_cell_check.*` | 2 | pending |
| B13-residual-R78-R94 | `reviews/side_lane/r90_phi_return_check.*` | 2 | pending |
| B13-residual-R78-R94 | `reviews/side_lane/r92_inverse_tree_check.*` | 2 | pending |
| B13-residual-R78-R94 | `reviews/side_lane/r93_r94_check.*` | 2 | pending |
| B09-residual-R11-R24 | `reviews/side_lane/release_families_check.*` | 2 | pending |
| B09-residual-R11-R24 | `reviews/side_lane/residual_cylinder_core.*` | 2 | pending |
| B09-residual-R11-R24 | `reviews/side_lane/residual_vs_induction.*` | 2 | pending |
| B10-residual-R25-R39 | `reviews/side_lane/run_bridge_check.*` | 2 | pending |
| B11-residual-R40-R60 | `experiments/residual_progress/double_inverse` | 9 | pending |
| B09-residual-R11-R24 | `experiments/residual_progress/duality` | 4 | pending |
| B13-residual-R78-R94 | `experiments/residual_progress/even_exit_history` | 4 | pending |
| B10-residual-R25-R39 | `experiments/residual_progress/even_pair_closure` | 6 | pending |
| B11-residual-R40-R60 | `experiments/residual_progress/exact_absorption_bound` | 4 | pending |
| B12-residual-R61-R77 | `experiments/residual_progress/exit_continuation` | 4 | pending |
| B12-residual-R61-R77 | `experiments/residual_progress/finite_centres` | 4 | pending |
| B09-residual-R11-R24 | `experiments/residual_progress/forcing` | 4 | pending |
| B11-residual-R40-R60 | `experiments/residual_progress/forward_continuation` | 6 | pending |
| B12-residual-R61-R77 | `experiments/residual_progress/frontier_progress` | 4 | pending |
| B13-residual-R78-R94 | `experiments/residual_progress/history_cell_scope` | 4 | pending |
| B13-residual-R78-R94 | `experiments/residual_progress/history_cover_scope` | 4 | pending |
| B13-residual-R78-R94 | `experiments/residual_progress/history_frontier` | 4 | pending |
| B13-residual-R78-R94 | `experiments/residual_progress/history_lifting` | 4 | pending |
| B13-residual-R78-R94 | `experiments/residual_progress/history_transition` | 4 | pending |
| B12-residual-R61-R77 | `experiments/residual_progress/integer_prefix` | 4 | pending |
| B10-residual-R25-R39 | `experiments/residual_progress/inverse_ancestry` | 6 | pending |
| B11-residual-R40-R60 | `experiments/residual_progress/inverse_escape` | 4 | pending |
| B11-residual-R40-R60 | `experiments/residual_progress/inverse_scope` | 5 | pending |
| B12-residual-R61-R77 | `experiments/residual_progress/itinerary_complexity` | 4 | pending |
| B11-residual-R40-R60 | `experiments/residual_progress/joint_frontier` | 6 | pending |
| B10-residual-R25-R39 | `experiments/residual_progress/known_saturation` | 5 | pending |
| B13-residual-R78-R94 | `experiments/residual_progress/later_target_probe` | 3 | pending |
| B12-residual-R61-R77 | `experiments/residual_progress/lattice_cycles` | 4 | pending |
| B13-residual-R78-R94 | `experiments/residual_progress/lower_loop_scope` | 4 | pending |
| B10-residual-R25-R39 | `experiments/residual_progress/merger_scope` | 4 | pending |
| B12-residual-R61-R77 | `experiments/residual_progress/mixed_exit` | 4 | pending |
| B12-residual-R61-R77 | `experiments/residual_progress/mixed_rank_recursion` | 4 | pending |
| B13-residual-R78-R94 | `experiments/residual_progress/native_growth_escape` | 4 | pending |
| B13-residual-R78-R94 | `experiments/residual_progress/native_history` | 5 | pending |
| B13-residual-R78-R94 | `experiments/residual_progress/native_nine` | 4 | pending |
| B13-residual-R78-R94 | `experiments/residual_progress/native_nine_growth` | 4 | pending |
| B11-residual-R40-R60 | `experiments/residual_progress/nonselected_forward` | 4 | pending |
| B11-residual-R40-R60 | `experiments/residual_progress/nonselected_inverse` | 6 | pending |
| B11-residual-R40-R60 | `experiments/residual_progress/nonselected_multiples` | 6 | pending |
| B10-residual-R25-R39 | `experiments/residual_progress/odd_pair_closure` | 6 | pending |
| B10-residual-R25-R39 | `experiments/residual_progress/pair_one` | 5 | pending |
| B10-residual-R25-R39 | `experiments/residual_progress/pair_scope` | 4 | pending |
| B10-residual-R25-R39 | `experiments/residual_progress/paired_completion` | 5 | pending |
| B09-residual-R11-R24 | `experiments/residual_progress/phase_depth` | 3 | pending |
| B11-residual-R40-R60 | `experiments/residual_progress/phase_rank` | 5 | pending |
| B13-residual-R78-R94 | `experiments/residual_progress/phi_exit_control` | 4 | pending |
| B11-residual-R40-R60 | `experiments/residual_progress/rank_mixing` | 3 | pending |
| B12-residual-R61-R77 | `experiments/residual_progress/refined_obstruction` | 5 | pending |
| B12-residual-R61-R77 | `experiments/residual_progress/refined_rules` | 4 | pending |
| B09-residual-R11-R24 | `experiments/residual_progress/release` | 3 | pending |
| B09-residual-R11-R24 | `experiments/residual_progress/release_coverage` | 3 | pending |
| B09-residual-R11-R24 | `experiments/residual_progress/release_packing` | 3 | pending |
| B09-residual-R11-R24 | `experiments/residual_progress/residual_return` | 5 | pending |
| B12-residual-R61-R77 | `experiments/residual_progress/resolved_rules` | 4 | pending |
| B13-residual-R78-R94 | `experiments/residual_progress/retained_history` | 4 | pending |
| B11-residual-R40-R60 | `experiments/residual_progress/returning_continuation` | 4 | pending |
| B11-residual-R40-R60 | `experiments/residual_progress/returning_phase` | 4 | pending |
| B11-residual-R40-R60 | `experiments/residual_progress/rule_avoidance` | 4 | pending |
| B10-residual-R25-R39 | `experiments/residual_progress/second_return` | 5 | pending |
| B11-residual-R40-R60 | `experiments/residual_progress/selected_cycle_exit` | 4 | pending |
| B11-residual-R40-R60 | `experiments/residual_progress/selected_forward` | 4 | pending |
| B11-residual-R40-R60 | `experiments/residual_progress/selected_inverse` | 4 | pending |
| B11-residual-R40-R60 | `experiments/residual_progress/selected_rules` | 4 | pending |
| B13-residual-R78-R94 | `experiments/residual_progress/shadow_precision` | 5 | pending |
| B09-residual-R11-R24 | `experiments/residual_progress/sufficient_sets` | 3 | pending |
| B09-residual-R11-R24 | `experiments/residual_progress/templates` | 11 | pending |
| B09-residual-R11-R24 | `experiments/residual_progress/transport` | 3 | pending |
| B10-residual-R25-R39 | `experiments/residual_progress/tripling_equivalence` | 4 | pending |
| B13-residual-R78-R94 | `experiments/residual_progress/two_source_history` | 4 | pending |
| B12-residual-R61-R77 | `experiments/residual_progress/uniform_pair_scope` | 4 | pending |
| B11-residual-R40-R60 | `experiments/residual_progress/w9_closure` | 6 | pending |
| B13-residual-R78-R94 | `experiments/residual_progress/w9_history_repair` | 4 | pending |
| B09-residual-R11-R24 | `experiments/residual_progress/window_components` | 3 | pending |
| B14-convergence-phase6 | `experiments/phase6/LEDGER.md` | 1 | pending |
| B14-convergence-phase6 | `experiments/phase6/LITERATURE.md` | 1 | pending |
| B14-convergence-phase6 | `experiments/phase6/NEXT_ATTEMPT.md` | 1 | pending |
| B14-convergence-phase6 | `experiments/phase6/README.md` | 1 | pending |
| B14-convergence-phase6 | `experiments/phase6/REPORT.md` | 1 | pending |
| B14-convergence-phase6 | `experiments/phase6/ROUTE_MAP.md` | 1 | pending |
| B14-convergence-phase6 | `experiments/phase6/cycle_fixtures.json` | 1 | pending |
| B14-convergence-phase6 | `experiments/phase6/growth_norm_transport` | 7 | pending |
| B14-convergence-phase6 | `experiments/phase6/linear_density_audit` | 43 | pending |
| B14-convergence-phase6 | `experiments/phase6/setup_verification.json` | 1 | pending |
| B14-convergence-phase6 | `experiments/phase6/side_lane_review_e4f8231.json` | 1 | pending |
| B14-convergence-phase6 | `experiments/phase6/stopping_calibration` | 5 | pending |
| B14-convergence-phase6 | `experiments/phase6/stopping_transport` | 4 | pending |
| B14-convergence-phase6 | `experiments/phase6/transfer_controls.py` | 1 | pending |
| B14-convergence-phase6 | `experiments/phase6/transfer_controls_audit.json` | 1 | pending |
| B14-convergence-phase6 | `reviews/side_lane/p6_001_stopping_check.*` | 2 | pending |
| B14-convergence-phase6 | `reviews/side_lane/p6_002_transport_check.*` | 2 | pending |
| B14-convergence-phase6 | `reviews/side_lane/p6_003_growth_norm_check.*` | 2 | pending |
| B15-convergence-explicit-tao | `experiments/explicit_tao/LOG.md` | 1 | pending |
| B15-convergence-explicit-tao | `experiments/explicit_tao/README.md` | 1 | pending |
| B15-convergence-explicit-tao | `experiments/explicit_tao/STATE.md` | 1 | pending |
| B15-convergence-explicit-tao | `experiments/explicit_tao/check_L2.py` | 1 | pending |
| B15-convergence-explicit-tao | `experiments/explicit_tao/check_L4_window.py` | 1 | pending |
| B15-convergence-explicit-tao | `experiments/explicit_tao/lemmas` | 3 | pending |
| B15-convergence-explicit-tao | `experiments/explicit_tao/receipts` | 2 | pending |
| B15-convergence-explicit-tao | `reviews/side_lane/fable_L2_check.*` | 2 | pending |
| B15-convergence-explicit-tao | `reviews/side_lane/fable_L4_window_check.*` | 2 | pending |
| B16-invariants-viewpoints | `experiments/viewpoints/LOG.md` | 1 | pending |
| B16-invariants-viewpoints | `experiments/viewpoints/MAP.md` | 1 | pending |
| B16-invariants-viewpoints | `experiments/viewpoints/README.md` | 1 | pending |
| B16-invariants-viewpoints | `experiments/viewpoints/V001` | 7 | pending |
| B16-invariants-viewpoints | `experiments/viewpoints/V002` | 8 | pending |
| B16-invariants-viewpoints | `experiments/viewpoints/V003` | 12 | pending |
| B16-invariants-viewpoints | `experiments/viewpoints/V004` | 12 | pending |
| B16-invariants-viewpoints | `experiments/viewpoints/V005` | 10 | pending |
| B16-invariants-viewpoints | `experiments/viewpoints/V006` | 11 | pending |
| B16-invariants-viewpoints | `experiments/viewpoints/V007` | 6 | pending |
| B16-invariants-viewpoints | `experiments/viewpoints/V008` | 7 | pending |
| B16-invariants-viewpoints | `experiments/viewpoints/V009` | 7 | pending |
| B16-invariants-viewpoints | `experiments/viewpoints/briefs` | 5 | pending |
| B16-invariants-viewpoints | `reviews/side_lane/automatic_rigidity_control.*` | 2 | pending |
| B16-invariants-viewpoints | `reviews/side_lane/v003_digit_count_check.*` | 2 | pending |
| B16-invariants-viewpoints | `reviews/side_lane/v004_rigidity_check.*` | 2 | pending |
| B16-invariants-viewpoints | `reviews/side_lane/v005_sparse_growth_check.*` | 2 | pending |
| B16-invariants-viewpoints | `reviews/side_lane/v006_quadratic_check.*` | 2 | pending |
| B16-invariants-viewpoints | `reviews/side_lane/v009_escape_check.*` | 2 | pending |
| B16-invariants-viewpoints | `reviews/side_lane/v13_coloring_check.*` | 2 | pending |
| B16-invariants-viewpoints | `reviews/side_lane/viewpoint_v001_check.*` | 2 | pending |
| B17-leftovers | `.github` | 6 | pending |
| B17-leftovers | `AGENTS.md` | 1 | pending |
| B17-leftovers | `CLAUDE.md` | 1 | pending |
| B17-leftovers | `CONTRIBUTING.md` | 1 | pending |
| B17-leftovers | `README.md` | 1 | pending |
| B17-leftovers | `archive/AGENTS_2026-10-19.md` | 1 | pending |
| B17-leftovers | `archive/COLLATZ_PROGRAMME_MASTER_HANDOFF.md` | 1 | pending |
| B17-leftovers | `archive/README.md` | 1 | pending |
| B17-leftovers | `archive/README_2026-10-19.md` | 1 | pending |
| B17-leftovers | `archive/docs` | 2 | pending |
| B17-leftovers | `archive/side_lane` | 9 | pending |
| B17-leftovers | `docs/CONVENTIONS.md` | 1 | pending |
| B17-leftovers | `docs/FRONTIER.md` | 1 | pending |
| B17-leftovers | `docs/HISTORY.md` | 1 | pending |
| B17-leftovers | `docs/RESULTS.md` | 1 | pending |
| B17-leftovers | `docs/STATUS.md` | 1 | pending |
| B17-leftovers | `experiments/README.md` | 1 | pending |
| B17-leftovers | `reviews/README.md` | 1 | pending |
| B17-leftovers | `reviews/side_lane/README.*` | 1 | pending |
| B11-residual-R40-R60 | `reviews/side_lane/backward_word_rule.*` | 2 | pending |
| B09-residual-R11-R24 | `reviews/side_lane/chain_cancellation_scan.*` | 2 | pending |
| B12-residual-R61-R77 | `reviews/side_lane/closure_frontier_meter.*` | 2 | pending |
| B09-residual-R11-R24 | `reviews/side_lane/coalescence_check.*` | 2 | pending |
| B12-residual-R61-R77 | `reviews/side_lane/complete_core_classes.*` | 2 | pending |
| B09-residual-R11-R24 | `reviews/side_lane/delayed_release_check.*` | 2 | pending |
| B09-residual-R11-R24 | `reviews/side_lane/depth_probe.*` | 2 | pending |
| B09-residual-R11-R24 | `reviews/side_lane/excursion_merge_probe.*` | 2 | pending |
| B11-residual-R40-R60 | `reviews/side_lane/expanded_union_meter.*` | 2 | pending |
| B10-residual-R25-R39 | `reviews/side_lane/fibre_count_check.*` | 2 | pending |
| B12-residual-R61-R77 | `reviews/side_lane/itinerary_complexity_general.*` | 2 | pending |
| B17-leftovers | `reviews/side_lane/jterm_gap_check.*` | 2 | pending |
| B10-residual-R25-R39 | `reviews/side_lane/pair_merge_controls.*` | 2 | pending |
| B09-residual-R11-R24 | `reviews/side_lane/q1_giant_component.*` | 2 | pending |
| B09-residual-R11-R24 | `reviews/side_lane/q2_end_depth.*` | 2 | pending |
| B10-residual-R25-R39 | `reviews/side_lane/quotient_iteration_probe.*` | 2 | pending |
| B11-residual-R40-R60 | `reviews/side_lane/selected_rules_meter.*` | 2 | pending |
| B11-residual-R40-R60 | `reviews/side_lane/sigma_stopping_plans.*` | 2 | pending |
| B09-residual-R11-R24 | `reviews/side_lane/slow_cluster_probe.*` | 2 | pending |
| B11-residual-R40-R60 | `reviews/side_lane/union_acceptance_meter.*` | 2 | pending |
| B11-residual-R40-R60 | `reviews/side_lane/union_gap_map.*` | 2 | pending |
| B17-leftovers | `scripts/check_lean_receipts.py` | 1 | pending |
| B17-leftovers | `scripts/check_links.py` | 1 | pending |
| B17-leftovers | `scripts/run_checks.py` | 1 | pending |
| B17-leftovers | `scripts/verify_all.py` | 1 | pending |
