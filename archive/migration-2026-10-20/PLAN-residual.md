# Migration plan: residual progress (R11–R94) and its side-lane checks

## 0. Facts the plan rests on

- **Where the R-numbers live.** I mapped folders to R-numbers from the links in `_triage/archive/docs/RESULTS.md` (R10–R94). It agrees with `REPORT.md`.
  - **R10 has no folder here.** It lives in `experiments/annular_construction/duality`, which B08 owns. R1–R9 belong to B07. This line starts at R11.
  - **`adjacent_history/` is the only folder without an R-number.** It holds one note: a failed-hypothesis audit, written in the R69–R71 batch, about the R65/R68 interface.
- **Multi-R folders:** R11 is `duality` and `forcing`; R16 is `release` and `release_packing`; R53 is `continued_rules` and `forward_continuation`; R57 is `selected_cycle_exit`, `selected_rules` and `rank_mixing`; R61 is `exit_continuation` and `refined_rules`; R63–R64 share `refined_obstruction`, and R64 also has `resolved_rules`; R78 is `native_nine` and `lower_loop_scope`; R94 is `child_history_scope` and `later_target_probe`.
- **Scripts load sibling folders by name** (`HERE.parent/'<legacy_folder>/x.py'`, `sys.path.insert(HERE.parent/'…')`). Many checkers also hash files relative to `HERE.parents[2]` (the repository root at the legacy depth), and some hash their own note by its legacy name.
  - Node folders get new slug names and sit at a different depth (`areas/convergence/results/<slug>/`). So **almost every residual checker will fail at its new path** and must go under `evidence` with "passed at be73a66 as `<old path>` via `scripts/verify_all.py`".
  - The batch split cannot change this. The clusters in §7 matter for keeping dependencies one-directional and for writing accurate `evidence` notes, not for keeping scripts green.
  - **Likely certificates** (no sibling loads, no repository-relative hashing; confirm each with `_triage/try_script.py`):
    - topic folders: `lattice_cycles/check_balanced_cycles.py`, `cylinder_barrier/check_cylinder_barrier.py`, `bridge_normal_form/check_normal_form.py`, `sufficient_sets/check_recursive_sieve.py`;
    - only if their note is kept byte-identical under its legacy file name next to a new `README.md`, as B04 did with `ROTATION_DEFECTS.md`: `two_source_history`, `child_history_scope`, `uniform_pair_scope`. Each of these hashes its own note by name.
  - **Side-lane probes that import nothing:** `batch_r15_r18_r21_r29_check`, `batch_r68_r70_check`, `r42_joint_frontier_check`, `r71_mechanical_check`, `r71a/b/c`, `r82_anchor_lift_check`, `r89_retained_cell_check`, `r93_r94_check`, `fibre_count_check`, `transfer_3xd`, `itinerary_complexity_general`, and `c0_basin_receipt`, which needs `cc`, so it is evidence.
- **Known failure.** `history_frontier/check_history_frontier.py` pins the hash of `native_history_audit.json` and already failed at `be73a66` (see `archive/legacy-checker-run-be73a66.md`). Mark it evidence with that reason.
- **External loads into B07/B08 material.** Both are backward references:
  - `duality` loads `packet_currents/right_aligned_packets.py`, now `areas/convergence/results/right-aligned-fixed-core-remainder/`.
  - Many side-lane probes import `affine_controls.py` and `progress_measures_audit.py`, now `areas/convergence/results/locally-collatz-like-control-barrier/`.
  - `forcing` loads `annular_construction/components/annular_components.py`; `auxiliary` and `transport` load `annular_construction/arithmetic/check_arithmetic_reductions.py`; `release_packing` loads `annular_construction/arithmetic/combined_partial_current.py`.
  - `templates/check_inverse_exposure.py` and `merger_scope/check_merger_scope.py` load `current_construction/recursive/check_annular_recursion.py`.
  - The B07 slugs are provisional until B07's edit commit lands.
- **Outward loads.** `experiments/phase6/stopping_calibration/check_calibration.py` loads `residual_progress/bridge_normal_form/normal_form.py` and `tripling_equivalence/tripling.py`. Both land in B10, and the phase6 batch must record where they went.
- **Lean.**
  - R71-a, b, c and d are verified units in `_triage/lean/STATE.md`, in `lean/CycleSpectrum.lean` (`LeanLane.Cyc.mech_gcd_one`, `mech_gcd_one_phase`, `mech_D_ne_one`, `den_mech`, `den_rep`, `mech_rep`, `mech_state_bound`, `mech_cycle_state_bound`, `den_mech_gt_one`, …).
  - `PairObligation.lean` (STATE row 4, "R.1/R40 reformulation") belongs to phase6's ROUTE_MAP. The R40 node should mention it in its Remarks, without a `lean:` field.

## 1. The partition: 5 batches by R-range

| Batch | R-range | Topic folders | Files in folders | Note lines (md) | Side-lane stems | Root files |
|---|---|---|---|---|---|---|
| B09-residual-R11-R24 | R11–R24: forcing compiler, exposure templates, release, complement | 16 | 66 | 4843 | 14 | 6 |
| B10-residual-R25-R39 | R25–R39: bridge normal form, run bridges, shrinking pairs, pair domains | 15 | 71 | 4942 | 7 | 5 |
| B11-residual-R40-R60 | R40–R60: critical-nine, rank, inverse phases, selected dispatcher | 24 | 114 | 5335 | 17 | 6 |
| B12-residual-R61-R77 | R61–R77: defects, mixed growth, integer lattice, **R71 to cycles** | 19 | 74 | 4796 | 15 | 10 |
| B13-residual-R78-R94 | R78–R94: native and history line, W9 repair, windows, final child | 19 | 81 | 5496 | 12 | 6 |

- **Why five.** Each batch reads about 5k lines of notes plus 7–17 probes. With four batches each would carry about 6.3k lines, and B09/B10 would hold most of the side-lane volume.
- **Effect on the manifest.** The manifest's current B09–B12 rows are alphabetical. Relabel them as above. Two ways to fit the fifth batch:
  - **(a)** renumber `B13-convergence-phase6` → B14, B14 → B15, B15 → B16, B16 → B17;
  - **(b)** keep the numbers and call the fifth batch `B12b-residual-R78-R94`.
  - Do this in one bookkeeping commit before B09 starts.
- **Rows that move into these batches:**
  - Side-lane rows now under B09 or B11 (`c0_basin_*`, `fixed_h_check`, `negative_cycle_shadows`, `rho_prefix_plans`, `transfer_3xd`) are reassigned in §6.
  - Twenty of the 21 B16 probe rows move into these batches (§6). Only `jterm_gap_check` stays outside.

**Forward links.** I ran a script over every topic-folder note. Under this partition no note links (`../<folder>/`) to a folder in a later batch. Every script dependency also points to an equal or earlier batch (§7). The only forward references are two links in root review files:
- `side_lane_review_767af32.md` (B11) → `exit_continuation/` (B12);
- `PAIR_DOMAIN_REVIEW.md` (B10) → `critical_rank/` (B11).

Both get FOLLOWUPS rows; see §8.

**Conventions for all batches.**
- Area `convergence` unless stated otherwise.
- Aliases are the R-number. The main node of a multi-node unit gets the plain alias; the others get `R13-b`, `R13-c`, ….
- Authors: `ChatGPT main lane (Codex)` for R-nodes; `Claude side lane (Opus)` for side-lane claims.
- Slugs below are suggestions. Check MAP.md for clashes first.

