# C011 — The next step requires coupled arithmetic

**Status: exact identity and actual-cycle counterexamples to a proposed
extension.** No growing-defect bound or unrestricted q1 exclusion is
proved. Raw positive odd-only cycles are used throughout.

## Exact identity at arbitrary mismatch count

Let w and v be cyclic rotations with prefix totals P_j and P'_j.
For every positive word,

```
C_v-C_w = sum_(j=0)^(m-1) 3^(m-1-j)(2^P'_j-2^P_j).       (1)
```

The prefix discrepancy `P'_j-P_j` is constant between positions at
which the valuations differ. Group (1) into its maximal nonzero
constant-discrepancy intervals. A group with nonzero discrepancy delta
is `+/- 2^u 3^v (2^abs(delta)-1) C_arc`, with a positive arc
intercept. Negative discrepancies are represented by factoring out
the smaller power of two, so the terms remain integer.
The common cycle divisor g divides the full sum and the corresponding
sum at every cyclic cut.

With two mismatches, an appropriate cut leaves one nonzero interval.
That isolates `(2^k-1) C_arc` as divisible by g after removing powers
of 2 and 3. The factor `2^k-1` cannot be discarded; the arc alone
is automatically divisible only in the unit-amplitude case k=1.
For more mismatches, the same inference for each individual interval
is false, even if every summand is positive.

## Three actual controls

| Reduced q | Word | Rotation | g | Nonzero plateau contributions | Residues modulo g |
| --- | --- | --- | --- | --- | --- |
| 97 | (2,4,3) | 1 | 5 | 36,64 | 1,4 |
| 233 | (1,1,2,1,2,1,3,2) | 3 | 7 | 972,8352 | 6,1 |
| 359 | (1,1,2,3,1,1,2,4) | 1 | 73 | 972,3888,1536,14336 | 23,19,3,28 |

Every row has a total divisible by g and no plateau contribution
divisible by g. The respective mismatch counts are 3,4,6.
For q97 the actual cycle is `17 -> 37 -> 13 -> 17`, with
`C=85,D=485`. Its rotated intercept is 185, so the difference is
`100=36+64`. This supplies the smallest possible mismatch count
outside the two-defect theorem. Three mismatches are possible for
valuation alphabets with at least three letters.

[check_coupled_defects.py](check_coupled_defects.py) verifies every
prescribed arrow, primitive period, prefix plateau, residue and presence
in the stored actual-cycle corpus. The
[receipt](coupled_defect_controls.json) contains exact states and
source hashes. These controls refute only termwise divisibility,
not a bound using all coupled sums.

## Next bounded mechanism under the unchanged cycle goal

Combine the sums at all cyclic cuts of one rotation pair and determine
which integer eliminations isolate arc information without introducing
uncontrolled determinant factors. Retain the common divisor, signed
coefficients, and dependencies among cuts. C004 already showed that
ordinary rotation integrality conditions are one obstruction; merely
rewriting those equations as a matrix would not supply a new bound.

The desired intermediate result is one quantitative estimate valid for
an arbitrary mismatch count, with a useful consequence for every
hypothetical q1 cycle. An explicit lower bound on the minimum mismatch
count growing with period would qualify. It remains a target, not a
known consequence of C011 or a replacement for the all-cycle headline.
Three- and four-mismatch examples are diagnostics for that general
estimate. Excluding one fixed count after another is not the programme.

A bounded next pass should either produce a coupled estimate retaining
an exponential saving, or an exact family showing why the proposed
elimination loses it. In the latter event, compare another arithmetic
mechanism. Do not infer that all possible methods using rotations fail.
Fable's formalization of stable affine identities is useful verification
infrastructure; no reported Lean build supplies the missing estimate.

## Draft correction

Independent review caught an omitted `2^abs(delta)-1` factor in the
first draft's description of each plateau. It also corrected the
implied divisibility of the arc alone to divisibility of
`(2^k-1) C_arc`. The exact checker and main two-arc theorem already
retained these factors; their statements and evidence are unchanged.
