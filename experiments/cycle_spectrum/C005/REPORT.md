# C005 — From dyadic order to an arbitrary rotation-block exclusion

**2026-10-19. Progress; the original all-cycle headline remains open.**
Baseline main is `61cf54ad52df1caa5cc250b0d1464432ed90b162`.
The selected mechanism is order across dyadic ranges and its interaction
with arithmetic cancellation. It produces a denominator theorem, as
well as exact obstructions to a stronger but invalid inference.

## 1. Main gain: arbitrary concatenations of mechanical rotations

Fix any primitive positive mechanical valuation word v, with coprime
totals `(A0,m0)` and `2^A0>3^m0`. Form any nonempty finite concatenation
of cyclic rotations of v. The number, order and multiplicities of the
blocks are arbitrary. Then

```
den(concatenation)>1,
```

unless the base is `(2)`, in which case all words repeat the fixed
cycle at 1. This is an all-size exclusion for the stated class.

The [written proof](ORDER_THEORY.md) has two parts:

1. An integer cycle with maximum odd state less than eight times its
   minimum has coprime primitive totals `(A,m)`. Exact odd-numerator
   spacing prevents inversions after dyadic normalization in this
   range. The successor becomes a transitive rank rotation.
2. If the base mechanical cycle has ratio R<2, every mixed block cycle
   has ratio at most R cubed, hence less than 8. Full blocks are
   contractions toward points in the base interval; their prefixes
   preserve a multiplicative comparison with base-cycle states. An
   integer mixed cycle would therefore reduce to one base block, whose
   exact denominator is already known from R71.

This permits arbitrary changes of phase between blocks. It removes
the two-block-order restriction within this rotation class, but does
not contain all C002/C003 cases, which admit nonmechanical blocks.
Arbitrary cycles need not have a common mechanical block decomposition.
No general denominator growth or fixed-denominator finiteness follows.

The [literature comparison](LITERATURE.md) gives a primitive six-phase
family with arbitrarily large minimum and arbitrarily many shortcut
local minima. It is nonmechanical and falls outside the direct fixed-count
and mechanical exclusions reviewed there. This is not a new universal
numerical record or a novelty claim against all literature.

## 2. Exact order criterion and the failed shortcut

For reduced numerator states n_i at parameter q, set L=min n_i,
`h_i=floor(log_2(n_i/L))`, and `z_i=n_i/2^h_i`. The normalized image is

```
F_i=3z_i+q/2^h_i,
c_i=a_i+h_(i+1)-h_i.
```

For a sorted pair `z_i<z_j` with height difference k>0, the odd integer
`r=n_j-2^k*n_i` is positive and

```
F_j-F_i=[3r-q*(2^k-1)]/2^h_j.
```

Ties are impossible inside a simple cycle. At q=1 no inversion is
possible with k<=2. More generally, strict F order gives a rank rotation
and mechanical normalized c. When q<=L, the converse also holds.

The original word a still differs from c by the retained height labels.
The fixed-point intercept contains weights `2^(-h_i)`. Removing them
changes its gcd. Therefore mechanical c does not imply no cancellation.

Two exact actual controls make that failure concrete:

| Reduced q | Odd period | Height range | gcd(C,D) | Normalized F order |
| ---: | ---: | --- | ---: | --- |
| 233 | 8 | 0,1 | 7 | Strict; rank shift 5 |
| 5 | 17 | 0,1,2,3 | 1,015,513 | Strict; rank shift 10 |

Both have mechanical normalized c and nonmechanical original words.
The q=233 example defeats the attempted inference already in two dyadic
bands. Conversely, the q=11 cycle with minimum numerator 13 has an
inversion despite q<=L; it also satisfies H<8L and gcd(A,m)=2, correctly
surviving the denominator theorem with q>1.

## 3. Exact checks and review

The [order checker](check_order.py) and [receipt](order_audit.json) replay:

- 2,459 actual cycles across 333 parameters, with 36,912 actual arrows
  and 36,912 normalized arrows; all eleven historical fixtures survive.
- 1,184 distinct normalized cycles and 739,757 exact state pairs.
  There are 71 monotone-image cycles, including 26 wide cycles with
  nontrivial cancellation. Four of those occupy just two height bands.
- 21,844 generated words of length 1–7 and valuations 1–4, including
  21,298 primitive positive realizations and 407,897 primitive pairs.
- 1,424 separate input pairs exercising the inversion formula, including
  128 q=1 inversions and 36 equal-image pairs with a common successor.
  These pair controls are not asserted to lie in a common cycle.

The separate [rotation-block checker](check_mechanical_blocks.py) and
[receipt](mechanical_blocks_audit.json) exercise arbitrary phase words,
proper repetitions, actual-cycle recognition and the high prime-base
family. Its independent root replay passes: 9,664 phase-grid words
exercise 227,860 raw arrows and 36,700 block boundaries, including
7,368 words with at least three distinct phases. The twenty prime-base
examples exercise 6,192 odd arrows and 9,876 shortcut arrows. There are
48 fixed-base controls, retaining all eight tested repetitions of `(2)`.
Among actual normalized cycles it recognizes 22 cycles, including three
mixed-block cycles at denominators 59, 295 and 943.

Both C005 checkers pass separate root replay. The historical gate also
passes, including independent C++ checks at 4096 and 262144 and all
eleven raw transfer cycles. Its scope is the preserved historical
mathematics; the separate new checkers cover C005.

[Independent proof review](INDEPENDENT_REVIEW.md),
[root review](ROOT_REVIEW.md), the [historical gate](full_gate.json), and
[delivery checks](delivery_checks.json) have distinct scopes. None turns
a finite test into the universal proof. Novelty, human peer review and
formal verification of C005 are unclaimed.

## 4. External input and next obligation

Read the side branch at local tracking pin
`67c691b93ddd3d07748f557c8a26f9883e37389b`. The fetch attempt failed in
automatic approval review because its model was at capacity. The
[side review](SIDE_REVIEW.md) records this limitation, the reported
stronger C002 Lean declaration, and an exact correction to identifying
narrowness with discrepancy centered on log_2(3). No side branch changed.

The shared local reference subsequently advanced to `2ea1c7f6e51e31b80d354b458d8fa121e4f6e8aa`.
The [addendum](SIDE_ADDENDUM.md) records its reported C003 effective-bound
Lean check. Main has not independently replayed that build; it supplies
no new C005 premise.

The next proposed intermediate target is denominator-1 exclusion for
cycles with circular normalized successor order, without a prescribed
block decomposition or a bound on period or height. The exact obstructions
above rule out simply discarding heights or treating a normalized
mechanical word as an ordinary mechanical cycle. The argument must retain
the weighted intercept and allow the ordered q5 and q233 controls.
No theorem places all hypothetical integer cycles in the ordered class,
and no fixed ratio bound on all cycles is supplied.

The headline remains exclusion of all nontrivial integer cycles. The
suggested bounded-denominator-finiteness goal was not activated, and
divergence remains separate.
