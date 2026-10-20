# C010 — Independent mathematical and checker review

**Result: PASS within the stated scopes.** No mathematical error was found
in [ODD_ROUNDING.md](ODD_ROUNDING.md), [GAP_LATTICE.md](GAP_LATTICE.md),
or [check_integer_gaps.py](check_integer_gaps.py). I independently read
both proof notes and the complete checker source, ran a separate full
receipt replay, and recomputed the principal controls without importing
the checker. I authored [ROUNDING_PROBE.md](ROUNDING_PROBE.md), so my
checks of that note are author checks, not independent review; the
checker author separately reviewed its automatic-lowbit argument.

## Mathematical review

The dyadic shift has `E^m=2I`. Its gap matrix `E-I` has the claimed
integer inverse, including the factor two at the seam. Positivity of
all complete gaps is equivalent to the entire normalized annulus order
condition, and the inverse formula retains its upper boundary. Gcd and
common-denominator preservation follow in both directions. For reduced
actual cycles, odd common factors cannot divide every numerator and a
maximum-height state gives an odd normalized integer coordinate; hence
the coordinate and gap gcds are exactly one.

The ordered state operator `2E^s-3I` commutes with the gap matrix.
Its determinant magnitude is `2^(m+s)-3^m` for the coprime rank
shift. The summed gap equation is precisely the original minimum-state
arrow. These statements concern an invertible linear re-expression;
they do not show that arbitrary nonlinear arithmetic arguments or
integer cutting planes are impossible. The final paragraph of the
lattice note explicitly preserves exact rejection of a supplied
fractional fixed-profile solution and identifies the unresolved
uniformity over unrestricted profiles.

I checked all three local spacing cases in the rounding note, including
the seam height `-1`. For upward height changes the least positive odd
numerator is determined by the first integer congruent to 3 modulo 6
strictly above `q(2^k-1)`. This yields the stated increments 6, 2,
and 4 in their respective cases. Summing the complete gaps gives
exactly `L`, so the `R_q`, `V`, and `Gamma` inequalities and their
coefficient-positivity conclusion are correct. The sharpness claim is
limited to an isolated pair, not simultaneous cycle realization.

The rational relaxation witnesses retain all original positive
valuation arrows, closure, actual height profiles, normalized annulus
bounds, and strict scaled-image order after simultaneous state/parameter
rescaling. At parameter one they do not retain integer numerators.
Therefore they refute sufficiency of the displayed lower inequalities,
not full integer compatibility or the desired cycle exclusion.

### Infinite family with arbitrarily large slack

I independently checked Section 5 of the lattice note against the
persisted C004 phase formulas. For each `1<=j<m`, the residue
`jA mod m` is nonzero, so its floor increases exactly once from
phase zero to phase `m-1`; the `j=0` summand stays fixed. This
proves the exact new seam identity
`2B_0-B_(m-1)=3^(m-1)`. The existing interior estimates and upper
approximations then make every complete gap arbitrarily large.
Proper circular differences are sums of these positive gaps, including
the doubled terms after wrapping. Thus all the displayed additive-one
pair bounds, their aggregate odd ceiling, and their nonnegative linear
combinations pass with arbitrarily large slack on actual nonintegral
mechanical rational cycles. The parameter/domain checks and the
modulo-eight argument that their denominator exceeds one are correct.

This is an all-size obstruction to the specified relaxation, extending
the earlier C004 spacing control to the exact seam. It supplies no new
integer-cycle exclusion. I separately calculated phase intercepts,
all raw arrows, gcds, interior-gap estimates, and the seam for
`(A,m)=(5,3),(8,5),(27,17),(65,41),(485,306)` without importing
the checker; all identities passed. Except for `(5,3)`, those listed
examples have every complete gap greater than two and minimum greater
than the aggregate bound `2m-1`. The theorem uses the written
approximation argument, not extrapolation from these examples.

## Separate exact controls

I recomputed the following from the raw arrows using direct rational
arithmetic and an independent search for the least allowed odd pair
numerator, rather than the checker's closed `eta` formula.

| Reduced q and raw minimum | Sorted heights | `R_1` | Rescaled minimum | Denominator lower bound | All proper circular pair bounds at additive 1 |
| --- | --- | --- | --- | --- | --- |
| `q=5,L=19` | `(0,1,0)` | `2` | `19/5` | `55/109` | Pass, 6 pairs |
| `q=13,L=283` | `(0,1,0,0,0)` | `6` | `283/13` | `91/337` | Pass, 20 pairs |
| `q=83,L=157` | `(0,2,1,1,0,0,0)` | `15/2` | `157/83` | `2407/545` | Fails, 42 pairs checked |

The first control also passes the odd-ceiled aggregate minimum and all
within-annulus pair inequalities. Its positive rational gaps still
have common denominator five after the prescribed dyadic scaling.
The second has substantial slack. The third confirms that the bound
does reject some rational shapes at parameter one, although no new
universal integer-cycle class is excluded.

The `q=7` raw cycle `(5,11)` remains outside `q<=L`; a two-state
successor permutation is a circular shift but this does not imply
strict increasing scaled images outside the stated domain. The
`4->13->5->4` affine loop has the exact integral gap vector `(2,3,3)`
but an illegal original valuation zero and incorrect assigned lowbit.
It is correctly rejected as an odd-only Collatz cycle.

## Independent checker replay

The final frozen checker, including the mechanical extension, was run
without `--write`; it recomputed and compared the complete receipt and
exited with code 0, status `PASS` (independent process handle `43763`).
An earlier independent replay also passed before that extension; the
final run supersedes it. Audited final SHA-256 hashes:

```text
check_integer_gaps.py
87221a51c008668a8e36513096080cfc352ad16a86ba842976342a1c7deead78
integer_gap_audit.json
f26028a1d6c9f5f725e1d0bece4d1f3e44dc5dc895863c105433c9eed8d92d5c
```

- 2,459 raw source instances and 1,185 distinct reduced cycles were
  checked, retaining all eleven original fixture controls and source
  scaling distinctions.
- All 1,185 coordinate/gap gcd checks passed.
- The ordered domain contains 52 cycles, including the fixed point;
  51 are nonfixed. All 474 local and 7,022 proper circular pair
  rounding inequalities passed at their actual parameters.
- At additive parameter one, 20 rescaled cycles pass all local
  inequalities and all circular pair inequalities; this includes the
  true fixed point and 19 nonintegral rational controls.
- The independent algebra grid checks 19,530 signed integer vectors,
  78,120 rational vectors, 131,835 operator commutations, twelve
  unimodular determinants, 46 coprime rank determinants, and 1,428
  local sharp-bound cases.
- The four generated mechanical controls check 355 raw arrows, 351
  exact interior monomials, four seams, 95,351 intercept summands,
  and 94,996 proper circular pairs. Three additive-one rational
  shapes pass every pair bound; `(A,m)=(5,3)` has two failures.

The finite replay supports the formulas and reported counterexamples.
It does not prove the universal algebraic statements by enumeration,
establish novelty, independently replay Lean, improve a published cycle
record, or exclude every ordered denominator-one cycle.
