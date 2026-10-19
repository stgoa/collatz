# C012 — The complete defect-cut system and its forced denominator factors

**Status: written elementary theorem and exact infinite obstruction to
adjugate elimination.** This note derives the coupled system at an
arbitrary number of mismatches. It proves no unrestricted denominator
bound and does not refute estimates retaining the coupled arithmetic.
All cycles use the raw positive odd-only map, including at state 1.

## 1. Objects and compression at every defect

Let `w=(a_0,...,a_(m-1))` be a positive valuation word and let v be a
cyclic rotation of w. Put

```
A=sum a_i,     D=2^A-3^m>0,
C_w=sum_(j=0)^(m-1) 3^(m-1-j)2^(a_0+...+a_(j-1)),
g=gcd(C_w,D),  q=D/g.
```

Suppose w and v differ at exactly s positions. A nonzero mismatch count
cannot be 1 because the totals agree. Thus `s>=2`. A rotation fixing the
word has `s=0` and is outside the construction. Repeated words are allowed
when the selected rotation is nontrivial; primitivity is required only
for the explicit family in Section 6. In particular no claim discards
the fixed word `(2)` or its repetitions.

Cut both words just after every mismatch. In cyclic order this gives
paired blocks `(u_i,u'_i)`, `0<=i<s`, whose interiors agree and whose
last letters differ. Write

```
ell_i=length(u_i),  alpha_i=3^ell_i,
B_i=sum(u_i),      beta_i=2^B_i,
B'_i=sum(u'_i),    beta'_i=2^B'_i,
delta_i=B'_i-B_i != 0,   sum delta_i=0,
c_i=C_(u_i)=C_(u'_i).
```

The last equality is exact: a word intercept omits its last valuation.
The products of the two beta lists agree, so

```
product beta_i=product beta'_i=2^A,
product alpha_i=3^m.
```

Let X_i and Y_i be the full-word intercepts at the corresponding block
starts in w and v. Concatenation gives

```
beta_i X_(i+1)-alpha_i X_i=D c_i,
beta'_i Y_(i+1)-alpha_i Y_i=D c_i.                 (1)
```

The indices in (1) are cyclic. Since v is a rotation, each X_i and Y_i
is one of the full rotated intercepts, so g divides them all.

These cuts retain every full-cut difference divisibility. Inside a block,
the valuations agree until its last letter. If E_j is the difference of
the two full intercepts at an internal cut, the one-arrow recurrence is

```
2^a_j E_(j+1)=3 E_j.
```

For any modulus coprime to 6, divisibility at an internal cut is therefore
equivalent to divisibility at the block start. There is no additional
independent full-cut difference congruence hidden inside a matching run.

## 2. The exact s by s matrix

Let B have diagonal entries `-alpha_i` and cyclic superdiagonal entries
`beta_i`; define B' by replacing beta with beta'. Both determinants are
`(-1)^(s-1)D`. Define integer matrices

```
W=D B^(-1),    W'=D B'^(-1),    M=W'-W.            (2)
```

They are integer because `W=(-1)^(s-1)adj(B)` and likewise for W'.
Explicitly, the coefficient in row i of c at cyclic position `i+j` is

```
W_(i,i+j) = product_(h=0)^(j-1) beta_(i+h)
             * product_(h=j+1)^(s-1) alpha_(i+h),
                    0<=j<s,                     (3)
```

with empty products equal to 1. Replacing beta with beta' gives W'.
Equations (1) say

```
X=W c,     Y=W' c,     Y-X=M c.                   (4)
```

Thus `g | (M c)_i` is exactly the coupled system of all block-cut
differences, and hence of all full-cut differences. In particular the
unknown vector c must not be replaced by independent divisibilities of
its entries: C011 already gives actual counterexamples to that step.

## 3. Determinant theorem

**Theorem.** For every such pair,

```
|det M| = D^(s-2) product_i |beta'_i-beta_i|.       (5)
```

Every factor on the right is nonzero, so M is nonsingular over Q.

