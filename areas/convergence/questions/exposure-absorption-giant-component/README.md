---
id: exposure-absorption-giant-component
kind: question
title: Does the component of 1 absorb all but a vanishing fraction of an annulus's positive mass by exposure depth c log N?
status: open
claim: >
  Odd-only 3x+1 map, absorbing at 1; A_N the six-band annulus; G_d(N) the first d forward arrows exposed from
  every nonzero source of A_N. Is there a constant c such that the share of the positive mass of A_N lying in
  the component of 1 in G_d(N) tends to 1 when d = c log N (along the five rays, or along N = 96 2^k)? And
  what sets the whole-annulus depth d*(N), the first depth at which no component outside that of 1 has
  positive source mass? The side lane's question Q1; the finite data are heuristic evidence only.
created: 2026-10-17
evidence:
  - "q1_giant_component.py, q1_giant_component.json: side-lane probe (Claude side lane, 2026-10-18) for N = 96 2^k, k = 0..9: the absorbed share of positive mass as a function of depth and the depths reaching 50%, 90%, 99%, 99.9% and 100%. Its receipt is nondeterministic in the legacy record and is never a certificate. Fails at its new path: it imports affine_controls and progress_measures_audit from experiments/packet_currents/negative_controls/ by repository-relative path (now ../../results/locally-collatz-like-control-barrier/). Passed at be73a66 as reviews/side_lane/q1_giant_component.py (archive/legacy-checker-run-be73a66.md, exit 0)"
  - "slow_cluster_probe.py, slow_cluster_probe.json: side-lane probe (Claude side lane, 2026-10-17): d*(N) at N = 96, 112, 128, 144, 168 and 64N, and the last positive component. Fails at its new path: it imports affine_controls and progress_measures_audit from experiments/packet_currents/negative_controls/ by repository-relative path (now ../../results/locally-collatz-like-control-barrier/), and it imports depth_probe from its own folder (now ../../results/unbounded-exposure-depth-necessary/). Passed at be73a66 as reviews/side_lane/slow_cluster_probe.py (archive/legacy-checker-run-be73a66.md, exit 0) (about 120 s)"
tags: [convergence, packet-currents, annular, exposure-depth, density, side-lane]
---

# Does the component of 1 absorb all but a vanishing fraction of an annulus's positive mass by exposure depth c log N?

## Question

For the annulus `A_N` of [`disjoint-annular-recursion`](../../results/disjoint-annular-recursion/README.md) and its historical exposure graphs `G_d(N)` ([`depth-32-aggregate-exposure-obstruction`](../../results/depth-32-aggregate-exposure-obstruction/README.md)), let `ε_N(d)` be the share of the positive mass of `A_N` outside the component of 1 in `G_d(N)`. Is `ε_N(c·log N) → 0` for some constant `c`, along the required rays? Separately, what governs `d*(N)`, the least depth at which no component outside that of 1 has positive source mass?

## Why it matters

If all but an explicitly thin remainder of the positive mass is absorbed at logarithmic depth, almost-all descent estimates (which apply to unions of residue classes over long intervals, e.g. [`tao-2019-almost-all`](../../../../sources/tao-2019-almost-all.md)) might reduce the annular supply problem [`five-ray-annular-current-supply`](../five-ray-annular-current-supply.md) to that remainder (side lane's motivation; speculative). A depth law for `d*(N)` would also say whether an induction down the `×64` ladder of [`disjoint-annular-recursion`](../../results/disjoint-annular-recursion/README.md) is plausible.

## Known progress

- **Proved:** `d*` is unbounded on the ladder, `d*(96·64^k) ≥ v_3(k + 2) + 4` ([`unbounded-exposure-depth-necessary`](../../results/unbounded-exposure-depth-necessary/README.md), [`delayed-release-cancellation`](../../results/delayed-release-cancellation/README.md)); no uniform depth works ([`uniform-aggregate-exposure-depth`](../uniform-aggregate-exposure-depth.md)).
- **Finite data, `N = 96·2^k`, `k = 0..9`** (feed 2026-10-18 10:58, `q1_giant_component.py`): the depths at which 50%, 90%, 99% of the positive mass is absorbed stay at about 2, 7 and 22–25 while `N` grows 512-fold; the unabsorbed share at fixed depth barely moves (about 17% at depth 4, 8% at 8, 2.5% at 16, 0.4–0.5% at 32). Only the extreme tail grows: the last positive source joins at depth 33 for `N = 96` and 113 for `N = 49152`, about `7.3·log₂N` at the top of this range. In the measured range a fixed depth absorbs all but `ε(d)`, nearly independent of `N`; no asymptotic claim is made.
- **Finite data, slow clusters** (feed 2026-10-17 19:34, `slow_cluster_probe.py`): `d*(N)` for `N = 8a`, `a ∈ {12, 14, 16, 18, 21}`, is 28, 32, 44, 29, 34, and for `64N` it is 64, 91, 90, 90, 90. At `64N` the last positive component for rays 14, 16, 18 and 21 contains the same twelve absolute states `270271, 360361, 405407, 432923, 480481, 487039, 608111, 649385, 730559, 810815, 865847, 912167` (stopping times of about 150 odd steps). So in these samples the end of the last plateau is fixed by absolute slow orbits, not inherited from the obstruction one scale down.
- For the protected three-source chains, the plateau ends when the chain's own orbit returns to the source support ([`unbounded-exposure-depth-necessary`](../../results/unbounded-exposure-depth-necessary/README.md), Remarks).

## Suggested attacks

- Speculative (side lane): treat the absorbed share as a giant-component problem and bound `ε_N(d)` by an almost-all stopping-time estimate on the union of residue classes forming `A_N`; any such argument must also run on the `T_61` increments of [`progress-measures-control-3x-61`](../../results/progress-measures-control-3x-61.md), where a positive component persists forever.
- Explain `d*` by absolute slow clusters: show that the last positive component at scale `N` is governed by orbits with the largest stopping times in the window, not by the scale.
