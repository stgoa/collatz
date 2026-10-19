# Parallel-work review: the original-rank stopping threshold

**Status: reviewed conditional argument and reproduced finite probes.**
Collatz and universal current supply remain open. This review imports no
new external theorem and makes no novelty claim.

## Remote state and the merged PR

A fresh fetch and GitHub merged-PR listing on 18 October 2026 still show
[PR1](https://github.com/stgoa/collatz/pull/1) as the only merged PR. Its
merge commit is `ba6b3371fabd7fcabebb442d7c89ea3ed5c02149`; it and the
subsequent scope corrections are already ancestors of main `793e835`.
There was no additional main-branch change to integrate.

The separate side branch advanced to
`33c3829702fe35d0b112a3abdd5255c95b7e6b00`. Its two latest entries concern
the original-rank stopping threshold and R62 compatibility. The branch was
read without modification. The merged negative controls remain useful;
the [existing PR review](../packet_currents/negative_controls/PR1_REVIEW.md)
retains the exact counterexamples to the broad claim that alternative
minimum-cost one-sided certificates cannot help.

## The stopping-threshold argument is correct, conditional on reaching it

For `w in W5`, put `q=rho(w)=nu(3w)` and `z=nu(w)`. Suppose an actual
finite quotient prefix reaches `x=T^k(q)` satisfying

    9x+5 < 8q.                                             (1)

Let `B_i` be the exact quotient bridge at `T^i(q)`, and write
`div H_s=[s]-sum A_s(u)P(u)`. Then the full current

    J=N_(3w)+sum_(i<k) B_i+H_x-N_w-H_z

has the exact boundary

    div J=P(w)-sum_u (A_x(u)-A_z(u))P(u).                   (2)

R43 bounds every request in `H_x` by `(9x+5)/8<q`. Equivalently,
R51's sigma bound combined with R62's compatibility identity gives this
same inequality. For the lower partner, `z< w/4` and `q>w`, so
`(9z+5)/8<q` for every `w>=5`. Thus every nonzero signed request in (2)
has strictly smaller original rho, including after equal terms cancel.
The first hitting time is optional: any supplied prefix satisfying (1)
has this property. Its length and all intermediate heights may be large.

Universal finite hitting of (1) would therefore supply all W5 currents by
strong induction on rho, and R40 would imply Collatz. Conversely Collatz
implies that every quotient orbit reaches 1, which satisfies (1) because
`q>=7`. This is a correct equivalent stopping-time formulation. It does
not establish universal finite hitting. Logical equivalence also does not
show that every useful signed-current construction must trace this
particular prefix, or rule out a different proof of the sufficient premise.

## Independent reproduction

Both external probes and their helper were inspected, then run unchanged
in temporary storage against all Python sources from pinned main
`793e8357dabe251941bfbddd5af3d2471c07ee66`. Each subprocess had a 90-second
wall-clock cap; neither hit it. Both generated receipts agree with the
external JSON exactly. Hashes, pinned revisions and full returned data are
in the [reproduction receipt](side_lane_review_33c3829.json).

- The stopping-prefix probe validates 3,600 complete signed plans,
  1,200 each at 24, 40 and 64 bits. The largest observed quotient prefix
  has 79 arrows. These sampled lengths do not bound other inputs.
- The compatibility probe checks 20,000 returning-index identities and
  3,000 complete sigma plans. All 159 returning-parent plans are
  rho-valid. Among 2,841 other parents, the five failed rho tests have
  exactly R62's predicted returning requests in its offending interval.

The earlier closure meter was read, not rerun in this batch. Its sample
percentages and the two new probes are finite evidence, not integer-density
theorems or premises in the written argument above.

## Research decision

Continue the focused pivot toward a complete recursion with one coherent
progress argument. Keep the negative controls, exact signed currents and
the distinction between a terminating computation and a supplied current.
The sharper threshold is a useful correctness test for forward plans; its
unproved hitting assertion is the central difficulty in another form.

This batch tests whole mechanisms rather than another finite acceptance
rate: the complete ray-index/height tradeoff for two prescribed inverse
rotations, repeated growth under actual mixed-rank choices, and inverse
versus forward comparison at the adjacent source's original native height.
Their scoped conclusions determine which proposed mechanisms need to
change. None supplies a universal recursion or justifies abandoning all
other current constructions.