**Proof.** Put `H=B'-B`. It is a weighted cyclic permutation matrix with
nonzero weights `beta'_i-beta_i`. The inverse-difference identity gives

```
M = -D B'^(-1) H B^(-1).
```

Taking determinants and using `|det B|=|det B'|=D` gives (5). QED.

For two defects the exponent of D is zero, consistent with C011's two
separately divisible arcs. For every `s>=3`, multiplying the coupled
congruences by `adj(M)` yields only

```
g | det(M)c_i,
```

which is automatic because `g|D` and `D|det(M)`. This is a precise
failure of this adjugate elimination. It is not a failure theorem for
all integer combinations, for smaller minors, or for size estimates on
the remaining coupled expressions.

## 4. Every larger minor has the same contamination

**Theorem.** Every k by k minor of M is divisible by

```
D^max(k-2,0).                                     (6)
```

**Proof.** From `BW=D I`, consecutive rows satisfy

```
beta_i W_(i+1,*) = alpha_i W_(i,*) mod D.
```

Each beta is a unit modulo D. Choosing integer representatives of the
cumulative ratios gives integer column u and row v such that
`W=u v mod D`; one may take v to be the first row of W. Similarly
`W'=u'v' mod D`. Hence there is an integer matrix N with

```
M=D N+(u'v'-u v).                                 (7)
```

The second term has rank at most 2 over Q. Expand any minor by
multilinearity in its columns. A term with more than two columns from
that rank-two matrix vanishes. Every remaining term has at least k-2
columns from D N, proving (6). The assertion for `D=1` is immediate.
QED.

In particular every reduction of M modulo a prime dividing D has rank
at most 2, even when s is arbitrarily large. The two-dimensional bound
concerns the matrix acting on free block-intercept variables. The actual
rotation relation still constrains those variables; this calculation
does not discard that relation or infer a general impossibility result
from matrix rank alone.

## 5. Sharpness: unit defects give exactly two constraints

**Local Smith theorem.** Let p divide D, and suppose p divides none of
the numbers `beta'_i-beta_i`. Over the p-local integers, the Smith form
of M has two unit factors and s-2 factors associated to D:

```
diag(1,1,D,...,D).                                (8)
```

**Proof.** Modulo p, B and B' each have rank s-1: their cyclic recurrence
has one freely chosen starting coordinate and all coefficients are
units. Their adjugates have rank 1. Their right kernels are distinct,
since a common kernel vector would lie in the kernel of the invertible
matrix H. Their left kernels are distinct for the same reason.
Consequently W and W' are rank-one matrices with distinct column spaces
and distinct row spaces, and `W'-W` has rank exactly 2 modulo p.

Write `t=v_p(D)` and let `e_1<=...<=e_s` be the valuations of the Smith
factors of M. Rank 2 gives `e_1=e_2=0`. For `s>=3`, (6) for three by
three minors gives `e_3>=t`, and hence every later exponent is at least
t. Formula (5) gives total valuation `(s-2)t`; therefore every exponent
from the third onward equals t. The case s=2 follows directly from (5).
QED.

If every defect has unit amplitude, `delta_i=+1` or `-1`, then each
`beta'_i-beta_i` is a signed power of 2. Thus over `Z[1/6]` the Smith
form is exactly (8). There are no further nonunit factors away from 2
and 3, by (5).

For every divisor `g>1` of D, invertible row and column transformations
modulo g reduce `M c=0 mod g` to exactly two independent congruences on
the transformed c. The other s-2 rows have coefficient D and vanish
modulo g. This statement describes the complete difference matrix;
it supplies no bound on g from those two coupled congruences.

## 6. An infinite primitive actual-cycle obstruction

For integers `r>=2,t>=1`, consider

```
w_(r,t) = (1^t 2^(2t))^(r-1) 1^t 2^(3t),
m=(3r+1)t,   A=(5r+2)t.                           (9)
```

There are r runs of ones and r runs of twos. The unique maximal run of
twos of length 3t rules out every proper repetition. Under rotation by
one position, exactly the 2r run endpoints differ, all by one. Thus

```
s=2r,
2^A/3^m = ((32/27)^r * 4/3)^t > 1.
```