## 2. B09-residual-R11-R24

**Owns.**
- **Topic folders:** `duality`, `forcing`, `transport`, `templates`, `closure`, `auxiliary`, `release`, `release_packing`, `complement`, `alternating`, `release_coverage`, `complement_recursion`, `window_components`, `phase_depth`, `residual_return`, `sufficient_sets`.
- **Root files:** `README.md`, `REPORT.md`, `side_lane_review.json`, `side_lane_review_20261017_2005.json`, `side_lane_review_20261017_latest.md`, `side_lane_review_20261017_latest.json`.
- **Side-lane stems:** `batch_r15_r18_r21_r29_check`, `release_families_check`, `delayed_release_check`, `chain_cancellation_scan`, `depth_probe`, `q1_giant_component`, `q2_end_depth`, `slow_cluster_probe`, `fixed_h_check`, `residual_vs_induction`, `residual_cylinder_core`, `excursion_merge_probe`, `coalescence_check`, `r24_check`.

| Folder | R | What it is | Nodes (kind: slug) | Main dependencies |
|---|---|---|---|---|
| `duality` | R11 | Finite rational cone; a finite rational current with `‖Z⁺‖₁<1` converts to an integer certificate (conditional) | result: `finite-rational-cone-integer-certificate` | R10 (B08), R5 rays (B07) |
| `forcing` | R11 | Actual-graph compiler that keeps boundary terms; forced U112 demo | result: `actual-graph-current-compiler` (R11-b) | R11 |
| `transport` | R12 | Root-collapse/transport normal form (`I, R, Pᵗ, RPᵗ`), surviving atoms | result: `root-transport-normal-form` | B08 arithmetic reductions |
| `templates` | R13 | 3 notes: depth-32 aggregate obstruction; infinite family; unbounded exposure depth for every D | 3 results: `depth-32-aggregate-exposure-obstruction` (R13-b), `depth-32-obstruction-infinite-family` (R13-c), `unbounded-exposure-depth-necessary` (R13) | R10, R6 (B07/B08) |
| `closure` | R14 | Local packet calibration and the sign of the remaining obligation | result: `local-packet-calibration-extension` | R11 (`forcing`) |
| `auxiliary` | R15 | Terminating auxiliary normalisation with an unavoidable remainder | result: `auxiliary-normalisation-remainder` | B08 arithmetic |
| `release` | R16 | Delayed-release cancellation after an unbounded delay | result: `delayed-release-cancellation` | R13, R8 (B07) |
| `release_packing` | R16 | Additional source-packing families (pair and triple) | result: `release-source-packing` (R16-b) | R16, B08 `combined_partial_current` |
| `complement` | R17 | Retained-arrow complement constructor (conditional on inner absorption) | result: `retained-graph-complement-constructor` | R14 |
| `alternating` | R18 | Signed path collapse, intermediate capacity, retained frontiers | result: `signed-path-collapse-capacity` | R15 |
| `release_coverage` | R19 | Phase coverage; the all-phase short-delay candidate is refuted | result: `short-delay-all-phase-obstruction` | R16 |
| `complement_recursion` | R20 | Annular cancellation transferred to exact outer-seed descent | result: `annular-complement-outer-descent` | R16, R17 |
| `window_components` | R21 | Sharp bounded source clusters in the restricted path graph | result: `bounded-source-cluster-local-bound` | R18 |
| `phase_depth` | R22 | Unbounded exposure depth with ternary order fixed at 2 | result: `fixed-ternary-order-unbounded-depth` | R13 |
| `residual_return` | R23 | Halving identity removes half the outer residual (halving coalescence) | result: `halving-coalescence-return` | R17, R20 |
| `sufficient_sets` | R24 | `SUFFICIENT_SETS_AUDIT`: completing the five-ray profile suffices by induction; `RECURSIVE_SIEVE_AUDIT`: a counterexample to one displayed step of Ansari 2025 | result: `five-ray-profile-completion-suffices` (R24); result: `ansari-sieve-step-counterexample` (R24-b); **new source** `ansari-2025-recursive-sieve` | R17, R20, R23 |

