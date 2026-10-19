# Independent review of side lane cbe77bc

**Status: finite reproduction PASS; no universal conclusion imported.**

Reviewed exact side commit `cbe77bce62d0a5ba2fbac1af3f686806cc7f6d4a`, compared with `64a598169be279de8551a1be9959c91eed865875`, while main was `7d86314672ac0ac8763843e329df3cfacaa85671`. The new files are the R64 probe and its receipt; FEED and SYNTHESIS also changed. The side branch was read only.

## Reproduction

The unchanged `reviews/side_lane/r64_lifted_cycle_check.py` and its only nonstandard import, `collatz_research_20261017/negative_controls/affine_controls.py`, were materialized from the same exact commit in an isolated `/tmp` directory. The probe ran without Python optimization, under a 90-second external process cap. It exited successfully in approximately 0.06 seconds and reproduced the published JSON **byte for byte**.

The [machine receipt](side_lane_review_cbe77bc.json) records both pins, source and dependency SHA-256 hashes, the execution output, the receipt comparison, and every sampled parameter cell.

## What was checked

The 85 constructed representatives span the stated acceptance-table boundaries through `k=85`, with feasible `j` among `J(k)-1,J(k),J(k)+1`. All cells were constructed; none was skipped. There are 58 accepted and 27 rejected representatives. The longest checked ordinary word has 600 arrows.

For each representative the probe verifies:

- the input congruences and the recomputed maximal cycle and point depths;
- the exact ordinary word `(2,7,1,4)` from the specified base predecessor to `q`;
- the exact ordinary word `1^j,(1,1,2,1,1,4,1)^k,(2,7,1,4)` from `eta` to `q`;
- agreement of `eta<q` with the stated threshold `j>=J(k)`.

These are genuine arithmetic checks of the selected R64 boundaries. They agree with the scoped main theorem in [LIFTED_CYCLE.md](refined_obstruction/LIFTED_CYCLE.md).

## Limits

There is one constructed seed per sampled cell. The positive-cycle constructions use only `h-7k` equal to 0 or 1; they do not test remainders 2 through 6. Interior cycle counts, arbitrarily large cycle counts, other point depths, and every seed in a cell are not exhaustively checked. Full signed plans, W9 substitution, dispatcher priority, supplied input currents, and universal completion are outside this probe.

The probe can label its report PASS even if its bounded builder skips a cell. This review separately required `boundary_cells_tested=85` and an empty skipped list, so that issue does not affect this reproduction. The side lane supplies useful independent finite evidence; the universal R64 statements continue to depend on the main written proof. No new acceptance rule or convergence claim follows from the replay.
