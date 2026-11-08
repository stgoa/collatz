---
id: two-level-four-arc-phase-exclusion
kind: result
title: Short rational phases exclude the two-level four-arc family
status: written
claim: >
  Raw odd-only 3x+1 clock. Let a,b,c>=1, V>=3,
  m=1+a+b+c, and gcd(h,m)=1. Suppose a positive valuation
  word, read along a cyclic h-track, is V,1^a,2^b,1^c.
  Under EXT-1, m>=2^34 and D_w>0 imply den(w)>1, with no
  density or continued-fraction restriction. A hypothetical
  integer cycle forces b+512<m/3. The inverse-continuant
  bridge then supplies Qk-pm=+j or -j, with gcd(p,Q)=1
  and jQ<=512. For Q>=2 every Q-window of the binary
  template expands; for Q=1 two consecutive maximal ones
  runs contradict exact integral run divisibility and the
  minimum-state bound. With the additional declared Barina
  convergence input, the replayed odd-period lower bound
  72,057,431,991>2^34 excludes denominator one for every
  length in this specified family. The first conclusion
  does not use that convergence or period input. Other
  four-mismatch patterns and other background alphabets
  remain outside the claim.
authors:
  - Codex signed-endpoint research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex main research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [paired-state-run-law, four-mismatch-inverse-continued-fraction-bound, sparse-two-level-four-arc-exclusion, cycle-length-lower-bound-from-convergents]
assumes: [musson-collatz-gap-all, barina-2025-convergence-2-71]
certificates: [check_phase_runs.py]
evidence:
  - "check_phase_runs.json: rational-grid windows, small-step run decompositions, exact integer-run identities, dyadic thresholds, local descent and actual-cycle controls"
tags: [cycles, four-arcs, rotation-distance, continued-fractions, ones-runs, effective-exclusion]
---

# Short rational phases exclude the two-level four-arc family

## Statement

Use the raw odd-only clock. Let `a,b,c>=1`, `V>=3`,
`m=1+a+b+c`, and `gcd(h,m)=1`. Reading a valuation word
along the cyclic index track `x,x+h,...,x+(m-1)h` gives

```
V, 1^a, 2^b, 1^c.                                      (1)
```

The exponents in (1) count letters. The track order need
not be chronological order. The unique letter `V` makes
the word primitive.

**Large-period theorem.** Under
[EXT-1](../../../../sources/musson-collatz-gap-all.md),

```
m>=2^34 and D_w>0  imply  den(w)>1.                     (2)
```

There is no restriction on `b/m`, on the size of `V`, on
the continued fraction of the inverse track step, or on
the position of the cycle minimum. This theorem uses no
imported period or convergence bound. The only convergence
calculation needed for (2) is the local replay of odd seeds
from 3 through 127.

