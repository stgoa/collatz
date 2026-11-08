---
id: three-label-four-mismatch-exclusion
kind: result
title: Three valuation labels cannot realize a coprime four-mismatch cycle
status: written
claim: >
  Raw odd-only 3x+1 clock. Let w be a positive valuation word
  of length m with exactly three distinct labels, and suppose
  0<h<m, gcd(h,m)=1, and s_w(h)=4. Under EXT-1, D_w>0
  and den(w)=1 force m<=3501056435; consequently
  m>=2^32 and D_w>0 imply den(w)>1. With the additional declared
  Barina convergence input, D_w>0 implies den(w)>1 at
  every length in this class. The maximum label may occupy one
  or two track arcs, without any restriction on h/m. The proof reduces the two-arc maximum
  profile to a height bound, the previously treated strong
  cluster regime, and two residual geometric configurations.
  All three-label coprime four-mismatch words are covered;
  four labels and noncoprime three-label tracks remain outside
  the claim. Neither conclusion uses LMN or Chim.
authors:
  - Codex four-arc research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex root research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex formal research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex residue research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [general-three-label-four-arc-exclusion, contiguous-maximum-four-arc-exclusion, clustered-two-maximum-arcs-exclusion, four-mismatch-inverse-continued-fraction-bound, denjoy-koksma-height-bound, paired-state-run-law, cycle-length-lower-bound-from-convergents]
assumes: [musson-collatz-gap-all, barina-2025-convergence-2-71]
certificates: [check_arc_classification.py, check_residual_geometry.py, check_three_labels.py]
evidence:
  - "check_arc_classification.json: single-arc oscillation reduction and exact concentration controls"
  - "check_residual_geometry.json: exact residual-case margins and faithful profile controls"
  - "check_three_labels.json: structural word classification, addend-aware cycles, pinned arithmetic replay and full-period comparisons"
tags: [cycles, four-arcs, rotation-distance, three-labels, height-profile, effective-exclusion]
---

# Three valuation labels cannot realize a coprime four-mismatch cycle

## Statement

Use the raw odd-only clock. Let `w` be a positive
valuation word of length `m` using exactly three
labels. Suppose `0<h<m`, `gcd(h,m)=1`, and

```
s_w(h)=#{i:w_i!=w_(i+h)}=4.
```

Under [EXT-1](../../../../sources/musson-collatz-gap-all.md),

```
D_w>0 and den(w)=1 imply m<=3501056435<2^32.          (1)
```

In particular `m>=2^32` and `D_w>0` imply `den(w)>1`.
With the additional declared
[Barina convergence input](../../../../sources/barina-2025-convergence-2-71.md),
`D_w>0` implies `den(w)>1` at every length in this
class. The all-length corollary uses the
[replayed full odd-period lower bound](../cycle-length-lower-bound-from-convergents/README.md)
`72057431991`. The external convergence computation
is not rerun. Neither conclusion uses LMN or Chim.

The new geometric argument treats two track arcs
carrying the maximum label, for every coprime shift
without a clustering hypothesis. For a maximum on
one arc, the proof extracts the stronger EXT-1-only
period bounds from existing calculations, separating
the arithmetic gap from their final Barina comparison.
The earlier nodes and their stated claims remain
unchanged. Four distinct labels and noncoprime
three-label tracks are not covered.

## Proof

### 1. Four track runs give two structural branches

Because `h` is coprime to `m`, the cyclic `h`-track
visits every index. Its four mismatches are exactly
four positive constant runs. With three labels,
precisely one label occurs twice; the two copies
cannot be adjacent. Each of the other labels has
one proper interval as its indicator, so the word
has no nonidentity rotational period. In particular
it is primitive.

If the maximum appears in one run, rotation and
renaming put the track word in the form
`V^d,A^a,B^b,A^c`, with pairwise distinct labels and
`V>max(A,B)`. We extract the needed period bound
from the existing contiguous-maximum proof in section 7.
The new geometric work treats

```
V^a,A^b,V^c,B^d,    a,b,c,d>=1,    V>max(A,B).        (3)
```

