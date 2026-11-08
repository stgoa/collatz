---
id: clustered-two-maximum-arcs-exclusion
kind: result
title: Clustered maximum arcs exclude three-label four-arc words
status: written
claim: >
  Raw odd-only 3x+1 clock. Let a,b,c,d>=1, m=a+b+c+d,
  0<h<m, gcd(h,m)=1, and let V,A,B be pairwise distinct positive
  valuation labels with V>max(A,B). Suppose the word read
  along a cyclic h-track is V^a,A^b,V^c,B^d. Put r=a+c
  and u=min(h,m-h)/m. If r*u<1, then under EXT-1,
  D_w>0 and den(w)=1 force m<=3501056435; in particular
  m>=2^32 and D_w>0 imply den(w)>1. When a=c=1, all coprime
  shifts qualify and the sharper bound is m<=394381472,
  so m>=2^29 and D_w>0 imply den(w)>1. With the additional declared
  Barina convergence input, D_w>0 implies den(w)>1 at
  every length in the stated clustered family. Three
  ordering cases force profile error greater than 1/(104r).
  For two isolated maxima the margin 1/208 is sharp
  in a closed rational relaxation,
  not asserted to occur in an admissible integer cycle.
  Both lower-label arrangements and arbitrary amplitudes
  are covered. Neither conclusion uses LMN or Chim.
authors:
  - Codex four-arc research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex root research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex formal research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex residue research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [contiguous-maximum-four-arc-exclusion, general-three-label-four-arc-exclusion, four-mismatch-inverse-continued-fraction-bound, denjoy-koksma-height-bound, paired-state-run-law, cycle-length-lower-bound-from-convergents]
assumes: [musson-collatz-gap-all, barina-2025-convergence-2-71]
certificates: [check_cluster_geometry.py, check_clustered_arcs.py]
evidence:
  - "check_cluster_geometry.json: exact three-order inequalities, faithful profile geometry and sharp singleton relaxation"
  - "check_clustered_arcs.json: profile identities, addend-aware cycle controls, pinned logarithm-gap replay and full-period comparisons"
tags: [cycles, four-arcs, rotation-distance, height-profile, discrepancy, effective-exclusion]
---

# Clustered maximum arcs exclude three-label four-arc words

## Statement

Use the raw odd-only clock. Let `a,b,c,d>=1`, `m=a+b+c+d`,
`0<h<m`, and `gcd(h,m)=1`. Suppose a positive valuation word,
read along a cyclic index track, is

```
V^a,A^b,V^c,B^d.                                    (1)
```

where the three labels are pairwise distinct and
`V>max(A,B)`. Put `r=a+c`, `u=min(h,m-h)/m`, and
assume the strong clustering condition `r*u<1`. Under
[EXT-1](../../../../sources/musson-collatz-gap-all.md),

```
D_w>0 and den(w)=1 imply m<=3501056435.               (2)
```

Thus `m>=2^32` and `D_w>0` imply `den(w)>1`. If `a=c=1`, every
coprime shift satisfies the clustering condition and
the sharper conclusion is `m<=394381472`, hence the
cutoff `m>=2^29` under `D_w>0`. With the additional
declared [Barina convergence input](../../../../sources/barina-2025-convergence-2-71.md),
the exclusion holds at every length. Only this final
corollary uses the imported convergence computation,
through the [replayed raw odd-period lower bound](../cycle-length-lower-bound-from-convergents/README.md)
`72057431991`. The general EXT-1-only bound uses local
descent below `2^17`; the isolated-maxima bound needs
only the 63 odd seeds from 3 through 127. No LMN or
Chim estimate is used.

The indicator of label `A` is one nonempty proper
interval on the coprime track. Its unique entry boundary
precludes a nonidentity rotational period, so (1) is
primitive. This also covers the case of antipodal
maximum positions: `A!=B` prevents a half-turn period
of the full word. Two maximum arcs with `r*u>=1` and
noncoprime tracks are outside the general claim.

## Proof

Assume `D_w>0` and `den(w)=1`. The rotated intercept
identity propagates divisibility by the odd number
`D_w`, yielding a primitive nontrivial positive odd
integer cycle with exactly these valuations. Write

```
alpha=log_2(3), L=min_i n_i, ell=log_2(L),
Y=log_2(L+1), E=sum(w), delta=E-alpha*m,
eta=(2^E-3^m)/2^E.
```

### 1. The common discrepancy and minimum bounds

Local descent through 127 gives `L>=129`. The product
identity, `388^5<2^8*129^5`, and `ln(2)>2/3` imply

