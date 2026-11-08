---
id: sparse-two-level-four-arc-exclusion
kind: result
title: Two rotations and discrepancy exclude two-level four-arc classes
status: written
claim: >
  Raw odd-only 3x+1 map. Let m=1+a+b+c, a,b,c>=1, V>=3,
  and gcd(h,m)=1. Suppose a positive valuation word, read along
  the cyclic index track x,x+h,..., is V followed by a ones,
  b twos and c ones. Under the declared gap EXT-1, no such word
  with m>=2^22 and b<=m/128 is the valuation word of a positive
  integer cycle. The unique letter V makes the word primitive.
  All positive arc lengths, every coprime track step and every V>=3
  are covered; no minimum-position, near-criticality or imported
  period hypothesis is used. An exact rational certificate over all
  1440 ordering cells proves that the agreeing-run inequalities
  for h and 2h need error greater than 1/193, whereas the stated
  integer-cycle hypotheses give a smaller error. This is a scoped
  four-mismatch exclusion, not the general rho>=5 claim.
  The same m>=2^22 exclusion also holds at every b when
  K(k/m)<=m/512, where k is the least positive inverse of h modulo m
  and K is the sum of regular continued-fraction partial quotients.
  This additional case uses the binary template obtained by replacing
  V by 1 and its proper-factor discrepancy 2(K-1); no new external
  assumption is needed.
authors:
  - Codex four-arc research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex main research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [paired-state-run-law, denjoy-koksma-height-bound]
assumes: [musson-collatz-gap-all]
certificates: [check_four_arcs.py]
evidence:
  - "check_four_arcs.json: exact dual replay for all 1440 cells, discrete mismatch and run checks, local descent, finite constants and eleven actual-cycle controls"
  - "explore_cells.py and explore_cells.json: discovery of sparse rational Farkas multipliers; only their standard-library exact verification is used in the proof"
  - "check_four_arcs.json: binary-template continued fractions, all proper factors on the stated finite grid, both envelope regimes and the additional exact cutoff"
tags: [cycles, rotation-distance, four-arcs, size-method, exact-certificates]
---

# Two rotations and discrepancy exclude two-level four-arc classes

## Statement

All clocks are raw odd-only. Let `a,b,c>=1`, `V>=3`,
`m=1+a+b+c`, and `gcd(h,m)=1`. Starting at an index `x`,
read the word along the track `x,x+h,...,x+(m-1)h` modulo `m`:

```
V, 1^a, 2^b, 1^c.                                      (1)
```

The superscripts here count letters. The order in (1) is
the track order, not necessarily the chronological order.
Assume the effective gap
[EXT-1](../../../../sources/musson-collatz-gap-all.md).
Then

```
m>=2^22 and b<=m/128  imply  den(w)>1 whenever D_w>0.    (2)
```

There is also an alternative that allows every positive `b`.
Let `k` be the unique integer `1<=k<m` with `kh=1 (mod m)`.
Write the regular continued fraction in its canonical finite form
`k/m=[0;d_1,...,d_l]`, with every `d_i>=1` and `d_l>=2`, and put
`K(k/m)=sum_i d_i`. Then

```
m>=2^22 and K(k/m)<=m/512  imply  den(w)>1
whenever D_w>0, with no density restriction on the twos. (2a)
```

The unique occurrence of `V` makes the word primitive.
Rotation by `h` has exactly four mismatches. We impose no
lower bound on the three arc lengths beyond positivity,
no upper bound on `V`, and no condition locating the cycle
minimum relative to `V`. This result does not cover all
four-mismatch words, other track-label patterns, or the
finite lengths below `2^22`. In (2a), it is the chronological
increment `k=h^(-1)` on the track whose continued fraction is used.

The argument completes one part of the earlier
[multi-rotation attempt](../../attempts/multi-rotation-four-mismatch-exclusion/README.md):
its equal-outer-label pattern, with sparse twos. The sampled
continuous cells are replaced by an exhaustive exact
certificate, and the finite-length, short-arc and
minimum-location errors are retained.

## Proof

If `D_w>0` and `den(w)=1`, the positive rotated states
`C_rot/D_w` are integers. The rotation identity
`2^(w_i)*C_next=3*C_rot+D_w` propagates integrality,
because `D_w` is odd; both intercepts and `D_w` are odd.
Thus these are positive odd states with exactly the
specified valuations. It suffices to exclude that actual
integer cycle.

### 1. The two mismatch supersets

