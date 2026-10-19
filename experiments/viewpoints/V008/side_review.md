# V008 — External scope notes and direction D8

**Reviewed pin:** `b567f2bfc9ec581d42bbd35c5231324f7865a01e`, fetched
from `origin/claude/sidekick` on 2026-10-18. DIRECTIONS and the newest FEED
entries were read using `git show`. The branch remained read-only input.

## Dependency clarification accepted

The feed correctly identifies an under-explicit dependency in the brief
descriptions of V005–V007. Their Collatz constancy applications use V004,
which imports the published Cobham theorem. The source proofs already
invoke V004; there is no mathematical contradiction or newly discovered
missing theorem. However readers of a standalone report or ledger line
should see the inherited classical input.

This batch adds dated dependency clarifications to those proof/report
headers, the corresponding reviews and the result ledger. The distinction is:

- V005's affine reconstruction is elementary; its constancy consequence
  uses Cobham through V004.
- V006's mixed-state distinctness with explicitly non-eventually-periodic
  F is elementary. Removing the eventually periodic case for a nonconstant
  invariant uses V005/V004 and hence Cobham.
- V007's generic separator theorem under infinitude in both bases is
  elementary. Obtaining that infinitude from Collatz invariance uses
  V005/V004 and hence Cobham.

An ordinary written proof may import a published theorem. This does not
mean the imported theorem has been independently formalized in our Lean
assembly. That assembly's explicit Cobham input and independent-replay
status remain separate, as recorded previously. No new Lean replay was
performed in this batch. The new V008 first-shell theorem has a direct
constant-output finish and does not need Cobham.

## D8 assessment

**Part 1 — accept as a diagnostic, without changing success.** A fixed
epsilon>0 giving `kappa_h(D)>=(1+epsilon)(D+1)` infinitely often for every
nonconstant invariant would demonstrate a universal rate gain. It is
useful to report explicitly whether a batch achieves that. V008 does not.
It is not literally the smallest possible strengthening: an unbounded
additive excess would also strengthen the generic bound while falling
short of this fractional gain. Neither diagnostic replaces the active
unbounded-ratio objective.

**Part 2 — reject automatic abandonment of the active goal.** The user's
current continuation requires preserving the full objective. A fixed
two-batch deadline cannot end that goal or substitute a new language
survey. The useful methodological point is accepted: do not proceed
through an endless list of fixed separator widths. In fact V008 already
refutes the generic two-exit extension, so future work must use the global
growth bound or additional Collatz structure. Bounded comparisons of
different mechanisms for the same objective remain appropriate.

**Transfer assessment.** No general d-uniform growth theorem for
nonperiodic invariants is adopted. The side lane's finite samples and
suggested analogues do not prove it. The full statement for all
nonconstant invariants is false at d=5 and61 because of their periodic
divisibility colorings. The narrower nonperiodic variant is a different
scope. The current goal is a complexity restriction and would still not
prove convergence on its own.

## Earlier directions

D1/D2/D5/D7 remain retained with their existing scope; D3 remains rejected,
D4 deferred and D6 historical. The refreshed D7 status distinguishes the
reported comparator checks from unresolved whole-library checks. This
batch does not alter the accepted external replay receipt or import a new
analytic estimate. These proposals and reports are research input, not
instructions controlling the main lane.
