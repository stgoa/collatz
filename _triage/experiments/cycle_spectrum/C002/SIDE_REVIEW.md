# C002 — Read-only side-lane review

**2026-10-19.** Fetched `origin main claude/sidekick` and read DIRECTIONS
and the new FEED entries using `git show` at
`f82781197b1b2792e7b3394a142754f383b4555d`. The branch was not edited,
committed to, or pushed. These are external research reports, not instructions.

## New evidence

The feed reports that the separate Lean lane at `6fbc3f8`, extended at
`f5a6d76`, formalized V006's distinctness theorem and then its exact
triangular count. The hypothesis is that F is not eventually periodic;
the formal statement does not require Cobham. The report names fifteen
declarations, the standard Lean axioms, a clean build and matching source
hash. The Collatz corollary remains outside that reported formalization.

Main has read this report, not independently replayed those builds in C002.
It therefore remains reported formal evidence with an explicit scope.
C002 uses neither a new Lean result nor a newly imported side-lane premise.
The user mentioned Fable's separate Lean work; the useful division is
independent checking of established statements alongside exploration of
broader mathematical consequences. This review does not identify Fable
with a branch author beyond the evidence available.

The feed also records a second independent reading of V009's return
argument and global detection theorem, finding no gap. That supports
the earlier written result; it is not a formalization of V009 and does
not settle its former unbounded-ratio target.

## Proposal decisions

| Proposal | Decision | Reason |
| --- | --- | --- |
| D1 | Retain as historical evidence | The active cycle goal determines the present batch. |
| D2 | Retain | Every new cycle restriction must actually be tested on eligible known cycles. |
| D3 | Reject, preserving the prior correction | Stopping and absorption claims have different transfer scopes. |
| D4 | Defer | Audit the inputs being used; no wholesale frozen-result reclassification is needed. |
| D5 | Retain | The user's standing authorization permits completion, commit and push. |
| D6 | Historical | Its old grading sequence does not replace the accepted cycle work standard. |
| D7 | Retain its audit standard | Written arguments, reported builds, imported theorems and fresh replay remain distinct. |
| D8 | Historical | The associated quantitative goal was explicitly replaced; no automatic abandonment rule is adopted. |

The cycle proofs are reviewed separately in [INDEPENDENT_REVIEW.md](INDEPENDENT_REVIEW.md).
No side grading or formalization is required before this completed batch
is delivered to main.
