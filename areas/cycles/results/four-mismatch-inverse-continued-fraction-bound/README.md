---
id: four-mismatch-inverse-continued-fraction-bound
kind: result
title: Four mismatches bound inverse continued-fraction complexity
status: written
claim: >
  Raw odd-only 3x+1 clock. Assume EXT-1. In a primitive positive integer
  cycle of period m>=2^1536, let 0<h<m be coprime to m and suppose
  its valuation word has at most four mismatches with its rotation by h.
  If 0<k<m is the inverse of h modulo m, the sum K(k/m) of the
  canonical continued-fraction coefficients satisfies K(k/m)<m/512.
  The elementary arithmetic bridge holds for m>=2^34: K(k/m)>=m/512
  supplies positive integers j,Q with jQ<=512 and |jh|_m=Q.
  There is no period import or global convergence assumption; a local
  check establishes the minimum-state bound used in the proof.
  Together with the all-density two-level four-arc theorem, this excludes
  denominator one for every word read along a coprime track as
  V,1^a,2^b,1^c, with a,b,c>=1, V>=3, m=1+a+b+c>=2^1536 and D_w>0,
  without a density or continued-fraction restriction.
  Other four-mismatch words remain outside that corollary.
authors:
  - Codex signed-endpoint research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex main research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [rise-lemma, paired-state-run-law, sparse-two-level-four-arc-exclusion]
assumes: [musson-collatz-gap-all]
certificates: [check_inverse_complexity.py]
evidence:
  - "check_inverse_complexity.json: continuant identities and end coefficients, exact cutoff constants, local minimum verification and actual-cycle controls"
tags: [cycles, rotation-distance, continued-fractions, rise-lemma, effective-bounds]
---

# Four mismatches bound inverse continued-fraction complexity

## Statement

Let `n_0,...,n_(m-1)` be distinct positive odd integers forming
a raw odd-only `3x+1` cycle, with positive valuation word
`w=(a_0,...,a_(m-1))`. Write

```
s(d)=#{i mod m:a_i!=a_(i+d)},
|d|_m=min(d mod m, m-(d mod m)).
```

Fix `0<h<m` with `gcd(h,m)=1` and `s(h)<=4`. Let `0<k<m`
satisfy `kh=1 mod m`. For the canonical finite continued
fraction

```
k/m=[0;c_1,...,c_n],    c_i>=1, c_n>=2,
K(k/m)=c_1+...+c_n,
```

the following conclusion holds under
[EXT-1](../../../../sources/musson-collatz-gap-all.md):

```
m>=2^1536  ==>  K(k/m)<m/512.                       (1)
```

This is a restriction on the inverse of a coprime rotation.
It is not an exclusion of arbitrary four-mismatch words,
and it makes no claim about the smaller finite interval.
The cutoff is explicit and very large.

The proof supplies an unconditional arithmetic bridge:
for every reduced `k/m` with `m>=2^34`,

```
K(k/m)>=m/512
 ==> there are integers j,Q>=1 with
     jQ<=512 and |j*k^(-1)|_m=Q.                    (2)
```

No cycle hypothesis is used in (2).

**Two-level four-arc corollary.** Let `a,b,c>=1`, `V>=3`,
`m=1+a+b+c`, and `gcd(h,m)=1`. Suppose a positive word `w`,
read along the index track `x,x+h,...,x+(m-1)h`, is

```
V, 1^a, 2^b, 1^c.
```

If `m>=2^1536` and `D_w>0`, then `den(w)>1` under EXT-1,
with no restriction on `b/m` or on `K(h^(-1)/m)`. This
corollary uses the
[all-density four-arc result](../sparse-two-level-four-arc-exclusion/README.md).
It is a statement about this specified track pattern, not
about arbitrary four-mismatch words.

## Proof

### 1. Elementary continuant bounds

For a list of positive integers, let its continuant be

```
C()=1, C(c_1)=c_1,
C(c_1,...,c_t)=c_t*C(c_1,...,c_(t-1))+C(c_1,...,c_(t-2)).
```

The denominator of `[0;c_1,...,c_n]` is `m=C(c_1,...,c_n)`.
Three consequences of the recurrence will be used:

1. Its positive polynomial expansion contains the full product
   of the coefficients. Thus `m>=c_i*c_j` for any distinct
   indices, since every other coefficient is at least one.
2. Every continuant is at least the sum of its coefficients
   (the empty sum is zero). For the inductive step, write
   `P=C(c_1,...,c_(t-1))`, `Q=C(c_1,...,c_(t-2))`, and
   `S=c_1+...+c_(t-1)`. Then

   ```
   c_t*P+Q-(S+c_t)
     =(c_t-1)*(P-1)+(Q-1)+(P-S)>=0.
   ```

   The one-term case is equality, and the displayed induction
   also covers two terms, where `Q=1`.