Rotate chronological indices so the spike is at `x=m-1`.
Reversing the track exchanges `a` and `c`, so we may choose
the orientation with `0<h<m/2`. Both `h` and `2h` are
nonidentity rotations: `gcd(h,m)=1` and `m>=4`.
Put

```
P1=x+a*h,       P2=x+(a+b)*h             (mod m).
```

The mismatch set for `h` is exactly

```
E1={x, x-h, P1, P2}.                                (3)
```

A mismatch for `2h` lies in `E1` or `E1-h`. That union
differs from the displayed `E2` only by `x-h`; at that point
the two compared letters are both 1, because `a,c>=1`.
Consequently

```
mis(2h) is a subset of
E2={x, x-2h, P1, P1-h, P2, P2-h}.                    (4)
```

The points in (4) may coincide, and some may be agreements.
This causes no problem. Cutting an agreeing run at extra
points only shortens it. For two consecutive distinct
points of either superset, separated by `d` chronological
steps, the `d-1` positions strictly between them agree.
Primitivity supplies distinct paired states for both
rotations even when an endpoint is an artificial cut.

### 2. An exact continuous obstruction

Use coordinates `(i+1)/m` in `(0,1]`, so the spike has
coordinate `X=1`. Let `u=h/m`, and let `p<=q` be the
coordinates of `P1,P2` in either order. Thus `0<u<=1/2`
is a harmless closed relaxation. The two boundary lists are

```
E1: 1, R=1-u, p, q;
E2: 1, Q=1-2u, p, p-u (mod 1), q, q-u (mod 1).       (5)
```

Represent residues in `(0,1]`. At a boundary coordinate
`e`, the larger of the two paired coordinates for rotation
`ku`, `k=1,2`, is

```
H_k(e)=e+ku  if e<=1-ku,
       e     if e>1-ku.                              (6)
```

In particular equality in the first branch has partner 1,
not 0. For consecutive boundary points, write `gap` for
their forward circular distance; the first gap after the
point 1 is the first coordinate itself.

The finite certificate establishes the following rational
statement:

```
There are no u,p,q,epsilon satisfying (5), all ordering
conditions, epsilon<=1/193, and, for every gap of both lists,

gap <= (3/8)*H_k(e)+epsilon.                         (7)
```

Here is the exhaustive construction behind that statement.
Each of `p-u,q-u` has two representatives, according to
whether 1 is added. There are `2^2=4` wrap choices. Order
the five non-spike points of `E2` in every one of `5!=120`
ways. Since `p<=q`, there are three orders of `p,q,R`
in `E1`. This gives exactly `4*120*3=1440` cells. Every
cell includes the box, wrap and weak-order inequalities.
The position of `R` or `Q` in its list determines the
branch of (6). All constraints are rational linear
inequalities in `(u,p,q,epsilon)`.

This enumeration covers boundary cases too. If `p=u`,
choose the wrapped representative `p-u+1=1`. If several
points equal a witness threshold, place all other tied
points before the labelled `R` or `Q`; they then use
the partner 1. Such weak orders occur in the enumeration.
Duplicate consecutive points have gap zero and impose
only a redundant inequality.

For every cell, the certificate supplies nonnegative
rational multipliers for at most five of its inequalities.
The four variable coefficients cancel exactly, while the
weighted constant side is strictly negative. Thus that
cell would imply that zero is at most a negative number.
All 1440 combinations are checked
with rational arithmetic. The smallest negative magnitude
is `1/4824`; no optimization solver, floating-point
tolerance, sampled-cell coverage or unproved LP result
is used by the checker.

### 3. A finite envelope without aligning the minimum

Suppose (1) were the valuation word of an integer `3x+1`
cycle. Let `L` be its minimum and `n0` its state just after
the spike. Exact local descent for the 63 odd seeds
`3,5,...,127` proves that every one reaches 1. The cycle
is primitive and contains a letter `V>=3`, so it is
nontrivial and

```
L>=129.                                             (8)
```

Every odd step grows by at most
`(3+1/L)/2 <= 194/129`. The exact comparison

```
388^8 < 27*256*129^8
```

therefore bounds its logarithmic growth, in base 3, by
strictly less than `3/8` per step.

The chronological path from `n0` to the global minimum
does not cross the spike again. A valuation-1 step
increases a positive state, while a valuation-2 step
multiplies it by more than `3/4`. There are at most `b`
such 2-steps, so

```
n0 < (4/3)^b*L,
log_3(n0) < log_3(L)+b/3,                            (9)
```

