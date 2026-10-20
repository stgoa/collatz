# C013 — Root integration and proof review

**Outcome: progress under the active cycle-spectrum goal.** No claim of
full cycle exclusion, unrestricted mismatch growth, novelty or formal
verification is made. This review is separate from the proof authors,
the independent cross-reviews, the exact finite checker and external
Lean reports.

## Reviewed proof versions

| File | SHA-256 |
| --- | --- |
| OVERLAP_CONTROLS.md | 66d6b4eee55410ceee5b8da2e3b509f6ac29f37f8e0993aa0534e2ef17688ec8 |
| OVERLAP_THEORY.md | 43c44f9ef6a2d9f42b1ce956a70d69db5f7c5b9582baf81b87c554aadb0605f9 |
| check_overlap.py | 911b5adf0688c4e5954f95b3439902db221f118ead0ca7ce45ed7a5d793d84d5 |
| overlap_audit.json | 21a5f84c35f8b15ebcbf88597ac50bf2fa68ed719750c079c915ec359fc2ec75 |

## Positive theorem

Root independently derived the Fourier pair coefficient and the
support bound `s*binom(e,2)>=r`, including cancellation of the diagonal
frequency pairs. The coefficient counts unordered distinct pairs;
using e or e squared without that derivation would change the bound.
Zero-distance rotations are explicitly excluded.

The exact homogeneous extraction preserves signs and the remaining
gcd with E. The resultant divisibility is valid after clearing powers
of u because the residual divisor is coprime to u. Polynomial
coprimality alone does not imply numerical coprimality. The actual q5
period17 control exercises precisely this distinction.

Root supplied and checked the uniform resultant bound using separation
of the roots of `X^r-2^T`, then checked the strict denominator inequality
and both stages of effective finiteness. The background prefix bound
uses every remaining positive valuation; it also remains correct for
empty U. In the large-total branch, bounding n must be followed by
bounding A_U using the sharper inequality. The proof does both.

The q1 consequence requires nonconstant markers as well as a nontrivial
primitive cycle. Cross-review found that section4 should repeat this
local premise explicitly; the author added it before freezing the
proof. No formula or historical theorem changed. The README, ledger
and report retain that restriction. The asymptotic concerns the count
r of shared-background blocks with T<=H_mark*r. It is not a theorem
about the unrestricted rotation mismatch count s.

Final integration review also corrected the report's phrase "remaining
polynomial gcd" to the numerical gcd of the homogeneous evaluations:
the residual polynomials are already coprime. The proof and checker
always used the numerical gcd. README wording now states minimum
rotation distance three, without suggesting every rotation has that
distance. These were summary clarifications before delivery.

## Height obstruction

The paired differences in a primitive cycle are nonzero even integers.
This supplies the extra factor2 at both run endpoints. The strict
minimum conversion uses `H/L<2^(B+1)` and therefore retains B.

Root checked the marker/run affine composition, the minimum immediately
after a marker, the limiting constants 5/6 and2, and the balanced
rescaling of upper convergents. A finite two-run may increase toward1;
the minimum argument remains valid because the whole U block increases
its input and the first run is increasing. No unproved uniform bound
on continued-fraction coefficients is used.

The near-critical family has linear normalized minimum and linear
dyadic height at distance3, but q grows exponentially. It refutes the
stated generic height conversions and supplies no counterexample at
fixed q. The separate independent review reconstructs its three exact
finite instances. Those instances do not establish the limiting claim.

## Code and source scope

Root read the complete checker, including primitive polynomial
pseudo-remainders, exact quotient checks, homogeneous evaluation,
integer resultant, all maximal agreeing runs, actual raw/scaled
cycles, and negative/repetition controls. Primitive normalization in
the polynomial remainder algorithm preserves the rational gcd; exact
division and a coprime residual check separately verify the result.
All1,185 actual polynomial gcds are computed; the earlier exploratory
limit at m32 is not the final receipt's coverage.

The four long-background controls have a certified lower bound greater
than one, so they exercise the quantitative inequality beyond an
empty-background identity. By contrast all243 structured passes of
the unrestricted candidate are already implied by observed q and m/s.
They are explicitly nondiscriminating, and that search was stopped.

The author performed --write with immediate JSON roundtrip comparison.
A different agent performed the saved-receipt replay and source review;
see [INDEPENDENT_CHECKER_REVIEW](INDEPENDENT_CHECKER_REVIEW.md). Root
does not claim a third independent full execution. The historical
finite gate was run once with C++ and transfer controls, completed
successfully, and is checked by the delivery verifier.

Root inspected the primary Matveev statement directly. It is already
in product-minus-one form, so the side feed's suggested log(2)
conversion is unnecessary for the cited version. The analytic theorem
remains imported. Fable's reported C010 Lean result was read as external
evidence, without a fresh main-side kernel replay.

## Delivery scope

The completed batch updates the eight programme index/log/instruction
files and adds C013 proof, code and evidence. The delivery verifier
checks byte identity of all earlier cycle files, the frozen R ledger,
the seventeen-family dispatcher and the open LaTeX source. No side
branch or attached Library file is edited. The commit and push are
authorized by the user's standing repository instructions.

The high-level recommendation is unchanged: seek a growing structural
restriction on every hypothetical integer cycle, within the all-cycle
headline. The next bounded attempt should charge numerical gcd terms
for distinct compatible shared arcs. C013 is a proved common-background
case and a height obstruction; it is not completion of that programme.
