# Pair-domain batch: external evidence and research decision

The remote review still finds only [PR1](https://github.com/stgoa/collatz/pull/1),
merged as `ba6b337`, already incorporated into main. At this review both
main and origin/main were `1603bf3`. The newer independent feed was read at
`dbb0dea5930ec667b70b5dfcbb595e5d566451b0`; that branch was left unchanged.
The [earlier review](../locally-collatz-like-control-barrier/PR1_REVIEW.md)
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

## Updated assessment after complete critical-nine elimination

A fresh remote review at main436f51f again found PR1 as the only merged
PR. It is already incorporated. The independent feed advanced to
`1a2dfc5710c5e17a4f42355a3dce2d6984b2b09b`, adding direct checks of R37–R39
and controls on their exact W domain. Its probe and both imported
dependencies were inspected and reproduced unmodified in temporary storage
under a60-second cap. The published receipt matched:16668 critical roots
and images,100000 odd interfaces,6250 coupled-recursion inputs, and the
three stated finite control counts. The [pinned reproduction receipt](side_lane_review_1a2dfc5.json)
retains all source hashes. The independent branch was left unchanged.

**Decision: focus on universal W5 construction and the exact dependencies
of its recursive rules.** R40 eliminates the whole W9 domain as an
independent premise. R41 distinguishes a complete decreasing W5 phase
from the exact returning branch, including P21→P9→P21. This is a genuine
scope reduction and a concrete failure of an attempted composition.
It is not a universal constructor. The merged audit's controls remain
useful; its stronger pessimistic claims do not invalidate these exact
reductions or show that other current constructions are impossible.

The same controls fail even on W5: examples include w5 for3x−1 and w133
for3x+61. Thus restricting the input domain does not remove the need for
specific3x+1 arithmetic in a universal argument. The finite checks and
independent model reviews do not provide a human review or novelty audit.

## Assessment with the common critical-image rank

The user's renewed merged-PR question prompted a fresh fetch and remote
PR listing at main4a45eb0. PR1, merged asba6b337, is still the only merged
PR returned and is already incorporated. The side feed has since advanced
to8c3f96f9b3da3df68ba49bfe2a5dfdd64e04abf1, adding finite R37/R40/R41 checks.
Those new receipts were read but not independently reproduced in this
batch and are not premises of its results. The side branch was unchanged.

**Decision: keep exact currents and pivot the induction to rho(w)=nu(3w).**
The rank theorem (legacy R43, `experiments/residual_progress/critical_rank/CRITICAL_IMAGE_RANK.md`, not yet migrated) explains why some
larger pair indices still make genuine progress. R44–R46 remove further
complete arithmetic domains and compose with R41 under this common rank.
The merged audit's controls remain mandatory tests of claims intended to
be generic. Its corrected minimality result does not prohibit these
constructions. Neither the new finite examples nor the external checks
establish universal coverage. The remaining obligation is explicit supply
or reduction of every unhandled W5 leaf, using arithmetic absent from the
control counterexamples.

## Forward/inverse assessment aftera06ef3c

The batch-start feed at3d69784a47790e5716d35a6a31b656aea0c73e79 adds
independent finite checks of R46 and three rank examples. Its exact probe,
normalizer dependency and unchanged control module were inspected and run
in temporary storage under a60-second cap. The published receipt matched:
33333 inverse-word cases and1112 complete small depth4 targets. The
pinned reproduction (legacy `experiments/residual_progress/side_lane_review_3d69784.json`, not yet migrated) retains source hashes
and notes the header's untested2549 value; main verifies that value separately.
The probe does not independently reprove R43 composition or R44/R45 domains.
The external branch was unchanged.

The next constructive pivot keeps both directions available. R47 extends
inverse phases to nonselected multiples of3; R48 handles whole forward
blocks; R50 composes inverse stages through an intermediate increase.
R49 proves that inverse-only descent is not universally available even
at fixed absorbed critical inputs, while the same examples have short
forward resolutions. This is a concrete operation-set limitation, not an
argument against uniform inverse formulas where they work. The seven-rule
union still retains unhandled leaves, and no finite coverage figure is a
universal construction. Claude's controls and the corrected PR1 scope
continue to apply.

The latest user-requested remote refresh still finds only merged
[PR1](https://github.com/stgoa/collatz/pull/1), merge commit
`ba6b3371fabd7fcabebb442d7c89ea3ed5c02149`; main remains at `a06ef3c`
before this batch's delivery. Its original PR description retains the
overbroad C3 wording, so the corrected repository note and
[explicit review](../locally-collatz-like-control-barrier/PR1_REVIEW.md)
should govern interpretation. The later feed explicitly accepts that
correction.

The feed now points to `8bc27dfeeba7804d57964b68f6149eb1f6f6c247`.
Its new size survey measures the earlier four-rule dispatcher, using that
dispatcher's own predicates. The source and receipt were inspected but
not reproduced or used as mathematical premises. It neither measures
the new seven-rule union nor proves an asymptotic law. In our complete
bounded comparison on the same 1024 W5 inputs below8192, acceptance rises
from195 to442. These are conditional rule acceptances, not442 independently
closed proofs or a percentage of Collatz solved.

**Recommendation: retain the verified current framework and prioritize
eventual rank descent across forward blocks and combined comparisons.**
R49 rules out universal smaller-ancestor search; R50 shows how composing
before requesting inputs can cross an intermediate increase. The next
decisive obligation is a complete rule for the remaining returning and
nonselected inputs, or a proof that a broader comparison always reaches
smaller rank. Additional isolated families and improving sample acceptance
alone do not meet that obligation.
