---
id: half-period-s-unit-approximation-law
kind: result
title: A half-period four-mismatch cycle forces a rational approximation of 2^c/3^N with N/25 spare bits
status: written
claim: >
  Raw odd-only 3x+1 clock. Assume EXT-1. Let a positive odd integer cycle have valuation word W = A B A[p] B[q],
  with nonempty positive words A, B, integers p, q >= 1, [.] raising only the final letter, and half length
  N = len(A)+len(B) >= 2^22. Let x, z, y, t be its states before the four blocks, a = len(A), b = len(B),
  h = (y-x)/2^sum(A) and j = (z-t)/2^sum(B). Then h is a positive integer, j is a nonzero integer, and exactly one
  of two cases holds. (I) j < 0: then p < q, every minimum of the cycle is a state before a letter of the first
  copy of A, and 0 < 2^(sum(B)+p+q) x - 3^N h < 2^(sum(B)+p+q-N/25) / h. (II) j > 0: every minimum is a state
  before a letter of the copy B[q], and 0 < 2^(sum(A)+p) t - 3^N j < 2^(sum(A)+p-N/25) / j. The two differences
  are exactly 2^sum(B) y + (2^p - 1) C_B and 3^a 2^q x + C_A, for the ordinary block intercepts C_A, C_B.
  Consequently, writing (c, U, V) for (sum(B)+p+q, x, h) or (sum(A)+p, t, j), every fraction other than V/U that
  is at least as close to 2^c/3^N as V/U has denominator greater than U (2^(N/25) - 1)/2. Every word whose
  rotation by half its length has exactly four mismatches takes the form A B A[p] B[q] after a cyclic rotation.
  This is a necessary condition, valid for both parities of p+q and with no bound on p, q or the letters. It
  excludes no cycle by itself. For 3x+d the identities hold with C replaced by d C; the gap estimate uses the
  d = 1 bound on the minimum and is not transferred.
authors:
  - Claude cycles lane (Fable 5.2; directed by Santiago Armstrong)
created: 2026-11-23
assumes: [musson-collatz-gap-all]
lean:
  - LeanLane.HalfPeriodSUnit.exists_h
  - LeanLane.HalfPeriodSUnit.exists_j
  - LeanLane.HalfPeriodSUnit.h_pos
  - LeanLane.HalfPeriodSUnit.intercept_identity
  - LeanLane.HalfPeriodSUnit.p_lt_q_of_j_neg
  - LeanLane.HalfPeriodSUnit.identity_I
  - LeanLane.HalfPeriodSUnit.identity_II
  - LeanLane.HalfPeriodSUnit.theta_I_lt
  - LeanLane.HalfPeriodSUnit.theta_II_lt
  - LeanLane.HalfPeriodSUnit.isolated
certificates: [check_s_unit_law.py]
evidence:
  - "check_s_unit_law.json: the exact constants and thresholds, the local descent below 2^17, the identities and every elementary inequality on 57781 actual 3x+d cycles of this shape (true addend retained), and the approximation lemma on exact continued fractions"
tags: [cycles, rotation-distance, half-defects, s-units, diophantine-approximation, frontier]
---

# A half-period four-mismatch cycle forces a rational approximation of 2^c/3^N with N/25 spare bits

## Statement

Use the raw odd-only map `x -> (3x+1)/2^v_2(3x+1)` on positive odd integers. For a positive word `w` (a finite
sequence of positive integers), `sum(w)` is its total, `len(w)` its length, and

```
C_w = sum over 0 <= i < len(w) of 3^(len(w)-1-i) * 2^(w_0 + ... + w_(i-1))
```

its intercept, so that an orbit segment with valuation word `w` from `u` to `v` satisfies
`2^sum(w) v = 3^len(w) u + C_w`. For a nonempty word `A`, `A[p]` is `A` with its last letter increased by `p`;
its intercept is `C_A`.

**Setting.** A positive odd integer cycle has valuation word

```
W = A B A[p] B[q],     a = len(A) >= 1,  b = len(B) >= 1,  p, q >= 1,  N = a + b,
```

read over `2N` odd steps. Its states before the four blocks are `x, z, y, t`:

```
x --A--> z --B--> y --A[p]--> t --B[q]--> x.
```

Write `sA = sum(A)`, `sB = sum(B)`, `E = 2 sA + 2 sB + p + q`, and

```
h = (y - x) / 2^sA,        j = (z - t) / 2^sB.
```

**Theorem.** Assume [EXT-1](../../../../sources/musson-collatz-gap-all.md) and `N >= 2^22`. Then `h` is a
positive integer, `j` is a nonzero integer, and exactly one of the following holds.

