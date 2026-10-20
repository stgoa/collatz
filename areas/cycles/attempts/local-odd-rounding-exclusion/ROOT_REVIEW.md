# C010 — Main review and completed runs

**Status: written arguments reviewed and finite checks PASS.** The main
agent authored GAP_LATTICE.md and the batch synthesis; review of that
note by its author is not independent review. The separate arithmetic,
rounding and checker agents reviewed it independently. Their signed
review notes identify their own authorship and execution scopes.

## Argument and control checks

The complete gap map has integer inverse `I+E+...+E^(m-1)` because
`E^m=2I`. It retains the seam, integer lattice and collective common
denominator. Under legal positive original valuations, integer scaled
coordinates force odd integer original states and their prescribed
lowbits. The zero-valuation affine loop is outside those hypotheses.
This is an exact reformulation, with no new integrality obstruction.

The sharp spacing argument distinguishes equal, increasing and decreasing
heights, and includes seam height -1. Its sum is a necessary inequality;
isolated-pair sharpness does not imply simultaneous attainability. The
q5 and q13 rational rescalings retain nontrivial denominators while
passing all displayed pair inequalities. The q83 example fails the
relaxation, confirming that the test has some discriminatory power.
The raw q7 control is retained outside the stated q<=L ordered domain.

The infinite family extends the persisted C004 phase construction.
The seam identity `2B_0-B_(m-1)=3^(m-1)` combines with the existing
interior monomial bounds and upper approximations to make every gap
arbitrarily large. The resulting local-spacing denominator lower bound
can tend to zero. This rejects this relaxation, including nonnegative
linear combinations of its pair inequalities; it does not reject
arbitrary global integer inequalities or all arithmetic methods.

The main agent inspected the complete final checker and its mechanical
extension. Its source pins, actual cycle parameters, primitive/scaled
distinctions, malformed-input controls and finite grid ranges agree
with the report. The final independent main replay completed with exit
code 0 in process 75349: `status=PASS`, `mode=replay`, with exact equality
to the saved receipt. The arithmetic and rounding reviewers also ran
separate final replays, documented in their review notes. Their own
finite calculations and the written universal arguments remain distinct.

## Historical verification

The full required gate `python3 scripts/verify_all.py --cpp --transfer-controls`
completed once with exit code 0 in process 16122. Its saved JSON has
status PASS and 119 fields, including the independent C++ and transfer
controls. The delivery checker separately checks that receipt, source
pins, local links, prior C001–C009 files, and the frozen result ledger,
LaTeX source and dispatcher. It checks preservation and consistency;
it does not replace the executed mathematical checks.

No historical mathematical error was found or corrected. The questioned
C006 seam recurrence was checked and retained. No formal Lean replay,
novelty determination, published-record improvement or new integer-cycle
exclusion is claimed. Ordered denominator-one exclusion, the all-cycle
headline and divergence remain open.