Assume `D_w>0` and `den(w)=1`. The rotated intercept
identity gives a primitive nontrivial positive odd
integer cycle with exact word `w`. Write

```
r=a+c, alpha=log_2(3), L=min_i n_i,
ell=log_2(L), Y=log_2(L+1), E=sum(w),
delta=E-alpha*m, eta=(2^E-3^m)/2^E.
```

Reverse the track if necessary, so
`u=h/m=min(h,m-h)/m<1/2`, then put `k=h^(-1) mod m`.
The strict upper bound follows from coprimality and
`m>=4`. Interchange the two maximum arcs if needed
so `a>=c`. All continued fractions below use this
chosen inverse `k`, not the unreversed clock.

### 2. Common arithmetic transfer, without clustering

The nongeometric estimates in the
[clustered-two-arcs theorem](../clustered-two-maximum-arcs-exclusion/README.md),
sections 1, 2 and 5, do not require `ru<1`.
We record their hypotheses and constants to make
that separation explicit.

Local descent below `2^17` gives `L>=2^17`, hence
also `L>=129`. The product bound gives
`E<8m/5` and `0<delta/m<2^-18`. Thus the lower
labels must be `{A,B}={1,t}` with `t>=2`.
The integral maximal ones run beginning at `L`
gives `t-1<(3/5)Y`.
Replace every `V` by `A`; the resulting template
has one interval of each lower label. Its proper
factor discrepancy is at most

```
Delta=2(t-1)(K-1)<(6/5)Y(27n+64Y),
K=sum digits(k/m)<27n+64Y, n<=2log_2(m)+1.           (4)
```

This uses the [inverse-complexity bound](../four-mismatch-inverse-continued-fraction-bound/README.md)
and [discrete Denjoy--Koksma estimate](../denjoy-koksma-height-bound/README.md).
EXT-1 and the cycle product also give

```
eta>=2^-172*m^-341, eta<m/(3L),
Y<173+342log_2(m).                                  (5)
```

Put `W=V-A>0`. Let `X` be the maximum positions,
with chronological coordinates `e=(i+1)/m`, and
use the periodic pre-drop profile

```
F(e)=r*e-#{z in X:z<e},     g=(F-inf F)/r.
```

The exact cyclic-factor identity from the clustered
node yields

```
log_2 n_i<=ell+rW*g(e_i)+Delta+delta.
```

The paired-state witness for every circular mismatch
gap `G` ending at `e` then implies

```
G < c0*max(g(e),g(e+u))+epsilon,
c0=rW/(alpha*m)<3/8,
epsilon=(ell+Delta+delta+alpha)/(alpha*m).           (6)
```

The agreeing run has length `mG-1`; the full one-step
loss is retained in epsilon. In particular, every
geometric bound proved with coefficient `R=3/8`
is valid here.

There is a stronger coefficient useful for height
bounds. If `beta` is the template mean, then
`E=m beta+rW` and `beta>=1`. The weaker local estimate
`delta/m<1/258`, together with `3^80<2^127`, gives

```
c0<1-(257/258)(80/127)=6103/16383.                  (7)
```

Consequently, if `osc(F)/r<=2/3`, at least one of
the four gaps has length at least `1/4`, and (6)
forces

```
epsilon>1/4-(2/3)(6103/16383)
        =325/196596>1/3952.                         (8)
```

For `m>=2^22`, the variation
`V_h=2(V-A)+2(V-B)<4V`, the rise estimate, and (5)
force `V>m/64`. The mean then permits at most 38
maximum letters: `r<=38`. These are precisely the
multiplicity estimates in the clustered theorem;
no spacing condition was used in their proof.

We will show that every remaining profile also
forces `epsilon>1/3952`. This is the only new input
needed for its arithmetic closure.

### 3. Single-arc oscillation reduces the possible geometries

For a single orbit segment of `j` maximum points,
write `F_j(x)=j*x-count(points before x)` up to a
constant. If `ju<=1`, direct ordering gives

```
osc(F_j)=j[1-(j-1)u].                               (9)
```