where `(4/3)^3<3` proves the second, deliberately loose,
bound. If the minimum is already `n0`, (9) remains strict
because `b>=1`. At every coordinate `e=(i+1)/m`, the
state before that letter consequently satisfies

```
log_3(n_i) < log_3(L)+b/3+(3/8)*m*e.                (10)
```

The extra coordinate step in (10) only enlarges the
upper bound.

For an induced agreeing run of length `t=d-1`, the
[paired-state run law](../paired-state-run-law.md) gives
`max(n_e,n_(e+kh))>2*3^t`. This also follows directly by
subtracting the paired arrows: their nonzero even state
difference at the run end is a nonzero multiple of
`2*3^t`. Combine this with (10). Every positive gap in
(5) satisfies (7) with

```
epsilon=[log_3(L)+1]/m+b/(3m).                      (11)
```

The `+1` retains the difference between a gap of `d`
steps and its `d-1` agreeing positions. Zero gaps satisfy
the same inequalities automatically.

### 4. EXT-1 makes the error smaller than the exact margin

Write `A=sum(w)`, `D=2^A-3^m`, and `eta=D/2^A>0`.
The product identity and `log(1+t)<t` give

```
eta < log(2^A/3^m) < m/(3L).
```

EXT-1 gives `eta>=1/(2^172*m^341)`. Hence

```
L<2^172*m^342/3,
log_3(L)<172+342*log_2(m).                          (12)
```

Combining (11), (12) and `b<=m/128` yields

```
epsilon < [173+342*log_2(m)]/m+1/384.               (13)
```

For `2^k<=m<2^(k+1)`, `k>=22`, the right side is at most

```
[173+342*(k+1)]/2^k+1/384.
```

This decreases with `k`: the next numerator increases
by 342 while its denominator doubles. At `k=22` it is

```
56885/12582912 < 1/193,
1/193-56885/12582912 = 1604107/2428502016.            (14)
```

Thus (11) supplies a solution forbidden by the exact
certificate (7). This contradiction proves (2).

### 5. Every density of twos with controlled continued fractions

For this extension, first fix the original track orientation `h`
from the Statement, before making the geometric reversal in
section 1. Establish (15) using its original inverse `k`.

Replace the single letter `V` by 1, obtaining the binary template
`U`. Its total is `F=m+b`, with mean `beta=F/m`. On the track,
the two outer 1-arcs merge, so the mean-zero function `U-beta`
has cyclic total variation exactly 2. Consecutive chronological
letters advance by `k=h^(-1) (mod m)` on this track.

The discrete Denjoy--Koksma and Ostrowski core in
[the height result](../denjoy-koksma-height-bound/README.md)
applies to any mean-zero periodic function and every starting
phase. Hence every proper chronological factor of `U`, of any
length `j<m`, satisfies

```
|sum(factor)-beta*j| <= Delta,     Delta=2(K(k/m)-1).   (15)
```

This is a bound for all factors, including those crossing the
chronological cut. It does not apply a cycle-height bound to
the spiked word or charge the large letter `V` to the variation.
Reversing the track in section 1 changes no word or factor in
(15); the bound remains available without recomputing `K`.

First suppose `beta<alpha=log_2(3)`. The chronological segment
from the state `n0` just after the spike to the global minimum
contains no spike. For its length `j`, (15) bounds its affine
slope below by

```
3^j/2^(sum of its letters) >= 2^(-Delta)*(3/2^beta)^j
                           >= 2^(-Delta).
```

Its additive term is nonnegative, so `n0<=2^Delta*L`; this also
holds for the empty segment. Replace (9) by
`log_3(n0)<=log_3(L)+Delta/alpha`. Sections 2--4 therefore apply
with the new error

```
epsilon=[log_3(L)+Delta/alpha+1]/m.                   (16)
```

Since `alpha>3/2` and `K<=m/512`,
`Delta/(alpha*m)<4K/(3m)<=1/384`. Thus (13)--(14) bound
(16) by exactly the same ceiling below `1/193`, proving (2a)
in this first case. This replaces the density term by discrepancy;
no restriction on `b/m` was used beyond `beta<alpha`.

Now suppose `beta>=alpha`. Increasing one letter cannot reduce
any factor sum, so every proper factor of `w` has total at least
`beta*j-Delta`, even if it contains the spike. Its slope and the
slope of each of its suffixes are at most `2^Delta`, because
`3/2^beta<=1`. The exact affine expansion of a segment of length
`l<m` is

```
n_l=(3^l/2^E_l)*n_0
    +(1/3)*sum_(j=1)^l 3^j/2^(total of the length-j suffix).
```

