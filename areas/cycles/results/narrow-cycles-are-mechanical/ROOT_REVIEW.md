# C004 root review

**2026-10-19. Written proofs and fresh finite replay pass.** This is
not formal verification, human publication review or a novelty claim.

## Mathematical review

I independently checked the complete cyclic-matrix argument. At every
prime dividing D, the homogeneous recurrence has exactly one free
coordinate; other primes give invertibility. This proves that the first
m-1 Smith factors are one, including prime-power cancellation. The
augmented maximal minors are the rotation coefficients and D. The
displayed kernel vector is primitive and generates the entire integer
kernel. Positive odd scaling, and the additional prime-to-3 restriction
on the supported parameter domain, are explicit.

The one-letter commutator identity implies
`gcd(D,K_i)=g*gcd(D/g,2^a_i-3)`, not an unconditional equality to g.
The extra factor disappears at valuations1/2. The maximum-state
argument requiring a valuation1 is specifically for a nontrivial d1
integer cycle. These statements do not assume generalized maps lack
their actual cycles.

I supplied the geometric mechanism and independently checked the
author's final derivation. If all odd states lie in `[L,2L)`, the
increasing values `3x+1` also span less than a factor two. Exact
normalization has one exponent threshold. The high-exponent block of
h sorted states moves to the first h ranks, so the successor adds h
modulo m. Primitivity supplies coprimality and the mechanical floor
differences. The converse retains the unchanged first coefficient term,
making the factor-two bound strict. Proper powers reduce their totals
before the exact denominator is used. Fixed points and the impossible
H=2L endpoint are treated separately.

The result identifies R71's existing mechanical class by an intrinsic
condition. I do not count it as an expansion of the excluded word set
or a new published-record bound. Wide cycles remain open. The exact
spectrum criterion D dividing d follows in both directions from odd
scaling and is not an exhaustive numerical solution of the exponential
equation for fixed d.

I independently reviewed SIZE_PROBE.md. For coprime mechanical totals,
each adjacent phase changes exactly one nonzero-index summand. Its
positive increment exceeds `3^(m-1)/2`. The same bound on every term
gives the minimum estimate. The pigeonhole argument supplies small
errors of either sign; the transformation using floor(1/epsilon) turns
a lower approximation into a strictly upper one. Irrationality makes
both endpoints strict. Gcd reduction preserves sign and smallness, and
the reduced denominators m are unbounded. Thus every pair gap can grow
without bound. This does not produce unbounded gaps at a fixed d.

The [independent review](INDEPENDENT_REVIEW.md) audits the separate
lattice/geometric source and binds its final hash. Its last hash update
checks two prose-only changes by recovering the previously reviewed
source. The root's updates to SIZE_PROBE only replace stale forward
references with the completed companion result; its proof is unchanged.

## Code, data and source checks

I read the full checker, including its final gcd refinements and receipt
compaction. It recomputes coefficients independently from prefixes,
replays every actual and normalized raw arrow, and compares every
rotation with its exact state. The full cut-gcd formula and coefficients-
only gcd are exercised, rather than just their weaker divisibility
consequences. Scaling, primitive cycles and fixed points are separate.

The small matrix audit computes determinants by the Leibniz formula and
checks determinantal divisors. Its negative-D examples are algebra tests
using absolute determinants; positive cases also replay raw arrows.
The short-word audit checks both directions of the narrow equivalence,
with proper powers separated before testing g=1. The mechanical family
checks point and sorted-gap inequalities by integer products. It uses
exact binary bit lengths, not floating-point approximations to logs.

The author's final default replay and optimized/unknown-argument rejection
checks passed. The root then ran a fresh default replay, which recomputed
the full receipt and returned PASS. The receipt hashes every complete
normalized metrics row and retains explicit controls and counterexamples;
compaction does not skip their calculations.

The separate historical gate
`python3 scripts/verify_all.py --cpp --transfer-controls` completed with
PASS and 119 fields, including the independent C++ checks and eleven
raw cycle controls. It verifies preserved finite infrastructure, not
the new quantified theorem. Its exact output is [full_gate.json](full_gate.json).
The final [delivery checks](delivery_checks.json) bind source hashes,
local links and preservation. C001–C003, R1-onward ledger mathematics,
the dispatcher and the open LaTeX source remain unchanged.

Report review clarified that the positive-cycle Smith diagonal uses
D>0; the checker additionally tests negative-D algebra using |D|.
It also clarified that coprime totals follow for narrow primitive
cycles, not arbitrary cycles. These were current prose scope fixes,
not corrections to historical results.

The primary-source pass checked the Halbeisen–Hungerbühler paper and
Fernández–Ibáñez preprint at the scope recorded in SIZE_PROBE. Neither
is used to assume the new converse. The side lane's Lean reports remain
external reports without a new independent build replay in this batch.

## Decision

C004 supplies an intrinsic classification, a precise dependence
obstruction and a proved counterfamily to absolute proximity. It
does not complete the cycle headline. The next mechanism must retain
ordered-state information and cancellation across wider dyadic ranges;
none of the rejected shortcuts supplies that missing implication.
