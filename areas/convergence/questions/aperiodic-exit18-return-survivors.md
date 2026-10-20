---
id: aperiodic-exit18-return-survivors
kind: question
title: Does any positive integer make infinitely many exit-18 returns to the mixed-growth guard?
status: open
claim: >
  Odd-only 3x+1 map S, absorbing at 1. In the two-return subsystem of exit18-return-integer-cylinders (guard G = {w
  = 40529845 mod 2^26}, returns V(w) = (3^12 w + 311195)/2^19 and R(w) = (3^24 w + 328537586155)/2^37 on their
  complete return domains), prove or refute: no positive integer follows an infinite V/R itinerary. Every finite
  word is realised (with a seed depending on the word), eventually periodic itineraries have negative rational
  points, possible survivors have density zero with at most 3 (X/2^26)^alpha of them in [1, X], and a fixed
  survivor needs factor complexity liminf p(L)/L >= 18.285...; so the target is the aperiodic, high-complexity
  case. A constraint on the same integer across unbounded prefixes is needed.
created: 2026-10-18
tags: [convergence, outer-residual, mixed-rank, two-adic-coding, factor-complexity, frontier]
---

# Does any positive integer make infinitely many exit-18 returns to the mixed-growth guard?

## Question

In the return subsystem of [`exit18-return-integer-cylinders`](../results/exit18-return-integer-cylinders/README.md) (R74), the guard of the mixed growing block `G = {w > 0 : w ≡ 40529845 (mod 2^26)}` has two disjoint complete returns, `V` on `2218391138229 mod 2^45` and `R` on `8515171531530858421 mod 2^63`, both strictly increasing. Is there a positive integer whose itinerary of `V`/`R` returns is infinite? Equivalently, is the 2-adic point of some infinite word over `{V, R}` a positive integer?

## Why it matters

Each return retains a higher leading pair request, so an infinite survivor would be an unbounded chain of the conditional growing comparisons of [`mixed-rank-growing-blocks`](../results/mixed-rank-growing-blocks/README.md) (R67) and [`mixed-exit-growing-reentry`](../results/mixed-exit-growing-reentry/README.md) (R70) that this rule choice never closes. Proving that none exists would show that this subsystem always exits, a step toward a progress measure across complete block exits; it would not by itself supply the pair currents of [`universal-w5-tripling-currents`](universal-w5-tripling-currents.md), nor show termination of other comparisons. No positive survivor is known or constructed.

## Known progress

- **Finite words are realised; periodic words are not.** Every finite word has one complete cylinder mod `2^(26+e)` of positive realisations; every eventually periodic infinite itinerary has a negative rational starting point ([`exit18-return-integer-cylinders`](../results/exit18-return-integer-cylinders/README.md)). Finite-prefix integrality, even with an extra odd congruence, cannot exclude any word.
- **Sparsity.** For fixed `m` the integers with at least `m` returns have density `2^(−26)·s^m`, `s = 2^(−19) + 2^(−37)`; possible survivors have density zero and number at most `3(X/2^26)^α` in `[1, X]`. Sparsity does not prove emptiness.
- **Same-seed complexity.** A fixed survivor's itinerary has `liminf p(L)/L ≥ 19/log₂(3^24/2^37) = 18.285…`, so `p(L) ≤ 18L + O(1)` is impossible; every seed at most `260028359941009900571662033` makes fewer than 37 consecutive returns ([`same-seed-factor-complexity-bound`](../results/same-seed-factor-complexity-bound/README.md), R77). The general-orbit analogue is [`divergent-orbit-itinerary-complexity`](../results/divergent-orbit-itinerary-complexity/README.md).
- **Limits.** Real and 2-adic limits of the inverse expansions cannot be identified (an explicit powers-of-three sequence has real limit 0 and 2-adic limit 1), and periodic negative rational points need not be the only obstruction.

## Suggested attacks

- A constraint tying one integer across unboundedly many prefixes that grows faster than the linear complexity bound (the legacy decision after R74: "a constraint on the **same integer across unbounded prefixes**, a well-founded state that survives both return branches, or a different signed-current construction").
- Any argument must use the integrality of the one seed, not identities that transfer to rationals (see the cycles attempt [`scaling-transfer-to-3x-plus-d`](../../cycles/attempts/scaling-transfer-to-3x-plus-d/README.md)). Speculation: combining the 2-adic cylinder spacing with an archimedean height bound sharper than `Λ^j`, as in R77, is the only mechanism tested so far.
