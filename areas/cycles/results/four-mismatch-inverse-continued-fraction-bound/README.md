---
id: four-mismatch-inverse-continued-fraction-bound
kind: result
title: Inverse continued fractions force rotation mismatch growth
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
  More generally, for every coprime nonidentity rotation h of a
  primitive positive integer cycle with m>=2^40, its mismatch count
  s(h) satisfies K(h^(-1)/m)<2*s(h)*m/log_2(m), under EXT-1 alone.
  This bound uses the actual mismatch count, with no fixed upper bound
  on it. In particular K=O(s*m/log m), uniformly in the rotation.
  A stronger four-mismatch estimate follows from exact integer block
  repetition: without external inputs, K(k/m)<27*n+64*log_2(L+1),
  where n is the number of continued-fraction digits and L the minimum
  state. More precisely, every 1<=Q<m with gcd(p,Q)=1 and
  Qk-pm=+j or -j, j>=1, satisfies m<16*j*log_2(L+1)+27*j*Q.
  All four-arc label patterns and lengths are allowed. Under EXT-1
  the resulting bound is K(k/m)<21942*log_2(m)+11099, at every
  period admitting a primitive four-mismatch integer cycle.
authors:
  - Codex signed-endpoint research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex main research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex four-arc research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [rise-lemma, paired-state-run-law, sparse-two-level-four-arc-exclusion]
assumes: [musson-collatz-gap-all]
certificates: [check_inverse_complexity.py, check_phase_blocks.py]
evidence:
  - "check_phase_blocks.json: four-boundary rational phases, repeated integer blocks, continued-fraction sums and addend-aware actual-cycle controls"
  - "check_inverse_complexity.json: continuant identities and end coefficients, exact cutoff constants, local minimum verification and actual-cycle controls"
  - "check_inverse_complexity.json: exact polynomial induction certificates for the general mismatch-growth bound at m>=2^40"
tags: [cycles, rotation-distance, continued-fractions, rise-lemma, effective-bounds]
---

# Inverse continued fractions force rotation mismatch growth

## Statement

**Logarithmic inverse complexity for four mismatches.** Let a
primitive positive integer cycle of the raw odd-only `3x+1` map
have period `m`, minimum `L`, and exactly four valuation mismatches
under a coprime rotation `h`. Put `k=h^(-1) mod m` in `(0,m)`,
`Y=log_2(L+1)`, and write the canonical continued fraction as
`k/m=[0;a1,...,an]`. The count `n` excludes the initial zero.
Then, without external inputs,

```
K(k/m)<27*n+64*Y,       n<=2*log_2(m)+1.             (R0)
```

The proof covers every four-arc track pattern, arbitrary label
sizes and arc lengths. It gives the stronger intermediate inequality
`m<16*j*Y+27*j*Q` whenever `1<=Q<m`, `j>=1`, `gcd(p,Q)=1`
and `Qk-pm=+j` or `-j`. It applies this inequality to every
proper convergent, including the initial fraction `0/1`.

With EXT-1 and the local minimum replay, `Y<173+342*log_2(m)`,
so (R0) implies

```
K(k/m)<21942*log_2(m)+11099.                         (R0a)
```

The coefficients are `54+64*342=21942` and `27+64*173=11099`.

This is `O(log m)` for four mismatches. Sections 7--9 give the
new proof. The earlier results below remain unchanged, including
the general estimate with no fixed upper bound on mismatch count.
None of these statements excludes every four-mismatch word.

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

**General mismatch-growth bound.** Under the same EXT-1 input,
let a primitive positive odd integer `3x+1` cycle have length
`m>=2^40`. For every `0<h<m` coprime to `m`, put
`s=s(h)` and let `k=h^(-1) mod m` lie in `(0,m)`. Then

```
K(k/m) < 2*s*m/log_2(m),
s > K(k/m)*log_2(m)/(2m).                           (3a)
```

The mismatch count is positive, but need not be at most four.
The conclusion is uniform in `h` and `s`. For a fixed mismatch
bound it gives `K(k/m)=O(m/log m)`, strengthening a fixed
linear-complexity restriction as the period grows. The earlier
four-mismatch cutoff (1) is retained: its numerical bound can
be stronger at particular lengths.

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

### 6. The bound for every mismatch count

Keep the primitive integer-cycle hypotheses and write
`x=log_2(m)`, `s=s(h)>=1`, `K=K(k/m)`. Suppose, contrary
to (3a), that `K>=2sm/x`. Let `n` be the number of continued-
fraction coefficients and `C` their maximum. The continuant
identities in sections 1--2 apply without change.

First, `C>=K/2`. Otherwise `C>=K/n` and
`K-C<=(n-1)m/C`, together with `K-C>K/2`, give

```
K^2<2n(n-1)m,
m<n(n-1)x^2/(2s^2)<=2x^4+x^3.                     (12)
```

