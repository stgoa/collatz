---
id: weighted-high-arc-concentration
kind: result
title: One of the two highest labels must occur at most five times
status: written
claim: >
  Raw odd-only 3x+1 clock. Let a positive valuation word w of
  length m have exactly four distinct labels, gcd(h,m)=1, and
  s_w(h)=4. Let c,d be the multiplicities of the two largest
  labels and u=min(h,m-h)/m. Under EXT-1, if c,d>=2 and
  3u(min(c,d)-1)>=1, then D_w>0 and den(w)=1 force
  m<=1069729381<2^30. The same finite bound holds whenever
  min(c,d)>=6, without the cone hypothesis. With the additional
  declared Barina convergence input, the cone contains no
  denominator-one word at any length, and every hypothetical
  cycle in the stated four-label class has min(c,d)<=5.
  All cyclic orders and arbitrary unequal high-label excesses
  are allowed. The auxiliary localization is more general:
  under EXT-1 every primitive nontrivial 3x+1 cycle with
  s_w(h)=4 and m>=2^23 has min(h,m-h)>m/15, without requiring
  h coprime to m. These are concentration restrictions, not
  an exclusion of all four-label or noncoprime words.
authors:
  - Codex residue research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex root research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex four-arc research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [contiguous-maximum-four-arc-exclusion, rise-lemma, paired-state-run-law, denjoy-koksma-height-bound, four-mismatch-inverse-continued-fraction-bound, cycle-length-lower-bound-from-convergents]
assumes: [musson-collatz-gap-all, barina-2025-convergence-2-71]
certificates: [check_concentration.py]
evidence:
  - "check_concentration.json: exact cone profiles and weighted identities, all-order word controls with actual addends, localization constants, pinned local descent and logarithm-gap replay"
tags: [cycles, four-arcs, rotation-distance, four-labels, concentration, height-profile]
---

# One of the two highest labels must occur at most five times

## Statement

Use the raw odd-only clock. Let `w` be a positive valuation
word with exactly four distinct labels and full length `m`.
Suppose `0<h<m`, `gcd(h,m)=1`, and `s_w(h)=4`.
The cyclic `h`-track therefore consists of four nonempty
constant arcs, one for each label. Write `c,d` for the
multiplicities of the two largest labels, and put

```
u=min(h,m-h)/m.
```

Under [EXT-1](../../../../sources/musson-collatz-gap-all.md),
either of the following hypotheses implies
`D_w>0 and den(w)=1 ==> m<=1069729381<2^30`:

```
c,d>=2 and 3u(min(c,d)-1)>=1;                       (1)
min(c,d)>=6.                                       (2)
```

The two high arcs may be adjacent or separated. Their
labels and excesses need not be equal. With the additional
declared [Barina convergence input](../../../../sources/barina-2025-convergence-2-71.md),
(1) excludes denominator one at every length, and every
hypothetical integer cycle in the four-label class satisfies

```
min(c,d)<=5.                                       (3)
```

Only this all-length conclusion uses the external
convergence computation and its
[replayed full odd-period bound](../cycle-length-lower-bound-from-convergents/README.md)
`72057431991`. Neither conclusion uses LMN or Chim.

We also prove the localization used to pass from (1) to (2).
For every primitive nontrivial positive integer `3x+1` cycle,
any rotation with exactly four mismatches satisfies, under
EXT-1,

```
m>=2^23 ==> min(h,m-h)>m/15.                         (4)
```

Statement (4) does not require a coprime shift or a bound
on the number of labels. The four-label concentration
claim does require coprimality. The remaining small
multiplicities are not excluded here.

## Proof

### 1. Integer cycles, labels and the low template

Assume `D_w>0` and `den(w)=1`. The rotation identity
`2^(w_i) C_next=3C_rot+D_w` propagates divisibility by the
odd number `D_w`, giving positive odd integer states with
the exact valuations `w`. A proper interval on a cyclic
coprime track has no nonidentity rotational period. Each
label indicator is such an interval, so `w` is primitive.

Let `L,H` be its minimum and maximum and write

```
alpha=log_2(3), ell=log_2(L), Y=log_2(L+1),
E=sum(w), delta=E-alpha*m, eta=(2^E-3^m)/2^E.
```

The locally replayed descent below `2^17` gives `L>=2^17`.
In particular `L>=129`. The product identity, `ln(2)>2/3`,
and `388^5<2^8*129^5` imply

```
E<8m/5,       0<delta<m/2^18<m/258.                 (5)
```

Thus the smallest label is 1. Name the other three
`1<t<U<V`. At `L`, the first valuation must be 1:
otherwise its successor `(3L+1)/2^e` would be below `L`.
Let the initial maximal ones run have length `l>=1`,
followed by a valuation `e>=t`. If `y` is the state before
that valuation, then `y=1 mod4` and
`y+1=3^l(L+1)/2^l`. Consequently `2^(l+1)` divides
`L+1`, so `l+1<=Y`. The state after the whole block is
at least `L`. Multiplying the step ratios gives
`l+e<=kappa(l+1)`, where

