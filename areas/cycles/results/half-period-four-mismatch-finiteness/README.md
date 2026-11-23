---
id: half-period-four-mismatch-finiteness
kind: result
title: Only finitely many 3x+1 cycles can have a half-period rotation with exactly four mismatches
status: written
claim: >
  Raw odd-only 3x+1 clock. Assume EXT-1 and Ridout's theorem. Then the set of positive odd integer cycles whose
  valuation word, read over an even number 2N of odd steps, differs from its rotation by N in exactly four
  positions is finite. Both parities of the two half-defects, both orders of their magnitudes and all letters
  are covered. With the non-half-period exclusion, also under EXT-1, at most finitely many nontrivial primitive
  positive integer cycles have a nonidentity rotation with exactly four mismatches. The proof is ineffective:
  Ridout's theorem, in the form cited, bounds neither N nor the number of exceptional cycles, so no particular
  cycle is excluded and the question rotation-distance-at-least-5 stays open. For 3x+d the argument is not transferred.
authors:
  - Claude cycles lane (Fable 5.2; directed by Santiago Armstrong)
created: 2026-11-23
depends_on: [half-period-s-unit-approximation-law, non-half-period-four-mismatch-exclusion]
assumes: [musson-collatz-gap-all, ridout-1958-p-adic-roth]
reviewed_by:
  - by: Claude review lane (Fable 5.2; fresh-context subagent with an adversarial brief; directed by Santiago Armstrong)
    date: 2026-11-23
    link: REVIEW-2026-11-23-claude-review-lane.md
    scope: "The size bounds, the coprimality and the p-adic absolute values, the match with both quoted forms of Ridout's theorem and with the two-variable p-adic subspace theorem, and the passage from finitely many rationals to finitely many cycles. Verdict: holds, with wording corrections, applied. The reviewer is a subagent launched and briefed by the authoring session, on the same model, with a fresh context; for that reason the status is left at written. Not checked: Ridout's original papers, EXT-1, and non-half-period-four-mismatch-exclusion, on which only the corollary rests"
tags: [cycles, rotation-distance, half-defects, s-units, ridout, finiteness, ineffective, frontier]
---

# Only finitely many 3x+1 cycles can have a half-period rotation with exactly four mismatches

## Statement

Use the raw odd-only map on positive odd integers. A cycle with `2N` odd steps has a valuation word `W` of
length `2N`. Call it a **half-period four-mismatch cycle** if `W` and its rotation by `N` differ in exactly four
positions.

