---
id: fibonacci-four-arc-spike-denominator-growth
kind: result
title: A Fibonacci four-arc family far from mechanical words has growing denominators
status: written
claim: >
  Raw odd-only positive valuation words. Let F_0=0,F_1=1 be the
  Fibonacci sequence, n>=7, m=F_n, h=F_(n-1), b=floor(m/10),
  a=m-2b-1, A=ceil(m*log_2(3)), and M=A-m-3b+1. Define W by
  reading 1^a,2^b,3^b,M along the h-track, so W_(jh mod m) is
  its jth track letter. Every W is primitive, has rotation
  distance exactly 4, is near-critical, and differs at at least b
  positions from every positive mechanical word of length m,
  regardless of its total or phase. Its unique largest letter is
  M=(log_2(3)-13/10)*m+O(1). Unconditionally, with
  eta=(2^A-3^m)/2^A, den(W)>2^(m/10-4)*eta/m^9.
  Under only the replayed gap EXT-1, this gives
  den(W)>2^(m/10-176)/m^350 and excludes denominator one for
  every n>=7; the finitely many lengths below 2^16 are checked
  exactly. More generally, for a three-interval 1,2,3 template
  of length m>=6, total F<m*log_2(3), and coprime chronological
  rotation k, a primitive word obtained by one positive edit,
  with D=2^A-3^m>0, satisfies
  den(W)>eta*3^(t+1)*2^F/(2^(4(K-1))*m*3^m), where
  t=floor((m-2)/4), K=K(k/m), and eta=D/2^A.
  This excludes one specified infinite four-mismatch
  family, not arbitrary four-mismatch words or integer cycles.
authors:
  - Codex cycle research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [paired-state-run-law, denjoy-koksma-height-bound, mechanical-word-exact-denominator]
assumes: [musson-collatz-gap-all]
certificates: [check_fibonacci_spike.py]
evidence:
  - "check_fibonacci_spike.json: Fibonacci inverse and continued-fraction checks, exact arc spectra, template factors and discrepancy, denominator inequalities, finite closure and actual-cycle controls"
tags: [cycles, rotation-distance, four-arcs, denominators, discrepancy, fibonacci]
---

# A Fibonacci four-arc family far from mechanical words has growing denominators

## Statement

Write `F_0=0`, `F_1=1`, and `F_(n+1)=F_n+F_(n-1)`.
For every `n>=7`, define

```
m=F_n,             h=F_(n-1),          b=floor(m/10),
a=m-2b-1,          alpha=log_2(3),      A=ceil(m*alpha),
M=A-m-3b+1.
```

The **track word** is the concatenation

```
1^a  2^b  3^b  M,
```

where exponents denote repetition. The valuation word `W` is in
chronological order: its letter at position `jh mod m` is the
track word's letter at position `j`. This permutation is defined
because consecutive Fibonacci numbers are coprime.

Every such word has the following properties:

- All letters are positive, and the unique largest letter `M>=4`
  makes the word primitive.
- Its total is `A`, and `3^m<2^A<2*3^m`.
- Its rotation distance is exactly 4, attained at `h` and `-h`.
- Every positive mechanical word of length `m`, with any total
  and phase, differs from `W` in at least `b` positions. This
  remains true after any cyclic cut.
- The large letter satisfies
  `(alpha-13/10)m+1 < M < (alpha-13/10)m+5`.

Thus the family has a coprime four-mismatch rotation, a
near-critical total and a largest letter proportional to its
length, while its distance from every mechanical word grows
linearly. In particular, once `b>10` it lies outside the
ten-edit hypothesis of the
[mechanical-edit exclusion](../mechanical-edit-denominator-law/README.md).

Put `D=2^A-3^m`, `eta=D/2^A`, and `q=den(W)=D/gcd(C_W,D)`.
The unconditional denominator bound is

```
q > 2^(m/10-4)*eta/m^9.                                (1)
```

With the sole external input
[EXT-1](../../../../sources/musson-collatz-gap-all.md),
`2^A<=2^172*m^341*D`, this implies

```
q > 2^(m/10-176)/m^350.                                (2)
```

Equation (2) excludes denominator one for `m>=2^16`.
Exact checks for the remaining Fibonacci lengths establish
`q>1` for **every `n>=7`**. No external period or convergence
verification is used. The normalized rational `3x+1` cycle
has states `C_(R_iW)/D`; its actual reduced `3x+q` cycle has
integer states `C_(R_iW)/gcd(C_W,D)`. The theorem excludes
integer `3x+1` cycles only within this specified word family.

**Reusable template form.** Let `m>=6`, let `0<k<m` be coprime
to `m`, and label three nonempty cyclic track intervals by
1, 2 and 3. Read this template `U` chronologically with track
increment `k`, and suppose its total `F` satisfies
`F<m*log_2(3)`. Let `W` be a primitive positive word obtained
by increasing exactly one entry of `U`, with total `A` and
`D=2^A-3^m>0`. Write `K=K(k/m)` for the continued-fraction
partial-quotient sum, `eta=D/2^A`, and `t=floor((m-2)/4)`.
Then, without an external input or a near-critical assumption,

