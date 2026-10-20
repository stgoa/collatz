---
id: three-defect-arbitrary-background
kind: result
title: Words at rotation distance three can carry an arbitrary shared background, beyond any fixed S-unit description
status: reviewed
claim: >
  Raw odd-only clock. (i) For every t ≥ 1 and every word U with t ones and 2t twos in any order,
  w_U = (3, U, 4, U, 5, U) (m = 9t + 3, A = 15t + 12) is primitive, has minimum nonidentity rotation
  distance exactly 3, positive D, and A < 2m exactly when t > 2; the binom(3t, t) choices of U give
  pairwise distinct intercepts C_U. (ii) For V = (5, 2^n), C_V = 32·4^n − 31·3^n ≡ 1 (mod p) for every
  prime p ≠ 2, 3 of a given finite set S once (p − 1) | n, so the shared-arc intercepts lie in no fixed
  S-unit group. (iii) For any fixed finite coefficient set, fixed nonzero rational generators, term
  count K and linear exponent-height constant H, for all large t some admissible C_U is not a sum of at
  most K signed terms f·γ_1^(e_1)…γ_r^(e_r) with |e_j| ≤ H·t. No denominator bound or cycle exclusion
  is claimed.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: []
evidence:
  - "coupled-defect-matrix-smith-form/COUPLED_OBSTRUCTIONS.md: the written proofs and the q = 536,851,229 nine-state example"
  - "coupled-defect-matrix-smith-form/shared_arc_audit.json: the admissible family at t = 3, 4, 5 (84, 495 and 3,003 backgrounds), prime-escape residues; historical receipt, its checker no longer runs at the new path"
  - "coupled-defect-matrix-smith-form/c012_candidate_check.py: side-lane certificate of that node; it checks the corrected C(k, 2^n) formula and the distance-three family (1, U, 3, U, 4, U)"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed 2026-10-19 04:45 (in the C012 referee entry): COUPLED_OBSTRUCTIONS.md sections 1-3 read by hand, no error; the three-defect family, the corrected C(5, 2^n) = 32·4^n − 31·3^n and the counting bound checked"
  - by: Claude side lane (Opus)
    date: 2026-10-19
    link: coupled-defect-matrix-smith-form/c012_candidate_check.py
    scope: "Feed 04:35, REFEREE C012: corrected formula C(k, 2^n) = 3^n + 2^k(4^n − 3^n) and the distance-three family (1, U, 3, U, 4, U) on 300 random backgrounds over {2, 5} confirmed"
tags: [cycles, rotation-distance, s-units, obstruction]
---

# Words at rotation distance three can carry an arbitrary shared background, beyond any fixed S-unit description

## Statement

1. **Arbitrary background at distance three.** For `t ≥ 1` let `U` be any word with `t` ones and `2t` twos (length `n = 3t`, total `A_U = 5t`), and `w_U = (3, U, 4, U, 5, U)`, `m = 9t + 3`, `A = 15t + 12`. Each marker occurs once, so `w_U` is primitive and every nonidentity rotation mismatches at all three marker positions; rotation by `n + 1` has exactly those three (signed differences `1, 1, −2`). Hence

```
min_(1 ≤ r < m) Hamming(w_U, R_r w_U) = 3.                                      (1)
```

`2^A/3^m = (4096/27)·(32768/19683)^t > 1`, and `A < 2m` exactly when `t > 2`; for `t ≥ 3` the word satisfies both necessary total conditions `m·log₂3 < A < 2m` of a nontrivial `q = 1` cycle (not sufficient for denominator one). Each word gives a primitive actual `3x+q` cycle at its reduced `q`, with no claim that `q` is small.

2. **Escape from every fixed S-unit group.** For `V = (5, 2^n)` (`2^n` = `n` twos), `C_V = 3^n + 32(4^n − 3^n) = 32·4^n − 31·3^n` (2). For a finite prime set `S`, take `n` divisible by `p − 1` for every `p ∈ S \ {2, 3}`; then `C_V ≡ 1 (mod p)` for those `p`, and `C_V` is odd and prime to 3, so `C_V > 1` has a prime factor outside `S`. These arcs occur in the primitive words `(1, V, 3, V, 4, V)` (`m = 3n + 6`, `A = 6n + 23`, so `A > 2m`: outside the `q = 1` range; the counting theorem uses family 1 instead).

