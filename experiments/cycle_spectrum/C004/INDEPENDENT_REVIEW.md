# C004 — Independent review of the rotation lattice and narrow-cycle theorem

**Reviewer:** quantitative_literature lane. **Status:** source-level
mathematical review; the stated results pass this audit. This is not
formal verification, a human peer review, a novelty assessment, or an
independent replay of the full C004 data receipt.

## Source and scope

Reviewed [ROTATION_LATTICE.md](ROTATION_LATTICE.md), including its final
exact narrow-cycle spectrum corollary and the final scope clarifications.
The final reviewed source has SHA-256

```
c3687aab765f7665862cc3c5b5a08ec6c622b1625ab43f5051260d85a78059f7
```

Also checked the relied-on primitive and repeated-word denominator
arguments in [R71](../../residual_progress/lattice_cycles/BALANCED_DENOMINATORS.md).
The review retains the raw odd-only clock and distinguishes normalized
rational states from integer states for a specified odd parameter d.

The final header links this completed review, and the next-test row
asks for an order or cancellation constraint across several dyadic
ranges. Reversing exactly those two prose edits reproduces the previous
reviewed source hash; the mathematical proof text is unchanged.

## 1. Cycle lattice: passes

- The cyclic matrix has determinant `(-1)^(m-1) D`, including `m=1`,
  where the two entries in the row are added.
- For each prime dividing D, the recurrence modulo that prime has
  exactly one free coordinate. Thus the nullity is exactly one. If a
  Smith factor before the last were nontrivial, a prime dividing it
  would divide the last factor as well and force nullity at least two.
  This proves `diag(1,...,1,D)`, with no assumption that D is squarefree.
- Cramer's rule gives absolute maximal augmented minors
  `D,C_0,...,C_(m-1)`. Their gcd is g, and the earlier determinantal
  divisors remain 1 because the original matrix is a submatrix.
- The rational kernel is one dimensional. The displayed kernel vector
  `(C_0/g,...,C_(m-1)/g,D/g)` is primitive since its first and last
  coordinates are coprime. Therefore it generates the full integer
  kernel, rather than only a sublattice.
- Positive odd integer realizations are precisely positive **odd**
  multiples of that primitive vector. When `gcd(d,6)=1` is imposed,
  the multiplier must also be prime to 3. The statement for arbitrary
  odd d correctly permits odd scaling divisible by 3.

The lattice result supplies the same exact denominator obstruction as
the cyclic affine formula. It does not turn many rotated divisibility
conditions into independent restrictions.

## 2. One-letter cut formula: passes, including its extra factor

For a first-letter cut with `U=2^a`, direct expansion gives

```
U K = (U-3) C_i-D.
```

First g divides K because U is coprime to g. Dividing by g and using
`gcd(C_i/g,D/g)=1` then yields exactly

```
gcd(D,K)=g*gcd(d_0,U-3).
```

The extra gcd is essential. For the repeated word `(3,3)`,
`C=11,D=55,g=11,d_0=5`, while every cut has `K=0` and
`gcd(D,K)=55`. The formula gives `11*gcd(5,5)=55` correctly. A letter
1 or 2 makes the extra factor 1, as stated.

The largest-state argument correctly shows that a nontrivial positive
integer cycle for parameter 1 must contain valuation 1. It does not
assume the corresponding fact for every positive rational cycle or
every generalized parameter. The resulting limitation concerns bare
cut divisibilities; bounds on the size or structure of K remain outside
that limitation.

## 3. Narrow ratio forces the mechanical word: passes

Let the distinct rational states in increasing order be
`L=y_0<...<y_(m-1)=H<2L`. Their values `f_j=3y_j+1` increase strictly
and satisfy `f_(m-1)<2f_0`. Every f_j has exactly one power-of-two
normalization into `[L,2L)`, so the actual cycle valuations are q on an
initial block and q+1 on a final block of h indices.

