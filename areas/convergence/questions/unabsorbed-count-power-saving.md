---
id: unabsorbed-count-power-saving
kind: question
title: Is the number of integers up to X not absorbed by a computable horizon at most C X^(0.84 - epsilon)?
status: open
claim: >
  Odd-only 3x+1 map S absorbing at 1; tau_1 the absorbed odd-arrow hitting time of 1 (infinite for a nonconvergent
  orbit). Produce constants 0 < epsilon < 0.84, C > 0, X0 and a finite computable integer horizon H(X) (clock and
  any growth bound stated; no monotonicity needed) such that #{1 <= n <= X : tau_1(oddpart(n)) > H(X)} <=
  C X^(0.84 - epsilon) for every integer X >= X0. With Krasikov-Lagarias this implies convergence, and convergence
  implies it (take H(X) the maximum stopping time below X), so it is Collatz-equivalent; it is much stronger than
  density zero and fails for every 3x+d, d > 1. Phase 6 route node C.2.
created: 2026-10-18
aliases: [P6-C.2]
tags: [convergence, phase6, density, predecessors, collatz-equivalent]
---

# Is the number of integers up to X not absorbed by a computable horizon at most C X^(0.84 - epsilon)?

## Question

As in the claim. All positive integer seeds are counted, starting the odd-only clock at `oddpart(n)`, so that the count is comparable with published inverse counts.

## Why it matters

With the Krasikov–Lagarias lower bound ([`krasikov-2003-predecessors`](../../../sources/krasikov-2003-predecessors.md)) this bound implies convergence: [`nonabsorbing-set-linear-lower-density`](../results/nonabsorbing-set-linear-lower-density/README.md) (ii), route node C.3. Convergence conversely permits the computable maximum of the finite stopping times below `X` as `H(X)`. Calling it a counting target does not weaken its universal difficulty. Since the audited linear lower bound (C.1a), the weaker [`nonabsorbed-fraction-arbitrarily-small`](nonabsorbed-fraction-arbitrarily-small.md) suffices.

**Transfer.** Fails for every fixed `d > 1`: the positive multiples of `d` stay multiples of `d` and never hit 1; there are `floor(X/d)` such seeds through `X` ([`baseline-obligation-transfer-controls`](../results/baseline-obligation-transfer-controls/README.md)). No extra cycle is needed.

## Known progress

None directly. Tao's almost-bounded theorem and the stopping-time results are benchmarks with weaker or different conclusions ([`route-literature-transfer-audit`](../results/route-literature-transfer-audit.md) L1, L1a, L2); no published bound of this form is imported. Lagarias's bound `c_1 X^h`, `h ≈ 0.95`, counts seeds with infinite strict stopping time, not unabsorbed seeds.

## Suggested attacks

The Phase 6 programme moved from this node to C.2a once the linear lower bound was audited; an attack on C.2 should first say why it would not already settle the weaker C.2a.