| Case | Sign | Minimum | Exact identity | Gap |
|---|---|---|---|---|
| I | `j < 0`, and then `p < q` | in the first copy of `A` | `2^(sB+p+q) x - 3^N h = 2^sB y + (2^p - 1) C_B` | `h * (left side) < 2^(sB+p+q-N/25)` |
| II | `j > 0` | in the copy `B[q]` | `2^(sA+p) t - 3^N j = 3^a 2^q x + C_A` | `j * (left side) < 2^(sA+p-N/25)` |

"In a copy" means: every minimum of the cycle is the state before one of the letters of that copy. Both
identities hold for every such cycle, of any length; only the gap needs EXT-1 and `N >= 2^22`.

**Corollary (isolated approximation).** Put `(c, U, V) = (sB+p+q, x, h)` in Case I and `(sA+p, t, j)` in Case II,
and `Theta = 2^c U - 3^N V`. Then `0 < Theta`, `Theta * V < 2^(c - N/25)`, and every fraction `P'/Q'` different
from `V/U` with `|2^c/3^N - P'/Q'| <= |2^c/3^N - V/U|` has

```
Q' > U * (2^(N/25) - 1) / 2.
```

**Scope.** The word shape is general: a word of even length `2N` whose rotation by `N` has exactly four
mismatches is a cyclic rotation of some `A B A[p] B[q]` (section 1). Both parities of `p+q`, both orders of the
magnitudes and all letters are allowed. The theorem is a necessary condition. It does not exclude a cycle.
[`half-period-four-mismatch-finiteness`](../half-period-four-mismatch-finiteness/README.md) combines it with Ridout's
theorem.

## Proof

Throughout, `alpha = log_2 3`. The certificate checks `15849/10000 < alpha < 317/200`.

### 1. Normal form

Let `W = u v` with `len(u) = len(v) = N`, and suppose the rotation by `N` has exactly four mismatches. Then `v`
differs from `u` in exactly two positions `i_1 < i_2`, by nonzero integers `delta_1, delta_2`. Rotating `W` by `k`
positions, `k <= N`, gives halves `u' = u[k:] v[:k]` and `v' = v[k:] u[:k]`. A difference at a position `i >= k`
keeps its sign and moves to `i - k`. A difference at `i < k` changes sign and moves to `N - k + i`. Exchanging
the halves changes both signs. Rotate by `i_2 + 1` when the signs are equal, and by `i_1 + 1` when they differ;
then exchange the halves if both signs are negative. In every case both differences become positive and the
later one sits at the last position. That is `W = A B A[p] B[q]` with `{p, q} = {|delta_1|, |delta_2|}`.
The four states `x, z, y, t` are cycle states, so they are positive odd integers coprime to 3.

### 2. The integers h and j

The four block equations are

```
2^sA z = 3^a x + C_A,          2^sB y = 3^b z + C_B,
2^(sA+p) t = 3^a y + C_A,      2^(sB+q) x = 3^b t + C_B.              (1)
```

Subtracting the equations with the same intercept gives

```
2^sA (2^p t - z) = 3^a (y - x),      2^sB (y - 2^q x) = 3^b (z - t).
```

Powers of 2 and 3 are coprime, so `h` and `j` are integers and

```
y - x = 2^sA h,   2^p t - z = 3^a h,   z - t = 2^sB j,   y - 2^q x = 3^b j.      (2)
```

**`h > 0`.** If `h <= 0` then `y <= x` and `2^p t <= z`. The first gives `y < 2^q x`, so `j < 0` and `z < t`.
Then `z < t <= z/2^p`, which is impossible.

**`j != 0`.** If `j = 0` then `z = t`. The orbit from `z` and the orbit from `t`, `N` odd steps later, would
coincide, so `W` would equal its rotation by `N`.

**`j < 0` implies `p < q`.** From (2), `(2^q - 1) x = 2^sA h - 3^b j` and `(2^p - 1) z = 3^a h + 2^(sB+p) j`.
Substituting in `C_A = 2^sA z - 3^a x`:

```
(2^p - 1)(2^q - 1) C_A = 3^a 2^sA (2^q - 2^p) h + [2^(sA+sB+p)(2^q - 1) + 3^N (2^p - 1)] j.      (3)
```

The bracket is positive and `C_A > 0`. If `j < 0`, the first term must be positive, so `q > p`.

### 3. Two exact identities

From (1), `3^b z = 2^sB y - C_B` and `3^b t = 2^(sB+q) x - C_B`. Multiply `3^a h = 2^p t - z` by `3^b`:

```
3^N h = 2^(sB+p+q) x - 2^sB y - (2^p - 1) C_B.                         (4)
```

