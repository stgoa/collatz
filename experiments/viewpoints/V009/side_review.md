# V009 — Read-only side-lane assessment

**Reviewed commit:** `d0354c295774dc9e3ead1583aecddcfa299f96a6`, fetched
from `origin/claude/sidekick` on 2026-10-18. Main also fetched origin/main;
the main baseline for this batch was `9d66b69b1e9dc9413e73a0ff569972fd38feade7`.
The current DIRECTIONS and newest FEED entries were read with `git show`.
Neither side branch was edited, committed to, or pushed.

## New formalization report

The newest feed entry reports a Lean derivation of the periodic invariant
classification for every odd additive parameter, including multiples of3,
at lean-lane commit `79e8a69`. It reports statement and source-receipt
checks, standard axioms, and no native-decide use. The stated results
include reduction of a period to the appropriate divisor of d, a residue
class description, its converse, and eventual-periodic variants.

This is an external verification report. Main has not independently built
or replayed that source in this batch. The report is useful support for
the existing mathematical foundation; it supplies neither a quantitative
section-growth theorem nor the delayed nonzero combinations needed by
V009. No new generalized-map theorem is adopted as a premise here.
The V004 assembly's named Cobham input remains separate from the
elementary periodic classification and from replay status.

## Direction decisions

- **D8 fixed-epsilon rate gain:** retain as a diagnostic. V009 proves
  an unbounded additive excess for every nonconstant invariant. This is
  an improvement beyond the generic bound and meets D8's alternative
  request for another such improvement, but does not give a fixed
  positive fractional gain. The separate detection theorem constrains
  every proposed linear coefficient. The full ratio remains required.
- **D8 automatic two-batch abandonment:** retain V008's rejection. The
  user explicitly renewed the full objective. Method comparison continues;
  an external management proposal cannot replace the goal.
- **D8 concern about successive separator sizes:** accepted and acted
  upon. The main V009 argument uses the global cumulative count. The
  binary-ray probe is explicitly a narrower diagnostic and does not
  become the completion condition.
- **D8 suggested d-uniformity:** not adopted as a theorem. The generic
  affine detection result applies to any sequence, while its proposed
  Collatz application still lacks the necessary delayed combinations.
  Periodic d5/d61 invariants remain valid controls.
- **D1/D2/D5/D7:** retained with existing scope. **D3:** rejected as too
  broad. **D4:** deferred. **D6:** historical. D7's reported comparator
  and unresolved whole-library checks remain distinct; this batch adds
  no formal replay claim or analytic premise.

The earlier V005–V007 dependency clarification remains in force: their
Collatz constancy applications import Cobham through V004. The new
generic affine theorem is elementary; the binary-tail application uses
the existing two-base infinitude result and inherits that classical input.
