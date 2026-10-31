---
id: five-ray-current-criterion
kind: result
title: Finite current certificates on five dyadic rays of cutoffs are equivalent to Collatz convergence
status: reviewed
claim: >
  Odd-only clock, absorbing at 1; Π_M is the right-aligned packet measure Π^R_M of
  right-aligned-fixed-core-remainder. Let G_5 = {a·2^b : a ∈ {12, 14, 16, 18, 21}, b ≥ 3}. Each of the following
  is equivalent to the Collatz conjecture (every positive integer reaches 1): (i) for every M ∈ G_5,
  sup_L H_L(Π_M) < ∞; (ii) for every M ∈ G_5 there is a finite exact current for Π_M; (iii) for every M ∈ G_5
  there is a finite current for Π_M whose residual is everywhere nonpositive. No bound on certificate size,
  cost or running time uniform in M is assumed. Moreover G_5 splits into 30 sequences N_k = a·2^r·64^k
  (r = 3, …, 8) whose 30 initial cutoffs are at most 5376, and exact finite currents exist for all 30 initial
  packets, because every odd seed below 12096 reaches 1 within 98 odd steps (finite check). This is a
  reformulation: no current is supplied at the infinitely many remaining cutoffs.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [qualitative-current-criterion, right-aligned-fixed-core-remainder, finite-current-certificate-identity]
certificates: [check_sparse_criteria.py, check_five_rays_independent.py]
evidence:
  - "sparse_criteria_audit.json: receipt of check_sparse_criteria.py (rewritten byte for byte by each run)"
  - "sparse_ray_independent_audit.md, check_five_rays_independent.py: a re-check of the maximum-principle argument and its arithmetic by another agent of the main lane (legacy obstructions/ folder); not an independent review"
  - "../locally-collatz-like-control-barrier/main_claims_audit.py, main_claims_audit.json: the PR1 lane's independent check of the cutoffs, targets, exponents and constant for 3 ≤ b ≤ 400 (a certificate of that node)"
reviewed_by:
  - by: Claude PR1 lane (Opus)
    date: 2026-10-17
    link: ../locally-collatz-like-control-barrier/NOTE.md
    scope: "NOTE §10 (ledger C1): 'I re-read the written maximum-principle argument on the grid and found no gap'; independent code checks the exact cutoffs (M/4 − 1, 3M/2, 3M/4), the upper targets, the comparison exponents, that every target with exponent below 3 lies below 96, and λ_5 < 89/90, for all five rays and 3 ≤ b ≤ 400. The corollary on the 30 initial cutoffs was not part of that audit. Model-assisted, not human peer review"
aliases: [R5]
tags: [convergence, packet-currents, right-aligned, five-rays, maximum-principle, equivalence]
---

# Finite current certificates on five dyadic rays of cutoffs are equivalent to Collatz convergence

## Statement

Odd-only Syracuse map `S`, absorbing at 1. Let `e(x) = 1` precisely when the positive odd state `x` never reaches 1 (`e(1) = 0`), and `B(u) = Σ_(odd x ≤ u) e(x)`. For every integer `N ≥ 8` keep the two-component source `ν_N` and the right-aligned depth-one packet measure `Π_N = Π^R_N` of [`right-aligned-fixed-core-remainder`](../right-aligned-fixed-core-remainder/README.md); its remainder lives on the terminating core `{5, 7, 11, 13}`. With

```
n_0 = floor((N−1)/4),   n_1 = floor((3N+1)/2),   n_2 = floor((3N+1)/4),
(𝓛f)(N) = f(n_0) + f(n_1)/3 + f(n_2)/3,
d_N := ⟨e, Π_N⟩ = ⟨e, ν_N⟩ = 3·(B(N) − (𝓛B)(N)).                                   (1)
```

These are exact identities, with no missing boundary constant ([`qualitative-current-criterion`](../qualitative-current-criterion.md), (5)–(6)). `Π_N` is a finite signed integer measure, so `d_N` is an integer.

Let `(a_0, a_1, a_2, a_3, a_4) = (12, 14, 16, 18, 21)` and `G_5 = {a_i·2^b : 0 ≤ i ≤ 4, b ≥ 3}`.

**Theorem (five rays).** Each of the following is equivalent to Collatz:

- for every `M ∈ G_5`, the packet work `H_L(Π_M)` is bounded above over all integer horizons `L ≥ 0`;
- for every `M ∈ G_5`, there is a finite exact current for `Π_M`;
- for every `M ∈ G_5`, there is a finite current whose residual is everywhere nonpositive.

There is no uniform bound on certificate size, cost or running time. There are five selected cutoffs in each interval `[12·2^b, 24·2^b)`.

**Corollary (thirty initial cutoffs).** Writing `b = r + 6k` with `r = 3, …, 8`, the five rays split into exactly 30 sequences `N_k = a_i·2^r·64^k`. Their initial cutoffs are distinct, the largest being `21·2^8 = 5376`, and exact finite currents exist for all 30 initial packets.

## Proof

It suffices to assume `d_M ≤ 0` for every selected cutoff; each of the three hypotheses implies this as in [`qualitative-current-criterion`](../qualitative-current-criterion.md) (4 ⇒ 2 and the limit (5) there). The key arithmetic inequalities are

```
 i                        0     1     2      3      4
 a_i                     12    14    16     18     21
 3a_i/2                  18    21    24     27   63/2
 chosen upper target     18    21  2·12   2·14   2·16                                 (2)
```

Write `i + 3 = 5s + j` with `0 ≤ j ≤ 4`. For `M = a_i·2^b`, the upper target in (2) is `M' = a_j·2^(b+s) ≥ 3M/2`; its half is at least `3M/4`. Every selected cutoff is divisible by 8, so the source recurrence has `n_0 = M/4 − 1`, `n_1 = 3M/2`, `n_2 = 3M/4` exactly.

Define the comparison value on the selected grid by `F(a_i·2^b) = 2^((5b+i)/3)`. Representations on this grid are unique. Use the same formula for the finitely many lower exponents required below. Since `5s + j − i = 3`, the three upper targets have comparison values

```
F(M/4) = 2^(−10/3)·F(M),   F(M') = 2·F(M),   F(M'/2) = 2^(1−5/3)·F(M).                (3)
```

Any of these target points with exponent below 3 is strictly below 96: `M/4` at such exponents is at most 84, and `M'/2` at exponent 2 is either 72 or 84. Every odd seed below 96 has been verified to terminate, so its `B` value is zero and causes no boundary error.

`F(M)` is bounded above and below by fixed positive multiples of `M^(5/3)` on the five-ray grid, so `B(M)/F(M) → 0` as `M → ∞` through the grid. If any exceptional seed exists, the ratio has a positive global maximum `C` at some selected cutoff `M` (the grid is unbounded and eventually includes any exceptional seed in its count). For target points in the grid use `B ≤ C·F`; at lower target points use `B = 0 ≤ C·F`. Equations (1)–(3) and monotonicity give

```
C·F(M) = B(M) ≤ B(M/4 − 1) + B(3M/2)/3 + B(3M/4)/3
              ≤ C·[F(M/4) + F(M')/3 + F(M'/2)/3]
              = C·F(M)·[2^(−10/3) + (2/3)(1 + 2^(−5/3))].
```

But `2^10 = 1024 > 1000 = 10^3` and `2^5 = 32 > 27 = 3^3`, so the bracket is

```
λ_5 = 2^(−10/3) + (2/3)(1 + 2^(−5/3)) < 1/10 + (2/3)(1 + 1/3) = 89/90 < 1.
```

This contradicts positivity of `C·F(M)`. Conversely, Collatz gives finite absorption of every packet and hence an exact finite current, as in [`qualitative-current-criterion`](../qualitative-current-criterion.md) (1 ⇒ 3). ∎

The maximum is taken **only on the grid**, so the proof needs neither a subsolution inequality at non-grid cutoffs nor rounding of a non-grid maximizer (legacy `sparse_ray_independent_audit.md`).

**Proof of the corollary.** Every packet endpoint at an initial cutoff is below 12096: an odd source is at most `3N/2 − 1`, so its one-step endpoint is at most `(3(3N/2 − 1) + 1)/2 = 9N/4 − 1 ≤ 12095`. The companion script verifies convergence of every odd seed below 12096 as part of its larger finite base check: there are 6048 such seeds, all absorbed within 98 odd-only steps. Therefore exact currents exist for all 30 initial packets by finite absorption: one may take `J_N = Σ_(j=0)^(97) P^j Π_N`. This establishes existence for these initial cutoffs. **The thirty full current tables are not stored.** ∎