```
E<8m/5,             0<delta<m/258.                   (3)
```

If `A,B>=2`, the mean contradicts (3). Therefore
`{A,B}={1,t}` with `t>=2`. The minimum starts a
positive maximal ones run of length `l`, followed by
a valuation `e>=t`. Terminal oddness gives
`L+1=2^(l+1)z` for a positive odd integer `z`.
The state after this block is at least `L`, whence

```
l+1<=Y,    l+e<=kappa(l+1),
kappa=alpha+1/[3L ln(2)]<8/5,
t-1<(3/5)Y.                                         (4)
```

These are the minimum-run estimates from the
[contiguous-maximum argument](../contiguous-maximum-four-arc-exclusion/README.md),
section 1; they do not depend on the maximum positions.
The bound on `kappa` follows from `3^32<2^51`,
`ln(2)>1/2`, and `2/387<1/160`.

Reverse the track if necessary so `u=h/m<=1/2`,
and then define the inverse `k=h^(-1) mod m`, the
chronological step along the track. No continued-fraction
symmetry is assumed when reversing: all subsequent
digits belong to this chosen `k/m=[0;a1,...,an]`.
Write `K=sum ai`.

Replace every maximum letter by `A`, obtaining a
binary template `U` with one cyclic interval of each
label `1,t`. Put `W=V-A>0` and let `beta` be the
template mean, so `E=m beta+rW`. The discrete
[Denjoy--Koksma estimate](../denjoy-koksma-height-bound/README.md)
and the [logarithmic inverse-complexity theorem](../four-mismatch-inverse-continued-fraction-bound/README.md)
give, for every proper chronological factor,

```
|sum(U_factor)-beta*length|<=Delta=2(t-1)(K-1),
K<27n+64Y,       n<=2log_2(m)+1,
Delta<(6/5)Y(27n+64Y).                               (5)
```

The four mismatch boundaries of (1) are distinct.
Finally EXT-1 and the product give

```
eta>=2^-172*m^-341,       eta<m/(3L),
ell<172+342log_2(m),      Y<173+342log_2(m).           (6)
```

### 2. The maximum positions control the height

Use chronological coordinates `e=(i+1)/m` and evaluate
profiles before their downward jumps. If `X` is the
set of maximum positions, define the periodic profile

```
F(e)=r*e-#{z in X:z<e},    f_min=inf F,
g(e)=(F(e)-f_min)/r,       R=3/8.                    (7)
```

The exact profile identity from the
[contiguous-maximum result](../contiguous-maximum-four-arc-exclusion/README.md),
section 3, applies to any set of maximum positions.
For a forward factor of length `l<m` with `N` maximum
letters, `F(end)-F(start)=rl/m-N`, including wrapped
factors and pre-jump endpoints. If
`epsilon_i=log_2(1+1/(3n_i))`, then their sum is `delta`,
and exactly

```
log_2(n_end/n_start)
 =W(F(end)-F(start))-dev_U
   +sum_factor epsilon_i-delta*l/m.                 (8)
```

The last two terms have absolute value at most `delta`.
Starting at a global minimum gives

```
log_2 n_i<=ell+rW*g(e_i)+Delta+delta.                (9)
```

Since `beta>=1`, (3) implies
`rW/m<alpha-1+1/258`. The comparison
`alpha<51/32` and `257/258-255/256=1/33024>0`
therefore gives

```
rW/(alpha*m)<3/8.                                  (10)
```

For a circular mismatch gap `G` ending at `e`, the
agreeing run has length `mG-1`. The
[paired-state run law](../paired-state-run-law.md)
makes its larger endpoint exceed `2*3^(mG-1)`.
Combining this with (9)--(10), and retaining a full
one-step loss, yields

```
G<J(e)+epsilon,    J(e)=R*max(g(e),g(e+u mod 1)),
epsilon=(ell+Delta+delta+alpha)/(alpha*m).           (11)
```

### 3. Three order cases for two strongly clustered arcs

This geometric step uses only `a,c>=1`, `r=a+c`,
`0<u<1/r`, and four distinct boundary points. The
maximum positions are two disjoint finite `u`-orbit
segments of lengths `a,c`. The following argument
shows that even the weak version of (11) forces

```
epsilon>1/(104r).                                  (12)
```

A global minimum of the profile is immediately after
a maximum. It cannot be internal to either orbit
segment: the next point of that segment is distance
`u` ahead, so the change between the two post-drop
values is at most `u-1/r<0`. Rotate to put such an
arc end at 1 and rename the two arc lengths if needed.
The first arc then has points
`1-(a-1)u,...,1-u,1`. The other arc cannot wrap across
this origin: its first point after the minimum would
be less than `u` away and would make the profile
negative after its drop. Thus its points are
`v-(c-1)u,...,v-u,v` for some `0<v<1`.

