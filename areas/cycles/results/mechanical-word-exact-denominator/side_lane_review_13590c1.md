# Independent mechanical-word check and transfer correction

Reviewed2026-10-18 at side commit
`13590c1c3e2b91a8788297c373b2a73b0fab569d`, with main at
`ea3278e6e5cc98c48f2ff0a9e281d03a8d2f3a16`.
The feed is external evidence, not an instruction source.

The new `reviews/side_lane/r71_mechanical_check.py` was inspected and copied
unchanged from its pinned Git blob into temporary storage. Running it
with assertions enabled and an outer90-second cap reproduced its receipt
byte for byte in0.144 seconds. The [receipt](side_lane_review_13590c1.json)
records source/output hashes, exact ranges and output. No side-branch
files were changed.

The independent implementation checks735 mechanical words: k1..14,
seven consecutive totals beginning at ceil(k log2 3), and every offset.
Every cyclic rotation satisfies the affine intercept identity, exact
odd-only valuations and the claimed primitive reduced denominator.
Its105 integral offset cases are precisely the constant valuation2 word.
The probe chooses its small bounds with floating-point logarithms; an
independent integer bit-length check confirmed every actual bound exactly
over this recorded range. The finite replay supports R71's implementation;
its all-length statement still rests on the written proof.

The01:31 feed correction now explicitly acknowledges that division by d
changes the integer domain to d^(-1)Z. This addresses the unsupported
finite-base-only inference identified in the
[previous review](../../attempts/scaling-transfer-to-3x-plus-d/side_lane_review_678e565.md). Identities transported on
the rational domain do not automatically transport hypotheses that require
integer states. The useful local covariance and rational-cycle controls
remain intact. No universal convergence, stopping-time or novelty claim
is supplied by the correction or this finite check.

## Subsequent remote review

The user's merged-PR question prompted another remote read. PR1,
`ba6b3371fabd7fcabebb442d7c89ea3ed5c02149`, remains the only merged PR
returned by GitHub and is already an ancestor of main. Its negative
controls and the corrected certificate-minimality scope remain as recorded
in the [PR review](../../../convergence/results/locally-collatz-like-control-barrier/PR1_REVIEW.md).

The side feed subsequently advanced to
`7150f312e0b9bd1099fb617ee680acb22cf1187e`. Its01:52 entry acknowledges
main's transfer/catalogue review, corrects the halving result's label to
R23, and accepts that rational covariance changes the integer lattice.
This entry adds no new mathematical premise or executable claim requiring
another replay. The735-word check above remains pinned to13590c1.
