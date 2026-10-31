---
id: dyadic-order-lemma
kind: result
title: Dyadic normalisation of a cycle, the exact inversion formula and the order lemma
status: reviewed
claim: >
  Raw odd-only 3x+q map, q odd and coprime to 6, primitive cycle n_0 = L < …, 3n_i + q = 2^(a_i)·n_(i+1).
  With heights h_i = floor(log₂(n_i/L)), z_i = n_i/2^(h_i) ∈ [L, 2L), F_i = 3z_i + q/2^(h_i) and
  c_i = a_i + h_(i+1) − h_i: F_i = 2^(c_i)·z_(i+1), c_i ≥ 1, the z_i are distinct and Σc_i = Σa_i = A.
  For z_i < z_j with h_j = h_i + k, k ≥ 1, r = n_j − 2^k·n_i is a positive odd integer and
  F_j − F_i = [3r − q(2^k − 1)]/2^(h_j); ties F_i = F_j are impossible. If sorted F increases with
  sorted z, the normalised successor is a circular rank shift, c is the mechanical word of total A,
  and gcd(A, m) = 1 for m > 1; when q ≤ L the converse holds. The original word a still differs from
  c by the height coboundary, so this says nothing by itself about gcd(C_w, D).
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [narrow-cycles-are-mechanical]
lean:
  - LeanLane.Cyc.inversion_formula
  - LeanLane.Cyc.exponent_dichotomy_F
  - LeanLane.Cyc.no_inversion_of_le_two
  - LeanLane.Cyc.OrdCycle.cword_eq_mech_ord
  - LeanLane.Cyc.OrdCycle.coprime_Apre
evidence:
  - "../rotation-block-exclusion/ORDER_THEORY.md, sections 1-2: the written proofs"
  - "../rotation-block-exclusion/order_audit.json: 739,757 exact state pairs and 1,424 inversion-formula input pairs (historical receipt; its checker no longer runs at the new path)"
  - "../rotation-block-exclusion/c005_c006_order_check.py, part (2): side-lane check of the q = 1 inversion arithmetic"
  - "../ordered-cycle-sparse-forcing/c006f_order_word_check.py: side-lane check of the word form on actual ordered cycles (needs a side-lane helper, see that node)"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed 2026-10-19 02:13, update 02:19: the inversion formula, the order lemma and its converse under q <= L re-derived by hand with no error. Lean units C005-a (order lemma in abstract form, inversion formula over Q) and C006-f (the word form at any q) verified; the converse is not formalised"
    link: ../../../archive/side-lane/FEED.md
  - by: Claude side lane (Opus)
    date: 2026-10-19
    scope: "Feed 02:13, REFEREE C005 + C006: the q = 1 inversion arithmetic and the order controls (q = 233, q = 5, q = 11) reproduced on the corpus"
    link: ../../../archive/side-lane/FEED.md
tags: [cycles, dyadic-order, normalisation, mechanical-words]
---

# Dyadic normalisation of a cycle, the exact inversion formula and the order lemma

## Statement

Let `n_0, …, n_(m−1)` be distinct positive odd integers in a raw `3x+q` cycle, `q ≥ 1` odd and coprime to 6, with exact valuations `3n_i + q = 2^(a_i)·n_(i+1)`, `a_i ≥ 1`. Rotate so `n_0 = L = min n_i`, and put `H = max n_i`,

```
h_i = floor(log₂(n_i/L)),
z_i = n_i/2^(h_i) ∈ [L, 2L),
F_i = (3n_i + q)/2^(h_i) = 3z_i + q/2^(h_i),
c_i = a_i + h_(i+1) − h_i.                         (1)
```

1. **Normalisation.** `F_i = 2^(c_i)·z_(i+1)`, `c_i ≥ 1`, the `z_i` are distinct, and `Σc_i = Σa_i = A`; `c` and `a` differ by the height coboundary `h_(i+1) − h_i`. When `q ≤ L`, all `c_i ∈ {1, 2}`.
2. **Inversion formula.** If `z_i < z_j`: when `h_j ≤ h_i`, `F_j > F_i`; when `h_j = h_i + k`, `k ≥ 1`, `r = n_j − 2^k·n_i` is a positive odd integer and

```
F_j − F_i = [3r − q(2^k − 1)]/2^(h_j).             (2)
```

