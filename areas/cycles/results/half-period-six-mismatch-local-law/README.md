---
id: half-period-six-mismatch-local-law
kind: result
title: At most six half-period mismatches force a three- or four-term relation with N/50 spare bits
status: written
claim: >
  Raw odd-only 3x+1 clock. Assume EXT-1. Let a positive odd integer cycle be read over 2N odd steps, N >= 2^22,
  with valuation word W = V V', len(V) = len(V') = N, where V and V' differ in exactly d positions, 1 <= d <= 3
  (the rotation by N has exactly 2d mismatches). After a cyclic rotation the differences are the last letters
  of d blocks of each half, of lengths B_k and common totals s_k, the two last letters of block k exceeding
  their minimum by nu_k and nu'_k (one is 0, the other is p_k >= 1), and a minimum of the cycle lies in the
  first block. With x_k, y_k the states before the two copies of block k, the quotients
  g_k = (y_k - x_k)/2^(s_k) are nonzero integers (g_d = -g_0, s_d = s_0) and satisfy the exact relations
  3^(B_k) g_k = (2^(nu'_k) - 2^(nu_k)) xi + 2^c g_(k+1), with (xi, c) = (x_(k+1), nu'_k + s_(k+1)) or
  (y_(k+1), nu_k + s_(k+1)). Then for some k and one of the two choices, with
  T = max(3^(B_k)|g_k|, 2^c|g_(k+1)|): either |g_k| |g_(k+1)| (2^(p_k) - 1) xi <= 2^(-N/50) T, or
  |g_k| |g_(k+1)| xi^2 <= 2^(-N/50) max(T, 2^(p_k) xi). For d = 1 the size constraints are contradictory, and
  for d = 2 the first alternative always occurs for some relation. The linear step is an exact rational
  certificate over 84 sign cases. This is a necessary condition and excludes no cycle. For 3x+q the identities
  hold with the true addend; the size constraints use the q = 1 bound on the minimum and are not transferred.
  Four changed positions are not covered: in a normalised model these relations, and longer ones, do not
  force the conclusion (exploration only).
authors:
  - Claude cycles lane (Fable 5.2; directed by Santiago Armstrong)
created: 2026-11-23
assumes: [musson-collatz-gap-all]
certificates: [check_local_relations.py]
evidence:
  - "check_local_relations.json: the constants, 84 sign cases with exact Farkas multipliers verified from scratch, the two complements, the identities and the addend-free size rows on 12000 actual 3x+q cycles (true addend retained), and the normal form on 3000 random words"
  - "explore_relation_families.py and explore_relation_families.json: a normalised mixed-integer model (numpy, scipy; floating point) comparing families of relations for d = 2, 3, 4. Exploration, not run by CI; it supports the remarks only"
tags: [cycles, rotation-distance, half-defects, s-units, linear-programming, exact-certificates, frontier]
---

# At most six half-period mismatches force a three- or four-term relation with N/50 spare bits

## Statement

Use the raw odd-only map `x -> (3x+1)/2^v_2(3x+1)` on positive odd integers. For a positive word `w`,
`sum(w)` is its total, `len(w)` its length and `C_w` its intercept, as in
[`half-period-s-unit-approximation-law`](../half-period-s-unit-approximation-law/README.md): an orbit segment
with valuation word `w` from `u` to `v` satisfies `2^sum(w) v = 3^len(w) u + C_w`. The intercept does not
depend on the last letter of `w`. Throughout, `alpha = log_2 3`.

**Setting.** A positive odd integer cycle is read over `2N` odd steps. Its valuation word is `W = V V'` with
`len(V) = len(V') = N`, and `V`, `V'` differ in exactly `d >= 1` positions. Equivalently, `W` and its rotation
by `N` differ in exactly `2d` positions.

**Normal form** (section 1). After a cyclic rotation of `W`,

```
V  = b_0 b_1 ... b_(d-1),        b_k  = u_k (kappa_k + nu_k),
V' = b'_0 b'_1 ... b'_(d-1),     b'_k = u_k (kappa_k + nu'_k),
```

where `u_k` is a positive word, possibly empty, `kappa_k >= 1`, and one of `nu_k, nu'_k` is `0` while the other
is an integer `p_k >= 1`. Moreover a minimum of the cycle is the state before a letter of `b_0`. Put

```
B_k = len(u_k) + 1,      s_k = sum(u_k) + kappa_k,      B_0 + ... + B_(d-1) = N.
```

The states before the blocks are named

```
x_0 --b_0--> x_1 --b_1--> ... --b_(d-1)--> x_d = y_0 --b'_0--> y_1 --b'_1--> ... --b'_(d-1)--> y_d = x_0.
```

**Quotients and relations** (section 2). For `0 <= k < d` the number `g_k = (y_k - x_k)/2^(s_k)` is a nonzero
integer. With the conventions `g_d = -g_0` and `s_d = s_0`, for `0 <= k < d`:

```
(U_k)   3^(B_k) g_k = (2^(nu'_k) - 2^(nu_k)) x_(k+1) + 2^(nu'_k + s_(k+1)) g_(k+1),
(V_k)   3^(B_k) g_k = (2^(nu'_k) - 2^(nu_k)) y_(k+1) + 2^(nu_k  + s_(k+1)) g_(k+1).
```

Write any of these `2d` relations as `R: 3^(B_k) g_k = (2^(nu'_k) - 2^(nu_k)) xi + 2^c g_(k+1)` and put

```
T(R)   = max( 3^(B_k) |g_k| ,  2^c |g_(k+1)| ),
P_3(R) = |g_k| |g_(k+1)| (2^(p_k) - 1) xi,
P_4(R) = |g_k| |g_(k+1)| xi^2.
```

**Theorem.** Assume [EXT-1](../../../../sources/musson-collatz-gap-all.md). Let `N >= 2^22` and `1 <= d <= 3`.
Then some relation `R` among `(U_k)`, `(V_k)`, `0 <= k < d`, satisfies

```
P_3(R) <= 2^(-N/50) T(R)        or        P_4(R) <= 2^(-N/50) max( T(R), 2^(p_k) xi ).
```

**Complements.** (a) For `d = 1` the size constraints of section 3 are contradictory, so no such cycle has
`N >= 2^22`. (b) For `d = 2` some relation satisfies the first alternative, `P_3(R) <= 2^(-N/50) T(R)`.

**Reading.** `R` is a vanishing sum of the three integers `3^(B_k) g_k`, `-2^c g_(k+1)` and
`-(2^(nu'_k) - 2^(nu_k)) xi`. Splitting the last one as `-2^(nu'_k) xi + 2^(nu_k) xi` makes it a vanishing sum
of four integers. The part of each term that is coprime to 6 is at most `|g_k|`, `|g_(k+1)|` and
`(2^(p_k) - 1) xi`, or `xi` and `xi` after splitting. So `P_3(R)` and `P_4(R)` bound the product of the parts
coprime to 6, and the theorem says that for one relation this product is smaller than the largest term by a
factor `2^(N/50)`. [`half-period-six-mismatch-finiteness`](../half-period-six-mismatch-finiteness.md) feeds this
to a theorem of Evertse.

**Scope.** Both signs of every change and all letters are allowed. The theorem is a necessary condition. It
does not exclude a cycle. Complement (a) is the half-period case of
[`two-mismatch-exclusion-via-gap`](../two-mismatch-exclusion-via-gap/README.md), which is formal under its own
inputs; it is recorded here as a cross-check of the constraints. Four changed positions are not covered
(see the remarks).

## Proof

### 1. Normal form

Let `D` be the set of positions `i < N` with `V_i != V'_i`, so `D` has `d` elements. For `0 <= r <= N` the
rotation of `W` by `r` positions has the halves `V[r:] V'[:r]` and `V'[r:] V[:r]`. They differ exactly at the
positions `i - r` for `i` in `D` with `i >= r`, and `N - r + i` for `i` in `D` with `i < r`. Take
`r = max(D) + 1`: the last difference moves to position `N - 1`. So assume `N - 1` is in `D`. Cut both halves
after every position of `D`. This gives `V = b_0 ... b_(d-1)` and `V' = b'_0 ... b'_(d-1)`, where `b_k` and
`b'_k` have the same length and differ exactly in their last letter. Let `kappa_k` be the smaller of the two
last letters. This is the displayed form.

Rotating `W` further by `len(b_0) + ... + len(b_(j-1))` gives the halves `b_j ... b_(d-1) b'_0 ... b'_(j-1)`
and `b'_j ... b'_(d-1) b_0 ... b_(j-1)`, which have the same form with the `2d` block copies renumbered
cyclically. Rotating by `N` exchanges the halves. So any of the `2d` copies `b_0, ..., b_(d-1), b'_0, ...,
b'_(d-1)` can be made the first block. Every state of the cycle is the state before a letter of exactly one
copy. Choose a copy that contains a minimum of the cycle and make it the first block. The certificate tests
both rotations on random words (V4).

### 2. The quotients and the relations

The intercepts of `b_k` and `b'_k` are equal, since they share all letters but the last. Call it `C_k`. The
block equations are

```
2^(s_k + nu_k) x_(k+1) = 3^(B_k) x_k + C_k,        2^(s_k + nu'_k) y_(k+1) = 3^(B_k) y_k + C_k.      (1)
```

Subtracting,

```
3^(B_k) (y_k - x_k) = 2^(s_k) ( 2^(nu'_k) y_(k+1) - 2^(nu_k) x_(k+1) ).
```

Powers of 2 and 3 are coprime, so `g_k = (y_k - x_k)/2^(s_k)` is an integer and

```
3^(B_k) g_k = 2^(nu'_k) y_(k+1) - 2^(nu_k) x_(k+1),        0 <= k < d.                               (2)
```

Also `y_(k+1) - x_(k+1) = 2^(s_(k+1)) g_(k+1)` for `0 <= k < d`: for `k + 1 < d` this is the definition, and
for `k + 1 = d` it reads `x_0 - y_0 = -2^(s_0) g_0`, which is the convention `g_d = -g_0`, `s_d = s_0`.
Substituting `y_(k+1) = x_(k+1) + 2^(s_(k+1)) g_(k+1)` in (2) gives `(U_k)`. Substituting
`x_(k+1) = y_(k+1) - 2^(s_(k+1)) g_(k+1)` gives `(V_k)`.

**`g_k != 0`.** If `y_k = x_k`, the orbit from `x_k` and the orbit `N` odd steps later coincide, so `W` equals
its rotation by `N` and `V = V'`.

**Coprimality.** Every state is a positive odd integer, and it is coprime to 3 because it has the form
`(3u + 1)/2^v`.

### 3. Sizes

Let `M` be the minimum state, `ell = log_2 M`, `E = sum(W) = 2 (s_0 + ... + s_(d-1)) + p_0 + ... + p_(d-1)` and
`tau = E/2 - N alpha`.

- **Budget.** The product of `2^(w_i) = 3 + 1/x_i` over the cycle gives
  `2 tau = sum of log_2(1 + 1/(3 x_i)) > 0`, and each of the `2N` summands is below `1/(2M)`. So
  `0 < tau < N/(2M)`.
- **The minimum is large.** The certificate verifies that every odd `3 <= n < 2^17` reaches a smaller odd
  number (V1). The word of the trivial cycle is `(2, ..., 2)`, for which `V = V'`. So `M >= 2^17` and
  `tau < N/2^18`.
- **The minimum is small.** EXT-1, applied to the pair `(2N, E)`, gives
  `eta = 1 - 3^(2N)/2^E >= 1/(2^172 (2N)^341)`. Also `eta < -ln(1 - eta) = sum of ln(1 + 1/(3 x_i)) < 2N/(3M)`.
  Hence `M < 2^172 (2N)^342 / 3` and `ell < 514 + 342 log_2 N`. The right side divided by `N` decreases in `N`
  and is below `1/500` at `N = 2^22` (V1). So `ell < N/500`.
- **The first block.** The minimum is reached from `x_0` after `j <= B_0 - 1` letters of `u_0`, with total
  `t_j`. Then `2^(t_j) M >= 3^j x_0`, with equality only for `j = 0`. Each letter `w` has `2^w/3 < 2^(w-1)`, so
  `x_0 <= M 2^(t_j - j) <= M 2^(sum(u_0) - len(u_0)) <= M 2^(s_0 - B_0)`, because `kappa_0 >= 1`.
- **Block copies.** Number the copies `K = 0, ..., 2d - 1` in the order `b_0, ..., b_(d-1), b'_0, ...,
  b'_(d-1)`, cyclically, and let `z_K` be the state before copy `K`: `z_k = x_k` and `z_(k+d) = y_k`. Let
  `nu(K)` be `nu_k` for `K = k` and `nu'_k` for `K = k + d`. By (1), and since `3^B z + C` equals `3^B z`
  times the product of `1 + 1/(3 z')` over the `B` states `z'` before the letters of the copy,
  `log_2 z_(K+1) + s_k + nu(K) = B_k alpha + log_2 z_K + eta_K` with `0 < eta_K < B_k/(2M) <= N/2^18`.
- **Quotients.** `2^(s_k) |g_k| = |y_k - x_k| < max(x_k, y_k)`.

Divide everything by `N`:

```
b_k = B_k/N,   e_k = (s_k - B_k)/N,   pi_k = p_k/N,   G_k = log_2|g_k| / N,   Z_K = log_2(z_K) / N,
```

and `nubar(K) = nu(K)/N`, which is `pi_k` or `0`. All these numbers are nonnegative: every letter is at least 1,
so `s_k >= B_k`; the `g_k` are nonzero integers; the states are at least 1. The facts above become linear
constraints.

| Row | Constraint | From |
|---|---|---|
| L1 | `b_0 + ... + b_(d-1) = 1` | the blocks fill a half |
| L2 | `alpha <= sum of (b_k + e_k) + (1/2) sum of pi_k <= alpha + 2^-18` | budget, `tau < N/2^18` |
| L3 | `0 <= Z_(K+1) - Z_K - alpha b_K + b_K + e_K + nubar(K) <= 2^-18` for every copy `K` | block copies |
| L5 | `Z_0 <= e_0 + 1/500` | the first block and `ell < N/500` |
| L6 | `G_k + b_k + e_k <= max(Z_k, Z_(k+d))` | quotients |

In L3 the indices of `b` and `e` are read modulo `d` and those of `Z` modulo `2d`. Two families of signs make
every row linear: `eps_k = +1` if `nu'_k = p_k` and `-1` if `nu_k = p_k`, which decides `nubar(K)`; and
`rho_k = +1` if `y_k > x_k` and `-1` otherwise, which decides the maximum in L6 and adds the row
`Z_(k+d) >= Z_k` or `Z_k >= Z_(k+d)`. That is `4^d` cases.

### 4. What a failing relation says

Say that a relation `R` **fails** if both `P_3(R) > 2^(-N/50) T(R)` and
`P_4(R) > 2^(-N/50) max(T(R), 2^(p_k) xi)`. Let `Z_xi` be the normalised height of `xi`, and `chi = pi_k` if the
exponent `c` of `R` contains `p_k`, and `chi = 0` otherwise. Taking logarithms and dividing by `N`:

```
F3:   G_k + G_(k+1) + pi_k + Z_xi  >=  t - 1/50     for t = alpha b_k + G_k  and  t = chi + b_(k+1) + e_(k+1) + G_(k+1);
F4:   G_k + G_(k+1) + 2 Z_xi       >=  t - 1/50     for the same two t and for t = pi_k + Z_xi.
```

F3 uses `2^(p_k) - 1 < 2^(p_k)`. The exponent `c` contains `p_k` for `(U_k)` when `eps_k = +1` and for
`(V_k)` when `eps_k = -1`. Indices are read modulo `d` for `b, e, G` and modulo `2d` for the heights, in
agreement with the conventions `g_d = -g_0`, `s_d = s_0`, `x_d = y_0`, `y_d = x_0`.

### 5. The linear step

Fix `d` and the signs. Suppose all `2d` relations fail. Then the `6d` nonnegative numbers
`b_k, e_k, pi_k, G_k, Z_K` satisfy the rows L1, L2, L3, L5, L6, the sign rows and the rows F3, F4 of all
relations. Every row has the form `a . v <= c` with rational data once `alpha` is replaced by a rational
bound in the valid direction: where `alpha` multiplies `b_k >= 0`, the rows use
`15849/10000 < alpha < 158497/100000` (V1).

The certificate exhibits, for each of the `4 + 16 + 64 = 84` sign cases with `d = 1, 2, 3`, nonnegative
rational multipliers `lambda_i` such that the combination `sum of lambda_i a_i` has nonnegative coefficients
and `sum of lambda_i c_i < 0`. Applied to a solution `v >= 0` this gives
`0 <= (sum of lambda_i a_i) . v <= sum of lambda_i c_i < 0`. So the rows have no solution, and not all
relations fail. The multipliers are found by an exact simplex and then verified from scratch; only the
verification is part of the proof (V2). At most 13 rows carry a nonzero multiplier in any case.

This proves the theorem: some relation `R` does not fail, that is, `P_3(R) <= 2^(-N/50) T(R)` or
`P_4(R) <= 2^(-N/50) max(T(R), 2^(p_k) xi)`.

### 6. The complements

(a) For `d = 1` the certificate finds multipliers for the rows L1 to L6 and the sign rows alone, in all four
sign cases. (b) For `d = 2` it finds multipliers in all 16 sign cases when the rows F4 are removed. Then
"all relations have `P_3(R) > 2^(-N/50) T(R)`" is contradictory.

## Certificates

`check_local_relations.py`, standard library only, exact arithmetic for every decision, valid under
`python3 -O`:

- **V1** the two bounds for `alpha`, the descent of every odd `3 <= n < 2^17`, `(514 + 342*22)/2^22 <= 1/500`
  and the monotonicity condition, and the two size thresholds quoted in the finiteness node.
- **V2** the linear step: 84 sign cases, the four cases of complement (a) and the sixteen of complement (b).
  `--show d signs signs` prints the multipliers of one case, for instance `--show 2 ++ ++`, where seven rows
  suffice.
- **V3** 12000 actual cycles of `3x+q`, `q = 2^sum(W) - 3^(2N)`, built from random words of the normal form
  with `d = 1, 2, 3`: the divisibility `2^(s_k) | y_k - x_k`, `g_k != 0`, the identities (2), `(U_k)`,
  `(V_k)`, the inequality on quotients, the bound of the first block, and the rows L1, L3 (lower bound), L6 and
  the sign rows evaluated through the same indexing code as V2. The smallest value of `ell/N` among them is
  2.32, far above `1/500`: these cycles violate L5.
- **V4** the two rotations of section 1 on 3000 random words.

`explore_relation_families.py` is an exploration (numpy, scipy, floating point). It is not run by CI and
supports only the remarks below.

## Remarks

- **Where the map 3x+1 enters.** Rows L1, L3 (lower bound) and L6 hold for every `3x+q` cycle and are tested on
  actual ones. Rows L2, L3 (upper bound) and L5 use `q = 1`: the minimum is at least `2^17`, and, through
  EXT-1, at most a power of the length. Every one of the 84 certificates uses L5. The actual cycles of V3
  satisfy the addend-free rows and violate L5, so the theorem says nothing about them.
- **Why four terms.** In the normalised model of the exploration, the three-term alternative alone is forced
  for `d = 2` and is not forced for `d = 3`; adding longer three-term relations (states further along a track,
  quotients two or more blocks apart) does not change that. With the four-term alternative the conclusion is
  forced for `d = 3`. The model drops subexponential factors, so these statements are indications; the proved
  statements are the theorem and its complements.
- **Four changed positions.** In the same model the conclusion is not forced for `d = 4`: neither with the
  relations of the theorem, nor after adding the longer relations in three- and four-term form (receipt of the
  exploration). Whether relations with more terms reach `d = 4` is open.
- **Comparison with the earlier law.** For `d = 2`, in the notation `A B A[p] B[q]`, `h`, `j` of
  [`half-period-s-unit-approximation-law`](../half-period-s-unit-approximation-law/README.md), the four
  relations are `3^a h = (2^p - 1) z - 2^(sB+p) j`, `3^a h = (2^p - 1) t - 2^sB j`,
  `2^sA h - 3^b j = (2^q - 1) x` and `2^(sA+q) h - 3^b j = (2^q - 1) y`. That law used two longer relations,
  each over half a turn, and a hand proof with the constant `N/25`. Complement (b) is a second route to a
  three-term relation with spare bits for four mismatches, by different relations and with a machine-checked
  linear step.
- **What the rows cannot see.** The rows do not use the divisibility of `g_k` by powers of 3, the exact
  2-adic valuation of `y_k - x_k`, or any relation between different cycles. They are size constraints only.
- **Novelty.** Undetermined. Rotation distance and these quotients are this repository's notions; no
  literature search for this statement was made.

## History

- 2026-11-23: found and proved by the Claude cycles lane (Fable 5.2; directed by Santiago Armstrong). The
  linear step was first seen in a floating-point exploration and then replaced by exact certificates.
