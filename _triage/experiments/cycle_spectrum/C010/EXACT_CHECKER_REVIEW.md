# C010 — Exact checker and independent proof review

**Status: author run/replay PASS; separate mathematical notes independently
reviewed.** The author of this note wrote
[check_integer_gaps.py](check_integer_gaps.py), so its two executions are
author checks, not independent replay. The reviews below concern notes
written by other agents. A main or separate-agent replay must be identified
separately.

## Checker coverage and scope

The checker loads and source-pins the inspected C009 `certificate`,
`word_data`, and raw `step` helpers. It does not invoke C009's excursion
report. All 2,459 original source instances across 333 parameters retain
their exact raw arrows and scaling. The 1,184 distinct reduced cycles plus
the C007 addition give 1,185 normalized cycles and 28,831 distinct-cycle
arrows. All eleven raw fixtures are retained.

For every normalized cycle, the checker independently constructs the
integer sorted vector `Z`, all gaps including the seam, and the explicit
integer inverse. It checks `gcd(G)=gcd(Z)=1`, actual lowbits and common
denominator preservation after division by `q`. These equalities do not
require circular successor order.

The ordered `q<=L` domain has 52 cycles, 51 nonfixed, with 474 arrows.
There the checker verifies the full state and gap equations, their
commutation, and the exact sum identity

```text
2 sum_(j<s) G_j - sum_j G_j = q 2^B,  s=A-m.
```

The fixed point is handled explicitly with `m=s=1`; its rank permutation
is the singleton permutation although the extended shift is one. Every
actual sharp adjacent bound and all 7,022 proper circular pair bounds
pass, including wrapped pairs with the correctly decreased target height.

Among additive-one rational rescalings, 20 of the 52 ordered examples
pass every adjacent bound and every circular pair bound; 19 of these
are nonintegral. The unrounded sum passes for 31, and the least-odd-integer
rounding of that sum passes for 28. These are counts of necessary-inequality
tests on rational controls, not counts of integer cycles.

The signed-vector grid checks 19,530 vectors in dimensions 1 through 6
with entries from -2 through 2, including zero and negative vectors.
It also checks 78,120 rational vectors, 131,835 operator commutations,
12 unit determinants for the gap map, and 46 coprime rank determinants.
The sharp local formula is checked independently at 1,428 triples of
parameter and pair heights. These bounded grids support exact written
identities; they are not universal proof substitutes.

The mechanical extension checks exactly four total pairs,
`(A,m)=(5,3),(8,5),(65,41),(485,306)`. These generate four known
mechanical shapes, independently recomputed from the source-pinned C004
phase formula; they are not a new cycle census. All 355 raw arrows,
95,351 phase summands, 351 interior gap monomials, and four exact seams
pass. The checker additionally tests 94,996 proper circular pair
inequalities on their additive-one rational rescalings. Three shapes
pass all pair bounds; `(5,3)` has two failing pair bounds. Every complete
gap satisfies the exact rational lower bound `3^(m-1)/(2D)`.

Author execution and receipt replay both exited zero. Frozen hashes:

| File | SHA-256 |
| --- | --- |
| `check_integer_gaps.py` | `87221a51c008668a8e36513096080cfc352ad16a86ba842976342a1c7deead78` |
| `integer_gap_audit.json` | `f26028a1d6c9f5f725e1d0bece4d1f3e44dc5dc895863c105433c9eed8d92d5c` |

## Independent review of odd rounding

I read [ODD_ROUNDING.md](ODD_ROUNDING.md), hash
`4647d1b51ddf73e1e6a5b5161414c5368d3c9098baa115cd61748c52132a59ac`.
The pair calculation retains the exact strict image inequality
`3r>q(2^k-1)` and odd `r`. The increments 2, 4, and 6 follow from
the required residue of `3r` modulo 6. The equal-height and descending
cases use different odd-spacing bounds, and the seam has destination
height -1. Summing all gaps gives `L`, with no missing boundary term.

The q5 control has rescaled minimum `19/5`, gaps
`(11/10,13/10,7/5)`, and parameter-one bounds `(1/2,1/2,1)`.
It also passes all proper circular pair inequalities and the odd-rounded
total 3. Its gap coordinates still have denominator 5. The q13 control
similarly survives. For q83, `V=3/4`, `Gamma_1=29/4`, and the bound
`2407/545` agrees with the displayed computation. No error found.

## Independent review of automatic lowbits

I read [ROUNDING_PROBE.md](ROUNDING_PROBE.md), hash
`62b9d2da833ce97fa1025e2bc22aafa6ee768c16e84c24044330beed8b76dbf2`.
The inverse `I+E+...+E^(m-1)` follows from `E^m=2I`, so the full gap
system retains the whole integer lattice. For legal positive valuations,
every rotated intercept and the cycle denominator are odd. Therefore
integer scaled states force integer odd unscaled states: multiplication
by powers of two cannot cancel an odd denominator. The lowbit conditions
then follow automatically, while positivity reconstructs the actual
height labels and distinct states. No independent lowbit obstruction is
left after the full legal integral system.

The excluded affine loop `(4,13,5)` is correctly kept separate. Its
valuation zero breaks the odd-intercept argument; the integral vector
`Z=(8,10,13)` satisfies the stated equations while its first lowbit is
8 rather than the assigned 2. This is a useful hypothesis control and
not an integer Collatz cycle. No error found.

This review establishes no formal verification, novelty, new excluded
integer-cycle class, or improvement over published cycle records.

## Independent review of the complete gap lattice and all-size control

I also read [GAP_LATTICE.md](GAP_LATTICE.md), including its appended
mechanical family. The integer inverse and positivity equivalence are
exact for the dyadic seam; all-common-denominator and gcd preservation
follow in both directions. The rank operator is unchanged by the
coordinate change because both operators are polynomials in `E`.
The scalar sum is the original minimum arrow, with the correct first
`s` gaps retained. The missing step in the short gcd explanation was
reported and clarified: a common odd divisor of all numerators also
divides `q` by every raw arrow, contradicting reduction.

The all-size extension correctly adds the seam identity
`2B_0-B_(m-1)=3^(m-1)` to C004's interior monomial formula. For
every nonzero phase summand, coprimality makes its exponent increase by
one from phase 0 to phase `m-1`; the constant summand stays fixed.
The complete gap lower bound therefore holds even at the seam. Along
coprime upper approximants with `epsilon=A-m log_2(3)` tending to
zero, it tends to infinity. Every proper circular pair difference
contains at least one complete gap, with positive dyadic factors on
wrapped terms, so all the parameter-one pairwise lower bounds can hold
with arbitrarily large slack. The summed odd bound `2m-1` also passes
once all gaps exceed 2.

This strengthens the finite counterexample to an infinite family of
obstructions to the specified lower-bound relaxation. It does not rule
out exact integer cutting planes, does not make the rational states
integer, and does not provide a new exclusion theorem for Collatz cycles.
No mathematical error found.
