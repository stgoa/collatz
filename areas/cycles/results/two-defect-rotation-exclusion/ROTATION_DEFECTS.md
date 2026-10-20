# C011 — Two rotation defects and a uniform cancellation bound

**Status: elementary written two-arc theorem, structural classification,
and effective bounded-denominator finiteness using the published two-logarithm
input already recorded in C006.** An explicit all-size integer-cycle
application requires its own quantitative inputs and audit. This note
supplies no proof excluding all nontrivial integer cycles and makes no
novelty or formal-verification claim.

All cycles use the raw positive odd-only clock, with no absorber. Let
`w=(a_0,...,a_(m-1))`, with `m>=2` and `a_i>=1`. Put

```text
P_j=sum_(i<j) a_i,      A=P_m,
C_w=sum_(j=0)^(m-1) 3^(m-1-j) 2^P_j,
D=2^A-3^m>0,           g=gcd(C_w,D),        q=D/g.
```

The rational cycle has states `C_i/D` over its rotations. Its reduced
numerators `C_i/g` are positive odd integers and give an actual `3x+q`
cycle. These are the conventions and exact identities of
[C004](../narrow-cycles-are-mechanical/ROTATION_LATTICE.md).

## 1. Two defects, their amplitude, and automatic primitivity

Let `R_r w` be the left rotation by a nonzero `r mod m`. Suppose it
differs from `w` at exactly two positions. Rotation preserves the
multiset of entries, so the two differing entries are swapped. Let
`k>=1` be their absolute difference, called the amplitude here.

A two-defect word is automatically primitive. If it were `e>=2`
repetitions of a shorter word, its Hamming distance from any rotation
would be `e` times the shorter word's distance from the induced rotation.
That shorter distance is either zero or at least two, since a rotation
cannot change a multiset at exactly one position. Distance two for the
full word is therefore impossible. In particular repetitions of `(2)`
are correctly outside this hypothesis; their reduced denominator 1 is
not excluded by anything in this note.

There is a useful structural description. The permutation `i -> i+r`
has `h=gcd(r,m)` cycles, the residue classes modulo `h`. On each such
cycle, the differences `a_(i+r)-a_i` sum to zero. The two nonzero
differences must therefore lie on the same permutation cycle. Every
other permutation cycle has a constant letter. The active cycle has
exactly two switches and only the two exchanged values. Hence a
coprime shift gives a binary word, whereas a noncoprime shift may have
additional constant-letter classes. No binary-alphabet hypothesis is
needed in the arithmetic theorem below.

## 2. Both mismatch arcs retain cancellation

Cyclically cut and, if necessary, exchange the two compared words so
that the mismatches occur at positions `0` and `ell`, `1<=ell<m`,
with

```text
w_0=a,       w_ell=a+k,
w'_0=a+k,    w'_ell=a,             a>=1, k>=1,
```

where `w'` remains a rotation of `w`. Elsewhere the words agree.
Their prefix sums differ by `k` exactly at `j=1,...,ell`. Thus

```text
C_(w')-C_w
  = (2^k-1) sum_(j=1)^ell 3^(m-1-j) 2^P_j
  = (2^k-1) 2^a 3^(m-1-ell) C_u,                 (1)
u=(w_1,...,w_ell).
```

Write the complementary original arc as
`v=(w_(ell+1),...,w_(m-1),w_0)`. Recut at the other mismatch and
exchange comparison roles. The same calculation gives the other arc
intercept. In that calculation its final letter is `a+k` instead of
`a`; **an intercept does not depend on the last valuation**, so this
is precisely `C_v`. This last-letter observation is essential when
using the original arc totals, which satisfy

```text
len(u)+len(v)=m,       sum(u)+sum(v)=A.
```

All rotated intercepts are divisible by `g`, and `g` is coprime to 6.
Removing the powers of 2 and 3 in (1) and its complementary version
yields the two-arc cancellation theorem:

```text
g divides (2^k-1) gcd(C_u,C_v).                   (2)
```

This is a divisibility bound, not generally an equality. Indeed, for
an arbitrary rotation the exact identity is

```text
gcd(D,C_(R_r w)-C_w)
   = g gcd(q, 2^P_r-3^r).                         (3)
```

