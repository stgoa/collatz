---
id: sparse-four-arc-near-critical-classification
kind: result
title: A sparse four-arc family has exactly one near-critical full-plus cancellation
status: written
claim: >
  Raw odd-only clock, positive valuation words for rational 3x+1 cycles,
  equivalently reduced integer 3x+q cycles. Let r>=2, a,b>=1, c>=2,
  w=(1^(2r-4),a,1,c,1^(2r-2),c,1,b), and suppose its total
  A=4r+a+b+2c-4 is even and 3^(4r)<2^A<2*3^(4r).
  Then P=2^(A/2)+3^(2r) divides C_w if and only if
  (r,a,b,c)=(3,3,5,2). This unique word has reduced denominator 295,
  so no word in this explicitly near-critical family has denominator 1.
  The proof reduces all unbounded parameters to 11697 exact finite cases:
  for r>=38 a positive-letter size bound forces an integer residue to
  vanish, whose only solution is incompatible with near-criticality.
  Under the coprime shift 2r-1, the family has at most four constant
  arcs, with prescribed block lengths (4r-4,1,2,1); no classification
  of arbitrary four-arc words or asymptotic cancellation bound is claimed.
authors:
  - Codex four-arc research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [near-critical-four-mismatch-corpus-counterexample]
certificates: [check_classification.py]
evidence:
  - "check_classification.json: polynomial identity, exact cutoff, exhaustive finite remainder, unique cancellation, and actual 3x+d controls"
tags: [cycles, four-arcs, near-critical, denominators, cancellation, classification]
---

# A sparse four-arc family has exactly one near-critical full-plus cancellation

## Statement

Write `1^j` for a string of `j` letters equal to 1, allowing `j=0`.
For integers `r>=2`, `a,b>=1`, and `c>=2`, consider

```
w = (1^(2r-4), a, 1, c, 1^(2r-2), c, 1, b),
m = 4r,       A = 4r+a+b+2c-4.
```

Assume `2 | A` and the explicit near-critical inequalities
`3^(4r)<2^A<2*3^(4r)`. Put

```
t = (a+b+2c-4)/2,        P = 2^(A/2)+3^(2r),
D = 2^A-3^(4r) = (2^(A/2)-3^(2r))*P.
```

Then **`P | C_w` holds exactly when `(r,t,a,b,c)=(3,4,3,5,2)`**.
The surviving word is
`(1,1,3,1,2,1,1,1,1,2,1,5)`, the existing `3x+295`
[counterexample](../near-critical-four-mismatch-corpus-counterexample/README.md).
Its reduced denominator is 295. Since denominator 1 would require
`D | C_w`, hence `P | C_w`, **this near-critical family contains no
denominator-1 word**.

The word class is deliberately narrow. The shift `h=2r-1` is
coprime to `m=4r`. Following the index track from the final letter
`b` gives

```
(b, c, c, a, 1^(4r-4)).
```

Thus there are at most four constant arcs, with the indicated cyclic
block lengths `(4r-4,1,2,1)`. If adjacent labels coincide, arcs merge.
The theorem does not require primitivity. It does not cover other arc
lengths, general coprime shifts, or words whose total is odd. The same exclusion holds for cyclic rotations of these words,
because cancellation by the odd divisor `P` of `D` is rotation invariant.

## Proof

### 1. An explicit intercept and its small residue

Set

```
X=2^r,  Y=3^r,  U=2^t,  R=2^c,  Q=2^a,  T=2^b.
```

Here `t>=1`: the integer `2t=a+b+2c-4` is positive.
Near-criticality gives `U>(9/4)^r>=81/16`, so `U>=8`.
The letter-total relation is

```
Q*T*R^2 = 16U^2,               P = Y^2+UX^2.                 (1)
```

The intercept concatenation identity
`C_(uv)=3^len(v)*C_u+2^sum(u)*C_v`, together with
`C_(1^j)=3^j-2^j`, gives

```
32C_w = 32Y^4 + 6[Q(5+2R)-18]X^2Y^2
                    + Q R(5R-18)X^4.                       (2)
```

For a direct derivation, use the blocks
`1^(2r-4), (a), (1), (c), 1^(2r-2), (c), (1), (b)`;
the final letter `b` does not enter an intercept. The certificate
also verifies (2) as a polynomial identity: if
`V=3^(2r-4)` and `Z=2^(2r-4)`, the two long blocks have
numerator weights `V,9V`, denominator weights `Z,4Z`, and
intercepts `V-Z,9V-4Z`; substitute `Y^2=81V`, `X^2=16Z`.

