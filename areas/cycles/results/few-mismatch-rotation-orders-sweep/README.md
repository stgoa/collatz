---
id: few-mismatch-rotation-orders-sweep
kind: result
title: "Heuristic sweep: every rotation structure tested with five to seven mismatches is impossible or forced into a small relation"
status: proposed
claim: >
  Heuristic. Floating-point explorations of two normalised linear models, with no error terms, no exact
  certificates and finite lists of cases. Raw odd-only 3x+1 clock, nontrivial cycle with minimum of height 0
  in the model (the bound of EXT-1). Model 1, fixed rotation order M: the word is M copies of a long period
  whose blocks differ only in their last letters; rows are the valuation budget, positivity, the place of the
  minimum and, for every shift, the bound of each paired quotient by the higher of its two starting states;
  relations are the three- and four-term relations between consecutive quotients of every shift. For every
  pattern tested, either the rows are contradictory or some relation is forced to have a product of parts
  coprime to 6 below its largest term by a positive fraction of the period: four mismatches for M = 2 to 7,
  five for M = 3 to 8, six for M = 2 to 6, seven for M = 3 and 4. No pattern is left free. The models stop at
  eight mismatches: M = 2 and M = 3 have free patterns. Model 2, large order: bulk of constant excess density,
  special letters on orbit segments of the rotation, explicit heights, rows for the first ten multiples of the
  rotation. Among seven families of five-mismatch patterns only one is feasible anywhere on the grid, a giant
  letter with an adjacent run of small defects and a separate run of small defects, and at every feasible
  grid point a relation is forced with more than m/5 spare bits. With the rows of sixteen multiples no grid
  point of that family remains (runs of at most 8 defects). With the rotation number a/M exact, that family has
  feasible points only at the orders 3, 4, 5, 7, 8, 10, 11, 13, 15, 18, 19 among 3 to 32, all forced. If
  these indications are correct and complete, only finitely many cycles have a rotation with exactly five
  mismatches (under EXT-1 and Evertse's theorem). They are not proofs; the gaps are listed in the node.
authors:
  - Claude cycles lane (Fable 5.2; directed by Santiago Armstrong)
created: 2026-11-23
depends_on: [half-period-six-mismatch-local-law]
evidence:
  - "explore_rotation_orders.py and explore_rotation_orders.json: model 1 (numpy, scipy; mixed-integer, floating point). Exploration, not run by CI"
  - "explore_large_order_model.py and explore_large_order_model.json: model 2 (standard library, floating point). Exploration, not run by CI"
tags: [cycles, rotation-distance, s-units, linear-programming, exploration, heuristic, frontier]
---

# Heuristic sweep: every rotation structure tested with five to seven mismatches is impossible or forced into a small relation

## Statement

**This node is a record of explorations. Nothing in it is proved.** It says what two floating-point models
return, what that suggests, and what is missing for a theorem.

Setting: the raw odd-only `3x+1` map, a hypothetical nontrivial cycle of period `m`, a nonidentity rotation
`H` of its valuation word with `s` mismatches, of order `M = m/gcd(H, m)`. For `s <= 4` the situation is
known: `s <= 3` is excluded, and `s = 4` forces `M = 2`
([`non-half-period-four-mismatch-exclusion`](../non-half-period-four-mismatch-exclusion/README.md)), where
only finitely many cycles remain
([`half-period-four-mismatch-finiteness`](../half-period-four-mismatch-finiteness/README.md)). For six
mismatches and `M = 2` there is a proof with exact certificates
([`half-period-six-mismatch-local-law`](../half-period-six-mismatch-local-law/README.md)).

**Heuristic claim.** In the two models described below, every rotation structure tested with five, six or
seven mismatches is of one of two kinds:

- **empty**: the size rows are contradictory, so no cycle has that structure;
- **forced**: every configuration allowed by the rows has a three- or four-term relation between consecutive
  paired quotients whose parts coprime to 6 have a product below the largest term by a fixed fraction of the
  period. By Evertse's theorem this leaves finitely many cycles, as in
  [`half-period-six-mismatch-finiteness`](../half-period-six-mismatch-finiteness.md).

No structure tested is **free** (rows satisfiable with every relation failing) up to seven mismatches. At
eight mismatches free structures appear, for `M = 2` and `M = 3`.

## Model 1: fixed rotation order

The word is `M` copies of a period of length `P = m/M`, read in time order. A period is cut into `d` blocks at
the positions where the copies differ; the copies of a block share all letters but the last. A *pattern*
gives, for each block, the weak ordering of the `M` last letters. The hypothesised rotation shifts the copies
by `h`, with `gcd(h, M) = 1`; it has a mismatch at every block end where the letters of copies `j` and `j + h`
differ. The model lets `P` tend to infinity with `M` fixed, divides by `P`, and drops subexponential factors.

- **Unknowns.** Block lengths, common totals, the excess of each last letter over the smallest one, the height
  of the state before each of the `M d` block copies, and `G = log_2 |g| / P` for the paired quotient `g` of
  every maximal agreeing run of every shift.
- **Rows.** The valuation budget; heights at least 0; a minimum in the first block copy; and, for every shift
  and every run, `G + (2-adic total of the run) <=` the higher of the two starting heights.
- **Relations.** At every mismatch of every shift, the two relations
  `3^n g = (2^nu' - 2^nu) xi + 2^c g'` of
  [`half-period-six-mismatch-local-law`](../half-period-six-mismatch-local-law/README.md), in three-term and
  four-term form.
- **Question.** Maximise `t` such that every relation has (sum of logs of the parts coprime to 6) at least
  (log of the largest term) `+ t`. A negative maximum means *forced*.

Results, from `explore_rotation_orders.json`. "Weakest" is the largest (least negative) maximum among the
forced patterns, in units of `P`.

| Mismatches | Order `M` | Shift `h` | Patterns | Empty | Forced | Free | Weakest |
|---|---|---|---|---|---|---|---|
| 4 | 2 | 1 | 4 | 2 | 2 | 0 | -0.576 |
| 4 | 3 | 1 | 36 | 36 | 0 | 0 |  |
| 4 | 4 | 1 | 180 | 180 | 0 | 0 |  |
| 4 | 5 | 1 | 590 | 590 | 0 | 0 |  |
| 4 | 5 | 2 | 590 | 590 | 0 | 0 |  |
| 4 | 6 | 1 | 1464 | 1464 | 0 | 0 |  |
| 4 | 7 | 1 | 3094 | 3094 | 0 | 0 |  |
| 4 | 7 | 2 | 3094 | 3094 | 0 | 0 |  |
| 4 | 7 | 3 | 3094 | 3094 | 0 | 0 |  |
| 5 | 3 | 1 | 72 | 64 | 8 | 0 | -0.731 |
| 5 | 4 | 1 | 576 | 572 | 4 | 0 | -1.543 |
| 5 | 5 | 1 | 2670 | 2670 | 0 | 0 |  |
| 5 | 5 | 2 | 2670 | 2666 | 4 | 0 | -1.488 |
| 5 | 6 | 1 | 8820 | 8820 | 0 | 0 |  |
| 5 | 7 | 1 | 23310 | 23310 | 0 | 0 |  |
| 5 | 7 | 2 | 23310 | 23310 | 0 | 0 |  |
| 5 | 7 | 3 | 23310 | 23298 | 12 | 0 | -2.354 |
| 5 | 8 | 1 | 52752 | 52752 | 0 | 0 |  |
| 5 | 8 | 3 | 52752 | 52744 | 8 | 0 | -2.488 |
| 6 | 2 | 1 | 8 | 2 | 6 | 0 | -0.029 |
| 6 | 3 | 1 | 252 | 200 | 52 | 0 | -0.299 |
| 6 | 4 | 1 | 3216 | 3092 | 124 | 0 | -0.638 |
| 6 | 5 | 1 | 19200 | 19092 | 108 | 0 | -0.773 |
| 6 | 5 | 2 | 19200 | 18892 | 308 | 0 | -0.46 |
| 6 | 6 | 1 | 77934 | 77870 | 64 | 0 | -1.231 |
| 7 | 3 | 1 | 648 | 442 | 206 | 0 | -0.03 |
| 7 | 4 | 1 | 12192 | 11016 | 1176 | 0 | -0.041 |
| 8 | 2 | 1 | 16 | 2 | 2 | 12 | -0.068 |
| 8 | 3 | 1 | 1944 | 1174 | 706 | 64 | -0.029 |

For `M = 4` and `M = 6` a few patterns are fixed by a rotation of smaller order ("invariant"); they belong to
that smaller order and are not counted above.

For five mismatches, all survivors found have the same shape: no excess in the bulk, heights rising at the
maximal rate over the whole cycle, one giant last letter, and small defects (excess negligible on the scale
of `P`) at one offset in a run of copies next to the giant in the order of the rotation, plus one more run of
small defects at another offset. They are close to the circuits of Steiner, with a few extra letters.

## Model 2: large rotation order

For a rotation of large order the period `P = m/M` is short and Model 1 no longer applies. Model 2 divides by
`m`. The bulk has a constant excess density `beta`; finitely many special letters sit on orbit segments
`{q + i h}` of the rotation number `h`; a special letter is either *visible* (excess a positive fraction of
`m`) or *small*. The last letter is visible and brings the height back to 0. Heights are then explicit,
`Z(t) = (alpha - 1 - beta) t` minus the visible excesses before `t`, and the rows and the margins of the
relations are closed formulas. With the indices read modulo `M` the model reproduces Model 1 on the order-7
survivor: the margin is `0.3363` per unit of `m` in both.

Seven families of five-mismatch patterns were scanned over `h`, the phase `q`, run lengths up to 7 and
`beta` in `{0, 0.05, 0.15}`, with rows for the first ten multiples of the rotation
(`explore_large_order_model.json`):

| Family | Grid points per density | Feasible at `beta = 0` | at `0.05` | at `0.15` | Weakest best margin (per unit of `m`) |
|---|---|---|---|---|---|
| giant with adjacent small run, separate small run | 1499400 | 15 | 2 | 0 | 0.2184 |
| giant alone, separate run with two small letters | 699720 | 0 | 0 | 0 |  |
| two adjacent visible letters, separate small run | 1199520 | 0 | 0 | 0 |  |
| giant with adjacent small run, separate run of visible letters | 2056320 | 0 | 0 | 0 |  |
| run of equal visible letters, separate run with two small letters | 685440 | 0 | 0 | 0 |  |
| one orbit: giant, small run, gap, small run | 81634 | 0 | 0 | 0 |  |
| one orbit: giant followed by three different small runs | 15232 | 0 | 0 | 0 |  |

For the one feasible family, the same scan on a 200 by 200 grid with run lengths up to 8, keeping the
feasible points as more multiples of the rotation are imposed:

| Multiples imposed | Feasible grid points | Weakest best margin |
|---|---|---|
| 8 | 143 | 0.1868 |
| 12 | 24 | 0.2683 |
| 16 | 0 |  |
| 24 | 0 |  |
| 32 | 0 |  |
| 48 | 0 |  |

So in this model the only five-mismatch structures that survive the rows of ten multiples are those found by
Model 1, and they are forced with a large margin, uniformly in the rotation number. With the rows of sixteen
multiples nothing survives on the second grid: for a rotation number whose first sixteen multiples are
distinct, the model has no five-mismatch configuration with runs of at most 8 small defects. Survivors would
then exist only at small orders, where the multiples wrap around.

**Exact small orders in Model 2.** The same explicit model, with the rotation number `a/M` exact and indices
read modulo `M`, was run for the feasible family at every order from 3 to 32, with rows for every nonzero
multiple and runs of at most 8 defects:

| Order `M` | Numerators `a` with feasible points | Feasible grid points | Weakest best margin (per unit of `m`) |
|---|---|---|---|
| 3 | 1 | 132 | 0.2624 |
| 4 | 1 | 10 | 0.3879 |
| 5 | 2 | 76 | 0.3014 |
| 7 | 3 | 22 | 0.3365 |
| 8 | 3 | 64 | 0.3111 |
| 10 | 3 | 8 | 0.4546 |
| 11 | 3, 4 | 14 | 0.217 |
| 13 | 5 | 30 | 0.3023 |
| 15 | 4 | 2 | 0.3712 |
| 18 | 7 | 1 | 0.3748 |
| 19 | 4, 8 | 5 | 0.2933 |

No feasible grid point at the orders 6, 9, 12, 14, 16, 17, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32.

This agrees with Model 1 where both were run (orders 3 to 8: survivors at 3, 4, 5, 7, 8, none at 6). It
assumes a bulk of constant density, which Model 1 does not.

**Connection with an earlier attempt.**
[`multi-rotation-four-mismatch-exclusion`](../../attempts/multi-rotation-four-mismatch-exclusion/README.md)
found, in a continuous model of the same single-drop shape, that five and six mismatches survive the size
inequalities of twelve rotations, and concluded that size inequalities alone stop at four mismatches. The
present sweep agrees on that point and adds the relations: where a five-mismatch structure survives the
sizes, a relation is forced.

## What this suggests

**Conjectural consequence.** Under EXT-1 and Evertse's theorem, only finitely many nontrivial cycles have a
rotation with exactly five mismatches; with the known cases this would give the case `s = 5` of
[`rotation-distance-finite-exceptions`](../../questions/rotation-distance-finite-exceptions.md). The same
would hold for six and seven mismatches if the pattern persists for all orders. Eight mismatches are out of
reach of these relations.

## Gaps

1. **No error terms.** Both models drop subexponential factors: the logarithm of the minimum, the drift
   `tau`, rounding of `2^p - 1`. The proof for `M = 2`, `s <= 6` shows how to restore them; it was not done
   here.
2. **Floating point.** Model 1 uses a mixed-integer solver. On one programme of this family the solver
   returned an infeasible point as optimal; variables are boxed and every returned point is re-checked, but
   "empty" verdicts rest on the solver. No exact certificate exists outside `M = 2`.
3. **Orders not covered.** Model 1 was run for the orders in the table only. Model 2 is meant for large
   orders, but it assumes a bulk of constant density, which is exact only in the limit, and special letters
   of two sizes only. No argument joins the two ranges, and no threshold for "large" is known.
4. **Completeness of the families in Model 2.** The seven families were written by hand from the ways of
   making five mismatches with at most two orbits. Their completeness was not proved, and Model 2 was not run
   for six or seven mismatches.
5. **Runs and multiples in Model 2.** Runs of small defects were limited to length 8 (7 in the family scan).
   Longer runs give more freedom: the end of a run can then sit anywhere on the circle. They were not scanned
   systematically. The feasible sets are read on finite grids; thin feasible regions can be missed, and a
   finer grid needed more multiples before the feasible set became empty.
6. **From forced relations to finiteness.** For the relations of the hypothesised rotation and of its
   multiples, the nondegeneracy needed by Evertse's theorem is the same as in
   [`half-period-six-mismatch-finiteness`](../half-period-six-mismatch-finiteness.md) (states are coprime to
   3), but this was not written out for general orders, and a uniform margin over all orders is needed.
7. **Controls.** Not tested against actual `3x+q` cycles. As for `M = 2`, the only `q = 1` inputs are the
   bounds on the minimum.

## How to harden it

- For each order in the table: exact rational certificates, as in
  [`half-period-six-mismatch-local-law`](../half-period-six-mismatch-local-law/README.md). The disjunction
  "which of the two paired states is higher" becomes a case split.
- For large orders: a statement that the rows force the shape of Model 2 (constant density, one giant
  letter), with an explicit threshold on the order, followed by an exact treatment of the explicit model.
  The pure geometric method of
  [`free-four-cut-eighteen-rotation-obstruction`](../free-four-cut-eighteen-rotation-obstruction/README.md) is
  the model for the first part.

## History

- 2026-11-23: explored by the Claude cycles lane (Fable 5.2; directed by Santiago Armstrong), right after the
  proof for six half-period mismatches. Recorded as `proposed` at the request of the director to move fast and
  harden later.
