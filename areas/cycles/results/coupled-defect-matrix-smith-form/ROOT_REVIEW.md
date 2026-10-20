# C012 — Root review and verification scope

## Written proof review

Root independently checked the complete block convention, cyclic matrix
orientation, determinant identity, integer rank-two decomposition modulo
D and local Smith argument in `COUPLED_SYSTEM.md`, SHA-256
`c71362d09e2480971fd473f902f47387d2c31a482852d3f6d964d6d9ad9c46c2`.
In the sharp case, distinct left **and** right kernels are needed to
get rank exactly two; the invertible beta-difference matrix supplies
both. The three-minor bound and total determinant valuation then force
all remaining local invariant factors to have valuation v_p(D).

The all-size family has the stated totals and unique longest two-run.
Selecting t in the common multiplicative orders modulo any M0 coprime
to6 forces each constant-run intercept and D to vanish modulo M0.
This proves arbitrary cancellation divisors at fixed r without claiming
small reduced denominators or refuting a relative estimate.

Root independently checked `COUPLED_OBSTRUCTIONS.md`, SHA-256
`c9bfcf8fec24a56084a6e93230fdededec621ebc882cf422e570dd29a65ce9f3`.
Unique markers prove both primitivity and minimum rotation distance3.
The fixed-length/fixed-total intercept injection correctly recovers
the last valuation from the total, since the intercept omits it.
The finite-generator expression count is polynomial only with all
stated coefficient, arity and exponent-height bounds retained.

Root requested the strengthened counting family with t ones and2t
twos, markers3/4/5, m=9t+3 and A=15t+12. It has D>0 and A<2m for
t>=3. This matters: the first marker family lies outside the necessary
total range of a nontrivial integer cycle. The final note explicitly
separates those families. Neither family proves integer-cycle existence.

The common-background calibration is also correct. At the stated cut,
all three block intercepts equal E, and the polynomial reductions give
gcd(D,S)|23. It illustrates why failure to compress each separate arc
does not exclude correlated arithmetic. It is not a new unrestricted
denominator estimate. No novelty or formal-verification conclusion is
drawn from these written arguments.

## Errors found and corrections

1. The exploratory shared-arc formula initially used 3^(n+1). Root
   corrected it to3^n; the specified residue becomes1, not3. The
   incorrect draft was never stored as a theorem. The exact checker
   exercises the corrected identity.
2. The first default independent coupled-checker replay completed its
   arithmetic but failed receipt equality. Integer dictionary keys and
   tuple fields had different types after JSON reload. The author was
   asked to normalize those fields and regenerate the receipt, followed
   by another independent replay. The final outcome and hashes are in
   [INDEPENDENT_CHECKER_REVIEW.md](INDEPENDENT_CHECKER_REVIEW.md).
3. A shared-checker replay during author edits likewise detected a stale
   dependency hash. It is a staging mismatch, not a passed replay; the
   final matching replay is recorded in the theory review.
4. Final summary review caught two scope omissions. The README now
   says C011 excludes denominator one, preserving generalized cycles.
   The report's exact two-congruence statement now explicitly repeats
   the unit-amplitude and g>1 hypotheses. The conditional growing bound
   states A<2m and the natural-log convention. Neither written proof
   required correction for these summary clarifications.

These corrections do not alter C001–C011 or the historical R-ledger.

## Verification

The full historical command `python3 scripts/verify_all.py --cpp
--transfer-controls` ran once in session79576, completed with exit0,
and wrote the saved119-field PASS receipt. It was not restarted because
of silence. This checks historical infrastructure; it is not a proof
of the new all-size theorems.

The coupled checker is author-run and separately replayed as documented
in its independent review. Its all-cut counters refer to the selected
block starts; the written recurrence supplies equivalence for matching
internal cuts. Selected determinants use independent integer arithmetic,
and prime-power checks have explicit finite scope. The global candidate
estimate remains unproved, with no discriminating finite success.

Root authored and ran the separate shared-arc checker. Another agent
reviewed and replayed it; see [INDEPENDENT_THEORY_REVIEW.md](INDEPENDENT_THEORY_REVIEW.md).
It checks3,932 backgrounds, seven prime-set cases,177,288 raw arrows
and173,349 rotations. No counting theorem is inferred from these counts.

[EXACT_REVIEW.md](EXACT_REVIEW.md) separately records review of both
proofs by the coupled-checker author. No latest Lean build was replayed
by main. The [delivery check](delivery_checks.json) verifies final pins,
local links,147 unchanged previous cycle files, the frozen ledger and
dispatcher, and the unchanged open TeX.

## Decision

Persist the exact failures and retire the two specified shortcuts.
Retain a growing rotation-distance law as a proposed intermediate
objective, with actual shared-word correlations as the next missing
ingredient. No goal replacement or completion is justified by C012.