```
p_U(t)<=3t,
|sum(factor)-F*length/m|<=4(K-1)  for every proper factor,
den(W)>eta*3^(t+1)*2^F/(2^(4(K-1))*m*3^m).           (T)
```

The Fibonacci family is an explicit all-length application of
this template inequality, including a complete finite closure.

## Proof

### 1. Exact four-arc structure and mechanical distance

The total of the track word is `m+3b-1+M=A`. The strict
near-critical comparisons follow from the irrationality of
`alpha`. Since `alpha>3/2` and `b<=m/10`,

```
M > m/5+1 >= 18/5,
```

using `m>=F_7=13`. Hence the four labels are distinct and
`M>=4`. The bounds on `M` follow from
`m/10-1<b<=m/10` and `m*alpha<A<m*alpha+1`.
A unique occurrence of `M` prevents any proper period.

Let `k=h^(-1) mod m`. A chronological shift by `r` is a
track shift by `rk mod m`. For a cyclic interval of length
`l`, the number of points leaving that interval under this
shift is

```
min(||rk||_m,l,m-l),       ||x||_m=min(x mod m,(-x) mod m).
```

This follows by counting the two ends of the interval, or its
complement if the interval is longer than half the circle.
Since each of the four labels occupies exactly one nonempty
proper interval, the mismatch count is

```
s_W(r)=sum_(l in (a,b,b,1)) min(||rk||_m,l,m-l).         (3)
```

For nonzero `r` every summand is at least 1. At `r=+h,-h`
every summand equals 1. Therefore `rho(W)=4`.

A mechanical word has at most two consecutive integer letter
values. Its alphabet cannot contain both 1 and 3. The word
`W` has `a>=b` ones and `b` threes, so at least `b` positions
must disagree. Counts are unchanged by a cyclic cut. This
argument allows every mechanical total and phase.

### 2. Remove the spike and control the template discrepancy

Replace the unique `M` by 1 and call the resulting chronological
word `U`. On the cyclic track, its two adjacent 1-runs merge.
Thus `U` is a coding by three cyclic intervals, with labels
1, 2 and 3, total

```
T=m+3b,       beta=T/m<=13/10<alpha.
```

For any `t>=1`, its cyclic factor complexity satisfies

```
p_U(t)<=3t.                                            (4)
```

Indeed, a length-`t` factor at track phase `x` reads the labels
at `x,x+k,...,x+(t-1)k`. Each of the three interval boundaries
has `t` preimages. These at most `3t` boundary positions
partition the cyclic phase set into at most `3t` factor classes.
Coincident boundaries can only reduce the count.

The clock is essential for the discrepancy estimate: consecutive
chronological letters advance by **`k=h^(-1)` on the track**,
not by `h`. Cassini's identity gives

```
h^2=(-1)^n (mod m),
k=h when n is even,       k=m-h when n is odd.
```

The continued fraction of `h/m` consists of `n-3` ones and
a final 2, after its initial zero. Its partial-quotient sum is
`n-1`. Taking the complement preserves that sum (combine the
initial 1 with the next coefficient), so `K(k/m)=n-1` as well.

For any coprime chronological increment `k`, apply the discrete
Denjoy--Koksma and Ostrowski bound from
[the formal discrepancy core](../denjoy-koksma-height-bound/README.md)
to the mean-zero track function `f=U-beta`. Its cyclic total
variation is `1+1+2=4`. The core applies to any mean-zero
periodic function; no ordering or cycle-state assumption is
needed. Thus its discrepancy is at most `4(K(k/m)-1)`. For
the Fibonacci template this is `4(n-2)`: every proper cyclic
factor of `U`, of length `j<m`, satisfies

```
|sum(factor)-beta*j| <= Delta,       Delta=4(n-2).       (5)
```

The recurrence `F_n>=2F_(n-2)`, with the bases `n=2,3`,
gives `F_n^2>=2^(n-2)`. Consequently

```
Delta <= 8*log_2(m).                                   (6)
```

### 3. Repeated clean windows force a large integer state

Set `t=floor((m-2)/4)`, which is positive for `m>=6`.
The single edited position lies in exactly `t` of the `m`
cyclic windows of length `t`. Thus at least `m-t` windows
of `W` agree with `U`, and

```
m-t >= 3t+2 > p_U(t).
```

Two such windows repeat. Realize `W` as its reduced positive
odd `3x+q` cycle, using the
[word-cycle correspondence](../mechanical-word-exact-denominator/README.md).
Its states are distinct because `W` is primitive.
The [paired-state run law](../paired-state-run-law.md) gives a
nonzero difference of size at least `2*3^t` between the states
at the ends of these matching windows. If `H` is the maximum
state, positivity of the smaller state gives

```
H > 2*3^t.                                             (7)
```

Overlapping or cyclic windows cause no change to the run law.

### 4. Growth from the minimum gives the denominator bound

The edit only increases a letter. Equation (5) therefore gives
`sum(factor of W)>=beta*j-Delta` for every proper factor.
Put

