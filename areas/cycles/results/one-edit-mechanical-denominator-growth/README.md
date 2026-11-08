---
id: one-edit-mechanical-denominator-growth
kind: result
title: One change to a mechanical word forces denominator growth
status: written
claim: >
  Raw odd-only clock. Let W be a primitive positive valuation word
  of length m>=2, total A and D=2^A-3^m>0. Suppose W differs in at
  most one position from a mechanical valuation word of the same
  length, with any positive total and phase. The changed letter
  may increase or decrease by any amount while staying positive.
  With q=den(W) and k=floor(m/2), unconditionally
  q>[2/(m+3)]*(4/3)^k*D/2^A.
  Conditional only on the replayed gap EXT-1, this is an effective
  exponential denominator lower bound, and every such W has q>1.
  The exclusion uses the exact cutoff m<32768, exact denominator
  comparisons for 42<=m<32768, and a local descent through 2^18
  with cycle-product comparisons for 2<=m<=41.
  No prime-length, coprimality, near-critical or fixed-slope
  hypothesis is imposed. Nonprimitive words and arbitrary cycles
  are not excluded.
authors:
  - Codex four-arc research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [paired-state-run-law, mechanical-word-exact-denominator]
assumes: [musson-collatz-gap-all]
certificates: [check_growth.py]
evidence:
  - "check_growth.json: finite mechanical factors, exact cycle arrows and denominator laws, cutoff and gap comparisons, local descent and actual-cycle controls"
tags: [cycles, mechanical-words, denominators, factor-complexity, effective-exclusion]
---

# One change to a mechanical word forces denominator growth

## Statement

For integers `m>=2`, `F>=m` and `0<=ell<m`, a mechanical valuation
word is

```
u_i=floor(((i+1)*F+ell)/m)-floor((i*F+ell)/m),  0<=i<m.
```

Every real phase gives one of these integer phases, and upper
mechanical conventions give the same collection. Cyclic rotations
replace `ell` by `ell+hF mod m`. No condition on `gcd(F,m)` is needed.

Let `W` be a primitive positive word of length `m`, differing from
such a `u` in at most one position. The two totals need not agree;
the replacement can have either sign and arbitrary size. Write

```
A=sum(W),       D=2^A-3^m>0,       q=D/gcd(C_W,D),
k=floor(m/2).
```

There is an unconditional denominator law

```
q > [2/(m+3)]*(4/3)^k * D/2^A.                         (1)
```

With the sole external input
[EXT-1](../../../../sources/musson-collatz-gap-all.md),
`2^A<=2^172*m^341*D`, it follows that

```
q > 2*(4/3)^k / [(m+3)*2^172*m^341].                   (2)
```

In particular, **every word in this class has `q>1`**, conditional
on EXT-1. The finite steps are replayed locally; no external
convergence-range or period bound is used.

The [prime four-mismatch family](../sparse-rotation-bounded-period-reduction-obstruction/README.md)
is a subfamily. Its failure of bounded short-period descriptions
remains valid, but its exact denominator arithmetic rules it out
at `q=1`. No assertion that arbitrary four-mismatch words lie in
this one-substitution class is made.

## Proof

### 1. One unchanged mechanical segment supplies a long repeat

Rotate the exceptional position to the last letter; when there is
no change, choose any cut. The first `m-1` letters remain a factor
of a cyclic mechanical word. For each `t>=0`, a mechanical word has
at most `t+1` different length-`t` factors. Here is the finite reason.
At phase `a` in `0,...,m-1`, the first `j` letters sum to
`floor((jF+a)/m)`. For each `1<=j<=t`, this is constant in `a`
except at at most one threshold. At most `t` thresholds split the
phase interval into at most `t+1` classes. The full factor is
determined by those prefix sums. This also covers repeated
mechanical words and the empty factor at `t=0`.

Put

```
t=floor((m-2)/2),       k=t+1=floor(m/2).
```

The `t+2` length-`t` windows starting at `0,...,t+1` fit inside
the unchanged prefix because `2t+1<=m-1`. Two are equal, at distinct
starts `i<j<=t+1`.

Realize `W` as its reduced positive odd integer `3x+q` cycle,
using the [word-cycle correspondence](../mechanical-word-exact-denominator/README.md).
Primitivity makes its odd states distinct. Let the repeated factor
have total `E`, and let `z_start=n_j-n_i`,
`z_end=n_(j+t)-n_(i+t)`. The
[paired-state run law](../paired-state-run-law.md) gives

```
2^E*z_end=3^t*z_start,
z_start=2^(E+1)*b,       z_end=2*3^t*b,       b!=0.
```

Thus, with `H` the largest odd state,

```
H > 2*3^t.                                              (3)
```

Overlapping windows are allowed. For `m=2,3`, `t=0`: any two
distinct odd states differ by a nonzero even integer, so the same
argument and (3) still apply.

### 2. Eliminate the cycle minimum and maximum

Let `L` be the smallest odd state and
`Lambda=ln(2^A/3^m)>0`. Multiplication of all raw odd-only arrows
and `ln(1+x)<x` give

```
Lambda=sum_i ln(1+q/(3n_i)) < mq/(3L).
```

Since `ln(y)>1-1/y` for `y>1`,

```
L < mq*2^A/(3D).                                       (4)
```

At every odd step, `S_q(x)+q<=(3/2)(x+q)`, since its exact
valuation is at least one. Starting at the minimum and reaching
the maximum within `m-1` odd steps therefore gives