From (1) and (2), `2^(sA+p) t = 3^a y + C_A` and `y = 2^q x + 3^b j`:

```
2^(sA+p) t = 3^N j + 3^a 2^q x + C_A.                                  (5)
```

Put `Theta_1 = 2^sB y + (2^p - 1) C_B` and `Theta_2 = 3^a 2^q x + C_A`. Both are positive. Since
`C_B < 2^sB y` and `C_A < 2^sA z` by (1),

```
Theta_1 < 2^(sB+p) y,          Theta_2 < 2^(sA+q) z.                   (6)
```

The second uses `2^q (3^a x + C_A) > 3^a 2^q x + C_A`. Equations (4), (5) are the identities of the table.

### 4. Slopes, budget and the minimum

Let `M` be the minimum state, `ell = log_2 M`, and

```
tau = E/2 - N alpha.
```

The product of `2^(w_i) = 3 + 1/x_i` over the cycle gives `2 tau = sum of log_2(1 + 1/(3 x_i)) > 0`, hence

```
0 < tau <= N log_2(1 + 1/(3M)) < N/(2M).                               (7)
```

Each of the four maps "half a turn" has a positive intercept. For instance `2^(sA+sB+p+q) x = 3^N y + C` with
`C > 0`. With `sA + sB = E/2 - (p+q)/2` this gives

```
y/x < 2^((p+q)/2 + tau),   z/t < 2^((p-q)/2 + tau),   t/z < 2^((q-p)/2 + tau).      (8)
```

The second comes from the map `B A[p]` from `z` to `t`, the third from the map `B[q] A` from `t` to `z`.
Every letter is at least 1, so

```
sA + sB = alpha N + tau - (p+q)/2 >= N,    (p+q)/2 <= (alpha - 1) N + tau.      (9)
```

**The minimum is large.** The certificate verifies that every odd `3 <= n < 2^17` reaches a smaller odd number.
The word `W` is not the word `(2, ..., 2)` of the trivial cycle, so `M >= 2^17` and `tau < N/2^18`.

**The minimum is small.** EXT-1, applied to the pair `(2N, E)`, gives
`eta = 1 - 3^(2N)/2^E >= 1/(2^172 (2N)^341)`. Also `eta < -ln(1 - eta) = sum of ln(1 + 1/(3 x_i)) < 2N/(3M)`.
Therefore

```
ell < 172 + 342 log_2(2N) = 514 + 342 log_2 N.                         (10)
```

**A step bound.** With `kappa = log_2(3 + 1/M)`, every odd step multiplies a state by at most `2^(kappa - 1)`.
The certificate checks `kappa < 317/200` for `M >= 2^17`.

### 5. Where the minimum is

Along `A`, the paired states `x_i` (first copy) and `y_i` (second copy) satisfy `y_i - x_i = 3^i (y - x)/2^(prefix)`,
which has the sign of `h`. Along `B`, the pairs `z_i`, `t_i` satisfy `z_i - t_i = 3^i (z - t)/2^(prefix)`, which
has the sign of `j`. So `x_i < y_i` always. If `j < 0` then `z_i < t_i`, and every minimum is in the first half
`A B`. If `j > 0` then `t_i < z_i`, and every minimum is in the first copy of `A` or in the copy `B[q]`. Four
cases remain. Two of them are impossible for large `N`.

**Case B: `j < 0`, a minimum in the first copy of `B`,** at offset `i`. By (2), `t > 2^sB`, and by (8),
`t/z < 2^((q-p)/2 + tau)`. A prefix of `B` of length `i` has total at most
`sB - (b - i)`, so `M >= 3^i 2^(b-i) z / 2^sB > 2^(b - (q-p)/2 - tau)`. Also `y > 2^sA >= 2^a` by (2), and the
remaining `b - i` steps give `y <= M 2^((kappa-1) b)`. Hence

```
b < ell + (q-p)/2 + tau,       a < ell + (kappa - 1) b.
```

**Case C: `j > 0`, a minimum in the first copy of `A`,** at offset `i`. By (2), `z > 2^sB >= 2^b` and
`y > 2^sA`, so `x > 2^(sA - (p+q)/2 - tau)` by (8) and `M >= 3^i 2^(a-i) x / 2^sA > 2^(a - (p+q)/2 - tau)`.
The remaining steps give `z <= M 2^((kappa-1) a)`. Hence

```
a < ell + (p+q)/2 + tau,       b < ell + (kappa - 1) a.
```

In both cases, using `|q-p|/2 <= (p+q)/2` and (9),

