---
id: five-ray-annular-current-supply
kind: question
title: Supply currents with nonpositive residual for every annular increment on the thirty five-ray sequences
status: open
claim: >
  Odd-only 3x+1 map, absorbing at 1; A_N = Π^R_(64N) − Π^R_N the six-band annulus of disjoint-annular-recursion.
  For every N = a·2^r·64^k with a ∈ {12, 14, 16, 18, 21}, r ∈ {3, …, 8}, k ≥ 0, construct finite signed J_N, ζ_N
  with A_N = (I − P)J_N + ζ_N and ζ_N ≤ 0 (no bound on size or cost required), or equivalently construct such
  certificates for Π^R_M at every M on the five rays and prove the construction terminates. By
  five-ray-current-criterion and disjoint-annular-recursion this suffices for the Collatz conjecture, and the
  conjecture implies it; it is a sharper form of packet-current-supply, not an easier problem.
created: 2026-10-17
tags: [convergence, packet-currents, annular, five-rays, frontier, collatz-equivalent]
---

# Supply currents with nonpositive residual for every annular increment on the thirty five-ray sequences

## Question

For every cutoff `N` on the thirty sequences `N_k = a·2^r·64^k` (`a ∈ {12, 14, 16, 18, 21}`, `r = 3, …, 8`, `k ≥ 0`), construct finite signed measures `J_N, ζ_N` with

```
A_N = (I − P)J_N + ζ_N,     ζ_N ≤ 0 pointwise,
```

where `A_N` is the explicit six-band annulus of [`disjoint-annular-recursion`](../results/disjoint-annular-recursion/README.md) and `P` pushes through the odd-only map, killing mass at 1. Size and positive cost may depend arbitrarily on `N`. Equivalently (legacy wording): prove that an arithmetic current construction terminates on all five rays.

## Why it matters

The initial packets of the thirty sequences already have exact currents ([`five-ray-current-criterion`](../results/five-ray-current-criterion/README.md), corollary), and `Π^R_(N_k) = Π^R_(N_0) + Σ_(i<k) A_(N_i)` with disjoint supports. So a positive answer gives certificates at every five-ray cutoff and hence, by [`five-ray-current-criterion`](../results/five-ray-current-criterion/README.md), the Collatz conjecture; conversely the conjecture gives exact currents for every `A_N`. The unresolved input is fully explicit: the six rows of the modulo-18 table. By [`class-wise-obligation-equivalence`](../results/class-wise-obligation-equivalence.md) the obligation is equivalent, invariant class by invariant class, to the absence of nontrivial cycles and of divergent orbits at full strength. It is the target of the legacy residual-progress line (R10–R94).

## Known progress

