---
id: mersenne-boundary-exact-divisibility
kind: result
title: Mersenne block endpoint equations force two exact powers of two
status: written
claim: >
  Integer affine equations for raw odd-only 3x+d valuation words.
  Let A,B be lists of natural exponents, a=len(A), b=len(B),
  P=sum(A), T=sum(B), J>r>=1, N=2^J, L=2^r, p=J-r,
  and C_A,C_B the standard additive-one word intercepts. For odd
  integers q,h,z,Y and an integer X, the four signed and
  changed-final-valuation endpoint equations in either Mersenne
  order imply both displayed boundary identities and exact binary
  divisibility. In high-to-low order, assuming p<=P and r<=T,
  the exact powers are P-p for (N-1)X+qh and T-r for
  (L-1)Y-qz. In low-to-high order, assuming J<=T, they are
  P for (L-1)X+qh and T-J for (N-1)Y-qz. Exact means
  divisibility by 2^k and failure of divisibility by 2^(k+1).
  Each target is nonzero and has absolute value at least 2^k.
  The final identities are derived from block endpoint equations,
  not assumed. No positivity, cycle existence, denominator-one,
  logarithmic-gap or cycle-exclusion hypothesis or conclusion is used.
authors:
  - Codex signed-endpoint formalisation lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
assumes: [mathlib-065356127b1d]
lean:
  - LeanLane.MersenneBoundaries.high_low_boundaries
  - LeanLane.MersenneBoundaries.low_high_boundaries
  - LeanLane.MersenneBoundaries.ExactTwoPower.ne_zero
  - LeanLane.MersenneBoundaries.ExactTwoPower.le_abs
  - LeanLane.MersenneBoundaries.negative_difference_control
evidence:
  - "../../../../lean/receipts/MersenneBoundaries.build.txt: pinned library build including the new module"
  - "../../../../lean/receipts/MersenneBoundaries.axioms.txt: axiom audit of every new theorem"
  - "../../../../lean/receipts/MersenneBoundaries.sha256.txt: compiled source hash"
tags: [cycles, half-defects, signed-orbits, divisibility, parity, lean]
---

# Mersenne block endpoint equations force two exact powers of two

## Statement

For a list `W` of natural exponents, let `C_W` be the usual
integer additive-one intercept, defined by

```
C_[]=0,       C_(e::W)=3^len(W)+2^e*C_W.
```

Thus a word with additive parameter `d` has affine endpoint
equation `2^sum(W)*y=3^len(W)*x+d*C_W`. Natural exponents
may be zero in this algebraic theorem; positive odd-only
valuation words are included. No claim about intermediate
states follows merely from the terminology "endpoint".

Let `A,B` be two such words and put

```
a=len(A), P=sum(A), b=len(B), T=sum(B),
J>r>=1, p=J-r, N=2^J, L=2^r.
```

Let `q,h,z,Y` be odd integers and `X` an integer. In the
cycle application, `X=q*x` and `Y=q*y` are cleared positive
odd states, while the signed segments join `-h -> z -> h`.
The theorem itself needs no positivity or cycle assumption.

For an integer `t`, define

```
ExactTwoPower(k,t) := 2^k divides t and 2^(k+1) does not divide t.
```

**High-to-low order.** Suppose `p<=P`, `r<=T`, and the four
block endpoint equations are

```
2^P*z = -3^a*h+(N-1)C_A,
2^(P-p)*Y = 3^a*X+q*C_A,
2^T*h = 3^b*z+(L-1)C_B,
2^(T-r)*(N*X+q*h) = 3^b*Y+q*C_B.                  (1)
```

Then

```
3^a*((N-1)X+q*h)
  =2^(P-p)*((N-1)Y-2^p*q*z),
ExactTwoPower(P-p, (N-1)X+q*h),

3^b*((L-1)Y-q*z)
  =2^(T-r)*(N*(L-1)X-q*h),
ExactTwoPower(T-r, (L-1)Y-q*z).                     (2)
```

**Low-to-high order.** Suppose `J<=T`, and instead

```
2^P*z = -3^a*h+(L-1)C_A,
2^(P+p)*Y = 3^a*X+q*C_A,
2^T*h = 3^b*z+(N-1)C_B,
2^(T-J)*(L*X+q*h) = 3^b*Y+q*C_B.                  (3)
```

Then

```
3^a*((L-1)X+q*h)
  =2^P*((L-1)*2^p*Y-q*z),
ExactTwoPower(P, (L-1)X+q*h),

3^b*((N-1)Y-q*z)
  =2^(T-J)*(L*(N-1)X-q*h),
ExactTwoPower(T-J, (N-1)Y-q*z).                     (4)
```

Every target in the four exact-divisibility statements is
nonzero and has absolute value at least the displayed power
of two. The theorem imposes no sign on either start difference.