Each word therefore generates a primitive positive rational cycle and,
after reduction, an actual positive odd integer cycle at d=q. Indeed the
rotated intercepts divided by g are positive odd integers and satisfy
every raw arrow. A smaller state period would force a repeated exact
valuation word, contradicting the unique long run.

In this family the determinant is explicitly

```
|det M|=2^(A-r) D^(2r-2),                         (10)
```

because the minimum of the two beta exponents is B_i for each one-run
and B_i-1 for each two-run. Its Smith form over `Z[1/6]` is exactly
`diag(1,1,D,...,D)`. Both the mismatch count and the period can vary
without removing the forced factors.

The cancellation gcd can also be arbitrarily large at each fixed r.
For any positive M0 coprime to 6, choose t with
`2^t=3^t=1 mod M0`. All run lengths are multiples of t, and

```
C_(1^L)=3^L-2^L,     C_(2^L)=4^L-3^L.
```

Every run intercept and D is then divisible by M0. Concatenation gives
`M0|C_w`, hence `M0|g`. Such t exist by the finite unit groups modulo
M0, and may be chosen arbitrarily large. The matrix obstruction is
therefore present on primitive actual cycles with unbounded cancellation,
not just on formal block variables or on repeated fixed points.

This does **not** refute a relative estimate such as an exponential
saving for `g/2^A` in terms of `m/s`. The family proves failure of the
specified determinant elimination and of a constant-g bound; its
denominators remain free to grow.

### Small exact example

For `r=2,t=1`, the word is `(1,2,2,1,2,2,2)`, with

```
C=5095, D=q=1909, g=1,
states=(5095,8597,6925,5671,9461,7573,6157).
```

At the four run starts, `c=(1,7,1,37)` and the difference matrix is

```
M = [    0, 162,    0, 64 ]
    [-1024,   0, -648,  0 ]
    [    0, 256,    0, 54 ]
    [ -864,   0,-1024,  0 ].

det(M)=-3731743744=-2^10*1909^2.
```

This first example is mechanical and already lies in the known narrow
class; it is an arithmetic calibration, not a newly excluded family.
For `r=3,t=2` the same construction has `m=20,A=34`,
`C=30653364553,D=13693084783,g=7,q=1956154969`.

## 7. Scope and next decision

The known q5, q7 and q13 cycles remain valid. The two-defect result is
the s=2 case and loses none of its factors. C011's q97, q233 and q359
controls remain counterexamples to dividing individual plateau terms;
the present matrix retains their coupled sums. Every displayed formula
has a direct exact finite test, but the all-size assertions rest on the
written arguments above, not on a census.

| Required field | Outcome |
| --- | --- |
| Objects | Paired cyclic rotations, all mismatch cuts, common arc intercepts and the complete integer difference matrix. |
| Structural gain | Exact determinant, divisibility of every larger minor, and sharp Smith form for unit defects at arbitrary s. |
| Translated unresolved gap | The two surviving coupled arithmetic conditions still need a size estimate exploiting actual rotation compatibility. |
| Worked example | The explicit four-defect q1909 matrix above, with its exact determinant. |
| Known-cycle controls | C011's q97/q233/q359 coupled controls, raw q5/q7/q13, and the primitive family with arbitrary prescribed divisors of g. |
| Cheapest meaningful next test | Test a specific bound on the two coupled forms, preserving signed terms and factors; ordinary adjugate elimination is now ruled out. |
| Intermediate milestone | A uniform relative cancellation estimate at arbitrary s, sufficient to force mismatch complexity to grow in any hypothetical q1 cycle. This note does not achieve it. |

The obstruction sharpens C004's single-lattice warning for this concrete
proposed elimination. It is not a comparison win over published cycle
exclusions: no new positive q1 exclusion or larger admissible period is
proved here. A different estimate on the surviving arithmetic may still
be useful. The determinant argument treats the block intercepts as free
variables and does not exploit their additional overlap constraints from
being pieces of one word and its rotation. No arbitrary-method
impossibility or novelty claim is made.
