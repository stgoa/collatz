# A decreasing paired recurrence beyond the normalized return

2026-10-17. **Written arithmetic proof and finite certificates.** The rule
below is a partial construction with complete parameter domains. Its recursive
parameter decreases, and its accepted family has arbitrarily large recursive
depth. It resolves infinite subfamilies of R26's unbounded-return example.
It does not cover every complementary root or prove Collatz. No novelty,
human review, or formal verification is claimed.

Use the odd-only Syracuse map S, absorbing at1, and killed divergence
`div=I-P`. All currents below are finite integer currents with their signs
retained. Let nu and the canonical set B be as in
[R25](../bridge_normal_form/BRIDGE_NORMAL_FORM.md): B consists of1 modulo8
and complementary3-modulo4 roots.

## 1. The obstruction supplies a useful large comparison state

For a>=7 with a=7 modulo16 put

```
x=2^a-1,   N=12*2^(a-4),   q=(x-1)/2=2^(a-1)-1,
w=(3^(a-1)-1)/8,          f=3w=(3^a-3)/8.
```

Here N is a required-ray cutoff, q<N, and x is an actual weight1 R_N root
in `(9N/8,3N/2)`, with x=7 modulo12. It is in R23's complementary
branch. R26's normalized return is exactly f, already1 modulo8, and
f/x is unbounded along the family. Its next exact arrow is

```
S(f)=(3^(a+1)-1)/32,              v_2(3f+1)=2.        (1)
```

Indeed `v_2(3^(a+1)-1)=2+v_2(a+1)=5`, by elementary repeated squaring.
The binary information a=7 modulo16 fixes this arrow but does not fix
the subsequent normalized return.

The important comparison is supplied from below:

```
S^(a-1)(q)=w,             S^a(x)=4f+1.               (2)
```

For q the first a-2 arrows have valuation1 and the closing arrow has
valuation4, since `v_2(3^(a-1)-1)=3`. For x the first a-1 arrows have
valuation1 and the closing arrow has valuation2. This proves (2).
Thus a supplied absorption current through N certifies w by q's actual
path. No absorption hypothesis at the larger height w or f is needed.
This state w can be outside the elementary known set `{y:nu(y)<=N}`;
that set does not exhaust the states in the supplied lower-seed paths.

The next task is consequently to construct a finite signed bridge between
3w and w. The following rule applies to general w, not just the exponential
values in (2).

## 2. A complete paired run identity

Let w be any positive integer with w=3 modulo8, and put

```
h=v_2(3w-1).
```

This h is at least3. If it is even, write

```
h=2k+2,   k>=1,   C=(3w-1)/2^h odd,   z=3^k C.
```

Then the exact paired prefixes are

```
S^k(3w)=4z+1,              S^(k+1)(w)=2z+1.          (3)
```

To prove this, start with `3w=1+2^h C` and
`S(w)=1+2^(h-1) C`. Each of the next k arrows in both paths has
valuation2. The identity
`S(1+2^e c)=1+3*2^(e-2)c`, valid for odd c and e>=3,
gives terminal exponents2 and1. This proves all valuations in (3), not
only endpoint equalities.

### Terminal branch: z is canonical

If z belongs to B, the elementary bridge for2z+1 has minimum z.
For z=1 modulo8 this is the selected run of length2; for a complementary
`z=2^b t-1`, doubling changes its label to a selected run of length b+1.
In both cases put `A=v_2(2z+2)`. R23 gives

```
S^A(2z+1)=S^A(z).
```

Since S(4z+1)=S(z), equation (3) implies the explicit merger

```
S^(k+A)(3w)=S^(k+A+1)(w).                            (4)
```

Subtracting the two prescribed path currents constructs
`div J_w=delta_(3w)-delta_w`. Equivalently, append the sibling current
from4z+1 to z to the left prefix in (3), append R23's bridge from2z+1
to z to the right prefix, and subtract. There is no search past these
prescribed finite prefixes.

### Recursive branch: z=101 modulo128

In this branch write

```
z=4u+1,  u=25 modulo32,
w'=(3u+1)/4=(3z+1)/16=3 modulo8.                    (5)
```

The numerator for S(u) has valuation exactly2, so S(u)=w'. Equation (3)
and the sibling identity give