```
kappa=alpha+1/[3L ln(2)]<8/5.
```

Here `3^32<2^51` and `2/387<1/160` suffice for the last
inequality. Therefore

```
t-1<(3/5)Y.                                       (6)
```

Orient the track so `0<h<m/2` and define its chronological
inverse `k=h^(-1) mod m`. Write `k/m=[0;a1,...,an]`
canonically, and `K=sum a_i`. All fractions below use
this chosen orientation. Replace both high labels `U,V`
by `t`. The resulting template has one interval of ones
on the track and is `t` everywhere else, in every cyclic
order of the original four arcs. Its variation is exactly
`2(t-1)`. The discrete
[Denjoy--Koksma estimate](../denjoy-koksma-height-bound/README.md)
therefore bounds the deviation of every proper
chronological factor from its template mean `beta` by

```
Delta=2(t-1)(K-1).
```

The [inverse-complexity theorem](../four-mismatch-inverse-continued-fraction-bound/README.md)
and (6) give

```
K<27n+64Y,       n<=2log_2(m)+1,
Delta<(6/5)Y(27n+64Y).                              (7)
```

Finally, the cycle product and EXT-1 imply

```
eta<m/(3L),       eta>=2^-172*m^-341,
ell<172+342log_2(m),       Y<173+342log_2(m).          (8)
```

### 2. Unequal excesses retain a weighted height profile

Set `A=U-t>0`, `B=V-t>0`, and `W=cA+dB`. Use the
chronological coordinates `e_i=(i+1)/m` in `(0,1]`.
Let `X_U,X_V` be the positions of the high letters and
define periodic profiles, evaluated before their jumps,

```
F_U(e)=c*e-#{x in X_U:x<e},
F_V(e)=d*e-#{x in X_V:x<e},
F(e)=A F_U(e)+B F_V(e).
```

For a forward factor of length `r<m`, the profile
increment is `Wr/m-A N_U-B N_V`, where `N_U,N_V`
count the high letters in that factor. This includes
factors wrapping across the chronological cut. Since
`E=m beta+W`, subtracting the template mean gives the
exact identity

```
log_2(n_end/n_start)
 = F(e_end)-F(e_start)-dev_template
   +sum_factor log_2(1+1/(3n_i))-delta*r/m.          (9)
```

The last two terms together have absolute value at most
`delta`. Start at the global minimum and use one proper
factor, including the empty factor. Then

```
log_2 H <= ell+osc(F)+Delta+delta.                  (10)
```

No minimum is aligned with either high arc, and no
comparison of `A` and `B` is used. Since `beta>=1`, (5)
and `3^80<2^127` give

```
W/(alpha*m)<1-(257/258)(80/127)=6103/16383.          (11)
```

### 3. The cone bounds both normalized oscillations

For any translated orbit segment of `j>=2` positions
at step `u` with `0<u<=1/2`, write
`F_j(e)=j e-count(points before e)`. The
[single-arc profile argument](../contiguous-maximum-four-arc-exclusion/README.md),
section 4, gives

```
ju<=1:  osc(F_j)/j=1-(j-1)u;
ju>=1:  osc(F_j)/j<=2/3.                            (12)
```

For completeness, the first formula orders the cluster
without wrap. In the spread range, partition at the
rational point collisions. The pre/post jump values
are affine on each ordering cell, so their range is
convex there and continuous at collisions. At a cell
endpoint `u=p/q`, `2<=q<=j`, write `j=Nq+r`,
`0<=r<q`. There are `N` full uniform q-grids and `r`
remaining points. Their profile ranges add to at most
`N+r<=2j/3`, since `r<=q-1<=N(2q-3)`. This proves
the spread bound on every cell, not just rational samples.

It follows from (12) that

```
3u(j-1)>=1 ==> osc(F_j)<=2j/3.                     (13)
```

Under (1), both high arcs satisfy (13). Positivity of
the unequal weights and oscillation subadditivity give

```
osc(F)<=A osc(F_U)+B osc(F_V)<=2W/3.                (14)
```

Four mismatches leave an agreeing run of length at
least `m/4-1`. Distinct odd paired states and the
[run law](../paired-state-run-law.md) give
`H>2*3^(m/4-1)`. Combining this with (10)--(14), put

```
epsilon=(ell+Delta+delta+alpha)/(alpha*m).
```

The full one-step loss in the run length is included.
We obtain

```
epsilon>1/4-(2/3)(6103/16383)
       =325/196596>1/1216.                          (15)
```

### 4. Exact period closure for the cone

Define `B0(Y,n)=Y+(6/5)Y(27n+64Y)+2`. Equations
(5)--(8), `alpha>3/2`, and `alpha<2` give

```
epsilon<2B0(Y,n)/(3m)+1/393216,
m<(4980736/6125)B0(Y,n).                            (16)
```

