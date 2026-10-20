# C009 — Removing one rank usually destroys circular order

**Status: elementary written theorem, independently checked; no novelty
or Collatz-cycle exclusion is claimed.** This is a structural obstruction
to the proposed recursive excursion compression. The theorem concerns
finite rank permutations; its application to actual odd cycles retains
C005's domain and exact height labels.

## One-point deletion theorem

Let `R(j)=j+s mod m`, with `m>=2`, `1<=s<m` and `gcd(s,m)=1`.
Delete one rank and take the first-return permutation on the remaining
`m-1` ranks, keeping their circular order. This induced permutation is
a circular rank shift **if and only if** `s=1` or `s=m-1`.

For m2 the retained singleton has the identity permutation. The statement
is still true since its only possible s is1. A choice of circular origin
does not affect whether a permutation is a rank shift, so rotate the
deleted rank to0. Retained ranks `j=1,...,m-1` have compressed ranks
`j-1`. All but one return take one old step; the predecessor `j=m-s`
takes two steps through0. Their compressed shifts, modulo `m-1`, are:

| Old source ranks | Number | Compressed shift |
| --- | ---: | ---: |
| `1<=j<m-s` | `m-s-1` | `s` |
| `m-s<j<m` | `s-1` | `s-1` |
| `j=m-s`, via0 to s | 1 | `2s-1` |

For `2<=s<=m-2`, both regular groups are nonempty, and their shifts
are distinct modulo m-1. The induced map is therefore not a rotation.
For s1 all shifts reduce to1; for s=m-1 all reduce to-1. This proves
both directions. The exact shift formula is checked by directly
following all retained ranks in [check_return_order.py](check_return_order.py).

## Actual ordered-cycle consequence

Suppose a primitive ordered `3x+q` cycle with q<=L has exactly one
positive-height state, and normalized successor shift s. Its height-zero
first-return map is precisely the one-point-deleted permutation above.
For an interior shift `2<=s<=m-2`, it loses circular order at every
period covered by those hypotheses. This is a conditional structural
statement, not an assertion that such actual cycles exist at every m.

An exact example is the reduced q13 cycle

```text
n = (283,431,653,493,373)
a = (1,1,2,2,2),   h = (0,0,1,0,0),   A=8, m=5.
```

Its sorted normalized coordinates are `(283,653/2,373,431,493)`.
The corresponding scaled images are
`(862,986,1132,1306,1492)`, strictly increasing. The normalized successor
shift is s3. Removing653 leaves sorted core `(283,373,431,493)` with
first-return rank permutation `(2,0,3,1)`. Its shifts are not constant.
The positive excursion `431 -> 653 -> 493` has exact relation
`8*493=9*431+13*5` and increases despite remaining within a closed
ordered cycle. Thus both order preservation and automatic descent fail
for this proposed operation on actual controls.

An even stronger slope shortcut fails on the ordered q83 cycle
`(157,277,457,727,283,233,391)`: its excursion
`277 -> 457 -> 727 -> 283` has slope27/32 but rises by6. The affine
forcing term matters. Exact integer states and denominator checks are
in [excursions_audit.json](excursions_audit.json).

## What remains possible

Keeping a more general return permutation and each block's distinct
affine coefficients preserves the data. It does not preserve the
single-step circle-order theorem as an induction hypothesis. The
endpoint reconstruction theorem in [EXCURSION_ARITHMETIC.md](EXCURSION_ARITHMETIC.md)
also shows that exact block closure already contains all internal
valuation congruences. Additional global inequalities could still be
useful; this result excludes only the stated automatic compression
step. In particular it does not exclude a q1-specific argument and
does not decide divergence.
