---
id: uniform-aggregate-exposure-depth
kind: question
title: Is there a uniform exposure depth that certifies every whole packet or annulus?
status: answered
answered_by: [unbounded-exposure-depth-necessary]
claim: >
  Odd-only 3x+1 map, absorbing at 1; historical exposure of d forward steps from every nonzero source atom of
  the whole right-aligned packet Π^R_N (or annulus A_N). Is there a constant D such that, for every cutoff N
  on the five rays, every exposed component at depth D not containing 1 has nonpositive source mass? A positive
  answer would be a strong theorem implying the universal current criterion. Legacy status: "a separate
  candidate, not a theorem".
created: 2026-10-17
tags: [convergence, packet-currents, exposure-depth, candidate]
---

# Is there a uniform exposure depth that certifies every whole packet or annulus?

## Question

Expose `D` steps from every source atom of the whole packet `Π^R_N` (or of the annulus `A_N`), retaining historical intersections ([`orbit-component-current-criterion`](../results/orbit-component-current-criterion/README.md)). Is there a single `D`, independent of `N` on the five rays, such that every component not linked to 1 has nonpositive source mass?

## Why it matters

A uniform aggregate depth would give finite certificates at every five-ray cutoff by a bounded search, and so would imply the universal current criterion ([`five-ray-current-criterion`](../results/five-ray-current-criterion/README.md)). Its failure would show that any constructor must let its depth grow with the cutoff.

## Known progress

- The per-triple obstruction [`bounded-packet-certificate-obstruction`](../results/bounded-packet-certificate-obstruction.md) does not decide it: the aggregate construction uses many more atoms and allows cancellation between triples.
- Finite data only: depths at most 71 fail at `N = 65536` for whole packets, in both certificate modes, and the first successes at ten sampled cutoffs range from 8 to 72 ([`whole-packet-historical-certificates`](../results/whole-packet-historical-certificates/README.md)). The sample is too small to infer eventual boundedness or growth.
- Fixed-precision shadow indicators cannot be positive dual witnesses for the annulus ([`binary-residue-projection-information-loss`](../results/binary-residue-projection-information-loss.md)); literal fixed-modulus pushforward does not close ([`outer-profile-closure-obstruction`](../results/outer-profile-closure-obstruction.md)). Neither proves unbounded aggregate depth.
- **Answered (negatively) for annuli** by [`unbounded-exposure-depth-necessary`](../results/unbounded-exposure-depth-necessary/README.md) (legacy R13): for every fixed `D`, infinitely many cutoffs `N = 96·64^(3^D t − 2)` on the required ladder have a complete exposed component of `A_N` at depth `D` with source mass 2, not containing 1; so `d*(96·64^k) ≥ v_3(k + 2) + 1`, sharpened to `+ 4` by [`delayed-release-cancellation`](../results/delayed-release-cancellation/README.md), and even with the ternary order fixed at 2 ([`fixed-ternary-order-unbounded-depth`](../results/fixed-ternary-order-unbounded-depth/README.md)). The legacy record states the answer for annuli ("it cannot"); it does not write out a separate whole-packet version. The route went through the complete depth-32 obstruction [`depth-32-aggregate-exposure-obstruction`](../results/depth-32-aggregate-exposure-obstruction/README.md) and its infinite lift [`depth-32-obstruction-infinite-family`](../results/depth-32-obstruction-infinite-family.md).
- How the whole-annulus depth `d*` actually grows is the open, data-driven [`exposure-absorption-giant-component`](exposure-absorption-giant-component/README.md).

## Suggested attacks

A negative answer needs a shadowing argument that controls all extra source atoms in the actual exposed component and produces a positive total after their cancellations, not only an isolated triple. (Done for annuli by the inverse-history invariant of [`unbounded-exposure-depth-necessary`](../results/unbounded-exposure-depth-necessary/README.md).)
