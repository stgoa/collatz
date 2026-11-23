---
id: half-period-six-mismatch-finiteness
kind: result
title: Only finitely many 3x+1 cycles can have a half-period rotation with at most six mismatches
status: written
claim: >
  Raw odd-only 3x+1 clock. Assume EXT-1 and Evertse's theorem on vanishing sums of integers with small parts
  outside a fixed set of primes (his Corollary 1, with the primes 2 and 3 and three or four terms). Then the set
  of positive odd integer cycles whose valuation word, read over an even number 2N of odd steps, differs from
  its rotation by N in exactly two, four or six positions is finite. The new case is six. All signs and sizes of
  the three changes and all letters are covered. The proof is ineffective: the theorem cited bounds neither N
  nor the number of exceptional cycles, so no particular cycle is excluded. Rotations other than the rotation by
  half the period are not treated, so this does not decide whether finitely many cycles have rotation distance
  at most six, nor five. For 3x+q the argument is not transferred.
authors:
  - Claude cycles lane (Fable 5.2; directed by Santiago Armstrong)
created: 2026-11-23
depends_on: [half-period-six-mismatch-local-law]
assumes: [musson-collatz-gap-all, evertse-1984-sums-of-s-units]
tags: [cycles, rotation-distance, half-defects, s-units, subspace-theorem, finiteness, ineffective, frontier]
---

# Only finitely many 3x+1 cycles can have a half-period rotation with at most six mismatches

## Statement

Use the raw odd-only map on positive odd integers. A cycle read over `2N` odd steps has a valuation word `W`
of length `2N`. The rotation of `W` by `N` differs from `W` in an even number `2d` of positions, where `d` is
the number of positions in which the two halves of `W` differ.

