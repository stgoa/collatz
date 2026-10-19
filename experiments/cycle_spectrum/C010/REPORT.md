# C010 — Exact gap lattices and the limit of local odd rounding

**Status: written necessary inequality, an exact lattice equivalence,
and finite and infinite obstructions to the proposed rounding mechanism.
No new denominator-one cycle exclusion is obtained. The original
all-cycle goal remains active.** C009 was progress: its completed
excursion audit selected this bounded next test.

## Mechanism tested

Retain the complete sorted gap system, all odd numerator constraints,
height labels and the dyadic seam. Try to turn exact integer rounding
into a global lower bound on the reduced denominator. All actual cycles
use raw positive odd-only arrows, without absorption at1.

The result identifies a useful necessary inequality and the precise
information lost when it replaces the full integer lattice.

## Written results

### 1. Complete gaps preserve the entire denominator obstruction

Let E shift sorted coordinates by one place and double the wrapped
coordinate. Since E^m=2I, the gap transformation U=E-I has the integer
inverse I+E+...+E^(m-1). Explicitly, the first state is the sum of all
gaps, and every other state adds the appropriate prefix sum.

The [lattice proof](GAP_LATTICE.md) shows that positivity, common
denominator and the complete integer lattice are retained exactly.
For ordered cycles the original operator2E^s-3I commutes with U;
the full gap equations therefore supply the same integrality condition.
Their scalar sum is just the original minimum-state arrow.

Under legal positive original valuations, integer gaps already force
the exact odd numerators, lowbits and actual heights. The
[independent lowbit argument](ROUNDING_PROBE.md) retains every premise.
The invalid affine loop4→13→5→4 illustrates why valuation zero must
remain excluded. Neither result rules out arbitrary integer cuts or
a future global argument.

### 2. Sharp odd-spacing bounds give a genuine diagnostic

For sorted heights H, let V be the sum of decreases of2^(-H) on
upward height transitions. Exact odd spacing and strict image order give

```
L >= R_q(H) = q V(H)/3 + Gamma_(q mod6)(H),
q [C_h/D - V(H)/3] >= Gamma_(q mod6)(H).
```

The [rounding proof](ODD_ROUNDING.md) gives every local coefficient,
including the seam, and preserves the true weighted intercept C_h.
This is valid at arbitrary periods and heights. It can reject some
candidate rational shapes: the q83 control gives the residue1 lower
bound q>=2407/545>4. It is not a universal q1 exclusion.

### 3. The relaxation fails with arbitrarily large slack

The actual q5 cycle19→31→49→19, divided by5, is an exact rational
cycle at additive parameter1. Its sorted normalized gaps are
11/10,13/10,7/5. They exceed the corresponding sharp bounds
1/2,1/2,1. Every circular pair bound and the odd-ceiled total also
pass. Its denominator remains5; it is not an integer counterexample.

The failure persists at unbounded periods. In the existing C004
mechanical construction, the complete seam is exactly
`(2B_0-B_(m-1))/D=3^(m-1)/D`. Together with the already proved
interior gap bounds and coprime upper approximations, this gives
primitive rational cycles with every complete gap larger than any
prescribed K. Their height profile is zero, so all displayed q1
circular spacing bounds are at most2. Every one passes with
arbitrarily large slack, while the reduced denominator remains D>1.
The resulting rounded denominator bound can tend to zero.

This extends C004's existing spacing obstruction to the complete seam
and the proposed integer-rounding relaxation. These mechanical cycles
are already known nonintegral; no new excluded word class is claimed.

## Evidence and scope

The [compact exact receipt](integer_gap_audit.json) checks all2,459
stored source cycles across333 parameters, all1,185 distinct normalized
cycles, source scaling, and all11 raw fixtures. The52 ordered cases
include the trivial q1 cycle and51 nonfixed cases.

- All474 adjacent gap equations and sharp actual-parameter bounds pass.
- All7,022 proper circular pair bounds pass at actual parameters.
- After rescaling to additive1,19 noninteger cycles still pass every
  circular pair inequality. This is failure of a relaxation, not new
  integer cycles or a denominator census.
- The summed bound passes31/52 cases; rounding that bound to the next
  odd integer still leaves28/52. These counts include the trivial case.
- Independent signed/rational grids exercise the unimodular inverse,
  common-denominator preservation and operator commutation. Four
  generated mechanical examples check the complete-seam formula with exact
  integer arithmetic. The universal family argument is written above.

Author runs, independent replays, proof reviews and historical
preservation are separated in [ARITHMETIC_REVIEW.md](ARITHMETIC_REVIEW.md),
[INDEPENDENT_REVIEW.md](INDEPENDENT_REVIEW.md),
[EXACT_CHECKER_REVIEW.md](EXACT_CHECKER_REVIEW.md), and
[ROOT_REVIEW.md](ROOT_REVIEW.md). The historical gate and
[delivery checks](delivery_checks.json) are separate receipts.
[Literature scope](LITERATURE.md) records primary sources and the
absence of a novelty, formal-verification or numerical-record claim.

## Decision and next mechanism

Retire exclusion by the displayed local spacing inequalities and their
nonnegative linear combinations. Adding exact lowbit checks after the
full legal integral system creates no independent condition. Preserve
the diagnostic bound, the complete lattice interface and the counterfamilies.

The next bounded mechanism will return to **cyclic word arithmetic**:
compare a positive valuation word with a nontrivial rotation, identify
the positions where they differ, and test whether sparse differences
force a useful bound on gcd(C_w,D_w). The test must allow arbitrary
block sizes, retain common-cycle/repetition exceptions and recover all
actual d5/7/13 controls. It must distinguish a uniform bound from C001's
already established fixed-block identities. No such new bound is claimed.

This changes the mechanism, not the completion criterion. Ordered q1
exclusion remains an open intermediate target; unrestricted integer
cycles remain the headline, and divergence is separate. Circular order
has not earned a presumption of being the decisive ingredient. A bounded
catalogue of additional spacing cases would not answer the present goal.

## High-level recommendation after the user's question

The next objective is an arithmetic law with a new consequence for
denominator-one cycles, uniform as period and height grow. Whole-word
cancellation is the object; sparse differences from a cyclic rotation
are the next bounded test. Success requires a structural exclusion
beyond the existing block and mechanical classes, with exact coverage
and exceptions. A new notation, another finite census or the original
condition D|C is not sufficient.

Demote ordered-cycle exclusion from the presumed route to an open
benchmark. Its conditional payoff remains: C005 and a complete ordered
q1 exclusion would force H>8L for every nontrivial integer cycle.
C006–C010 do not prove that exclusion, and C010 gives a concrete reason
to change mechanism. Restore priority only when a new arithmetic
ingredient actually addresses the missing integrality step. Reject
attempts that become vacuous at q1, assume an unproved complexity bound,
or merely extend a fixed-motif catalogue without uniform gain.

Fable's parallel Lean work is valuable for checking stable statements
and exposing hidden premises. Its latest reported gap and run theorems
cover parts of C006; they do not supply the next structural exclusion.
Main has not independently replayed those builds. This is strategic
advice within the active all-cycle goal, not a replacement goal.
