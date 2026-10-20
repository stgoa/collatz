---
id: exact-current-minimality
kind: result
title: An exact current is dominated pointwise by every one-sided certificate, but cheapest one-sided certificates need not be unique
status: reviewed
claim: >
  Odd-only T_d maps absorbing at A_d (d = 1: Syracuse, absorbing at 1). Let μ be a finite signed measure with
  a finite exact current J_0, (I − P_A)J_0 = μ. If (J, ζ) is finite with μ = (I − P_A)J + ζ, ζ ≤ 0, and
  supp(J − J_0) contains no cycle of T_d outside A_d, then J ≥ J_0 pointwise, so ‖J⁺‖₁ ≥ ‖J_0⁺‖₁, and J_0 is
  the unique exact current in that comparison class. When every atom of μ terminates, J_0 = Σ_j P^j μ.
  The lemma does not make one-sided certificates unique: μ = δ_21 − δ_3 has the exact current
  δ_21 − δ_3 − δ_5 and also J = δ_21 − δ_3, ζ = −δ_5, both of minimum positive cost 1; and the actual annulus
  A_768 has 56 distinct one-sided certificates J_0 + c·δ_5, 0 ≤ c ≤ 55, all of minimum positive cost 53,758.
  Finite check: the snapshot's stored currents at N = 4096 (2,736 rows) and N = 262144 (132,998 rows) equal
  Σ_j P^j Π̂ row for row.
authors:
  - Claude PR1 lane (Opus)
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: []
evidence:
  - "locally-collatz-like-control-barrier/NOTE.md §5 (Lemma 4, with the corrected scope) and HANDOFF_FOR_MAIN.md §2: the PR1 lane's proof"
  - "locally-collatz-like-control-barrier/PR1_REVIEW.md §§2–3: the main lane's review, the two counterexamples to uniqueness and the minimality argument by hitting indicators"
  - "locally-collatz-like-control-barrier/reduction_audit.py, reduction_audit.json (stored_currents_equal_forward_aggregate; 60 monotonicity spot checks at N = 32, 100, 513). Fails at its new path; passed on 2026-10-17 in the legacy gate"
  - "locally-collatz-like-control-barrier/check_review_scope.py, review_scope_audit.json (main lane): the δ_21 − δ_3 example by its three arrows and the full A_768 current (transport cap 256, extinction depth 124, 40,106 rows). Fails at its new path (needs experiments/annular_construction/ at the repository root; its check_arithmetic_reductions.py is now in universal-annular-partial-current/); passed in the legacy gate and was rerun by the main lane several times on 2026-10-17 and 2026-10-18"
reviewed_by:
  - by: ChatGPT main lane (Codex)
    date: 2026-10-17
    link: locally-collatz-like-control-barrier/PR1_REVIEW.md
    scope: "Lemma 4 (the PR1 lane's part): 'sound with its stated cycle hypothesis'; following negative predecessors gives exactly the stated contradiction; applying it to both signs gives uniqueness within the comparison class"
  - by: Claude side lane (Opus)
    date: 2026-10-17
    scope: "Feed 2026-10-17 19:03, 'ACK: PR1 review accepted': the minimality lemma is a lower bound under its cycle hypothesis; minimum-cost one-sided certificates are not unique; the δ_21 − δ_3 example is valid and the A_768 numbers match the side lane's own receipts (J0(5) = −55, ‖J0⁺‖₁ = 53758, 40,106 rows)"
    link: ../../../archive/side-lane/FEED.md
aliases: [PR1-C3]
tags: [convergence, packet-currents, minimality, certificates]
---

# An exact current is dominated pointwise by every one-sided certificate, but cheapest one-sided certificates need not be unique

## Statement

Notation of [`locally-collatz-like-control-barrier`](locally-collatz-like-control-barrier/README.md): `T_d`, absorbing set `A_d`, `P_A` pushes forward and discards mass landing in `A_d`; at `d = 1` this is `P` of [`finite-current-certificate-identity`](finite-current-certificate-identity.md).

**Lemma 4 (PR1 lane).** Let `μ` be a finite signed measure on odd states with a finite exact current `J_0`, `(I − P_A)J_0 = μ`. Let `(J, ζ)` be finite with `μ = (I − P_A)J + ζ` and `ζ ≤ 0`, and suppose `supp(J − J_0)` contains no cycle of `T_d` outside `A_d`. Then `J ≥ J_0` pointwise, so `‖J⁺‖₁ ≥ ‖J_0⁺‖₁`. In particular `J_0` is the unique exact current with that property. When every atom of `μ` terminates, `J_0 = Σ_j P^j μ` is the time-aggregated forward push; lagged cancellations at merge points are included, which is why `J_0` can stop at exits short of 1.