If `ju>=1` and `j>=2`, then

```
osc(F_j)<=ceil(j/2).                               (10)
```

Here is a uniform proof of (10), strengthening the
oscillation argument already used in the contiguous
node. Between consecutive collisions of two points,
the pre/post jump values are affine functions of
`u`; their range is convex. At a collision, intermediate
limiting jump values lie between the merged pre/post
values, so the range is continuous. It therefore
suffices to bound cell endpoints, including `1/j`
and `1/2`. They are rational `u=p/q` with `2<=q<=j`.
Write `j=Nq+s`, `0<=s<q`. The multiset is `N` full
uniform q-grids and `s` extra points. Oscillation
subadditivity gives `osc<=N+s`. Since
`s<=q-1<=N(q-2)+1`, this integer is at most
`floor((j+1)/2)=ceil(j/2)`. Convexity extends the
bound to every cell. The same argument also gives
`osc(F_j)/j<=2/3` throughout the spread range, as
proved in the contiguous node.

The full profile is the sum of the two translated
single-arc profiles, so its oscillation is at most
the sum of their oscillations. The strong cluster
case `ru<1` is already excluded at error at most
`1/(104r)` by the clustered theorem. Assume `ru>=1`.

If both arcs are clustered (`au<=1`, `cu<=1`), (9)
gives

```
osc(F)<=r-(a^2+c^2-r)u
       <=r+1-(a^2+c^2)/r<=r/2+1.
```

Thus (8) applies for `r>=6`. For `r=3,4,5`, direct
substitution leaves only the first, second and
fourth rows of the table below. For `r=2`, `ru>=1`
is impossible because `u<1/2`.

If both arcs are spread, their individual normalized
oscillations are at most `2/3`, so (8) again applies.
In the mixed regime `au>=1`, `cu<=1`, (9)--(10) give

```
osc(F)<=ceil(a/2)+c-c(c-1)/a.                        (11)
```

For even `a`, comparison with `2(a+c)/3` reduces to
`(a-c)^2+5c^2-6c>=0`. This holds for `c>=2`; for
`c=1` it is `a(a-2)>=0`.
For odd `a`, put `z=a-c`. The corresponding
polynomial is `5c^2-9c+z^2-3z`. If `c>=3`, use
`z^2-3z>=-2` for integer `z>=0`. If `c=2`, then
`z` is odd and at least one, and the polynomial is
`(z-1)(z-2)>=0`. If `c=1`, it is `(z-4)(z+1)`;
only `a=3` fails. The case `a=1` cannot be spread
for `u<1/2`. For `a=3`, direct ordering gives
`osc(F_3)=6u-1` on `[1/3,1/2]`. Adding the singleton
therefore suffices through `u=4/9`.

The only possible failures of the height criterion
outside strong clustering are consequently

| Maximum arc lengths `(a,c)` | Remaining interval |
|---|---|
| `(2,1)` | `1/3<=u<1/2` |
| `(2,2)` | `1/4<=u<1/3` |
| `(3,1)` | `4/9<u<1/2` |
| `(3,2)` | `1/5<=u<5/24` |

Threshold endpoints omitted from this table already
satisfy the height bound. This is an analytic
classification, not an inference from a finite grid.

### 4. Concentration handles `(2,1)` and `(3,2)`

For a profile with `r` jumps, its oscillation is the
largest downward loss across a consecutive circular
block of `k` maximum points. If their first-to-last
span is `s`, this loss is `k-rs`, measured from
before the first jump to after the last. This follows
by taking a global pre-drop maximum and the following
post-drop minimum in one period; conversely every
such downward loss is bounded by the range.

For `(2,1)`, the points are `{0,u,v}`. Losses using
at most two points are at most two. A circular span
containing all three must contain `0,u`, whose
minimum circular separation is `u` because `u<1/2`.
Thus the three-point loss is at most `3-3u<=2`.
Hence `osc(F)/3<=2/3`, so (8) applies.

