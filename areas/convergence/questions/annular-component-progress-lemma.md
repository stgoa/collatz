---
id: annular-component-progress-lemma
kind: question
title: Prove that every positive exposed-component plateau of an annulus ends after finitely many arithmetic extensions
status: open
claim: >
  Odd-only 3x+1 map, absorbing at 1; A_N the annulus of disjoint-annular-recursion on the thirty five-ray
  sequences; Φ the exposure potential of exposure-potential-boundary-flux. Prove that for every such N and
  every positive component C of an exposed graph of A_N not containing 1, some finite arithmetic extension of
  the graph either merges C with enough negative source mass to lower Φ or connects it to 1; that is, every
  positive plateau of Φ ends. Since Φ is a nonnegative integer, this would give a terminating constructor and
  answer five-ray-annular-current-supply.
created: 2026-10-17
tags: [convergence, packet-currents, annular, progress-potential, frontier]
---

# Prove that every positive exposed-component plateau of an annulus ends after finitely many arithmetic extensions

## Question

Given a positive exposed component of an annular source `A_N` on one of the thirty base-64 sequences, prove that a finite arithmetic extension of the graph either reduces its positive mass through a negative merger or connects it to the absorber. Equivalently, give a finite arithmetic rule that ends every positive exposed-component plateau of the potential `Φ` of [`exposure-potential-boundary-flux`](../results/exposure-potential-boundary-flux/README.md).

## Why it matters

`Φ` is a nonnegative integer that never increases and is zero exactly when the exposed graph supports a current with nonpositive residual. A strict decrease after each finite extension therefore bounds the number of steps and gives a terminating constructor, answering [`five-ray-annular-current-supply`](five-ray-annular-current-supply.md) and hence the Collatz conjecture.

## Known progress

- At `A_96`, `Φ = 17` at depths 20–27 and 0 at depth 28 ([`exposure-potential-boundary-flux`](../results/exposure-potential-boundary-flux/README.md)). A finite scan cannot establish the lemma for all cutoffs.
- Neither the scalar five-ray contraction, nor source-table balance, nor the fixed-residue identities supplies it: the five-ray comparison is in the cutoff index and gives no bound on plateau duration; omitting the boundary flux of the scale identity, or zeroing it at one cutoff, does not prove progress ([`exposure-potential-boundary-flux`](../results/exposure-potential-boundary-flux/README.md), [`binary-residue-projection-information-loss`](../results/binary-residue-projection-information-loss.md)).
- On `3x+61`, `Φ` falls by about 97% early and then stays positive forever because a positive component contains a cycle ([`progress-measures-control-3x-61`](../results/progress-measures-control-3x-61.md)); a proof must use a property of `3x+1` that `T_61` lacks.
- The residual-progress rounds pursued this obligation. R11–R24: a finite compiler that ends a plateau if its packet inputs are supplied ([`finite-rational-cone-integer-certificate`](../results/finite-rational-cone-integer-certificate/README.md)); no fixed exposure depth suffices ([`unbounded-exposure-depth-necessary`](../results/unbounded-exposure-depth-necessary/README.md)); explicit cancellations after arbitrarily long isolation ([`delayed-release-cancellation`](../results/delayed-release-cancellation/README.md)), which fail to cover most phases at short depth ([`short-delay-all-phase-obstruction`](../results/short-delay-all-phase-obstruction/README.md), [`fixed-ternary-order-unbounded-depth`](../results/fixed-ternary-order-unbounded-depth/README.md)); terminating normalizations with unavoidable positive remainders ([`auxiliary-normalisation-remainder`](../results/auxiliary-normalisation-remainder/README.md), [`signed-path-collapse-capacity`](../results/signed-path-collapse-capacity/README.md)); and exits into source-empty components ([`bounded-source-cluster-local-bound`](../results/bounded-source-cluster-local-bound/README.md)). R25–R39 continued through bridge and pair constructions on the outer complement (see [`five-ray-complementary-profile-completion`](five-ray-complementary-profile-completion.md), Known progress), and the later rounds R40–R94 (`experiments/residual_progress/`, not yet migrated) through rank and history constructions; it stayed open.

## Suggested attacks

- Use the explicit finite measure `K_N` of the scale identity to expose arithmetic boundary rows instead of expanding every orbit uniformly, and prove the extensions reduce positive mass (legacy suggestion in [`exposure-potential-boundary-flux`](../results/exposure-potential-boundary-flux/README.md)).
- If an argument instead shows that all sources enter a known halting interval, describe it as a descent proof, not as current cancellation ([`whole-packet-historical-certificates`](../results/whole-packet-historical-certificates/README.md)).
