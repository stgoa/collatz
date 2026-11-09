---
id: non-half-period-four-mismatch-exclusion
kind: result
title: A four-mismatch rotation must be the half-period shift
status: written
claim: >
  Raw odd-only 3x+1 clock. Let a nontrivial primitive positive integer
  cycle have m odd states and valuation word w, and suppose a
  nonidentity shift H has exactly four mismatches. Put
  M=m/gcd(H,m). Under EXT-1 alone, every such shift has M=2:
  m is even and H=m/2 modulo m. Hence at most one shift of a
  hypothetical cycle can have exactly four mismatches, and an
  odd-period cycle has none. The half-period case, larger mismatch
  counts and divergent orbits are not settled. The finite geometric
  step covers all orders 3 through 18 using the fact that four
  mismatches occupy one track with four cuts or two tracks with
  two cuts each; the pure eighteen-rotation obstruction handles
  M>18. A full-period gap bootstrap, exact minimum bounds and
  complete local descent below 18000000 close every period.
authors:
  - Codex root research lane (GPT-6; directed by Santiago Armstrong)
  - Codex residue research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex formal research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [free-four-cut-eighteen-rotation-obstruction]
assumes: [musson-collatz-gap-all]
certificates: [check_non_half_period.py]
evidence:
  - "check_non_half_period.json: exhaustive rational polygons, full-period gap bootstrap, complete local descent and actual addend-aware controls"
tags: [cycles, four-mismatch, half-period, rotation-tracks, exact-certificates]
---

# A four-mismatch rotation must be the half-period shift

## Statement

Let `n_i`, with indices modulo `m`, be the distinct positive odd
states of a nontrivial primitive cycle of the raw odd-only `3x+1`
map, with valuation word `w`:

```
2^w_i*n_(i+1)=3n_i+1,       w_i>=1.
```

For a nonidentity shift `H`, let `s(H)` count indices where
`w_i!=w_(i+H)`, and put `M=m/gcd(H,m)`. Under
[EXT-1](../../../../sources/musson-collatz-gap-all.md),
every shift with `s(H)=4` has order two:

```
m is even,       H=m/2 modulo m.                      (1)
```

There is at most one such shift. If the least odd period `m` is
odd, no shift has exactly four mismatches. There is no restriction
on the letters or their multiplicities, and no coprimality
assumption on `H`.

This does not exclude the half-period case or all cycles. The
pure geometric lemma below is unconditional. The cycle exclusion
uses EXT-1 and finite computations proved by this node's own
certificate; it imports no convergence bound or cycle-period
lower bound. The earlier two-input conclusion is retained in
History.

## Proof

### 1. Four mismatches occupy at most two tracks

Write `g=gcd(H,m)`, `M=m/g` and, after reversing the shift if
necessary, `H=a*g` with `0<a<M/2` and `gcd(a,M)=1`.
Reversing preserves the mismatch count and order. We are considering
`M>=3`, so equality with a half-period is absent.

The orbits of addition by H are exactly the residue classes modulo
g. Each is a cyclic track of M positions. A nonconstant cyclic
track has at least two changes: if just one adjacent pair differed,
the other M-1 equalities around the track would equate that pair.
Thus four total mismatches have exactly one of two distributions:

- one track contributes four mismatches;
- two tracks contribute two mismatches each.

A position in track `r`, `0<=r<g`, has normalized state coordinate

```
i/m=(k+x)/M,       x=r/g,       k in {0,...,M-1}.       (3)
```

Distinct tracks have distinct phases x. Consequently the four
mismatch cuts have one of the forms

```
C={(k+x)/M: k in K},                  |K|=4;           (4a)
C={(k+x)/M: k in K} union
  {(l+y)/M: l in L},                  |K|=|L|=2,      (4b)
```

where `0<=x<1` in (4a), and track names in (4b) are chosen so
`0<=x<y<1`. The sets K and L contain distinct integers between
zero and M-1. The finite geometric problem may allow arbitrary
real phases in these intervals; this enlarges the actual rational
phase class and preserves the implication.

### 2. The finite geometric lemma

Set `R=37/100`, `e_0=1/750`, and
`f(0)=1`, `f(t)=t` for `0<t<1`, reducing arguments modulo one.
For each `3<=M<=18`, each reduced numerator `0<a<M/2`, and
every C of form (4a) or (4b), put