For `(3,2)`, the points are
`{0,u,2u,v,v+u mod1}`, with `1/5<=u<5/24`.
Losses using at most three points are at most three.
Four points include two from the same original arc.
Every pair within either original arc has minimum
circular separation at least `u`, since `u<1/3`.
Thus any four-point loss is at most `4-5u<=3`.
A span containing all five must contain `0,u,2u`.
Those three points have largest complementary gap
`1-2u`, hence any such span is at least `2u`, and
its loss is at most `5-10u<=3`. Therefore
`osc(F)/5<=3/5<2/3`, and again (8) applies.

### 5. The `(2,2)` residual

Swap the equal arcs and rotate so `0<v<=1/2`.
The maximum positions are `{0,u,v,v+u}`, with no
wrap, and `1/4<=u<1/3`. Write `R=3/8` and
`F=4x-count`; paired heights are `R/4` times shifted
profile maxima. The four boundaries are
`u,1-u,v-u mod1,v+u` and are distinct.

If `v<u`, their order is `u,v+u,1-u,1+v-u`.
The gap ending at `u` is `2u-v>u>=1/4`.
The post-drop minimum is
`z=min(4u-3,4v+4u-4)`. The partner at `2u` has
lower profile than at `u`, giving

```
J(u)=(3/32)max(1,2-4v)<=3/16.
```

Thus `epsilon>1/16`.
If `v>u`, then `v<2u` except the excluded boundary
collision `u=1/4,v=1/2`. The post-minimum is
`4v-3`, and `J(v-u)=3/32`. The preceding gap is
`v` if `v<1-2u`, or `1-2u` if `v>1-2u`.
Both are at least `1/4`, giving `epsilon>=5/32`.
The equality `v=1-2u` merges boundaries and cannot
occur. This proves a uniform margin greater than
`1/16>1/3952`.

### 6. The `(3,1)` residual

Let `4/9<u<1/2`, with maximum positions
`{0,u,2u,v}`. Put `R=3/8`, `F=4x-count`, and name
the four boundaries

```
P=1-u, Q=2u, S=v-u mod1, T=v.
```

Overlaps `v=u,2u` and boundary coincidences
`v=3u-1,1-u` are excluded. Paired heights below
are `R/4` times the indicated shifted profile value.
Four ranges for `v` exhaust the faithful family.

**`0<v<u`.** The post-minimum is
`z=min(4v-2,4u-3)`. The partner of `P` is zero,
whose pre-drop value is higher than at `P`, while
`T` has higher value than its partner. Hence

```
J(P)=-R*z/4,    J(T)=R*(4v-1-z)/4.
```

If `v<3u-1`, the gaps ending at `P,T` sum to
`2-3u>1/2`. Their paired heights sum to at most
`9/32`: when `z=4v-2` the sum is
`R*(3-4v)/4<=3R/4`; when `z=4u-3`, use
`4v+5-8u<4u+1<3`. Therefore `epsilon>7/64`.
If `v>3u-1`, the gap ending at `T` is `u`, the
minimum is `4u-3`, and
`J(T)=R*(2+4(v-u))/4<3/16`, giving a stronger bound.

**`u<v<1-u`.** The gap ending at `Q` is
`3u-1>1/3`. Here `z=min(-1,4v-3)`, and the
paired maximum is at `Q`:

```
J(Q)=R*(8u-3-z)/4.
```

For `v<1/2` this is `R*(2u-v)<Ru<3/16`;
for `v>=1/2` it is `R*(2u-1/2)<3/16`.
Thus `epsilon>7/48`.

**`1-u<v<2u`.** The post-minimum is `-1`.
The gaps ending at `P,S` sum to `2-3u>1/2`, and

```
J(P)=R*(3-4u)/4,    J(S)=R*(4v-1)/4.
```

Their sum is `R*(2+4(v-u))/4<R=3/8`, since
`v<2u` and `u<1/2`. Hence `epsilon>1/16`.

**`2u<v<1`.** The post-minimum is `-1` and the
boundary order is `S<P<Q<T`. The gap ending at
`Q` is `3u-1>1/3`, while
`J(Q)=R*(8u-1)/4<9/32`. Hence `epsilon>5/96`.

