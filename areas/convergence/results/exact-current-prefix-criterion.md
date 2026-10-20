---
id: exact-current-prefix-criterion
kind: result
title: Exact currents at all cutoffs up to M are equivalent to convergence of the odd seeds up to (3M+1)/2
status: written
claim: >
  Odd-only clock, absorbing at 1; Π^R_N the right-aligned packets. For each integer M ≥ 8 the following are
  equivalent: (1) every positive odd seed r ≤ floor((3M+1)/2) reaches 1; (2) Π^R_N has a finite exact current
  for every integer 8 ≤ N ≤ M; (3) Π^R_N has a finite exact current for every integer 8 ≤ N ≤ M with
  N mod 8 ∈ {2, 5}. Hence Collatz is equivalent to exact finite currents at the cutoffs N ≥ 8 with
  N mod 8 ∈ {2, 5}. Scoped to exact currents: the argument does not give the sparse criterion for currents
  with nonpositive residual. It supplies no current.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [right-aligned-fixed-core-remainder, finite-current-certificate-identity]
evidence:
  - "No script of its own. The base seeds through 15 are checked by ../right-aligned-fixed-core-remainder/right_aligned_packets.py (a certificate of that node)"
aliases: [R6-b]
tags: [convergence, packet-currents, right-aligned, exact-currents, finite-prefix]
---

# Exact currents at all cutoffs up to M are equivalent to convergence of the odd seeds up to (3M+1)/2

## Statement

The packet definitions, source measure `ν_N`, fixed core and absorption convention are those of [`right-aligned-fixed-core-remainder`](right-aligned-fixed-core-remainder/README.md); odd-only clock, absorbing at 1.

**Theorem.** For each integer `M ≥ 8`, the following are equivalent:

1. Every positive odd seed `r ≤ floor((3M+1)/2)` reaches 1.
2. For every integer `8 ≤ N ≤ M`, `Π^R_N` has a finite exact current.
3. For every integer `8 ≤ N ≤ M` with `N mod 8 ∈ {2, 5}`, `Π^R_N` has a finite exact current.

The interval is an exact finite statement, not a claim that existence can be decided without convergence information. The implication from 3 can be vacuous at tiny `M`; the required finite seed interval there is part of the directly terminating base core below.

**Corollary.** Taking all `M`, Collatz is equivalent to the existence of exact finite currents only at integer cutoffs `N ≥ 8` with `N mod 8 ∈ {2, 5}`.

## Proof

From the legacy note, kept as written.

Let `e(r)` indicate nontermination. It is invariant under `S`, with `e(1) = 0`. Every finite signed divergence has zero pairing with `e`. The fixed core `{5, 7, 11, 13}` has zero pairing with `e`, so `⟨e, Π^R_N⟩ = ⟨e, ν_N⟩`.

**1 ⇒ 2.** All sources in `ν_N` lie below `floor((3M+1)/2)`, hence they and their packet endpoints terminate. Summing the finitely many packet pushes through their last absorption time gives an exact finite current.

**2 ⇒ 3** is immediate.

**3 ⇒ 1.** Suppose a nonterminating odd seed exists in the named interval and let `r` be the least nonterminating positive odd seed. The odd seeds through 15 terminate by direct finite computation, so `r ≥ 17`. Minimality gives two elementary restrictions:

- If `r ≡ 1 (mod 4)`, its first valuation is at least 2 and `S(r) < r`, a contradiction. Thus `r ≡ 3 (mod 4)`.
- If `r ≡ 2 (mod 3)`, the odd integer `x = (2r − 1)/3` is positive and smaller than `r`, and `S(x) = r`, another contradiction.

It follows that `r = 12m + 3` or `r = 12m + 7`. Set `N = ceil((2r − 1)/3)`. For the two residue cases this is `N = 8m + 2` or `N = 8m + 5`. Therefore `N mod 8 ∈ {2, 5}`, `8 ≤ N ≤ M`, and its upper cutoff `n_1(N)` is `r` or `r + 1`; the latter extra point is even. The second component cutoff `n_2(N)` is strictly smaller than `r`. All other odd source states therefore terminate. As `r` is not 2 modulo 3, its one remaining source coefficient is `−1`, yielding `⟨e, ν_N⟩ = −1`. An exact current for `Π^R_N` would instead make this pairing zero. This contradiction proves 1. ∎

## Remarks

- **Scope.** This thins the exact-certificate target to one quarter of the cutoffs. It does not provide any of those currents.
- **Exact currents only.** At the cutoff that first isolates a least exceptional seed, the packet's unknown component has coefficient `−1`. A finite exact current excludes that seed because the pairing must vanish; an everywhere nonpositive residual permits a negative pairing. So the same proof does **not** establish the sparse criterion for incomplete currents. This is the observation behind Lemma 3 of [`qualitative-current-criterion`](qualitative-current-criterion.md): for currents with nonpositive residual the maximum principle is load-bearing.
- No trajectory scan is needed beyond the fixed base seeds through 15. The argument does not claim that finite exact currents at a single large cutoff imply all smaller seeds terminate.
- Related: [`sparse-paired-exact-current-criterion`](sparse-paired-exact-current-criterion.md) (exact currents at sparse pairs). Novelty undetermined.

## History

- Migrated from `experiments/current_construction/recursive/exact_current_prefix.md` (written in the legacy R5–R7 round; filed under the R6 folder, alias `R6-b` here) at commit `be73a66`, by the B08 migration (Claude, Opus 5.5). Legacy status: "written elementary proof, scoped to exact finite signed currents".
- Main lane (ChatGPT, Codex), 2026-10-17. No review from another lane is on record.
