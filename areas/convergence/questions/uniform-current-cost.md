---
id: uniform-current-cost
kind: question
title: Bound the exit-profile cost of currents for the exact-source packets uniformly in the cutoff
status: open
claim: >
  Odd-only clock, absorbing at 1. With m = floor(2·ceil(log₂N)/9) and Π̂_(m,N) the exact-source packet
  family of packet-currents-snapshot, construct finite currents J_N with Π̂_(m,N) = (I − P)J_N + ζ_N such
  that the exit-profile positive cost satisfies C_+(J_N) = O(N) and ‖ζ_N⁺‖₁ = O(N^(4/5)/log N), uniformly in
  N, by an arithmetic construction from the source words (exact currents with C_+(J_N) = O(N) would be
  stronger). This would give a one-sided O(N) bound on the programme's discrepancy E_T(N) on its
  source-power time window.
created: 2026-10-17
tags: [convergence, packet-currents, current-cost, quantitative]
---

# Bound the exit-profile cost of currents for the exact-source packets uniformly in the cutoff

## Question

Let `b = ceil(log₂ N)`, `m = floor(2b/9)`, and `Π̂_(m,N)` the exact-source packet family of [`packet-currents-snapshot`](../results/packet-currents-snapshot/README.md). Find finite currents `J_N` with

```
Π̂_(m,N) = (I − P)J_N + ζ_N,     C_+(J_N) = O(N),     ‖ζ_N⁺‖₁ = O(N^(4/5)/log N),           (7.2)
```

uniformly in `N`, where `C_+(J) = Σ_z max(0, max_u F_z(u))` is the exit-profile upper cost of [`finite-current-certificate-identity`](../results/finite-current-certificate-identity/README.md). The stronger exact form is `Π̂_(m,N) = (I − P)J_N` with `C_+(J_N) = O(N)` (7.1). No estimate on the negative residual is needed for the upper bound. The cost must be derived from the source-word arithmetic and the fixed interval cutoffs; a universal construction algorithm with no cost control would not suffice.

## Why it matters

By Corollary 2.2 of [`packet-currents-snapshot`](../results/packet-currents-snapshot/README.md) and the exit-profile bound, (7.1) or (7.2) would give the one-sided `O(N)` discrepancy estimate on the programme's source-power time window, the quantitative "mean stopping-work" target of the inherited handoff. It is **not** needed for the qualitative conjecture: [`qualitative-current-criterion`](../results/qualitative-current-criterion.md) shows that finite certificates of arbitrary cost at every cutoff already suffice (for a different packet family), which is why the legacy programme moved to [`packet-current-supply`](packet-current-supply.md).

## Known progress

- Finite only: at 14 named cutoffs currents were found by following orbits, and the observed exit-profile upper costs are below `N` (e.g. 63,824 at `N = 262144`, less than `N/4`) ([`packet-currents-snapshot`](../results/packet-currents-snapshot/README.md)). The snapshot explicitly declines to extrapolate: "a larger list of successful certificates cannot establish their asymptotic validity".
- Neither (7.1) nor (7.2) is proved for any infinite set of cutoffs.

## Suggested attacks

The snapshot's roadmap (`collatz_packet_currents/roadmap.md` in [`packet-currents-snapshot`](../results/packet-currents-snapshot/README.md)) asks for an arithmetic construction from the source words, not a larger search. Its guardrails: a current is signed arithmetic on arrows, not a probability distribution; equal-time total-variation contraction is unnecessary; no iid tail, no assumed convergence of an unexamined exit, and no deletion of source multiplicities. The minimality lemma ([`exact-current-minimality`](../results/exact-current-minimality.md)) gives a lower bound on any exact construction's cost.