Reducing (2) modulo `P`, so that `Y^2=-UX^2`, yields

```
P | C_w  iff  P | H,
H = A_0+Q B_0,
A_0 = 4U(8U+27),
B_0 = R(5R-18)-6(5+2R)U.                                   (3)
```

Indeed, the remainder in (2) is `X^4 H`; both 32 and `X`
are units modulo the odd number `P`.

### 2. The residue can vanish only at the counterexample parameters

Suppose `H=0`. Then

```
Q = (32U^2+108U)/(6(5+2R)U-R(5R-18)).                        (4)
```

The denominator is positive, and the numerator has 2-adic
valuation `t+2`. The two terms in that denominator have
2-adic valuations `t+1` and `c+1`, respectively.

If `c<t`, their valuations differ and (4) forces
`a=t-c+1`, hence `Q=2U/R`. Substitution gives

```
(30-4R)U = R(36+5R).
```

Since `R>=4` is a power of 2, positivity forces `R=4`.
Then `U=16`, so `(t,c,a,b)=(4,2,3,5)` by (1).

If `c>t`, (4) instead forces `Q=2`. Substitution gives

```
16U^2+(24-12R)U+5R^2-18R = 0.
```

But `R>=2U`. Writing `R=2U+s`, `s>=0`, makes the left side
`12U(U-1)+(8U-18)s+5s^2`, strictly positive for `U>=4`.

If `c=t`, then `R=U` and (4) is
`Q=4(8U+27)/(7U+48)`. This is strictly between 2 and 8.
The only possible power of 2 is 4, which would require `U=21`,
not a power of 2.

Consequently

```
H=0  iff  (t,c,a,b)=(4,2,3,5).                              (5)
```

### 3. Positivity supplies a uniform size bound

Equation (1) and `Q,T>=2` imply

```
R<=2U,       Q,T<=8U^2/R^2.
```

Since `U,R>=4`,

```
A_0<=59U^2,
|B_0| <= 5R^2+18R+30U+12RU <= 34RU.                        (6)
```

The second bound uses, term by term, `R<=2U`, `U>=4`,
and `R>=4`. We choose an integer residue `J` equivalent to `H`
for divisibility by `P`, as follows.

If `a<=b`, then `Q<=sqrt(QT)=4U/R`, so take `J=H` and get
`|J|<=195U^2`.

If `a>=b` and `R>=sqrt(U)`, take `J=H` again. Now (6) gives
`|J|<=59U^2+272U^3/R<=331U^(5/2)`.

In the remaining case `a>=b`, `R<=sqrt(U)`, use

```
J = R^2 T(8U+27)+4U B_0 = [R^2 T/(4U)] H.                  (7)
```

The first expression shows that `J` is an integer. The multiplier
in brackets is a power of 2, possibly with negative exponent.
Clearing a power-of-two denominator and using that `P` is odd
shows `P | J` if and only if `P | H`; also `J=0` if and only
if `H=0`. Since `T<=4U/R`,

```
|J| <= 59RU^2+136RU^2 <= 195U^(5/2).
```

In every case, therefore, we have an integer `J` satisfying

```
P | J iff P | C_w,       J=0 iff H=0,
|J| <= 331U^(5/2).                                         (8)
```

This is the structural input: the two special letters cannot
both be arbitrarily large at a fixed total. It uses the actual
word shape and positivity, beyond the generic mismatch-cut
congruences.

### 4. Near-criticality makes the reduction finite

The near-critical inequalities are equivalent to

```
(9/4)^r < U < sqrt(2)*(9/4)^r.
```

Since `P>UX^2=U4^r`, (8) gives

```
|J|/P < 331 U^(3/2)/4^r
      < 331*2^(3/4)*(27/32)^r.                              (9)
```

The exact integer inequality

```
8*331^4*27^152 < 32^152
```

certifies that the last expression is below 1 at `r=38`,
and it decreases with `r`. Thus `r>=38` and `P | C_w` force
`J=0`, hence the parameters in (5). Those have `t=4`; but for
`r>=4`, `3^(4r)>2^(4r+8)`, because it holds at `r=4` and
the ratio increases by `81/16` at each increment. They cannot
be near-critical for `r>=38`. Therefore **`r<=37`**.

