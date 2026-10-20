---
id: five-ray-complementary-profile-completion
kind: question
title: Certify every complementary outer root from absorption below N, at every interleaved five-ray cutoff
status: open
claim: >
  Odd-only 3x+1 map, absorbing at 1. For every cutoff N = a 2^b, a in (12, 14, 16, 18, 21), b >= 9, and using
  only a supplied exact current for U_N (the odd seeds <= N), construct finite exact certificates (absorption
  paths, finite signed currents, or capacity-checked annular blocks at M = N/64) for every root of the
  complementary profile R'_N of halving-coalescence-return. By five-ray-profile-completion-suffices this implies
  the Collatz convergence statement, and the convergence statement implies it, so it is a sharper form of the
  convergence problem, not a weakening.
created: 2026-10-17
tags: [convergence, outer-residual, induction, frontier, collatz-equivalent]
---

# Certify every complementary outer root from absorption below N, at every interleaved five-ray cutoff

## Question

At every cutoff of the interleaved five-ray sequence `12·2^b, 14·2^b, 16·2^b, 18·2^b, 21·2^b` (`b ≥ 9`), given a supplied exact current for `U_N`, certify every root `x = 2^a t − 1` (`t ≡ −3^a mod 4`) of the complementary profile `R'_N` of [`halving-coalescence-return`](../results/halving-coalescence-return/README.md), with its full coefficient (1 or 2). Allowed certificates: finite absorption paths, finite signed currents whose positive dependencies are already absorbed, or capacity-checked annular blocks `P − Q = (I − Push)J`, `0 ≤ P ≤ A_M⁺`, `0 ≤ Q ≤ A_M⁻`, with `Q(t) = 1` at the root's exit ([`annular-complement-outer-descent`](../results/annular-complement-outer-descent/README.md)); a proved decreasing parameter for a recursive rule also qualifies.

## Why it matters

By [`five-ray-profile-completion-suffices`](../results/five-ray-profile-completion-suffices/README.md), such a rule extends absorption from `U_N` to `U_(3N/2)` at every cutoff, and induction from the checked base `U_6144` proves that every positive integer reaches 1. Conversely, if every orbit reaches 1, the absorption paths are the certificates. It is the target of the residual-progress rounds after R24.

## Known progress

- The roots are the shell climbers outside `S([1,N]) ∪ S²([1,N])` ([`outer-residual-strong-induction-support`](../results/outer-residual-strong-induction-support/README.md)); the complementary profile has mass `25N/576 + O(log N)`, and on it `S^a(x) = 3·2^(d−1)·w + 1` with `w` the smaller partner's iterate, so knowing the partner does not certify `x` ([`halving-coalescence-return`](../results/halving-coalescence-return/README.md)).
- Annular blocks: the existing catalogue covers only `N/9216 + O(1)` roots; the delayed families give infinitely many shrinking branches with unbounded excursions ([`annular-complement-outer-descent`](../results/annular-complement-outer-descent/README.md)).
- Fixed-bit cylinder rules leave a positive linear remainder ([`cylinder-certificates-outer-residual`](../attempts/cylinder-certificates-outer-residual/README.md)).
- Published sufficient-set and inverse-count theorems do not supply height- and capacity-controlled witnesses ([`five-ray-profile-completion-suffices`](../results/five-ray-profile-completion-suffices/README.md)).
- R25–R39 attacked the complementary profile directly. Sibling and halving identities form an exact quotient with a terminating normal form, and every remaining R23 root is already canonical ([`elementary-bridge-quotient-normal-form`](../results/elementary-bridge-quotient-normal-form/README.md); whether the normalised quotient map terminates is [`normalised-quotient-termination`](normalised-quotient-termination.md)). Normalised run bridges cover the whole complementary parameter domain but return to cutoff-independent heights ([`complementary-run-bridges`](../results/complementary-run-bridges/README.md)); supplied history, absorbed fibres and inverse ancestry enlarge the certifiable targets ([`supplied-path-saturation-core`](../results/supplied-path-saturation-core/README.md), [`absorbed-fibre-uniform-counts`](../results/absorbed-fibre-uniform-counts/README.md), [`decreasing-inverse-ancestry`](../results/decreasing-inverse-ancestry/README.md)). The remaining comparisons reduce to tripling and doubling pairs ([`tripling-doubling-pair-decomposition`](../results/tripling-doubling-pair-decomposition/README.md)), with shrinking pair recursions on partial domains ([`shrinking-paired-return-recursion`](../results/shrinking-paired-return-recursion/README.md), [`mixed-shrinking-pair-rules`](../results/mixed-shrinking-pair-rules/README.md), [`missing-one-mod-8-pair-domain`](../results/missing-one-mod-8-pair-domain/README.md), [`coupled-even-pair-recursion`](../results/coupled-even-pair-recursion/README.md)) and an exact critical tripling domain whose universal supply is Collatz-equivalent ([`critical-tripling-domain-equivalence`](../results/critical-tripling-domain-equivalence/README.md), [`odd-h-pair-interface-compiler`](../results/odd-h-pair-interface-compiler/README.md)). Scope results: no finite-label height potential decreases on every return ([`bounded-runs-exclude-finite-label-potentials`](../results/bounded-runs-exclude-finite-label-potentials/README.md)); fixed prefix rules have exact symbolic rates that do not bound arbitrary bridges ([`prefix-rule-cylinder-rate-barrier`](../results/prefix-rule-cylinder-rate-barrier/README.md), [`merger-catalogue-scope`](../results/merger-catalogue-scope/README.md)).
- R40–R60 continued on the critical pair domain: [`critical-nine-elimination`](../results/critical-nine-elimination/README.md) leaves the single Collatz-equivalent premise [`universal-w5-tripling-currents`](universal-w5-tripling-currents.md), which [`critical-image-rank-composition`](../results/critical-image-rank-composition/README.md) and the strict-rank rules up to [`maximal-inverse-cycle-continuation`](../results/maximal-inverse-cycle-continuation/README.md) reduce without closing (Known progress there). The later legacy rounds R61–R94 (`experiments/residual_progress/`, not yet migrated) continued through dispatchers and history constructions; it stayed open.

## Suggested attacks

- The legacy §4 interface of [`five-ray-profile-completion-suffices`](../results/five-ray-profile-completion-suffices/README.md): partition the exits `t ≡ 5, 11 (mod 18)` by exact valuation cylinders and record, per cylinder, the first certified descent or merger word, its height and descent cutoff, every annular attachment and the capacity it consumes; keep failed cylinders and growing depths explicit, and prove termination through source-empty components.
- Any rule must use a property of `3x+1` that the `3x+61` controls lack ([`locally-collatz-like-control-barrier`](../results/locally-collatz-like-control-barrier/README.md)).
