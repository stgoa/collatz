---
id: contiguous-maximum-four-arc-exclusion
kind: result
title: A contiguous maximum arc excludes three-label four-arc words
status: written
claim: >
  Raw odd-only 3x+1 clock. Let a,b,c,d>=1, m=d+a+b+c,
  gcd(h,m)=1, and let A,B,V be pairwise distinct positive
  valuation labels with V>max(A,B). Suppose that a word
  read along a cyclic h-track is V^d,A^a,B^b,A^c.
  Under EXT-1, m>=2^48 and D_w>0 imply den(w)>1.
  With the additional declared Barina convergence input,
  D_w>0 implies den(w)>1 at every length in this family.
  Both lower-label arrangements and arbitrary amplitudes
  are covered. The proof retains the deterministic multispike
  height profile of the maximum letters. The rise and mean
  bounds reduce the maximum multiplicity to d<=38 at large
  periods. For h/m>=1/d a convexity argument bounds the
  profile's oscillation; for h/m<1/d three exact rank cases
  give a contradiction at error at most 1/(32d). The logarithmic
  inverse-complexity bound and an independently checked
  logarithm-gap bootstrap make that error small. Neither
  conclusion uses LMN or the Chim estimate. Maxima on two
  separate track arcs, other four-mismatch
  patterns and noncoprime tracks remain outside this claim.
authors:
  - Codex four-arc research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex root research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [general-three-label-four-arc-exclusion, background-maximum-four-arc-exclusion, rise-lemma, four-mismatch-inverse-continued-fraction-bound, denjoy-koksma-height-bound, paired-state-run-law, cycle-length-lower-bound-from-convergents]
assumes: [musson-collatz-gap-all, barina-2025-convergence-2-71]
certificates: [check_maximum_arc.py]
evidence:
  - "check_maximum_arc.json: exact rank-case margins, profile collision endpoints and discrepancy identities, integer cycle controls, dyadic cutoff and independently reconstructed logarithm-gap bootstrap"
tags: [cycles, four-arcs, rotation-distance, height-profile, discrepancy, effective-exclusion]
---

# A contiguous maximum arc excludes three-label four-arc words

## Statement

Use the raw odd-only clock. Let `a,b,c,d>=1`,
`m=d+a+b+c`, and `gcd(h,m)=1`. Suppose a positive
valuation word read along a cyclic index track is

```
V^d,A^a,B^b,A^c,                                    (1)
```

where `A,B,V` are pairwise distinct and `V>max(A,B)`.
Superscripts count letters. Under
[EXT-1](../../../../sources/musson-collatz-gap-all.md),

```
m>=2^48 and D_w>0  imply  den(w)>1.                  (2)
```

With the additional declared
[Barina convergence input](../../../../sources/barina-2025-convergence-2-71.md),
this exclusion holds at every length. The corollary uses
the [replayed raw odd-period lower bound](../cycle-length-lower-bound-from-convergents/README.md)
`72057431991`; the external convergence computation is
not rerun. The large-period theorem uses only EXT-1
and local descent below `2^17`. Neither conclusion uses
the LMN or Chim estimates.

The maximum occupies one nonempty proper track arc,
of arbitrary length. Maxima on two separate arcs are
not covered. The maximum indicator is a single proper
interval on a coprime track, which has no nonidentity
rotational period; this makes (1) primitive. The case
`d=1` is already the
[singleton-arc theorem](../general-three-label-four-arc-exclusion/README.md).
Below we prove the new case `d>=2`.

## Proof

Assume `D_w>0` and `den(w)=1`. The rotated intercept
identity propagates divisibility by the odd number `D_w`,
giving positive odd integer states with the exact
valuations (1). They form a primitive nontrivial cycle.
Let `L,H` be its minimum and maximum, and write

```
alpha=log_2(3), ell=log_2(L), Y=log_2(L+1),
E=sum(w), delta=E-alpha*m, eta=(2^E-3^m)/2^E.
```

Reverse the track if necessary, exchanging `a,c`, so
`0<h<m/2`, and then define `k=h^(-1) mod m`. All
continued-fraction bounds below use this chosen `h,k`;
no symmetry identity for their continued fractions is
assumed. Put `u=h/m` and let `K` be the sum of the
positive digits in the canonical expansion
`k/m=[0;a1,...,an]`.

### 1. Label and discrepancy bounds

The local replay of odd seeds below `2^17` gives
`L>=2^17`; in particular `L>=129`.
The product identity and exact inequalities
`388^5<2^8*129^5`, `ln(2)>2/3` give

```
E<8m/5,       0<delta<m/2^18<m/258.
```

If both lower labels were at least two, then `E>=2m`,
a contradiction. Thus `{A,B}={1,t}` for some `t>=2`.
Let