A strict inversion occurs exactly when `3r < q(2^k − 1)`; equality cannot occur inside a primitive cycle. Checking (2) on adjacent sorted `z` suffices for the whole sorted `F` list.
3. **Order lemma.** If the sorted `F_i` are strictly increasing with the sorted `z_i`, the normalised successor permutation is a circular rank shift, its chronological `c` word is mechanical with total `A`, and `gcd(A, m) = 1` when `m > 1`.
4. **Converse under `q ≤ L`.** For a primitive cycle with `m > 1` and `q ≤ L`, the successor is a circular rank shift if and only if sorted `F` is strictly increasing.

More generally, with `B = max h_i`, `q(2^B − 1) ≤ 3` ensures strict sorted `F` order; for supported odd `q` this is useful chiefly at `q = 1`, `B ≤ 2` ([`three-band-collatz-cycles-are-ordered`](three-band-collatz-cycles-are-ordered.md)).

## Proof

Written proofs: [`ORDER_THEORY.md`](rotation-block-exclusion/ORDER_THEORY.md) §§1–2. The least `F` is `3L + q`, and every `F` is below `6L + q < 2(3L + q)`, so the powers of 2 moving the increasing `F` list back into `[L, 2L)` take two consecutive values, the higher on a final block of `b` sorted ranks whose outputs precede the lower block's; the successor rank is `j + b mod m`, primitivity gives `gcd(b, m) = 1`, and the carry calculation of [`narrow-cycles-are-mechanical`](narrow-cycles-are-mechanical/README.md) makes `c` mechanical. For the converse with shift `+s`, `c = 1` is forced on the first `m − s` sorted ranks (since `F ≤ 3z + L ≤ 4z`) and `c = 2` on the final `s`, and every first-block value is below `4L` while every final-block value is at least `4L`.

## Lean

Partly formal. `LeanLane.Cyc.inversion_formula` is (2) over ℚ; `no_inversion_of_le_two` is the three-band arithmetic `3r ≥ 2^k − 1` for `k ≤ 2`, `r ≥ 1`. Lean unit C005-a generalises the narrow-cycle structure `NarrowCycle` to images `F` with `x_i < x_j ⇔ F_i < F_j`, `F_i < 2F_j` and `2^q·lo ≤ F_i < 2^(q+2)·lo` (`exponent_dichotomy_F` and the rank lemmas), i.e. exactly the order lemma's hypotheses, so the rank shift, mechanical letter formula, `gcd(h, m) = 1` and `A = mq + h` hold for every ordered dyadically normalised cycle. Lean unit C006-f states the word form on actual cycles: `LeanLane.Cyc.OrdCycle.cword_eq_mech_ord` (the normalised word read from the minimum is `mech A m 0`) and `coprime_Apre` (`gcd(A, m) = 1`), for every ordered primitive odd cycle at any `q`. The converse (claim 4) is not formalised; hence `reviewed`.

## Remarks

- **What order does not give.** A mechanical `c` can coexist with inversions and a non-rotation successor permutation, and a strictly ordered cycle with mechanical `c` can still have large cancellation; see [`mechanical-normalized-word-transfer`](../attempts/mechanical-normalized-word-transfer.md) and [`ordered-cycle-shortcuts`](../attempts/ordered-cycle-shortcuts/README.md). The `q = 11` cycle with minimum 13 has an inversion despite `q ≤ L` (`F(13) = 50 > 49 = F(29/2)`, `k = 1`, `r = 3`).
- **Weighted intercept.** Starting at `n_0 = L`, `(2^A − 3^m)·L = q·Σ_j 3^(m−1−j)·2^(P_j − h_j)` with `P_j = Σ_(i<j) c_i`; since `P_j = A_j + h_j` this sum is exactly the original intercept `C_w`. Normalisation is an invertible change of coordinates only when the height labels are retained.
- **Generic baseline.** The order-free comparisons are in [`generic-cycle-minimum-baselines`](generic-cycle-minimum-baselines/README.md).

## History

- Split from `experiments/cycle_spectrum/C005/` (legacy ID `C005`; `REPORT.md` §2, `ORDER_THEORY.md` §§1–2) at commit `be73a66`, by the B03 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex), 2026-10-19. The word form at any `q` was observed by the side lane on all 370 tested ordered cycles (feed 10:05) and then formalised as C006-f.
