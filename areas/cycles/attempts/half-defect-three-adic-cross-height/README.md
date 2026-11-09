---
id: half-defect-three-adic-cross-height
kind: attempt
title: The basic 3-adic cross-height bound loses the block intercepts
status: written
claim: >
  For positive odd integer raw 3x+d cycles with word A B A[p] B[q],
  nonempty positive blocks A,B and 1<=p<q, a proposed unweighted
  cross congruence is false: an exact d=1631 cycle violates it modulo 9.
  The corrected congruence retains both ordinary block intercepts.
  When p,q have opposite parity and the second paired quotient is
  negative, its positive expression is already larger than its
  3-adic modulus by elementary intercept floors, even after cancelling
  the common amplitude factor. Thus the positive-multiple lower-bound
  step gives no additional height restriction. This does not exclude
  other uses of the exact congruence or further intercept cancellation.
authors:
  - Codex residue research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on:
  - half-defect-positive-order-exclusion
  - baseline-obligation-transfer-controls
certificates: [check_cross_congruence.py]
evidence:
  - "check_cross_congruence.json: exact omitted-intercept countercontrol, scaled actual cycles, corrected congruences and eleven standard 3x+d fixtures"
tags: [cycles, half-defects, three-adic, intercepts, failed-route]
---

# The basic 3-adic cross-height bound loses the block intercepts

## Idea

Use the two paired differences of a half-period word to obtain a
positive multiple of a large power of three. A lower bound on that
multiple might then force one paired difference, and hence a cycle
state, to be large. The intended target was the remaining opposite-parity
branch of [half-defect-positive-order-exclusion](../../results/half-defect-positive-order-exclusion/README.md).

All arrows here use the raw odd-only map
`x -> (3x+d)/2^v_2(3x+d)`, with positive odd `d` and positive odd states.
For nonempty positive valuation words `A,B`, let `[j]` increase only
the final letter, and write

```
W = A B A[p] B[q],             1 <= p < q,
a = len(A), b = len(B),        n = a+b,
P = 3^a, R = 3^b,
Q = 2^sum(A), S = 2^sum(B),    k = 2^p, l = 2^q.
```

The full word has `2n` odd-only arrows. Its actual boundary states are
`x -> z -> y -> t -> x`. The ordinary additive-one intercepts are
`C_A,C_B`; the affine action of `A` is `(Px+d C_A)/Q`. Define

```
H = (y-x)/Q,                  J = (z-t)/S.
```

The cited paired-state result proves that `H` is a positive odd integer
and `J` is a nonzero odd integer. Its `d=1` exclusion leaves `J<0`
when `p<q`. The failed height argument below addresses that sign and
opposite-parity `p,q`; it does not assume a `d=1` cycle exists.

## What happened

The exploratory formula omitted the block intercepts. With
`r=min(a,b)`, it proposed

```
3^r divides l(k-1)H-k(l-1)J.                 [false in general]
```

For `A=B=(1)`, both intercepts equal one, so this omission is invisible.
The actual `d=47` cycle with word `(1,1,2,3)` passes that bare formula.
For longer blocks it fails. Take

```
A=(1,1), B=(2,1), p=1, q=2,
W=(1,1,2,1,1,2,2,3), d=1631.
```

The exact cycle is

```
9145 -> 14533 -> 22615 -> 17369 -> 26869 -> 41119
     -> 31247 -> 23843 -> 9145.
```

Here `C_A=5`, `C_B=7`, `H=4431`, `J=-1079`, and `r=2`.
The bare cross expression is `24198`, whose residue modulo nine
is six. The corrected expression is `133938`, divisible by nine.
This is an actual `3x+1631` cycle, not a `3x+1` counterexample.
No merged claim used the omitted-intercept formula.