The first index has valuation q; hence `h<m`. If h were zero, the
successor permutation would be increasing and hence the identity,
contrary to primitive period greater than 1. The high block lands
strictly below the low block after normalization. Its h outputs occupy
the first h sorted ranks, giving precisely the permutation

```
j -> j+h (mod m).
```

This checks the direction and the size of the rank shift. Transitivity
of the primitive orbit forces `gcd(h,m)=1`. Starting at rank zero, the
valuation q+1 occurs exactly at a carry in successive additions of h,
which gives the displayed floor-difference word and `A=mq+h`.
Consequently `gcd(A,m)=1`. No theorem about continuous circle maps or
an unverified symbolic conjugacy is needed.

## 4. Converse, endpoints, and spectrum: pass

For coprime mechanical totals, R71 identifies every phase with a
rotation. Each phase prefix floor exceeds the phase-zero floor by at
most one, with no change in the `j=0` summand. Thus every phase
intercept lies in `[C_0,2C_0)`, proving the strict ratio bound.

If a displayed mechanical word is a proper power, R71 reduces both
totals by their gcd and obtains the same primitive cycle. This is why
one must use its primitive period before claiming reduced denominator
`2^A-3^m`. The example `(1,2,2)^2` has unreduced difference 295 and
common factor 59, retaining reduced denominator 5.

The case `m=1` is included: the positive rational fixed points have
valuation `A>=2` and value `1/(2^A-3)`. Only A=2 gives denominator 1.
For `m>1`, R71's mod-8 argument rules out D=1 in the primitive
mechanical class. The boundary `H=2L` is impossible because all states
have odd numerators over one common odd denominator. Therefore a
hypothetical nontrivial integer Collatz cycle has `H>2L`.

For a fixed positive odd parameter d, normalize an integer cycle by d.
This preserves its exact valuation word, primitive period, and size
ratio. A narrow cycle is then primitive mechanical and has reduced
denominator D, so D divides d. Conversely a coprime pair `(A,m)` with
positive `D=2^A-3^m` dividing odd d gives odd scaling `d/D` of the
mechanical numerators. Every resulting arrow has its exact stated
valuation. The orbit is primitive because a repetition would make
both A and m divisible by its repetition count. The valuation word
and primitive length recover A and m, proving uniqueness up to
cyclic rotation. This verifies both directions of the exact spectrum,
including fixed points and odd d divisible by 3.

## 5. Independent arithmetic checks and remaining scope

I separately recomputed the intercept, D, g, reduced denominator, and
every one-letter cut for `(2)`, `(4)`, `(1,2,2)`, `(1,3)`, `(3,3)`,
and `(1,2,2)^2`. All displayed equations and controls agreed, including
the nonunit-cut and proper-power cases. These are local arithmetic
checks, not an independent run of another agent's full catalogue.

No proof correction was required. Two scope clarifications were
inspected in the final source: the maximum-state argument explicitly
says d=1, and the generic R71 large-height family is only said to
have reduced denominator greater than 1, which can be smaller than
its unreduced D. The latter addresses this reviewer's warning that
arbitrary ceil-total R71 words can be proper powers.
[SIZE_PROBE.md](SIZE_PROBE.md), Sections 3–4, separately supplies
coprime upper approximants and the stronger unbounded-pair-gap
obstruction. The final large-height sentence makes no pair-gap
inference from a minimum bound alone.

The primary-source pass in that note found extremal-minimum results
and the established mechanical/Christoffel connection. It did not
identify an inspected primary statement matching the narrow-ratio
converse. No novelty inference follows from that bounded search.

The audited theorem is an intrinsic classification of all narrow
primitive cycles, with an exact arithmetic realization criterion. It
does not exclude wide cycles, classify all denominator layers, or
address divergence. In particular, the failed absolute close-pair
criterion cannot be reinstated as a consequence of narrowness:
mechanical cycles can have ratio below 2 and every pair gap arbitrarily
large.