These are the same constants as the spread branch of
the contiguous-maximum theorem. We state the arithmetic
separately from that node's final Barina comparison.
On a dyadic interval `2^j<=m<2^(j+1)`, (8) bounds
the right side by the positive quadratic

```
P(j)=(4980736/6125)B0(342j+515,2j+3).
P(48)=549617186130624512/30625<2^48.
```

For `j>=48`, `P(j+1)/P(j)<=((j+1)/j)^2<2`, so the
base comparison persists. Thus `m<2^48`.
The independently replayed 80-term rational logarithm
enclosure verifies the unimodular opposite bracket

```
83130157078217/52449289519716 < alpha
 <683381996816440/431166034846567,
q'>2^48,       q alpha-p>2^-62.
```

Writing any integer pair `(m,E)` in this unimodular
basis proves `E-m alpha>2^-62` whenever `0<m<2^48`
and that difference is positive: positivity forces the
upper-vector coefficient at least one, and `m<q'`
forces the lower-vector coefficient at most minus one.
Hence `eta>2^-64`, `L<m*2^64/3`, `Y<112`, and `n<=97`.
Substituting in (16) gives

```
m<32760462311424/30625,
m<=1069729381<2^30.                                (17)
```

This proves the cone bound using only EXT-1 and the
local exact checks. The declared Barina period input
is used only to compare (17) with `72057431991`,
excluding the cone at every length.

### 5. A four-mismatch rotation cannot be too short

This section applies to any primitive nontrivial `3x+1`
cycle with exactly four mismatches at `h`, even if the
shift is not coprime. Replace `h` by `min(h,m-h)`.
Every one-step log rise is below `kappa-1<3/5`, so
the forward partner-height difference is below `3h/5`.
The [rise lemma](../rise-lemma/README.md) from minimum
to maximum, with at most four mismatches, gives

```
height=log_2(H/L)
 <(29643/3125)(ell+1+3h/5),                         (18)
```

because `(8/5)^5-1=29643/3125`. The same agreeing-run
witness and the exact inequality `3^12>2^19` give,
with `m>=4` because there are four mismatches,

```
19m/48-7/12<ell+height.                            (19)
```

If `h<=m/15`, combining (18)--(19) yields

```
(61511/3750000)m
 <(32768/3125)ell+29643/3125+7/12.                  (20)
```

On a dyadic interval `2^j<=m<2^(j+1)`, EXT-1 gives
`ell<172+342(j+1)`. At `j=23`, the left lower bound
minus the resulting right upper bound is exactly

```
46609724897/937500>0.
```

At each later index the left doubles, whereas the
right increases by `(32768/3125)*342`, less than the
initial left bound. Thus (20) is impossible whenever
`m>=2^23`, proving (4).

Return to the four-label family. If `min(c,d)>=6` and
`m>=2^23`, (4) implies `3u(min(c,d)-1)>1`, so (17)
applies. Smaller periods already satisfy (17). This
proves the finite bound under (2). The Barina comparison
then gives (3). Throughout, `m` counts the full primitive
odd-only period; no half-period or shortcut clock is used.

## Certificates

Run from the repository root:

```
python3 areas/cycles/results/weighted-high-arc-concentration/check_concentration.py
python3 -O areas/cycles/results/weighted-high-arc-concentration/check_concentration.py
```

The deterministic standard-library checker verifies exact
cone and collision formulas, arbitrary positive weighted
profile identities, the localization constants and dyadic
induction, all cyclic arc orders in its stated finite range,
and actual reduced `3x+q` cycles with their addends retained.
It also replays the eleven shared controls and invokes the
existing local descent, rational-gap, and cutoff functions
after checking their source and receipt hashes. Its
generated receipt distinguishes those local computations
from the externally supplied Barina input. Use
`--write-receipt` to regenerate it. Finite profile grids
are controls for the analytic proof, not evidence of
general absence of cycles.

## Remarks

The new step is the weighted use of two different high
arc profiles. Replacing both by the smaller non-one
label leaves a low template with only two boundaries,
independently of whether the high arcs are adjacent.
The prior single-arc oscillation and discrepancy tools
then apply without equating their amplitudes. The
separate short-rotation calculation turns this geometric
cone into the multiplicity restriction (3).

The [two-singleton theorem](../two-singleton-high-arcs-exclusion/README.md)
already excludes `c=d=1` under its declared inputs.
The present result permits one or both high multiplicities
to be larger and does not settle the remaining pairs
with minimum at most five. Four-label words with small
high arcs and noncoprime four-label tracks remain open.
Novelty outside the repository is undetermined.

For `3x+q`, every actual step error is
`log_2(1+q/(3n_i))`, and the first ones run involves
`L+q`. The exact profile identity survives with that
addend. The q=1 minimum and `L+1` arguments cannot be
applied to normalized rational controls as integrality
statements. The certificate retains `q` explicitly.
Same-session audits do not confer independent-review status.

## History

- 2026-11-08: combined unequal weighted high-arc
  oscillations with an exact four-mismatch localization,
  obtaining the cone exclusion and the at-most-five
  concentration restriction with separate input scopes.
