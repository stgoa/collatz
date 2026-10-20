---
id: predecessor-exponent-certificate-replay
kind: question
title: Reproduce the Krasikov–Lagarias predecessor exponent 0.84 with a certified feasible vector and explicit cutoffs
status: open
claim: >
  Calibration target (Phase 6 route node C.1): for the shortcut map C and every fixed positive a not divisible by
  3, Krasikov-Lagarias (2003, Theorem 6.1) prove #{1 <= n <= X : some C^j(n) = a} >= X^0.84 for X >= X0(a).
  Independently reproduce the certified inequality system behind it (Theorem 2.2 with k = 11, lambda = 1.7922310;
  a certified feasible vector, not the paper's displayed decimals, with error bounds) and make the target-dependent
  threshold X0(a) explicit, counting all positive integer predecessors. Transfer to 3x+d is unchecked.
created: 2026-10-18
aliases: [P6-C.1]
tags: [convergence, phase6, predecessors, calibration, krasikov-lagarias]
---

# Reproduce the Krasikov–Lagarias predecessor exponent 0.84 with a certified feasible vector and explicit cutoffs

## Question

As in the claim; see [`krasikov-2003-predecessors`](../../../sources/krasikov-2003-predecessors.md) and [`route-literature-transfer-audit`](../results/route-literature-transfer-audit.md) L3. Published existence of an `a`-dependent threshold is enough for the logical C.3 contradiction ([`nonabsorbing-set-linear-lower-density`](../results/nonabsorbing-set-linear-lower-density/README.md) (ii)); it is not an already reproduced explicit calibration.

## Why it matters

It was the lower premise of the C route before the linear bound of [`lau-density-formal-replay`](../results/lau-density-formal-replay/README.md) was audited. Since then it is no longer the strongest audited lower premise here, and the C route needs the upper side ([`nonabsorbed-fraction-arbitrarily-small`](nonabsorbed-fraction-arbitrarily-small.md)) instead. It remains a well-posed calibration of a published theorem.

**Transfer:** unestablished for the exponent and quantifiers stated; the inverse-tree congruences and collisions must be audited anew for `3x+d`; neither covariance nor the presence of a cycle settles it.

## Known progress

None. The Phase 6 ledger deferred it: the published 0.84 computation needs a reconstructed 59,049-principal-variable certificate that the paper's summary decimals do not supply. A small `k = 2` exponent-2/5 benchmark was suggested as a possible later entry, not the stated 0.84 calibration.

## Suggested attacks

Rebuild the linear program of Theorem 2.2 at `k = 11` with exact rational arithmetic and certify a feasible vector; or start with the `k = 2` benchmark (speculative).