## Proof

In each order, multiply the signed first endpoint equation
by `q` and subtract the modified first equation multiplied
by the first Mersenne addend. The intercept cancels. Use
`2^P=2^(P-p)*2^p` in high-to-low order and
`2^(P+p)=2^P*2^p` in low-to-high order. This gives the first
identity in (2) or (4).

Do the same with the signed and modified second equations,
using the second Mersenne addend. The term from the shifted
endpoint simplifies to `-q*h` because that addend is one
less than the corresponding power of two. This gives the
second identity in (2) or (4). In particular these difference
identities are conclusions of (1) or (3).

In the high-to-low first identity, `(N-1)Y` is odd and
`2^p*q*z` is even. In the low-to-high first identity,
`(L-1)*2^p*Y` is even and `q*z` is odd. In both second
identities the first term of the right bracket is even and
`q*h` is odd. Every right bracket is therefore odd.

If `3^e*t=2^k*u` with `u` odd, coprimality of 2 and 3
first gives `2^k|t`. Were `2^(k+1)|t`, canceling `2^k`
would make `u` even, a contradiction. This proves each exact
power. Such a target cannot be zero, because every power
of two divides zero. Finally, a nonzero integer divisible
by `2^k` has absolute value at least `2^k`.

## Lean

Build from `lean/` with `lake build LeanLane`. From the
repository root, run `python3 tools/check_lean_receipts.py`
to check the recorded source hashes and permitted axioms.
The axiom receipt contains the new module's eight reports
from the completed library build; build receipts omit elapsed
durations and retain the command, pins and successful result.

The module
[`LeanLane/MersenneBoundaries.lean`](../../../../lean/LeanLane/MersenneBoundaries.lean)
uses the actual shared `LeanLane.Words.C`, `List.sum` and
`List.length`. The word endpoint hypotheses in (1) and (3)
are the hypotheses of `high_low_boundaries` and
`low_high_boundaries`. Each theorem returns both identities
and both `ExactTwoPower` statements in (2) or (4).

The formal hypotheses are slightly weaker than the common
statement above: high-to-low does not need `z` odd, and
low-to-high does not need `Y` odd. Neither requires `X` odd.
The application supplies all these parity conditions, so
there is no additional assumption in the formal version.
The inequalities on the totals prevent truncated natural
subtraction from changing the endpoint exponents.

`ExactTwoPower.ne_zero` and `ExactTwoPower.le_abs` give the
nonzero and absolute-value conclusions. The helper
`exact_two_power_of_ternary_eq` proves the cancellation
argument; its assumption is used only after the main
theorems derive the boundary identities from the endpoint
equations. The two remaining helpers establish parity of
positive powers of two and their Mersenne predecessors.

The module is imported by `LeanLane.lean`; the
[library-root receipt](../../../../lean/receipts/LeanLane.build.txt)
and [root hash](../../../../lean/receipts/LeanLane.sha256.txt)
bind that import to the same build. Its
[build receipt](../../../../lean/receipts/MersenneBoundaries.build.txt),
[axiom receipt](../../../../lean/receipts/MersenneBoundaries.axioms.txt)
and [source hash](../../../../lean/receipts/MersenneBoundaries.sha256.txt)
record the pinned compilation and standard axioms. The
[Mathlib source](../../../../sources/mathlib-065356127b1d.md)
is the sole external input; LMN is not used.

This node is a formalisation of the stated algebraic bridge.
It does not formalise the existence or reconstruction of
the signed segments, the positive state enclosure, the
logarithmic estimates or the full cycle exclusions.

## Remarks

These are the exact arithmetic restrictions used by
[`positive-interface-mersenne-exclusion`](../positive-interface-mersenne-exclusion/README.md).
The hypotheses there imply (1) or (3) at the indicated
cuts. That written result retains its own status and LMN
assumption; no part of its broader exclusion claim is
promoted by this node.

The known high-to-low control `J=3,r=1,h=1`, with
`A=(2,1,1,3)`, `B=(4)`, has reduced additive parameter
`q=361`, cleared state `X=17` and cleared first endpoint
`Y=1205`. Its second difference is `Y-q*z=-600`, of exact
binary order 3. The Lean declaration `negative_difference_control`
instantiates the high-to-low theorem and checks its endpoint
hypotheses, obtaining exact orders 5 for the first target 480
and 3 for the second target -600. The theorem allows that sign and does not
exclude this cycle or the actual `3x+5,7,13,61` controls.
No denominator-one hypothesis or contradiction conclusion
appears in the formal statements. Novelty undetermined.

## History

- 2026-11-08: isolated the two derived boundary identities
  and their exact binary divisibility as a scoped Lean
  statement, separate from the written Mersenne exclusions.