```
h=a/M,
C_j=union(C-i*h: 0<=i<j),       1<=j<=M-1,             (5)
D_j(e)=gap_j(e)-R*max(f(e),f(e+j*h)).
```

Coincident cuts are removed. The circular gap ends at e and starts
at the preceding distinct cut. The lemma is

```
max_(1<=j<=M-1,e in C_j) D_j(e) >= e_0.               (6)
```

Every shift used in (5) is nonidentity. No integrality of states or
cycle equation enters (6).

First consider generic phases `0<x<y<1`. For (4a), use an unused
dummy y with `x<y<1`; it does not occur in any cut. Define the
discrete level sets

```
K_j={(k-i*a) mod M: k in K, 0<=i<j},
L_j={(l-i*a) mod M: l in L, 0<=i<j}.                  (7)
```

These are sets, so repeated translates within a track are
deduplicated exactly. A cut in the first track is (k+x)/M and one
in the second is (l+y)/M. Their entire circular order is obtained
by sorting their discrete level first, and their phase second.
At equal levels, the x-track precedes the y-track. This order
does not depend on the particular generic x and y.

Let an endpoint have level k and phase z, with the preceding cut
having level k' and phase z'. Its partner has the same phase and
level `k''=(k+j*a) mod M`. Both points are nonzero in the generic
region, so

```
M*gap_j(e)=k-k'+z-z'+M*I,
M*max(f(e),f(e+j*h))=max(k,k'')+z,                    (8)
```

where I is one only for the first endpoint in the sorted list,
and zero otherwise. Thus `D_j(e)<e_0` is exactly the strict
affine inequality

```
z-z'-R*z+k-k'+M*I-R*max(k,k'')-M*e_0 < 0.            (9)
```

All coefficients are rational. A generic counterexample to (6)
would satisfy every row (9) together with `0<x<y<1`.

### 3. Exhaustive exact polygon clipping

For each M and a, enumerate every four-element K for (4a), and
every ordered pair of two-element sets K,L for (4b). Thus the
number of discrete families per shift is

```
binom(M,4)+binom(M,2)^2.                              (10)
```

Every track pattern in section 1 is included. Empty four-element
families when M=3 are handled automatically.

Start with the closed triangle `0<=x<=y<=1`, whose vertices are
`(0,0),(1,1),(0,1)`. Intersect it successively with the closed
half-planes obtained by replacing the strict signs in (9) by
non-strict signs. The checker computes each intersection exactly:
an edge whose endpoint row values have opposite signs crosses
the new boundary at affine parameter

```
t=value_at_start/(value_at_start-value_at_end).
```

Endpoints already on the permitted side are retained. Every
coordinate is a rational fraction; there is no numerical tolerance.
This is ordinary convex-polygon half-plane clipping, so at each
step the polygon is exactly the preceding polygon's intersection
with the new half-plane. Its doubled area is the absolute value
of the cyclic cross-product sum.

A strict generic solution would have an open neighborhood
satisfying the finitely many constraints. Its closed feasible
polygon would therefore have positive area. An empty polygon
or a polygon of zero area excludes such a solution. It is safe
to stop that family's enumeration as soon as this occurs;
remaining inequalities could only shrink the feasible set.

The complete deterministic check covers 50 reduced shifts up
to reversal and 468340 discrete families over M=3 through 18.
After 571465 affine rows in total, every family has zero feasible
area; none survives. A positive-area survivor is a failure of the
certificate; the program has no search cutoff and trusts no saved
solver output. This exact replay proves (6) for generic phases.

### 4. Zero phases and structural coincidences

Actual two-track phases are distinct. The only nongeneric
phase boundary still needing coverage is a phase equal to zero.
Suppose a configuration at that boundary violated (6) strictly.
Translate every cut a sufficiently small common distance to
the left, keeping h fixed. All circular gaps are unchanged.
Each endpoint or partner formerly at zero approaches it from
the left, so its f value tends to 1, exactly the specified
value at zero. All other heights vary continuously.

The zero-phase track is now represented with a phase just below
one and with every discrete level reduced by one modulo M.
In the two-track case, swap the track names if necessary to
restore x<y. The enumeration includes all resulting K,L.
Distinct phases stay distinct. In the one-track case, choose
any dummy y between the perturbed x and one.