**Theorem.** Assume [EXT-1](../../../../sources/musson-collatz-gap-all.md) and
[Ridout's theorem](../../../../sources/ridout-1958-p-adic-roth.md). Then there are only finitely many half-period
four-mismatch cycles of the `3x+1` map.

**Corollary.** Under the same two inputs, at most finitely many nontrivial primitive positive integer cycles
have a nonidentity rotation with exactly four mismatches. Indeed
[`non-half-period-four-mismatch-exclusion`](../non-half-period-four-mismatch-exclusion/README.md) shows, under
EXT-1, that such a rotation is the rotation by half the period.

**What this is not.** The theorem is ineffective. In the form cited, Ridout's theorem gives no bound on `N`
and no bound on the number of exceptional cycles. It does not show that the exceptional set is empty, so it does not settle
[`rotation-distance-at-least-5`](../../questions/rotation-distance-at-least-5.md). No cycle length is excluded.

## Proof

### 1. The input from the approximation law

Let a half-period four-mismatch cycle have half length `N >= 2^22`. By
[`half-period-s-unit-approximation-law`](../half-period-s-unit-approximation-law/README.md), after a cyclic
rotation its word is `A B A[p] B[q]`, and there are positive integers `c, U, V` with

```
0 < Theta = 2^c U - 3^N V,        Theta * V < 2^(c - N/25).            (1)
```

Here `U` is a state of the cycle, namely `x` or `t`, so `U` is odd and coprime to 3. `V` is `h` or `j`, a
positive integer, and `V` is odd: in `y - x = 2^sum(A) h` the two states have the same valuation word along `A`
up to its last letter, where they differ, so `v_2(y - x) = sum(A)` exactly; the same holds for `j`. The exponent
is `c = sum(B) + p + q` or `c = sum(A) + p`.

Three size bounds are needed. Let `E` be the total of `W`.

- **`c < 4N` and `U < 2^N`.** The cycle product gives `2^E = product of (3 + 1/x_i) < 4^(2N)`, and `c <= E`.
  Sections 6 and 7 of the approximation law show `log_2 U <= (alpha - 1) N + tau + ell - (p+q)/2`, which is
  below `N`.
- **`c > N/3`.** In Case I, `h >= 1` gives `y > 2^sum(A)`, hence
  `len(A) <= sum(A) < log_2 x + (p+q)/2 + tau <= (alpha - 1) N + 2 tau + ell`. So
  `len(B) > (2 - alpha) N - 2 tau - ell > N/3` and `c >= sum(B) >= len(B)`. Case II is symmetric:
  `z > 2^sum(B)` bounds `len(B)`, and `c >= sum(A) >= len(A) > N/3`.

The numerical steps use `alpha < 317/200`, `tau < N/2^18` and `ell < 514 + 342 log_2 N`. For
`2^k <= N < 2^(k+1)` with `k >= 22` they give `2 tau + ell < 2^(k-16) + 514 + 342 (k+1) < 2^k/20`; the
certificate of the approximation law checks this. Hence `log_2 U < (117/200 + 1/20) N < N` and
`(2 - alpha) N - 2 tau - ell > 73N/200 > N/3`.

### 2. A solution of Ridout's inequality

Let `g = gcd(U, V)` and put

```
P = 3^N V / g,        Q = 2^c U / g.
```

These are coprime: `U/g` and `V/g` are coprime, `V` is odd, and `U` is coprime to 3. By (1), `0 < Q - P` and
`Q - P = Theta/g < Q/2`, so `max(P, Q) = Q < 2P`. The 2-adic absolute value of `Q` is `2^(-c)`. The 3-adic
absolute value of `P` is at most `3^(-N)`. Therefore

```
Q * |Q - P| * |Q|_2 * |P|_3  <=  (2^c U / g)(Theta / g) / (2^c 3^N)
                              =  U Theta / (g^2 3^N)
                              <  U 2^(c - N/25) / (V 3^N)
                              =  (Q/P) * 2^(-N/25)
                              <  2^(1 - N/25).                          (2)
```

On the other hand `Q <= 2^c U < 2^(5N)`. Take `epsilon = 1/250`. Then `1/Q^epsilon > 2^(-N/50)`, and
`2^(1 - N/25) < 2^(-N/50)` because `N > 50`. So

```
Q * |Q - P| * |Q|_2 * |P|_3  <  1 / max(P, Q)^epsilon.                  (3)
```

This is the inequality of Ridout's theorem in the form recorded in the
[source node](../../../../sources/ridout-1958-p-adic-roth.md), with `alpha = beta = 1`, the linear form `q` at the
prime 2 and the linear form `p` at the prime 3. In Bilu's form it is the case `S = {infinity, 2, 3}` with
targets `1`, `infinity`, `0`: for `xi = P/Q < 1` the three factors are `|1 - xi| = (Q - P)/Q`,
`|1/xi|_2 = 2^(-c)` and `|xi|_3 <= 3^(-N)`, and `H(xi) = Q`.

### 3. Finiteness

By Ridout's theorem, only finitely many rationals `P/Q` satisfy (3). The reduced denominator of `P/Q` is
`Q = 2^c U/g` with `U/g` odd, so `P/Q` determines `c`. Hence only finitely many values of `c` occur, and
`N < 3c` is bounded. Together with the cycles of half length `N < 2^22`, all half-period four-mismatch cycles
have `N <= N_1` for some `N_1`. A cycle with `2N` odd steps has a word of length `2N` and total below `4N`.
There are finitely many such words, and a word determines at most one cycle. This proves the theorem.

## Remarks

- **Why Ridout is needed.** Inequality (1) says `0 < 1 - 3^N V/(2^c U) < 2^(-N/25)/(U V)`. Roth's theorem alone allows agreement up to `1/Q^2`, which is useless here because `Q`
  contains the huge powers. Ridout's theorem discounts the parts of `P` and `Q` that are powers of 2 and 3, so
  only the cofactors `U` and `V` count. This is the mechanism of Mahler's theorem on the fractional parts of
  `(3/2)^n`.
- **Ineffectivity.** Ridout's theorem, in the form cited, gives no bound on the solutions. An effective substitute
  would need a lower bound `|2^c U - 3^N V| > 2^(c - N/25)/V` for small cofactors. Baker-type bounds for three
  logarithms give only `|2^c U - 3^N V| > 2^c U / exp(K log N log max(U, V))` with a large constant `K`, which
  is far weaker when `U` or `V` is large. An explicit form of the abc conjecture would suffice. Neither route is
  claimed here.
- **Controls.** The argument does not exclude the actual cycles of `3x+5`, `3x+7`, `3x+13` or `3x+61`, nor the
  half-period four-mismatch cycles of `3x+47` and `3x+1631` replayed in the approximation law's certificate.
  The gap (1) comes from the bound of the minimum of a `3x+1` cycle by a power of its length. For `3x+d` that
  bound involves `d`, and no finiteness statement is made.
- **Status of the question.** Before this node the half-period case was an infinite open family, with partial
  exclusions listed in the question. Under EXT-1 and Ridout's theorem it is now a finite, non-explicit set of
  possible exceptions.
- **Reading for the rotation distance.** [`three-mismatch-exclusion`](../three-mismatch-exclusion/README.md) gives
  `rho(w) >= 4` for every hypothetical nontrivial cycle under its own inputs (EXT-1, Barina's verification and a
  period bound). Under those inputs and Ridout's theorem, `rho(w) >= 5` for all but finitely many nontrivial
  cycles. This reading is not part of the claim above.
- **Novelty.** Undetermined. Rotation distance is this repository's notion. The use of the p-adic Roth theorem
  for powers of 2 and 3 is classical (Mahler). No literature search for this application was made.

## History

- 2026-11-23: proved by the Claude cycles lane (Fable 5.2; directed by Santiago Armstrong).
- 2026-11-23, correction after merging. The status was merged as `reviewed` and is set back to `written`. The
  recorded review was made by a subagent that the authoring session launched and briefed. Whether that is
  "independent of the authoring session" in the sense of the contribution rules is left to the maintainer; the
  review itself stands and is kept in `reviewed_by`. The review file was replaced by the reviewer's final text,
  which includes an addendum. The claim and the proof are unchanged.
- 2026-11-23, later: [`non-half-period-four-mismatch-exclusion`](../non-half-period-four-mismatch-exclusion/README.md),
  on which only the corollary rests, was independently reviewed and holds. This node is unchanged.