**All-length corollary.** Assume in addition
[Barina's declared verification below `2^71`](../../../../sources/barina-2025-convergence-2-71.md).
Then `D_w>0` implies `den(w)>1` for every word (1),
without a length restriction. The
[replayed period theorem](../cycle-length-lower-bound-from-convergents/README.md)
supplies `m>=72,057,431,991>2^34` for a nontrivial
integer cycle. This is the only use of that additional
source; it is not used in the proof of (2).

The result concerns this particular coprime-track
four-arc family. It does not exclude every four-mismatch
word or every positive `3x+1` cycle.

## Proof

Suppose `D_w>0` and `den(w)=1`. The rotated intercept
identity `2^(w_i) C_next=3 C_rot+D_w`, with `D_w` odd,
supplies positive odd integer states with exactly the
specified valuations. The unique `V` prevents a shorter
word period, so these states form a primitive nontrivial
cycle. We prove (2) by contradiction.

Put

```
alpha=log_2(3), L=min(n_i), H=max(n_i),
ell=log_2(L), B=log_2(H/L), k=h^(-1) mod m, 0<k<m.
```

Replacing the single `V` by 1 gives a binary template `U`.
On the track its twos occupy one cyclic interval of `b`
sites, and the complementary ones interval has length
`n=m-b`. Consecutive chronological positions advance by
`k` on this track.

### 1. Integer-cycle height forces less than one third twos

The local descent replay gives `L>=129`. Each valuation-1
arrow increases the state by at most `194/129`, while
every arrow with valuation at least 2 strictly decreases
it. The exact integer comparisons

```
194^32 < 2^19*129^32,     3^53 > 2^84                 (3)
```

give an upper bound `19/32` for the dyadic increase per
one-arrow and `alpha>84/53`. A chronological path from
the minimum to the maximum uses at most the word's
`m-b-1` one-arrows. Therefore

```
B < (19/32)(m-b-1).                                  (4)
```

Rotation by `h` has exactly four mismatches. Some
agreeing run has length at least `m/4-1`, and the
[paired-state run law](../paired-state-run-law.md)
gives `H>2*3^(m/4-1)`. Using (3), and `m>=4`,

```
ell+B > alpha*m/4+1-alpha > 21m/53-1.
```

Combining with (4) yields

```
b < (335/1007)m+(32ell+13)/19.                        (5)
```

Write `E=sum(w)` and `eta=(2^E-3^m)/2^E`. The product
identity and `log(1+t)<t`, followed by EXT-1, give

```
eta < m/(3L),       eta >= 2^-172*m^-341,
ell < 172+342log_2(m).                               (6)
```

For `m>=2^34`, (5)--(6) imply the useful strict margin

```
b+512 < m/3.                                        (7)
```

Here is an integer verification of the whole unbounded
range. If `2^d<=m<2^(d+1)`, `d>=34`, the desired
inequality follows from

```
2^(d+1) > 4164051+1740096d.                          (8)
```

At `d=34` the margin is `34296411053`. Twice the right
side at `d` minus its value at `d+1` is
`2423955+1740096d>0`, so induction proves (8).
The constants in (8) simply clear denominators in (5),
using `1/3-335/1007=2/3021`.

### 2. Retain the full rational phase from the inverse bridge

The earlier
[two-level theorem](../sparse-two-level-four-arc-exclusion/README.md)
already excludes this integer cycle if either `b<=m/128`
or `K(k/m)<=m/512`, since `m>=2^34>=2^22`. We may hence
assume

```
b>m/128,       K(k/m)>m/512.                          (9)
```

The elementary part of the
[inverse-continuant result](../four-mismatch-inverse-continued-fraction-bound/README.md)
applies at `m>=2^34`. Retaining its preceding convergent,
rather than just the short cyclic distance, gives integers

```
Q>=1, j>=1, gcd(p,Q)=1,
Qk-pm=+j or -j,       jQ<=512.                       (10)
```

This is equation (5) of that result, with its tail
continuant renamed `j`. Both end coefficients are
included: the initial preceding fraction is `0/1`,
and the empty final tail has continuant 1. In particular,
`Q,j<=512`. No cycle estimate is used to derive (10).

### 3. If Q is at least two, every Q-window expands

Fix any chronological starting phase `theta`. The `Q`
successive template positions, normalized to the unit
circle, are

```
theta+p*s/Q +/- j*s/(Qm)  (mod 1),    0<=s<Q.         (11)
```

The unperturbed points form a translated uniform `Q`-grid,
because `gcd(p,Q)=1`. The perturbations are one-sided and
their range has length strictly less than `j/m`. The
twos form a half-open circle interval of length `b/m`.
Every grid point whose perturbed point is a two therefore
lies in a circle interval of length at most `(b+j)/m`,
which is strictly less than `1/3` by (7).

An interval of length less than `1/3` contains at most
`ceil(Q/3)` points of a uniform `Q`-grid: one more point
would span at least `ceil(Q/3)/Q>=1/3`. This argument
includes wrapped intervals and arbitrary endpoint phases.
For `Q>=2`, `ceil(Q/3)<=Q/2`. Consequently every
chronological template window of length `Q` has total
valuation at most `3Q/2` and affine slope at least

```
3^Q/2^(3Q/2)>1,                                    (12)
```

using `3^2>2^3`. Its additive term is positive, so it
increases its starting positive state.

Let `n0` be the state immediately after the spike. The
chronological path from `n0` to the global minimum
does not cross the spike. Partition this path into
full `Q`-windows and a final remainder of fewer than
`Q` arrows. Every full window expands by (12); each
remaining binary arrow multiplies its state by more
than `3/4`. Thus, including the empty-path case,

```
n0 < (4/3)^(Q-1)*L,
log_3(n0) < log_3(L)+(Q-1)/3,                        (13)
```

where `(4/3)^3<3` and `Q>=2` preserve strictness.

The exact two-rotation obstruction in section 2 of the
[two-level theorem](../sparse-two-level-four-arc-exclusion/README.md)
now applies with its error term

```
epsilon=[log_3(L)+(Q-1)/3+1]/m
       < [173+342log_2(m)+511/3]/m.                  (14)
```

Indeed, that obstruction only needs the post-spike
height envelope, the per-step base-3 slope below `3/8`
at `L>=129`, and the agreeing-run end witnesses. It
does not need the earlier density estimate for `n0`.
Its exact rational certificate says every such envelope
has `epsilon>1/193`.

For `2^d<=m<2^(d+1)`, the bound in (14) is at most

```
(2056+1026d)/(3*2^d).
```

At `d=34`, its product with 193 is
`1782355/12884901888<1`. It decreases thereafter,
because `2(2056+1026d)-(2056+1026(d+1))=1030+1026d>0`.
This contradicts the exact obstruction and rules out
`Q>=2`.

### 4. If Q equals one, two long runs force a large minimum

Equation (10) now says `k=+j` or `-j mod m`, with
`gcd(j,m)=1` and `1<=j<=512`. By (7) and (9), both
binary track intervals have length greater than `j`.

For the chronological step `+j`, each entry into the
ones interval starts at one of its first `j` residues.
The orbit visits each residue once, so there are exactly
`j` entries and `j` maximal positive ones runs. Their
lengths are

```
floor(n/j) or ceil(n/j),       n=m-b.                (15)
```

To see (15) directly, put the ones interval at `[0,n)`.
An entry residue is `r` with `0<=r<j`; its run has
`ceil((n-r)/j)` points. The other interval has length
greater than `j`, so the orbit cannot jump over it and
merge runs. Reversing chronological order proves the
same assertion for `-j`.

Changing one 1 to `V` splits at most one of these
binary runs. Let `t0,t1` be the lengths of any two
consecutive maximal positive ones runs of the actual
word, counting cyclically. Then

```
t0+t1 >= floor(n/j)-1.                              (16)
```

If either run is an unchanged binary run, it already
has length at least `floor(n/j)`. Otherwise the two
runs are the pieces of the single split run, with
total at least `floor(n/j)-1`. A zero split piece is
discarded when taking maximal positive runs. If there
is only one positive run, take it twice cyclically;
the same inequality holds. These possibilities include
`j=1` and a spike at either end of a binary run.

The global minimum `L` starts a maximal positive ones
run: a non-one arrow starting there would decrease it,
and a preceding one-arrow would have a smaller state.
We use (16) for the first two runs from this minimum.

For a maximal ones run of length `t>=1` starting at
an integer state `x`, followed by a valuation `e>=2`,
the exact formula and terminal congruence give

```
x+1=2^(t+1)u,       u a positive odd integer,
x_after=(3^(t+1)u-1)/2^(e-1).                       (17)
```

In particular,

```
t+1 <= log_2(x+1),
x_after+1 <= (3^(t+1)u+1)/2
          < 3^(t+1)u <= (x+1)^alpha.                (18)
```

All further non-one arrows before the next positive
ones run decrease the state and its shift by 1.
Applying (18) twice, starting at `L`, therefore gives

```
t0+t1+2 < (1+alpha)log_2(L+1)
         < (13/5)(173+342log_2(m)).                 (19)
```

Here `alpha<8/5` follows from `3^5<2^8`, and (6)
bounds `log_2(L+1)<ell+1`.
On the other hand, (7) and (16) give

```
t0+t1+2 >= floor(n/j)+1 > n/j
         > 2m/(3j) >= m/768.
```

Combining with (19),

```
m < (9984/5)(173+342log_2(m))
  < 2048(173+342log_2(m)).                           (20)
```

This is impossible at `m>=2^34`. On the dyadic interval
above it would require
`2^d<2048(515+342d)`. At `d=34` the opposite inequality
has margin `17155000320`; its persistence follows from
`2(515+342d)-(515+342(d+1))=173+342d>0`.
Thus `Q=1` is also impossible, proving (2).

### 5. The separately sourced all-length corollary

Under the additional Barina input, the
[period replay](../cycle-length-lower-bound-from-convergents/README.md)
gives at least `72,057,431,991` odd states in every
nontrivial positive integer `3x+1` cycle. The unique
spike in (1) ensures primitivity and nontriviality, and

```
72057431991 > 2^34=17179869184.
```

The large-period theorem therefore applies. Barina's
external convergence computation is not rerun here;
the continued-fraction period certificate is replayed.
The graph lists both sources because it records this
corollary as well as (2), but sections 1--4 use only EXT-1.

## Certificates

Run from the repository root:

```
python3 areas/cycles/results/two-level-four-arc-phase-exclusion/check_phase_runs.py
python3 -O areas/cycles/results/two-level-four-arc-phase-exclusion/check_phase_runs.py
```

The standard-library [checker](check_phase_runs.py)
checks exact rational phase windows, both signs of the
short step, all spike positions on its stated finite
run grid, the exact integral ones-run identities, all
dyadic base margins and induction coefficients, and
local descent through 127. It replays the existing
period certificate and the exact two-rotation cell
certificate, and checks the eleven shared actual
`3x+5,7,13,61` cycles with their addends retained.
Its generated [receipt](check_phase_runs.json) states
the finite coverage; use `--write-receipt` to regenerate
it. The proof above, not a census of words, covers
unbounded lengths and amplitudes.

## Remarks

The new step retains the rational phase in the inverse
bridge. A uniform grid with at least two points forces
short expanding blocks once the integer-cycle height
budget gives (7). The one-point grid instead forces
long actual ones runs; exact integrality then supplies
the missing constraint. A bounded number of periodic
pieces alone would not justify either argument.

This extends the earlier sparse-density, controlled-
continued-fraction and `2^1536` conclusions without
altering those merged statements. The counterfamily
in the
[bounded-period reduction obstruction](../sparse-rotation-bounded-period-reduction-obstruction/README.md)
does not contradict this proof: (5)--(7) are necessary
conditions for an actual integer `3x+1` cycle, and
(10) is used only in the large-complexity regime.

The argument is specific to `q=1`. At addend `q>1`,
the product and minimum bounds contain `q`, the
one-arrow growth depends on `q/L`, and (17) involves
`x+q`; dividing states by `q` loses the integer
quotient used in (18). The actual positive `3x+d`
controls are not excluded.

Novelty beyond the repository is undetermined. The
continued-fraction arithmetic, agreeing-run law and
few-runs divisibility are classical or already present
here; the scoped phase/run combination is the present
contribution. Same-session audits do not confer
independent-review or formal status.

## History

- 2026-11-08: used the inverse-continuant phase, a
  q=1-specific twos-density constraint and two maximal
  ones runs to close the large-complexity branch of
  this four-arc family at `m>=2^34`; separated the
  EXT-1-only theorem from the all-length corollary
  using the declared convergence-derived period input.