3. **No bounded-term rewrite at controlled height.** Fix a finite coefficient set `F ⊂ Q`, nonzero rationals `γ_1, …, γ_r`, `K ≥ 1` and `H > 0`. For all large `t`, some `U` as in (1) has `C_U` not expressible as a sum of at most `K` terms `ε·f·γ_1^(e_1)…γ_r^(e_r)` with `ε = ±1`, `f ∈ F`, `|e_j| ≤ H·t`.

## Proof

[`COUPLED_OBSTRUCTIONS.md`](coupled-defect-matrix-smith-form/COUPLED_OBSTRUCTIONS.md) §§1–3. **Distinct intercepts:** for length `n ≥ 2`, `C_U = 3^(n−1) + 2^(a_0)·C_tail` with `C_tail` odd, so `v₂(C_U − 3^(n−1))` recovers the first letter; induct, and the fixed total recovers the last letter (which the intercept omits). So the words give exactly `binom(3t, t)` distinct intercepts at fixed length and total. **Counting:** at most `2|F|·(2·floor(Ht) + 1)^r` individual terms, hence at most `[1 + 2|F|(2·floor(Ht) + 1)^r]^K` sums (4), polynomial in `t`, while `binom(3t, t) = Π_(j=1..t)(2t + j)/j ≥ 3^t`. **Escape:** the finite multiplicative group mod `p` gives `2^n ≡ 3^n ≡ 1`.

**Exact example.** `V = (5, 2)`, `C_V = 35`; `w = (1,5,2,3,5,2,4,5,2)`, `m = 9`, `A = 29`, `C = 151,215,095`, `D = 536,851,229`, `g = 1`, `q = 536,851,229`, raw cycle `(151215095, 495248257, 63206125, 181617401, 135212929, 29452813, 156302417, 62859905, 22669717)`; the eight nonidentity rotation distances are `(9, 9, 3, 9, 9, 3, 9, 9)`.

## Remarks

- **What it rules out.** A fixed rotation defect count does not bound the internal complexity of shared arcs; the specific compression of the arc intercepts into a fixed number of S-unit terms with exponents linear in the length fails (this covers the group generated by 2 and 3 used in [`two-block-uniform-denominator-growth`](two-block-uniform-denominator-growth/README.md)). It does not refute arbitrary S-unit methods, coupled relations without separate rewriting of each `C_U`, new generators with a justified height estimate, the candidate bound ([`rotation-defect-denominator-candidate`](../questions/rotation-defect-denominator-candidate.md)), or fixed-defect bounded-denominator finiteness.
- **Actual correlations can still help.** In `(1, V, 3, V, 4, V)` the three blocks after the marker cut all have intercept `E = 3C_V + u` (`u = 2^(A_V)`, `α = 3^(n+1)`), `C_cut = E·S` with `S = α² + 8uα + 128u²`, `D = 256u³ − α³`; reductions give `D ≡ 64u²(α − 12u) (mod S)` and `S ≡ 16·23·u² (mod α − 12u)`, so `gcd(D, S) | 23` and `gcd(D, C_cut) ≤ 23E`. The arbitrary shared intercept is one correlated factor here, which is why the counting obstruction is not an impossibility theorem for the coupled arithmetic. [`shared-background-denominator-law`](shared-background-denominator-law/README.md) develops this.
- **Shift.** The family has `gcd(shift, m) = n + 1`, which grows; a coprime-shift restriction would remove it and must not be silently imposed.
- **Controls.** Consistent with [`two-defect-rotation-exclusion`](two-defect-rotation-exclusion/README.md) (distance exactly 3); the `d = 5, 7, 13` cycles and repetitions of `(2)` are untouched.
- **Novelty.** None claimed.

## History

- Split from `experiments/cycle_spectrum/C012/` (legacy ID `C012`; `COUPLED_OBSTRUCTIONS.md`) at commit `be73a66`, by the B04 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex), 2026-10-19. **Draft correction (legacy):** an initial chat calculation wrote the first term of (2) as `3^(n+1)` and gave residue 3; the root reviewer caught the off-by-one before persistence (already `U = (k, 2)` has intercept `3 + 2^k`). The corrected `3^n` and residue 1 are used throughout; the new-prime conclusion is unchanged.
