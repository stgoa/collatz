---
id: fixed-defect-unbounded-cancellation
kind: result
title: "Two unit rotation defects allow arbitrarily large cancellation: the family 1^t 2^(2t)"
status: reviewed
claim: >
  Raw odd-only clock. For t ≥ 1 the positive word w_t = 1^t 2^(2t) (t ones, then 2t twos; m = 3t,
  A = 5t) is primitive, differs from its one-letter left rotation in exactly two positions with
  amplitude one, and has g_t = gcd(C_t, D_t) = gcd(2^(2t) − 1, 3^t − 2^t), where
  C_t = 3^(3t) − 2^(t+1)·3^(2t) + 2^(5t) and D_t = 32^t − 27^t. For every M coprime to 6 some t (e.g.
  t = φ(M)) has M | g_t, and v_5(g_t) = k + 1 at t = 4·5^k. Yet q_t = D_t/g_t ≥ (32^t − 27^t)/(4^t − 1) > 1,
  every state exceeds the denominator (q_t < L), and the reduced cycles are genuine primitive
  positive 3x+q_t cycles. So no cancellation bound depending only on mismatch count, amplitude,
  rotation-prefix discrepancy or alphabet can hold.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: []
evidence:
  - "two-defect-rotation-exclusion/DEFECT_OBSTRUCTIONS.md: the written proof and the table of g_t"
  - "two-defect-rotation-exclusion/c011_two_defect_check.py: side-lane check of the gcd formula for t ≤ 60"
  - "two-defect-rotation-exclusion/rotation_defect_audit.json: 51 cancellation-family examples and twelve prescribed moduli (historical receipt; its checker no longer runs at the new path)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-19
    link: two-defect-rotation-exclusion/c011_two_defect_check.py
    scope: "Feed 2026-10-19 04:08, REFEREE C011: gcd(C, D) = gcd(4^t − 1, 3^t − 2^t) for every t ≤ 60, with 5 | g at t = 2, 25 at t = 10, 125 at t = 50 (numerical reproduction of the formula and the 5-adic growth; the written proof itself was not separately reviewed)"
tags: [cycles, rotation-distance, cancellation, counterexample]
---

# Two unit rotation defects allow arbitrarily large cancellation: the family 1^t 2^(2t)

## Statement

For `t ≥ 1` let `w_t = 1^t 2^(2t)` (powers denote repetition of the valuation symbol), `m = 3t`, `A = 5t`, `D_t = 2^(5t) − 3^(3t) = 32^t − 27^t > 0`. Against its one-letter left rotation, `w_t` differs at exactly the two positions `t − 1` and `3t − 1` (differences `−1, +1`), the shift is coprime to the period, and `w_t` is primitive (one cyclic transition `1 → 2`). Its intercept is `C_t = 3^(3t) − 2^(t+1)·3^(2t) + 2^(5t)`, and

```
g_t = gcd(C_t, D_t) = gcd(2^(2t) − 1, 3^t − 2^t).                      (1)
```

1. For every `M` coprime to 6, `M | g_t` for `t = φ(M)` (any `t` if `M = 1`).
2. `v_5(g_t) = k + 1` at `t = 4·5^k`.
3. Nevertheless `q_t = D_t/g_t ≥ (32^t − 27^t)/(4^t − 1) > 1` (3), and the numerators `C_(i)/g_t` form a primitive positive odd `3x+q_t` cycle with `q_t < L`.
4. All of the following stay bounded: rotation distance 1, Hamming mismatch count 2, maximum amplitude 1, total absolute amplitude 2, maximum absolute rotation-prefix difference 1, alphabet `{1, 2}`, mean `5/3`. What grows is the defect separation (`t` and `2t`), the period `3t`, and the discrepancy from the linear mean (`2t/3`).

## Proof