For a fully discrete contradiction, choose `d>=40` with
`2^d<=m<2^(d+1)`. Then `n<=2d+2` and (12) would imply
`2^d<(d+1)^3(2d+1)`. Put `P(d)=(d+1)^3(2d+1)`.
At `d=40`, `2^40-P(40)=1099506045175>0`. The polynomial
`2P(d)-P(d+1)`, expanded in `z=d-40`, has coefficients
`[5015898,505238,19056,319,2]`, all positive. Thus the
opposite inequality persists at every larger `d`.

Take the split at a maximal coefficient. In the notation
of section 2, `QR<=m/C<=2m/K<=x/s`. The sum of all the
other coefficients is at most `Q+R<=QR+1<=x+1`. Also
`K>=2m/x>=4(x+1)`: it suffices that
`2^d>=2(d+1)(d+2)`, whose base at `d=40` and doubling
induction are checked exactly. Consequently

```
C>=K-(x+1)>=3K/4,
QR<=4m/(3K)<=2x/(3s).                              (13)
```

The exact inverse congruence again gives a nonidentity
rotation `Rh` with cyclic distance `Q`: here `Q<=2x/3<m/2`.
Its mismatch count `s'` obeys

```
1<=s'<=sR<=2x/3,       Q<=2x/3.                    (14)
```

Sections 3--4 used only a nonidentity rotation and its
actual mismatch count in the rise and end-witness bounds.
Apply them to this rotation. With `ell=log_2(L)` and
`B=log_2(H/L)`, put `c=ell+1+(kappa-1)Q`. Then

```
ell+B+1 <= kappa^(s'+1)*c,
m < (2s'/3)*(ell+B+1).
```

The same local descent gives `kappa<8/5<2^(7/10)`.
EXT-1 still gives `ell<172+342x`. Hence

```
m < (4x/9)*2^(7x/15+7/10)*(173+(342+2/5)x)
  < (8x/9)*2^(7x/15)*(173+343x).                    (15)
```

Finally, in the dyadic band above, let
`F(d)=(d+1)(516+343d)`. Equation (15) would require

```
2^(8d-7) < [(8/9)F(d)]^15.                         (16)
```

At `d=40` the reverse inequality is checked by the integer
comparison `2^313*9^15>4669408^15`. Further,
`4F(d)-3F(d+1)`, expanded in `z=d-40`, has coefficients
`[497750,26241,343]`, all positive. Thus the right side of
(16) increases by less than `(4/3)^15<2^8` at each step,
whereas its left side increases by exactly `2^8`.
The contradiction holds throughout the unbounded range,
proving (3a).

The new quantitative restriction uses the same elementary
continuant bridge, rise lemma and external gap as (1).
It does not impose a hypothesis on the letter amplitudes
or the arrangement of mismatches, and it does not exclude
all coprime rotations or all four-mismatch words.

### 7. Exact repetition bounds do not require expanding blocks

For this new argument assume only a primitive positive integer cycle
of the raw odd-only `3x+1` map and a coprime rotation with exactly
four mismatches. No external input, minimum-state threshold or period
bound is used in sections 7--9. Write `L` for the cycle minimum,
`Y=log_2(L+1)`, `alpha=log_2(3)`, and `rho=3/2`.
Along the `h`-track the word has exactly four constant arcs, with
arbitrary positive lengths and labels; chronological steps advance
by `k=h^(-1) mod m` on that track.

Consider `N>=1` consecutive copies of a positive valuation
block of length `Q<m` and total `S>=Q` inside the cycle.
Let `x_i` be the state at its successive block cuts and
put `d_i=x_(i+1)-x_i`. Since the same affine map applies
at every copy,

```
d_(N-1)=3^(Q(N-1))d_0 / 2^(S(N-1)).
```

All states are integers. Primitivity and `Q<m` give
`d_0!=0`, so `2^(S(N-1))` divides this nonzero integer.
Each positive valuation arrow satisfies
`x_next+1<=rho(x+1)`. Thus

```
2^(S(N-1)) <= |d_0| < rho^Q(x_0+1).
```

Writing `Y0=log_2(x_0+1)` and using `S>=Q` yields

```
NQ < Y0+alpha Q,
log_2(x_N+1) < alpha Y0+alpha(alpha-1)Q.              (R1)
```

Equivalently, with `Z=log_2(x+1)+alpha Q`, such a
segment has length less than its initial `Z`, and
`Z_out<alpha Z_in`. This includes `N=1`.
No sign of `2^S-3^Q` is assumed.

### 8. Every proper rational phase gives a short-regime prefix

The next estimate uses only primitivity and four track
boundaries; it has no restriction on labels or arc lengths. Let `Q,p,j` be integers satisfying

```
1<=Q<m, j>=1, gcd(p,Q)=1, Qk-pm=+j or -j.            (R2)
```

We prove

```
m < 16jY+27jQ.                                     (R3)
```