## Certificates

- [`check_sparse_criteria.py`](check_sparse_criteria.py) (main lane, about 8 s, standard library; checks by `assert`, so run it without `-O`). It rewrites [`sparse_criteria_audit.json`](sparse_criteria_audit.json) byte for byte. For this node it checks the five-ray transitions and the strict `89/90` comparison, the finite base (all 32768 odd seeds below 65536, by exact iteration with cycle detection and a 10000-step cap; largest hitting time 125, at 52527), and the 30 initial cutoffs with their endpoint bound 12096 (6048 seeds, largest hitting time 98). The same run checks the constants of [`mesh-maximum-principle-alternative-grids`](../mesh-maximum-principle-alternative-grids.md) and [`sparse-paired-exact-current-criterion`](../sparse-paired-exact-current-criterion/README.md). The receipt records `universal_current_existence_proved: false`.
- [`check_five_rays_independent.py`](check_five_rays_independent.py) (main lane, under 1 s; `assert`-based, run without `-O`; prints its result, writes no file). A separate implementation of the finite base below 96 (largest hitting time 42), the five transitions, the low-target cases and the exact integer bounds.

## Remarks

- **What it does and does not do.** The theorem reduces the family of required cutoffs from every `N ≥ 8` to five rays; it supplies no certificate on any infinite ray. The open target is [`five-ray-annular-current-supply`](../../questions/five-ray-annular-current-supply.md); along each of the 30 sequences the increments are the six-band annuli of [`disjoint-annular-recursion`](../disjoint-annular-recursion/README.md).
- **Alternatives.** The general mesh lemma, the earlier 21-ray and 30-ray grids and the subunit-defect reformulations are in [`mesh-maximum-principle-alternative-grids`](../mesh-maximum-principle-alternative-grids.md); a separate criterion for exact currents on arbitrarily sparse arithmetic pairs is [`sparse-paired-exact-current-criterion`](../sparse-paired-exact-current-criterion/README.md). No minimality of five rays is claimed.
- **The maximum principle is load-bearing.** The least-exception argument alone only gives pairing `−1`, which contradicts exact currents but not nonpositive residuals; see Lemma 3 in [`qualitative-current-criterion`](../qualitative-current-criterion.md).
- **Controls.** Restricted to the 39 five-ray cutoffs `≤ 20000`, the analogous criterion still fails on the false analogues `d = −1` (24 grid failures, first at 96) and `d = 61` (23 failures, first at 224) ([`locally-collatz-like-control-barrier`](../locally-collatz-like-control-barrier/README.md)), as the logic requires. This is a consistency observation only: the five-ray inclusions use `d = 1` offsets. By [`class-wise-obligation-equivalence`](../class-wise-obligation-equivalence.md) the five-ray obligation is equivalent, class by class, to the absence of nontrivial cycles and of divergent orbits.
- **Reviews.** The legacy note also says the five-ray argument "was independently checked by the parent research agent"; that check, and `sparse_ray_independent_audit.md`, are by agents of the same (main) lane and are kept as evidence, not as a review. The independent verdict is the PR1 lane's (`reviewed_by`).
- Novelty undetermined.

## History

- Migrated from `experiments/current_construction/frontier/sparse_current_criteria.md` §§1–2 and §8 (legacy ID R5) at commit `be73a66`, by the B08 migration (Claude, Opus 5.5). Its §§3–6 became [`mesh-maximum-principle-alternative-grids`](../mesh-maximum-principle-alternative-grids.md) and §7 became [`sparse-paired-exact-current-criterion`](../sparse-paired-exact-current-criterion/README.md). `sparse_ray_independent_audit.md` and `check_five_rays_independent.py` moved here from `experiments/current_construction/obstructions/`. The legacy ledger entry is R5 in `archive/docs/RESULTS.md` (legacy path), status "written equivalence, independently model-audited, with exact finite base checks"; the main proof note is Theorem 4 of [`papers/right-aligned-reduction`](../../../../papers/right-aligned-reduction/README.md).
- Main lane (ChatGPT, Codex), 2026-10-17, commit `8d62dcc`. Re-read and cross-checked by the PR1 lane the same day (ledger C1).