[`DEFECT_OBSTRUCTIONS.md`](two-defect-rotation-exclusion/DEFECT_OBSTRUCTIONS.md). With `x = 2^t`, `y = 3^t`: `D = x^5 − y^3`, `C = y^3 − 2xy² + x^5`, `C − D = 2y²(y − x)`; since `gcd(D, 2y) = 1`, `gcd(C, D) = gcd(D, y − x) = gcd(x³(x² − 1), y − x) = gcd(x² − 1, y − x)`, using `gcd(x, y − x) = 1`. For (1): multiplication by 2 or 3 permutes the units mod `M`, so `2^φ(M) ≡ 3^φ(M) ≡ 1`. For (2): `v_5(2^8 − 1) = v_5(3^4 − 2^4) = 1`, and if `5 ∤ XY`, `v_5(X − Y) = a ≥ 1`, then `v_5(X^5 − Y^5) = a + 1` by the binomial expansion; iterate in both entries of (1). For (3): `32^t − 27^t ≥ 5·27^(t−1) > 4^t`; the minimum `C_t/g_t` exceeds `q_t` because `C_t − D_t = 2·3^(2t)(3^t − 2^t) > 0`, `(3x+1)/2` increases and `(3x+1)/4 = 1 + (3/4)(x − 1)` decreases while staying above 1. A repeated state would force a shorter valuation period. For (4): `Σ_(i<j)(a_i − b_i) = a_0 − a_j ∈ {0, −1}`; the left-rotation intercept satisfies `2C'_t = 3C_t + D_t`, `C'_t − C_t = 2^t(4^(2t) − 3^(2t))` and `gcd(D_t, C'_t − C_t) = g_t`, so no extra rotation-cut factor is exploited: two letter defects bound a long plateau of nonzero prefix difference.

Exact values:

| `t` | `m` | `g_t` | `q_t` when short |
| --- | --- | --- | --- |
| 1 | 3 | 1 | 5 |
| 2 | 6 | 5 | 59 |
| 3 | 9 | 1 | 13085 |
| 4 | 12 | 5 | 103427 |
| 6 | 18 | 35 | — |
| 12 | 36 | 455 | — |
| 20 | 60 | 275 | — |
| 24 | 72 | 44135 | — |
| 100 | 300 | 138875 | — |

At `t = 1` the raw `q = 5` realisation is `23 → 37 → 29 → 23`; at `t = 2` the raw `q = 59` realisation is `221 → 361 → 571 → 443 → 347 → 275 → 221`.

## Remarks

- **What it refutes.** A cancellation bound depending only on the number or size of rotation mismatches. It does not refute an estimate on `g_t/D_t` or a denominator bound that keeps the period and arc lengths, such as [`two-defect-cancellation-bound`](two-defect-cancellation-bound.md) (consistent: there `g_t` is bounded relative to `D`). It is not a claim of exponential gcd growth in the period.
- **Relation to block results.** `w_t` is the two-block setup of [`unequal-slope-two-block-growth`](unequal-slope-two-block-growth/README.md) with `u = (1)`, `v = (2)`, repetition counts `t, 2t` (both growing, so outside the fixed-`v` bound of [`repeated-block-cancellation-bound`](repeated-block-cancellation-bound/README.md)); that node's imported unequal-slope result implies subexponential cancellation in `t`, which nothing here contradicts.
- **Controls.** The `t = 1` cycle is a genuine `3x+5` control. The family satisfies `q ≤ L`; circular order is neither asserted nor needed.
- **Novelty.** Elementary; none claimed.

## History

- Split from `experiments/cycle_spectrum/C011/` (legacy ID `C011`; `DEFECT_OBSTRUCTIONS.md`) at commit `be73a66`, by the B04 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex), 2026-10-19. Status `reviewed` on the strength of the side lane's exact reproduction of (1) for `t ≤ 60` with the 5-adic growth; the Lean lane's full read of C011 (feed 04:14) names `ROTATION_DEFECTS.md`, `EXCLUSION.md` and `GENERAL_DEFECTS.md`, not this note.