The post-drop value at 1 is zero, and every first
maximum after it is at least `1/r` away. Therefore

```
R_A=1-a*u>0,       R_B=v-c*u>0,
E_h={R_A,R_B,v,1},        R_B<v,
J(1)=R/r=3/(8r).                                   (13)
```

The paired value at 1 uses `g(1)=1/r` before its drop;
its partner at `u` has value at most `u<1/r`.
The four boundaries are distinct because both
intervening lower-label arcs in (1) have positive
length. In particular no boundary-collision limit
is substituted into the next three cases.

**First order: `R_B<v<R_A<1`.** Before either first
maximum there is no intervening maximum between
its predecessor boundary and its partner. Hence

```
J(R_B)=R[v-(c-1)u],
J(R_A)=R[a/r-(a-1)u].
```

The first, third, and last gap inequalities give

```
v <= (c+3/5)u+(8/5)epsilon,
1 <= v+(5a/8+3/8)u+3a/(8r)+epsilon,
a*u <= 3/(8r)+epsilon.
```

Combining them gives

```
L0 <= r[(129a)/40+c+39/40]epsilon,
L0=5a^2/8+a*c-15a/64-3c/8-117/320.
```

If `epsilon<=1/(104r)`, the difference is positive:

```
L0-[(129a)/40+c+39/40]/104
 =3/5+(129/65)(a-1)+(8/13)(c-1)
   +(5/8)(a-1)^2+(a-1)(c-1)>0.
```

**Second order: `R_B<R_A<v<1`.** The same first
paired value and the last gap give

```
v <= (c+3/5)u+(8/5)epsilon,
v >= 1-3/(8r)-epsilon.
```

Using `u<1/r` yields
`a-39/40<(13/5)r*epsilon`. Since `a>=1`, this proves
(12).

**Third order: `R_A<R_B<v<1`.** There are no maxima
before the first point of the first arc, so
`J(R_A)=R[1-(a-1)u]`. Its first gap gives
`5/8<=(5a/8+3/8)u+epsilon`. Thus

```
epsilon>(5c-3)/(8r)>=1/(4r)>1/(104r).
```

These are all possible strict orders, proving (12).
The essential hypothesis `ru<1` ensures minimum
alignment at an arc end. No claim is made here for
intermediate overlap or spread configurations.

### 4. The isolated-maxima refinement and sharp relaxation

When `a=c=1`, coprimality and `m>=4` give `u<1/2`,
so (12) already covers every track shift. A separate
closed-relaxation argument identifies the sharp
constant. Choose which maximum is zero so the other
is `v>=1/2`. Then the normalized pre-drop profile is

```
g(0)=1/2,
g(e)=e                     for 0<e<=v,
g(e)=e-1/2                 for v<e<1,
E_h={0,v-u,1-u,v}.
```

With `f=Rg`, the essential paired values are
`J(0)=R/2` and `J(v-u)=Rv`.
If `v+u<=1`, the first and last witnesses imply
`u<=R/2+epsilon` and `(1-R)v<=u+epsilon`. Hence
`epsilon>=(1-2R)/4=1/16`.
If `v+u>=1`, they instead imply
`v>=1-R/2-epsilon` and
`(1-R)v<=u+epsilon<=1/2+epsilon`. Therefore

```
epsilon >= (1-3R+R^2)/(2(2-R)) = 1/208.             (14)
```

At `v+u=1` these weak inequalities remain valid with
the pre-drop value at zero. This closed relaxation
may include an ordering-boundary coincidence; the
actual integer family has four distinct boundaries.

The rational values `u=1/2`, `v=21/26` give endpoints
`(0,4/13,1/2,21/26)`, gaps
`(5/26,4/13,5/26,4/13)`, and paired heights
`(3/16,63/208,3/16,63/208)`. Every gap minus its
height is `1/208`. This is a sharp geometric
relaxation control, not an admissible coprime word
or an integer cycle.

### 5. Exact period closure with separated external inputs

Define

```
B(Y,n)=Y+(6/5)Y(27n+64Y)+2.
```

First consider the general clustered family. For
`m>=2^22`, the maximum-letter forcing calculation in
[the contiguous-maximum proof](../contiguous-maximum-four-arc-exclusion/README.md),
section 2, applies unchanged: the present variation
is `V_h=2(V-A)+2(V-B)<4V`. If `V<=m/64`, the rise
and end witness would give

