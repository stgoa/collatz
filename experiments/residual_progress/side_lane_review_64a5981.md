# Pinned independent review:64a5981

**Verdict: PASS within the finite scopes below.** All three probes were copied unchanged, with both exact pinned local dependencies, into this isolated temporary tree. Each ran under an outer90-second process cap, without optimization. Every output receipt is byte-identical to the pinned receipt. No repository or side-branch file was edited.

- Side pin: `64a598169be279de8551a1be9959c91eed865875`.
- Comparison base: `b9203ff32801b15725d4c9b7e5890386f1d8a07f`.
- Main HEAD at replay: `3acae93f9fc9dbb2cf6411dc1e341aff2c13fcd5`.
- Evidence: [reproduction receipt](side_lane_review_64a5981.json), including hashes, stdout, stderr, caps and exact coverage.

## What changed from b9203ff

Two new probes/receipts cover R60 and R86. The R81/R83 source removes an unreachable ternary-minimality branch and corrects its docstring; its receipt is unchanged. FEED acknowledges the previous coverage error. SYNTHESIS adds R60 and R84/R85 rows; its generic R81 “with minimality” wording should be read as binary minimality only, as explicitly corrected in FEED and source.

## Reproduction and limits

| Probe | Exact replay | Actual finite coverage | Limits |
|---|---|---|---|
| R60 | exit0, 0.115s; byte-identical | 100 cells,400 cases: k1..20,j0..4, four inputs each; exact h=7k. Exact ordinary word, height formula and threshold checks. | No k0, nonzero h remainder, larger k/j, complete signed plans or current supply. The imported nu function is unused. |
| R86 | exit0, 0.088s; byte-identical | 96 cells,1152 cases: H3..14,b1..8, twelve each;396 inside and756 outside. Selected normalization, one-step target, clocks and raw inequality checked. | No universal extrapolation, full current, old17 exclusion or R87 repair. A larger raw target does not imply no other certificate exists. |
| R81/R83 | exit0, 0.117s; byte-identical | 3301 fixed-cell lifts;400 random anchors×41 lifts; binary-halving failure per anchor. R83 parameter pairs(740,8148),(2028089,22308995). | Ternary minimality was not executed. R83 s1 is exhaustive; s2 uses a checked exact order. Full CRT families and long currents were not rebuilt. |

R81’s revised receipt also matches the b9203ff receipt byte for byte. The corrected ternary statement rests on coupled integrality: at most one period has a positive power of3, so simultaneous division by3 would make the other period nonintegral. This is a mathematical explanation, not an additional executed branch.

R86 has no explicit per-cell assertion that twelve samples were made, but each cell is capped at twelve and the observed total equals96×12, so all cells are populated in this replay. R60 uses an uncapped outer sampling loop internally; the external90-second cap bounds this reproduction. No timeout occurred.

## Source hashes

| Exact pinned source/dependency | SHA-256 |
|---|---|
| `collatz_research_20261017/negative_controls/affine_controls.py` | `9e5ad66deaf7ede55b1d607f6d85d57f58d38e9dd2c551d45f1b7a2d58538e3c` |
| `reviews/side_lane/batch_r81_r83_check.py` | `ec88e50282d281030fec8c023c556caa8e2e04433a7a213170f3c74fc6494360` |
| `reviews/side_lane/fibre_count_check.py` | `071b2d076702ff0ab87746b9c130c0271c2adcf82b45f59e5d0ffec53b14923a` |
| `reviews/side_lane/r60_cycle_inverse_check.py` | `4d6c516e9526b18ceb0764dc405beb79880901b46361ba44454db36a13d03df2` |
| `reviews/side_lane/r86_even_exit_check.py` | `68b8577fe8ff083a786ecc5ca7f6ce988a8657ba2f873ee021e9df3e021d37ed` |

These checks support the named arithmetic identities in the tested ranges. They do not establish universal acceptance, guaranteed search termination, current supply, or a new theorem beyond main’s written proofs.