```
S^(k+1)(3w)=w'.
S^(k+1)(w)=8u+3,
S(8u+3)=12u+5,
S^2(8u+3)=9u+4=4(3w')+1,
S^3(8u+3)=S(3w').                                   (6)
```

The middle two arrows have valuations1 and2 respectively. In particular,
the current consisting of the left prefix of length k+1 minus the right
prefix of length k+4, plus the single row at3w', has divergence

```
delta_(3w)-delta_w + delta_(3w')-delta_w'.             (7)
```

Consequently, if J_(w') has divergence `delta_(3w')-delta_w'`, subtract
it from this explicit current to obtain J_w. The orientation reverses:
the recursive current must be **subtracted**, not added.

This recursion is well founded. In fact

```
z=3^k(3w-1)/4^(k+1) < (3/4)^(k+1) w < w,
0<w'=(3z+1)/16 < w/4.                               (8)
```

Each recursive transition stays in w=3 modulo8 and strictly decreases
the positive integer parameter. The arithmetic recognizer therefore always
terminates. It returns unresolved when h is odd or z is in neither the
terminal nor recursive class. That outcome proves no nonconvergence claim.

The same rule retains an exact merger clock. If the child satisfies
`S^l(3w')=S^(l+1)(w')`, (6) implies

```
S^(k+l+2)(3w)=S^(k+l+3)(w).                          (9)
```

Thus every accepted pair has a computed integer l with
`S^l(3w)=S^(l+1)(w)`. The current implementation retains the smaller
local pieces (7); the checker independently verifies the corresponding
complete path equality.

## 3. Complete cylinders with arbitrarily deep recursion

The simple terminal class is

```
w=59 modulo128.                                     (10)
```

It has h=4, k=1, and `z=(9w-3)/16=1 modulo8`, so its merger clock
is l=3. More generally, for every k>=1 the binary cylinder

```
3^(k+1)w = 3^k+2^(2k+2) modulo2^(2k+5)             (11)
```

has exactly h=2k+2 and z=1 modulo8. The extra bits enforce the exact
valuation and the canonical terminal condition.

For a complete family of recursive examples, fix k=1 in (5). Then

```
R(w)=(27w+7)/256,       fixed point 7/229,
229 R^r(w)-7=(27/256)^r(229w-7).                    (12)
```

For each r>=0 define c_r as the unique residue modulo `2^(8r+7)` with

```
27^r(229c_r-7) = 256^r(229*59-7) modulo2^(8r+7).    (13)
```

Every positive w in that cylinder has **exactly r recursive branches**
with k=1, followed by (10). This is a complete infinite parameter family.

Here are the integrality details. Equation (13) forces 229w-7 to be
divisible by256^r. Formula (12), using256=27 modulo229, shows that
all R^j(w), j<=r, are positive integers. For j<r they are3 modulo8;
the final value is59 modulo128. If v=R(w) is an odd integer3 modulo8,
then

```
3w-1=16(16v-1)/9,
z=(9w-3)/16=(16v-1)/3=101 modulo128.
```

Both quotients are integers by (12); the first has exact valuation4.
Thus each of the first r steps is precisely the recursive branch, with
no premature terminal case. At the final value (10) applies. Equations
(4) and (9) give the explicit clock

```
S^(3r+3)(3w)=S^(3r+4)(w).                           (14)
```

The domain is nonempty for every r. For a convenient integer witness,
choose a positive v satisfying

```
v=59 modulo128,     v=7/229 modulo27^r,
```

by CRT, then apply the inverse `(256v-7)/27` exactly r times. Each
division is integral: the same fixed-point formula reduces the required
power of27 by one. This yields the stored tests through r=64 without
constructing the much larger exponential seeds below.

## 4. Every recursive depth occurs in R26's actual obstruction family

For a=7 modulo16, the map `w=(3^(a-1)-1)/8` runs through every residue
3 modulo8 modulo any fixed power of2 as a runs through a suitable binary
exponent class. More precisely, for M>=3 and c=3 modulo8 there is a
unique a=7 modulo16 modulo `2^(M+1)` such that

```
3^(a-1)=1+8c modulo2^(M+3).                          (15)
```