```
v=t-1,       W=V-A>0.
```

The minimum begins a positive ones run of length `l`,
followed by a letter `e>=t`. Exact terminal oddness
gives `L+1=2^(l+1)z` with `z` a positive odd integer,
so `l+1<=Y`. The state after this block is at least `L`.
Multiplying its step ratios, with
`kappa=alpha+1/[3L ln(2)]<8/5`, therefore gives
`l+e<=kappa(l+1)`, and hence

```
v<(3/5)Y.                                          (3)
```

Here `kappa<8/5` follows from `alpha<51/32`,
`ln(2)>1/2`, and `2/387<1/160`.

Replace all copies of `V` by the outer label `A`.
The resulting template `U` has one cyclic interval
of each label `1,t` on the track. Write `beta` for
its mean. The discrete
[Denjoy--Koksma bound](../denjoy-koksma-height-bound/README.md)
gives every proper chronological factor discrepancy
at most

```
Delta=2v(K-1).
```

The [logarithmic inverse-complexity theorem](../four-mismatch-inverse-continued-fraction-bound/README.md)
applies to this primitive four-mismatch word and gives

```
K<27n+64Y,       n<=2log_2(m)+1,
Delta<(6/5)Y(27n+64Y).                              (4)
```

Finally, the product and EXT-1 imply

```
eta<m/(3L),       eta>=2^-172*m^-341,
ell<172+342log_2(m),       Y<173+342log_2(m).          (5)
```

### 2. At large periods there are at most 38 maximum letters

For the present track shape,
`V_h=2(V-A)+2|A-B|<4V`. The rise and end-witness
calculation in the
[background-maximum theorem](../background-maximum-four-arc-exclusion/README.md),
section 2, uses only this variation inequality and
`delta<m/258`, not the maximum's multiplicity. Explicitly,
if `V<=m/64` it gives

```
(49/2064)m < 11ell+11 < 11(172+342log_2(m))+11.
```

The same exact dyadic comparison rules this out for
`m>=2^22`. Therefore `V>m/64` in that range.
If `d>=39`, the excess valuation would satisfy

```
E-m > 39(V-1) > 39(m/64-1) > 3m/5,
```

contradicting the mean bound. The final inequality
holds already at `m=2^22`, with margin `196413/5`,
and increases thereafter. Hence

```
m>=2^22  implies  d<=38.                            (6)
```

The statements below treat all `d>=2` analytically;
(6) will only be used to choose a uniform error margin.

### 3. The maximum positions determine a height profile

Rotate the chronological indices so that the last
maximum along the chosen track is at `x=m-1`.
Use coordinates `e=(i+1)/m` in `(0,1]`. The maximum
positions form the multiset

```
X={1-ju mod 1 : 0<=j<d},
F_d(e)=d*e-#{z in X : z<e}.                         (7)
```

Residues are represented in `(0,1]`. For the actual
word these positions are distinct; allowing collisions
will be useful for a continuous estimate below.
At a maximum position, (7) is evaluated before its
downward jump. Its periodic extension has slope `d`
and drops by the appropriate multiplicity after each
maximum position. Put `f_min=inf F_d`.

For a forward chronological factor of length `r<m`,
let `N` count its maximum letters. Then the difference
of profile values at its endpoint states is `dr/m-N`,
including wrapped factors. Since `E=m beta+dW`,
`alpha-beta=dW/m-delta/m`. Write the actual step
increment as `alpha-w_i+epsilon_i`, where
`epsilon_i=log_2(1+1/(3n_i))>0` and their sum is `delta`.
This gives the exact identity

```
log_2(n_end/n_start)
 = W(F_end-F_start)-dev_U
   +sum_factor epsilon_i-delta*r/m.                 (8)
```

The factor discrepancy has absolute value at most
`Delta`; the last two terms together have absolute
value at most `delta`. Starting at the global minimum
and using its profile value at least `f_min` yields

```
log_2(n_i) <= ell+W(F_d(e_i)-f_min)+Delta+delta.      (9)
```

The empty factor is included. This uses a single
factor discrepancy; it does not align the global
minimum with a maximum letter.

Since `beta>=1`,
`dW/m<alpha-1+1/258`. The elementary bounds
`alpha<51/32` and `alpha<127/80` respectively imply

```
W/(alpha*m)<3/(8d),
W/(alpha*m)<(6103/16383)/d.                         (10)
```

For the first, the exact positive margin is
`257/258-255/256=1/33024`. For the second, use
`1-(257/258)(80/127)=6103/16383`.
Define the common error

```
epsilon=(ell+Delta+delta+alpha)/(alpha*m).           (11)
```

### 4. Spread maximum positions have small profile oscillation

Suppose `1/d<=u<=1/2`. We claim

```
osc(F_d)/d <= 2/3.                                 (12)
```