Coincidences within each track remain identical under this
translation; they were already removed in (7). They do not
create additional gaps or require independent perturbations.
All finitely many strict deficits remain below e_0 for a
sufficiently small left translation. This would give a generic
counterexample already excluded in section 3. Hence (6)
includes the phase-zero boundary.

### 5. The same geometric margin covers every order above two

For `M>18`, the strengthened parameter case of the
[pure eighteen-rotation obstruction](../free-four-cut-eighteen-rotation-obstruction/README.md)
uses the same coefficient `R=37/100` and margin `e_0=1/750`.
It applies to any four distinct cuts, because every `jH`,
`1<=j<=18`, is nonidentity. For `3<=M<=18`, use (6) with
all `j=1,...,M-1`. Consequently, in either order range, a
simultaneous family of inequalities

```
gap_j(e)<(37/100)*max(f(e),f(e+j*h))+epsilon
```

forces

```
epsilon>=1/750.                                      (11)
```

Only the pure geometric result is imported here. We derive the
state transfer and period closure below, so the earlier high-order
cycle theorem and its convergence input are not dependencies.

### 6. Transfer in the full odd-state clock

Rotate the actual cycle so `n_0=L=min_i n_i`. Put

```
alpha=log_2(3),       ell=log_2(L),
E=sum_i w_i,         delta=E-m*alpha>0.
```

Multiplying all step equations gives

```
delta=sum_i log_2(1+1/(3n_i)).                         (12)
```

For `0<=i<m`, the prefix equations and `w_i>=1` imply

```
log_2(n_i)
 =ell+i*alpha-sum_(k<i) w_k
       +sum_(k<i) log_2(1+1/(3n_k))
 <=ell+(alpha-1)*i+delta
 <=ell+(alpha-1)*m*f(i/m)+delta.                      (13)
```

The value `f(0)=1` deliberately enlarges the bound at the minimum.
This is an envelope in actual state-index order, with no assumption
on a maximum letter or on the number of height drops.

Let `C` be the four mismatch cuts for H. Telescoping comparisons
shows that the mismatch set for `jH` is contained in `C_j`: if
all successive H-comparisons agree, the first and last letters
agree. Thus a positive circular gap G between successive distinct
cuts of `C_j`, ending at `e=b/m`, contains exactly

```
r=m*G-1>=0                                           (14)
```

agreeing arrows, starting just after the preceding cut. This is
valid even when a refined cut is artificial, meaning that the
jH-comparison agrees there.

Subtract the paired step equations on those r arrows. If F is
the sum of their common valuations, their signed differences obey

```
2^F*d_end=3^r*d_start.
```

Primitivity and the nonidentity of jH make both differences
nonzero. Both are even because the actual states are odd.
Coprimality of 2 and 3 therefore gives a nonzero integer t with

```
d_start=2^(F+1)*t,       d_end=2*3^r*t.
```

This also holds for the empty run `r=F=0`. Positive endpoint
states consequently satisfy

```
max(n_b,n_(b+jH))>abs(d_end)>=2*3^(m*G-1).            (15)
```

Combining logarithms of (15) with (13) gives

```
G<((alpha-1)/alpha)*max(f(e),f(e+j*h))
       +(ell+delta+alpha-1)/(alpha*m).
```

The exact integer comparisons

```
3^12>2^19,       3^63<2^100
```

give `alpha>19/12` and `(alpha-1)/alpha<37/100`.
Enlarging the error to

```
epsilon=(ell+delta+alpha)/(alpha*m),                  (16)
```

we obtain all the geometric inequalities in section 5.
Hence every hypothetical cycle with `M>=3` satisfies (11).
No shortcut clock or half-period clock has been substituted for m.

### 7. EXT-1 reduces the full period below 24000

The certificate checks that every odd seed `3<=s<18000000`
reaches a smaller positive odd integer. Strong induction, with
base 1, excludes a nontrivial cycle minimum in that range;
the raw fixed point at 1 also cannot belong to a nontrivial cycle.
In particular `L>=2^17`. From (12), `ln(1+x)<x` and `ln(3)>1`,

```
delta/(alpha*m)<1/(3L*ln(3))<1/393216.
```