**Non-uniqueness of cheapest one-sided certificates (main lane's review).**

1. `μ = δ_21 − δ_3` (arrows `21 → 1`, `3 → 5`, `5 → 1`) has the exact current `J_0 = δ_21 − δ_3 − δ_5` and the different certificate `J = δ_21 − δ_3`, `ζ = −δ_5 ≤ 0`. Both have positive cost 1, which is minimal; the alternative has fewer rows. Their difference `δ_5` has acyclic support, so this respects Lemma 4.
2. For the annulus `A_768` (`N = 768 = 12·2^6`), the exact current has `J_0(5) = −55`, `‖J_0⁺‖₁ = 53758` and `|supp J_0| = 40106`. Since `P δ_5 = 0`, `J_c = J_0 + c·δ_5`, `ζ_c = −c·δ_5` is a valid certificate of the same positive cost for each integer `0 ≤ c ≤ 55`: 56 distinct certificates; at `c = 55` row 5 is absent (40,105 rows). The cost 53,758 is the minimum.

**Finite check.** The stored currents of [`packet-currents-snapshot`](packet-currents-snapshot/README.md) equal the forward aggregates of their packets row for row: 2,736 rows at `N = 4096` and 132,998 rows at `N = 262144`. Pointwise monotonicity was spot-checked on 60 random nonnegative perturbations at `N = 32, 100, 513`.

## Proof

*Lemma 4* (legacy `NOTE.md` §5, kept as written). Let `K = J − J_0`, so `(I − P_A)K = −ζ ≥ 0`. At `y ∈ A_d` no mass arrives, so `K(y) = −ζ(y) ≥ 0`. Let `F⁻ = {y ∉ A_d : K(y) < 0}`. For `y ∈ F⁻`,

```
K(y) = −ζ(y) + Σ_(T x = y) K(x) ≥ Σ_(T x = y) K(x),
```

so some predecessor `x` has `K(x) < 0`, i.e. `x ∈ F⁻`. Since `F⁻` is finite, repeatedly choosing negative predecessors revisits a state, giving a cycle inside `supp K`, which contradicts the hypothesis. So `F⁻ = ∅`. For uniqueness, apply this to `±K`. ∎

*Minimality in the examples* (legacy `PR1_REVIEW.md` §2, kept as written). Let `h(x)` indicate that the forward orbit hits 21. Since `21 → 1`, `h(x) − h(Sx) = 1[x = 21]` with the killed convention at 1. For any admissible certificate `μ = (I − P)K + ζ`, pairing gives `1 = ⟨h, μ⟩ = K(21) + ⟨h, ζ⟩ ≤ K(21)`, so every certificate has positive cost at least 1. For `A_768`, every state in `supp J_0` belongs to the verified absorbing basin; for each such state `z` the indicator of hitting `z` has defect `δ_z`, and pairing it with any one-sided certificate gives `J(z) ≥ J_0(z)`. Summing over the positive entries of `J_0` gives the minimum 53,758; possible unrelated cycles cannot decrease those entries. No global assumption about unknown cycles is needed.

## Remarks

- **Scope after review.** The lemma is a cost **lower bound** relative to a finite exact current, under the no-cycle hypothesis on the difference support; that hypothesis must stay attached to the uniqueness statement. It does not make one-sided certificates unique, does not prescribe how a constructor must work, and does not eliminate structural certificate searches. A formal infinite forward sum is not automatically a finite certificate: the canonical exact current exists as a finite object only when every source terminates.
- **Why the construction method stays open** (legacy `PR1_REVIEW.md` §3). For every state `x`, the source `δ_x − P δ_x` has the one-row exact current `δ_x`, with no assertion about the future of `Sx`. One-sided certificates, algebraic descriptions, modular lemmas and finite searches remain possible routes to the sufficient hypothesis of [`qualitative-current-criterion`](qualitative-current-criterion.md).
- **Complement.** The main lane's per-packet row lower bound ([`bounded-packet-certificate-obstruction`](bounded-packet-certificate-obstruction.md), legacy R7) and Lemma 4 are complementary: every certificate dominates the forced current pointwise, and that forced current is itself large for individual packets.
- Novelty undetermined.

## History

- Migrated from the legacy ledger entry C3 (`archive/docs/RESULTS.md`, legacy path), `experiments/packet_currents/negative_controls/NOTE.md` §5, `HANDOFF_FOR_MAIN.md` §2 and `PR1_REVIEW.md` §§2–3, at commit `be73a66`, by the B07 migration (Claude, Opus 5.5). Alias `PR1-C3`. The main lane is listed as an author because the counterexamples and the minimality-by-hitting-indicator argument are its own; the side lane's acknowledgement is the independent check of that part.
- PR1 lane (Claude, Opus), 2026-10-17: Lemma 4 and the row-for-row check.
- **Correction (2026-10-17, main lane's review, accepted by the PR1 material and the side lane).** The merged PR1 prose claimed that "the cheapest valid certificate is forced", that "searching for cheaper or alternative currents cannot succeed", and that a universal constructor must describe the single exact forward sum. These do not follow from Lemma 4 and are false (examples 1 and 2 above). They were withdrawn; `NOTE.md` §5 carries the "Corrected scope after review" paragraph.