- **What a certificate must do:** a current exists exactly when every nonabsorbing orbit component has nonpositive mass ([`orbit-component-current-criterion`](../results/orbit-component-current-criterion/README.md)); zero total mass in a band does not imply finite current existence. On a finite exposed graph the obstruction is the integer potential `Φ` ([`exposure-potential-boundary-flux`](../results/exposure-potential-boundary-flux/README.md)); the open step is [`annular-component-progress-lemma`](annular-component-progress-lemma.md).
- **Partial currents:** an explicit universal partial current removes positive mass `73N/48 + O(1)` of `99N/4` ([`universal-annular-partial-current`](../results/universal-annular-partial-current/README.md), [`affine-common-tail-tree-lifting`](../results/affine-common-tail-tree-lifting/README.md)); a one-pass compression to `19/22` of the norm cannot be iterated ([`annular-root-collapse-contraction`](../results/annular-root-collapse-contraction/README.md)).
- **Finite certificates:** stored currents for `A_96` (nonpositive residual) and `A_168` (exact), with cross-band cancellation at 168 ([`affine-common-tail-tree-lifting`](../results/affine-common-tail-tree-lifting/README.md)).
- **Obstructions to narrow strategies:** positive cost is necessary (`H_53(A_96) = 699`); bounded per-packet catalogues fail ([`bounded-packet-certificate-obstruction`](../results/bounded-packet-certificate-obstruction/README.md)); fixed-modulus profiles do not close under literal pushforward ([`outer-profile-closure-obstruction`](../results/outer-profile-closure-obstruction.md)); fixed binary-residue views see zero ([`binary-residue-projection-information-loss`](../results/binary-residue-projection-information-loss.md)); balanced bands and zero scalar work do not imply a current ([`reflected-negative-annulus-control`](../results/reflected-negative-annulus-control/README.md)); the source-scale recursion keeps an expanding `3N/2` term ([`disjoint-annular-recursion`](../results/disjoint-annular-recursion/README.md)); cancelling above the bottom stalled ([`annular-bottom-cancellation-attempt`](../attempts/annular-bottom-cancellation-attempt.md)).
- **Barriers:** no argument using only properties shared by `3x+61` can work ([`locally-collatz-like-control-barrier`](../results/locally-collatz-like-control-barrier/README.md), [`progress-measures-control-3x-61`](../results/progress-measures-control-3x-61.md)).
- **Rounds R11–R24.** A conditional finite compiler that turns supplied five-ray packet certificates into integer absorption ([`finite-rational-cone-integer-certificate`](../results/finite-rational-cone-integer-certificate/README.md), demonstrated in [`actual-graph-current-compiler`](../results/actual-graph-current-compiler/README.md)); the automatic inner-interval input is circular ([`local-packet-calibration-extension`](../results/local-packet-calibration-extension/README.md)); the packing grows to `1073N/432 + O(1)` ([`release-source-packing`](../results/release-source-packing/README.md)); exact obstructions to fixed operator words, fixed depths and short delays ([`root-transport-normal-form`](../results/root-transport-normal-form/README.md), [`unbounded-exposure-depth-necessary`](../results/unbounded-exposure-depth-necessary/README.md), [`short-delay-all-phase-obstruction`](../results/short-delay-all-phase-obstruction/README.md), [`fixed-ternary-order-unbounded-depth`](../results/fixed-ternary-order-unbounded-depth/README.md)). The line then pivoted to the outer complement of the single-cutoff packet: given absorption through `N`, the remaining outer roots `R_N` ([`retained-graph-complement-constructor`](../results/retained-graph-complement-constructor/README.md)), reduced by annular transfer and halving ([`annular-complement-outer-descent`](../results/annular-complement-outer-descent/README.md), [`halving-coalescence-return`](../results/halving-coalescence-return/README.md)); completing the rest on the interleaved rays would suffice ([`five-ray-complementary-profile-completion`](five-ray-complementary-profile-completion.md)).
- R25–R39 worked on the outer complement of [`five-ray-complementary-profile-completion`](five-ray-complementary-profile-completion.md) (Known progress there): an exact bridge quotient ([`elementary-bridge-quotient-normal-form`](../results/elementary-bridge-quotient-normal-form/README.md)), complete run bridges ([`complementary-run-bridges`](../results/complementary-run-bridges/README.md)), and a reduction to tripling and doubling pairs on an exact critical domain ([`tripling-doubling-pair-decomposition`](../results/tripling-doubling-pair-decomposition/README.md), [`critical-tripling-domain-equivalence`](../results/critical-tripling-domain-equivalence/README.md)). R40–R60 reduced the critical pair domain to the Collatz-equivalent question [`universal-w5-tripling-currents`](universal-w5-tripling-currents.md) and built strict-rank rules and scoped obstructions on it (Known progress there). The later legacy main-lane rounds built many further partial constructions and exact obstructions: R61–R77 on the same critical pair domain (Known progress of [`universal-w5-tripling-currents`](universal-w5-tripling-currents.md), from [`exponent-eleven-exit-continuation`](../results/exponent-eleven-exit-continuation/README.md) to [`same-seed-factor-complexity-bound`](../results/same-seed-factor-complexity-bound/README.md)), and R78–R94 ran native and smaller-origin history comparisons on the same domain, from [`native-critical-nine-continuation`](../results/native-critical-nine-continuation/README.md) to [`prescribed-ternary-child-unbounded-clocks`](../results/prescribed-ternary-child-unbounded-clocks/README.md) (Known progress of [`universal-w5-tripling-currents`](universal-w5-tripling-currents.md)), and left the final obligation [`residual-pair-864z-257-supply`](residual-pair-864z-257-supply.md); universal terminal supply stayed unresolved.

## Suggested attacks

- Close the residual of [`universal-annular-partial-current`](../results/universal-annular-partial-current/README.md) in a family with a proved decreasing integer parameter, or prove the progress lemma for `Φ`.
- A source-scale induction must address its expanding `3N/2` term. Run every candidate on the `T_61` increments first; anything that "succeeds" there is wrong. Do not assume a generic tree lift covers an annulus, do not reapply `19/22` to an unproved residual class, and do not treat coarse zero projections as integer matching (legacy round report, [`archive/convergence-annular-construction/REPORT.md`](../../../archive/convergence-annular-construction/REPORT.md)).
