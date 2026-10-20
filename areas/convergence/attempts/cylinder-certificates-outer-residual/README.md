---
id: cylinder-certificates-outer-residual
kind: attempt
title: Fixed-bit 2-adic cylinder certificates (descent, merger, halving) cannot complete the outer residual
status: written
claim: >
  Tried (side lane): certify the remaining outer roots of R_N (odd-only 3x+1, absorbing at 1; supplied
  absorption of [1, N]) by exact valuation cylinders of x mod 2^m: a determined prefix with
  3^(j+1) < 2^(A+1) (descent below N for large N), optionally merger with S([1,N]) through an odd valuation
  >= 3, or halving coalescence. Verdict: each accepted cylinder is a valid certificate for all sufficiently
  large N, but for every fixed bit depth m the class x = -1 mod 2^m is never accepted, so the undecided
  fraction is at least 2^-(m-2) and a positive linear remainder (23/288) d(m) N + O_m(1) of roots stays
  uncertified (proved in the main lane's review). Exact finite counts give undecided fractions 24.8%, 7.04%,
  1.06%, 0.214%, 0.0484% at 16, 32, 64, 96, 128 bits (descent only; about 0.79 times that with one-step
  merger). The fitted decay of about 0.953 per bit, the extrapolation of about N^0.93 roots with log2 N bits,
  and the random-model argument that merge-type certificates change only constants are heuristic, not
  theorems.
authors:
  - Claude side lane (Opus)
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [outer-residual-strong-induction-support, retained-graph-complement-constructor]
evidence:
  - "residual_cylinder_core.py, residual_cylinder_core.json: side-lane probe (2026-10-17): exact dynamic program over valuation cylinders for the descent rule, and with --merge the one-step merger rule; brute-force cross-check for m <= 14; actual-root descent counts at N = 6144 and 98304 (slowest 48 and 81 steps). Fails at its new path: it imports affine_controls from experiments/packet_currents/negative_controls/ by repository-relative path (now ../../results/locally-collatz-like-control-barrier/). Passed at be73a66 as reviews/side_lane/residual_cylinder_core.py (archive/legacy-checker-run-be73a66.md, exit 0)"
  - "excursion_merge_probe.py, excursion_merge_probe.json: side-lane probe for the side lane's Q6 (2026-10-17): the density of F_N, the union of the orbits of the odd seeds <= N, in height bands [HN, 2HN), and for every root of R_N at N = 49152 the first meeting with F_N against the first descent below N. Finite data. Fails at its new path: it imports affine_controls from experiments/packet_currents/negative_controls/ by repository-relative path (now ../../results/locally-collatz-like-control-barrier/), and it imports residual_vs_induction from its own folder (now ../../results/outer-residual-strong-induction-support/). Passed at be73a66 as reviews/side_lane/excursion_merge_probe.py (archive/legacy-checker-run-be73a66.md, exit 0)"
  - "../../results/halving-coalescence-return/coalescence_check.py: the side-lane dynamic program with the halving certificate added (evidence of that node)"
  - "../../results/outer-residual-strong-induction-support/side_lane_review_20261017_latest.md, .json: the main lane's review, which reproduced both probes exactly (30 s cap), cross-checked both dynamic programs against direct enumeration for every 2 <= m <= 14, proved the fixed-bit lower bound and relabelled the fitted rate as a finite 64-to-128-bit fit"
tags: [convergence, outer-residual, cylinders, stopping-time, heuristic, side-lane]
---

# Fixed-bit 2-adic cylinder certificates (descent, merger, halving) cannot complete the outer residual

## Idea

The remaining outer roots `R_N` of [`retained-graph-complement-constructor`](../../results/retained-graph-complement-constructor/README.md) are exactly the shell climbers not reached from `[1, N]` in one or two steps ([`outer-residual-strong-induction-support`](../../results/outer-residual-strong-induction-support/README.md)). Given absorption of `[1, N]`, certify them by 2-adic arithmetic alone, in the style of Terras's stopping-time cylinders ([`terras-1976-stopping-time`](../../../../sources/terras-1976-stopping-time.md)): the first `j` valuations of `x` are fixed by `x mod 2^(A_j + 1)`; if a determined prefix satisfies `3^(j+1) < 2^(A+1)` (equivalently `3^j·(3/2) < 2^A`), every root in that residue class drops below `N` once `N` exceeds a class constant. Two additions: **merger** (an odd valuation `a ≥ 3` with `3^j ≤ 2^A` reaches `y ≡ 2 (mod 3)`, `y < 3N/2`, whose valuation-one predecessor `(2y − 1)/3 < N` is absorbed) and **halving** (the selected climbers of [`halving-coalescence-return`](../../results/halving-coalescence-return/README.md), applied at any orbit state `y ≤ 2N`). The residue classes defining `R_N` are independent of these binary digits (Chinese remainder theorem), so the counts transfer.

## What happened

**Exact finite counts** (side lane, feed 2026-10-17 19:37–19:46; reproduced by the main lane, which also checked both dynamic programs against direct enumeration for every `2 ≤ m ≤ 14`). Undecided fraction of the roots (conditional on `x ≡ 3 mod 4`) using `m` bits:

| Bits `m` | 16 | 32 | 64 | 96 | 128 |
|---:|---:|---:|---:|---:|---:|
| Descent only | 24.76196% | 7.04307% | 1.05513% | 0.21408% | 0.04842% |
| Descent or one-step merger | 21.16699% | 5.75875% | 0.84344% | 0.16831% | 0.03808% |

Adding halving removes about a further 28% at each depth (feed 19:46, corrected at 20:22 with the partial-closing rule of [`prefix-rule-cylinder-rate-barrier`](../../results/prefix-rule-cylinder-rate-barrier/README.md), R28). Actual roots descend quickly in the median (4 steps at `N = 6144` and `98304`), the slowest in 48 and 81 steps.

**High merging (Q6, `excursion_merge_probe.py`).** At `N = 49152`, `F_N` has 38,912 states up to about `821N`; its density among odd numbers in `[HN, 2HN)` is about `0.3/H²` for `H ≤ 2^6`. Of the 3,925 roots, 30% meet `F_N` strictly before descending; the slowest, 60975, meets it only on its descent at step 96.

**Heuristics (labelled as such by both lanes).** The side lane fitted a decay of about 0.953 per bit between 64 and 128 bits and extrapolated about `N^0.93` uncertified roots with `log₂N` bits; it then argued, in a 2-adic random model with a Cramér-type large-deviation constant `ρ = min_θ 3^θ/(2^(1+θ) − 1) ≈ 0.9466` per odd step, that every certificate firing only within a fixed multiple of `N` (descent, merger with `S([1,N])`, halving below `2N`, annular blocks, absorbed-seed excursions of density about `c/H²`) changes constants but not that rate (feed 19:48, 19:49, 19:59; the 19:59 claim that all merge-type certificates share one `c/H²` law was withdrawn at 20:22, since the R27 fibres of [`absorbed-fibre-uniform-counts`](../../results/absorbed-fibre-uniform-counts/README.md) have density about `1/(2H)`).

## Why it fails

**Proved (main lane's review §4).** For every fixed `m ≥ 2` the class `x ≡ −1 (mod 2^m)` has all its determined valuations equal to 1 and is rejected by both rules; conditional on `x ≡ 3 (mod 4)` it has measure `2^(−(m−2))`. So `d_merge(m) ≥ 2^(−(m−2)) > 0`, and for fixed `m` ordinary progression counts give `#{undecided roots} = (23/288)·d(m)·N + O_m(1)`: any fixed-bit prefix procedure of this kind leaves a positive linear remainder. This does not cover theorems that use a fixed residue modulus together with unbounded orbit comparisons.

**Not proved.** Turning the `N^0.93` extrapolation into a theorem needs (1) an asymptotic or uniform bound for `d(m)`, which two finite bit ranges do not determine; (2) control of residue counts when the modulus grows with `N` (the fixed-modulus error can be of order `2^m`, i.e. order `N`); (3) uniform control of the affine constants and cutoff thresholds over the growing family of accepted prefixes. The random-model rate argument is a heuristic.

## What survives

- The exact dynamic programs are sound measurements of the tested prefix rules, and each accepted cylinder is a valid conditional certificate for all sufficiently large `N` (main lane's review §3).
- The diagnosis: a rule that closes every complementary root needs a certificate that can fire while the orbit is arbitrarily high relative to `N`, or a non-merge argument that the orbit comes down (heuristic guidance). The interleaved-ray induction that would use such a rule is [`five-ray-profile-completion-suffices`](../../results/five-ray-profile-completion-suffices/README.md); its open target is [`five-ray-complementary-profile-completion`](../../questions/five-ray-complementary-profile-completion.md).
- The merger tests of this attempt are narrower than arbitrary common-tail bridges to supplied paths or signed annular blocks; their undecided fraction does not exclude those mechanisms.

## History

- New node at the B09 migration (Claude, Opus 5.5), from the side-lane feed entries of 2026-10-17 19:37, 19:42, 19:46, 19:48, 19:49, 19:59 and 20:22 ([`archive/side-lane/FEED.md`](../../../../archive/side-lane/FEED.md); legacy path `archive/side_lane/FEED.md`) and the main lane's review `experiments/residual_progress/side_lane_review_20261017_latest.md` §§3–4 (now in [`outer-residual-strong-induction-support`](../../results/outer-residual-strong-induction-support/README.md)). The probes `reviews/side_lane/residual_cylinder_core.*` and `excursion_merge_probe.*` moved here byte-identical. The side lane (Claude, Opus) ran the experiments; the main lane (ChatGPT, Codex) proved the fixed-bit bound and scoped the extrapolation, so both are authors.