```
N < (1 + kappa) ell + kappa (alpha - 1) N + 2 kappa tau.               (11)
```

Now `kappa (alpha - 1) < (317/200)(117/200) < 0.928`. With (10) and `tau < N/2^18`, the certificate shows that
(11) fails for every `N >= 2^22`. So Cases B and C do not occur, and:

- if `j < 0`, every minimum is in the first copy of `A` (**Case I**, and `p < q` by section 2);
- if `j > 0`, every minimum is in the copy `B[q]` (**Case II**).

### 6. Case I

Write `X = log_2 x`. Let a minimum sit at offset `i` in the first copy of `A`.

- The prefix of `A` of length `i` takes `x` to `M`, so its total is at least `i alpha + X - ell`. The other
  `a - i` letters are at least 1. Hence `sA >= a + X - ell`.
- By (2), `2^q x = y + 3^b |j| > 3^b`, so `b < (X + q)/alpha`.
- By (9) and `sB >= b`, `N + X - ell <= alpha N + tau - (p+q)/2`, so
  `X <= (alpha - 1) N + tau + ell - (p+q)/2`.

Therefore

```
sA - 2X - p >= a - X - ell - p
            >  N - (1 + 1/alpha) X - q/alpha - ell - p
            >= (1 - alpha + 1/alpha) N + (1 - 1/alpha)(q - p)/2
               - (1 + 1/alpha) tau - (2 + 1/alpha) ell.                (12)
```

The last step inserts the bound on `X` and uses `(1 + 1/alpha)(alpha - 1) = alpha - 1/alpha`. The coefficient
`1 - alpha + 1/alpha` is positive because `alpha` is below the golden ratio. It is at least `2911/63400`.

By (6), (2) and (8), `Theta_1 < 2^(sB+p) y`, `h < y/2^sA` and `y < 2^((p+q)/2 + tau) x`. So

```
Theta_1 * h < 2^(sB + p - sA) y^2 < 2^(c + 2 tau - (sA - 2X - p)),      c = sB + p + q.
```

With (12), `q > p`, (10) and `tau < N/2^18`:

```
Theta_1 * h < 2^(c - [(2911/63400) N - (3 + 1/alpha) tau - (2 + 1/alpha) ell]) < 2^(c - N/25).
```

The certificate proves the last inequality for every `N >= 2^22`, block by block in `N`.

### 7. Case II

Write `T = log_2 t`. Let a minimum sit at offset `i` in the copy `B[q]`. Its first `i` letters are ordinary
letters of `B`, since `i <= b - 1`.

- As before, `sB >= b + T - ell`.
- By (2), `2^p t = z + 3^a h > 3^a`, so `a < (T + p)/alpha`.
- By (9) and `sA >= a`, `T <= (alpha - 1) N + tau + ell - (p+q)/2`.

Therefore

```
sB - 2T >= b - T - ell > N - (1 + 1/alpha) T - p/alpha - ell
        >= (1 - alpha + 1/alpha) N + (1 - 1/alpha) p/2 + (1 + 1/alpha) q/2
           - (1 + 1/alpha) tau - (2 + 1/alpha) ell.                    (13)
```

By (6), (2) and (8), `Theta_2 < 2^(sA+q) z`, `j < z/2^sB` and `z < 2^((p-q)/2 + tau) t`. So

```
Theta_2 * j < 2^(sA + q - sB) z^2 < 2^(c' + 2 tau - (sB - 2T)),         c' = sA + p,
```

and (13) gives `Theta_2 * j < 2^(c' - N/25)` exactly as in Case I.

### 8. The corollary

Let `xi = 2^c/3^N`, so `|xi - V/U| = Theta/(3^N U)`. If `P'/Q' != V/U` is at least as close to `xi`, then

```
1/(Q' U) <= |P'/Q' - V/U| <= 2 Theta/(3^N U),       Q' >= 3^N/(2 Theta).
```

From `3^N V = 2^c U - Theta`,

```
3^N/Theta = U (2^c/(Theta V) - 1/(U V)) > U (2^(N/25) - 1).
```

## Certificates

[`check_s_unit_law.py`](check_s_unit_law.py) uses exact integer and rational arithmetic only.

- **V1.** The bounds on `alpha` and `kappa`, the value `2911/63400`, and the two threshold inequalities for every
  `N >= 2^22`. Each is checked on the block `2^k <= N < 2^(k+1)` at `k = 22`, with a monotone step for larger `k`.