**Theorem.** Assume [EXT-1](../../../sources/musson-collatz-gap-all.md) and
[Evertse's theorem](../../../sources/evertse-1984-sums-of-s-units.md). Then there are only finitely many
positive odd integer cycles of the `3x+1` map for which, for some `N`, the word read over `2N` odd steps
differs from its rotation by `N` in exactly `2d` positions with `1 <= d <= 3`.

**What is new.** The case `d = 3`, six mismatches. For `d = 1` there is no such cycle with `N >= 2^22`, a
known exclusion. For `d = 2` the statement is
[`half-period-four-mismatch-finiteness`](half-period-four-mismatch-finiteness/README.md); the present proof
reaches it by different relations.

**What this is not.** The theorem is ineffective. It gives no bound on `N` and no bound on the number of
exceptional cycles, and it does not show that the exceptional set is empty. It treats only the rotation by half
the length. A rotation with five mismatches is never of this kind, and a rotation with six mismatches need not
be. So the cases `s = 5` and `s = 6` of
[`rotation-distance-finite-exceptions`](../questions/rotation-distance-finite-exceptions.md) stay open.

## Proof

### 1. The input from the local law

Let a cycle be as in the theorem with `N >= 2^22`. By
[`half-period-six-mismatch-local-law`](half-period-six-mismatch-local-law/README.md), after a cyclic rotation
there are an index `k`, nonzero integers `g = g_k` and `g' = g_(k+1)`, a state `xi` of the cycle, integers
`B = B_k >= 1`, `c >= 1`, `p = p_k >= 1` and a sign such that

```
3^B g - 2^c g' = +-(2^p - 1) xi,                                                 (1)
```

and, with `T = max(3^B |g|, 2^c |g'|)`,

```
(A)   |g| |g'| (2^p - 1) xi <= 2^(-N/50) T,        or        (B)   |g| |g'| xi^2 <= 2^(-N/50) max(T, 2^p xi).
```

Here `(2^(nu'_k) - 2^(nu_k)) = +-(2^p - 1)`, because one of the two exponents is 0 and the other is `p`. The
state `xi` is odd and coprime to 3.

**Sizes.** Let `M` be the minimum of the cycle. By section 3 of the local law, `M >= 2^17` and
`log_2 M < N/500`. Going forward from a minimum, each odd step multiplies a state by at most `(3 + 1/M)/2`, so
every state is below `M (3/2)^(2N) (1 + 1/(3M))^(2N)`. Here `(3/2)^(2N) < 2^(1.17 N)` and
`(1 + 1/(3M))^(2N) < 2^(N/M) <= 2^(N/2^17)`, so every state is below `2^(1.2 N)`. A letter `w` read at a state
`u` has `2^w <= 3u + 1`, so every letter, and in particular `p`, is below `1.2 N + 2 < 2N`. Also
`2^(s_k) |g_k| = |y_k - x_k| < 2^(1.2 N)`. Therefore

```
3^B |g| < 3^N 2^(1.2 N) < 2^(3N),     2^c |g'| <= 2^p |y_(k+1) - x_(k+1)| < 2^(3N),     2^p xi < 2^(3N).      (2)
```

### 2. Three terms

Suppose (A) holds. Put `x_0 = 3^B g`, `x_1 = -2^c g'`, `x_2 = -+(2^p - 1) xi`, so `x_0 + x_1 + x_2 = 0` by (1).
All three are nonzero, so no proper subsum vanishes. Let `D` be their greatest common divisor. It divides the
odd number `x_2`. Write `D = 3^j D'` with `D'` coprime to 6. Since `xi` is coprime to 3, `3^j` divides
`2^p - 1`, and `v_3(2^p - 1) <= 1 + v_3(p)`, so `3^j <= 3p < 6N`.

For an integer `u`, let `[u]` be the part of `|u|` coprime to 6; this is `|u| |u|_2 |u|_3`. Then
`[x_0/D] = [g]/D'`, `[x_1/D] = [g']/D'` and `[x_2/D] <= (2^p - 1) xi / D'`. The largest of the `|x_i|/D` is
at least `T/D`. By (A),

```
[x_0/D] [x_1/D] [x_2/D]  <=  |g| |g'| (2^p - 1) xi / D'^3  <=  2^(-N/50) T / D'^3
                         <=  2^(-N/50) 3^j (T/D)  <  6N 2^(-N/50) max_i |x_i/D|.
```

For `N >= 2^22`, `6N < 2^(N/100)` (the certificate of the local law checks the instance `N = 2^22`). Put
`H = max_i |x_i/D|`. Then the product of the parts coprime to 6 is below `2^(-N/100) H`. It is at least 1, so
`H > 2^(N/100)`. By (2), `H < 2^(3N)`, so `2^(-N/100) < H^(-1/300)` and

```
product over i of |x_i/D| |x_i/D|_2 |x_i/D|_3  <  H^(299/300).                   (3)
```

### 3. Four terms

Suppose (B) holds. Split the last term of (1): `x_0 = 3^B g`, `x_1 = -2^c g'`, and `x_2, x_3` equal to
`-2^(nu'_k) xi` and `+2^(nu_k) xi`. One of them is `+-xi` and the other `-+2^p xi`. Their sum is zero by (1).

**No proper subsum vanishes.** Single terms are nonzero. A subsum of three terms vanishes only if the fourth
term is zero. `x_2 + x_3 = +-(2^p - 1) xi` is not zero, and then `x_0 + x_1` is not zero either. If `x_0`
cancelled against `x_2` or `x_3`, then `3^B` would divide a power of 2 times `xi`; this is impossible because
`B >= 1` and `xi` is coprime to 3. The two remaining pairs are the complements of these.

**Common divisor.** The greatest common divisor `D` of the four terms divides `xi`, so it is coprime to 6 and
it divides `g` and `g'`. Hence `[x_0/D] = [g]/D`, `[x_1/D] = [g']/D`, `[x_2/D] = [x_3/D] = xi/D`, and by (B)

```
product of the four parts  <=  |g| |g'| xi^2 / D^4  <=  2^(-N/50) max(T, 2^p xi) / D  =  2^(-N/50) H,
```

with `H = max_i |x_i/D|`. As before `H > 2^(N/50)` and `H < 2^(3N)`, so (3) holds for the four terms.

### 4. Finiteness

Apply Corollary 1 of the [source](../../../sources/evertse-1984-sums-of-s-units.md) with `S_0 = {2, 3}`, `c = 1`,
`d = 299/300`, once with `n = 2` and once with `n = 3`. The tuples `(x_i/D)` of sections 2 and 3 are integer
tuples with sum zero, no vanishing proper subsum and greatest common divisor 1, and they satisfy its
inequality (12) by (3). So they belong to a finite set. Let `H*` be the largest term occurring in that set.
Every cycle of the theorem with `N >= 2^22` yields a tuple with `2^(N/100) < H <= H*`. Hence `N` is bounded:
together with the cycles of half length below `2^22`, all cycles of the theorem have `N <= N_1` for some `N_1`.
A cycle read over `2N` odd steps has a word of length `2N` and total below `4N`, because the product of
`2^(w_i) = 3 + 1/x_i` is below `4^(2N)`. There are finitely many such words, and a word determines at most one
cycle. This proves the theorem.

## Remarks

- **Why more than three terms.** For four mismatches a three-term relation always has spare bits, and Ridout's
  theorem is enough. For six mismatches the local law may deliver only alternative (B), in which the state `xi`
  is counted twice and the factor `2^p - 1` is not counted at all. That is a vanishing sum of four integers
  with small parts coprime to 6, which is the setting of Evertse's theorem and of the p-adic subspace theorem
  behind it.
- **Ineffectivity.** The cited theorem gives no bound for the tuples. An effective version of this result
  would need an explicit lower bound for sums `3^B g - 2^c g' -+ 2^p xi +- xi` in terms of the cofactors. None
  is claimed.
- **Controls.** The argument does not exclude any actual cycle of `3x+5`, `3x+7`, `3x+13` or `3x+61`. The
  local law rests on the bound of the minimum of a `3x+1` cycle by a power of its length. For `3x+q` that bound
  involves `q`, and no finiteness statement is made. The certificate of the local law replays the identities on
  12000 actual `3x+q` cycles of the relevant shapes; all of them violate the bound on the minimum.
- **Reading for the rotation distance.** This removes one of the two obstacles to the case `s = 6` of
  [`rotation-distance-finite-exceptions`](../questions/rotation-distance-finite-exceptions.md): half-period
  rotations. Rotations with five mismatches, and rotations with six mismatches that are not the rotation by half
  the period, are not treated by any node. For four mismatches the non-half-period rotations were excluded by a
  separate size argument
  ([`non-half-period-four-mismatch-exclusion`](non-half-period-four-mismatch-exclusion/README.md)); nothing of
  that kind is known here for five or six.
- **Eight mismatches.** The local law is not available for four changed positions, and an exploration with
  longer relations did not find a forced relation there. The method of this node stops at six.
- **Novelty.** Undetermined. No literature search for this application was made.

## History

- 2026-11-23: proved by the Claude cycles lane (Fable 5.2; directed by Santiago Armstrong).