To verify it, use `2^P_r C_(R_r w)=3^r C_w+D C_prefix`, divide
`D` and `C_w` by `g`, and use `gcd(q,C_w/g)=1`. Thus a rotation
difference can retain an extra factor from the reduced denominator.
Neither (2) nor intersecting its two factors licenses removing that
factor without proof.

## 3. A uniform bound, including the unused terminal valuations

Let a positive word `z` have length `l`, total `S`, and last
valuation `b`. Its prefix before position `j` obeys

```text
P_j <= S-(l-1-j)-b = S-l+j-(b-1).
```

Consequently

```text
C_z <= 2^(S-l-(b-1)) (3^l-2^l)
    <  2^(S-l-(b-1)) 3^l.                         (4)
```

The exponent is nonnegative because all the other `l-1` valuations
are positive. This argument also covers `l=1`, for which `C_z=1`.

The two original arcs end in `a+k` and `a`. Applying (4) to both
arcs in (2) gives

```text
g <= (2^k-1) sqrt(C_u C_v)
  <  (2^k-1) sqrt(2^(A-m-k-2a+2) 3^m)
  <= (2^k-1) sqrt(2^(A-m-k) 3^m).                 (5)
```

Neither arc needs positive pure-block denominator. No coprimality
between its pure-block denominators, no bound on other letters, and
no coprimality between the shift and `m` is assumed.

**Uniform two-defect denominator theorem.** Put
`delta=A log 2-m log 3>0`, with natural logarithms. Every word in
the declared two-defect domain satisfies

```text
q > 2^(a-1+(m+k)/2) [2 sinh(delta/2)]/(2^k-1)
  >= 2^((m+k)/2) [2 sinh(delta/2)]/(2^k-1)
  >  2^((m-k)/2) [2 sinh(delta/2)].               (6)
```

**Proof.** Divide `D` by (5), and use
`D/sqrt(2^A 3^m)=2 sinh(delta/2)`. Finally `a>=1` and
`2^k-1<2^k`. QED.

This is uniform in the period, original word, alphabet, two arc sizes,
and chosen rotation. It controls the two-defect relation itself, rather
than assuming a representation by repetitions of fixed blocks.

### Removing the amplitude restriction

Since one valuation is at least `k+1` and all others are positive,
`k<=A-m`. The last inequality in (5), together with `2^k-1<2^k`,
therefore gives

```text
g^2 < 2^(A-m+k) 3^m <= 2^(2A-2m) 3^m,
g   < 2^A (sqrt(3)/2)^m,
q   > (1-3^m/2^A) (2/sqrt(3))^m.                (7)
```

There is **no amplitude restriction** in (7). No assumption about the
other valuations or the two arc lengths has been added.

### Every bounded denominator layer of the two-defect class is finite

The published effective two-logarithm bound used in
[C006](../ordered-cycle-sparse-forcing/ORDER_RIGIDITY.md) supplies absolute effective `c_0>0`
and `K_0>0` such that `delta>=c_0 m^-K_0` when `A<2m`.
Its inputs are the fixed algebraic numbers 2 and 3, degree 1, and
integer coefficients `(A,-m)`. Decrease `c_0` to at most 1. Then
`1-exp(-delta)>=c_0 m^-K_0/2`. For `A>=2m`,
`1-exp(-delta)>=1-(3/4)^m>=7/16`, since `m>=2`.
Thus there are effective absolute constants `c,K>0` such that

```text
q > c (2/sqrt(3))^m m^-K                         (8)
```

for **every** positive two-defect word, allowing unbounded amplitude.
In particular, a fixed denominator ceiling `q<=Q` bounds `m`,
effectively in principle.

It remains to bound the valuations, because bounded length alone does
not give finitely many words. Put `S=A-k`. If
`A<m log_2 3+1`, the bounded `m` already bounds `A`. Otherwise
`1-3^m/2^A>=1/2`; the stronger bound (5), before using `k<=A-m`,
gives

```text
q > (1/2) 2^(S/2) (2/3)^(m/2).                  (9)
```

Thus bounded `q,m` bound `S`. Rotate the upper defect letter `a+k`
to the final position. The intercept ignores that final valuation,
and (4) gives

