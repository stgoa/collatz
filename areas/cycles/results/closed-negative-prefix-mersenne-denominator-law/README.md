---
id: closed-negative-prefix-mersenne-denominator-law
kind: result
title: Closed negative prefixes force a Mersenne denominator bound
status: written
claim: >
  Raw odd-only words reconstructed from the low-to-high two-half-defect
  Mersenne normal form with r=1 and a closed first segment. For J>1
  and positive odd h, let A be any nonempty exact 3x+1 segment from
  -h back to -h and B any nonempty exact 3x+(2^J-1) segment from
  -h to h, with last(B)>J. Set u=A[J-1]B[-J], v=AB[1],
  m=len(A)+len(B), S=sum(A)+sum(B), D=2^S-3^m>0,
  eta=D/2^S and q=den(uv). If every normalized rational 3x+1
  cycle state is at least 3, then unconditionally
  q*h>eta*2^(3m/10-2). Under EXT-1 this implies
  q*h>2^(3m/10-174)/m^341. Under that sole external input,
  every such word with h<=91 and D>0 has q>1, without bounds
  on J, either segment length, valuations or intermediate states.
  A local exact descent and finite gap replay close half-lengths
  m<32768. No classification or nonexistence of the auxiliary
  signed returns or of arbitrary negative cycles is asserted.
authors:
  - Codex closed-prefix research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [two-half-defect-mersenne-normal-form, mersenne-join-state-enclosure, baseline-obligation-transfer-controls]
assumes: [musson-collatz-gap-all]
certificates: [check_closed_prefix.py]
evidence:
  - "check_closed_prefix.json: symbolic identities, exact finite gap closure, bounded local descent, negative-cycle and boundary controls, and all eleven standard positive cycles"
tags: [cycles, denominators, half-defects, signed-orbits, effective-bounds]
---

# Closed negative prefixes force a Mersenne denominator bound

## Statement

Use the raw odd-only maps
`T_d(y)=(3y+d)/2^v_2(3y+d)` on nonzero odd integers,
excluding zero numerators. Let `J>1`, `N=2^J`, and let
`h` be positive odd. Suppose that two nonempty exact signed
segments have positive valuation words `A,B`, with

```
A: -h -> -h under T_1,
B: -h ->  h under T_(N-1),       last(B)>J.
```

For a word `A`, the notation `A[t]` changes only its last
letter by `t`. The low-to-high normal form reconstructs

```
u=A[J-1]B[-J],       v=AB[1],
a=len(A), P=sum(A), b=len(B), T=sum(B),
m=a+b,              S=P+T,
D=2^S-3^m,          eta=D/2^S,
q=den(uv).                                             (1)
```

All reconstructed letters are positive. The complete word
has length `2m`, total valuation `2S`, and denominator
`D_(uv)=(2^S+3^m)D`. Throughout suppose `D>0`.
A normalized state means the positive rational `3x+1`
cycle state, not its integer multiple under `3x+q`.

**Denominator law with a state floor.** If every normalized
cycle state is at least 3, then

```
q*h > eta * 2^(3m/10-2).                              (2)
```

This inequality has no external input. Applying
[EXT-1](../../../../sources/musson-collatz-gap-all.md) gives

```
q*h > 2^(3m/10-174) / m^341.                          (3)
```

**Bounded-endpoint exclusion under EXT-1.** For every segment
pair in (1) with `h<=91`, `D>0` implies `q>1`.
There is no restriction on `J`, either segment length, the
letters or intermediate states. No primitivity or near-critical
hypothesis is used. The only external input is EXT-1;
the finite convergence check is replayed here.

This includes `h=1`, when necessarily `A=(1)^k`, and every
origin on the explicit negative cycles with absolute states

```
(1),       (5,7),       (17,25,37,55,41,61,91).
```

These examples are verified, not asserted to list every
negative cycle. The result excludes denominator one for the
stated reconstructions, not the auxiliary signed returns
themselves or all low-to-high normal forms.

## Proof