3. The prefix denominators are nondecreasing and each is at
   least twice the denominator two places earlier. Hence
   `m>=2^floor(n/2)` and `n<=2log_2(m)+1`.

Suppose `K(k/m)>=m/512`, and put `C=max_i c_i`. If
`C<m/1024`, the first bound and `K<=nC` give

```
C>=m/(512n),
K-C>m/1024,    K-C<=(n-1)m/C,
m<2^19*n*(n-1).                                    (3)
```

This is impossible for `m>=2^34`. To check the entire
unbounded range with integers, choose `d>=34` with
`2^d<=m<2^(d+1)`. The third bound gives `n<=2d+2`.
At `d=34`,

```
2^34 > 2^19*70*69.
```

The inequality `2^d>2^19*(2d+2)*(2d+1)` persists by
induction, since

```
2*(2d+2)*(2d+1)-(2d+4)*(2d+3)=4d^2-2d-8>0
```

for every `d>=34`. This contradicts (3). Therefore

```
C>=m/1024.                                         (4)
```

### 2. A large coefficient produces a short multiple

Choose `i` with `c_i=C`. Let `p/Q` be the convergent before
that coefficient, and let `p'/Q'` be the preceding convergent.
For `i=1` use `p/Q=0/1` and `p'/Q'=1/0`.
Set

```
R=C(c_(i+1),...,c_n),    F=C(c_i,...,c_n).
```

The tail is empty when `i=n`, so then `R=1`. The usual
convergent recurrences, or direct multiplication of their
two-by-two matrices, give

```
m=QF+Q'R,    k=pF+p'R,
Qp'-pQ'=(-1)^(i-1),
Qk-pm=(-1)^(i-1)*R,    m>=CQR.                      (5)
```

These formulas include both end coefficients: at `i=1`
the initial pair above gives the sign `+1`; at `i=n` the
tail is `R=1` and `F=C`.

Equation (4) gives `QR<=1024`. The other coefficients have
sum at most `Q+R`, by the continuant-sum bound applied to
the prefix and tail. Since `Q,R>=1`,

```
K-C<=Q+R<=QR+1<=1025,
C>=m/512-1025.
```

If `QR>=513`, (5) would imply

```
m>=513*(m/512-1025),
m<=512*513*1025=269222400<2^34,
```

a contradiction. Thus `QR<=512`. Multiplying the congruence
in (5) by `h=k^(-1)` gives `Rh=+Q` or `-Q mod m`.
Both `Q` and `R` lie between 1 and 512, and `Q<m/2`.
Taking `j=R` proves the exact cyclic distance in (2).

### 3. Apply the short rotation to the cycle

Mismatch counts are subadditive:
`s(d+e)<=s(d)+s(e)`. Indeed, a mismatch between positions
`i` and `i+d+e` implies a mismatch in at least one of the
comparisons through the intermediate position `i+d`.
Translations preserve cardinalities. Induction gives

```
s(jh)<=j*s(h)<=4j<=2048.                            (6)
```

The rotation `jh` is nonidentity, since its cyclic distance
is `Q>=1`. Its mismatch count `s` is positive: a zero
mismatch rotation would repeat the primitive cycle's
valuation word. Equivalently, iterating its affine map
would force coincident states.

Let `L,H` be the minimum and maximum cycle states, and put

```
ell=log_2(L), B=log_2(H/L), alpha=log_2(3),
epsilon=1/[3L*ln(2)], kappa=alpha+epsilon.
```

The certificate traces every odd seed from 3 through 127 to
1. A nontrivial cycle therefore has `L>=129`. Using the
exact comparisons `3^32<2^51`, `ln(2)>1/2`, and
`2/387<1/160`,

```
kappa < 51/32+1/160=8/5,    kappa-1<3/5.           (7)
```

Let `A=sum_i a_i`, `D=2^A-3^m`, and `eta=D/2^A`.
The cycle product gives `D>0` and

```
eta < A*ln(2)-m*ln(3)
    =sum_i ln(1+1/(3n_i)) <m/(3L).
```

EXT-1 gives `eta>=2^-172*m^-341`. Hence

```
L<2^172*m^342/3,
ell<172+342log_2(m).                                (8)
```

This is the only external-input step. No period lower bound
or convergence verification beyond the local check above is
used.

### 4. Rise and end witnesses contradict a long period

Apply the [rise lemma](../rise-lemma/README.md) to the
rotation from (2), in the orientation of forward length `Q`:

```
B <= (kappa^(s+1)-1)*(ell+1+(kappa-1)Q).             (9)
```