This follows by elementary lifting. Start with a-1=6 modulo16; at each
stage exactly one of b and b+2^j fixes the next bit, because
`3^(2^j)=1+2^(j+2) modulo2^(j+3)` for j>=1. It proves existence,
uniqueness, and an executable finite algorithm; no unproved discrete-log
or prime-distribution assertion is used.

Apply (15) to (13), M=8r+7. This gives an explicit exponent residue
a_r modulo `2^(8r+8)` for every r>=0. The first values are

| r | a_r | period |
|---|---:|---:|
| 0 | 199 | 256 |
| 1 | 2887 | 65536 |
| 2 | 7768903 | 16777216 |
| 3 | 938904391 | 4294967296 |
| 4 | 192064949063 | 1099511627776 |

For **every** a=a_r modulo the displayed period, a>=7, equations (2)
and (14) prove the same-clock merger

```
S^(a+3r+3)(2^a-1)=S^(a+3r+3)(2^(a-1)-1).           (16)
```

The right seed is below N. Along each such infinite progression the old
normalized return f/x still tends to infinity, yet the supplied lower-seed
path and this explicit bridge certify x. This resolves those unbounded
returns by an actual common tail, without an assumed larger cutoff.

A second example uses the variable k version: the cylinder

```
a=39 modulo2^20                                     (17)
```

has the word k=3 recursively, then k=1 terminally. Indeed its w satisfies
`243w+175=59*4096 modulo2^19`, so the first child
`w'=(243w+175)/4096` is59 modulo128. The same integrality check as above
gives h=8, z=101 modulo128 in the first branch. Equation (9) gives l=8,
and the original two seeds merge at time a+8. The current receipt uses
the smallest positive exponent a=39 as its actual conversion example.

The elementary known-set test is not being changed by a guessed density.
The new information is the exact pair relation and the already supplied
path from q to w. The rules leave, for example, a=7 and a=23 unresolved.
They establish no coverage of all remaining R26 roots.

## 5. Current construction, signs, and supplied absorption

Let D_x be R26's explicit current with divergence `delta_x-delta_f`,
let H_(q,w) be the path in (2), and let J_w be the accepted paired current.
Then

```
B_x=D_x+J_w-H_(q,w),
div B_x=delta_x-delta_q.                             (18)
```

Given a finite exact input H_q with divergence delta_q, the current
`B_x+H_q` has divergence delta_x. No unseen future is exposed. A signed
input is sufficient: on the graph of the nonzero rows of this summed
finite current, a component disjoint from the absorber has divergence
sum zero. Since the source is nonnegative and equals delta_x, the x
component must contain1. A finite functional graph component containing1
has an actual forward path from every vertex to1. Following these existing
edges extracts a nonnegative integer absorption current. This argument
does not assume global cycle absence.

For any coefficient c>=1 multiply the entire construction and the
lower-seed input by c. A source coefficient is never silently replaced
by1, and distinct roots may reuse a proved lower-seed path as a proof
input. This is not an assertion about joint capacity inside an annulus.

For a=39 the actual values are

```
N=412316860416,
x=549755813887,
q=274877906943,
w=168856464709124011,
f=506569394127372033.
```

The finite demonstration discovers only the path from q, with a stated
cap of5000 odd steps. It then supplies that exact path to (18), and extracts
the current stored in `mersenne_39_current.csv` using only the nonzero
rows of the summed supplied and explicit currents. The separate arithmetic
constructor never performs an unbounded absorption search.

## 6. Reproduction and scope

```
python3 experiments/residual_progress/second_return/check_paired_return.py
```

The default checker is read-only. `--write-receipt` regenerates the receipt
and the small actual current. It checks4096 w values,72 complete terminal
cylinders,56 recursive integer cases through depth64,65 exponent lifts,
eight actual Mersenne bridges, and the supplied-current conversion.
Every tested accepted current has its exact signed divergence checked;
merger clocks are independently checked with ordinary Syracuse prefixes.

The accepted pair recursion has a proved decreasing parameter. This is a
positive partial construction, not merely a finite density observation.
Its remaining obligation is also precise: handle the odd-h branch and
the noncanonical z classes other than101 modulo128, or find a separate
finite bridge for them. The present written proof does neither.
