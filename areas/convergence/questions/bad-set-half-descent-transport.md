---
id: bad-set-half-descent-transport
kind: question
title: Does first-half transport contract the truncated power count of the actual nonabsorbing set?
status: open
claim: >
  Odd-only 3x+1 map S absorbed at 1; B the positive odd nonabsorbing seeds; L(n) the first odd iterate <= n/2 of odd
  n > 1; G(B) = {odd n > 1 : L(n) in B}; for fixed modulus M and positive rational residue weights w_r, F(X) and g(X)
  the weighted counts of B and G(B) through X, and C_alpha(X) = max_(1<=Y<=X) F(Y)/Y^alpha. Find, for some
  alpha < 1 (e.g. alpha = 99/100), explicit M, weights, an integer X0 >= 2 and a rational 0 <= kappa < 1 such that
  (P) g(X) <= kappa X^alpha C_alpha(floor(X/2)) for every integer X >= X0, covering the whole first-half map with
  arbitrary input-dependent odd clocks; or show no such data exist. Its analogue fails for every 3x+d, d > 1, so a
  proof must use 3x+1 arithmetic.
created: 2026-10-18
tags: [convergence, phase6, stopping-time, transport, nonabsorbing-set, frontier]
---

# Does first-half transport contract the truncated power count of the actual nonabsorbing set?

## Question

Premise (P) of [`bad-set-transport-bootstrap`](../results/bad-set-transport-bootstrap.md) §2, for the actual `d = 1` set `B`. It uses only a finite input maximum `C_alpha(floor(X/2))`, so it does not hide the desired finite global norm in its hypotheses. A finite word catalogue alone does not establish it.

## Why it matters

By [`bad-set-transport-bootstrap`](../results/bad-set-transport-bootstrap.md), (P) with the explicit S.1 exceptional bound gives `B(X) ≤ (C*/w_min) X^alpha`, and (P) with `e(X) = o(X)` alone gives `B(X) = o(X)`. With the linear lower bound of [`nonabsorbing-set-linear-lower-density`](../results/nonabsorbing-set-linear-lower-density/README.md) either conclusion makes `B` empty, so (P) is a Collatz-equivalent criterion, not an easier theorem. It is the `B`-specific premise left open by the two arbitrary-target barriers of route node S.2 ([`universal-w5-quotient-stopping`](universal-w5-quotient-stopping.md)).

## Known progress

- The analogue of (P) is **false** for the actual nonabsorbing set of every supported `3x+d`, `d > 1` ([`bad-set-transport-bootstrap`](../results/bad-set-transport-bootstrap.md) §4): the odd multiples of `d` give `limsup F_d(X)/X > 0`.
- Arbitrary-target versions are refuted: [`arbitrary-target-linear-transport-barrier`](../results/arbitrary-target-linear-transport-barrier/README.md), [`growth-norm-transport-barrier`](../results/growth-norm-transport-barrier/README.md). Their constructed targets are not in `B` and do not satisfy its invariance, so they do not refute (P).
- The exact two-level ternary residue system cannot prove (P) through its leading-coefficient relaxation: [`c2a-two-level-residue-relaxation`](../attempts/c2a-two-level-residue-relaxation.md).

## Suggested attacks

Write a sound finite inequality system that incorporates actual invariance, the ternary-lift constraints (each odd arrow needs one more ternary digit at the target; the `a = 1` cutoff `(3X+1)/2` is advanced) and the complete first-half map, then test the same reasoning on `B_d`, where it must fail. Krasikov–Lagarias's finite residue difference inequalities give lower bounds on inverse basins; a positive vector or spectral-radius computation must be tied to the correct inequality direction.
