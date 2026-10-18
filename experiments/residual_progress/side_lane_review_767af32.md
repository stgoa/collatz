# Parallel-work review and research decision, 18 October 2026

**Status: remote-state check, review of existing proofs, and strategic
decision.** No new external theorem or acceptance-rate claim is imported.

## What was merged

A fresh remote fetch and GitHub merged-PR listing identify only
[PR1](https://github.com/stgoa/collatz/pull/1), merged on 17 October at
21:30:44 UTC, commit `ba6b3371fabd7fcabebb442d7c89ea3ed5c02149`.
Both local and remote main were at `7206f9c` when checked. PR1 and the
subsequent scope corrections are already incorporated. There was no new
main-branch change to merge into the current research batch.

The newer parallel findings are on the separate `claude/sidekick` branch,
reviewed at `767af32b377fe48f447ab76941ae6727c6999374`. Its latest entries
report an independent finite R57 check and a random sample of the existing
twelve-family dispatcher. Those two new probes were read, not rerun here.
Their finite percentages are neither proof premises nor global coverage
theorems. The branch was not modified.

## Mathematical assessment

The merged negative controls remain useful. Early compression and large
finite reductions also occur for `3x+61`, which has certified nonabsorbing
cycles. A universal progress argument must use arithmetic or hypotheses
that separate the actual Collatz case from that control.

The conditional minimality lemma remains valid with its finite-current
and cycle hypotheses. Its broader conclusion that alternative certificates
cannot help is unsupported. The existing
[PR review](../../collatz_research_20261017/negative_controls/PR1_REVIEW.md)
gives exact counterexamples, including 56 distinct one-sided minimum-cost
certificates on the actual required annulus A768. The review checker was
rerun in this batch and passed: positive cost53758 is retained after
removing row5. The displayed PR description still contains the older broad
wording; the repository records the corrected scope.

The newer seven-arrow inverse formula was already independently checked
in the [preceding pinned review](side_lane_review_bae3969.md). Its exact
domain is R56's first inverse class. It supports the forward/inverse
comparison approach but adds no distinct domain to that result. The feed
has withdrawn its unsupported positive-density inference about inverse
failure; no universal search limitation follows from its capped samples.

## Decision: prioritize a complete recursion

Retain signed-current comparisons, the common rho order, and the negative
controls. Shift the main success criterion from another isolated residue
family or a higher acceptance percentage to a theorem that handles the
whole unresolved recursion.

The present batch supplies concrete structure for that task:

- [R58](exact_absorption_bound/EXACT_ABSORPTION_BOUND.md) identifies the
  only way unchanged formal absorption can request a rank above its
  canonical seed. The exceptional request is unique and has coefficient+1.
- [R59](deferred_rank/DEFERRED_RANK.md) allows larger intermediate
  requests to be expanded under a fixed already-proved resolver before
  testing the original rank. Formal expansion terminates, but it can
  retain an unresolved request. Two complete domains now pass this test.
- [R60](cycle_inverse/CYCLE_INVERSE.md) gives an exact acceptance table
  for a maximal inverse-cycle word and its maximal valuation1 continuation.
  These words can cross arbitrary prescribed forward-growth depth on
  complete families.
- [R61](exit_continuation/ELEVEN_EXIT_CONTINUATION.md) proves that one
  natural continuation procedure returns the identical unfinished current
  on full families. Its limitation concerns that procedure and the old
  twelve rules; other comparisons remain available.

The next decisive obligation is to eliminate every retained high or
original request by a compatible further comparison, or prove a different
well-founded recursion covering them. First classify the remaining inputs
against the enlarged dispatcher; the old twelve-rule exclusion is not
automatically an exclusion from newer rules. Generic rewriting termination
alone does not prove success, and no finite acceptance percentage supplies
this missing step. Collatz and universal current supply remain open.
