---
id: canonical-rigidity-bounded-invariants
kind: question
title: Must every bounded T-invariant coefficient sequence on the canonical roots vanish?
status: open
claim: >
  Let K be the positive canonical roots of elementary-bridge-quotient-normal-form and T = nu S its quotient map
  (odd-only 3x+1, absorbing at 1). For a bounded real sequence (h_q), q in K, with h_1 = 0, put F(z) = sum h_q z^q
  (analytic for |z| < 1). Show that h_(T(q)) = h_q for every q in K forces F = 0, i.e. every h_q = 0. Every
  hypothetical nonabsorbing component supplies a bounded 0/1 solution, so this is Collatz-equivalent; analyticity
  in the disk is automatic and supplies no rigidity. Phase 6 route node H.2.
created: 2026-10-18
aliases: [P6-H.2]
tags: [convergence, phase6, invariants, analytic, rigidity, collatz-equivalent]
---

# Must every bounded T-invariant coefficient sequence on the canonical roots vanish?

## Question

As in the claim. Any additional regularity assumption must be proved for the component indicators, which already satisfy boundedness and analyticity.

## Why it matters

The finite-support graph duality behind it (route node H.1) is [`orbit-component-current-criterion`](../results/orbit-component-current-criterion/README.md): a finite pair current exists iff every invariant function on the killed graph takes equal values at the two sources; an invariant is constant on each orbit component and zero at the absorber. H.2 asks for the corresponding analytic rigidity on the canonical quotient ([`elementary-bridge-quotient-normal-form`](../results/elementary-bridge-quotient-normal-form/README.md)). A positive answer is equivalent to convergence; a precise rigidity mechanism would be a new route.

**Transfer.** The ordinary-graph analogue fails when there is a nonprincipal cycle, through its basin indicator ([`baseline-obligation-transfer-controls`](../results/baseline-obligation-transfer-controls/README.md)). The quotient-specific `d` version is unestablished: no `d`-quotient is defined, and no analytic mechanism was registered in the Phase 6 harness.

## Known progress

None. The closest published formulation is Berg–Meinardus's analytic encoding ([`berg-1994-analytic-encoding`](../../../sources/berg-1994-analytic-encoding.md); [`route-literature-transfer-audit`](../results/route-literature-transfer-audit.md) L5), whose function space and equivalence differ from this quotient coefficient space; no precise operator or function-space theorem is imported. The Phase 6 ledger deferred H.2 because its conditional natural-boundary classification replaced the missing assertion with an unproved regularity assumption.

## Suggested attacks

A Phase 6 barrier here would be a proof that a named proposed regularity condition does not follow from the coefficient relations; an equivalent reformulation without such a result gives nothing. The invariants area proves rigidity for restricted classes of invariant colourings of the ordinary map (not of this quotient): periodic invariants are constant ([`periodic-invariant-colourings-classification`](../../invariants/results/periodic-invariant-colourings-classification/README.md), formal), and so are binary-automatic ones, given Cobham's theorem ([`binary-automatic-invariant-colourings-constant`](../../invariants/results/binary-automatic-invariant-colourings-constant/README.md), formal), with a complementary finite 2- and 3-Mahler derivation in its `mahler_route.md`; for `3x+d` the automatic ones are exactly functions of `n mod d` ([`d-uniform-automatic-invariant-colourings`](../../invariants/results/d-uniform-automatic-invariant-colourings.md)). Each needs a regularity hypothesis that the component indicators are not known to satisfy, which is exactly the gap named above; the quantitative version is open as [`section-count-depth-ratio-unbounded`](../../invariants/questions/section-count-depth-ratio-unbounded/README.md).

## History

- 2026-10-20, B16 migration (Claude, Opus 5.5): the general pointer to the invariants area in Suggested attacks replaced by links to its rigidity nodes (FOLLOWUPS row from B14).
