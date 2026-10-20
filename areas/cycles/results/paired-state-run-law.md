---
id: paired-state-run-law
kind: result
title: Along an agreeing run of a rotation, state differences factor as 2^(E+1)k → 2·3^t·k, bounding q below with the height
status: formal
claim: >
  Raw odd-only 3x+q map, q > 0, no order and no q ≤ L assumed. Let n_0, …, n_(m−1) be a cycle
  3n_i + q = 2^(a_i)·n_(i+1) of odd positive integers with distinct states, n_0 = L its minimum, total A,
  D = 2^A − 3^m > 0, δ = A·log 2 − m·log 3, B its maximum dyadic height (H < 2^(B+1)·L), and h a
  nonidentity rotation, z_i = n_(i+h) − n_i. Then every z_i is even and nonzero; at an agreeing position
  (a_i = a_(i+h)) 2^(a_i)·z_(i+1) = 3z_i; along t consecutive agreeing positions with valuation sum E,
  z_start = 2^(E+1)·k and z_end = 2·3^t·k for a nonzero integer k; hence H − L ≥ 2·max(2^E, 3^t),
  2·max(2^E, 3^t) < (2^(B+1) − 1)·L, 6δ·max(2^E, 3^t) < m·q·(2^(B+1) − 1), and
  6D·max(2^E, 3^t) < m·q·2^A·(2^(B+1) − 1).
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [ordered-cycle-sparse-forcing]
lean:
  - LeanLane.Cyc.OddCycle.z_even
  - LeanLane.Cyc.OddCycle.z_ne_zero
  - LeanLane.Cyc.OddCycle.z_step
  - LeanLane.Cyc.OddCycle.z_run
  - LeanLane.Cyc.OddCycle.z_run_factor
  - LeanLane.Cyc.OddCycle.diameter_ge
  - LeanLane.Cyc.OddCycle.K_mul_L_gt
  - LeanLane.Cyc.OddCycle.q_bound_delta
  - LeanLane.Cyc.OddCycle.q_bound_rational
  - LeanLane.Cyc.OddCycle.q_bound_rational_prim
  - LeanLane.Cyc.run_factor
