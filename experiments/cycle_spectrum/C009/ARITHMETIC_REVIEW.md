# C009 independent mathematical and checker review

**Result: PASS within the stated scope.** I authored
[EXCURSION_ARITHMETIC.md](EXCURSION_ARITHMETIC.md); its checks here are
author review. I independently reviewed
[FIRST_RETURN_ORDER.md](FIRST_RETURN_ORDER.md) and
[check_return_order.py](check_return_order.py), which other agents wrote.
The separate [checker review](CHECKER_REVIEW.md) independently reviews
my arithmetic note. These are written
elementary results and a finite replay, not a proof excluding an
ordered denominator-one cycle. The domain is raw positive odd-only
`3x+q`, without absorption at 1.

## Mathematical checks

1. **Exact endpoint reconstruction.** For every prefix `j`, the identity
   `C_ell=3^(ell−j)C_j+2^A_j C_tail` reduces the exact endpoint equation
   modulo `2^A_j` to a unit multiple of
   `3^j x+q C_j=0 (mod 2^A_j)`. Thus every intermediate state is an
   integer. If `q` and both endpoints are odd, each intermediate source
   must be odd because `3u_j+q=2^a_j u_(j+1)` with `a_j>=1`; the odd
   successor makes the valuation exact. The lemma does retain all
   internal cylinders; there is no omitted extra bit.
2. **Cut elimination and Smith form.** For an excursion and complement,
   eliminating their shared endpoint gives
   `D x=q(3^r C_E+2^a C_P)`. The parenthesized quantity is the full
   rotated intercept. For any number of exact blocks, the cyclic
   coefficient determinant has magnitude `D=2^A−3^m`. Every prime
   dividing `D` is coprime to 6, and the displayed `(k−1)`-minor is
   a power of 3, so the Smith form is `(1,...,1,D)`, including `k=1`.
   Cramer's augmented maximal minors have gcd `gcd(D,qg)`, with
   `g=gcd(D,C)`. At `q=1`, the integer test is exactly `D|C`;
   rotation propagation then gives all odd states and exact arrows.
   This is a faithful compression of C004's existing one-obstruction
   calculation, not a new independent denominator restriction.
3. **One-rank deletion theorem.** After deleting rank zero from
   `j -> j+s mod m`, the `m−s−1` low sources have compressed shift `s`,
   the `s−1` high sources have shift `s−1`, and the predecessor of zero
   has shift `2s−1`, modulo `m−1`. For `2<=s<=m−2`, both regular
   types occur and differ, so the first return is not a rank rotation.
   For `s=1` or `m−1`, all shifts reduce to the same nearest-neighbor
   shift. The singleton retained case `m=2` is covered. This is a
   combinatorial obstruction to recursive order, not a claim that
   every abstract rank deletion is realized by a cycle.
4. **Actual controls.** For the ordered `q=13` cycle
   `(283,431,653,493,373)`, the sorted normalized states are
   `(283,653/2,373,431,493)` and their scaled images are
   `(862,986,1132,1306,1492)`. The height-zero return ranks are
   `(2,0,3,1)`, so order fails after the cut. Its excursion equation
   `8*493=9*431+13*5` and complement equation
   `32*431=27*493+13*37` are exact. The ordered `q=83` control has
   `277 -> 457 -> 727 -> 283`, with
   `32*283=27*277+83*19`: homogeneous slope `27/32<1` yet net
   increase 6. These examples invalidate only the named return-order
   and slope shortcuts. The `q=5` cut in the main note also checks.

## Finite checker audit

The deletion checker enumerates each `m=2..80`, each coprime
`1<=s<m`, and every deleted rank; it compares the first-return map
with the closed shift formula and classification. It does not infer an
actual `3x+1` cycle from a permutation. The endpoint checker constructs
odd endpoint residues modulo `2^(A+1)` for all positive words of
length 1..5 over valuations 1..4, parameters `q=1,5,7,13`, and three
lifts. It checks positivity, oddness and every exact arrow. The two
stored cycle controls check their full arrows, reduced denominator,
normalized order, return equations and the q83 drift. I replayed the
saved receipt with the checker: **PASS**, covering 105,388 deletion
permutations and 6,250,510 rank arrows, plus 16,368 endpoint pairs
and 76,464 exact odd arrows. The finite ranges are not an all-period
proof.

## Pinned source and limit

| File | SHA-256 |
| --- | --- |
| `EXCURSION_ARITHMETIC.md` | `7d4a0f7413dea67be2f3fd6e6643ace2ccb8b2decee6dc17f2b77f10b27eabcd` |
| `FIRST_RETURN_ORDER.md` | `10a7f10d396a8631c197f3203af498467d92551ad35f4e9ded63c7c621d354fa` |
| `check_return_order.py` | `58b016702d0292a5294027dd75139b36dad171fc2e314971ae07a46fb2a59355` |
| `return_order_audit.json` | `ab4672a38fa2dc688d34ced57d3af0148eab1b821267eb44ed013b016eba5d34` |

The resulting decision is precise: exact excursion closure contributes
no congruence beyond `D|C`, while first-return compression may lose
the circular order hypothesis. A q1-specific theorem might still use
the full weighted intercept and sorted inequalities together. No such
theorem, novelty claim, or formal verification is supplied here.
