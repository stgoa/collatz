---
id: second-largest-label-four-mismatch-bound
kind: result
title: Four distinct track labels force a large second-largest letter
status: written
claim: >
  Raw odd-only 3x+1 clock. Let w be a positive valuation word of
  length m with exactly four distinct labels and exactly four
  mismatches at a shift h coprime to m. Assume D_w>0, den(w)=1,
  m>=2^22 and EXT-1. Its labels are 1<t<U<V. Put z=log_2(m),
  c0=6125/4980736, and let r count all occurrences of U or V.
  Then U-1>(c0*m-175-342*z)/(43884*z+22196).
  For m>=2^24, U-1>m/(2^27*z) and r<(3/5)*2^27*z.
  The maximum label occurs at most 38 times for m>=2^22.
  All cyclic arc orders and all positive arc lengths are covered.
  This is a necessary structural restriction, not an exclusion
  of four-mismatch cycles. No imported convergence or period
  computation, LMN estimate or Chim estimate is used.
authors:
  - Codex four-arc research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex root research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [contiguous-maximum-four-arc-exclusion, single-sawtooth-multirotation-obstruction, four-mismatch-inverse-continued-fraction-bound, denjoy-koksma-height-bound, paired-state-run-law, rise-lemma]
assumes: [musson-collatz-gap-all]
certificates: [check_second_largest.py]
evidence:
  - "check_second_largest.json: exact constants and dyadic induction, local descent, all-order template and profile identities, addend-aware actual-cycle controls"
tags: [cycles, four-arcs, rotation-distance, second-largest-letter, discrepancy, structural-bound]
---

# Four distinct track labels force a large second-largest letter

## Statement

Use the raw odd-only clock. Let `w` have positive valuation
letters, length `m`, four distinct labels, and exactly four
mismatches at a shift `h` with `gcd(h,m)=1`. Suppose
`D_w>0`, `den(w)=1`, `m>=2^22`, and
[EXT-1](../../../../sources/musson-collatz-gap-all.md).
The four labels, in increasing order, are necessarily

```
1<t<U<V.
```

Put `z=log_2(m)` and `c0=6125/4980736`. Then

```
U-1 > (c0*m-175-342*z)/(43884*z+22196).              (1)
```

The right side may be negative near the lower threshold;
(1) is intended literally. For `m>=2^24` it gives the
simpler necessary restrictions

```
U-1 > m/(2^27*log_2(m)),
#{i : w_i>=U} < (3/5)*2^27*log_2(m).                (2)
```

In addition, the maximum label `V` occurs at most
38 times whenever `m>=2^22`.

A coprime track with four mismatches consists of four
nonempty constant arcs. With four distinct labels,
each label occupies exactly one such arc. Thus this
statement covers every ordering of the arcs and all
positive arc lengths. It does not exclude this class,
and does not cover noncoprime tracks. No imported
convergence or period computation, LMN estimate or
Chim estimate is used.

## Proof

The single proper track interval occupied by the maximum
has no nonidentity period, so `w` is primitive. The rotated
intercept identity propagates denominator one to every cut,
giving a nontrivial positive odd integer `3x+1` cycle with
exactly this valuation word and full odd period `m`.

Write

```
alpha=log_2(3), L=min_i n_i, ell=log_2(L),
Y=log_2(L+1), E=sum(w), delta=E-alpha*m,
eta=(2^E-3^m)/2^E.
```

### 1. Common bounds and the maximum multiplicity

The certificate replays exact descent below the starting
value for every odd seed `3<=s<2^17`. A nontrivial positive
cycle therefore has `L>=2^17`. The product identity gives

```
E<8m/5,       0<delta/m<2^-18<1/258,
eta<m/(3L).
```

For example, `L>=129` and the integer comparison
`388^5<2^8*129^5` prove the mean bound. The drift estimate
uses `ln(2)>2/3`. The smallest letter must consequently
be one. EXT-1 then gives

```
eta>=2^-172*m^-341,
ell<172+342log_2(m),       Y<173+342log_2(m).          (3)
```

Let `d` be the multiplicity of `V`. For every cyclic
ordering of the four labels,

```
V_h=sum_i |w_i-w_(i+h)| < 4V.                       (4)
```

