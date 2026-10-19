# C005 — Independent proof review

**Reviewer:** quantitative_literature lane. **Status:** the elementary
arguments reviewed below pass. This is an agent's mathematical source
review, not formal verification, human peer review, or a novelty claim.
The full cycle-exclusion goal remains open.

## Reviewed sources

The review covers [ORDER_THEORY.md](ORDER_THEORY.md),
[SIDE_REVIEW.md](SIDE_REVIEW.md), and the mathematical family and
scope comparison in [LITERATURE.md](LITERATURE.md), including normalization,
both directions of the order criterion under `q<=L`, the three-band
denominator corollary, the rotation-block theorem, and the exact controls.
Final reviewed SHA-256 fingerprints are:

| Source | SHA-256 |
| --- | --- |
| ORDER_THEORY.md | `bf1048e6de6c90bbc477c34b061b73435afc0d61553fd6309c4595c1ef929a44` |
| SIDE_REVIEW.md | `bb78d37dfabc993f043f9febed43c6e133043e2f0b4891ad20b210e82cb61e00` |
| LITERATURE.md | `d1a246f0ce9e569fe5a6bb70e7b0637057eea64d922f3aa4167acfe12859d5e9` |

After the last mathematical audit, the author changed only the title
and status/link to this review. Reversing exactly those two edits
reproduces the earlier audited source hash, confirming no further
proof changes.

I also read the latest relevant entries of `sidekick/FEED.md` and the
direction table in `sidekick/DIRECTIONS.md` directly at the stated pin
`67c691b93ddd3d07748f557c8a26f9883e37389b`. Those are external reports,
not mathematical premises or instructions. I did not repeat the fetch,
independently build the Lean lane, or run another agent's full receipt.

## 1. Normalization and the exact inversion test

For positive odd cycle numerators, the normalized points
`z_i=n_i/2^h_i` in `[L,2L)` are distinct: equality makes the ratio of
two odd numerators a power of 2, hence 1. The normalized successor
identity is exactly

```
F_i=3z_i+q*2^(-h_i)=2^c_i z_(i+1),
c_i=a_i+h_(i+1)-h_i.
```

Since `F_i>3L` and `z_(i+1)<2L`, the integral c_i is positive.
The height differences telescope, preserving the total A. Under
`q<=L`, the bounds `3/2<2^c_i<7` force `c_i` to be 1 or 2.

For `z_i<z_j` and increasing height gap k, the integer
`r=n_j-2^k n_i` is strictly positive and odd. Direct subtraction
gives `(3r-q(2^k-1))/2^h_j`, with the sign and the factor in the
denominator as stated. Nonincreasing heights give strict order directly.
Equal F-values cannot occur within a simple cycle: their unique
normalizations into `[L,2L)` would give the same successor z, hence
the same successor numerator and therefore the same predecessor index
in the cycle permutation. The equality exclusion correctly uses the
actual cycle and its distinct states.

## 2. Order lemma and its converse

The forward direction does not require `q<=L`. Under sorted F
monotonicity, the minimum normalized point is the original minimum L
with height zero, so the least F equals `3L+q`. Every F is less than
`6L+q<2(3L+q)`. The normalization exponents therefore take at most
two consecutive values, with the larger value on a final block.
Dividing that block by one extra factor of 2 moves its outputs strictly
before the other block. This gives exactly the rank shift stated in
the source. For primitive period greater than 1, its shift is nonzero
and coprime to the period. The carry calculation then yields a
primitive mechanical c-word with `gcd(A,m)=1`.

For the converse, retain `q<=L`, hence `c_i in {1,2}` and
`3z_i<F_i<=4z_i`. A nonwrapping successor has larger z; c_i=2
would violate the upper bound, so c_i=1. A wrapping successor has
smaller z; c_i=1 would violate the lower bound, so c_i=2.
Within each rank block F increases. Across the boundary the first
block's F-values are below `4L`, and the second's are at least
`4L`. Thus a rank rotation forces monotonicity. Both directions pass;
the restriction on q in the reverse implication is retained.

Mechanical c alone is weaker. The q=11 control has the repeated
mechanical word `(1,2,2,2)^2` but an inversion and a nonrotation
successor permutation. Its original cycle still has primitive period
8. This distinction prevents transferring primitivity from a to c
without the order hypothesis.

