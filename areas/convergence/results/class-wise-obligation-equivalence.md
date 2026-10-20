---
id: class-wise-obligation-equivalence
kind: result
title: The five-ray packet obligation splits class by class into "no nontrivial cycles" and "no divergent orbits"
status: reviewed
claim: >
  Odd-only 3x+1 map S, absorbing at 1. Let K be a set of odd positive integers with x ∈ K ⇔ S(x) ∈ K for
  x > 1, 1 ∉ K, and K ∩ [1, 12096) = ∅. Then K = ∅ ⇔ ⟨1_K, Π_M⟩ ≤ 0 for every M on the legacy five-ray grid
  G_5 = {a·2^b : a ∈ {12, 14, 16, 18, 21}, b ≥ 3} ⇔ ⟨1_K, A_N⟩ ≤ 0 for every 64-fold increment A_N on the
  legacy 30 sequences N = a·2^r·64^k. Rests on the five-ray maximum principle (five-ray-current-criterion,
  R5) and the annular recursion (disjoint-annular-recursion, R6). The obligation is thus equivalent, basin by basin, to the absence of
  nontrivial cycles and of divergent orbits, each at full strength; this gives no proof of either.
authors:
  - Claude PR1 lane (Opus)
created: 2026-10-17
depends_on: [qualitative-current-criterion, five-ray-current-criterion, disjoint-annular-recursion]
evidence:
  - "locally-collatz-like-control-barrier/NOTE.md §12.2, HANDOFF_FOR_MAIN.md §6: the written proof"
  - "locally-collatz-like-control-barrier/attempt_probes.py, attempt_probes.json (classwise_controls): a certificate of that node (exits 0 at its new path and rewrites its receipt byte for byte)"
reviewed_by:
  - by: ChatGPT main lane (Codex)
    date: 2026-10-17
    link: locally-collatz-like-control-barrier/PR1_REVIEW.md
    scope: "§1 and §4: 'The stated equivalence for an invariant set avoiding the verified finite base follows from the annular telescoping identity and the five-ray maximum principle'; 'a valid reduction'. It does not provide the missing universal construction, and equivalence to the original problem is not itself a theorem that the formulation has no use"
aliases: [PR1-C5]
tags: [convergence, packet-currents, equivalence, five-rays]
---

# The five-ray packet obligation splits class by class into "no nontrivial cycles" and "no divergent orbits"

## Statement

Odd-only clock, absorbing at 1, packets `Π_M = Π^R_M` of [`right-aligned-fixed-core-remainder`](right-aligned-fixed-core-remainder/README.md). Two main-lane results enter:

- **Five rays ([`five-ray-current-criterion`](five-ray-current-criterion/README.md), legacy R5).** Statement 4 of [`qualitative-current-criterion`](qualitative-current-criterion.md) may be restricted to the grid `G_5 = {a·2^b : a ∈ {12, 14, 16, 18, 21}, b ≥ 3}`; its proof is a maximum principle on the grid that uses, of the exceptional indicator, only the counting identity, monotonicity of the count, and vanishing below 96.
- **Annular recursion ([`disjoint-annular-recursion`](disjoint-annular-recursion/README.md), legacy R6).** For `8 | N`, `Π_(64N) = Π_N + A_N`; the grid splits into 30 sequences `N = a·2^(r+6k)`, `r = 3, …, 8`, with initial cutoffs at most 5376 and packet endpoints below 12096.

**Corollary (PR1 lane).** Let `K` be a set of odd positive integers with `x ∈ K ⟺ S(x) ∈ K` for `x > 1`, `1 ∉ K`, and `K ∩ [1, 12096) = ∅`. The following are equivalent:

- (a) `K = ∅`;
- (b) `⟨1_K, Π_M⟩ ≤ 0` for every `M ∈ G_5`;
- (c) `⟨1_K, A_N⟩ ≤ 0` for every increment on the 30 sequences `N = a·2^r·64^k`.

## Proof

From legacy `NOTE.md` §12.2 (folder [`locally-collatz-like-control-barrier`](locally-collatz-like-control-barrier/README.md)), kept as written.

- **(a) ⇒ (c)** is trivial.
- **(c) ⇒ (b).** Along a sequence, `Π_(N_k) = Π_(N_0) + Σ_(i<k) A_(N_i)`. The pairing `⟨1_K, Π_(N_0)⟩ = ⟨1_K, ν_(N_0)⟩` vanishes, because `ν_(N_0)` lives below `3·5376/2 < 12096`; here `1_K` is invariant and vanishes on the core and at 1. Every grid point lies on one of the 30 sequences.
- **(b) ⇒ (a).** The five-ray maximum principle uses only three facts about the exceptional indicator: the counting identity (valid for any invariant indicator vanishing at 1 and on the core), monotonicity of the count, and vanishing below 96. All three hold for `1_K`. ∎

If `3x+1` has a nontrivial cycle, the basin of that cycle is such a `K`, by the repository's finite base checks. If it has divergent orbits, the union of their basins is such a `K`. So the packet obligation is equivalent, class by class, to the two classical problems.

**Finite check on controls.** For `T_−1`, `T_5` and `T_13`, each of the 14 nontrivial cycle basins separately has a positive pairing at some cutoff, usually close to the basin's least seed (`attempt_probes.json`, `classwise_controls`). This checks the class-wise picture on controls, not on `3x+1`.

## Remarks

- **What it does not say.** The corollary gives no separate leverage on either classical problem, and it does not supply the missing certificates ([`packet-current-supply`](../questions/packet-current-supply.md)). The main lane's review notes that equivalence to the original problem is not itself a theorem that the formulation is useless; the PR1 lane's stronger reading ("no separate leverage", "no room") is an assessment of an approach, recorded in [`annular-bottom-cancellation-attempt`](../attempts/annular-bottom-cancellation-attempt.md).
- **Chain strength.** The node rests on [`five-ray-current-criterion`](five-ray-current-criterion/README.md) (reviewed by the PR1 lane) and [`disjoint-annular-recursion`](disjoint-annular-recursion/README.md) (written; cross-checked on finite ranges in [`right-aligned-reduction-independent-checks`](right-aligned-reduction-independent-checks.md)).
- Novelty undetermined.

## History

- Migrated from the legacy ledger entry C5 (first half; `archive/docs/RESULTS.md`, legacy path) and `experiments/packet_currents/negative_controls/NOTE.md` §12.2, at commit `be73a66`, by the B07 migration (Claude, Opus 5.5). Alias `PR1-C5`; the attempt half of C5 is [`annular-bottom-cancellation-attempt`](../attempts/annular-bottom-cancellation-attempt.md) (`PR1-C5-b`).
- PR1 lane (Claude, Opus), 2026-10-17. Main-lane review in `PR1_REVIEW.md` the same day.
- 2026-10-20 (B08 migration): the R5 and R6 nodes now exist; added them to `depends_on`, linked them in the Statement, and replaced the remark "Conditional on unmigrated nodes" by a chain-strength remark. No change to the claim's content.
