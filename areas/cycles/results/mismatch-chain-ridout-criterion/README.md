---
id: mismatch-chain-ridout-criterion
kind: result
title: A Ridout criterion along a chain of positions of a rotated 3x+1 cycle
status: written
claim: >
  Raw odd-only 3x+1 clock, positive odd integer cycle with m states x_i and letters w_i, positions taken modulo m,
  and a shift H; write x'_i = x_(i+H), w'_i = w_(i+H). Let i_0 be a position, n >= 0, i_r = i_0 + n, and let
  a >= 1 be such that the a-1 positions before i_0 have w = w'. Put xi = x_(i_0+1), xi' = x'_(i_0+1),
  zeta = x_(i_r+1), U = x'_(i_r+1), and let sigma, C and sigma', C' be the totals and intercepts of the words
  w_(i_0+1..i_r) and w'_(i_0+1..i_r). (a) Chain identity, valid for every such configuration:
  2^(w'_(i_0)) xi' - 2^(w_(i_0)) xi = 3^a G for an integer G, and
  3^(a+n) G = 2^(w'_(i_0)+sigma') U - 2^(w_(i_0)+sigma) zeta - (2^(w'_(i_0)) C' - 2^(w_(i_0)) C).
  (b) Criterion: assume w_(i_0) != w'_(i_0), let e = min(w_(i_0), w'_(i_0)), g = G/2^e (an odd integer),
  c = w'_(i_0) - e + sigma' and Theta = 2^c U - 3^(a+n) g, which equals
  2^(w_(i_0)-e) 3^n xi + 2^(w'_(i_0)-e) C' and is positive. Assume Ridout's theorem and fix epsilon > 0. Then only
  finitely many configurations (cycle, H mod m, i_0 mod m, n, a) satisfy U Theta < 3^(a+n) / (2^c U)^epsilon.
  (c) Two explicit sufficient forms when every position strictly between i_0 and i_r has w' >= w, with D' the
  sum of w' - w over those positions and Pi the product of 1 + 1/(3x) over the states x_(i_0+1), ..., x_(i_r):
  if w'_(i_0) > w_(i_0), it suffices that
  (1 + 2^(w'_(i_0) - w_(i_0) + D') (Pi - 1)) U xi < 3^a / (2^c U)^epsilon; if w'_(i_0) < w_(i_0) and n >= 1, it
  suffices that (2^(w_(i_0) - w'_(i_0)) + 2^(D') (Pi - 1)) U xi < 3^a / (2^c U)^epsilon. The two cases of
  half-period-s-unit-approximation-law are the instances with one further mismatch at i_r. The statement is
  ineffective and excludes no cycle. For 3x+d the identity holds with C, C' replaced by d C, d C'; part (b) is
  stated for d = 1 only.
authors:
  - Claude cycles lane (Fable 5.2; directed by Santiago Armstrong)
created: 2026-11-23
depends_on: [half-period-s-unit-approximation-law]
assumes: [ridout-1958-p-adic-roth]
certificates: [check_chain_criterion.py]
evidence:
  - "check_chain_criterion.json: the chain identity on every rotation, start, run length and end with n <= m of a deterministic family of actual 3x+d cycles, the reduced identity and the closed form of Theta at mismatched starts, the bounds of the two sufficient forms where they apply, and the two half-period configurations recomputed from the general definitions"
  - "explore_lp_half_period.py and explore_lp_half_period.json: a floating-point linear-programming exploration (numpy and scipy) of whether the elementary size constraints force a chain criterion for half-period words with 1, 2 or 3 changed positions. Exploration only, never run by CI, supports no claim"
  - "explore_referee_chain_test.py: the reviewer's own test of the identities (1965646 configurations of 2438 actual 3x+d cycles). Exploration, not run by CI"
reviewed_by:
  - by: Claude review lane (Fable 5.2; fresh-context subagent with an adversarial brief; directed by Santiago Armstrong)
    date: 2026-11-23
    link: REVIEW-2026-11-23-claude-review-lane.md
    scope: "Parts (a), (b), (c), (d) re-derived by hand and tested with a separate script. Verdict: holds, with corrections, all applied: the hypothesis of pattern (ii) made strict, redundant conditions removed, the certificate and the remarks reworded. The reviewer is a subagent launched and briefed by the authoring session, on the same model, so the status stays written. Not checked: Ridout's papers, EXT-1, the cited nodes' proofs, the model of the exploration"
tags: [cycles, rotation-distance, s-units, ridout, diophantine-approximation, tool]
---

# A Ridout criterion along a chain of positions of a rotated 3x+1 cycle

## Statement

Use the raw odd-only map on positive odd integers. A cycle has states `x_i` and letters `w_i`, indexed modulo
its number `m` of odd steps, with `2^(w_i) x_(i+1) = 3 x_i + 1`. Let `H` be a shift. Write

```
x'_i = x_(i+H),        w'_i = w_(i+H).
```

The primed sequence is the same cycle read `H` steps later. A position `l` is *matched* if `w_l = w'_l`.

**Configuration.** Choose a position `i_0`, an integer `n >= 0`, put `i_r = i_0 + n`, and choose an integer
`a >= 1` such that the `a - 1` positions `i_0 - a + 1, ..., i_0 - 1` are matched. Put

```
xi = x_(i_0+1),    xi' = x'_(i_0+1),    zeta = x_(i_r+1),    U = x'_(i_r+1),
sigma  = w_(i_0+1) + ... + w_(i_r),      C  = intercept of (w_(i_0+1), ..., w_(i_r)),
sigma' = w'_(i_0+1) + ... + w'_(i_r),    C' = intercept of (w'_(i_0+1), ..., w'_(i_r)),
```

with `sigma = sigma' = C = C' = 0` when `n = 0`. Intercepts are as in
[`half-period-s-unit-approximation-law`](../half-period-s-unit-approximation-law/README.md).

**(a) Chain identity.** There is an integer `G` with `2^(w'_(i_0)) xi' - 2^(w_(i_0)) xi = 3^a G`, and

```
3^(a+n) G = 2^(w'_(i_0) + sigma') U - 2^(w_(i_0) + sigma) zeta - (2^(w'_(i_0)) C' - 2^(w_(i_0)) C).      (1)
```

No hypothesis on the positions after `i_0` is needed.

**(b) Criterion.** Suppose `w_(i_0) != w'_(i_0)`. Then `H` is not a multiple of the primitive period. Let
`e = min(w_(i_0), w'_(i_0))`. Then `g = G/2^e` is an odd integer. Put

```
c = w'_(i_0) - e + sigma',
Theta = 2^c U - 3^(a+n) g = 2^(w_(i_0) - e) 3^n xi + 2^(w'_(i_0) - e) C'.
```

`Theta` is a positive integer. Assume [Ridout's theorem](../../../../sources/ridout-1958-p-adic-roth.md) and fix
`epsilon > 0`. Then only finitely many configurations `(cycle, H mod m, i_0 mod m, n, a)` satisfy

```
U * Theta < 3^(a+n) / (2^c U)^epsilon.                                                        (2)
```

Inequality (2) forces `g >= 1` and `c >= 1`.

**(c) Two sufficient forms.** Suppose every position `l` with `i_0 < l < i_r` has `w'_l >= w_l`. Let `D'` be the
sum of `w'_l - w_l` over those positions, and `Pi` the product of `1 + 1/(3 x_l)` over `l = i_0+1, ..., i_r`
(`Pi = 1` if `n = 0`).

| Pattern | Hypothesis at `i_0` | Sufficient for (2) |
|---|---|---|
| (i) | `w'_(i_0) > w_(i_0)` | `(1 + 2^(w'_(i_0) - w_(i_0) + D') (Pi - 1)) * U * xi < 3^a / (2^c U)^epsilon` |
| (ii) | `w'_(i_0) < w_(i_0)` and `n >= 1` | `(2^(w_(i_0) - w'_(i_0)) + 2^(D') (Pi - 1)) * U * xi < 3^a / (2^c U)^epsilon` |

In words: `U` is the primed state at the end of the chain, `xi` the unprimed state at its start, and `a - 1` the
length of the common run before the chain. The criterion holds when the product `U xi`, with the displayed
factor, is still much smaller than `3^a`.

**(d) The half-period law is an instance.** For `W = A B A[p] B[q]` and `H = N`, Case I of the approximation
law is pattern (i) with `i_0` the last position of the first `A` and `i_r` the last position of the first `B`.
Case II is pattern (ii) with `i_0` the last position of the copy `B[q]` and `i_r` the last position of the next
copy of `A`. Section 4 gives the dictionary.

**Scope.** Part (a) is an identity. Parts (b) and (c) are finiteness statements without a bound. They exclude no
cycle. They do not say that a configuration satisfying (2) exists: for a given class of cycles that is a separate
size statement, proved so far only in the half-period four-mismatch case (under EXT-1, for `N >= 2^22`).

## Proof

### 1. The chain identity

For every position `l`, subtracting the two step equations gives

```
2^(w'_l) x'_(l+1) - 2^(w_l) x_(l+1) = 3 (x'_l - x_l).                                        (3)
```

On a matched position this is `x'_(l+1) - x_(l+1) = 3 (x'_l - x_l)/2^(w_l)`. Apply it along the `a - 1` matched
positions before `i_0`, with `V` their total and `u = x'_(i_0-a+1) - x_(i_0-a+1)`:
`2^V (x'_(i_0) - x_(i_0)) = 3^(a-1) u`. Then (3) at `i_0` gives
`2^V (2^(w'_(i_0)) xi' - 2^(w_(i_0)) xi) = 3^a u`. Powers of 2 and 3 are coprime, so `3^a` divides
`2^(w'_(i_0)) xi' - 2^(w_(i_0)) xi`. This defines `G`.

The two tracks from `i_0 + 1` to `i_r + 1` satisfy `2^sigma zeta = 3^n xi + C` and `2^(sigma') U = 3^n xi' + C'`.
Multiply the definition of `G` by `3^n` and substitute `3^n xi' = 2^(sigma') U - C'` and
`3^n xi = 2^sigma zeta - C`. This is (1).

### 2. The criterion

Let `w_(i_0) != w'_(i_0)`. If `H` were a multiple of the primitive period, the primed and unprimed letters
would agree everywhere. In `G/2^e = (2^(w'_(i_0)-e) xi' - 2^(w_(i_0)-e) xi)/3^a`, exactly one of the two
exponents is zero and the states are odd, so `g` is an odd integer. Dividing (1) by `2^e` gives
`3^(a+n) g = 2^c U - Theta` with

```
Theta = 2^(w_(i_0) - e + sigma) zeta + 2^(w'_(i_0) - e) C' - 2^(w_(i_0) - e) C
      = 2^(w_(i_0) - e) 3^n xi + 2^(w'_(i_0) - e) C',
```

by `2^sigma zeta - C = 3^n xi`. So `Theta` is a positive integer.

Assume (2). Then `U Theta < 3^(a+n)`.

- If `g <= -1` then `Theta = 2^c U + 3^(a+n) |g| > 3^(a+n)`, which is impossible. As `g` is odd, `g >= 1`, so
  `0 < 3^(a+n) g < 2^c U`.
- If `c = 0` then `U = 3^(a+n) g + Theta > 3^(a+n)`, which is impossible. So `c >= 1`.

Let `k = gcd(U, g)` and

```
P = 3^(a+n) g / k,        Q = 2^c U / k.
```

`U` is a cycle state, so it is odd and coprime to 3, and `g` is odd. Hence `P` and `Q` are coprime, `0 < P < Q`,
`|Q|_2 = 2^(-c)` and `|P|_3 <= 3^(-(a+n))`. Therefore

```
Q * |Q - P| * |Q|_2 * |P|_3  <=  (2^c U / k)(Theta / k) / (2^c 3^(a+n))  <=  U Theta / 3^(a+n)
                              <   1/(2^c U)^epsilon  <=  1/max(P, Q)^epsilon.
```

This is the inequality of Ridout's theorem, in the form used in
[`half-period-four-mismatch-finiteness`](../half-period-four-mismatch-finiteness/README.md). So only finitely
many rationals `P/Q` arise. Fix one. Its reduced denominator `2^c U/k` determines `c` and `U/k`. Its numerator
shows `a + n <= v_3(P)`, so `a` and `n` are bounded. Finally `U <= U Theta < 3^(a+n)`, so `U` is bounded. A cycle
is determined by any one of its states, and for one cycle and bounded `a`, `n` there are finitely many
configurations. This proves (b).

### 3. The two sufficient forms

Let every position strictly between `i_0` and `i_r` have `w'_l >= w_l`. Each term of an intercept is
`3^(n-1-k) 2^(prefix total before position k)`, and only the letters at `i_0 + 1, ..., i_r - 1` enter these
prefix totals. The primed prefix totals exceed the unprimed ones by at most `D'`, so

```
C <= C' <= 2^(D') C.                                                                          (4)
```

Also `2^sigma zeta = 3^n xi + C = 3^n xi * Pi`, by the product of the step equations along the unprimed track.
Hence `C = 3^n xi (Pi - 1)`.

**Pattern (i).** Here `e = w_(i_0)` and `delta = w'_(i_0) - w_(i_0) >= 1`. The closed form of section 2 reads
`Theta = 3^n xi + 2^delta C'`. By (4), `Theta <= 3^n xi (1 + 2^(delta + D') (Pi - 1))`.

**Pattern (ii).** Here `e = w'_(i_0)` and `delta = w_(i_0) - w'_(i_0) >= 1`. The closed form reads
`Theta = 2^delta 3^n xi + C'`. By (4), `Theta <= 3^n xi (2^delta + 2^(D') (Pi - 1))`.

In both patterns multiply by `U`: the displayed strict hypothesis gives (2).

### 4. The half-period instances

Let `W = A B A[p] B[q]`, with the notation of the approximation law, positions `0, ..., 2N - 1` and `H = N`.
This word is primitive, so `m = 2N`.

- **Case I.** `i_0 = a - 1`, `i_r = N - 1`, run length `a - 1`. Then `w_(i_0)` is the last letter of `A` and
  `w'_(i_0)` is larger by `p`: pattern (i) with `delta = p`, `D' = 0`. The states are `xi = z`, `xi' = t`,
  `zeta = y`, `U = x`, and `sigma = sum(B)`, `sigma' = sum(B) + q`, `C = C' = C_B`. So `c = sum(B) + p + q`,
  `g = h` and `Theta = 2^sum(B) y + (2^p - 1) C_B`.
- **Case II.** `i_0 = 2N - 1`, `i_r = 2N - 1 + a`, run length `b - 1`. Then `w_(i_0)` is the last letter of
  `B[q]` and `w'_(i_0)` is smaller by `q`: pattern (ii) with `delta = q`, `D' = 0`. The states are `xi = x`,
  `xi' = y`, `zeta = z`, `U = t`, and `sigma = sum(A)`, `sigma' = sum(A) + p`, `C = C' = C_A`. So
  `c = sum(A) + p`, `g = j` and `Theta = 3^a 2^q x + C_A`.

These are the two identities of the approximation law.

## Certificates

[`check_chain_criterion.py`](check_chain_criterion.py) uses exact integer arithmetic.

- **V1.** On a deterministic family of actual `3x+d` cycles with distinct states, for every shift, every start
  `i_0`, every admissible run length `a - 1` and every end with `n <= m`: the divisibility by `3^a` and the
  identity (1) with `C, C'` replaced by `d C, d C'`. At a mismatched start: the oddness of `g`, the reduced
  identity `2^c U - 3^(a+n) g = Theta`, the closed form of `Theta` and its positivity. Where the patterns apply:
  the comparison (4) and the two estimates of section 3.
- **V2.** On actual `3x+d` cycles with word `A B A[p] B[q]`, the two configurations of section 4 are recomputed
  from the general definitions and compared with `c`, `h` or `j`, the four states and the right sides of the
  identities of the approximation law.

```
python3 areas/cycles/results/mismatch-chain-ridout-criterion/check_chain_criterion.py
```

The receipt is [`check_chain_criterion.json`](check_chain_criterion.json), regenerated with `--write-receipt`.
The finite checks support the identities. Part (b) rests on Ridout's theorem and is not checked numerically.

## Remarks

- **Reading.** With `n = 0` and `w'_(i_0) > w_(i_0)`, `Theta = xi`, and (b) says: apart from finitely many
  configurations, the two states right after a mismatch that follows a common run of `a - 1` positions have
  product at least `3^a / (2^c U)^epsilon`, with `U` the state on the track of the larger letter. For longer
  chains: after a long common run, a mismatch, and further mismatches where the primed track keeps the larger
  letters, the primed state at the end and the unprimed state at the start cannot both be small.
- **How the amplitudes on the way enter.** Only through the factors `1 + 2^(delta + D') (Pi - 1)` and
  `2^delta + 2^(D') (Pi - 1)`, where `Pi - 1 = C/(3^n xi)`. These factors are close to 1 and to `2^delta` when
  the unprimed states of the chain are large compared with `2^(delta + D')` and `2^(D')`.
- **A programme for more mismatches.** A rotation with `s` mismatches has at most `s^2` chains that start at a
  mismatch, take its whole common run and end at a mismatch. Finiteness of the cycles with such a rotation would
  follow from a size argument showing that, for large `m`, one of these chains satisfies a sufficient form with a
  fixed `epsilon`. The half-period four-mismatch case is the only one where this is proved. See
  [`rotation-distance-finite-exceptions`](../../questions/rotation-distance-finite-exceptions.md).
- **An exploration, not a result.** [`explore_lp_half_period.py`](explore_lp_half_period.py) writes the size
  constraints of a half-period word as linear inequalities in normalised variables and asks a
  linear-programming solver whether every chain criterion can fail at once. It uses the cruder cost
  `2^(delta + D')` for both patterns. It needs numpy and scipy, because it calls a solver, and it uses floating
  point. With one or two changed positions between the halves it finds no feasible case, in agreement with the
  approximation law. With three changed positions 54 of its 192 cases stay feasible. So the constraints used
  here do not by themselves force a criterion for six mismatches. The model is a relaxation written for this
  exploration. Its output proves nothing.
- **Controls.** The identity holds for every `3x+d` cycle. Part (b) uses that `U` is coprime to 6 and that the
  equation has addend 1, and it is a finiteness statement. It contradicts no actual cycle of `3x+5`, `3x+7`,
  `3x+13` or `3x+61`. An individual cycle of some `3x+d` can satisfy an inequality of the shape (2); the review
  file records one.
- **Novelty.** Undetermined.

## History

- 2026-11-23: derived by the Claude cycles lane (Fable 5.2; directed by Santiago Armstrong) as the general form
  of the two identities of the half-period approximation law. Corrected before merging after the review
  recorded in `reviewed_by`: strict hypotheses in (c), the sharper factor in pattern (i), and the removal of
  conditions in (2) that are automatic.