```
(49/2064)m<11ell+11<11(172+342log_2(m))+11,
```

which is impossible by the exact dyadic comparison
starting at `2^22`. Hence `V>m/64`. If there were
at least 39 maximum letters, their excess valuation
would exceed `39(m/64-1)>3m/5`, contradicting (3).
Thus `r<=38` throughout this range, and (12) gives
`epsilon>1/3952`.

The local replay below `2^17` gives `L>=2^17` and
`delta/m<2^-18`; consequently (11) gives

```
epsilon<2B(Y,n)/(3m)+1/393216,
m<(64749568/24329) B(Y,n).                          (15)
```

Here `(3/2)(1/3952-1/393216)=24329/64749568`.
For `2^d<=m<2^(d+1)`, (6) gives
`Y<342d+515`, `n<2d+3`. The resulting quadratic
`P(d)=(64749568/24329)B(342d+515,2d+3)` has positive
coefficients, and

```
P(48)=7145023419698118656/121645<2^48,
P(d+1)/P(d)<=((d+1)/d)^2<2       for d>=48.
```

Induction over dyadic bands forces `m<2^48`.

Now use only the universal exact arithmetic lemma in
[the singleton theorem's bootstrap](../general-three-label-four-arc-exclusion/README.md),
section 4: every integer `0<m<2^48` with
`E-m alpha>0` has `eta>2^-64`. Our certificate reruns
its hash-pinned checker and verifies the receipt
unchanged. The lemma uses an 80-term rational
logarithm enclosure and a unimodular convergent
bracket; it does not use Barina or any restriction
on the valuation word. Hence `eta<m/(3L)` gives
`Y<112`, and `n<=97`. Substitution into (15) gives

```
B(112,97)=6577434/5,
m<425886010048512/121645<2^32,
m<=3501056435.                                     (16)
```

The lengths `m<2^22` omitted from the multiplicity
argument already satisfy this bound. This proves
(2) under EXT-1 alone.

For two isolated maxima, use (14) and only `L>=129`.
No multiplicity reduction or lower period threshold
is needed. The lighter local bound gives

```
epsilon<2B(Y,n)/(3m)+1/387,
m<(53664/179)B(Y,n),
(3/2)(1/208-1/387)=179/53664.
```

The analogous positive quadratic at `d=48` is
`5921746640760288/895<2^48`, with the same dyadic
induction. The same arithmetic gap then gives

```
m<352971418176/895<2^29,
m<=394381472.                                      (17)
```

Finally, and only for the all-length corollaries,
import the declared Barina-dependent lower bound
`m>=72057431991`, contradicting (16) or (17). All
periods are the full raw odd-only period, not a
half-period or a shortcut period. The external
convergence computation itself is not replayed.

## Certificates

Run from the repository root:

```
python3 areas/cycles/results/clustered-two-maximum-arcs-exclusion/check_cluster_geometry.py
python3 areas/cycles/results/clustered-two-maximum-arcs-exclusion/check_clustered_arcs.py
python3 -O areas/cycles/results/clustered-two-maximum-arcs-exclusion/check_cluster_geometry.py
python3 -O areas/cycles/results/clustered-two-maximum-arcs-exclusion/check_clustered_arcs.py
```

The generated [geometry receipt](check_cluster_geometry.json)
checks the exact three-order eliminations, faithful
finite profiles with distinct boundaries, minimum
alignment, and the sharp isolated-maxima relaxation.
The [arithmetic and cycle receipt](check_clustered_arcs.json)
checks addend-aware reduced cycles, the eleven standard
actual-cycle fixtures, local descent below `2^17`,
and the constants in (15)--(17). The logarithm-gap
checker is replayed with pinned source and receipt
hashes. Its Barina-dependent comparison is separated
from its universal arithmetic lemma.

Finite controls test transfer and boundary conventions.
The analytic order arguments prove the geometric
claims for all parameters; no absence census is used.

## Remarks

This extends the height-profile method to two
separated maximum arcs in the strongly clustered
regime. The minimum must occur at an arc end, which
reduces the four mismatch witnesses to three orders.
The weighted discrepancy, maximum-multiplicity bound,
and exact gap tools are inherited. The two-isolated-
maximum case covers every coprime shift and admits a
stronger period bound. Intermediate overlap regimes,
four distinct labels, and noncoprime tracks remain
outside this result. Novelty is undetermined.
Same-session audits do not upgrade `written` status.

## History

- 2026-11-08: recorded the strongly clustered
  two-maximum-arc obstruction, the sharper isolated-
  maximum corollary, and their separated EXT-1 and
  Barina input scopes.
