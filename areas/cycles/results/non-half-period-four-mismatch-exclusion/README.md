---
id: non-half-period-four-mismatch-exclusion
kind: result
title: A four-mismatch rotation must be the half-period shift
status: written
claim: >
  Raw odd-only 3x+1 clock. Let a nontrivial primitive positive integer
  cycle have m odd states and valuation word w, and suppose a
  nonidentity shift H has exactly four mismatches. Put
  M=m/gcd(H,m). If M>=3, EXT-1 forces m<2^26. With the separately
  declared Barina convergence input, every such shift has M=2:
  m is even and H=m/2 modulo m. Hence at most one shift of a
  hypothetical cycle can have exactly four mismatches, and an
  odd-period cycle has none. The half-period case, larger mismatch
  counts and divergent orbits are not settled. The finite geometric
  step covers all orders 3 through 18 using the fact that four
  mismatches occupy one track with four cuts or two tracks with
  two cuts each; the general high-order theorem handles M>18.
authors:
  - Codex root research lane (GPT-6; directed by Santiago Armstrong)
  - Codex residue research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [high-order-four-mismatch-exclusion]
assumes: [musson-collatz-gap-all, barina-2025-convergence-2-71]
certificates: [check_non_half_period.py]
evidence:
  - "check_non_half_period.json: exhaustive rational polygon certificate, track reconstruction, exact modular comparisons and actual addend-aware controls"
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
`w_i!=w_(i+H)`, and put `M=m/gcd(H,m)`. If `s(H)=4` and
`M>=3`, then under
[EXT-1](../../../../sources/musson-collatz-gap-all.md),

```
m<2^26=67108864.                                      (1)
```

With the separately declared
[Barina convergence input](../../../../sources/barina-2025-convergence-2-71.md),
the replayed odd-period lower bound `72057431991` contradicts (1).
Therefore every four-mismatch shift has order two:

```
m is even,       H=m/2 modulo m.                      (2)
```

There is at most one such shift. If the least odd period `m` is
odd, no shift has exactly four mismatches. There is no restriction
on the letters or their multiplicities, and no coprimality
assumption on `H`.

This does not exclude the half-period case or all cycles. The
pure geometric lemma below is unconditional; the application to
cycles has the two input scopes just stated.

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

Set `R=3/8`, `eta=1/10000`, and
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
max_(1<=j<=M-1,e in C_j) D_j(e) >= eta.               (6)
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
and zero otherwise. Thus `D_j(e)<eta` is exactly the strict
affine inequality

```
z-z'-R*z+k-k'+M*I-R*max(k,k'')-M*eta < 0.            (9)
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
After 586929 affine rows in total, every family has zero feasible
area. No family survives. A positive-area survivor is a failure
of the certificate; the program has no search cutoff and trusts
no saved solver output. These finite counts and the exact replay
prove (6) for generic phases.

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
All finitely many strict deficits remain below eta for a
sufficiently small left translation. This would give a generic
counterexample already excluded in section 3. Hence (6)
includes the phase-zero boundary.

### 5. Transfer to an actual cycle

Use the actual minimum as state zero. The
[general high-order argument](../high-order-four-mismatch-exclusion/README.md),
sections 1--4, establishes the following implications for any
finite list of nonidentity multiples of H. Put

```
alpha=log_2(3),       ell=log_2(min_i n_i),
E=sum_i w_i,         delta=E-m*alpha,
epsilon=(ell+delta+alpha)/(alpha*m).
```

The state-index upper envelope is

```
log_2(n_i)<=ell+(alpha-1)*m*f(i/m)+delta.
```

Every gap G between consecutive refined cuts in C_j contains
exactly mG-1 agreeing arrows. Primitivity and oddness give
a nonzero paired difference of magnitude at least
`2*3^(mG-1)` at its endpoint. Combining these two facts gives

```
D_j(e)<epsilon.                                      (11)
```

These facts use only that jH is nonidentity, not that M exceeds
eighteen. Thus they apply to every j=1,...,M-1 in the present
finite-order lemma. Equations (6) and (11) force
`epsilon>=1/10000`.

The same input-separated cutoff proof then applies unchanged.
Local descent below `2^17` bounds the drift term by `1/393216`,
and EXT-1 gives

```
epsilon<(2/(3m))*(175+342log_2(m))+1/393216.
```

For `m>=2^26` this is at most

```
9665/100663296 < 1/10000,
```

a contradiction. Therefore (1) holds for 3<=M<=18.
For M>18 it is precisely the earlier high-order theorem.
All M>=3 are now covered under EXT-1 alone.

Finally, the separately declared Barina-dependent odd-period
bound `72057431991>2^26` excludes every M>=3 case. A
nonidentity rotation has M>=2, leaving only M=2, equivalent
to (2).

## Certificates

The self-contained standard-library checker is
[`check_non_half_period.py`](check_non_half_period.py).
Run from the repository root with Python 3.10 or later:

```
python3 areas/cycles/results/non-half-period-four-mismatch-exclusion/check_non_half_period.py
python3 -O areas/cycles/results/non-half-period-four-mismatch-exclusion/check_non_half_period.py
```

The generated [receipt](check_non_half_period.json) records the
complete discrete coverage, exact clipping totals, direct modular
comparisons, boundary checks and actual positive-addend controls.
The default command verifies it; `--write-receipt` regenerates it.
The exhaustive mathematical step is generated from M, a, K and L;
it does not depend on a saved list of numerical certificates.

The direct modular controls compare 670140 affine-row evaluations
with the actual circular gaps and paired heights. The cycle controls
cover 788 actual primitive positive-addend cycles, 21008 arrows
and 104208 refined agreement runs, including both track partitions
and shift gcds 1, 2 and 3. They exercise 53960 artificial cuts and
148832 raw-cut coincidences. All eleven shared positive-addend
fixtures are also replayed. These controls validate the formulas;
the full finite absence proof is the exhaustive polygon computation.

The controls retain their actual addends. The paired run identity
cancels the common addend, while the small drift budget in section 5
is specific to q=1. The known positive cycles for other addends
are not normalized into integer q=1 cycles.

The half-period boundary is checked separately: for M=2, h=1/2,
and `C={0,1/4,1/2,3/4}`, the single nonidentity rotation has
maximum deficit `-1/32`. This is a genuine two-track cut
configuration, and it survives even at zero error. The present
geometric method therefore does not remove the remaining order two.

## Remarks

The free-cut model admits controls at several small orders.
Their four cuts need not obey the track structure forced by an
actual mismatch set. The improvement here is to impose that
necessary structure before enumerating the remaining finite
orders; no letter-value assumption is added.

The general four-mismatch question is now the half-period
question under the stated inputs. For M=2, four mismatches
mean exactly two unequal pairs between the half-words.
The existing signed-endpoint and near-doubled results address
subclasses, but unrestricted half-word changes remain open.

This is a written conditional result, not a Lean formalization.
The exhaustive rational certificate and same-session audits do
not confer independent-session reviewed status. Novelty outside
the repository is undetermined. Neither all cycles nor the
Collatz conjecture are excluded.

## History

- 2026-11-08: used the cyclic-track partition of four mismatches
  to reduce the remaining geometry to exact polygons in two
  phase variables. Exhausted all orders 3 through 18 and combined
  the result with the high-order theorem, leaving only the
  half-period shift.
