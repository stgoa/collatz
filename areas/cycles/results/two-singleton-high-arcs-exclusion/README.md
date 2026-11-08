---
id: two-singleton-high-arcs-exclusion
kind: result
title: Two high singletons are excluded by two rotation witnesses
status: written
claim: >
  Raw odd-only 3x+1 clock. Let b,d>=1, m=b+d+2,
  0<h<m, gcd(h,m)=1, and let A,B,U,V be pairwise
  distinct positive valuation labels with min(U,V)>max(A,B).
  Suppose the cyclic h-track word is U,A^b,V,B^d or U,V,A^b,B^d,
  up to rotation and reversal.
  Under EXT-1, D_w>0 and den(w)=1 force m<=418657053;
  thus m>=2^29 and D_w>0 imply den(w)>1.
  With the additional declared Barina convergence input,
  D_w>0 implies den(w)>1 at every length in this class.
  The unequal two-drop height profile is dominated by a
  single sawtooth after alignment at a post-drop minimum.
  The simultaneous h and 2h cut systems for that dominating
  profile require error at least 5/2384, certified by exact
  nonnegative rational combinations on 57 complete cells across
  opposite and both aligned adjacent placements. Longer high arcs
  and noncoprime tracks are outside the claim. Neither conclusion
  uses LMN or Chim.
authors:
  - Codex four-arc research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex root research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [clustered-two-maximum-arcs-exclusion, four-mismatch-inverse-continued-fraction-bound, denjoy-koksma-height-bound, paired-state-run-law, cycle-length-lower-bound-from-convergents]
assumes: [musson-collatz-gap-all, barina-2025-convergence-2-71]
certificates: [check_two_rotations.py, check_singleton_highs.py]
evidence:
  - "check_two_rotations.json: complete affine-cell coverage, full-cell branch validation and exact rational dual witnesses"
  - "check_singleton_highs.json: exact numerical closure, pinned arithmetic replay and addend-aware actual-cycle controls"
tags: [cycles, four-arcs, rotation-distance, unequal-weights, height-profile, effective-exclusion]
---

# Two high singletons are excluded by two rotation witnesses

## Statement

Use the raw odd-only clock. Let `b,d>=1`, `m=b+d+2`,
`0<h<m`, and `gcd(h,m)=1`. Suppose the word read
along the cyclic h-track is

```
U,A^b,V,B^d   or   U,V,A^b,B^d,                     (1)
```

up to rotation and reversal, where the four labels
are pairwise distinct positive integers and
`min(U,V)>max(A,B)`. Under
[EXT-1](../../../../sources/musson-collatz-gap-all.md),

```
D_w>0 and den(w)=1 imply m<=418657053<2^29.           (2)
```

With the additional declared
[Barina convergence input](../../../../sources/barina-2025-convergence-2-71.md),
`D_w>0` implies `den(w)>1` at every length. Only this
last corollary uses the imported computation, through
the [replayed full odd-period lower bound](../cycle-length-lower-bound-from-convergents/README.md)
`72057431991`. The external convergence computation
is not rerun. The core uses local descent below
`2^17`; neither conclusion uses LMN or Chim.

The high labels occupy two singleton track arcs.
The other two arcs are nonempty; the highs may be
opposite or adjacent. Longer high arcs are not covered. A unique
occurrence of `U` makes (1) primitive. Its coprime
track has exactly four mismatches at `h`.

## Proof

Assume `D_w>0` and `den(w)=1`. The rotated intercept
identity gives a nontrivial primitive positive odd
integer cycle with exactly this valuation word.
Put

```
alpha=log_2(3), L=min_i n_i, ell=log_2(L),
Y=log_2(L+1), E=sum(w), delta=E-alpha*m,
eta=(2^E-3^m)/2^E.
```

### 1. A controlled binary template retains both high weights

The local descent, minimum-run, and product estimates
from the [clustered-two-arcs theorem](../clustered-two-maximum-arcs-exclusion/README.md)
apply without an equal-weight hypothesis:

```
L>=2^17, E<8m/5, 0<delta/m<2^-18,
eta<m/(3L), Y<173+342log_2(m).                       (3)
```

The last bound uses EXT-1. If both lower labels
were at least two, the mean in (3) would fail.
Thus `{A,B}={1,t}` for some `t>=2`. The maximal
integral ones run beginning at `L` gives
`t-1<(3/5)Y`.

Reverse the track if necessary so `u=h/m<1/2`,
and define the inverse `k=h^(-1) mod m`. Let `n`
be the number of positive canonical continued-
fraction digits of `k/m`, and let `K` be their sum.
Replace both high letters by `t`. The template has
one track interval of each label `1,t`, regardless
of which lower label precedes which high letter.
Its discrepancy is at most

```
Delta=2(t-1)(K-1)<(6/5)Y(27n+64Y),
K<27n+64Y,        n<=2log_2(m)+1,                   (4)
```

by the [logarithmic inverse-complexity bound](../four-mismatch-inverse-continued-fraction-bound/README.md)
and [Denjoy--Koksma estimate](../denjoy-koksma-height-bound/README.md).
Both use the chosen inverse clock `k`.