For completeness, `ln(3)>1` follows from `exp(1)<3`: the
exponential series tail is less than 1 because `k!>=2^(k-1)`
for `k>=2`, strictly for `k>=3`. Using `alpha>19/12` in (16),

```
epsilon<[(12/19)*ell+1]/m+1/393216.                  (17)
```

Define the full-period gap

```
eta=1-3^m/2^E.
```

The product of the arrows gives

```
eta=1-product_i(1-1/(3n_i+1))
   <=sum_i 1/(3n_i+1)<m/(3L).                        (18)
```

EXT-1 states `eta>=2^-172*m^-341`, so

```
ell<172+342log_2(m).                                 (19)
```

For `2^d<=m<2^(d+1)`, (17)--(19) bound epsilon above by

```
A_d=[12*(172+342*(d+1))+19]/(19*2^d)+1/393216.
```

Writing its variable numerator as `N_d=12*(172+342*(d+1))+19`,
we have `N_(d+1)=N_d+4104` and `2N_d-N_(d+1)>0` for
`d>=22`. Thus A_d decreases in those bands. At d=22,

```
1/750-A_22=3591763/29884416000>0.
```

This contradicts (11) whenever `m>=2^22`, proving

```
m<2^22.                                             (20)
```

We now sharpen the gap using a complete exact scan over the
ordinary full exponents `1<=m<2^22`. An 80-term atanh expansion
with its positive tail bound gives the outward enclosure

```
125573666586150569315490533898 /2^96 < alpha
 <125573666586150569315490533899 /2^96.                (21)
```

Specifically, for v=2 and v=3 put `z=(v-1)/(v+1)` and use

```
2*sum_(j=0)^79 z^(2j+1)/(2j+1) < ln(v)
 <2*sum_(j=0)^79 z^(2j+1)/(2j+1)
       +2*z^161/[161*(1-z^2)].
```

The ratio of opposite log endpoints, rounded outward to denominator
`2^96`, proves (21). For every m in (20), the two scaled endpoints
have the same integer part, and the upper endpoint's distance
from the next integer exceeds `2^-25`. The smallest certified
complement numerator is `7373341559091880256221` at `m=190537`,
which is greater than `2^71`.

Since E is an integer with `E>m*alpha` and `ln(2)>1/2`, the positive
natural-log gap `xi=E*ln(2)-m*ln(3)` exceeds `2^-26`.
The elementary estimate
`1-exp(-xi)>=min(xi/2,1/2)` for `xi>0` then gives

```
eta>2^-27.
```

Together with (18) and (20), this yields
`L<2^49/3<2^48`, hence `ell<48`. Substituting in (17),

```
epsilon<595/(19*m)+1/393216.
```

At `m=24000` the difference from `1/750` is
`8083/311296000>0`; the upper bound decreases for larger m.
Thus (11) forces

```
m<24000.                                            (22)
```

### 8. Exact minimum bounds close every remaining period

For each integer `1<=m<=23999`, compute

```
P_m=3^m,       E_m=bit_length(P_m),
gap_m=2^E_m-P_m,
U_m=m*2^E_m/(3*gap_m).
```

Here `E_m` is exactly the least integer E with `2^E>3^m`.
For any possible actual E, its gap eta is at least
`gap_m/2^E_m`; therefore (18) implies `L<U_m`.

The exact certificate checks every m in (22). For 23994 of them,
`U_m<18000000`, contradicting the complete local descent already
used in section 7. The remaining five periods are:

| Full odd period m | E_m | ceil(U_m) | h=bit_length(ceil(U_m)) |
|---:|---:|---:|---:|
| 12941 | 20511 | 22374667 | 25 |
| 13606 | 21565 | 30408724 | 25 |
| 14271 | 22619 | 45091226 | 26 |
| 14936 | 23673 | 80500006 | 27 |
| 15601 | 24727 | 285820187 | 29 |

For these periods, `L<U_m<=ceil(U_m)<2^h`, so `ell<h`.
For each row the certificate verifies

```
[(12/19)*h+1]/m+1/393216<1/750.
```

The largest of the five upper bounds is
`125681783/96683556864`, at `m=12941`, still strictly less
than `1/750`. Equation (17) contradicts (11) for these final
five periods as well. Hence no M>=3 is possible under EXT-1.
A nonidentity rotation has M>=2, leaving exactly M=2, which is (1).

