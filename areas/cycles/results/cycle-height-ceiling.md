---
id: cycle-height-ceiling
kind: result
title: The height of a cycle is at most (log₂3 − 1)(m − 1) plus a term in q/L, by climbing from the minimum
status: formal
claim: >
  Raw odd-only 3x+q map, q > 0, any cycle n_0 = L (the minimum), …, n_(m−1) with all letters a_i ≥ 1
  (automatic for odd q). With u_j the number of letters equal to 1 among a_0, …, a_(j−1):
  n_j ≤ L·(3/2)^(u_j)·(1 + q/(3L))^j for every j, and if the band B (heights h_i = floor(log₂(n_i/L)))
  is attained, B ≤ (log₂3 − 1)(m − 1) + (m − 1)·log₂(1 + q/(3L)). At q = 1 with L > 2^71 the last term is
  below 10^(−20)·m, so B ≤ 0.585(m − 1) up to that term.
authors:
  - Claude Lean lane (Fable)
  - Claude side lane (Opus)
created: 2026-10-19
lean:
  - LeanLane.Cyc.OddCycle.a_pos_of_odd
  - LeanLane.Cyc.OddCycle.n_succ_le
  - LeanLane.Cyc.OddCycle.n_le_climb
  - LeanLane.Cyc.OddCycle.h_le_climb
  - LeanLane.Cyc.OddCycle.B_le_ceiling
  - LeanLane.Cyc.OddCycle.B_le_ceiling_q1
evidence:
  - "two-mismatch-exclusion-via-gap/README.md, derivation step 3 (legacy S06 note), and mismatch-height-tradeoff/README.md, Remarks (legacy S05 note section 3): the written statements"
tags: [cycles, height, formal]
---

# The height of a cycle is at most (log₂3 − 1)(m − 1) plus a term in q/L, by climbing from the minimum

## Statement

Let `n_0, …, n_(m−1)` be a cycle of the raw odd-only `3x+q` map, `q > 0`, indexed from its minimum `n_0 = L`, with every letter `a_i ≥ 1` (automatic when `q` is odd). Heights are `h_i = floor(log₂(n_i/L))` and `B = max h_i`. Let `u_j` be the number of letters equal to `1` among `a_0, …, a_(j−1)`. Then

```
n_(i+1) ≤ (3/2)^([a_i = 1])·(1 + q/(3L))·n_i,       n_j ≤ L·(3/2)^(u_j)·(1 + q/(3L))^j,
B ≤ (log₂3 − 1)(m − 1) + (m − 1)·log₂(1 + q/(3L)).
```

At `q = 1` and `L > 2^71`, the last term is below `10^(−20)·m`.

## Proof

Along the arc from the minimum to the maximum, each step multiplies by `(3 + q/n_i)/2^(a_i) ≤ (3/2)(1 + q/(3L))` when `a_i = 1`, and by at most `(3/4)(1 + q/(3L))`, hence by at most `1 + q/(3L)`, when `a_i ≥ 2`. Multiply over the first `j` steps and use `u_j ≤ j ≤ m − 1` at the index `j` of the maximum.

## Lean

`lean/CycleSpectrum.lean`, Lean unit S6-a (iteration 64); axioms `propext`, `Classical.choice`, `Quot.sound` (`ones_succ`: `propext`; `ones_le`: `propext`, `Quot.sound`). In `OddCycle` (index 0 is the minimum; heights satisfy `2^h·L ≤ n < 2^(h+1)·L`): `a_pos_of_odd` (`q` odd ⇒ every letter `≥ 1`), `n_succ_le`, `n_le_climb` (`n_j ≤ L·(3/2)^(u_j)·(1 + q/(3L))^j`), `h_le_climb` (`h_j·log 2 ≤ u_j·(log 3 − log 2) + j·log(1 + q/(3L))`), `B_le_ceiling` (`B` attained, letters `≥ 1`: `B·log 2 ≤ (m−1)(log 3 − log 2) + (m−1)·log(1 + q/(3L))`), `B_le_ceiling_q1` (the same at `q = 1` with no letter hypothesis). The statements are in natural logarithms multiplied out; the base-2 form is division by `log 2`. `B` must be attained (`hB : ∃ i, h i = B`) because the structure's `B` is only an upper bound. The numerical remark for `L > 2^71` is not restated.

## Remarks

- The tracked form with the letter excess, `log₂(n_k/L) ≤ kκ − Σ_(i<k)(a_i − 1)`, is part of [`three-mismatch-exclusion`](three-mismatch-exclusion/README.md) (Lean `n_mul_pow_excess_le`, `h_add_excess_le`).
- **The minimum enters only through the last term.** For the slope comparisons of [`two-mismatch-exclusion-via-gap`](two-mismatch-exclusion-via-gap/README.md) one needs only `log₂(1 + 1/(3L)) < 0.2075`, i.e. `L ≥ 3`.
- Elementary; novelty: none claimed.

## History

- Created by the B05 migration (Claude, Opus 5.5) from the legacy S05 note §3 ("the height ceiling, sharpened by the Lean lane") and S06 note §2 step 3 (`experiments/cycle_spectrum/S05/MISMATCH_HEIGHT.md`, `S06/C011_VIA_S5.md`, at `be73a66`). The argument is the Lean lane's, from its review of S5 (feed 2026-10-19 11:35); the side lane wrote it into its notes.
- **Correction (2026-10-19 11:47, the Lean lane's review of S6).** The first written form was `B ≤ (log₂ 3 − 1)(m − 1) + 1 + m·log₂(1 + 1/(3L))`; the ceiling has no `+ 1`, and the `ε` term carries `(m − 1)`. This moved S6's threshold from 24,895 to 24,891. Formalised in the corrected form as S6-a (feed update 11:59).