Write the two positive excess weights as
`w_0,w_1` and put `S=w_0+w_1`. If the template mean
is `beta`, then `E=m beta+S`, so `beta>=1` gives

```
S/(alpha*m)<3/8.                                   (5)
```

For example, the weaker local estimate
`delta/m<1/258`, `alpha<51/32`, and
`257/258-255/256>0` prove (5) directly.

### 2. Dominate the unequal profile without equating its weights

Use chronological coordinates `(i+1)/m` and evaluate
profiles before their downward jumps. The exact
profile has slope `S`, one drop of size `w_0`, and
one of size `w_1`. Its minimum is immediately after
one of those drops. Rotate to put that drop at zero,
let the other high point be `v`, and write
`lambda=w_0/S`, relabelling the weights at this cut.
Then `0<v<1`, `0<lambda<1`, and `v>=1-lambda`.
The normalized profile with post-minimum zero is

```
g(0)=lambda,
g(s)=s                    for 0<s<=v,
g(s)=s-(1-lambda)          for v<s<1.                (6)
```

The inequality on `v` is exactly nonnegativity of
the post-drop value at the other high point.
In particular, (6) is pointwise at most the
single pre-drop sawtooth

```
f(0)=1,             f(s)=s for 0<s<1.               (7)
```

This domination retains the unequal weights in the
exact profile and then bounds them; it does not
substitute the equal-maximum profile.

For every proper chronological factor of length
`l`, the weighted profile increment is
`Sl/m` minus the sum of its high excess weights.
As in the exact profile identity of the clustered
node, the discrepancy and drift errors are at most
`Delta+delta`. Starting at the minimum gives

```
log_2 n_i<=ell+S*g(e_i)+Delta+delta.                 (8)
```

For opposite highs, the exact mismatch cut set at `h` is

```
C1={0,-u,v,v-u} mod 1.                              (9)
```

Its four members are distinct:
`v!=0,u,1-u`. For adjacent highs the aligned high
positions are either `0,u` or `-u,0`. The remaining
lower-label boundary is a free point `p`, so the
corresponding genuine four-cut sets are

```
C1+={-u,0,u,p},       C1-={-2u,-u,0,p} mod 1.
```

In either case all four points must be distinct.
For opposite highs at `2h`, use the possibly larger set

```
C2={0,-u,-2u,v,v-u,v-2u} mod 1.                     (10)
```

For either adjacent placement, use `C2=C1 union
(C1-u)` instead. In all three cases, `mis(2h)` is contained in
`mis(h) union (mis(h)-h)`. Coincident points in (10)
are deduplicated; remaining extra points are harmless
artificial cuts. Consecutive cuts with circular gap
`G` leave `mG-1` agreeing arrows, even when one of
the cuts is artificial. The rotation `2h` is
nonidentity because `m>=4` and `gcd(h,m)=1`.
The bound applies to these agreement subintervals,
not only to maximal agreeing runs. The [paired-state run law](../paired-state-run-law.md),
(5), (7), and (8) therefore give simultaneously,
for `j=1,2` and every gap of `Cj` ending at `e`,

```
G < R*max(f(e),f(e+j*u mod 1))+epsilon,
R=3/8,
epsilon=(ell+Delta+delta+alpha)/(alpha*m).           (11)
```

The value at a wrapped zero is the pre-drop value
one, not its right-hand limit zero.

### 3. A complete exact affine-cell obstruction

For all `0<u<1/2`, `0<v<1`, `v!=u,1-u`, the weak
version of the two cut systems (11) forces

```
epsilon>=5/2384.                                   (12)
```

The adjacent cut systems obey stronger respective
bounds `1/168` and `1/232`, so (12) applies to all
placements. Here is a finite exact proof, with no numerical
optimizer assumption. The orders of (9)--(10),
all wrap choices, and all paired-maximum branches
are fixed off the four lines

```
L1=v-u, L2=v-2u, L3=1-u-v, L4=1-2u-v.              (13)
```

The coordinate forms are `0,1-u,1-2u,v` and the
wrapped representatives of `v-u,v-2u`. For a cut
`e>0`, the larger value in (11) is `e+ju` if that
is below one, one if it equals one, and `e` after
wrapping; for `e=0` it is one. Thus (13) contains
all branch boundaries. The eight nonempty open
cells have these sign vectors and certified bounds:

| Signs of `(L1,L2,L3,L4)` | Lower bound on epsilon |
|---|---|
| `(-,-,+,-)` | `5/2384` |
| `(-,-,+,+)` | `11/312` |
| `(+,-,-,-)` | `83/1976` |
| `(+,-,+,-)` | `1/232` |
| `(+,-,+,+)` | `5/1352` |
| `(+,+,-,-)` | `1/12` |
| `(+,+,+,-)` | `1/16` |
| `(+,+,+,+)` | `5/104` |

The lines `L1=0,L3=0` erase an h-boundary and are
excluded. The permitted lines `v=2u` and `v=1-2u`
are each split at `u=1/4,1/3`. Their six open
intervals have respective certified bounds