The uniform residual margin is therefore
`epsilon>5/96>1/3952`.

### 7. Arithmetic closure and the full three-label claim

Every geometry has now been covered. For `m>=2^22`,
we have `r<=38`; strong clustering gives
`epsilon>1/(104r)>=1/3952`, while sections 3--6
give still larger margins in every other case.
Put

```
B(Y,n)=Y+(6/5)Y(27n+64Y)+2.
```

The same error bound as in the clustered theorem
then gives, without any restriction on `u`,

```
epsilon<2B(Y,n)/(3m)+1/393216,
m<(64749568/24329)B(Y,n).                            (12)
```

We reuse its exact arithmetic closure: the positive
quadratic obtained from (5) on dyadic bands first
gives `m<2^48`. The universal rational logarithm-gap
lemma then gives `eta>2^-64`, hence `Y<112` and
`n<=97`. Finally

```
m<425886010048512/121645,
m<=3501056435<2^32.                                (13)
```

The omitted lengths `m<2^22` already satisfy (13).
All these steps use EXT-1 and local exact computation
only. Our transfer certificate reruns the prior
arithmetic checker with pinned source and receipt
hashes. The universal logarithm-gap step is separated
from that checker's Barina-dependent comparison.
Only for the all-length corollary do we import
`m>=72057431991`, contradicting (13).

For the one-maximum-arc branch, assume first
`m>=2^22`. If that arc has multiplicity at least two,
section 6 of the [contiguous-maximum proof](../contiguous-maximum-four-arc-exclusion/README.md)
gives, using only EXT-1 and local descent,

```
m<(4980736/6125)B(Y,n).
```

Its preliminary bound `m<2^48` and the same universal
exact gap imply

```
m<32760462311424/30625<2^30<3501056435.
```

If the maximum is a singleton, the specific
`V>max(A,B)` branch of the
[singleton proof](../general-three-label-four-arc-exclusion/README.md),
sections 2--4, gives at every `m>=2^22`

```
m<(1536/5)Y(27n+64Y).
```

Again its preliminary bound and the universal gap
are independent of Barina, so

```
m<1683677184/5<2^29<3501056435.
```

The old all-length arguments invoked Barina to
supply `m>=2^22`. Here we condition on that threshold
ourselves; smaller periods already satisfy (1).
This is an explicit extraction of those calculations,
not a silent rewrite of the merged nodes or a use
of their other label-order branches. It proves (1)
for the single-maximum-arc case as well.

Finally the declared Barina period lower bound
contradicts (1), completing the all-length corollary.
Every period here is the full raw odd-only period;
no half-period or shortcut clock is substituted.

## Certificates

Run from the repository root:

```
python3 areas/cycles/results/three-label-four-mismatch-exclusion/check_arc_classification.py
python3 areas/cycles/results/three-label-four-mismatch-exclusion/check_residual_geometry.py
python3 areas/cycles/results/three-label-four-mismatch-exclusion/check_three_labels.py
```

Each checker also runs unchanged under `python3 -O`.
The generated receipts record exact profile reduction
and concentration checks, the two residual geometric
cases, the structural classification, addend-aware
actual cycles, the eleven standard cycle fixtures,
and the pinned arithmetic replay. Finite profile
grids test formulas and endpoint conventions; the
analytic classification above, not an absence census,
proves the universal statement.

## Remarks

This completes the three-label coprime four-mismatch
case by removing the clustering restriction from the
two-maximum-arc branch. It does not settle the general
rotation-distance-at-least-five question: four-label
coprime words and noncoprime three-label tracks remain.
The exact profile reduction, concentration bounds,
and residual witness arguments are the new steps;
the discrepancy, minimum, and logarithm-gap tools
are inherited. Novelty is undetermined. Same-session
audits do not upgrade the node beyond `written`.

## History

- 2026-11-08: recorded the all-profile classification
  for two maximum arcs and the resulting three-label
  coprime four-mismatch exclusion, retaining separate
  EXT-1-only and Barina-dependent conclusions.
