---
id: qualitative-current-criterion
kind: result
title: Collatz convergence is equivalent to finite current certificates for the right-aligned packets at every cutoff
status: reviewed
claim: >
  Odd-only clock, absorbing at 1; Π^R_N is the right-aligned depth-one packet measure of
  right-aligned-fixed-core-remainder. The following are equivalent: (1) every positive integer reaches 1
  under the Collatz map; (2) for every integer N ≥ 8, sup_L H_L(Π^R_N) < ∞, the bound allowed to depend
  arbitrarily on N; (3) for every N ≥ 8 there is a finite signed current J_N with Π^R_N = (I − P)J_N;
  (4) for every N ≥ 8 there are finite signed J_N, ζ_N with Π^R_N = (I − P)J_N + ζ_N and ζ_N ≤ 0
  pointwise. No uniform cost bound and no inverse-basin theorem is used. This is a reformulation: it does
  not prove any of (1)–(4).
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [right-aligned-fixed-core-remainder, finite-current-certificate-identity]
evidence:
  - "../right-aligned-fixed-core-remainder/right_aligned_packets.py: checks the rational inequalities of Lemma 2 and that the odd seeds below 16 reach 1"
  - "../locally-collatz-like-control-barrier/reduction_audit.py, reduction_audit.json: the PR1 lane's checks of Lemma 2 (ratio maximum 0.96751 on 16 ≤ N ≤ 2·10^4), of the partition (6) with orbit indicators, and of the least-exception arithmetic for odd r ≤ 10^6 (see right-aligned-reduction-independent-checks)"
reviewed_by:
  - by: Claude PR1 lane (Opus)
    date: 2026-10-17
    link: locally-collatz-like-control-barrier/NOTE.md
    scope: "NOTE §§4 and 6 (ledger C1): re-derived Theorem 3 and found no gap (valuation-partition bijections, telescoping in 4 ⇒ 2, the limit (5), the maximizer argument); showed by Lemma 3 that the N^(3/2) maximum principle is load-bearing for statements 2 and 4. Model-assisted, not human peer review"
aliases: [R3]
tags: [convergence, packet-currents, right-aligned, equivalence, maximum-principle]
---

# Collatz convergence is equivalent to finite current certificates for the right-aligned packets at every cutoff

## Statement

Notation of [`right-aligned-fixed-core-remainder`](right-aligned-fixed-core-remainder/README.md) (cutoffs `n_0, n_1, n_2`, source measure `ν_N`, packets `Π^R_N`) and of [`finite-current-certificate-identity`](finite-current-certificate-identity.md) (odd-only clock, `P` kills mass at 1, `H_L`). For functions `f` on nonnegative integers put

```
(𝓛f)(N) = f(n_0) + f(n_1)/3 + f(n_2)/3.
```

**Lemma 2 (a strict comparison function).** For every integer `N ≥ 16`, `𝓛(N^(3/2)) < (505/512)·N^(3/2)`.

**Theorem 3 (equivalent qualitative targets).** The following are equivalent:

1. Every positive integer reaches 1 under Collatz.
2. For every integer `N ≥ 8`, `sup_(L≥0) H_L(Π^R_N) < ∞`. The bound may depend arbitrarily on `N`.
3. For every integer `N ≥ 8` there is a finite signed current `J_N` with `Π^R_N = (I − P)J_N`.
4. For every integer `N ≥ 8` there are finite signed measures `J_N, ζ_N` with `Π^R_N = (I − P)J_N + ζ_N` and `ζ_N ≤ 0` pointwise.

Neither a uniform cost bound nor an inverse-basin theorem is required.

## Proof

From Lemma 2 and Theorem 3 of [`papers/right-aligned-reduction`](../../../papers/right-aligned-reduction/README.md), kept as written.

**Lemma 2.** The three ratios `n_0/N`, `n_1/N`, `n_2/N` are at most `1/4`, `49/32` and `49/64` for `N ≥ 16`. Hence

```
𝓛(N^(3/2))/N^(3/2) ≤ 1/8 + 343/(384·√2) + 343/1536 < 1/8 + 245/384 + 343/1536 = 505/512 < 1,
```

using `1/√2 < 5/7`. ∎

**1 ⇒ 3.** A finite packet has finitely many sources; under Collatz all are absorbed by some finite time `M`. Then `J_N = Σ_(j<M) P^j Π^R_N` is finite and telescopes to `Π^R_N`.

**3 ⇒ 4.** Take `ζ_N = 0`.

**4 ⇒ 2.** For a finite current, `H_L((I − P)J) = ⟨1, J − P^L J⟩ = Σ_y J(y)·1[τ(y) ≤ L] ≤ ‖J⁺‖₁` ([`finite-current-certificate-identity`](finite-current-certificate-identity.md)). Since `h_L ≥ 0`, a nonpositive residual contributes at most zero. No bound uniform in `N` is needed.

**2 ⇒ 1.** Let `e(x) = 1[τ(x) = ∞]`, `e(1) = 0`, and