Partition this interval at every collision of maximum
positions, including a collision with coordinate 1.
These occur only when `ju` is an integer for some
`1<=j<=d-1`. Between successive collisions the ordered
positions are affine in `u`. Each value just before
or after a jump is therefore affine in `u`. The
oscillation is the maximum of these affine values
minus their minimum, hence is convex on each cell.
At a collision, coalescing jumps have the same limiting
extreme values as the combined jump. Thus it suffices
to check the cell endpoints, including `u=1/d,1/2`.

Every such endpoint is a reduced rational `p/q` with
`2<=q<=d`. Write `d=Nq+r`, where `N>=1` and `0<=r<q`.
The maximum positions comprise `N` copies of the
uniform `q`-grid and a remaining set of `r` points.
The uniform-grid profile has oscillation 1. A profile
from any `r` points has oscillation at most `r`, since
a positive increment across a circular interval of
length at most 1 is at most `r`. Consequently

```
osc(F_d)<=N+r<=2(Nq+r)/3=2d/3.
```

The last inequality is equivalent to
`r<=N(2q-3)`, which follows from
`r<=q-1<=2q-3` and `N>=1`. This proves (12), including
the collision endpoints.

The four-mismatch agreeing-run witness gives
`H>2*3^(m/4-1)`. Combining it with (9)--(12),

```
1/4 < (2/3)(6103/16383)+epsilon,
epsilon > 325/196596 > 1/1216.                      (13)
```

This disposes of the spread-position case whenever
the common error is at most `1/1216`.

### 5. Clustered maximum positions contradict four end witnesses

Now suppose `0<u<1/d`. The maximum positions are
`1,1-u,...,1-(d-1)u`, without wrapping, and `f_min=0`.
Let `G=F_d/d`, `R=1-du`, and
`J(e)=max(G(e),G(e+u mod 1))`. Directly from the
successive jumps,

```
J(e)=e+u                    for e<=R,
J(e)<=e                     for e>R,
J(e)=e-(d-1)/d              for e>1-u,
J(R)=1-(d-1)u,       J(1)=1/d.                     (14)
```

Threshold equalities are evaluated before the jumps.
The four mismatch coordinates are `1,R,p,q`, where
`p,q` are the other two track boundaries. The actual
points are distinct. They may also be ordered weakly
in a relaxation, keeping zero gaps and assigning `R`
last among any points tied with it.

A circular gap `g` ending at mismatch coordinate `e`
contains `mg-1` agreeing letters. The
[paired-state run law](../paired-state-run-law.md)
and (9)--(11) therefore give

```
g < (3/8)J(e)+epsilon.                             (15)
```

The first gap after 1 is the first coordinate itself.
We prove that the weak inequalities in (15) are
impossible if `epsilon<=1/(32d)`. Let the three
nonfinal coordinates be `e1<=e2<=e3`, including `R`.
The last gap gives

```
e3>=1-3/(8d)-epsilon>=25/32.                       (16)
```

There are three cases.

* If `R=e1`, the first inequality gives
  `u>=(5-8epsilon)/(5d+3)`. Thus
  `R<=(3+8d epsilon)/(5d+3)<=1/4`, and
  `du>=(5d-1/4)/(5d+3)>=3/4>13/32`.
  In particular (16) forces `e3>1-u`.
  The next point satisfies
  `e2<=(8/5)(R+epsilon)<=7/12`.
  Since `(d-1)/d>=1/2`, the last branch of (14) gives
  `e3<=(8/5)(e2-3/16+epsilon)<=41/60<25/32`.

* If `R=e2`, the first inequality gives
  `e1<=(3/5)u+(8/5)epsilon`, while the inequality
  ending at `R` requires
  `e1>=5/8-((5d+3)/8)u-epsilon`.
  Hence `u>=(25-104epsilon)/(25d+39)` and
  `du>=(25d-13/4)/(25d+39)>1/2`.
  Again `e3>1-u`. Its final-branch inequality becomes
  `e3<=1+3/(5d)-(8d/5)u+(8/5)epsilon`
  `<1/5+13/(20d)<=21/40<25/32`.

* If `R=e3`, the last gap gives
  `u<=13/(32d^2)`. The earlier points are at or below
  `R`, so iterating their first-branch inequalities gives
  `e2<=(39/25)u+(104/25)epsilon`
  `<=507/(800d^2)+13/(100d)<=715/3200`.
  But the inequality ending at `R` gives
  `e2>=5/8-((5d+3)/8)u-epsilon>=455/1024`,
  which is strictly larger.

Every case contradicts (16). Therefore

```
epsilon>1/(32d).                                  (17)
```

Combining (6), (13), and (17), every hypothetical
cycle of the new `d>=2` class with `m>=2^22` must satisfy