## Certificates

The self-contained standard-library checker is
[`check_non_half_period.py`](check_non_half_period.py).
Run from the repository root with Python 3.10 or later:

```
python3 areas/cycles/results/non-half-period-four-mismatch-exclusion/check_non_half_period.py
python3 -O areas/cycles/results/non-half-period-four-mismatch-exclusion/check_non_half_period.py
```

The generated [receipt](check_non_half_period.json) records the
complete discrete geometry coverage, exact clipping totals,
direct modular comparisons and actual positive-addend controls.
It also verifies all 4194303 full-period logarithmic intervals,
all 23999 final power/minimum comparisons, the five residual
geometric bounds and complete local descent below 18000000.
The descent covers 8999999 odd seeds and 31421072 odd steps;
its longest trace has 181 steps, at seed 13421671. A seed is
followed until it first reaches a smaller odd number; these
are finite induction certificates, not a quoted convergence bound.

The default command verifies the generated receipt;
`--write-receipt` regenerates it. The exhaustive small-order
mathematical step is generated from M, a, K and L; it does not
depend on a saved list of numerical certificates. The high-order
pure geometry has its own separately cited exact certificate.

The direct modular controls compare the affine-row evaluations
with actual circular gaps and paired heights. The cycle controls
retain the existing 788 actual primitive positive-addend cycles,
21008 arrows and 104208 refined agreement runs, including both
track partitions and shift gcds 1, 2 and 3. They exercise 53960
artificial cuts and 148832 raw-cut coincidences. All eleven
shared positive-addend fixtures are also replayed. These controls
validate the formulas; the complete polygon computation is the
finite small-order absence proof.

Every control retains its actual addend d. The paired run
identity cancels a common addend, while (12) for `3x+d` has
`d/(3n_i)` in place of `1/(3n_i)`. The small drift budget and
local convergence argument are specific to `d=1`; the known
positive cycles for other addends are not normalized into
integer `3x+1` cycles.

The half-period boundary is checked separately: for M=2,
`h=1/2` and `C={0,1/4,1/2,3/4}`, the single nonidentity
rotation has maximum deficit `-11/400` at `R=37/100`.
This is a genuine two-track cut configuration and survives
even at zero error. The geometric method therefore does not
remove the remaining order two.

## Remarks

The free-cut model admits controls at several small orders.
Their four cuts need not obey the track structure forced by an
actual mismatch set. The finite-order improvement imposes that
necessary structure before enumerating the phase variables;
no letter-value assumption is added.

The sharper coefficient is essential to the new margin. The receipt
retains an exact order-18 two-track configuration with maximum
deficit `293/270000<1/750` at `R=3/8`; `R=37/100` excludes
that same configuration. This is a geometric control, not a
word or cycle construction.

Under EXT-1, the general four-mismatch question is now the
half-period question. For M=2, four mismatches mean exactly
two unequal pairs between the half-words. The signed-endpoint
and near-doubled results address subclasses, but unrestricted
half-word changes remain open.

The transfer is proved here without using the earlier
[high-order cycle theorem](../high-order-four-mismatch-exclusion/README.md).
That theorem remains a valid earlier result with its recorded
input scope. The present proof needs only the pure geometric
obstruction, EXT-1 and the internal finite certificate.

This is a written conditional result, not a Lean formalization.
Exact certificates and same-session audits do not confer
independent-session reviewed status. Novelty outside the repository
is undetermined. Neither all cycles nor the Collatz conjecture
are excluded.

## History

- 2026-11-08: used the cyclic-track partition of four mismatches
  to reduce the remaining geometry to exact polygons in two
  phase variables. Exhausted all orders 3 through 18 and combined
  the result with the high-order theorem. The original claim was
  `m<2^26` under EXT-1 and all-length exclusion of M>=3 after
  importing the separate Barina-dependent period lower bound.
- 2026-11-08: strengthened the small-order geometric parameters
  to `R=37/100`, error `1/750`, and used the matching strengthened
  pure high-order obstruction. Re-derived the actual-state
  transfer, then closed all periods by the full-clock logarithmic
  scan, exact power bounds and complete local descent below
  18000000. The current claim therefore rests on EXT-1 alone;
  the original two-input conclusion remains valid as an earlier
  weaker result. No change is made to the unresolved half-period
  case.
