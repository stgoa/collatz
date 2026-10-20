# Pinned review: rank checks and repeated-factor spacing

Date: 2026-10-18. Optional side-lane input at
`fcc7e8825073bf7a7f4363cd9427ed8ceefadf12` was read and materialized in
temporary storage. The side branch was not changed. At this refresh remote
main remained `e9effe1c7ee15dc4aada6e1aef98828fb9d78856`, and GitHub listed
only merged [PR1](https://github.com/stgoa/collatz/pull/1), already incorporated.
The newer findings are on the separate side branch, not a new merged PR.

The unmodified `batch_r75_r77_check.py` and
`itinerary_complexity_general.py` both passed with individual 60-second
execution caps. Both generated JSON receipts matched their pinned published
receipts byte for byte. Imports were also read from that exact commit.

| Pinned file | SHA-256 |
|---|---|
| `reviews/side_lane/batch_r75_r77_check.py` | `ab06b27788f18644fc00dbc92fc926448edee94d3c248e0c38709b8ae13f1845` |
| `reviews/side_lane/batch_r75_r77_check.json` | `06ef47a7d4db744867da72aa89890ef929b6b660a039c273d3aa3fc600f1b4a8` |
| `reviews/side_lane/itinerary_complexity_general.py` | `e5099124e39c13c92a9ea7914343a6441e3a691f1f11b773eb5a8a02840da23c` |
| `reviews/side_lane/itinerary_complexity_general.json` | `f4e65d5d79abeb5a85d6a3aed3e9ffe790ae952fad08c22e09411465ee7a8287` |
| `reviews/side_lane/fibre_count_check.py` | `071b2d076702ff0ab87746b9c130c0271c2adcf82b45f59e5d0ffec53b14923a` |
| `experiments/packet_currents/negative_controls/affine_controls.py` | `9e5ad66deaf7ede55b1d607f6d85d57f58d38e9dd2c551d45f1b7a2d58538e3c` |

## Reproduced evidence

- R75: 3,000 sampled returning inputs, testing the native W9 translation,
  exact two-arrow prefix and strict native height. The probe does not
  reconstruct all signed current tables or the nonzero lower loop.
- R77: 2,188 repeated factors in 150 legal finite trajectories, 200 complete
  copy-count cases and the exact all-seed 37-return cutoff. Its own
  arithmetic is independent of main's implementations.
- General spacing: 4,042,351 repeated valuation factors of lengths1–6 on
  ordinary odd orbits starting below100,000, stopping at1. The probe checks
  the exact residue and integer size statements, then a floating-point
  logarithmic inequality. The written argument below supplies the exact
  inequality independently of that floating-point check.

The side lane's ancestor census was read but not rerun in this batch or
used as a premise. No asymptotic density claim is imported.

## Review of the general argument

Suppose a nonrepeating ordinary odd Syracuse trajectory begins at x0.
Two occurrences of one exact valuation word of length L and total e, at
i<j, start in the same residue modulo2^(e+1). The extra bit is essential.
Since the starting integers are distinct and positive,

    2^(e+1) <= |x_j-x_i| < max(x_i+1,x_j+1)
                           <= (3/2)^j*(x0+1).

The final bound follows one step at a time from
`S(x)+1 <= (3/2)(x+1)` for positive odd x. It does not require the orbit
itself to increase. The first inequality is exact integer arithmetic.
If p(L) is finite, among the first p(L)+1 windows one repeats, with
j<=p(L). Since e>=L,

    p(L) > (L+1-log2(x0+1))/log2(3/2),
    liminf p(L)/L >= 1/log2(3/2) = 1.7095112913514547... .

If p(L) is infinite, the corresponding lower bound is automatic. A
hypothetical divergent orbit is nonrepeating, so the conditional complexity
conclusion follows. This is the same exact-cylinder/growth mechanism as
R77 with a weaker general constant. It excludes sufficiently low-complexity
itineraries and leaves higher-complexity ones open. The feed's informal
average-valuation refinement needs explicit prefix and window hypotheses;
it is not promoted here. No novelty claim is made, and no external theorem
is needed beyond the exact cylinder identity already proved in the repo.

## Research decision

Keep the negative controls and conditional minimality theorem, with the
[PR1 scope corrections](../locally-collatz-like-control-barrier/PR1_REVIEW.md).
They do not rule out alternative constructions. Keep repeated-factor
spacing as a constraint on one fixed hypothetical survivor, without treating
linear complexity growth as a termination proof.

The constructive priority is now smaller-origin histories. R80 proves a
whole blocked-W9 cylinder with a high meeting point and strict original-rank
inputs, while complete inverse comparisons cannot find a smaller ancestor
through arbitrarily prescribed depths. R78/R79 retain exactly where native
forward continuation works and where standard inverses undo earlier work.
The next target is coverage of an entire remaining type with all smaller
premises supplied, rather than another finite acceptance percentage.