```
rho=3/2^beta>1,       R=rho^m=3^m/2^T.
```

Every such factor has affine slope at most `2^Delta*rho^j`.
For a segment of length `l<m`, the exact affine expansion is

```
x_l=(3^l/2^E_l)*x_0
    +(q/3)*sum_(j=1)^l 3^j/2^(total of the length-j suffix).
```

Apply (5) to the segment and each suffix. Starting at the
minimum state `L` and reaching `H` within `m-1` steps gives

```
H <= 2^Delta*R*(L+mq/3).                               (8)
```

The cycle product and elementary logarithm bounds give

```
eta < ln(2^A/3^m)
    =sum_i ln(1+q/(3x_i)) < mq/(3L),
L < mq/(3eta).
```

Since `0<eta<1`, (8) implies
`H<2^(Delta+1)*R*mq/(3eta)`. Combining with (7) yields

```
q > 3^(t+1)*eta/(2^Delta*R*m).                         (9)
```

The same argument proves (T): use the general template total
`F`, its mean `F/m<alpha`, `Delta=4(K-1)`, and
`R=3^m/2^F>1`. The three-boundary complexity count and the
single-edit window count are unchanged. Primitivity is exactly
what supplies distinct states in the repeated-window step.

Now `t+1>(m-2)/4`, `T>13m/10-3`, and `alpha<8/5` give

```
alpha*(t+1)-log_2(R)
 > T-alpha*(3m+2)/4
 > m/10-19/5
 > m/10-4.
```

Use (6) in (9) to obtain (1). Substitution of EXT-1 gives (2).

### 5. Exact closure of every Fibonacci length

At `m=2^16`, the base-2 logarithm of the right side of (2) is

```
m/10-176-350*log_2(m)=3888/5>0.
```

It increases thereafter, since `ln(2)>1/2` gives derivative
greater than `1/10-700/m>0` for `m>=2^16`.
Thus `q>1` for every such length.

The remaining indices are exactly `7<=n<=24`:
`F_24=46368<2^16<F_25=75025`. The certificate constructs
each of these 18 words and verifies, using exact integers,

```
2^A-3^m > gcd(C_W,2^A-3^m).
```

This is exactly `q>1`. There is no time or orbit truncation
in this finite closure, and no external period lower bound.

## Certificates

[`check_fibonacci_spike.py`](check_fibonacci_spike.py) checks
the track-to-chronological permutation, inverse rotation and
continued-fraction identities, exact four-arc mismatch spectra,
all-factor discrepancy through exact prefix deviations, and
the finite denominator closure. On the smaller ranges
printed in its [receipt](check_fibonacci_spike.json), it also
checks direct rotation distances, every proper template factor,
factor complexity and the prefix-span identity. The denominator
bound (1) is checked with its fractional exponent cleared by
raising positive quantities to the tenth power.

The reusable form (T) is also checked on every expanding
three-interval template with `6<=m<=18`, every coprime step,
and one edit at each of the three boundary phases, at the two
totals specified in the receipt. Nonprimitive edited words are
counted separately and excluded from this formula check.

The script reconstructs actual reduced integer cycles of the
finite family and replays all eleven standard positive-cycle
fixtures. It also retains the existing near-critical `3x+295`
four-mismatch control; its length 12 lies outside this family.
No actual `3x+d` cycle is incorrectly excluded.

```
python3 areas/cycles/results/fibonacci-four-arc-spike-denominator-growth/check_fibonacci_spike.py
```

Use `--write-receipt` to regenerate the deterministic receipt.
All arithmetic is exact and standard-library only, and explicit
checks remain active under `python3 -O`. The arbitrary-length
claim is proved above; finite samples only check the formulas
and close the explicitly bounded residual set.

## Remarks

The [bounded-period coverage obstruction](../sparse-rotation-bounded-period-reduction-obstruction/README.md)
shows why four mismatches and a large letter do not force a short
periodic description. The present family also defeats a reduction
to a bounded number of changes from a mechanical word: its
mechanical distance is at least `floor(m/10)`. It is nevertheless
accessible through a three-interval template with logarithmic
discrepancy. The exceptional large letter increases valuations,
so it cannot spoil the lower factor-sum bound.

This uses the established repeated-factor separation and discrete
Denjoy--Koksma route, combined with the affine growth argument
also used in the [mechanical-edit law](../mechanical-edit-denominator-law/README.md).
The template's three-interval complexity and its chronological
rotation step are stated explicitly. No new general discrepancy
theorem or claim of novelty for those tools is made; novelty of
the scoped combination is undetermined.

The result does not infer near-criticality for hypothetical
integer cycles. Near-criticality is built into this family's
definition. It also does not assert that arbitrary four-arc
words have this template, these partial quotients, or a positive
edit. The general four-mismatch question remains open.

## History

- 2026-11-08: derived a denominator bound for a four-arc family
  that stays far from every mechanical word, using its
  three-interval template instead. The finite Fibonacci closure
  leaves EXT-1 as the sole external input. Same-session scrutiny
  is not an independent review; status remains `written`.