The rise/end-witness calculation in the
[contiguous-maximum theorem, section 2](../contiguous-maximum-four-arc-exclusion/README.md)
uses only (4), four mismatches, and `delta<m/258`.
If `V<=m/64`, its inequality is

```
(49/2064)m < 11ell+11
             < 11(172+342log_2(m))+11.
```

The exact dyadic comparison beginning at `m=2^22`
rules this out. Hence `V>m/64`. If `d>=39`, then

```
E-m > 39(V-1) > 39(m/64-1) > 3m/5,
```

contrary to the mean bound. The final margin at `m=2^22`
is `196413/5` and increases thereafter. Thus

```
d<=38.                                             (5)
```

This extraction invokes the earlier elementary proof,
not that node's later Barina-dependent corollary.

### 2. Replacing the maximum controls every arc order

Reverse the track if necessary so `0<h<m/2`, and only
then define its inverse `k=h^(-1) mod m`. Let `K` be the
sum of the positive canonical continued-fraction digits
of `k/m`. The [inverse-complexity bound](../four-mismatch-inverse-continued-fraction-bound/README.md)
and (3) give

```
K<21942log_2(m)+11099.                              (6)
```

Replace every occurrence of `V` by `t`. If `I_1,I_U`
are the indicators of the original one-arc and U-arc,
the template is exactly

```
T=t-(t-1)I_1+(U-t)I_U.                             (7)
```

Each indicator is a single proper cyclic interval on
the track and has total variation two. Therefore
`Var(T)<=2(t-1)+2(U-t)=2(U-1)` for every ordering.
In fact equality holds, but the upper bound suffices.
The two occurrences of the template label `t` need
not be adjacent; no binary-template hypothesis is used.
The [discrete Denjoy--Koksma estimate](../denjoy-koksma-height-bound/README.md),
with chronological step `k` along the track, bounds every
proper chronological factor discrepancy by

```
Delta=2(U-1)(K-1).                                 (8)
```

Put `W=V-t>0` and let `beta>=1` be the template mean.
Then `E=m beta+dW`. Rotate the last maximum along the
track to coordinate one, using the exact pre-drop clock
`e_i=(i+1)/m`. The maximum positions are
`1,1-u,...,1-(d-1)u mod 1`, where `u=h/m`. Define

```
F_d(e)=d*e-#{maximum positions strictly before e}.
```

Represent positions in `(0,1]` and evaluate before each
downward jump. The profile difference across a forward
factor of length `l<m` is `dl/m-N`, where `N` counts its
maximum letters. Subtracting the template mean gives

```
log_2(n_end/n_start)
 = W(F_end-F_start)-dev_T
   +sum_factor log_2(1+1/(3n_i))-delta*l/m.
```

The last two terms together have absolute value at most
`delta`; the discrepancy has absolute value at most
`Delta`. Starting at the actual minimum yields

```
log_2(n_i)<=ell+W(F_d(e_i)-inf F_d)+Delta+delta.      (9)
```

Neither the order of the other arcs nor equality of
any lower labels was used. Since `beta>=1`,
`dW/m<alpha-1+1/258`, so the same exact comparisons
`3^32<2^51` and `3^80<2^127` give

```
W/(alpha*m)<3/(8d),
W/(alpha*m)<6103/(16383d).                          (10)
```

### 3. The profile requires a uniform error

Set

```
epsilon=(ell+Delta+delta+alpha)/(alpha*m).           (11)
```

First suppose `d>=2`. The geometric arguments in
[sections 4--5 of the contiguous-maximum theorem](../contiguous-maximum-four-arc-exclusion/README.md)
apply verbatim to (9)--(10). To specify their scope:

- If `u>=1/d`, `osc(F_d)/d<=2/3`. A four-mismatch end
  witness then forces `epsilon>325/196596>1/1216`.
- If `u<1/d`, the maximum-arc endpoints are exactly
  `1` and `R=1-du`, and the two other mismatch cuts
  are arbitrary distinct points `p,q`. The three
  possible ranks of `R` among these cuts force
  `epsilon>1/(32d)>=1/1216`, by (5).

The earlier geometric proof uses only these two fixed
endpoints and two arbitrary other cuts. It never uses
the two other boundaries having equal outer labels.
Thus every cyclic ordering in the present class is
covered.