```
v=2u:     5/104, 1/16, 1/12;
v=1-2u:   1/16, 1/232, 1/24.
```

The `u=1/3` endpoints lie on excluded h-boundary
lines. The sole allowed intersection is
`(u,v)=(1/4,1/2)`, whose bound is `1/16`.
The rectangle edges are outside the stated domain.
These eight open cells, six open intervals and one
point exhaust every allowed opposite parameter pair.

For the adjacent placements use coordinates `(u,p)`.
The complete interior dividing lines are

```
C1+: p=u, p=2u, u=1/3, p=1-2u, p=1-u;
C1-: p=u, p=1-3u, u=1/3, p=1-2u,
     p=2-3u, p=1-u.
```

Each arrangement has eleven nonempty open polygons,
nine permitted open edges, and one permitted vertex.
Edges or vertices with fewer than four h-cuts are
excluded. The certificate constructs the complete
polygon arrangement, then every edge and vertex,
and tests the same exact witness systems on all
21 strata. Its minimum bounds are `1/168` for `C1+`
and `1/232` for `C1-`. Thus the three placements
have 57 strata in total. Every line is obtained from
a raw cut, raw paired point, or raw cut difference
crossing an integer; no other wrap, ordering, or
maximum branch is possible.

On each cell, write its linear domain inequalities
as `A_i*u+B_i*v+C_i*epsilon>=D_i`, and append the
affine forms of the gap inequalities in (11).
The [geometry certificate](check_two_rotations.py)
provides nonnegative rational coefficients whose
weighted left side is exactly `epsilon`; the
weighted right side is the stated bound. It also
verifies every branch and affine formula over the
whole cell by exact linear sign tests at all its
vertices, including the permitted one-dimensional
cells. Thus a sample point only selects a branch;
it is never the evidence that the branch is valid.
The [generated receipt](check_two_rotations.json)
records the exact combinations and cell coverage.

For example, in the minimizing cell, take
`u=129/298`, `v=65/298`. The three active second-
rotation witnesses have deficit `5/2384`, and all
other deficits are smaller. This shows sharpness
for the dominating-sawtooth relaxation. It is not
an admissible unequal-weight profile or an asserted
cycle: equality in the domination would require
a zero excess weight. Sharpness is not needed for
the cycle exclusion.

### 4. Numerical closure with separated inputs

Put `B(Y,n)=Y+(6/5)Y(27n+64Y)+2`. From (3)--(4),
`ell<Y`, `3/2<alpha<2`, and (11),

```
epsilon<2B(Y,n)/(3m)+1/393216.
```

Using (12) gives

```
m<(39059456/122731)B(Y,n),
(3/2)(5/2384-1/393216)=122731/39059456.              (14)
```

For `2^d0<=m<2^(d0+1)`, substitute
`Y<342d0+515`, `n<2d0+3`. The resulting quadratic
has positive coefficients. At `d0=48` its value is
`4310155828077002752/613655<2^48`, and its ratio
at successive indices is at most
`((d0+1)/d0)^2<2` for `d0>=48`. Induction therefore
forces `m<2^48`.

The universal exact logarithm-gap calculation in
the clustered node now gives `eta>2^-64`, so the
product gives `Y<112`, `n<=97`. Our arithmetic
checker reruns that source/receipt-pinned calculation
unchanged; its gap is independent of Barina and
of the earlier word class. Substitution in (14)
gives

```
m<256910993915904/613655,
m<=418657053<2^29.                                 (15)
```

This proves the EXT-1-only assertion. Only now, for
the all-length corollary, use the declared Barina-
dependent lower bound `m>=72057431991`, contradicting
(15). All clocks are full raw odd periods.

## Certificates

Run from the repository root:

```
python3 areas/cycles/results/two-singleton-high-arcs-exclusion/check_two_rotations.py
python3 areas/cycles/results/two-singleton-high-arcs-exclusion/check_singleton_highs.py
```

Both also run unchanged with `python3 -O`.
The geometry receipt contains 57 exact strata,
11448 full-cell vertex sign checks, and 16467 direct
profile controls for each placement. It records exact cell coverage,
branch validation, nonnegative rational combinations,
and the sharp relaxed control. The arithmetic and
cycle receipt verifies (14)--(15), the unchanged
local-descent/logarithm-gap replay, and genuine
`3x+q` cycles retaining their actual addends,
including the eleven standard `3x+5,7,13,61` fixtures.
The main receipt replays 7680 faithful word geometries
and 7648 genuine reduced cycles, including 73824
agreement subintervals. Finite profile and word controls
are not an absence proof.

## Remarks

Unequal weights can satisfy every h-only profile
witness, so the second rotation is a substantive
part of the argument. The domination in (7) applies
to both placements, while their linked second-rotation
cut systems differ and are certified separately.
Longer high arcs change the profile and the cut lists
and are not settled by this node. Novelty is undetermined; same-session
audits do not upgrade `written` status.

## History

- 2026-11-08: recorded the exact two-rotation
  obstruction and its separately scoped EXT-1-only
  and Barina-dependent cycle consequences.
