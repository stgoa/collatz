---
id: near-circuit-rotation-forced-relation
kind: result
title: "Heuristic: a near-circuit with a rotation of four or five mismatches is forced into a small relation"
status: proposed
claim: >
  Heuristic, in a normalised model without error terms; floating-point linear programmes and searches. Raw
  odd-only 3x+1 clock. A near-circuit is a cycle of period m with one giant letter, all other letters carrying
  an excess that is negligible compared with m, so that the heights rise at the maximal rate
  (alpha - 1) per step from the minimum to the giant letter. For a rotation of such a cycle with s
  mismatches, using only the size rows of that rotation and the three- and four-term relations between its
  consecutive paired quotients: s = 3 is impossible; for s = 4 and s = 5 some relation is always forced to
  have a product of parts coprime to 6 below its largest term by 0.329 m, respectively 0.107 m, bits; for
  s >= 6 the rotation alone forces nothing. The statement does not depend on the order of the rotation nor on
  where the small defects are. With two long runs of small defects along the rotation, near-circuits that
  satisfy the size rows of 12 and of 24 multiples of the rotation do exist in the model, at any order, and
  each of the 157 found has a forced relation with at least 0.20 m spare bits. If the model is made rigorous
  (a definition with a tolerance, error terms, exact certificates for seven small linear programmes), this
  gives: under EXT-1 and Evertse's theorem, only finitely many near-circuits have a rotation with four or five
  mismatches. Not proved here.
authors:
  - Claude cycles lane (Fable 5.2; directed by Santiago Armstrong)
created: 2026-11-23
depends_on: [half-period-six-mismatch-local-law]
evidence:
  - "explore_near_circuit_lp.py and explore_near_circuit_lp.json: one linear programme per order type for 3 to 10 mismatches (numpy, scipy; floating point). Exploration, not run by CI"
  - "explore_long_runs.py and explore_long_runs.json: search in the four-parameter family of long runs and the margins of the relations there (standard library; floating point; fixed seed). Exploration, not run by CI"
tags: [cycles, circuits, rotation-distance, s-units, linear-programming, exploration, heuristic, frontier]
---

# Heuristic: a near-circuit with a rotation of four or five mismatches is forced into a small relation

## Statement

**Nothing here is proved.** This node records a model computation and the theorem it points to.

**Near-circuits.** A circuit is a cycle whose valuation word is `(1, ..., 1, K)`: it climbs by the factor `3/2`
at every step and comes down in one step. Steiner excluded them
([`steiner-1977-one-cycles`](../../../../sources/steiner-1977-one-cycles.md)). Call a cycle of period `m` a
*near-circuit* if it has one letter `K` such that the other letters have total excess `sum of (w_i - 1)`
negligible compared with `m`. The number of letters different from 1 is not bounded, so near-circuits are not
covered by the exclusions of cycles with few local minima
([`simons-2005-m-cycles`](../../../../sources/simons-2005-m-cycles.md),
[`hercher-2023-cycle-length`](../../../../sources/hercher-2023-cycle-length.md)).

They matter here because every five-mismatch structure that survives the size rows in
[`few-mismatch-rotation-orders-sweep`](../few-mismatch-rotation-orders-sweep/README.md) is a near-circuit.

**Model.** Divide by `m`; time `t` runs over `(0, 1]`, the minimum is at time 0 and the giant letter at time 1.
The height of the state at time `t` is `(alpha - 1) t`. A rotation with rotation number `h` in `(0, 1/2]` has
its mismatches at the times `1` and `1 - h`, where the giant letter meets a small one, and at `s - 2` other
times, where two small letters differ. For each run between consecutive mismatches the paired quotient `g`
has `G = log_2|g|/m = (higher of the two starting heights) - (length of the run)`, and `G >= 0` is a row. At
each mismatch there are the two relations `3^n g = (2^nu' - 2^nu) xi + 2^c g'` of
[`half-period-six-mismatch-local-law`](../half-period-six-mismatch-local-law/README.md), read with three or
four terms.

**Heuristic claim.** In this model, with the rows and the relations of the rotation only:

| Mismatches `s` | Outcome | Spare bits per unit of `m` |
|---|---|---|
| 3 | the rows are contradictory | |
| 4 | some relation is forced | 0.3289 |
| 5 | some relation is forced | 0.1072 |
| 6 | not forced | |
| 7 to 10 | not forced | |

