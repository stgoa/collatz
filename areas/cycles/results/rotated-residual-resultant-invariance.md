---
id: rotated-residual-resultant-invariance
kind: result
title: "Unreviewed draft: rotated residual resultants agree away from 2 and 3, and their size can be quadratic in the period"
status: proposed
claim: >
  Unreviewed work in progress (legacy C014), unverified. For a positive word w with P_w(X) =
  Σ_j 2^(P_j)·X^(m−1−j), Q(X) = X^m − 2^A, G = monic gcd(P_w, Q) and R_w = Res(P_w/G, Q/G): the part of
  R_w coprime to 6 is the same for every cyclic rotation of w (from 2^(a_0)·P_(Rw) = X·P_w − Q). For
  t a positive multiple of 6, w_t = 1^t 2^(2t+1) (m = 3t + 1, A = 5t + 2, ρ = 2, G = 1) has prime-to-6
  resultant part S_t = (2^(t(2t+1)) − 1)/((2^t − 1)(2^(2t+1) − 1)) > 2^(2t²−2t−2), while D < 2^(5t+2); so the
  bound q ≥ D/(R_w)_(6) is vacuous (below 1) for t ≥ 6, at every rotation. No denominator bound or
  exclusion is claimed; the family lies inside the two-defect exclusion.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: []
evidence:
  - "compatible-arcs-common-partition-limits/OVERLAP_OBSTRUCTION.md: the draft's written argument"
  - "compatible-arcs-common-partition-limits/overlap_arithmetic_audit.json: the draft checker's receipt (historical; the checker no longer runs at the new path)"
tags: [cycles, rotation-distance, resultants, work-in-progress, unreviewed]
---

# Unreviewed draft: rotated residual resultants agree away from 2 and 3, and their size can be quadratic in the period

> **Work in progress, unreviewed.** Part of legacy C014, ChatGPT's uncommitted draft, committed on 2026-10-19 at the owner's request; no other lane reviewed or verified it. Everything below is the draft's claim.

## Statement

For a positive word `w = (a_0, …, a_(m−1))`, `P_j = Σ_(i<j) a_i`, `A = P_m`, define the whole-word polynomials `P_w(X) = Σ_j 2^(P_j)·X^(m−1−j)` and `Q(X) = X^m − 2^A`, so `C_w = P_w(3)` and `D = −Q(3)` (the empty-background case of [`shared-background-denominator-law`](shared-background-denominator-law/README.md)). Let `G` be their monic gcd, `Pbar_w = P_w/G`, `Qbar = Q/G`, `e = deg Qbar`, `R_w = Res(Pbar_w, Qbar) ≠ 0`, and `z_(6)` the part of `|z|` coprime to 6.

1. **Invariance under cuts.** With `Rw = (a_1, …, a_(m−1), a_0)`: `2^(a_0)·P_(Rw)(X) = X·P_w(X) − Q(X)` (1). Hence `P_w` and `P_(Rw)` vanish at the same roots of `Q`, have the same `G`, and `2^(a_0·e)·|R_(Rw)| = |Qbar(0)|·|R_w|` (3), with `Qbar(0)` a signed power of 2. So `(R_(Rw))_(6) = (R_w)_(6)` (4), for every positive word and every number of rotations. (This concerns the scalar resultants only, not the cut polynomials or their evaluated congruences.)
2. **A family where the resultant is huge.** For `t` a positive multiple of 6, `ℓ = 2t + 1`, `w_t = 1^t 2^ℓ`, `m = 3t + 1`, `A = 5t + 2`: `2^A/3^m = (4/3)(32/27)^t > 1`, `A < 2m`, `3A − 5m = 1` (so `gcd(A, m) = 1`, `w_t` primitive, `Q` irreducible, `G = 1`, `e = m`), and the minimum nonzero rotation distance is exactly 2. For a two-run word `1^a 2^b` with `gcd(a, b) = 1`: `|Res(P, Q)| = 2^(am + A(b−1))·(2^(ab) − 1)/[(2^a − 1)(2^b − 1)]` (6), so

```
|R_(w_t)| = 2^(13t² + 5t)·S_t,   S_t = (2^(t(2t+1)) − 1)/[(2^t − 1)(2^(2t+1) − 1)],   (R_(w_t))_(6) = S_t,   (7)–(8)
S_t > 2^(2t² − 2t − 2),   D < 2^(5t + 2),   S_t/D > 2^(2t² − 7t − 4) > 1  (t ≥ 6).       (9)
```

So `log S_t = Θ(m²)` while `log D = Θ(m)`, and the generic bound `q ≥ D/(R_w)_(6) = D/S_t < 1` (10) is vacuous, at every rotation by (4).

3. **Scope.** `gcd(C, D) | (R_w)_(6)` still holds here (`G = 1`), and `q ≥ D/gcd(D, (R_w)_(6))` (11) can be useful: direct evaluation gives `gcd(C, D) = gcd(D, S_t) = 1` at `t = 6, 12, 18, 24`, recovering `q = D`. At `t = 3` (outside the subsequence) the actual cancellation is 1 but `gcd(D, (R_w)_(6)) = 7`: `m = 10`, `A = 17`, `D = 72023`, `C = 155129`, `(R_w)_(6) = 2359 = 7·337`, and modulo 7 the common root of `P` and `Q` is 4, not the evaluation point 3. A scalar resultant can see a root other than `X = 3`.

## Proof

The draft's argument is [`OVERLAP_OBSTRUCTION.md`](compatible-arcs-common-partition-limits/OVERLAP_OBSTRUCTION.md) §§1–4: (1) from the prefix coefficients; (3) by evaluating the cancelled identity at the roots of `Qbar` and taking products; (6) from `(X − 2)(X − 4)·P(X) = (X − 4)·Q(X) + 2^(a+1)(X^b − 4^b)` and the permutation of `m`-th roots by `b`-th powers; (8) by `v_3(4^N − 1) = 1 + v_3(N)`. It also gives `gcd(C, D) = gcd(3^t − 2^t, 4^(t+1) − 3)` for this family. The finite values are calibrations, not a proof that the two gcds agree along the family. Unreviewed.

## Remarks

- **What the draft concludes.** Intrinsic polynomial gcd removal followed by a size bound on scalar residual resultants, at one cut or all cuts, cannot charge the resultant linearly in the period at fixed rotation distance. Arithmetic control of `gcd(D, R_(6))` that keeps the distinguished root `X = 3`, coupled congruences, and actual overlap relations are not ruled out.
- **Controls.** The identities apply to every raw cycle, including `q = 5, 7, 13`; the family `w_t` has `ρ = 2`, so [`two-defect-rotation-exclusion`](two-defect-rotation-exclusion/README.md) already handles it, which this draft must (and does) leave intact.
- **Novelty.** None claimed; "Collatz polynomials" in the literature are different objects (draft's `LITERATURE.md`).

## History

- Split from `experiments/cycle_spectrum/C014/` (legacy ID `C014`; `OVERLAP_OBSTRUCTION.md`) at commit `be73a66`, by the B04 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex) draft, 2026-10-19, uncommitted when that lane paused and committed at the owner's request. Status `proposed`: unreviewed work in progress.