## 3. Three-band denominator corollary

At q=1, increasing height gaps 1 and 2 give respective numerators
`3r-1>0` and `3r-3>=0` in the difference formula. The equality case
has already been excluded inside a primitive cycle. If `H<8L`, every
height is 0, 1, or 2, so every sorted pair has the required order.
The order lemma forces `gcd(A,m)=1` for primitive period greater
than 1.

Consequently the stated class

```
primitive period m>1, H<8L, gcd(A,m)>1
```

has reduced denominator greater than 1. This is a contraposition of
the q=1 statement; it does not assume order at every larger q.
The endpoint `H=8L` is impossible for odd numerators, giving the
strict `H>8L` conclusion for a hypothetical integer cycle with common
factor in its totals. The q=11 cycle satisfies the class hypotheses
and survives with reduced denominator 11.

The draft called the H<8L regime “two-band.” I flagged this: it has
three dyadic height bands. The revised source correctly says
three-band; the q=233 example with heights 0 and 1 is genuinely
two-band. No change to the proof was needed.

## 4. Weighted intercept and independently recomputed controls

Starting at the minimum gives `h_0=0` and
`P_j=A_j+h_j`. Iterating the normalized affine equations produces

```
D*L=q*sum_j 3^(m-1-j)*2^(P_j-h_j)=q*C_w.
```

Thus the source correctly retains the height-dependent coefficients.
Replacing them with 1 would substitute the mechanical c-intercept
for the original intercept and is not a permitted denominator step.

I independently recomputed the displayed examples with exact integers
and rational numbers, without importing the author's checker:

| q | m | A | Original C | D | gcd(C,D) | Normalized order |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 233 | 8 | 13 | 10745 | 1631 | 7 | Strict F order; rank shift 5 |
| 5 | 17 | 27 | 189900931 | 5077565 | 1015513 | Strict F order; rank shift 10 |
| 11 | 8 | 14 | 11609 | 9823 | 893 | Inversion; ranks `(7,6,0,1,2,3,4,5)` |
| 23 | 2 | 5 | 7 | 23 | 1 | Strict F order; rank shift 1 |

For each row I verified every raw arrow and its exact valuation,
oddness, coprimality with q, all height and c labels, all listed
sorted F-values, and the weighted identity. In particular the q=233
example already disproves full-denominator inheritance in two height
bands, with strict order and `q<=L`. The q=5 control gives large
cancellation, but one finite example cannot establish unbounded
cancellation at a fixed denominator.

The shorter d=5, d=7 and d=13 controls retain their correct raw-map
interpretation. A generalized raw cycle containing state 1 is not
presented as a nonconvergence witness for a map that absorbs there.

## 5. External scope and discrepancy correction

The stated side pin contains the C004 finite replay report, C003
contracting-bound report, and the update that the Lean lane's
`uniform_two_block_strong` includes the full C002 factor. SIDE_REVIEW
correctly labels these as external reports rather than this reviewer's
or main's independent Lean replay. I did not verify the reported builds
or their axioms during this audit.

The discrepancy counterexample is exact. The raw parameter-23 cycle
`7 -> 11 -> 7` has valuations `(2,3)` and ratio `11/7<2`, while
the full-period discrepancy centered on `log_2(3)` is
`5-2*log_2(3)>1`, since `32>18`. Mechanical coding centers on the
actual slope A/m. The two centers cannot be interchanged without the
accumulated additive-error term. The distinction between a fixed
spread restriction and exclusion for every finite spread restriction
is also correct: the latter already covers all finite cycles.

The cited primary literature remains contextual. No unverified
external theorem is used by the elementary arguments reviewed here;
novelty of these consequences has not been established.

## 6. Arbitrary concatenations of mechanical rotations

The new rotation-block theorem passes the independent argument check.
Let the primitive mechanical base have coprime totals `(A_0,m_0)`,
positive difference D_0, cycle interval `[l,h]`, and ratio `R<2`.
Every rotation block has the same contraction slope s and a fixed
point X in this interval. Their composition preserves the interval
and has one fixed point there; subsequent block boundaries also stay
inside it. Equivalently, each boundary is a convex combination of
the block fixed points with positive geometric weights.

