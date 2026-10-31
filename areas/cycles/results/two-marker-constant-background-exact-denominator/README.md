---
id: two-marker-constant-background-exact-denominator
kind: result
title: "Two markers on a constant background: cancellation exactly 4^n − 3^n and denominator 4^n + 3^n"
status: written
claim: >
  Raw odd-only clock. For n ≥ 1 let w_n = (1, 2^(n−1), 3, 2^(n−1)) (a 1, then n − 1 twos, a 3, then n − 1
  twos), so m = 2n and A = 4n. Then w_n is primitive, its rotation by n differs from it in exactly the two
  positions 0 and n (the letters 1 and 3 swap), its intercept is C = 3^(2n−1) + 2·3^(n−1)(4^n − 3^n) +
  4^(n+1)(4^(n−1) − 3^(n−1)), D = 16^n − 9^n = (4^n − 3^n)(4^n + 3^n), gcd(C, D) = 4^n − 3^n, and the
  reduced denominator is q = 4^n + 3^n = 2^m + 3^(m/2) exactly. The two natural-order arcs between the
  mismatches both have intercept 4^n − 3^n, so the two-defect bound g ≤ (2^k − 1)·√(C_u·C_v) is attained
  within the factor 3 = 2^k − 1, and the cancellation G = 2^(A/2)(1 − (3/4)^n) is within a factor
  1 − (3/4)^n of 2^(A/2). The reduced cycle is an actual 3x+(4^n + 3^n) cycle, e.g. 19 → 41 → 37 → 17 for
  n = 2 (q = 25) and 73 → 155 → 139 → 127 → 59 → 67 for n = 3 (q = 91).
authors:
  - Claude cycles lane (Fable 5.1; directed by Santiago Armstrong)
created: 2026-10-28
depends_on: [two-defect-cancellation-bound]
certificates: [check_marker_family.py]
tags: [cycles, denominators, cancellation, two-mismatch, control-family]
---

# Two markers on a constant background: cancellation exactly `4^n − 3^n` and denominator `4^n + 3^n`

## Statement

Notation of [`conventions/NOTATION.md`](../../../../conventions/NOTATION.md) §2. For `n ≥ 1`,

```
w_n = (1, 2, …, 2, 3, 2, …, 2)        (positions 0 … 2n−1; a_0 = 1, a_n = 3, all others 2),
m = 2n,   A = 4n,   D = 2^(4n) − 3^(2n) = (4^n − 3^n)(4^n + 3^n).
```

1. `w_n` is primitive and its rotation by `n` has exactly two mismatches, at positions `0` and `n`, where the letters `1` and `3` are exchanged (amplitude `k = 2` in the sense of [`two-defect-cancellation-bound`](../two-defect-cancellation-bound.md)).
2. `C_(w_n) = 3^(2n−1) + 2·3^(n−1)(4^n − 3^n) + 4^(n+1)(4^(n−1) − 3^(n−1))`.
3. `gcd(C_(w_n), D) = 4^n − 3^n` and `q = D/gcd = 4^n + 3^n`.
4. Cutting at the two mismatches, both arcs `u = (2^(n−1), 3)` and `v = (2^(n−1), 1)` have intercept `C_u = C_v = 4^n − 3^n`; so (5) of the two-defect bound, `g ≤ (2^k − 1)√(C_u·C_v) = 3(4^n − 3^n)`, holds with equality up to the factor 3, and `g = 2^(A/2) − 3^(m/2) = 2^(A/2)·(1 − (3/4)^n)`.

| `n` | `m` | `A` | `g = 4^n − 3^n` | `q = 4^n + 3^n` | the `3x+q` cycle |
|---|---|---|---|---|---|
| 1 | 2 | 4 | 1 | 7 | `5 → 11 → 5` |
| 2 | 4 | 8 | 7 | 25 | `19 → 41 → 37 → 17` |
| 3 | 6 | 12 | 37 | 91 | `73 → 155 → 139 → 127 → 59 → 67` |
| 4 | 8 | 16 | 175 | 337 | states `C_(w^(j))/175` |

(For `n = 1`, `w_1 = (1, 3)`, `C = 5`, `D = 7`: the `3x+7` cycle `5 → 11 → 5`, with letters `1, 3`: `3·5+7 = 22 = 2·11`, `3·11+7 = 40 = 8·5`.)

## Proof

**Primitivity and the rotation.** The letters `1` and `3` each occur once, so no proper rotation fixes `w_n`, and rotation by `n` maps position `0` to the `3` and position `n` to the `1`; all other positions carry `2` on both sides.

**The intercept.** With `s_j = a_0 + … + a_(j−1)`: `s_0 = 0`, `s_j = 2j − 1` for `1 ≤ j ≤ n`, and `s_j = 2j` for `n + 1 ≤ j ≤ 2n − 1` (the extra `3 − 2` at position `n` adds one). Hence

```
C = 3^(2n−1) + Σ_(j=1)^(n) 3^(2n−1−j)·2^(2j−1) + Σ_(j=n+1)^(2n−1) 3^(2n−1−j)·4^j.
```