The [certificate](check_cross_congruence.py) reconstructs these cycles,
checks every exact valuation, and compares its output with the
[generated receipt](check_cross_congruence.json). Further controls use
both paired orders, nontrivial common amplitude factors, and odd
scalings divisible by three. It also replays the eleven shared
[actual cycles](../../../convergence/results/baseline-obligation-transfer-controls/README.md),
retaining their true addends `5,7,13,61`. These finite checks support
the formulas; the all-length failure of the proposed lower-bound step
is the argument below.

## Why it fails

### The exact congruence must retain both intercepts

The four boundary equations are

```
Qz=Px+d C_A,                 Sy=Rz+d C_B,
kQt=Py+d C_A,               lSx=Rt+d C_B.
```

Consequently

```
kQS J = P(kx-y)+(k-1)d C_A,
lQS H = R(lz-t)+(l-1)d C_B.                              (1)
```

Multiply the first identity by `(l-1)C_B` and the second by
`(k-1)C_A`, then subtract. The `d` terms cancel. Since `QS` is
a power of two, it is invertible modulo `3^r`, giving

```
3^r divides l(k-1)C_A H-k(l-1)C_B J.                    (2)
```

This derivation does not require `3` to be coprime to `d`.
Removing `C_A,C_B` from (2) is unjustified.

### The corrected minimum-positive-multiple bound is automatic

Assume now that `p,q` have opposite parity and `J<0`. Put

```
g0 = gcd(k-1,l-1) = 2^gcd(p,q)-1.
```

The common exponent `gcd(p,q)` is odd, so `3` does not divide `g0`.
Cancelling the unit `k g0` in (2) gives a positive multiple of `3^r`:

```
U = u C_A H + v C_B(-J),
u = 2^(q-p)(k-1)/g0 >= 2,
v = (l-1)/g0 >= 3.                                     (3)
```

For the last inequality, `g0<=k-1` and `l>=2k`, so
`v>2`; it is an integer. This cancellation includes the common
amplitude factor, not merely a power of two.

Every positive word of length `a` has intercept at least `3^(a-1)`:
that is its first summand. Hence, before using any congruence,

```
C_A >= 3^(a-1),        C_B >= 3^(b-1),
H >= 1,               -J >= 1,
U >= 2*3^(a-1)+3*3^(b-1)
  >= 5*3^(r-1) > 3^r.                                  (4)
```

Thus replacing (2) by only `U>=3^r`, the minimum-positive-multiple
bound, adds nothing to these elementary floors. The proposed
height-growth step does not survive restoration of the intercepts.
The exact condition that `U` be a multiple of `3^r` remains stronger
than a size inequality and has not been discarded as information.

## What survives

The corrected coupled congruence (2) remains available. Each ordinary
intercept is a 3-adic unit: its last summand is a power of two, and
all earlier summands are divisible by three. Therefore, when
`3` does not divide `d`, (1) also gives the exact clipped valuations

```
min(v_3(J),a) = min(v_3(k-1),a),
min(v_3(H),b) = min(v_3(l-1),b).                         (5)
```

The paired quotients are nonzero, so these valuations are defined.
For addends divisible by three, the certificate checks (1) and (2)
but does not apply (5).

A useful continuation would exploit the exact intercepts, additional
common factors involving `C_A,C_B`, or restrictions on the residue of
`U/3^r`. The argument here does not address those possibilities or
rule out 3-adic approaches generally.

The distinction between a coupled relation and a stronger unsupported
consequence has precedents in
[coupled-defect-matrix-smith-form](../../results/coupled-defect-matrix-smith-form/README.md)
and [termwise-plateau-divisibility](../termwise-plateau-divisibility.md).
Their results are not used in the calculation above. This attempt
records a specific failed step, not a novelty claim; novelty is
undetermined.

## History

- 2026-11-08: recorded the failed cross-height route, its genuine
  omitted-intercept countercontrol, the corrected congruence, and the
  redundant positivity bound after amplitude-gcd cancellation.
  Same-session scrutiny is not an independent review.