```text
g <= C_rot < 2^(S-a-m+1) 3^m <= 2^(S-m) 3^m.
```

Consequently `D=qg` is bounded by `Q 2^(S-m)3^m`, and
`2^A=D+3^m` is bounded. This bounds `A`, `k`, and every positive
valuation. We have proved:

> For every fixed positive `Q`, only finitely many positive valuation
> words with a two-defect cyclic rotation have reduced denominator at
> most `Q`. This finiteness is effective in principle and uniform in
> the period, alphabet, defect amplitude and rotation.

The quantitative dependence on amplitude in (6) can still be useful:
it implies `q>c' 2^((m-k)/2)m^-K'` directly. In particular any fixed
amplitude ceiling or condition `k<=(1-epsilon)m` gives a stronger
exponential rate in its stated range. These are refinements, not
premises needed for the unrestricted two-defect finiteness theorem.

This qualitative imported-bound argument alone leaves finite exceptions
at `q=1`; it is not an all-size exclusion. An application using explicit
linear-form constants and published integer-cycle lower bounds must
record those additional constants, clocks and hypotheses separately.

## 4. The adjacent unit-amplitude case is the old mechanical class

If the two mismatch positions are adjacent, take `ell=1`. Equation
(2) has `C_u=1`, so

```text
g divides 2^k-1.                                  (10)
```

At `k=1` this gives `g=1`. This does not discover a new unit-amplitude
class: the primitive word is mechanical in this adjacent case.

Here is a direct classification. The shift-graph argument in Section 1
shows that `gcd(r,m)=1`, because the adjacent defects must lie on one
residue-class orbit. Every letter is `a` or `a+k`. Write
`b_i=(w_i-a)/k` and `t=sum_i b_i`, so `0<t<m`. With the orientation
above,

```text
b_(i+r)-b_i = 1_(i=0)-1_(i=1).
```

Multiply by `i` and sum around the cycle. Reindexing the rotated sum
gives `r t-m sum_(j<r)b_j=1`, so `rt=1 mod m` and `gcd(t,m)=1`.
Set `phi=m-1-t`. The mechanical mask

```text
b_i^* = floor(((i+1)t+phi)/m)-floor((it+phi)/m)
```

satisfies the same difference equation: rotation by `r` changes its
phase by one, creating the positive defect at 0 and the negative one
at 1. Hence `b-b^*` is invariant under a coprime shift and is constant;
its total is zero, so it vanishes. This proves the classification.

For `k=1`, `a+b_i^*` is the mechanical valuation word, up to phase;
R71 (`experiments/residual_progress/lattice_cycles/BALANCED_DENOMINATORS.md`, not yet migrated)
already gives its exact denominator `D`. For `k>1` the same binary
mask has a nonconsecutive letter substitution, so it need not be a
mechanical valuation word. With separated defects, even the binary
mask need not be mechanical. The general theorem therefore must not
be identified with the adjacent unit-amplitude special case.

## 5. An explicit family with unbounded minima and cycle complexity

For `r>=1`, put `n=2^r-1`, `A_0=ceil(n log_2 3)`, and let
`b_n` be the lower mechanical positive word of length `n` and total
`A_0`. Define

```text
w_n=(3,b_n,4,b_n),
m=2n+2=2^(r+1),               A=2A_0+7.
```

The markers 3 and 4 each occur exactly once, so `w_n` is primitive.
Rotation by `n+1` has exactly two mismatches of amplitude one.
Moreover `A` is odd, so `gcd(A,m)=1`, and

```text
2^A/3^m = (128/9)(2^A_0/3^n)^2 > 128/9 > 9.
```

Thus `2 sinh(delta/2)>8/3`. The two-arc bound (6) gives
`q>(8/3)2^(m/2)>1` for every member of this family. No linear-form
estimate or imported numerical cycle record is required for this
all-size exclusion.

Its rational minimum grows with `n`. The full affine map of `b_n`
has intercept `beta=C_(b_n)/2^A_0`. Every summand of `C_(b_n)`
is greater than `3^(n-1)/2`, while `2^A_0<2*3^n`. Therefore
`beta>n/12`. Every state immediately before either marker is the
output of the full `b_n` block on a positive input and exceeds `n/12`.
After a marker 3 or 4 it exceeds `n/64`. Every prefix of the lower
mechanical word has slope