### 1. Keep the endpoint and the residual denominator

The endpoint of any `T_1` arrow is nonzero modulo 3, so
the closed first segment gives `3` not dividing `h`.
If `J` is even, every output of `T_(N-1)` is divisible by
3, contrary to its endpoint `h`. Hence any pair in the
statement has odd `J>=3`.

Write `sigma=3^a/2^P` and `c=3^b/2^T` for the ordinary
additive-one slopes. The closed first segment and the
opposite endpoints of the second give

```
F_A(t)=sigma*t+h*(sigma-1),
F_B(t)=c*t+e,       e=h*(1+c)/(N-1).                 (4)
```

The intercept of `A` is positive, so `sigma>1`.
Put `lambda=sigma*c=3^m/2^S=1-eta`.
The normal-form boundary changes and canonical-state identity
give, for the canonical normalized state `x`,

```
F_u(t)=2c*F_A(t)+N*e,       F_u(x)=2x+h.
```

Substituting (4) yields the exact equations

```
2(N-1)D*x = h*[2(N-1)3^m+2^S-(N-2)2^P3^b],
2(N-1)x/h = 1+3^b*F/D,
F=(2N-1)3^a-(N-2)2^P.                               (5)
```

Since `3^a>2^P` and `N>=8`,

```
0<F<2N*3^a.                                         (6)
```

The reduced integer realization has addend `q` and
canonical state `qx`, both odd positive integers.
Multiplying (5) without dividing by `h` gives
`D | q*h*3^b*F`. Since `gcd(D,3)=1`,

```
D | q*h*F,       D <= q*h*F < 2N*q*h*3^a.           (7)
```

No factor of `h` or `N-1` is cancelled in this deduction.
Define `alpha=log_2(3)` and `L=log_2(q*h/eta)>0`.
Because `D=eta*2^S>eta*3^m`, (7) gives

```
alpha*b < J+L+1.                                    (8)
```

### 2. The closed negative prefix costs binary divisibility

The [state enclosure](../mersenne-join-state-enclosure/README.md),
with `M=K=2`, gives

```
x < h*(1+2lambda)/(2(1-lambda)) < 3h/(2eta).         (9)
```

Let `Y` be the odd integer state after the modified first
block `A[J-1]` in the reduced `3x+q` cycle. Equation (4)
at that boundary gives

```
3^a*q*(x+h) = 2^P*(2^(J-1)*Y+q*h).                 (10)
```

The parenthesis is odd, since `J>=2` and `q,h,Y` are odd.
In particular, `2^P | q*(x+h)`. Positivity, (9), and
`eta<1` now imply

```
2^P <= q*(x+h) < (5/2)*q*h/eta < 4q*h/eta,
a <= P < L+2.                                      (11)
```

Equations (8) and (11) give

```
alpha*m-J < (1+alpha)L+2alpha+1
          < (1+alpha)(L+2).                         (12)
```

This inequality already holds without the state-floor
hypothesis in (2).

### 3. A normalized floor converts (12) into denominator growth

Let the `2m` normalized cycle states be `x_i>=3`.
Multiplying their exact `3x+1` arrow equations gives

```
2^(2S) = product_i (3+1/x_i) <= (10/3)^(2m).
```

Since `(10/3)^4<2^7`, it follows that `S<7m/4`.
Also `last(B)>J` and all other letters are positive,
so `T>=J+b` and `P>=a`, whence `S>=m+J`.
Therefore `J<3m/4`. Combining this with (12) gives

```
L+2 > ((alpha-3/4)/(1+alpha))*m > 3m/10,
```

where the last inequality is equivalent to `alpha>3/2`,
or `3^2>2^3`. This proves (2).

The declared external input, applied to the half-length
`m` and total `S`, is

```
2^S <= 2^172*m^341*(2^S-3^m),
eta >= 2^(-172)*m^(-341).                            (13)
```

Combining (13) with (2) proves (3).

### 4. Exclude denominator one when h is at most 91