If `jQ>=m`, this is immediate. Suppose `jQ<m` and start
the chronological word at its minimum. Split its first
`R=floor(m/Q)` complete blocks into blocks of length `Q`.
On the track, their initial phases advance by `+j` or
`-j`. An actual word block at phase `theta` is

```
(f(theta+ks))_(0<=s<Q),
```

where `f` is the actual four-interval track labelling.
Its possible changes occur at four families of `Q`
boundary points, one for each track boundary.
Within each family, the cyclic spacing is at least

```
d=m/Q-j>0.                                         (R4)
```

Indeed `ks=pm*s/Q +/- js/Q`; the first terms form a
uniform `Q`-grid because `gcd(p,Q)=1`, and the perturbation
range is less than `j`. This also covers `Q=1`, where
the sole point in each family has cyclic spacing `m`.

Let `r1<...<r5` be the first five changes of the actual
block pattern, if there are five before `R`.
Each change crosses at least one of the boundary points.
Choose one such event per change. Assign events in
`(min(old,new),max(old,new)]` along the unwrapped phase
coordinate; this convention works in both directions
and prevents a boundary at a cut from being counted
twice. Among the five chosen events two belong to
the same family, so their separation is at least `d`.
Both occur within the first `r5` steps of size `j`, hence
`r5*j>=d` and `r5*Q>=m/j-Q`.

The prefix ending just before the fifth change has at
most five constant block regimes. If there
are fewer changes, use all `R` blocks; they also have
at most five regimes and total length `RQ>m-Q>=m/j-Q`.
In either case we obtain a prefix of length at least
`m/j-Q`, consisting of at most five segments, each a
repetition of one positive `Q`-block. The argument uses the actual word throughout.

Apply (R1) successively from `L`. Its length is less than

```
(1+alpha+alpha^2+alpha^3+alpha^4)(Y+alpha Q).
```

The exact bound `alpha<8/5` implies that the geometric
sum is less than 16 and its product with `alpha`, plus
one, is less than 27. Comparing with `m/j-Q` proves (R3).

### 9. Sum the constraint over all convergents

Write `k/m=[0;a1,...,an]`, with convergents `p_i/q_i`,
`q_(-1)=0`, `q_0=1`. For digit `a_i`, take the preceding
convergent `p/Q=p_(i-1)/q_(i-1)` and
`j=|Qk-pm|`. These are proper convergents, so `Q<m`
and `j>0`. The exact continuant split gives

```
m>=a_i Qj.
```

For example, this is the first term of
`m=a_i Qj+q_(i-2)j+Qj_prev`, with the nonnegative
remaining tail continuant `j_prev`; it includes both
endpoint digits. Applying (R3) gives

```
a_i<27+16Y/q_(i-1).
```

The denominator recurrence gives `q_(i+2)>=2q_i`.
Separating the even and odd indices therefore bounds
the sum of the reciprocals of all preceding denominators
by 4, including the possible two initial denominators 1.
The same recurrence gives `n<=2log_2(m)+1`. Consequently

```
K<27n+64Y,
n<=2log_2(m)+1.                                    (R5)
```

This uses every proper convergent, not a bounded search
for a favourable partial quotient.

## Certificates

The additional [phase-block checker](check_phase_blocks.py) and its
[generated receipt](check_phase_blocks.json) verify the finite phase
and repetition cases behind sections 7--9, including the boundary
conventions, endpoint convergents and actual integer `3x+d` controls
with their addends retained. Run it normally or with `python3 -O`;
`--write-receipt` regenerates its deterministic receipt. It does not
infer the unbounded theorem from the finite census.

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

For (3a), the checker also verifies the integer base
comparisons and polynomial identities for all three dyadic
inductions. Positivity of the shifted polynomial coefficients
certifies every later dyadic band; no finite-period sampling
is substituted for those inductions.

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

- 2026-11-08: added the integer-repetition and four-boundary phase
  argument in sections 7--9, yielding an unconditional minimum-state
  bound on inverse complexity and an EXT-1-only logarithmic bound
  for every coprime four-mismatch rotation. The previous fixed-cutoff
  and arbitrary-mismatch estimates are retained. Same-session audits
  do not promote the node beyond `written`.

- 2026-11-08: proved the inverse-continuant bridge, sharpened
  the multiplier-distance product from 1024 to 512, and
  combined it with the existing rise and end witnesses.
  Same-session audits do not confer independent review status.
- 2026-11-08: combined the generic bound with the merged
  all-density two-level four-arc theorem to remove its
  density and continued-fraction restrictions above `2^1536`.
- 2026-11-08: retained the four-mismatch statements and added
  the uniform bound `K(h^(-1)/m)<2s(h)m/log_2(m)` for
  `m>=2^40`, with the same sole external input EXT-1.
  This extends the inverse-continuant argument to every
  mismatch count; novelty remains undetermined.
