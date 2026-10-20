---
id: packet-current-supply
kind: question
title: Supply a finite current with nonpositive residual for the right-aligned packets at every cutoff
status: open
claim: >
  Odd-only clock, absorbing at 1. Prove that for every integer N ≥ 8 there are finite signed measures J_N,
  ζ_N with Π^R_N = (I − P)J_N + ζ_N and ζ_N ≤ 0 pointwise (no bound on the size or cost of J_N is required),
  or equivalently that sup_L H_L(Π^R_N) < ∞ for every N. By qualitative-current-criterion this is
  equivalent to the convergence half of the Collatz conjecture together with the absence of nontrivial
  cycles, i.e. to the full conjecture; it is a reformulation, not an easier special case.
created: 2026-10-17
tags: [convergence, packet-currents, frontier, collatz-equivalent]
---

# Supply a finite current with nonpositive residual for the right-aligned packets at every cutoff

## Question

For every integer `N ≥ 8`, construct finite signed measures `J_N, ζ_N` with `Π^R_N = (I − P)J_N + ζ_N` and `ζ_N ≤ 0`, where `Π^R_N` is the right-aligned packet measure of [`right-aligned-fixed-core-remainder`](../results/right-aligned-fixed-core-remainder/README.md) and `P` pushes forward through the odd-only map, killing mass at 1. The size and positive cost of `J_N` may depend arbitrarily on `N`. Exact currents (`ζ_N = 0`) are a special case.

## Why it matters

By [`qualitative-current-criterion`](../results/qualitative-current-criterion.md) a positive answer is equivalent to the Collatz conjecture: every positive integer reaches 1. A finite current is checkable one row at a time ([`finite-current-certificate-identity`](../results/finite-current-certificate-identity.md)), so any finite batch of cutoffs can be certified by computation, as in [`packet-currents-snapshot`](../results/packet-currents-snapshot/README.md) for a different packet family. The question is the universal supply. It is **not** a weaker problem: [`class-wise-obligation-equivalence`](../results/class-wise-obligation-equivalence.md) shows that, restricted to any invariant class avoiding the verified base, it is exactly "that class is empty", so it contains both "no nontrivial cycles" and "no divergent orbits" at full strength.

## Known progress

- **Reformulation:** [`qualitative-current-criterion`](../results/qualitative-current-criterion.md); the error terms are controlled by [`right-aligned-fixed-core-remainder`](../results/right-aligned-fixed-core-remainder/README.md) and, at dyadic cutoffs, [`dyadic-cutoff-core-remainder`](../results/dyadic-cutoff-core-remainder.md).
- **Sparser targets (legacy, not yet migrated):** five dyadic rays suffice (legacy R5), and along them the 64-fold annular increments `A_N` give an explicit sufficient target with its finite bases discharged (legacy R6); see `experiments/current_construction/` (batch B08).
- **What currents detect (legacy R7):** a finite exact current exists exactly when every nonabsorbing orbit component has total mass zero; bounded per-packet catalogues cannot suffice.
- **The legacy main-lane programme R8–R94** (`experiments/annular_construction/`, `experiments/residual_progress/`, not yet migrated) built many partial currents and proved many exact obstructions; universal terminal supply stayed unresolved, and the line was frozen at R94.
- **Lower bounds on certificates:** [`exact-current-minimality`](../results/exact-current-minimality.md).
- **Barriers:** no argument using only properties shared by `3x+61` can work ([`locally-collatz-like-control-barrier`](../results/locally-collatz-like-control-barrier/README.md)); one-pass compression and early fall of the exposure potential are not evidence of progress ([`progress-measures-control-3x-61`](../results/progress-measures-control-3x-61.md)); a direct cancellation-above-the-bottom attempt stalled ([`annular-bottom-cancellation-attempt`](../attempts/annular-bottom-cancellation-attempt.md)).

## Suggested attacks

Run every candidate constructor or progress argument on the controls `(d, N) = (61, 213)`, `(−1, 16)` and the `T_61` increments first; anything that "succeeds" there is wrong. Name the `d = 1`-specific arithmetic each step uses. *Speculation:* the legacy programme's later rounds pursued smaller-seed history comparisons and shrinking paired recursions; their nodes will be linked here when migrated.
