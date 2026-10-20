---
id: four-mismatch-sign-dichotomy
kind: result
title: A rotation with four mismatches has one sign change of each kind, or two of each in alternating order
status: formal
claim: >
  Odd-only 3x+q map, any primitive positive odd cycle with letters ≥ 1, and any rotation h ≢ 0 (mod m).
  Classify the mismatches of h by the state difference z_i = n_(i+h) − n_i: D the +→− changes, U the −→+
  changes, N the mismatches with no sign change. Then |mis h| = |D| + |U| + |N|, and between two changes of
  one kind there is a change of the other kind (also across the period). Hence if |mis h| = 4, either
  |D| = |U| = 1 and |N| = 2, or |D| = |U| = 2 and |N| = 0; in the second case the four mismatches
  a < b < c < d < m alternate down, up, down, up or up, down, up, down. Pure combinatorics of the sign
  sequence: no gap, no period bound, no size condition.
authors:
  - Claude Lean lane (Fable)
created: 2026-10-19
lean:
  - LeanLane.Cyc.OddCycle.mis_card_partition
  - LeanLane.Cyc.OddCycle.up_between_downs
  - LeanLane.Cyc.OddCycle.down_between_ups
  - LeanLane.Cyc.OddCycle.down_add_period
  - LeanLane.Cyc.OddCycle.up_add_period
  - LeanLane.Cyc.OddCycle.alternation_core
  - LeanLane.Cyc.OddCycle.mis_lt_m
  - LeanLane.Cyc.OddCycle.card_four
  - LeanLane.Cyc.OddCycle.four_mismatch_dichotomy
  - LeanLane.Cyc.OddCycle.four_mismatch_alternation
tags: [cycles, rotation-distance, sign-lemma, formal]
---

# A rotation with four mismatches has one sign change of each kind, or two of each in alternating order

## Statement

Primitive positive odd cycle `n_0, …, n_(m−1)` of the odd-only `3x+q` map, letters `≥ 1`, rotation `h ≢ 0 (mod m)`, `z_i = n_(i+h) − n_i` (nonzero by primitivity). The sign of `z` is constant along an agreeing run and can change only at a mismatch ([`three-mismatch-exclusion`](three-mismatch-exclusion/README.md), sign lemma (F2), Lean S7-a). Split `mis h` into `D` (`+ → −` changes), `U` (`− → +` changes) and `N` (mismatches with no change), all in `[0, m)`.

1. `|mis h| = |D| + |U| + |N|`.
2. Between two changes of one kind there is a change of the other kind, also across the period.
3. **Dichotomy.** If `|mis h| = 4`: `(|D|, |U|, |N|) = (1, 1, 2)` or `(2, 2, 0)`.
4. **Alternation.** If `|mis h| = 4` and `|D| = 2`: `mis h = {a, b, c, d}` with `a < b < c < d < m` and either `down a, up b, down c, up d` or `up a, down b, up c, down d`.

## Proof

A sketch by the B06 migration; the Lean proofs of unit S10-a are authoritative. Part 1 is a partition of a finite set. Part 2: the sign of `z` is constant on an agreeing run, so between two `+ → −` changes the sign must return to `+`, which needs a `− → +` change; across the period the same argument runs on `(y, x + m)`. Part 3: going once round the cycle there are as many `+ → −` as `− → +` changes (`card_down_eq_card_up`, S7-b), and both kinds occur because `Σ_i z_i = 0` with every `z_i ≠ 0`; so `|D| = |U| ∈ {1, 2}` and `|N| = 4 − 2|D|`. Part 4: with changes `x < y` of one kind and `p < q` of the other, the between-lemmas on `(x, y)` and across the period force the order `x, p, y, q` or `p, x, q, y` (`alternation_core`).

The sign lemma and `card_down_eq_card_up` are the gap-free parts of [`three-mismatch-exclusion`](three-mismatch-exclusion/README.md) (Lean S7-a, S7-b part 2); that node is not listed under `depends_on` because its headline uses the gap and the period imports, which this result does not.

## Lean

`lean/CycleSpectrum.lean`, Lean unit S10-a (iteration 75; axioms `propext`, `Classical.choice`, `Quot.sound` for 8 declarations, `[propext]` only for `down_add_period` and `up_add_period`; receipts `lean/receipts/CycleSpectrum.*`), namespace `LeanLane.Cyc.OddCycle`: `mis_card_partition` (part 1), `up_between_downs`, `down_between_ups`, `down_add_period`, `up_add_period` (part 2), **`four_mismatch_dichotomy`** (part 3: primitive cycle, `h % m ≠ 0`, `|mis h| = 4`), **`four_mismatch_alternation`** (part 4, via `alternation_core`), helpers `mis_lt_m`, `card_four`.

**Statement match.** Parts 1–4 are the four named theorems, with `D`, `U`, `N` the filters of `mis h` by the sign of `z` before and after the mismatch. Hypotheses: primitivity (distinct states), letters `≥ 1`, `h % m ≠ 0`. The proof text above is a summary of the Lean proofs by the B06 migration, not a separate written argument.

## Remarks

- **Purpose.** Requested by the side lane for an `s = 4` structure theorem toward `ρ ≥ 5` ([`multi-rotation-four-mismatch-exclusion`](../attempts/multi-rotation-four-mismatch-exclusion/README.md) §6 (c)). The single-drop model there is the first case `(1, 1, 2)`; the interleaving was requested for the second. The `(1, 1, 2)` window theorem was queued in the Lean lane and not done when the lanes stopped; the target is [`rotation-distance-at-least-5`](../questions/rotation-distance-at-least-5.md).
- It excludes nothing by itself.

## History

- New node by the B06 migration (Claude, Opus 5.5), from the Lean unit S10-a in legacy `lean/STATE.md` (the S10 note §6 (c) and the side lane's messages of 14:09–14:20). Verified in the Lean lane at iteration 75 (Lean-lane commit `7b957c3`), refereed from receipts by the side lane (feed S10 entry, update 14:36). The second build fixed a Mathlib name, a binder and a `tauto` timeout.