For `d=1`, `F_1` is a single sawtooth with pre-drop value
one at its maximum position and infimum zero. The
four genuine cuts, represented in `[0,1)`, are

```
C1={0,-u,p,q} mod 1,
```

with all four points distinct. For rotation `jh`, use

```
Cj=union_(i=0)^(j-1) (C1-i*u).
```

The actual mismatch set at `jh` is contained in this
union. After deduplicating, each consecutive circular
gap `G` supplies `mG-1` agreeing arrows, even when its
endpoints are artificial cuts. The paired-state run
law applies to these agreement subintervals and (9)--(11)
give

```
G < (3/8)max(f(e),f(e+j*u mod 1))+epsilon,
f(0)=1,       f(e)=e for 0<e<1.
```

Because `gcd(h,m)=1` and `m>=2^22`, the reduced
denominator of `u` is `m>12`, and all rotations
`h,...,11h` are nonidentity. The
[single-sawtooth multirotation obstruction](../single-sawtooth-multirotation-obstruction/README.md)
therefore forces `epsilon>=1/1000>1/1216`.
This also covers every faithful boundary configuration
of the cut model, with its prescribed pre-drop values.
Combining the cases,

```
epsilon>1/1216.                                   (12)
```

### 4. Second-largest label and total high multiplicity

Since `ell<Y`, `alpha>3/2`, `alpha<2` and
`delta/m<2^-18`, equations (8), (11)--(12) give

```
Y+2(U-1)(K-1)+2 > c0*m,
c0=(3/2)(1/1216-1/393216)=6125/4980736.              (13)
```

Substitute (3) and (6) into the left side. With
`z=log_2(m)`,

```
c0*m < 175+342z+2(U-1)(21942z+11098).
```

Rearranging proves (1); the denominator is positive,
so no sign hypothesis on its numerator is needed.

For `m>=2^24`, one has

```
175+342log_2(m) < c0*m/2.                           (14)
```

To verify this without rounding, on a dyadic band
`2^j<=m<2^(j+1)` its left side is below `517+342j`.
At `j=24`, the margin `c0*2^23-(517+342*24)` is
`30225/19>0`. Doubling preserves this comparison
because the positive affine bound grows by a factor
less than two. Also `K-1<2^15 z` in this range, and
`c0>1/1024`. Therefore (13)--(14) imply

```
U-1 > c0*m/[4(K-1)] > m/(2^27 z).
```

Finally, if `r=#{i:w_i>=U}`, positivity of all other
excesses and the mean bound give

```
r(U-1)<E-m<3m/5.
```

Together these prove (2). The count includes both
largest labels, regardless of their arc lengths.

## Certificates

Run from the repository root:

```
python3 areas/cycles/results/second-largest-label-four-mismatch-bound/check_second_largest.py
python3 -O areas/cycles/results/second-largest-label-four-mismatch-bound/check_second_largest.py
```

The certificate checks the exact constants, both dyadic
inductions, local descent below `2^17`, and finite
all-order template/profile controls with actual
`3x+q` cycles. It retains the true additive constant
and tests agreement subintervals, including refined
higher-rotation cuts. The eleven shared actual-cycle
fixtures are also replayed. These controls do not
claim a search-based absence theorem.

The two geometric profile bounds are used through
the cited proofs. In particular the single-sawtooth
node has its own complete rational branch certificate;
no floating optimization result enters this transfer.

## Remarks

This forces a second large valuation label, rather
than only the largest label already forced by the
rise lemma. After deleting the two largest-label arcs,
only the two smaller labels remain, and the total
number deleted is at most logarithmic in the period
with the explicit constant in (2). This is a structural
reduction for further arithmetic or weighted-profile
arguments, not a proof that the remaining profiles
or cycles cannot exist.

Although some cited nodes also state Barina-dependent
all-length exclusions, only their explicitly elementary
geometric and local portions are used here. The sole
external input to this statement is EXT-1. Novelty is
undetermined; same-session audits do not change the
`written` status.

## History

- 2026-11-08: extracted the maximum-arc geometry for arbitrary
  four-label order, used the certified singleton model for the
  remaining maximum multiplicity, and derived an explicit
  second-largest-label and combined-multiplicity restriction.