evidence:
  - "shared-background-denominator-law/OVERLAP_THEORY.md, sections 1-2: the written proof"
  - "shared-background-denominator-law/c013b_run_law_check.py: side-lane check on 77 actual cycles, every nonidentity rotation and every maximal agreeing run (12,550 runs); it no longer runs at the new path (see that node)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-19
    link: shared-background-denominator-law/c013b_run_law_check.py
    scope: "Feed 2026-10-19 update 10:44: Lean C013-b VERIFIED (receipts 19e73031…), statement match with OVERLAP_THEORY.md sections 1-2; independent check on 12,550 runs: z even and nonzero, run law, factorisation with k ≠ 0, diameter bound and (7) with the real B, slack between 4 and 1.8·10^7"
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed 05:03: the run law re-derived by hand, no error; Lean unit C013-b verified (iteration 58; called C013-a iteration 58 in the lane's STATE)"
tags: [cycles, rotation-distance, height, formal]
---

# Along an agreeing run of a rotation, state differences factor as 2^(E+1)k → 2·3^t·k, bounding q below with the height

## Statement

Let `n_0, …, n_(m−1)` be a primitive positive odd cycle at reduced parameter `q`, `m > 1`, `3n_i + q = 2^(a_i)·n_(i+1)`, `a_i ≥ 1`, `A = Σa_i`, `D = 2^A − 3^m > 0`, `L = min n_i`, `H = max n_i`, `B = floor(log₂(H/L))`, `δ = A·log 2 − m·log 3 > 0`, `K_B = 2^(B+1) − 1`. Fix a nonidentity rotation `h` and put `z_i = n_(i+h) − n_i`.

1. Every `z_i` is even (odd states) and nonzero (primitivity).
2. At an agreeing position `a_i = a_(i+h)`: `2^(a_i)·z_(i+1) = 3z_i` (2).
3. Along `t` consecutive agreeing positions with valuation sum `E`: `2^E·z_end = 3^t·z_start`, and `z_start = 2^(E+1)·k`, `z_end = 2·3^t·k` for a nonzero integer `k` (3); valid also for `t = E = 0`.
4. Hence `H − L ≥ 2·max(2^E, 3^t)` (4), `L > 2·max(2^E, 3^t)/K_B` (5), and

```
q > 6δ·max(2^E, 3^t)/(m·K_B),                                              (6)
6D·max(2^E, 3^t) < m·q·2^A·(2^(B+1) − 1).                                  (7)
```

No circular order and no `q ≤ L` are assumed; the actual height `B` is retained.

## Proof

[`OVERLAP_THEORY.md`](shared-background-denominator-law/OVERLAP_THEORY.md) §§1–2. (2) subtracts the two arrows; (3) iterates (2); since 2 and 3 are coprime, `2^E·z_end = 3^t·z_start` with `z_end` even forces `z_start = 2^(E+1)·k`, `z_end = 2·3^t·k`. (4) because `|z_i| ≤ H − L`. (5) from `H/L < 2^(B+1)`. (6) combines (5) with `δ = Σ log(1 + q/(3n_i)) < m·q/(3L)` ([`ordered-cycle-sparse-forcing`](ordered-cycle-sparse-forcing/README.md), which records `δ ≤ m·q/(3L)` for every cycle). (7) follows from `η = D/2^A = 1 − e^(−δ) < δ`.

## Lean

`lean/CycleSpectrum.lean`, Lean unit C013-b (legacy `lean/STATE.md`, iteration 58; the lane's STATE labels it a second "C013-a"), on `OddCycle` with no order hypothesis and nothing comparing `q` with `L`; axioms `propext`, `Classical.choice`, `Quot.sound` (`z_even`: `propext`, `Quot.sound`; `z_ne_zero`: `propext`); receipts `lean/receipts/CycleSpectrum.*`. "Nonidentity rotation" is `h % m ≠ 0`; "primitive" is `hprim : ∀ i j < m, n i = n j → i = j` (used only through `k ≠ 0`); a run is `(i, t, hagree)` with `hagree : ∀ j < t, a (i+j) = a (i+j+h)`.

- `z_even`, `z_ne_zero`: part 1. `z_step`: (2). `z_run`: `2^E·z_(i+t) = 3^t·z_i`. `z_run_factor` (with `run_factor`): (3), `k ≠ 0` when `z_(i+t) ≠ 0`.
- `diameter_ge`: (4), stated for every upper bound `H` of the states (equivalent). `K_mul_L_gt`: (5) as `2·max < K_B·L`.
- `q_bound_delta`: (6) cleared, over `ℝ`, through C006-c's `L_mul_delta_le` and `delta_pos` (`δ > 0` from `D > 0`). `q_bound_rational`: (7) over `ℤ`, through `η ≤ δ`; `q_bound_rational_prim`: (7) under the prose's hypotheses.

The statement matches the claim above, which is per run. Not in this unit (and not in the claim): the pigeonhole long run below and the orbit-sum identities.

## Remarks

- **Using a long run.** If the rotation has `s` mismatches, they split the `m − s` agreeing positions into `s` cyclic runs, so some run has `t ≥ ceil(m/s) − 1` (pigeonhole, written, not in Lean), giving `q > 6δ·3^(ceil(m/s)−1)/(m·K_B)`. The actual `E, t` of each run should be used rather than averages. The differences also satisfy the zero orbit sums `Σ z_i = 0` over each orbit of `+h` (written).
- **The height cannot be dropped.** (6) retains `B`; replacing it by a function of `s` would change the statement. [`distance-three-height-family`](distance-three-height-family.md) shows that bounded rotation distance, `q ≤ L` and vanishing drift do not bound `B`.
- **Later use.** The side lane's S05 ([`mismatch-height-tradeoff`](mismatch-height-tradeoff/README.md)), S06 ([`two-mismatch-exclusion-via-gap`](two-mismatch-exclusion-via-gap/README.md)), S07 ([`three-mismatch-exclusion`](three-mismatch-exclusion/README.md)) and S13 (legacy `experiments/cycle_spectrum/S13/`, not yet migrated) build on this run law with the replayed gap EXT-1; e.g. C013-b's `q_bound_rational` is the base of S5-a.
- **Novelty.** Elementary; none claimed.

## History

- Split from `experiments/cycle_spectrum/C013/` (legacy ID `C013`; `OVERLAP_THEORY.md` §§1–2) at commit `be73a66`, by the B04 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex), 2026-10-19. Formalised by the Lean lane (Claude Lean lane, Fable) as C013-b, iteration 58.