```
H+q <= (3/2)^(m-1)*(L+q),
H < (3/2)^(m-1)*q*(m+3)*2^A/(3D).                      (5)
```

The second line uses (4) and `D<2^A`. Combining (3) and (5),

```
q > [6*3^t/(m+3)]*(2/3)^(m-1)*D/2^A.
```

If `m=2k`, its coefficient is `3*(4/3)^k/(m+3)`;
if `m=2k+1`, it is `2*(4/3)^k/(m+3)`.
The weaker common coefficient proves (1), with no external input.
EXT-1 then proves (2).

### 3. An exact large-length cutoff

Suppose `q=1`. For `m>=3`, `m+3<=2m`, and
`log_2(4/3)>2/5` follows from `2^8>3^5`. Equation (2) gives

```
log_2(q) > (m-2)/5 - 172 - 342*log_2(m).                (6)
```

At `m=32768=2^15`, the right side equals `6256/5>0`.
It increases thereafter: its derivative is
`1/5-342/(m*ln2)>1/5-684/m>0`, using `ln2>1/2` and
`32768>3420`. This contradicts `q=1`. Hence

```
m < 32768.                                             (7)
```

### 4. The remaining finite step is local and exact

For each `m`, put `A_min=bit_length(3^m)` and
`D_min=2^A_min-3^m`. The ratio `D/2^A=1-3^m/2^A`
increases with `A`. The certificate verifies, by integer arithmetic,
for every `42<=m<32768`,

```
2*4^floor(m/2)*D_min
  > (m+3)*3^floor(m/2)*2^A_min.                         (8)
```

Thus (1) excludes those lengths for all admissible totals at once.
Only `2<=m<=41` remain.

The certificate checks that every odd seed `3<=x<2^18` reaches
a smaller positive odd integer under `3x+1`. Induction, with the
fixed point 1 as the base, proves that all such seeds reach 1.
A nontrivial raw cycle therefore has every odd state greater than
`L_*=2^18` (the threshold itself is even).

For every `2<=m<=41`, the certificate also verifies

```
(3L_*+1)^m < 2^A_min * L_*^m.                          (9)
```

But a `q=1` cycle of that length would satisfy
`2^A=product_i(3+1/n_i)<=(3+1/L_*)^m<2^A_min`,
contradicting `A>=A_min`. This finishes the exclusion. The local
descent and (8)-(9) are finite proof steps, not extrapolations.

## Certificates

Run [`check_growth.py`](check_growth.py) from the repository root.
It checks mechanical phase factors and repeated-factor divisibility
on an exact finite range, including increases, decreases, unchanged
words, and noncoprime base totals. It reconstructs reduced actual
cycles and checks (1) without floating point. The certificate also
replays all comparisons (8)-(9), the cutoff constants, every required
odd descent below `2^18`, and the eleven standard actual-cycle
fixtures. A fixed per-seed step guard makes a failed descent terminate
with an error. Exact counts and finite scope are in
[`check_growth.json`](check_growth.json).

The numerical samples check the implementation; the arbitrary-length,
arbitrary-phase and arbitrary-letter assertions follow from the proof.
Checks remain active under `python3 -O`.

## Remarks

**What is added.** This is an explicit denominator consequence and
complete finite closure of the established repeat method. The
[cycle-word repeat bound](../cycle-word-repeat-bound/README.md)
already supplies an asymptotic exclusion once a repeated factor of
length about `m/2` is identified. The same finite-cylinder and
pigeonhole mechanism occurs in
[R77-b](../../../convergence/results/divergent-orbit-itinerary-complexity/README.md).
We retain the denominator, eliminate the height explicitly, and close
all lengths with a small local computation and only EXT-1 externally.

The primary antecedent for the complexity argument is
[Dubickas (2009), Theorem 5 and its proof](../../../../sources/dubickas-2009-linear-map-complexity.md).
The finite mechanical-prefix route was also suggested by the public
[mechanical-itinerary formalization](https://github.com/msharpe248/collatz/blob/main/lean/Collatz/RationalMechanical.lean).
No theorem from that development is assumed or labeled replayed here.
Novelty of this scoped denominator law is undetermined.

This meaning of **one change** differs from the total-preserving
adjacent swaps or unit transfers called *one move* in the
[Christoffel-neighbourhood notes](https://github.com/mmusson/collatz/blob/main/christoffel-neighbourhood/christoffel-neighbourhood-working-notes.tex).
Here a nonzero substitution changes exactly one valuation and
therefore changes the total. The mechanical base's total `F` is
independent of the cycle word's total `A`.

Primitivity is essential: repeated `(2)` has denominator 1 and
zero changes from a mechanical word. Actual `3x+d` controls remain
valid. For example `(1,1,3)` differs once from `(1,1,1)` and realizes
the `3x+5` cycle `19 -> 31 -> 49 -> 19`; the result bounds its true
denominator and does not exclude it. The final local descent is used
only at `q=1`.

The [four-mismatch coverage obstruction](../sparse-rotation-bounded-period-reduction-obstruction/README.md)
and this arithmetic exclusion are compatible. Its words still
require many bounded-period pieces. Integrality, not a recovered
periodic decomposition, excludes denominator 1 for that family.
General four-mismatch words and words with two or more arbitrary
changes from mechanical backgrounds remain outside this theorem.

## History

- 2026-11-08: derived the denominator law by applying the established
  repeated-factor argument to one unchanged mechanical segment, then
  closed the finite lengths by exact comparisons and local descent.
  Same-session audits do not upgrade the node to `reviewed`.