```text
3^j/2^floor(jA_0/n) > 1/2,         0<=j<=n,
```

because `0<A_0-n log_2 3<1`. Its affine intercept is nonnegative.
Hence **every rational state of the full cycle exceeds `n/128`**.

The number of shortcut local minima is exactly
`2(A_0-n)+2`: each valuation-2 letter of the two mechanical blocks
and each marker contributes one last even-to-odd descent, followed by
an increasing odd shortcut step. It tends to infinity. This is a
shortcut count, not an odd-only count. Both the minimum and this
count eventually exceed any fixed numerical thresholds used by the
published cycle-record comparisons in the programme; this is not a
claim of novelty against all literature.

The family also separates the scoped existing block results. Unique
markers prevent any representation `u^k v^ell` with both exponents at
least two (C003). The coprime total and length prevent equal-total
block concatenations with more than one block (C002's equal-total
branch), and also prevent multiple rotations of a common base (C005).
The whole word is not mechanical. It cannot be an unbounded subfamily
of one fixed `u^k v` family from C001: both unique-marker distances
increase with `n`, whereas a fixed defect block containing both markers
would bound one such distance. These comparisons concern the stated
previous classes, not every possible consequence of their identities.

## 6. Actual cycles and limitations

The actual `q=359` cycle

```text
n=(209,493,919,779,337,685,1207,995),
w=(1,1,2,3,1,1,2,4),
C=15257,  D=26207=73*359,  g=73,
```

has a unit-amplitude two-defect rotation by four. Cutting at the
valuation 3 gives arcs `(1,1,2,4)` and `(1,1,2,3)`, both with
intercept 73. Thus (2) is exact here. This is not a mechanical word;
there are four different valuation letters. It demonstrates why
unit amplitude and two mismatches do not force `g=1` at arbitrary
separation.

The raw `q=5` cycle `(19,31,49)` has word `(1,1,3)`, with a
rotation differing twice at amplitude 2, `D=5,g=1`. The raw
`q=7` cycle `(5,11)` has word `(1,3)`, amplitude 2, `D=7,g=1`.
The actual `q=13` cycle `(283,431,653,493,373)` has word
`(1,1,2,2,2)`, with a unit-amplitude two-defect rotation,
`D=13,g=1`. Every bound here concerns their true reduced denominator
and allows these genuine cycles. There is no absorber convention or
extra `q<=L` restriction in this two-defect theorem.

The separate fixed-defect construction `1^t 2^(2t)` can have arbitrarily
large `g` while retaining exactly two rotation mismatches of amplitude
one. It therefore refutes a cancellation bound depending only on
mismatch count and amplitude. It does not refute (5)–(9), which retain
period and total valuation. Its detailed arithmetic belongs in the
companion obstruction note, rather than being assumed as a constant-g
lemma here.

## 7. Decision in seven fields

| Field | C011 two-defect assessment |
| --- | --- |
| Objects | Positive valuation words with a nontrivial rotation differing in exactly two entries; true reduced cycle denominator. |
| Structural gain | Two complementary arc intercepts bound cancellation uniformly; unused terminal valuations improve the amplitude cost by a square-root factor. |
| Translated unresolved gap | General words may have no two-defect rotation; finite-exception removal also needs quantified inputs beyond (7). |
| Worked example | The actual unit-amplitude `q=359` cycle has `g=73`, exactly recovered by both arc intercepts. |
| Known-cycle controls | Actual `q=5,7,13,359` examples retain their denominator and valuation clocks. |
| Cheapest meaningful next test | Audit explicit constants against independently verified integer-cycle bounds, and test how multiple mismatch arcs alter the cancellation bound. |
| Genuinely intermediate milestone | An all-size exclusion for an intrinsic sparse-rotation class, while arbitrary words without such a rotation remain outside its scope. |

The displayed family is an elementary all-size exclusion with growing
minimum and shortcut complexity. The general quantitative theorem is
uniform across varying words and periods. Neither conclusion supplies
the missing theorem for unrestricted nontrivial integer cycles.
