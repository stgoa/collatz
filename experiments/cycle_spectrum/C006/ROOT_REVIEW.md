# C006 — Root verification

## Written proof

The root reviewed the full gap argument and the generic extremal
comparison, separately from the author's finite checker. The proof source
reviewed is `ORDER_RIGIDITY.md`, SHA-256
`6c13342f0eba3ec13a869def8de5d4543d4b26f63afabc0794f9925c23658c70`.
The [independent review](INDEPENDENT_REVIEW.md) supplies another reading.

The critical checks are the dyadic seam, positivity and strict total-gap
bound, coprime rank shift, zero-run binary divisibility, the cases J=1
and J=m, and reduction from bounded period to finitely many rational
cycles. The count is for normalized rational cycles; arbitrary scaled
integer copies across unbounded parameters are not distinct objects in
this finiteness statement.

The analytic corollary uses exactly Bugeaud Theorem1.1(1.2), with inputs
2 and3, coefficients A and−m, degree1, and coefficient bound A<2m.
The original Matveev page was not successfully retrieved. The inspected
author statement and its mapping are recorded in [LITERATURE.md](LITERATURE.md).
No numerical constant, fresh formal replay or novelty is claimed.

The new report was also reviewed by the proof author. A wording change
replaced an ambiguous reference to a published bound with a classical
bound whose inspected statement is in an author preprint.

## Exact checker and the corrected receipt issue

The root inspected the independent checker, including direct affine
composition, exact valuations, primitive period, maximum-prefix
rotation, actual dyadic heights, circular rank recurrence and all
zero-forcing runs. The exact denominator diagnostic uses the run with
largest exponent sum; the longest run is retained separately for the
pigeonhole comparison.

The first author and root replays failed at saved-object comparison.
The isolated invalid affine control returned tuples, while its loaded
JSON receipt contained lists. All preceding arithmetic checks had
completed. The author changed those output fields and potential failure
rows to lists, regenerated the receipt, and started new replays. This
was a receipt-format correction, not a mathematical correction.

During the final mathematical review, the root found that the separate
height bound is redundant. Since each chronological height rise is at
most one, every label0..B occurs, forcing B+1<=J. This strengthens the
result to fixed-q,J finiteness and J>=sqrt(m)-O_q(log m). The proof author
and independent reviewer checked the deduction. The checker gained one
explicit assertion on the unchanged finite domain; a new write and
separate replays were required to test that new claim. No broader search
was added.

Final checker source hash:
`9ff33e44d2bfb08b46007c2b6859e4dd79842bc711f3a12f3bbfa45b83e4e961`.
Final exact receipt hash:
`6d12096dfd3f2b4940d0edc5f9d2ebf158db2a8f3d2b86a2d522087225625e88`.

The final independent replay outcome is recorded in
[root_replay.json](root_replay.json) and [delivery_checks.json](delivery_checks.json).
The final author replay and separate root replay both completed with
exit0 and PASS, at the hashes above. A completed PASS receipt, rather
than a running process, is the acceptance evidence.

## Finite coverage and what it means

| Check | Coverage |
| --- | --- |
| Actual source cycles | 2,459 across 333 parameters; 36,912 raw arrows and the same number of reduced arrows |
| Distinct normalized cycles | 1,184, all receiving the generic bound checks |
| Ordered nontrivial actual cycles | 50, of which 46 are wide |
| Ordered actual gap runs | 336 runs, 96 zero-forcing edges |
| Generated legal profiles | 360,618 with 5,840,503 raw arrows |
| Actual-height/order partition | 11,532 minimum-phase failures; 27,044 height failures; 4,583 order failures; 317,459 ordered profiles |
| Ordered profile gap checks | 5,368,529 recurrences; 4,229,502 zero-run checks |
| Known-cycle fixtures | All eleven stored raw cycles, including d5/7/13 |

The exact-run bound is at least 2 in 12 actual cases, eight wide, and
6,130 generated profiles, 6,111 wide. It exceeds the histogram bound in
five actual cases and 5,751 generated profiles. Conversely the histogram
bound is stronger in 16 actual cases and 1,303 ordered profiles. Neither
dominates the other in this finite comparison.

The coarser bound using only J is at least 2 in two actual cases, both
narrow, and 151 generated profiles. Its finite sample does not supply a
new wide-cycle exclusion. The all-period finiteness theorem depends on
the written proof and imported logarithm bound, not the number of tests.
The candidate B<=q−1 remains unproved despite finite success.

## Historical gate and preservation

The full required gate was run for this new mathematical-evidence batch:

```sh
python3 scripts/verify_all.py --cpp --transfer-controls
```

The gate completed with exit0 and PASS on all119 result fields; its
independent C++ checks and eleven raw transfer fixtures passed. Its
final output is stored in [full_gate.json](full_gate.json). The root separately
checked byte equality of the frozen R1-onward ledger, the open LaTeX source,
dispatcher proof/code, all 42 tracked files in C001–C004 and all 13 C005
batch files hashed by its prior delivery receipt. Earlier top-level
documentation snapshots are historical; current summaries intentionally
include C006. Publication is a separate outcome recorded in
[DELIVERY_STATUS.md](DELIVERY_STATUS.md).

The final staging attempt was not executed because automatic approval
review was at capacity. This does not change the completed verification
results. Commit and push remain outstanding; no publication is claimed.