The first sum is `(1/2)·3^(2n−1)·Σ_(j=1)^n (4/3)^j = 2·3^(2n−1)((4/3)^n − 1) = 2·3^(n−1)(4^n − 3^n)`. The second is `4^(n+1)·Σ_(i=0)^(n−2) 3^(n−2−i)·4^i = 4^(n+1)(4^(n−1) − 3^(n−1))`. This is (2).

**The gcd.** Put `P = 4^n − 3^n` and `Q = 4^n + 3^n`, so `D = PQ`, `gcd(P, Q) = gcd(P, 2·3^n) = 1`, and both are coprime to 6.
- Modulo `P`, `4^n ≡ 3^n`: the middle term of (2) vanishes and `4^(n+1)·4^(n−1) = 4^(2n) ≡ 3^(2n)`, `4^(n+1)·3^(n−1) ≡ 4·3^n·3^(n−1) = 4·3^(2n−1)`. So `C ≡ 3^(2n−1) + 3^(2n) − 4·3^(2n−1) = 3^(2n−1)(1 + 3 − 4) = 0`: `P | C`.
- Modulo `Q`, `4^n ≡ −3^n`: the middle term is `2·3^(n−1)(−2·3^n) = −4·3^(2n−1)`; `4^(2n) ≡ 3^(2n)` and `4^(n+1)·3^(n−1) ≡ −4·3^(2n−1)`. So `C ≡ 3^(2n−1) − 4·3^(2n−1) + 3^(2n) + 4·3^(2n−1) = 3^(2n−1) + 3^(2n) = 4·3^(2n−1)`, which is coprime to `Q`. So `gcd(C, Q) = 1`.

Hence `gcd(C, D) = P·gcd(C/P, Q) = P` and `q = Q`. This is (3).

**The arcs.** Cutting at the mismatches `0` and `n` as in the two-defect node, `u = (a_1, …, a_n) = (2^(n−1), 3)` and `v = (a_(n+1), …, a_(2n−1), a_0) = (2^(n−1), 1)`. An intercept does not depend on its last letter, and for `n − 1` twos followed by anything `C = Σ_(j<n) 3^(n−1−j)·4^j = 4^n − 3^n`. So `C_u = C_v = P`, and (5) of that node reads `g ≤ 3·P` while `g = P`. This is (4).

## Certificates

[`check_marker_family.py`](check_marker_family.py) (standard library, exact integers, about a second) verifies (1)–(4) for `1 ≤ n ≤ 200`, including the closed form (2) against the definition of the intercept.

## Remarks

- **Role.** It is the sharpness witness for two statements. For the proved two-defect bound (5), it shows the step `gcd(C_u, C_v) ≤ √(C_u·C_v)` cannot be improved in general (here `C_u = C_v`). For the conjectured half-cancellation bound `G² < 2^A` of [`half-cancellation-for-few-mismatch-words`](../../questions/half-cancellation-for-few-mismatch-words.md), it shows the exponent `A/2` is best possible: `log₂G − A/2 = log₂(1 − (3/4)^n) → 0⁻`. It is the family that attains the maximal half-cancellation excess in the four-arc census of [`few-arc-codings-denominator-census`](../few-arc-codings-denominator-census/README.md) (finding 2).
- **Compared with the other two-defect families.** [`fixed-defect-unbounded-cancellation`](../fixed-defect-unbounded-cancellation.md) (`1^t 2^(2t)`) has `G = gcd(4^t − 1, 3^t − 2^t)`, unbounded but erratic; [`two-defect-marker-family`](../two-defect-marker-family.md) (`(3, b_n, 4, b_n)` on a mechanical background) has `gcd(A, m) = 1` and only the lower bound `q > (8/3)·2^(m/2)`. Here `gcd(A, m) = m`, `D` has the full algebraic factorisation, and everything is exact: `q = 2^m + 3^(m/2)`, so `log₂q / m → 1`.
- **Mechanism.** The cancellation is the algebraic factor `2^(A/2) − 3^(m/2)` of `D`, which divides `C` because the two halves of the word are exchanged by the rotation by `m/2` with the two markers swapped. The same mechanism (an algebraic factor of `D` from `gcd(A, m) > 1` plus a compatible symmetry) accounts for every large cancellation seen in the census. It is unavailable to a near-critical word, whose `gcd(A, m)` is small.
- **Controls and scope.** Each member is a genuine primitive positive `3x+q` cycle with `q = 4^n + 3^n`, far from `q = 1`; `A = 2m` is far above the critical total. No cycle is excluded. Elementary; no novelty claimed.

## History

- Written 2026-10-28 by the Claude cycles lane (Fable 5.1), directed by Santiago Armstrong, after the family appeared as the extremal case of the few-arc census.
- 2026-10-31: the exact denominator is re-derived in two lines as the trivial-cycle instance (`u' = (2)^n`, `j = 1`) of corollary (ii) of [`doubled-words-periodic-and-antiperiodic-points`](../doubled-words-periodic-and-antiperiodic-points/README.md) (Claude cycles lane, Fable 5.1).