For a prefix map `f(x)=alpha*x+beta`, with `alpha>0,beta>=0`, the
ratio `f(x)/f(X)` is a weighted average of `x/X` and 1. All base
prefix values f(X) lie in `[l,h]`. Therefore all mixed-cycle states,
including intermediate states inside every block, lie in
`[l/R,Rh]`, giving the strict global ratio bound `H/L<=R^3<8`.
The positive whole-word difference and exact rational legality follow
from the positive valuation word and the contracting total slope.

The repetition argument must use the actual primitive period. If
the displayed r-block word is p repetitions of its primitive word,
then p divides both rA_0 and rm_0, hence p divides r. The gcd of the
primitive totals is exactly r/p. If the reduced denominator were 1,
the three-band corollary forces r/p=1 when the primitive period
exceeds 1. At primitive period 1 the gcd is already 1, with no need
to invoke that corollary. Thus p=r in both cases. The primitive word
has length m_0, every aligned block is identical, and the cycle is
the base mechanical cycle. R71 leaves only base `(2)` at denominator
1. The author added the requested period-1 sentence, and I inspected
it in the final proof. The m>1 corollary is now applied only within
its stated hypotheses.

I independently checked the smallest displayed mixed example:
`(122)(221)` has C=1805, D=295, g=5, denominator 59 and numerator
orbit `(361,571,443,347,275,221)`. Its ratio is `571/221>2` and
below 8. This is a genuinely nonnarrow control for the new theorem.
It also preserves the known generalized cycles rather than excluding
all denominators.

## 7. Primitive high family and comparison scope

For prime `m_0>=13`, `A_0=ceil(m_0*log_2(3))` lies strictly between
m_0 and 2m_0, so its gcd with m_0 is 1. The two chosen rotations
are distinct because the base word is primitive. The label word
`001011` has no cyclic period 1, 2 or 3.

For the full valuation word, a primitive cyclic period T must have
the same average valuation A_0/m_0. Its reduced denominator m_0
therefore divides T. The aligned period would induce a proper cyclic
period of `001011` unless T=6m_0. This proves primitivity and gcd 6
of the full totals. An arbitrary finite-word period not dividing the
cyclic length is not being assumed to have that average. The final
source explicitly takes the least cyclic period dividing 6m_0, as
requested in review, and specifies label 1 as the one-letter left
shift so the source, literature note and finite example convention
agree.

R71 gives `l>m_0/6`. The prefix envelope then gives every mixed
rational state above `l/R>m_0/12>1`. The valuation letters are 1
or 2; exactly `6(A_0-m_0)` of them are 2. In the raw shortcut clock
each odd step increases the state and each valuation-2 letter
introduces exactly one even descent before the next odd state.
Thus the stated shortcut local-minimum count is correct and grows
without bound. It is not the odd-only minimum count.

I separately realized the six-block family at prime base lengths
13, 17 and 19. Exact checks verified every arrow, full primitivity,
the ratio envelope, minimum bound, denominator greater than 1 and
the actual shortcut-local-minimum counts 48, 60 and 72, respectively.
These three cases are arithmetic controls; the unbounded statements
come from the proof, not this finite check.

The literature comparison correctly restricts its conclusion to
escaping every fixed minimum/count cutoff and the directly excluded
mechanical class. It does not assert an improved universal numerical
record or independence from all consequences of the cited papers.
The new class neither contains all C002/C003 words nor supplies
bounded-denominator finiteness as the block count increases. This
review checked that logical comparison and its clock conventions;
the fresh primary-paper retrievals are the root lane's work, not an
additional independent literature or computational replay by this
reviewer. Novelty remains unclaimed.

## 8. Review boundary

This review checks written proofs and named examples. The larger actual
cycle census, generated-word catalogue and historical finite gate have
their own receipts and authors; this note does not claim an independent
rerun of them. Normalized order and a mechanical c-word do not supply
the original word's denominator. The common-factor restriction and
rotation-block theorem exclude stated classes; they leave general
coprime-total words in the three-band regime and general wider cycles
unresolved, as well as every divergence question.
