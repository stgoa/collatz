# V001 — One rational map, invariant arithmetic layers

**Status: exploratory comparison; elementary identities below, no new convergence
result or novelty claim.** This bounded card supplements the mixed-place and
semigroup comparison in [symbolic_arithmetic.md](symbolic_arithmetic.md).
It changes no frozen result or programme standing.

## 1. Objects

On positive rational 2-adic units, use the **unabsorbed odd clock**

`R(x)=(3x+1)/2^v2(3x+1)`.

Write `x=a/b` in lowest terms, with a,b positive odd and `3∤b`. Then
`R(x)=(3a+b)/(b*2^v2(3a+b))`. Since `gcd(3a+b,b)=1`, the reduced denominator
b is invariant. Thus these are invariant subsets of positive rationals inside
the 2-adics, not assertions about generic 2-adic points.

For every positive odd d with `3∤d` and positive odd n,
`R(n/d)=S_d(n)/d`. To represent the repository's absorption at n=1, stop this
rational trajectory at **1/d**, not at rational 1. The identity otherwise
describes raw dynamics, including the continuation after that target.

## 2. Structural gain

The parameter d moves from the formula into the starting lattice and target.
There is a further exact decomposition: the reduced denominator of n/d is
`b=d/gcd(n,d)`, and `gcd(S_d(n),d)=gcd(n,d)`. Only the gcd-one stratum can
reach n=1. For composite d, a single d-system therefore uses several invariant
denominator layers. This separates primitive controls from scaled copies.

This language has a direct primary precedent: [Brent, *3x+1 dynamics on
rationals with fixed denominator*, §1](https://arxiv.org/html/math/0204170v1)
defines reduced-denominator layers and their invariance for denominators coprime
to 6. Brent uses the **shortcut clock**, whereas R here groups a whole odd arrow.

## 3. Translated gap

Denominator one consists of positive odd integers; the Collatz question is
whether every such orbit reaches 1. An invariant denominator supplies no
decreasing quantity and no coupling between different layers. Real lattice
spacing, exact valuation cylinders, affine offsets and word order remain the
same unresolved arithmetic information identified by the mixed-place card.
The frozen integer-prefix and itinerary-complexity results still apply;
renaming their realization problem does not strengthen them.

## 4. Exact small worked example

For d=1, `3 -> 5 -> 1` has odd word `(1,4)` and affine composition
`(9x+5)/32`. For d=5, normalization gives

`19/5 -> 31/5 -> 49/5 -> 19/5`,

with valuations `(1,1,3)` and composition `(27x+19)/32`. Its fixed point is
`x=19/5`. Hence this periodic word closes in denominator five and has no integer
fixed point. This excludes one integer cycle word; it does not exclude
nonperiodic divergence. A repeated word may also encode a shorter primitive
cycle, so its word length need not be the least period.

## 5. The 3x+d control and target check

The preceding cycle avoids 1/5. Also `S_5(5)=5`, which becomes `R(1)=1`:
calling rational 1 the universal absorber would incorrectly certify the original
seed 5. A proof using only the common rational formula must explain precisely
which property of denominator one, with its specified target, excludes the
controls. Denominator preservation alone cannot do so.

Brent's §2 presents the Böhm–Sontacchi–Lagarias periodic-word formula; its
Question 1.3 separately asks about divergent rational orbits. Its finite cycle
searches and proposed attracting basins are not convergence theorems. This
card imports none of those conjectures.

## 6. Cheapest next test

Translate one proposed survivor restriction into reduced numerator and denominator.
Require it to use denominator-one integrality over **unbounded nonperiodic
histories**, while preserving the d=5 cycle and the target distinction above.
If the denominator appears only as a constant label or in a closed-word
divisibility calculation, stop: that is already covered by this comparison
and the known cycle formula. No new computation is needed to reach that gate.

## 7. Genuinely partial milestone

A useful milestone would exclude positive integer realization of one explicitly
defined aperiodic survivor family, uniformly over all its prefix lengths,
beyond the frozen integer-prefix/complexity exclusions. That would address a
portion of possible divergent behavior, even while leaving other divergent
itineraries and nontrivial cycles unresolved. This first pass supplies neither
such a family nor a new estimate, so it is **not a ready proof target**.

**Selection:** retain rational layers as a precise control index and source of
target checks; defer them as an independent research direction. No extra
dynamical constraint beyond the mixed-place bookkeeping has emerged here.