- **V2.** Every odd `3 <= n < 2^17` reaches a smaller odd number.
- **V3.** 57781 actual `3x+d` cycles with word `A B A[p] B[q]`, the true addend retained: all blocks of length at
  most 3 over the letters 1 to 3 with `p, q <= 5`, and a fixed pseudo-random sample with longer blocks. It checks
  (1), (2), the sign facts, the identities (4) and (5) with `C` replaced by `d C`, the slopes (8), the placement
  of every minimum, and each elementary inequality of Cases I, II, B and C. The `3x+47` cycle with word
  `(1,1,2,3)` and the `3x+1631` cycle through `9145` are replayed explicitly.
- **V4.** The approximation step of section 8, and its continued-fraction form, on 11513 exact convergents.

```
python3 areas/cycles/results/half-period-s-unit-approximation-law/check_s_unit_law.py
```

The receipt is [`check_s_unit_law.json`](check_s_unit_law.json), regenerated with `--write-receipt`.
The finite checks support the identities and inequalities. The theorem for all `N >= 2^22` is the written
argument.

## Lean

Only the algebraic core is formalised. The node stays `written`.

[`LeanLane/HalfPeriodSUnit.lean`](../../../../lean/LeanLane/HalfPeriodSUnit.lean) takes the four block equations
(1), with a general addend `d` and integer intercepts, as the structure `Blocks`. From them it proves:

| Lean declaration | Statement in this node |
|---|---|
| `exists_h`, `exists_j` | the integers `h`, `j` and the four relations (2) |
| `h_pos` | `h > 0` for positive states and `p, q >= 1` |
| `intercept_identity` | identity (3) |
| `p_lt_q_of_j_neg` | `j < 0` implies `p < q` |
| `identity_I`, `identity_II` | the exact identities (4) and (5) |
| `theta_I_lt`, `theta_II_lt` | the two bounds (6) |
| `isolated` | section 8 in integer form: a different fraction at least as close has `3^N <= 2 Theta Q'` |

Not formalised: the normal form of section 1, `j != 0`, the slopes and the budget of section 4, the placement of
the minimum, the estimates (11) to (13) with their logarithms, and the use of EXT-1. So the gap `N/25` is
not machine-checked. Build with `lake build LeanLane` from `lean/`; the receipts are
`lean/receipts/HalfPeriodSUnit.*`.

## Remarks

- **What is new in the argument.** The size method stalls on half-period words because a large defect makes
  every bound consistent. Here the same large defect is used the other way. The half word after the larger
  defect runs at states so high that its map is linear up to a tiny intercept, and the paired difference `h`
  or `j` is a small cofactor. A size inequality then becomes a statement that `2^c U` and `3^N V` nearly agree.
- **Continued fractions.** By Legendre's criterion (Hardy and Wright, Theorem 184), `V/U` in lowest terms is a
  convergent of `2^c/3^N`, and the next partial quotient exceeds `2^(N/25) - 3`. The certificate checks this
  form on exact expansions. Legendre's criterion is standard and is not used by the corollary above.
- **Two immediate consequences.** In Case I, `Theta_1 > 2^sB y > 2^(sA+sB)` and `h >= 1`, so
  `p + q > sum(A) + N/25`. In Case II, `Theta_2 > 3^a 2^q x` and `j >= 1`. The block product gives
  `3^a x >= 2^(sA - 2 tau) z`, so `p - q > N/25 + log_2 z - 2 tau > 0`. Hence `p > q` in Case II, and `p = q`
  never occurs for `N >= 2^22`. Both defects cannot be small.
- **Relation to earlier nodes.** The signs of `h`, `j` and the placement of the minimum are also proved in
  [`half-defect-positive-order-exclusion`](../half-defect-positive-order-exclusion/README.md) and
  [`half-defect-imbalance-growth`](../half-defect-imbalance-growth/README.md), which give sharper constants and
  a finite closure for small `N`. They are not used here. Section 5 re-proves what is needed, with the weaker
  threshold `N >= 2^22`.
- **Controls.** Actual cycles of this shape exist for other addends, for example `3x+47` and `3x+1631`. They are
  not contradicted. The identities hold for them with `d C` in place of `C`. The gap needs (10), which bounds the
  minimum of a `3x+1` cycle by a power of its length. Short cycles of `3x+d` have `N` far below `2^22`.
- **What it does not do.** The inequality is an Archimedean statement about one pair `(U, V)`. No effective
  lower bound for `|2^c U - 3^N V|` of this strength is known, so no cycle is excluded here.
- **Novelty.** Undetermined. The identities are elementary. No search of the literature for this use of the
  half-period structure was made.

## History

- 2026-11-23: derived by the Claude cycles lane (Fable 5.2; directed by Santiago Armstrong) while attacking the
  half-period case of [`rotation-distance-at-least-5`](../../questions/rotation-distance-at-least-5.md).
