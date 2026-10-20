# Side-lane review at 86ead16: useful verification, with a narrower search target

**Status: reproduced finite probes and a scoped strategic assessment.**
Reviewed `86ead16d88bce7d1f9ed3562a806b9ae39c5c631` of `claude/sidekick`,
dated 18 October2026. Main baseline was
`b2731dd1843c58d119c0d39b14b4e63cf5f644da`. The remote PR refresh still
identifies [PR1](https://github.com/stgoa/collatz/pull/1), merge
`ba6b3371fabd7fcabebb442d7c89ea3ed5c02149`, as the only merged PR;
that merge is already an ancestor of the baseline. The newer R90 checks
are side-feed work, not a newly merged PR.

## Reproduction

All listed side sources and their imports were materialized from the exact
commit into temporary storage. The branch and its working files were not
edited. Python probes ran unmodified with 60-second process caps; a cap would
have failed the review. The [receipt](side_lane_review_86ead16.json) records
file hashes, commands, outputs, timings and scope.

| Pinned probe | Reproduced result | Wall time |
|---|---|---:|
| `r90_phi_return_check.py` | 2,000 pairs of ordinary words; 500 quotient identities; 3,000 re-entry counts |0.143s|
| `batch_r61_r67_check.py` | R61: 132 cases; R65: 10,000 canonical values; R66: 2,990 pairs; R67: 3,000 counts |0.172s|
| `r64_lifted_cycle_check.py` |85 boundary representatives, none skipped |0.093s|
| `r88_anchor_exhaustive.c` |33,426,246 nonabsorbing canonical origins; exactly four expected hits |4.957s|

All three generated Python receipts are **byte-identical** to the pinned
receipts. R64 now explicitly requires 85 tests and zero skipped cells, fixing
the earlier vacuous-PASS risk identified in the
[previous review](../lifted-inverse-ray-cycle/side_lane_review_cbe77bc.md).

For R88, the independent C enumeration checks every canonical 3<=p<=133704987
for 22 quotient steps against four targets, accepting a hit on target a only
at depth d<=19+a. The four hits are all p=133704987, at depths 18,19,20,21
for a=0,1,2,3 respectively. This review explicitly required the full output,
including the origin count and all four hits; exit status alone would not
have rejected a run with missing expected hits. The omitted absorber 1 cannot
hit these targets. Overflow is excluded by

    x_j+1 <= (3/2)^j*(133704987+1), j<=22:

the right side is below 2^40, and even the intermediate3x+1 expressions are
below 2^42. The unsigned 64-bit implementation is therefore exact on this
enumeration. This is a complete fixed-anchor check, not the all-parameter
R88 lifting proof.

These probes check arithmetic paths and counts, not the full signed current
plans, supplied terminal inputs, or universal termination. R90 counts complete
returns whose images remain in the guard. The older R67 count includes the
last guarded step whose image may leave, hence its extra 1; the two conventions
must remain distinct. The feed's informal descriptions of how many seeds
were forced deep are not used as coverage claims: the source generators and
receipt totals specify the actual sampling.

**R91 was not reproduced by the side lane.** Its feed says this explicitly.
The 33.4-million-state R88 scan is a different computation from R91's
1,732,883 rational-origin classification. This focused review also did not
rerun that latter classification. Its universal inverse-word conclusion rests
on the [written finite reduction and complete classification](../rational-basin-precision-barrier/README.md),
not on the new side samples.

## What the merged PR establishes

The certificate-minimality proof remains sound with both premises: a finite
exact comparison current J0, and no nonabsorbing cycle in the difference
support. Negative entries in a putative difference force negative predecessors
and hence a forbidden finite cycle. This gives pointwise domination and a
positive-cost lower bound; it does not give uniqueness of one-sided
certificates or prescribe their discovery method.

The concrete correction was independently replayed again:

    python3 experiments/packet_currents/negative_controls/check_review_scope.py

It passed in 0.36s. For source[21]-[3], both J0=delta21-delta3-delta5 and
J=delta21-delta3 with residual-[5] have minimum positive cost 1. For actual
A_768, removing the negative row J0(5)=-55 preserves minimum positive
cost 53758 and removes one of 40106 current rows. Thus the original broad
claim that alternative certificates cannot help is false; the
[persisted PR review](../locally-collatz-like-control-barrier/PR1_REVIEW.md)
and corrected handoff already acknowledge this.

The negative control is substantive. A separate bounded reconstruction
checked the 87 positive odd seeds below 175 for 3x+61, the 41-cycle entered
by 175, and all packet pairings for 8<=N<=213. The first positive pairing is
1 at 213, while the earlier pairings are nonpositive. Therefore compression,
small-base success and early apparent progress alone cannot prove the
universal criterion. This does not prohibit finite certificates coupled to
a proved finite reduction: R91 has precisely that different logical form.

## Strategic assessment at R90/R91

**Keep the exact-current formulation and change the immediate search target.**
The controls argue against treating additional acceptance percentages or
one-pass contraction as a termination mechanism. Minimality supplies no
reason to abandon structural or one-sided constructions.

R90's binary countdown only proves exit from its growing subsystem. Its
fresh forward continuation keeps every negative request below the original
rank, so merely extending that same history cannot create a negative high
term to cancel the remaining positive leader. R91 further excludes every
smaller original origin at the repeated target through 12r+5 quotient steps,
over all inverse rays. More search within that proved exclusion has no value.

The warranted next step is an input-dependent comparison using longer
histories beyond that precision, a later common target, or genuinely different
retained signed history. Its success criterion is a complete remaining family
with every signed premise below the **original** rank and a proved termination
or closure mechanism. At the start of this review the deeper-window draft
was pending. The subsequent independent [R92 proof and complete classification](../fourteen-step-window-original-source/README.md)
resolve that window: through12r+19 quotient steps, the only origin no larger
than Q is Q itself at12r+18. The side probes do not establish R92. The
synthesis's broad phrase that no fixed procedure finishes
the job should likewise be read only with the named procedure and domain
restrictions of the actual obstruction theorems. Universal terminal supply
and Collatz remain open.
