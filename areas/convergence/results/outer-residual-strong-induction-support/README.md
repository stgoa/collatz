---
id: outer-residual-strong-induction-support
kind: result
title: The outer residual roots are exactly the shell climbers not reached from [1, N] in one or two steps
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1. For every N divisible by 8, N >= 8, the support of the residual profile
  R_N of retained-graph-complement-constructor is exactly
  {odd x : N < x < 3N/2, x = 3 mod 4, x not in S([1,N]) or S^2([1,N])}, with [1,N] the odd seeds; so
  certifying the remaining outer roots from absorption through N is the strong-induction step on this set
  with two-step lookback. Coefficient-2 roots of R_N each represent two original shell atoms, so
  |supp R_N| = 23N/288 + O(1) while ||R_N||_1 = 25N/288 + O(1). Roots divisible by 3 (about half the support at
  the sampled cutoffs) have no odd Syracuse predecessor, so no backward lookback of any depth reaches them;
  this does not prevent forward coalescence or current certificates.
authors:
  - Claude side lane (Opus)
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [retained-graph-complement-constructor]
certificates: [check_support_recompute.py, check_legacy_replay.py]
evidence:
  - "residual_vs_induction.py, residual_vs_induction.json: side-lane probe (Claude side lane, 2026-10-17) that found the identity and checked it exactly at N = 96, 768, 6144, 9216, 49152, 98304 (support 7, 61, 490, 736, 3925, 7850). Fails at its new path: it imports affine_controls from experiments/packet_currents/negative_controls/ by repository-relative path (now ../locally-collatz-like-control-barrier/). Passed at be73a66 as reviews/side_lane/residual_vs_induction.py (archive/legacy-checker-run-be73a66.md, exit 0). The side-lane probes coalescence_check and excursion_merge_probe import its R from their own folders. Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
  - "side_lane_review_20261017_latest.md, side_lane_review_20261017_latest.json: the main lane's review (2026-10-17, side-lane commit 9a0c28d) of the side lane's residual-cylinder and induction feed: §2 is the written proof of this identity for every allowed N; §§3–4 scope the cylinder dynamic programs (cylinder-certificates-outer-residual); §5 corrects the reading of the fixed-h barrier (fixed-ternary-order-unbounded-depth); §6 rechecks the induction of five-ray-profile-completion-suffices. The receipt holds pinned source hashes, exact fractions and the six comparisons with the main lane's residual constructor"
aliases: [R17-b]
tags: [convergence, packet-currents, outer-residual, strong-induction]
---

# The outer residual roots are exactly the shell climbers not reached from [1, N] in one or two steps

## Statement

Odd-only map `S`, absorbing at 1; `R_N` the residual profile of [`retained-graph-complement-constructor`](../retained-graph-complement-constructor/README.md) for `8 | N`, `N ≥ 8` (weight 1 on `x ≡ 3 (mod 12)` in `(N, 3N/2)` and on `x ≡ 7 (mod 12)` in `(9N/8, 3N/2)`, weight 2 on `x ≡ 7, 19 (mod 36)` in `(N, 9N/8)`). Then

```
supp R_N = { x odd : N < x < 3N/2, x ≡ 3 (mod 4), x ∉ S([1,N]_odd) ∪ S²([1,N]_odd) }.
```

This is an identity of supports: `|supp R_N| = 23N/288 + O(1)`, whereas `‖R_N‖₁ = 25N/288 + O(1)` because each coefficient-2 root stands for the two original shell atoms `x` and `p = (4x − 1)/3`. Consequently, discharging the remaining outer roots from a supplied absorption of `[1, N]` is the classical strong-induction step on this set. Roots divisible by 3 have no odd predecessor at any lookback depth; only their forward orbits, or current certificates, can bring them into the absorbed set.

## Proof

(Main lane's written proof, [`side_lane_review_20261017_latest.md`](side_lane_review_20261017_latest.md) §2.) Every element of the support is a climber `x ≡ 3 (mod 4)`. Take an odd `x ∈ (N, 3N/2)`, `x ≡ 3 (mod 4)`.

- If `3 | x`, no odd Syracuse predecessor exists, so the climber remains (and it is `3 (mod 12)`, in `R_N`).
- If `x ≡ 2 (mod 3)`, the predecessor `(2x − 1)/3` is odd and below `N`, so the root is removed by one-step lookback (and `x ∉ supp R_N`).
- Otherwise `x ≡ 7 (mod 12)`. Its smallest odd predecessor is `p = (4x − 1)/3 > N`; all larger predecessors exceed `3N/2`, whereas a first iterate of a seed `≤ N` is below `3N/2`. So two-step lookback can only use `p`, and needs `x < 9N/8`.
- In that sliver, `p ≡ 2 (mod 3)` exactly when `x ≡ 31 (mod 36)`; then `q = (2p − 1)/3 = (8x − 5)/9 < N` and `S²(q) = x`. If `p ≡ 0 (mod 3)` it has no predecessor; if `p ≡ 1 (mod 3)` its smallest predecessor exceeds `N`. These are the surviving classes `x ≡ 7, 19 (mod 36)`.

The endpoint `9N/8` is a multiple of 9, never one of these `7 (mod 12)` roots. This exhausts the one- and two-step histories and gives the support of `R_N` exactly. ∎

## Certificates

[`check_support_recompute.py`](check_support_recompute.py) (written at the B09 migration, under 1 s, standard library). Checks the identity for every multiple of 8 through 4096 and at the six cutoffs of the side-lane receipt, that no support element is `2 (mod 3)`, that `|supp R_N| − 23N/288` stays in `[−3, 3]` (the largest deviation found is `11/9`), and reproduces the receipt rows (support, mass, roots divisible by 3) at `N = 96, 768, 6144, 9216, 49152, 98304`.

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B18-replay-revival migration; standard library) replays the unmodified legacy check `residual_vs_induction.py` in a temporary copy of the legacy layout built by `tools/legacy_replay.py`, requiring exit 0 and every file unchanged (about 10 s). It checks finite steps only; the status is unchanged.

## Remarks

- **Scope.** The finite-bit cylinder experiments that the side lane ran on this set, and the main lane's scoping of them, are [`cylinder-certificates-outer-residual`](../../attempts/cylinder-certificates-outer-residual/README.md). The identity does not exclude coalescence, longer common-tail bridges or annular block certificates; the halving identity [`halving-coalescence-return`](../halving-coalescence-return/README.md) and the transfer [`annular-complement-outer-descent`](../annular-complement-outer-descent/README.md) are such mechanisms.
- At the sampled cutoffs the roots divisible by 3 are about half the support (4 of 7 at `N = 96`, 256 of 490 at `N = 6144`, 4096 of 7850 at `N = 98304`).
- Novelty undetermined: two-step lookback in strong induction is classical; the content here is the exact identification with the profile `R_N`.

## History

- New node at the B09 migration (Claude, Opus 5.5); it has no legacy report of its own. The identity was found by the side lane (feed entry 2026-10-17 19:40, "R17's outer residual is exactly the strong-induction residual with two-step lookback", checked at six cutoffs by `reviews/side_lane/residual_vs_induction.py`), and the main lane wrote the proof for every allowed `N` in its review `experiments/residual_progress/side_lane_review_20261017_latest.md` (reviewed side-lane commit `9a0c28d`). Both lanes are listed as authors, so neither counts as an independent reviewer. The probe, the review and its receipt moved here byte-identical; three relative links in the review were pointed to the migrated nodes. Alias R17-b: the identity concerns the R17 profile.