All remaining parameter ranges are now bounded by the proof.
Near-criticality and `3<4` give

```
2^(4r+2t) < 2*3^(4r) < 2^(8r+1),
```

so the integer `t` satisfies `1<=t<=2r`. Positivity of `a,b`
gives `2<=c<=t+1`, and, for each such `c`,

```
1<=a<=2t-2c+3,        b=2t-2c+4-a.
```

The certificate exhausts these ranges for `2<=r<=37`, using
exact integer comparisons for near-criticality. The admissible
`(r,t)` are

```
(3,4), (4,5), (5,6), (9,11), (10,12), (11,13),
(15,18), (16,19), (17,20), (21,25), (22,26), (23,27),
(27,32), (28,33), (29,34), (33,39), (34,40), (35,41).
```

For a fixed `t`, the number of `(a,b,c)` is `t^2`. There
are **11,697** tuples in total. Direct calculation of the intercept
and of (3) finds exactly one with `P | C_w`:
`(r,t,a,b,c)=(3,4,3,5,2)`.

### 5. The other denominator factor survives

At the unique tuple,

```
P=1753,       2^(A/2)-3^(2r)=295,
C_w=1753*737, D=1753*295,       gcd(737,295)=1.
```

Hence `gcd(C_w,D)=1753` and `den(w)=295`, as also recorded
in the [counterexample node](../near-critical-four-mismatch-corpus-counterexample/README.md).
No other word in the specified near-critical family cancels
even the whole plus factor, and this one does not cancel the
remaining factor. This proves the denominator-1 exclusion.

For completeness, cyclic rotation preserves this conclusion:
if the first letter is `a_0`, the intercept identity
`2^(a_0) C_(R_1w)=3C_w+D` shows that divisibility by any
divisor of `D` is preserved, since `D` is coprime to 6.

## Certificates

[`check_classification.py`](check_classification.py) verifies the
intercept identity by polynomial arithmetic, the exact cutoff
inequality, all 11,697 remaining tuples, the residue bounds and
their equivalences, the prescribed coprime index track, and the
unique surviving denominator. Each finite tuple is also checked
against an independently evaluated intercept from the full word.
The script replays all eleven standard `3x+5,7,13,61` fixtures;
none of their odd-only periods is divisible by 4.

```
python3 areas/cycles/results/sparse-four-arc-near-critical-classification/check_classification.py
```

The script is deterministic, uses exact integers and the standard
library, and runs all checks under `python3 -O`. The generated
receipt is [`check_classification.json`](check_classification.json);
use `--write-receipt` to regenerate it. The finite certificate
completes a written reduction with no bound on the initial
parameters; it is not an extrapolation from a word census.

## Remarks

- **Scope and remaining work.** This isolates the known example
  inside one sparse four-arc shape. It does not settle part (C) of
  [`primitive-cancellation-below-half`](../../questions/primitive-cancellation-below-half.md),
  nor a general denominator-1 exclusion for four mismatches.
  Even within this family the theorem classifies complete plus
  cancellation, not the size of every proper divisor of `P` that
  can cancel. No assertion that every denominator-1 word is
  near-critical is used.
- **Why the generic elimination obstruction is avoided.** The
  [coupled mismatch matrix](../coupled-defect-matrix-smith-form/README.md)
  and [three-arc elimination attempt](../../attempts/three-arc-intercept-elimination/README.md)
  show that eliminating free block intercepts gives a condition
  already implied by `G | D`. Here the explicit background of
  ones makes the intercept a short polynomial, and the positive
  letters bound a representative of its residue below `P` for
  all sufficiently large `r`. That is extra size information
  specific to this word shape.
- **Controls.** The unique survivor is itself an actual positive
  `3x+295` cycle. The theorem preserves it, with denominator 295,
  and does not exclude the other `3x+d` control cycles. Scaling
  its states gives cycles at multiples of 295, as usual.
- **Novelty and status.** Novelty is undetermined. This is a
  written family-specific classification; no independent-session
  review or Lean formalisation is claimed.

## History

- 2026-11-08: Codex four-arc research lane (GPT-6 Astra; directed
  by Santiago Armstrong) analysed the coprime index track of the
  near-critical `3x+295` example, derived the polynomial residue
  and positive-letter bound, and completed the finite remainder.