Suppose `q=1` and `h<=91`. The word is not a repetition
of `(2)`: the final letter of `A[J-1]` is at least `J>=3`.
A positive integer `3x+1` cycle containing 1 is the fixed
odd cycle `(1)`, with valuation 2 at every step. Therefore
all states of the present hypothetical integer cycle are
at least 3, and (3) applies.

For `m>=2^15`, put

```
f(m)=3m/10-174-341log_2(m).
```

Then `f(2^15)=22707/5>7`, and its derivative
`3/10-341/(m ln 2)` is positive throughout this range,
using `ln 2>1/2`. Thus (3) would imply `h>2^7>91`.
Only `1<=m<=32767` remain; allowing `m=1` enlarges the
finite range harmlessly.

Set `a_m=bit_length(3^m)`, so `2^a_m` is the least power
of 2 strictly above `3^m`. For every integer `S` with
`2^S>3^m`, the quantity `eta=1-3^m/2^S` is at least
`eta_m=1-3^m/2^a_m`. The certificate verifies

```
3*2^a_m < 2*82443*(2^a_m-3^m)
                         for 1<=m<=32767.           (14)
```

Consequently (9) implies

```
x < 82443*h <= 7502313 < 2^23.                      (15)
```

The certificate checks that each odd seed `3<=s<2^23`
reaches a strictly smaller positive odd integer under
`3x+1`, with a fixed step guard that fails if exceeded.
Induction on odd seeds proves that every positive odd
integer below `2^23` reaches 1. The hypothetical cycle
contains the integer state `x` in (15), contradicting its
nontriviality. This closes every remaining half-length.

## Certificates

Run from the repository root:

```
python3 areas/cycles/results/closed-negative-prefix-mersenne-denominator-law/check_closed_prefix.py
python3 -O areas/cycles/results/closed-negative-prefix-mersenne-denominator-law/check_closed_prefix.py
```

The [certificate](check_closed_prefix.py) verifies its
[deterministic receipt](check_closed_prefix.json). Use
`--write-receipt` to regenerate the receipt deliberately.
Its finite proof steps are (14), all odd-seed descents below
`2^23`, and exact rational cutoff comparisons. It also
checks the polynomial identity in (5), the modified-prefix
divisibility, and the listed negative cycles and their
rotations and repetitions.

The actual arrow `-1 -> 1` under `+7` has valuation 2,
so fails `last(B)>J=3`. The level-15 congruence witness is
kept separate from its actual orbit, which closes away
from 1. A genuine low-to-high join with `r=3` checks that
a return from `-1` to `1` does not imply the closed-prefix
`r=1` hypothesis. All eleven shared positive cycles for
`d=5,7,13,61` are replayed. No abstract affine sample is
labelled an actual signed valuation segment.

## Remarks

The [odd-order obstruction](../odd-order-residue-signed-endpoint-divisibility/README.md)
and [order-depth refinement](../signed-endpoint-order-depth/README.md)
exclude auxiliary signed returns at specified infinite sets
of levels. Here the conclusion is different: every stated
reconstruction with `h<=91` fails denominator one under
EXT-1, whether or not its second signed segment exists.
Those residue results remain intact.

A uniform assertion that the canonical state is always below
1 is not needed. Repeating a negative cycle increases the
total slope, while (7) and (11) control the remaining
integer divisibility. The general denominator law retains
the endpoint factor `h`; it does not exclude unbounded
endpoints. Nonclosed first segments and other normal-form
parameters remain outside the theorem. The general
four-mismatch question stays open.

The proof uses the existing normal form and enclosure;
the finite descent method also occurs in the
[mechanical-edit denominator law](../mechanical-edit-denominator-law/README.md).
No external minimum or period bound is imported here.
Novelty of this scoped combination is undetermined.

## History

- 2026-11-08: combined residual-denominator divisibility with
  a closed negative prefix and the state enclosure. A local
  finite replay removes the need for an imported period
  bound. Same-session scrutiny leaves status `written`.