**Side-lane placement (node folder).**
- `batch_r15_r18_r21_r29_check` → R15 node; it also covers R18 and R21 here, and R29 in B10, which cites it backward.
- `release_families_check` and `side_lane_review.json` → `release-source-packing`.
- `delayed_release_check`, `chain_cancellation_scan` and `side_lane_review_20261017_2005.json` → `delayed-release-cancellation`.
- `depth_probe` and `q2_end_depth` → `unbounded-exposure-depth-necessary`.
- `q1_giant_component` and `slow_cluster_probe` → optional question `exposure-absorption-giant-component` (the side lane's Q1, with d*(N) as defined in R13). If no question is wanted, attach them to `depth-32-aggregate-exposure-obstruction`.
- `fixed_h_check` → R22.
- `residual_vs_induction`, `residual_cylinder_core`, `excursion_merge_probe` and `side_lane_review_20261017_latest.md/.json` → R17. That review also assesses R22 and R24; cite it from those nodes.
- `coalescence_check` → R23.
- `r24_check` → R24.

**Root files.** `REPORT.md` and `README.md` → `archive/convergence-residual-progress/` with `git mv`, plus a row in `archive/README.md`. Its "content now lives in" column reads: the R11–R94 nodes, aliases in MAP.md.
- Doing this in the first batch gives every later node a stable target for its `## History` line. `archive/` is exempt from link checks, so its links may stay stale.
- Later batches read `REPORT.md` at its archive path.

**Batch notes.**
- Clusters: the `forcing → closure → complement → complement_recursion → residual_return` chain, the `templates → release → release_coverage, phase_depth` chain, and the `auxiliary → alternating → window_components` chain all stay inside B09.
- The side-lane import hubs `depth_probe`, `delayed_release_check` and `residual_vs_induction` also stay in B09. Later importers (`run_bridge_check`, `quotient_iteration_probe` in B10) cite them backward.

## 3. B10-residual-R25-R39

**Owns.**
- **Topic folders:** `bridge_normal_form`, `complementary_bridge`, `absorbed_fibers`, `cylinder_barrier`, `known_saturation`, `second_return`, `bounded_run_cycles`, `merger_scope`, `paired_completion`, `inverse_ancestry`, `pair_scope`, `pair_one`, `tripling_equivalence`, `odd_pair_closure`, `even_pair_closure`.
- **Root files:** `PAIR_DOMAIN_REVIEW.md`, `check_pair_domain_external.py`, `pair_domain_external_review.json`, `side_lane_review_e3111d3.json`, `side_lane_review_1a2dfc5.json`.
- **Side-lane stems:** `run_bridge_check`, `quotient_iteration_probe`, `fibre_count_check`, `batch_64fff1d_check`, `batch_r33_r36_check`, `pair_merge_controls`, `batch_436f51f_check`.

| Folder | R | What it is | Nodes | Main dependencies |
|---|---|---|---|---|
| `bridge_normal_form` | R25 | Elementary bridge classes form an exact quotient; normal form `nu`. Hub module, also used by phase6 | result: `elementary-bridge-quotient-normal-form`; question: `normalised-quotient-termination` ("quotient termination remains open") | R23 |
| `complementary_bridge` | R26 | Complete complementary run bridges; normalised residual coverage | result: `complementary-run-bridges` | R17, R23, R25 |
| `absorbed_fibers` | R27 | Infinitely many known fibres with uniform counts `N/4+O(log N)` | result: `absorbed-fibre-uniform-counts` | R25 |
| `cylinder_barrier` | R28 | Exact symbolic prefix rates; scoped external barrier (+ `external_review.json`, a reproduction of B09 probes) | result: `prefix-rule-cylinder-rate-barrier` | R23, R27 |
| `known_saturation` | R29 | Supplied-path saturation and a finite ordinary certificate core | result: `supplied-path-saturation-core` | R25, R26 |
| `second_return` | R30 | Shrinking paired recursion; growing-return families; Mersenne mergers | result: `shrinking-paired-return-recursion` | R26 |
| `bounded_run_cycles` | R31 | Repeated bounded runs give growth; no finite-label height potential. **Convergence, not cycles**: the "cycles" are repeated valuation words | result: `bounded-runs-exclude-finite-label-potentials` | R26 |
| `merger_scope` | R32 | Scope of merger catalogues, known sets and cylinder rates (+ `external_review.json`, an `r24_check` reproduction) | result: `merger-catalogue-scope` | R24, R28, R29; B08 recursive |
| `paired_completion` | R33 | Mixed shrinking pair rules; binary-cylinder measure | result: `mixed-shrinking-pair-rules` | R30 |
| `inverse_ancestry` | R34 | Decreasing inverse ancestry; unbounded-return lower partners | result: `decreasing-inverse-ancestry` | R26, R29 |
| `pair_scope` | R35 | Tripling/doubling pair decomposition; scope of a restricted catalogue | result: `tripling-doubling-pair-decomposition` | R26 |
| `pair_one` | R36 | Two shrinking entries from the missing 1 (mod 8) pair domain | result: `missing-one-mod-8-pair-domain` | R33 |
| `tripling_equivalence` | R37 | Exact critical tripling domain (bijection `w → nu(3w)`); conditional plans. Also used by phase6 | result: `critical-tripling-domain-equivalence` | R25 |
| `odd_pair_closure` | R38 | Complete odd-h interface and critical input compiler | result: `odd-h-pair-interface-compiler` | R31, R35, R37 |
| `even_pair_closure` | R39 | Coupled even-pair recursion escapes the split-catalogue obstruction | result: `coupled-even-pair-recursion` | R33, R36, R37 |

**Side-lane and root placement.**
- `run_bridge_check` and `quotient_iteration_probe` → R26.
- `fibre_count_check` → R27. It is the import hub of 20 later side-lane checks. Every later `evidence` note should say it imports `fibre_count_check` from this node folder.
- `batch_64fff1d_check` and `side_lane_review_e3111d3.json` → R30; it also covers R31–R36 identities.
- `batch_r33_r36_check` → R33.
- `pair_merge_controls`, `PAIR_DOMAIN_REVIEW.md`, `check_pair_domain_external.py` (self-contained, a certificate candidate) and `pair_domain_external_review.json` → R35. The negative controls test exactly R35's tripling-pair obligation.
- `batch_436f51f_check` and `side_lane_review_1a2dfc5.json` → R37; it covers R37–R39.

**Cluster note.** The `bridge_normal_form`/`complementary_bridge` hub stays together. The pair chain `second_return → paired_completion → pair_one → even_pair_closure` stays inside B10; only `joint_frontier` (R42, B11) reads it later.

## 4. B11-residual-R40-R60

**Owns.**
- **Topic folders:** `w9_closure`, `critical_inverse`, `joint_frontier`, `critical_rank`, `returning_phase`, `nonselected_inverse`, `inverse_escape`, `nonselected_multiples`, `nonselected_forward`, `inverse_scope`, `double_inverse`, `phase_rank`, `returning_continuation`, `continued_rules`, `forward_continuation`, `rule_avoidance`, `selected_forward`, `selected_inverse`, `selected_rules`, `selected_cycle_exit`, `rank_mixing`, `exact_absorption_bound`, `deferred_rank`, `cycle_inverse`.
- **Root files:** `side_lane_review_3d69784.json`, `side_lane_review_bae3969.md`, `side_lane_review_767af32.md`, `side_lane_review_c2319c9.json`, `side_lane_review_64a5981.md`, `side_lane_review_64a5981.json`.
- **Side-lane stems:** `batch_r40_r41_check`, `r42_joint_frontier_check`, `batch_r43_r46_check`, `union_acceptance_meter`, `union_gap_map`, `r49_ancestor_free`, `expanded_union_meter`, `batch_r51_r54_check`, `sigma_stopping_plans`, `batch_r53_check`, `negative_cycle_shadows`, `backward_word_rule`, `r56_selected_inverse_check`, `batch_r57_check`, `selected_rules_meter`, `r58_excess_check`, `r60_cycle_inverse_check`.

| Folder | R | What it is | Nodes | Main dependencies |
|---|---|---|---|---|
| `w9_closure` | R40 | Complete critical-nine elimination leaves one sufficient pair class: tripling currents on W5 | result: `critical-nine-elimination`; question: `universal-w5-tripling-currents` (the line's objective; reuse B07's universal-supply question if one exists) | R37, R38 |
| `critical_inverse` | R41 | Decreasing W5 phase, exact returning branch, exhaustive inverse barrier | result: `decreasing-w5-phase-inverse-barrier` | R40 |
| `joint_frontier` | R42 | Joint-source interfaces keep an unbounded positive frontier | result: `joint-source-unbounded-frontier` | R38, R39 |
| `critical_rank` | R43 | Critical-image rank `rho`; finite signed composition. Also holds `rules_union.py`, the R41/R44–R46 fixed-priority union | result: `critical-image-rank-composition` | R40, R41 (union: R44–R46) |
| `returning_phase` | R44 | Complete returning forward interface; decreasing subdomains | result: `returning-forward-interface` | R41 |
| `nonselected_inverse` | R45 | Base inverse phases allow increasing pair indices | result: `base-inverse-phases-increasing-pairs` | R43 |
| `inverse_escape` | R46 | Variable-depth inverse escape; fixed-precision barrier | result: `variable-depth-inverse-escape-barrier` | R41, R43 |
| `nonselected_multiples` | R47 | Inverse interface for nonselected multiples of 3 | result: `nonselected-multiples-inverse-interface` | R43, R45, R46 |
| `nonselected_forward` | R48 | Complete forward blocks; exact low-exponent tests | result: `forward-blocks-low-exponent-tests` | R26, R44, R46 |
| `inverse_scope` | R49 | Permanent inverse-only exclusions coexist with short forward progress | result: `inverse-only-exclusions-short-forward` | R29, R43, R48 |
| `double_inverse` | R50 | Two inverse phases cross an intermediate increase. Also holds `expanded_union.py`, the seven-rule union | result: `two-inverse-phases-intermediate-increase` | R41, R43, R45, R47, R48 |
| `phase_rank` | R51 | Separate rank `sigma` removes the absorption-bound overhead | result: `sigma-rank-removes-absorption-overhead` | R40, R44, R50 |
| `returning_continuation` | R52 | Second forward interface for returning inputs | result: `returning-second-forward-interface` | R26, R43, R44 |
| `forward_continuation` + `continued_rules` | R53 | Low-block continuation through unbounded prescribed growth. `continued_rules` has no note; its dispatcher code attaches here | result: `low-block-continuation-prescribed-growth` | R48, R50, R52 |
| `rule_avoidance` | R54 | Growing positive prefixes keep an unhandled leading input | result: `growing-prefix-unhandled-leading-input` | R46, R51, R52, R53 |
| `selected_forward` | R55 | Forward tables for selected critical-five inputs | result: `selected-critical-five-forward-tables` | R26, R53, R54 |
| `selected_inverse` | R56 | Two selected inverse choices; fixed-length escape | result: `two-selected-inverse-choices` | R43, R54 |
| `selected_cycle_exit` + `selected_rules` | R57 | Exact guarded cycles and all exit phases; `selected_rules.py` is the twelve-family dispatcher | result: `guarded-cycle-exit-phases`; dispatcher code attached as evidence | R54, R55, R56 |
| `rank_mixing` | (R57) | Finite survey of mixing the `rho` and `sigma` dispatchers; compatibility unresolved | attempt: `rho-sigma-rank-mixing` | R51, R53 |
| `exact_absorption_bound` | R58 | Exact classification of rank excess in formal absorption | result: `rank-excess-absorption-classification` | R51, R57 |
| `deferred_rank` | R59 | Deferred original-rank testing; exact larger-request cancellation | result: `deferred-original-rank-testing` | R55, R57 |
| `cycle_inverse` | R60 | Maximal inverse-cycle continuation (cycle word of −17) with a descent table. **Convergence, not cycles** | result: `maximal-inverse-cycle-continuation` | R56, R57, R59 |

**Side-lane and root placement.**
- `batch_r40_r41_check` → R40.
- `r42_joint_frontier_check` → R42.
- `batch_r43_r46_check`, `union_acceptance_meter`, `union_gap_map` and `side_lane_review_3d69784.json` → R43, because `rules_union.py` lives there.
- `r49_ancestor_free` → R49.
- `expanded_union_meter` → R50.
- `batch_r51_r54_check` and `sigma_stopping_plans` → R51. The sigma stopping-plan claim stays evidence; measurements stay labelled as such.
- `batch_r53_check` → R53.
- `negative_cycle_shadows` → R54 (R53/R54 blocks as 2-adic shadows of the negative cycles −5, −17).
- `backward_word_rule`, `side_lane_review_bae3969.md` and `side_lane_review_767af32.md` → R56. bae3969 shows the backward word's domain is exactly R56's k4 domain; 767af32 re-assesses it and records a strategic decision.
- `r56_selected_inverse_check` → R56.
- `batch_r57_check` and `selected_rules_meter` → R57.
- `r58_excess_check` and `side_lane_review_c2319c9.json` → R58.
- `r60_cycle_inverse_check` and `side_lane_review_64a5981.md/.json` → R60. 64a5981 also covers R81, R83 and R84–R87, all in B13, which cite it backward.

**Cluster note.** The W9/rank cluster stays whole: `tripling(B10) → w9_closure → critical_inverse → returning_phase / inverse_escape / critical_rank → nonselected_* → double_inverse → phase_rank`. So does the dispatcher cluster: `continued_rules, forward_continuation, rule_avoidance, selected_*` and the three R58–R60 dispatcher consumers.

## 5. B12-residual-R61-R77 (includes the cycles material)

**Owns.**
- **Topic folders:** `exit_continuation`, `refined_rules`, `defect_resolution`, `refined_obstruction`, `resolved_rules`, `defect_normal_form`, `all_ray_continuation`, `mixed_rank_recursion`, `adjacent_recursion`, `adjacent_history`, `arithmetic_progress`, `mixed_exit`, `lattice_cycles`, `finite_centres`, `frontier_progress`, `integer_prefix`, `critical_basis`, `uniform_pair_scope`, `itinerary_complexity`.
- **Root files:** `side_lane_review_13590c1.md/.json`, `side_lane_review_678e565.md/.json`, `side_lane_review_33c3829.md/.json`, `side_lane_review_cbe77bc.md/.json`, `side_lane_review_d3a91fe.md`, `side_lane_review_fcc7e88.md`.
- **Side-lane stems:** `batch_r61_r67_check`, `closure_frontier_meter`, `complete_core_classes`, `r62_compatibility_check`, `rho_prefix_plans`, `r64_lifted_cycle_check`, `batch_r68_r70_check`, `r71_mechanical_check`, `r71a_mech_gcd_check`, `r71b_den_mech_check`, `r71c_state_bound_check`, `transfer_3xd`, `batch_r73_r74_check`, `batch_r75_r77_check`, `itinerary_complexity_general`.

| Folder | R | What it is | Nodes | Main dependencies |
|---|---|---|---|---|
| `exit_continuation` | R61 | Whole exponent-eleven exit; scoped limit of a continuation procedure | result: `exponent-eleven-exit-continuation` | R41, R58, R59, R60 |
| `refined_rules` | R61 | Fifteen-family dispatcher with signed closure | result: `fifteen-rule-dispatcher` (R61-b), or fold into R61 as evidence | R57–R60 |
| `defect_resolution` | R62 | Original-rank resolution of the unique absorption defect (compatibility theorem) | result: `absorption-defect-original-rank-resolution` | R58, R61 |
| `refined_obstruction` | R63, R64 | `REFINED_ELEVEN.md` (R63) and `LIFTED_CYCLE.md` (R64) | results: `exponent-eleven-fifteen-rule-classification` (R63), `lifted-inverse-ray-cycle` (R64) | R56, R59–R62 |
| `resolved_rules` | R64 | Seventeen-rule resolver with maximal continuation thresholds | result: `lifted-ray-continuation-thresholds` (R64-b), or merge with R64 | R62, R63 |
| `defect_normal_form` | R65 | The returning defect as an adjacent-source comparison (triangular equivalence) | result: `adjacent-source-defect-equivalence` | R58 |
| `all_ray_continuation` | R66 | Ray-index decision; uniform integer-count obstruction | result: `ray-index-decision-count-obstruction` | R63, R64 (scripts: R40, R43, R56, R60) |
| `mixed_rank_recursion` | R67 | Arbitrarily long growing blocks from actual mixed-rank comparisons | result: `mixed-rank-growing-blocks` | R62 |
| `adjacent_recursion` | R68 | Native-height inverse obstruction with a fixed forward comparison | result: `native-height-inverse-obstruction` | R44, R65 |
| `adjacent_history` | — | Failed hypothesis: retained lower currents do not escape the adjacent interface | attempt: `retained-lower-currents-adjacent-source` | R29, R65, R68 |
| `arithmetic_progress` | R69 | Valuation debt transport; a complete reset obstruction | result: `valuation-debt-reset-obstruction` | R44, R51, R67 |
| `mixed_exit` | R70 | Complete mixed exits; growing conditional re-entry | result: `mixed-exit-growing-reentry` | R26, R44, R67 |
| `lattice_cycles` | R71 | **Cycles.** Exact denominators of mechanical valuation words; rational controls | see §5a | — |
| `finite_centres` | R72 | No finite affine-valuation rank for the fixed mixed phases | result: `no-finite-affine-valuation-rank` | R44, R69 |
| `frontier_progress` | R73 | Exact normalisation and cancellation of signed pair frontiers | result: `signed-pair-frontier-normalisation` | R67, R69 |
| `integer_prefix` | R74 | Complete integer cylinders for every finite mixed exit-18 return word. **Convergence**; its periodic-word remark is local to the subsystem | result: `exit18-return-integer-cylinders`; question: `aperiodic-exit18-return-survivors` (R74/R77 open) | R67, R70 |
| `critical_basis` | R75 | Common critical rank after keeping both pair types (hub for B13) | result: `common-critical-rank-basis` | R37, R51, R67 |
| `uniform_pair_scope` | R76 | Complete exclusion of one uniform fixed-word pair model | result: `uniform-fixed-word-pair-exclusion` | R75 |
| `itinerary_complexity` | R77 | Same-seed factor complexity `> 18.285`; finite return bound | result: `same-seed-factor-complexity-bound` | R67, R74 |

**Side-lane and root placement.**
- `batch_r61_r67_check` → R61.
- `closure_frontier_meter` and `complete_core_classes` → R61-b (both measure `refined_rules.close`).
- `r62_compatibility_check` → R62.
- `rho_prefix_plans` and `side_lane_review_33c3829.md/.json` → a new side-lane result `quotient-prefix-plans-rho-decreasing` (R62-b). It is a side-lane written proof using R43, R51 and R62(1), reviewed by the main lane in 33c3829, so it can be `reviewed`. It imports `backward_word_rule` from the B11 R56 folder.
- `r64_lifted_cycle_check` and `side_lane_review_cbe77bc.md/.json` → R64.
- `batch_r68_r70_check` → R68.
- `batch_r73_r74_check` and `side_lane_review_d3a91fe.md` → R74.
- `batch_r75_r77_check` → R75.
- `itinerary_complexity_general` and `side_lane_review_fcc7e88.md` → a new side-lane result `divergent-orbit-itinerary-complexity` (R77-b). It claims `liminf p(L)/L ≥ 1/log₂(3/2)` for every divergent odd-only orbit, "likely known", so novelty is undetermined. fcc7e88 reviews the general argument, so it can be `reviewed`.

### 5a. Cycle-area material: `lattice_cycles` (R71) goes to `areas/cycles/`

R71 is a restricted cycle result with Lean units R71-a to R71-d, all verified. B03, B04 and B05 left FOLLOWUPS rows waiting for "the R71 node". Proposed nodes:

1. **result `mechanical-word-exact-denominator`** (aliases `R71`, `R71-a`, `R71-b`; `BALANCED_DENOMINATORS.md` §§1–2).
   - Claim: for the mechanical word `mech(A,k,l)` with `2^A > 3^k`, the reduced denominator is `2^(A/g) − 3^(k/g)` with `g = gcd(A,k)`.
   - Primitive case: `gcd(C,D) = 1` in every phase.
   - Mod 8: no nontrivial integer cycle in the family; only the all-2 word, giving cycle `{1}`.
   - Status: `formal`, provided `## Lean` can state the match from STATE R71-a/b. The declarations are `mech_gcd_one`, `mech_gcd_one_phase`, `mech_D_ne_one`, `gcd_rotate_eq`, `den_mech`, `den_rep`, `mech_rep`. Otherwise `reviewed`, with `reviewed_by` citing `r71_mechanical_check` and `r71a/b` (side lane) and the Lean lane.
   - `assumes`/related: cite `knight-2026-high-cycles` and `halbeisen-1997-rational-cycles` (they exist); write "published antecedents, no novelty claimed".
   - Attach: `BALANCED_DENOMINATORS.md` (becomes README), `balanced_cycles.py`, `check_balanced_cycles.py` (certificate candidate), the receipt, `r71_mechanical_check.*`, `r71a_mech_gcd_check.*`, `r71b_den_mech_check.*`, `side_lane_review_13590c1.*`.
   - `r71c_state_bound_check.py` goes in node 2, but `areas/cycles/results/ordered-cycle-sparse-forcing/c006b_erun_check.py` imports it by module name. Record that in node 2's evidence, and resolve the FOLLOWUPS row in §8.
2. **result `mechanical-cycles-high-rational-controls`** (aliases `R71-c`, `R71-d`; §3).
   - Every state exceeds `k/6`; `den > 1` for `k ≥ 3`. So the integer `3x+d` controls lie above any multiple of `d`, **with `d` varying**. They give no fixed-`d` high cycles.
   - Status `formal` per STATE R71-c/d (`mech_state_bound`, `mech_cycle_state_bound`, `den_mech_gt_one`).
   - `depends_on` node 1. Attach `r71c_state_bound_check.*`.
3. **attempt (optional) `scaling-transfer-to-3x-plus-d`** (§0 "Why this matters for the side-lane transfer").
   - The map `S_d(dy) = d·S_1(y)` transports local identities but not the integer lattice. Covariance alone cannot reduce `d` to a finite base check.
   - Attach `transfer_3xd.*` and `side_lane_review_678e565.*`. Status: `transfer_3xd` checks R23/R54/`18u+5` identities in `3x+d` form, which is convergence material, but R71 §0 is where it is judged.
   - Alternative: keep these files as evidence in node 1 and create no attempt.

**Checked and staying in convergence:**
- `integer_prefix` (R74): exit-18 return words. Its "eventually periodic ⇒ negative rational point" holds only inside the subsystem.
- `bounded_run_cycles` (R31): growth from repeated bounded-run words; the obstruction is about potentials.
- `cycle_inverse` (R60): inverse comparisons that follow the cycle word of −17.
- Probe `negative_cycle_shadows`: R53/R54 blocks as 2-adic shadows of negative `3x+1` cycles.
- Probe `transfer_3xd`: as above, with R71.
- `shadow_precision` and `deeper_window` (B13) use negative rational basins (c0); they are convergence.

**B12 must resolve FOLLOWUPS.** The B03 rows (`narrow-cycles-are-mechanical`, `rotation-block-exclusion`, `perturbed-mechanical-block-family`, `rotating-mechanical-two-block-family`, `narrow-cycle-spectrum-law`, `close-pair-lattice-criterion`), the B04 rows (`two-defect-cancellation-bound`, `local-odd-rounding-exclusion`) and the B05 rows (`single-forced-position-denominator`, `ordered-cycle-run-renormalisation`) all point to R71. They get `depends_on: mechanical-word-exact-denominator`, or `mechanical-cycles-high-rational-controls` where the `k/6` bound is used: `perturbed-mechanical-block-family` and `rotating-mechanical-two-block-family`.

**Cluster note.** These stay in B12: `mixed_rank_recursion → mixed_exit → integer_prefix → itinerary_complexity`; `arithmetic_progress → frontier_progress, finite_centres`; and the defect/resolver chain `refined_rules → defect_resolution → resolved_rules`, `refined_obstruction → all_ray_continuation`, `defect_normal_form → adjacent_recursion`. `critical_basis` is a hub imported by seven B13 folders; they import it backward.

## 6. B13-residual-R78-R94

**Owns.**
- **Topic folders:** `native_nine`, `lower_loop_scope`, `native_nine_growth`, `native_history`, `history_lifting`, `history_frontier`, `native_growth_escape`, `history_transition`, `history_cover_scope`, `even_exit_history`, `w9_history_repair`, `history_cell_scope`, `retained_history`, `phi_exit_control`, `shadow_precision`, `deeper_window`, `two_source_history`, `child_history_scope`, `later_target_probe`.
- **Root files:** `side_lane_review_9849c53.md`, `side_lane_review_b9203ff.md`, `side_lane_review_86ead16.md/.json`, `side_lane_review_8ed32bc.md/.json`.
- **Side-lane stems:** `batch_r78_r80_check`, `batch_r81_r83_check`, `r82_anchor_lift_check`, `batch_r84_r85_check`, `r86_even_exit_check`, `r88_anchor_exhaustive` (`.c` only), `r89_retained_cell_check`, `r90_phi_return_check`, `c0_basin_classify` (`.c` only), `c0_basin_receipt`, `r92_inverse_tree_check`, `r93_r94_check`.

| Folder | R | What it is | Nodes | Main dependencies |
|---|---|---|---|---|
| `native_nine` | R78 | Native critical-nine continuation at the original rank | result: `native-critical-nine-continuation` | R40, R52, R55, R56, R75 |
| `lower_loop_scope` | R78 | Lower relations of the immediate blocked-W9/E self-loop | result: `immediate-self-loop-lower-relations` (R78-b) | R75 |
| `native_nine_growth` | R79 | Native return counts; full original-rank exit obstruction | result: `native-growth-original-rank-exit-obstruction` | R45, R75 |
| `native_history` | R80 | A high smaller-origin history beats arbitrarily deep inverse barriers | result: `high-smaller-origin-history` | R44, R49, R52, R64, R75 |
| `history_lifting` | R81 | Maximal fixed-word history cells; original-rank transport | result: `fixed-word-history-cells` | R44, R52, R75, R80 |
| `history_frontier` | R82 | All-ray history classification from a finite supplied anchor | result: `finite-anchor-history-classification` | R80 |
| `native_growth_escape` | R83 | High histories beyond every prescribed native growth depth | result: `history-beyond-prescribed-growth` | R79 |
| `history_transition` | R84 | Later-target decision; sharp twenty-step quotient descent | result: `later-target-twenty-step-descent` | R44, R52, R75, R81 |
| `history_cover_scope` | R85 | All-ray exclusion of uniformly bounded smaller-history clocks | result: `bounded-history-clock-exclusion` | R25 |
| `even_exit_history` | R86 | Exact smaller-target cone after an even complementary exit | result: `even-exit-smaller-target-cone` | R48, R64, R75 |
| `w9_history_repair` | R87 | Every failed R84 W9 leader reduces to at most one higher W5 input | result: `failed-w9-leader-reduction` | R40, R46, R84 |
| `history_cell_scope` | R88 | Four-target history classification on a whole cell | result: `four-target-history-classification` | R25, R82, R87 |
| `retained_history` | R89 | Retained lower histories give a sharp three-node W9 reduction | result: `retained-history-w9-reduction` | R26, R73, R87, R88 |
| `phi_exit_control` | R90 | Binary return and maximal-exit control at the original rank | result: `binary-return-exit-control` | R89 |
| `shadow_precision` | R91 | A finite rational basin proves an all-word precision barrier (computer-assisted; C++ `independent_basin.cpp`) | result: `rational-basin-precision-barrier` | R88, R90 |
| `deeper_window` | R92 | `DEEPER_WINDOW.md`: 14 more history steps give only the original source. `CANDIDATE.md` is a historical draft resolved by R92. `NEXT_TARGET.md` is a research template | result: `fourteen-step-window-original-source`; `CANDIDATE.md` attached as evidence; question: `common-tail-comparison-after-r92` (from NEXT_TARGET; known progress R94) | R90, R91 |
| `two_source_history` | R93 | Two-source normalisation; reduces the pair to `[864z−257]−[z]` | result: `two-source-normalisation-first-departure`; question: `residual-pair-864z-257-supply` (the line's final open target) | R90, R92 |
| `child_history_scope` | R94 | The prescribed ternary child cannot use bounded clocks | result: `prescribed-ternary-child-unbounded-clocks` | R44, R83, R93 |
| `later_target_probe` | (R94) | A later Phi-exit target still defeats the two-ray/point procedure (finite witness) | attempt: `two-ray-point-procedure-later-target` | R44, R64, R83, R90 |

**Side-lane and root placement.**
- `batch_r78_r80_check` and `side_lane_review_9849c53.md` → R80.
- `batch_r81_r83_check` → R81.
- `r82_anchor_lift_check` → R82.
- `batch_r84_r85_check` and `side_lane_review_b9203ff.md` → R84. b9203ff also corrects the R81 probe's coverage claim; cite it from R81.
- `r86_even_exit_check` → R86.
- `r88_anchor_exhaustive.c` → R88.
- `r89_retained_cell_check` → R89.
- `r90_phi_return_check` and `side_lane_review_86ead16.md/.json` → R90 (it also covers R91 and R92).
- `c0_basin_classify.c`, `c0_basin_receipt.*` and `side_lane_review_8ed32bc.md/.json` → R91. It also validates the deeper-window candidate; cite it from R92.
- `r92_inverse_tree_check` → R92.
- `r93_r94_check` → R93; cite it from R94.

**Cluster note.** These stay in B13: `retained_history → phi_exit_control → shadow_precision → deeper_window`; `history_transition → w9_history_repair → history_cell_scope`; `native_history → history_frontier`; `native_nine_growth → native_growth_escape → later_target_probe`.

## 7. Script dependency clusters (folder → folders it loads)

| Cluster | Edges (all within or into earlier batches) | Batch |
|---|---|---|
| Annular / forcing | forcing→duality; closure→forcing; complement→closure; complement_recursion→{complement, release, release_packing}; residual_return→complement_recursion; release→templates; release_coverage→{release, templates}; phase_depth→templates; alternating→auxiliary; window_components→alternating. External: B07, B08 (§0) | B09 |
| Bridge hub | absorbed_fibers, known_saturation, merger_scope, tripling_equivalence, bounded_run_cycles, odd_pair_closure→bridge_normal_form; complementary_bridge→{bridge_normal_form, residual_return(B09)}; bounded_run_cycles, inverse_ancestry, known_saturation, pair_scope, second_return→complementary_bridge. Later readers: history_cover_scope, history_cell_scope (hash of the note) (B13); nonselected_forward, returning_continuation, selected_cycle_exit (B11); retained_history (B13); phase6 | B10 |
| Pair chain | paired_completion→second_return; pair_one→paired_completion; even_pair_closure→pair_one; joint_frontier(B11)→even_pair_closure | B10 (→B11) |
| W9 / rank | w9_closure→tripling_equivalence(B10); critical_inverse→w9_closure; returning_phase, inverse_escape→critical_inverse; critical_rank→{critical_inverse, inverse_escape, nonselected_inverse, returning_phase}; nonselected_inverse→critical_rank; nonselected_multiples→{nonselected_inverse, inverse_escape}; nonselected_forward→{complementary_bridge, inverse_escape, returning_phase}; inverse_scope→{critical_rank, known_saturation}; double_inverse→{critical_rank, nonselected_inverse, nonselected_forward, nonselected_multiples}; phase_rank→double_inverse | B11 |
| Selected dispatcher | continued_rules→{double_inverse, forward_continuation, returning_continuation}; forward_continuation→{double_inverse, critical_rank, nonselected_forward}; rule_avoidance→{double_inverse, forward_continuation, phase_rank, returning_continuation}; selected_forward→{continued_rules, critical_rank, nonselected_forward}; selected_inverse→critical_rank; selected_cycle_exit→{complementary_bridge, returning_phase, rule_avoidance, selected_forward, selected_inverse}; selected_rules→{continued_rules, selected_cycle_exit, selected_forward, selected_inverse}; rank_mixing→{continued_rules, phase_rank}; deferred_rank→selected_rules; cycle_inverse→{selected_inverse, selected_cycle_exit, selected_rules}; exact_absorption_bound→{critical_rank, nonselected_forward, selected_rules} | B11 |
| Defect resolvers | exit_continuation→{double_inverse, nonselected_inverse, selected_cycle_exit, selected_rules}; refined_rules→{cycle_inverse, deferred_rank, exact_absorption_bound, selected_rules}; defect_resolution→{phase_rank, refined_rules, returning_continuation, returning_phase}; refined_obstruction→{cycle_inverse, deferred_rank, exit_continuation, refined_rules, selected_inverse}; resolved_rules→{defect_resolution, refined_obstruction, refined_rules}; defect_normal_form→{critical_rank, exact_absorption_bound, returning_phase}; all_ray_continuation→{refined_obstruction, critical_rank, cycle_inverse, selected_inverse, w9_closure}; adjacent_recursion→defect_normal_form | B12 |
| Mixed growth | mixed_rank_recursion→defect_resolution; mixed_exit→mixed_rank_recursion; integer_prefix→mixed_exit; itinerary_complexity→integer_prefix (hash of the note); arithmetic_progress→{mixed_rank_recursion, phase_rank, returning_phase, critical_rank}; frontier_progress→arithmetic_progress; finite_centres→{arithmetic_progress, critical_inverse, critical_rank, mixed_rank_recursion, phase_rank, returning_phase, tripling_equivalence, w9_closure}; critical_basis→phase_rank | B12 |
| History | lower_loop_scope, native_nine, native_nine_growth, native_history, history_lifting, history_transition, even_exit_history→critical_basis(B12); native_history→{resolved_rules, returning_continuation}; history_frontier→native_history (pinned receipt hash); native_growth_escape→native_nine_growth; w9_history_repair→history_transition; history_cell_scope→{bridge_normal_form, history_frontier, w9_history_repair}; retained_history→{complementary_bridge, frontier_progress, w9_history_repair}; phi_exit_control→retained_history; shadow_precision→{history_cell_scope, phi_exit_control}; deeper_window→{shadow_precision, phi_exit_control}; later_target_probe→{phi_exit_control, resolved_rules, native_growth_escape}; even_exit_history→{resolved_rules, nonselected_forward} | B13 |
| Standalone | lattice_cycles, cylinder_barrier, sufficient_sets, uniform_pair_scope, two_source_history, child_history_scope, adjacent_history (note only), bridge_normal_form (as importer) | various |

**Side-lane import hubs**, imported by module name from the importer's own folder. After the moves, each importer's `evidence` must say where its helper landed:
- `fibre_count_check` (B10, R27) is imported by `batch_436f51f`, `batch_r33_r36`, `batch_r40_r41`, `batch_r43_r46`, `batch_r51_r54`, `batch_r53`, `batch_r57`, `batch_r61_r67`, `batch_r75_r77`, `batch_r78_r80`, `batch_r84_r85`, `r49`, `r56`, `r60`, `r86`, `r90`, `r92`, `run_bridge_check`, `quotient_iteration_probe`, `expanded_union_meter`, `selected_rules_meter`, `union_gap_map` and `negative_cycle_shadows`.
- `depth_probe` (B09) ← `delayed_release_check`, `slow_cluster_probe`, `fixed_h_check`.
- `delayed_release_check` (B09) ← `chain_cancellation_scan`, `fixed_h_check`.
- `residual_vs_induction` (B09) ← `coalescence_check`, `excursion_merge_probe`, `run_bridge_check` (B10), `quotient_iteration_probe` (B10).
- `run_bridge_check` (B10) ← `quotient_iteration_probe`.
- `backward_word_rule` (B11) ← `sigma_stopping_plans` (B11), `rho_prefix_plans` (B12), `r62_compatibility_check` (B12).
- `union_acceptance_meter` (B11) ← `union_gap_map`.
- Probes that load residual folders by path: `negative_cycle_shadows`, `backward_word_rule` → `phase_rank`, `continued_rules`; `closure_frontier_meter`, `complete_core_classes` → `refined_rules`; `union_acceptance_meter`, `r58_excess_check` → `critical_rank`; `expanded_union_meter` → `double_inverse`; `selected_rules_meter` → `selected_rules`.

All of these break at the new paths and become evidence-only. The partition keeps each helper in the same batch as its importers, or in an earlier one.

## 8. The 21 previously unassigned probes

| Probe | Belongs to | Batch and node |
|---|---|---|
| `backward_word_rule` | residual R54/R56 | B11, R56 `two-selected-inverse-choices` |
| `chain_cancellation_scan` | residual R16 (side lane's Q3) | B09, `delayed-release-cancellation` |
| `closure_frontier_meter` | residual R61 | B12, R61-b `fifteen-rule-dispatcher` |
| `coalescence_check` | residual R23 | B09, `halving-coalescence-return` |
| `complete_core_classes` | residual R61 | B12, R61-b |
| `delayed_release_check` | residual R16 | B09, `delayed-release-cancellation` |
| `depth_probe` | residual R13 | B09, `unbounded-exposure-depth-necessary` |
| `excursion_merge_probe` | residual R17 (side lane's Q6) | B09, `retained-graph-complement-constructor` |
| `expanded_union_meter` | residual R50 | B11, `two-inverse-phases-intermediate-increase` |
| `fibre_count_check` | residual R27 | B10, `absorbed-fibre-uniform-counts` |
| `itinerary_complexity_general` | residual R77 (general form) | B12, new `divergent-orbit-itinerary-complexity` |
| `jterm_gap_check` | **not residual: cycles, S-series C005/C006** (`reviews/side_lane/README.md` lists it as an S-series producer) | Stays B16, but should land in cycles node `ordered-gap-closed-form` (B05), where FOLLOWUPS rows from B04 and B05 already wait for it |
| `pair_merge_controls` | residual R35 (negative controls) | B10, `tripling-doubling-pair-decomposition` |
| `q1_giant_component` | residual R13 (side lane's Q1, d*(N)) | B09, question `exposure-absorption-giant-component` |
| `q2_end_depth` | residual R13 (side lane's Q2) | B09, `unbounded-exposure-depth-necessary` |
| `quotient_iteration_probe` | residual R25/R26 | B10, `complementary-run-bridges` |
| `selected_rules_meter` | residual R57 | B11, `guarded-cycle-exit-phases` (receipt nondeterministic, per `reviews/side_lane/README.md`) |
| `sigma_stopping_plans` | residual R51 | B11, `sigma-rank-removes-absorption-overhead` |
| `slow_cluster_probe` | residual R13 (d*(N) along the ×64 ladder) | B09, with `q1_giant_component` |
| `union_acceptance_meter` | residual R43–R46 union | B11, `critical-image-rank-composition` |
| `union_gap_map` | residual R43–R46 union | B11, `critical-image-rank-composition` |

**Nothing goes to phase6, explicit_tao or viewpoints/invariants.**
- `slow_cluster_probe` and `q1_giant_component` measure the annulus `A_N` of R6, which B07/B08 own. They are kept with residual R13 because they measure R13's d*(N).
- `pair_merge_controls`, `r24_check` and others import B07's `affine_controls`; that is only a code dependency.
- **Receipt flag:** `q1_giant_component.json` and `selected_rules_meter.json` are nondeterministic, so they can never be certificates.

## 9. Root files → nodes (all 33)

| File(s) | Destination | Role |
|---|---|---|
| `README.md`, `REPORT.md` | `archive/convergence-residual-progress/` (B09) | Round-by-round narrative and line index; `archive/README.md` row |
| `side_lane_review.json` | B09 `release-source-packing` | Main-lane reproduction of `release_families_check` and `depth_probe` (R16/R13) |
| `side_lane_review_20261017_2005.json` | B09 `delayed-release-cancellation` | Reproduction of `delayed_release_check`, `chain_cancellation_scan`, `depth_probe` |
| `side_lane_review_20261017_latest.md/.json` | B09 `retained-graph-complement-constructor` | Review of the residual-cylinder and induction feed (R17; also R22, R24) |
| `side_lane_review_e3111d3.json` | B10 `shrinking-paired-return-recursion` (R30) | Reproduction of `batch_64fff1d_check` (R30–R36) |
| `PAIR_DOMAIN_REVIEW.md`, `check_pair_domain_external.py`, `pair_domain_external_review.json` | B10 `tripling-doubling-pair-decomposition` (R35) | External pair-domain evidence (R33–R36 checks, `pair_merge_controls`); the checker is a self-contained certificate candidate |
| `side_lane_review_1a2dfc5.json` | B10 R37 | Reproduction of `batch_436f51f_check` (R37–R39) |
| `side_lane_review_3d69784.json` | B11 R43 | Reproduction of `batch_r43_r46_check` |
| `side_lane_review_bae3969.md`, `side_lane_review_767af32.md` | B11 R56 | Backward-word review; strategic re-assessment of the same formula |
| `side_lane_review_c2319c9.json` | B11 R58 | Reproduction of `r58_excess_check` |
| `side_lane_review_64a5981.md/.json` | B11 R60 | R60 and R86 probes; R81/R83 correction |
| `side_lane_review_13590c1.md/.json`, `side_lane_review_678e565.md/.json` | B12, cycles `mechanical-word-exact-denominator` (or the optional transfer attempt) | `r71_mechanical_check` and `transfer_3xd` reproductions |
| `side_lane_review_33c3829.md/.json` | B12 `quotient-prefix-plans-rho-decreasing` | Main-lane review of the side lane's stopping-threshold argument |
| `side_lane_review_cbe77bc.md/.json` | B12 R64 | `r64_lifted_cycle_check` |
| `side_lane_review_d3a91fe.md` | B12 R74 | `batch_r73_r74_check` |
| `side_lane_review_fcc7e88.md` | B12 `divergent-orbit-itinerary-complexity` | `batch_r75_r77` and the general complexity argument |
| `side_lane_review_9849c53.md` | B13 R80 | `batch_r78_r80_check` |
| `side_lane_review_b9203ff.md` | B13 R84 | `batch_r84_r85_check`; R81 correction |
| `side_lane_review_86ead16.md/.json` | B13 R90 | R90 checks; R91/R92 assessment |
| `side_lane_review_8ed32bc.md/.json` | B13 R91 | c0-basin reproduction |

Each review gives a `reviewed_by` entry, for example `by: ChatGPT main lane (Codex)`, `link: <file>`, with a `scope` naming the finite checks it reproduced. That entry goes on the side-lane-authored node it reviews. These are not reviews of the main-lane R-results.

## 10. Cross-batch dependencies and FOLLOWUPS

**Order:** B07 (in progress) → B08 → B09 → B10 → B11 → B12 → B13, then phase6. B12 should not be reordered, because it resolves the R71 rows.

**Backward references:**
- B09 depends on B07 (R5, R6, R8, `affine_controls`, `right_aligned_packets`) and B08 (R10, annular arithmetic and components, `check_annular_recursion`).
- B10 depends on B09 (R17, R20, R23, R24; `residual_vs_induction`).
- B11 depends on B10 (R25, R26, R29, R37, R38; `fibre_count_check`).
- B12 depends on B11 (R40–R60, `backward_word_rule`) and resolves the B03–B05 rows for R71.
- B13 depends on B12 (R64, R73, R75; `critical_basis`), B11 (R40, R44–R52) and B10 (R25, R26).

**FOLLOWUPS rows to add:**

| Created by | Node | Missing target | What to add |
|---|---|---|---|
| B10 | R35 `tripling-doubling-pair-decomposition` (`PAIR_DOMAIN_REVIEW.md`) | R43 `critical_rank` (B11) | Turn the link into a node link (the review is not hash-pinned) |
| B11 | R56 node (`side_lane_review_767af32.md`) | R61 `exit_continuation` (B12) | Same |
| B03 (existing, resolve in B12) | `ordered-cycle-sparse-forcing` (`c006b_erun_check.py` imports `r71c_state_bound_check`) | R71-c probe lands in `mechanical-cycles-high-rational-controls` | Update its `evidence` note |
| B07 (to add, resolve in B12) | `locally-collatz-like-control-barrier` (`PR1_REVIEW.md` links `side_lane_review_13590c1.md` and `side_lane_review_d3a91fe.md`) | R71 node, R74 node | Re-link |
| phase6 batch | `stopping_calibration` (loads R25/R37 code) | B10 nodes | Evidence note naming the new folders |

**Questions created:**
- B09 (optional): `exposure-absorption-giant-component`.
- B10: `normalised-quotient-termination`.
- B11: `universal-w5-tripling-currents`. If B07/B08 create a line-level "universal current supply" question, link it, don't duplicate it.
- B12: `aperiodic-exit18-return-survivors`.
- B13: `common-tail-comparison-after-r92`, `residual-pair-864z-257-supply`.

**Sources:** B09 creates `ansari-2025-recursive-sieve`. Each batch must check `sources/` for the Terras, Monks, Knight and Halbeisen sources (they exist), and check `cylinder_barrier/` and `merger_scope/external_review.json` for external inputs that might need one.

## 11. Status guidance (judgement calls to flag in each report)

- **Main-lane R-results default to `written`.** The legacy "independent model audits" (R13, R37–R39) were run by the main lane's own sub-agents, not a different lane.
- **Side-lane `batch_*` and `r*_check` probes re-check only the finite arithmetic.** For example, `batch_r15_r18_r21_r29` says outright that the `A_N` statements are not checked. Record them under `reviewed_by` with an explicit `scope`. Do not raise the status to `reviewed` unless the probe re-derives the whole argument; decide case by case and report it.
- **`reviewed` is justified for:**
  - the side-lane claims reviewed by the main lane: `quotient-prefix-plans-rho-decreasing` (33c3829) and `divergent-orbit-itinerary-complexity` (fcc7e88);
  - R71 nodes 1 and 2, as `formal` if `## Lean` states the match.
- **Computer-assisted results** (R91, R92; the C++ basin classifiers): claim exactly the finite statement plus the written corollary. Keep the "computer-assisted" wording.
- **Never drop scope wording:** "conditional on supplied currents", "inner absorption is an input", "terminal currents remain premises", "no novelty claimed".
- Wherever two lanes worked on one node, list both authors.

### Critical files for implementation

- `_triage/archive/docs/RESULTS.md` (R10–R94 entries: folder→R map, status lines, scope)
- `_triage/experiments/residual_progress/REPORT.md` (round narrative; links of root reviews; next obligations)
- `_triage/MANIFEST.md` (rows to relabel B09–B13 and the 21 B16 probes) and `_triage/FOLLOWUPS.md` (R71 rows that B12 resolves)
- `_triage/experiments/residual_progress/lattice_cycles/BALANCED_DENOMINATORS.md` with `_triage/lean/STATE.md` rows R71-a to R71-d (cycles move, formal status)
- `_triage/scripts/verify_all.py` (how residual checkers ran at `be73a66`; the basis for every "passed at be73a66" evidence note)
