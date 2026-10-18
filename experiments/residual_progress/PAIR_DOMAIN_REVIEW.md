# Pair-domain batch: external evidence and research decision

The remote review still finds only [PR1](https://github.com/stgoa/collatz/pull/1),
merged as `ba6b337`, already incorporated into main. At this review both
main and origin/main were `1603bf3`. The newer independent feed was read at
`dbb0dea5930ec667b70b5dfcbb595e5d566451b0`; that branch was left unchanged.
The [earlier review](../../collatz_research_20261017/negative_controls/PR1_REVIEW.md)
retains its negative controls and the cycle-qualified minimality lemma,
with explicit counterexamples to the stronger uniqueness wording.

## What was reproduced

The exact pinned `pair_merge_controls.py` and `batch_r33_r36_check.py`,
their two imported dependencies, and their published receipts were
inspected and materialized in temporary storage. Both unmodified probes
ran under a 60-second subprocess cap and reproduced their receipts exactly.
The [review receipt](pair_domain_external_review.json) retains source
hashes, results and four independently reconstructed finite control paths.

The control maps have tripling pairs whose endpoints enter different
components: one reaches an absorbing state, the other a nonabsorbing cycle.
The indicator of the latter cycle's basin pairs nontrivially with
`delta_(3w)-delta_w` and has zero defect on all unkilled arrows. Thus no
finite exact current exists for these control pairs. This is a rigorous
test against a proposed generic argument; it does not refute the d=1 claim.
The saved paths, closing cycle arrows and invariant pairings can be checked
without external access:

```sh
python3 experiments/residual_progress/check_pair_domain_external.py
```

The controls absorb both1 andd when d>1. Literal common-future language must
either identify those absorbers or distinguish absorption from an actual
shared state. The R33 probe uses three finite bands and200000 random100-bit
inputs; the feed's larger two-million-sample table was not reproduced.
R35 also needs tripling pairs beyond3 modulo8, so the control script's
introductory domain description is incomplete. These scope corrections
do not alter the reproduced arithmetic.

## Decision

Retain exact currents and shrinking comparisons. Focus on a complete
sufficient domain and on arithmetic that distinguishes d=1 from the controls.
The current batch's critical-domain proof gives that domain explicitly;
the odd-pair reduction and the coupled even-pair construction explain how
existing rules can reach or extend it. These are written reductions and
partial constructions. They do not supply every missing current.

The main open task is a terminating construction on the whole critical
domain. More isolated mergers, an improved sample percentage, or a formal
descent that assumes the missing pair current do not settle it. The external
checks support this sharper progress test; they do not show that all
structural current constructions are exhausted. No external finding is
used as an unverified premise in the new mathematical proofs.