The `s` mismatches split the remaining `m-s` positions into
agreeing runs. One has length `t>=m/s-1`. By the
[paired-state run law](../paired-state-run-law.md), the
difference at its end has absolute value at least `2*3^t`.
The law permits an empty run with `t=0`; in the present
range `m>s`, the chosen longest run is positive.
Both states are positive, so

```
ell+B>1+alpha*t,
ell+B+1>alpha*m/s,
m<(2s/3)*(ell+B+1),                                (10)
```

where `3/2<alpha<2` was used in the last two steps.

Put `V=(8/5)^2049`. From (6)-(9),

```
ell+B+1 < V*(ell+1+(3/5)Q) < V*(ell+309).
```

The rational inequality `(8/5)^10<2^7` follows from
`2^23<5^10`. Since `7*2049<10*1435`, this gives
`V<2^1435`. Combining (8) and (10), and using
`4096/3<2^11`,

```
m < 2^1446*(481+342log_2(m)).                       (11)
```

No integer `m>=2^1536` satisfies (11). For a discrete
verification of the unbounded range, choose `d>=1536`
with `2^d<=m<2^(d+1)`. Equation (11) would give

```
2^d < 2^1446*(823+342d).
```

At `d=1536`, `823+342d=526135<2^20`, while
`2^1536>2^1466`. The reverse inequality persists by
induction, because

```
2*(823+342d)-(823+342(d+1))=481+342d>0.
```

This contradiction proves (1).

### 5. Combine the two continued-fraction regimes

Consider a word in the corollary and suppose `den(w)=1`.
The word-cycle correspondence used in the
[four-arc result](../sparse-two-level-four-arc-exclusion/README.md)
supplies a positive odd integer `3x+1` cycle with this exact
valuation word. The unique occurrence of `V` makes the word
primitive. Rotation by `h` has exactly four mismatches,
because the three arcs have positive lengths and `V>=3`.

The generic theorem (1) therefore gives `K(k/m)<m/512`.
But `m>=2^1536>=2^22`, so the all-density conclusion (2a)
of the cited result excludes denominator one whenever
`K(k/m)<=m/512`. This contradiction proves the corollary.
The inverse `k` is taken in the original track orientation
in both arguments. No change of orientation or density
hypothesis is inserted.

## Certificates

Run from the repository root:

```
python3 areas/cycles/results/four-mismatch-inverse-continued-fraction-bound/check_inverse_complexity.py
python3 -O areas/cycles/results/four-mismatch-inverse-continued-fraction-bound/check_inverse_complexity.py
```

The [certificate](check_inverse_complexity.py) checks the
continuant recurrences, determinant signs, coefficient-product
and coefficient-sum bounds, and both end-coefficient cases
on a specified finite grid. It separately checks examples
above the arithmetic cutoff and replays the inverse congruence
and `jQ<=512` conclusion. These finite checks support the
general recurrence proof; they are not a census of possible
cycle periods.

It checks all exact rational constants and the polynomial
induction steps for the two unbounded thresholds, traces the
63 odd seeds from 3 through 127 to 1, and replays the eleven
standard actual `3x+5,7,13,61` cycles. On those controls it
also checks mismatch subadditivity, inverse-rotation
arithmetic, and exact agreeing-run witnesses.

The deterministic [receipt](check_inverse_complexity.json)
is generated with `--write-receipt` and compared byte for
byte on ordinary runs. Checks remain active under
`python3 -O`. No large-period cycle search is asserted.

## Remarks

The [short-rotation result](../short-rotation-mismatch-growth/README.md)
already shows that fixed small mismatch counts cannot occur
at short rotations of sufficiently long integer cycles.
The extra step here is the exact continuant bridge: large
complexity of the inverse rotation supplies a short multiple
with uniformly bounded multiplier. The final threshold is
deliberately conservative. Novelty is undetermined.

The argument is specific to `3x+1`: for a `3x+q` cycle,
the rise constant is `alpha+q/(3L ln(2))`, and the minimum
bound from the gap carries an extra factor `q`. The local
descent also concerns only `3x+1`. The actual-cycle controls
are not excluded by substituting their normalized rational
states for integer states.

No assumption on the number of distinct letters or the
arrangement of the four mismatches was made in the generic
bound. That conclusion is broader than the track family
in the corollary, while still requiring a coprime rotation.
Outside the stated track family, the lower-complexity
rotations remain open. The corollary makes no new exclusion
claim for `m<2^1536`.

## History

- 2026-11-08: proved the inverse-continuant bridge, sharpened
  the multiplier-distance product from 1024 to 512, and
  combined it with the existing rise and end witnesses.
  Same-session audits do not confer independent review status.
- 2026-11-08: combined the generic bound with the merged
  all-density two-level four-arc theorem to remove its
  density and continued-fraction restrictions above `2^1536`.