The numbers are the optima of linear programmes, one for each position of the time `1 - h` among the other
mismatch times (`explore_near_circuit_lp.json`). They hold for every `h` and every position of the small
mismatches, so for every order of the rotation.

**Long runs.** In the sweep, near-circuits at large orders with short runs of small defects did not survive
the size rows of many multiples of the rotation. With long runs they do. If the small defects form a run right
after the giant letter and a second run elsewhere, both longer than the number of multiples considered, the
mismatch times of the multiples depend only on four numbers: `h`, the start `q` of the second run, and the
ends `theta`, `theta'` of the two runs. A search in this family (`explore_long_runs.json`) found 163
configurations satisfying the rows of 12 multiples; 157 were confirmed by the explicit model with actual run
lengths, with rotation numbers between 0.21 and 0.44, and 19 of them also satisfy the rows of 24 multiples.
At every one of the 157 a relation of the first three multiples is forced, with between 0.202 and 0.5315
spare bits per unit of `m`.

So large rotation orders are not excluded by sizes for five mismatches, and the relations are still forced
there.

## What this suggests

**Target theorem.** Fix a small `epsilon > 0`. Under EXT-1 and Evertse's theorem, only finitely many cycles of
period `m` with one letter `K` and total excess of the other letters at most `epsilon m` have a rotation with
exactly four or five mismatches.

**Sketch of a proof, with its gaps.**

1. *Heights.* For such a cycle, `log_2` of the state at step `i` after the minimum lies between
   `(alpha - 1) i - epsilon m` and `(alpha - 1) i + log_2(minimum) + o(1)`. EXT-1 bounds the last term by
   `O(log m)`. So the model heights hold up to `epsilon m + O(log m)`. **Gap:** written here in one line, not
   checked against the block equations as was done for the half-period law.
2. *Rows and relations.* The 2-adic total of a run of `r` letters is between `r` and `r + epsilon m`; the
   length of a run is exact; the two letters at a mismatch other than the giant's differ by at most
   `epsilon m`. The identities are those of the half-period law for the rotation at hand; they hold for any
   rotation. **Gap:** the general-rotation form of the identities is in
   [`mismatch-chain-ridout-criterion`](../mismatch-chain-ridout-criterion/README.md) for chains; the two
   relations between consecutive quotients were written out only for the half-period rotation.
3. *Linear step.* With these perturbations the programmes of the table stay infeasible for `epsilon` small
   compared with `0.107`. **Gap:** floating point only. Exact rational certificates are needed for the three
   order types of `s = 4` and the four of `s = 5`, as in
   [`half-period-six-mismatch-local-law`](../half-period-six-mismatch-local-law/README.md).
4. *Finiteness.* As in
   [`half-period-six-mismatch-finiteness`](../half-period-six-mismatch-finiteness.md): the forced relation is a
   vanishing sum of three or four integers with no vanishing proper subsum (states are coprime to 3), and the
   spare bits are a fixed fraction of `m`. **Gap:** not written for a general rotation.

**What it would not give.** Nothing for six or more mismatches by this route; the sweep suggests that the
multiples of the rotation are needed there. Nothing for cycles that are not near-circuits: that a rotation
with five mismatches forces a near-circuit is observed in the sweep at the orders tested, not proved.

## Remarks

- **Controls.** For `3x+q` the heights of a near-circuit are the same, but the minimum is not bounded by a
  power of the length without using `q`; as elsewhere, nothing is transferred.
- **The case `s = 4`.** Four mismatches are already excluded for every order except 2
  ([`non-half-period-four-mismatch-exclusion`](../non-half-period-four-mismatch-exclusion/README.md)), and
  finitely many cycles remain at order 2. The model of this node uses no multiple of the rotation, so it does
  not see that exclusion; it only shows that a relation is forced whenever its own rows hold.
- **Novelty.** Undetermined. No literature search was made for near-circuits with unboundedly many small
  letters.

## History

- 2026-11-23: explored by the Claude cycles lane (Fable 5.2; directed by Santiago Armstrong), after the sweep
  showed that every five-mismatch survivor is a near-circuit. Recorded as `proposed`: fast exploration first,
  hardening later, at the request of the director.