Apply it from the minimum to the maximum `H`. It gives

```
H <= 2^Delta*(L+m/3)
  < (2/3)*2^Delta*m*G,       G=2^172*m^341,           (17)
```

using `L<mG/3` and `G>1`. The four mismatches for `h` leave
an agreeing run of length at least `m/4-1`; the paired-state
law therefore gives `H>(2/3)*3^(m/4)`. Combining with (17),

```
alpha*m/4 < Delta+172+342*log_2(m).                  (18)
```

But `Delta<m/256` and `alpha>3/2` would require
`95m/256<172+342*log_2(m)`. For `2^j<=m<2^(j+1)`, `j>=22`,
the left side is at least `95*2^j/256` and the right side
is less than `172+342*(j+1)`. At `j=22` their difference is
`1548442>0`; doubling the first bound and adding only 342
to the second preserves the contradiction for every larger
`j`. This proves (2a) in the second case, and completes the
all-density extension.

## Certificates

Run from the repository root:

```
python3 areas/cycles/results/sparse-two-level-four-arc-exclusion/check_four_arcs.py
python3 -O areas/cycles/results/sparse-two-level-four-arc-exclusion/check_four_arcs.py
```

The standard-library [checker](check_four_arcs.py) reconstructs
every cell, verifies its sparse rational multipliers in
[explore_cells.json](explore_cells.json), and checks the
discrete mismatch supersets and induced agreeing runs on
an exhaustive small-word grid that includes short arcs
and coincident points. It also replays local descent,
the exact constants above, and all eleven shared actual
`3x+5,7,13,61` fixtures and their paired-state run bounds.
Its deterministic [receipt](check_four_arcs.json) records
the finite coverage. Use `--write-receipt` to regenerate it.
The same checker also constructs the binary templates for all
coprime track steps and positive arc lengths in its stated small
length range, verifies the chronological inverse and every proper
factor discrepancy, and checks the two state envelopes on exact
reduced `3x+q` cycles. Those envelope comparisons retain `q` in
the additive term. The all-length argument and its `q=1` exclusion
are proved above, not inferred from this finite grid.

The discovery script [explore_cells.py](explore_cells.py)
uses SciPy only to find small dual supports. It then solves
and verifies the multipliers exactly before writing its
JSON. SciPy is not needed by the certificate or the proof;
the supplied rational combinations can be checked without
trusting their method of discovery. Exploration is not run
by CI.

## Remarks

This is a completion of a scoped branch of the old
[S10 attempt](../../attempts/multi-rotation-four-mismatch-exclusion/README.md),
not a claim that its full continuous programme is settled.
The old [S8 words](../../attempts/four-mismatch-size-method-limit/README.md)
have exactly the track pattern (1). Their sparse-twos
regime is now excluded whenever the explicit bounds (2)
hold. The proof covers arbitrary small arcs and every
coprime step; it does not assume the old minimum alignment
or replace a grid margin by an asserted uniform margin.

Other outer labels, two sign changes of each kind,
multiple tracks, and words satisfying neither the density nor
the continued-fraction condition remain outside this result.
The general
[four-mismatch question](../../questions/rotation-distance-at-least-5.md)
is still open. The minimum and slope estimates are
specific to `3x+1`; actual `3x+d` controls retain their
own addend and are not excluded.

The added discrepancy argument uses the same formal rotation core
and affine suffix expansion as the earlier
[Fibonacci-spike template result](../fibonacci-four-arc-spike-denominator-growth/README.md).
That result treats an expanding three-label template and an explicit
Fibonacci family. Here the binary template has variation 2, and the
two-rotation obstruction handles its expanding case even at very low
twos density. The contracting case uses the existing repeated-run
height method. No new discrepancy theorem or novelty for these tools
is claimed; novelty of the scoped extension is undetermined.

The multi-rotation mechanism and its proposed cell
certification come from the earlier Claude side lane
and its recorded review. This node supplies exhaustive
exact cells and the finite transfer for (1)--(2).
Novelty beyond this repository is undetermined.
Same-session audits do not constitute an independent
review or a Lean formalisation.

## History

- 2026-11-08: completed the sparse equal-outer-label
  branch of the multi-rotation size method with exact
  rational certificates and explicit finite errors.
- 2026-11-08: retained the original sparse-twos statement and
  added the alternative `K(h^(-1)/m)<=m/512` for every twos
  density, using the binary-template discrepancy and separate
  expanding and contracting mean cases. The cutoff remains
  `m>=2^22`, with EXT-1 still the sole external input.