```
B(u) = Σ_(1 ≤ x ≤ u, x odd) e(x),     B_r(u) = Σ_(1 ≤ x ≤ u, x ≡ r mod 6) e(x).
```

`e` is `S`-invariant. Finite support and (2) of [`right-aligned-fixed-core-remainder`](right-aligned-fixed-core-remainder/README.md) give

```
lim_(L→∞) H_L(Π^R_N)/L = ⟨e, Π^R_N⟩ = ⟨e, P ν_N⟩ = ⟨e, ν_N⟩,                                  (5)
```

because `e` vanishes on the fixed core `{5, 7, 11, 13}`. Statement 2 makes (5) nonpositive. Partitioning sources by first valuation gives the exact exceptional-count identity

```
B(N) = B(n_0) + B_5(n_1) + B_1(n_2) = 𝓛B(N) + ⟨e, ν_N⟩/3 ≤ 𝓛B(N).                             (6)
```

Valuation 1 maps `4j+3` bijectively to `6j+5`; valuation 2 maps `8j+1 > 1` to `6j+1 ≥ 7`; valuation at least 3 has sources `4z+1` with `z` odd and `S(4z+1) = S(z)`. The small cases 1 and 5 both have `e = 0`, so (6) has no additive constant.

The odd seeds `1, 3, …, 15` all terminate, so `B(N) = 0` for `N < 16`. Also `B(N) ≤ N`, so `B(N)/N^(3/2) → 0`. If `B` were nonzero, this ratio would attain a positive global maximum `M` at some integer `N ≥ 16`. Using (6) and Lemma 2 at that maximizer,

```
B(N) ≤ 𝓛B(N) ≤ M·𝓛(N^(3/2)) < M·N^(3/2) = B(N),
```

a contradiction. So all odd seeds terminate, and removing initial powers of two gives statement 1. ∎

**A second check for exact currents** (the paper's paragraph, kept). If `r` is the least nonterminating odd seed, take `N = ceil((2r−1)/3)`. Then `n_1 ∈ {r, r+1}` and `n_2 < r`, so `⟨e, ν_N⟩ = 3·1[r ≡ 2 mod 3] − 1 ∈ {−1, 2}`. The core has zero `e`-pairing, and every finite divergence has zero `e`-pairing by invariance, so an exact current is impossible. This short proof uses exact currents; the maximum principle is what also permits nonpositive residuals.

## Remarks

- **The maximum principle is load-bearing (PR1 lane, Lemma 3; written proof).** Let `r` be the least exceptional odd seed of `T_d(x) = (3x+d)/2^(v₂(3x+d))` with `(2r−d)/3 ≥ 1`. Then `r ≢ 2d (mod 3)`: otherwise `x = (2r−d)/3` is an odd integer with `T_d(x) = r` and `1 ≤ x < r`, and `x` is exceptional, contradicting minimality. At `d = 1` a least counterexample is never `2 mod 3`, so the "second check" above always evaluates to `−1`. That contradicts an exact current (pairing 0) but **not** bounded-above work or a nonpositive residual (pairing `≤ 0`). The `N^(3/2)` maximum principle is therefore necessary for statements 2 and 4, not redundant (legacy `NOTE.md` §4, in [`locally-collatz-like-control-barrier`](locally-collatz-like-control-barrier/README.md)).
- **What it does and does not do.** The equivalence does not reduce the logical strength of the conjecture, and no universal constructor or termination proof is established. Supplying the certificates is the open question [`packet-current-supply`](../questions/packet-current-supply.md). The legacy programme later restricted the cutoffs to five dyadic rays ([`five-ray-current-criterion`](five-ray-current-criterion/README.md), legacy R5).
- **Controls.** On the maps `T_d` where the analogous conjecture is false, the criterion fails at some cutoff, as the logic requires ([`locally-collatz-like-control-barrier`](locally-collatz-like-control-barrier/README.md)); the map `T_61` satisfies statement 4 at every `8 ≤ N ≤ 212` and fails it at `N = 213`. The class-by-class form is [`class-wise-obligation-equivalence`](class-wise-obligation-equivalence.md).
- **Sign.** Statement 2 is boundedness above for each cutoff, not a universal zero bound: `H_39(Π^R_32) = 57` ([`dyadic-cutoff-core-remainder`](dyadic-cutoff-core-remainder.md)).
- Novelty undetermined.

## History

- Migrated from the legacy ledger entry R3 (`archive/docs/RESULTS.md`, legacy path) and Lemma 2 and Theorem 3 of `papers/right_aligned_reduction/right_aligned_reduction.tex`, now [`papers/right-aligned-reduction/right-aligned-reduction.tex`](../../../papers/right-aligned-reduction/right-aligned-reduction.tex), at commit `be73a66`, by the B07 migration (Claude, Opus 5.5). Legacy status: "written equivalence; its universal hypothesis remains open".
- Main lane (ChatGPT, Codex), 2026-10-17. Audited by the PR1 lane the same day (ledger C1), which added Lemma 3.