```
epsilon>1/1216.                                   (18)
```

The spread and clustered arguments are analytic;
no sampled optimization or finite absence inference
is used.

### 6. Effective cutoff and separately sourced closure

By (3)--(5), `ell<Y`, `alpha>3/2`, `alpha<2`, and
`delta<m/2^18`, the error satisfies

```
epsilon < (2/(3m)) B(Y,n)+1/393216,
B(Y,n)=Y+(6/5)Y(27n+64Y)+2.
```

Since `(3/2)(1/1216-1/393216)=6125/4980736`,
(18) gives

```
m < (4980736/6125)B(Y,n).                          (19)
```

For `2^d0<=m<2^(d0+1)`, bound the right side by

```
P(d0)=(4980736/6125)B(342d0+515,2d0+3).
```

This is a quadratic with positive coefficients. At
`d0=48`,

```
P(48)=549617186130624512/30625 < 2^48.
```

For `d0>=48`, `P(d0+1)/P(d0)<=((d0+1)/d0)^2<2`.
The exact base comparison therefore persists on all
larger dyadic intervals, contradicting (19).
This proves the EXT-1-only theorem in the new branch.
The existing singleton theorem supplies `d=1`.

For the all-length corollary, additionally assume
Barina's declared input and its replayed period bound.
It gives `m>=72057431991>2^22`, so (18)--(19) apply.
The theorem just proved gives `m<2^48`. Independently
construct a rational enclosure of `alpha` and verify

```
p/q   =83130157078217/52449289519716 < alpha,
p'/q' =683381996816440/431166034846567 > alpha,
p'q-pq'=1, q'>2^48, q*alpha-p>2^-62.                (20)
```

For every integer pair with `0<m<q'` and positive
`E-m alpha`, write `(m,E)=r(q,p)+s(q',p')`.
Unimodularity makes `r,s` integers. Positivity of
that gap forces `s>=1`, since otherwise `r<0` and
`m<0`; then `m<q'` forces `r<=-1`.
Thus `E-m alpha>q alpha-p>2^-62`. Using
`ln(2)>1/2` gives `eta>2^-64`.
From `eta<m/(3L)` it follows that

```
L<m*2^64/3,       Y<112,       n<=97.
```

Equation (19) then gives

```
m < (4980736/6125)B(112,97)
   =32760462311424/30625 < 2^30 < 72057431991.        (21)
```

This contradicts the declared raw odd-period lower
bound. The exact-gap computation is reproduced here;
it introduces no LMN or Chim dependency.

## Certificates

Run from the repository root:

```
python3 areas/cycles/results/contiguous-maximum-four-arc-exclusion/check_maximum_arc.py
python3 -O areas/cycles/results/contiguous-maximum-four-arc-exclusion/check_maximum_arc.py
```

The standard-library [checker](check_maximum_arc.py)
verifies the rational rank-case margins, profile collision
endpoints, threshold conventions, finite exact identities and
weighted discrepancy controls, local descent, the
dyadic constants and the independent logarithm-gap
bootstrap. It also retains the addends in actual
reduced cycles and the eleven shared `3x+5,7,13,61`
fixtures. The generated [receipt](check_maximum_arc.json)
states all finite ranges. Use `--write-receipt` to
regenerate it. No unbounded claim is inferred from
a finite word census.

## Remarks

The earlier [singleton-arc theorem](../general-three-label-four-arc-exclusion/README.md)
uses a geometric cancellation at the singleton.
For a longer maximum arc, the same coarse post-maximum
height envelope need not contradict the end witnesses.
The new step retains the deterministic multispike
profile (7). If its points are spread, convexity bounds
its total oscillation. If they cluster, the three rank
cases retain its downward jumps. Neither argument
requires additional rotations or a new Farkas certificate.

The case `d=1`, and the case `b=1` after rotating the
track, overlap the earlier singleton theorem. The new
argument also allows `d,b>=2`. If the largest label
occupies both outer arcs, its maximum set has two
components on the track; that situation remains outside
this result.

For `3x+d_add`, the step errors contain `d_add/n_i`,
and the first ones run involves `L+d_add` rather than
`L+1`. The integer-cycle minimum and profile bounds
are not applied to normalized other-addend controls
as if their states were integers.

The logarithm-gap bootstrap reuses the exact method
of the singleton-arc theorem, with its arithmetic
reconstructed by this node's checker. The rotation,
discrepancy and integer-run tools are classical or
already present in the repository. Novelty beyond
the repository is undetermined. Same-session audits
do not confer independent-review or formal status.

## History

- 2026-11-08: retained the multispike maximum profile,
  separated spread and clustered maximum positions,
  and proved the resulting uniform obstruction.
  Separated the EXT-1-only `2^48` cutoff from the
  all-length corollary using the declared
  convergence-derived period input.
