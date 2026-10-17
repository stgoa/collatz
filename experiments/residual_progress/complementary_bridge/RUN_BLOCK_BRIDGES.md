# Complete run-block bridges for the complementary family

2026-10-17. **Written arithmetic construction and exact finite checks.**
Absorption through the stated lower cutoff is supplied. This is a partial
constructor with an explicit remaining profile; universal closure is open.
No novelty, human review, or formal verification is claimed.

## 1. The entire complementary parameter domain

Use odd-only Syracuse S, absorbing at1, and killed divergence div=I-P.
Every complementary R23 root is uniquely

```
x=2^a t-1,  a>=2,  t odd,  t=-3^a modulo4.
d=v_2(3^(a-1)t-1)>=2,     w=(3^(a-1)t-1)/2^d odd.
```

R23 gives the exact first run

```
S^a(x)=3*2^(d-1)w+1.                                  (1)
```

When C,w are positive odd and e>=3,

```
S(C*2^e*w+1)=3C*2^(e-2)*w+1                           (2)
```

has valuation exactly2: its numerator is
`4(3C*2^(e-2)w+1)`, with an odd parenthesis. Thus (2) consumes a whole
run, without any unknown future search. It yields two complete branches:

**Odd d>=3.** Put b=(d-1)/2 and z=3^b w. After (d-3)/2 further arrows,
the state is4z+1; one more arrow coalesces with z. Therefore

```
S^(a+(d-1)/2)(x)=S(z),
z=3^((d-1)/2)*(3^(a-1)t-1)/2^d.                       (3)
```

**Even d>=2.** Put b=d/2 and r=2*3^b w+1. After d/2-1 further arrows,

```
S^(a+d/2-1)(x)=r,
r=2*3^(d/2)*(3^(a-1)t-1)/2^d+1,      r=3 modulo4.     (4)
```

These statements exhaust all complementary roots. They use unbounded run
lengths and are not a list of fixed finite words. The total additional
prefix length is computed directly from a,d. In the odd branch subtract
the single arrow z->S(z) from the x prefix; in the even branch use the x
prefix alone. In either case the resulting finite integer current D_x has

```
div D_x=delta_x-delta_f(x),                            (5)
```

where f(x)=z or r respectively. Current rows at1 are omitted, and repeated
rows retain their exact multiplicities. The common state in (3) need not
be below the known cutoff.

## 2. Exact shrinking conditions and the universal local constructor

For either branch set `b=floor(d/2)`, C=3^b and A=C*3^(a-1).
The exact conditions for f(x)<x are

```
odd d:  (2^(a+d)-A)t > 2^d-C,
even d: (2^(a+d)-2A)t > 2^(d+1)-2C.                  (6)
```

There is no assumption that these inequalities always hold. For example,
all odd-d branches with a<=5 have f(x)<x: for a=5,d=3 the positive
coefficient on the left is13 and the right side5; reducing a or increasing
odd d by2 preserves the inequality for every t>=1. Equivalently one can
check `(2^a-1)2^d>(3^(a-1)-1)3^b` in these cases. Larger a are governed
by (6), not an extrapolation of those four values.

For a supplied exact U_N current, only the stronger **known-cutoff test**
`f(x)<=N` is used. Here8|N,N>=8, and both f(x) and x are odd. The test is
equivalent to x<H_(a,d)(N), where

```
odd d:  H=(2^(a+d)N+2^a C)/A-1,
even d: H=(2^(a+d)(N-1)+2^(a+1)C)/(2A)-1.             (7)
```

Strict and non-strict target tests coincide because N is even. The boundary
in (7) cannot equal an actual cylinder seed whose target equals N.

Let V_N be the full R23 complementary residual restricted to f(x)<N,
retaining its coefficients1 or2. Put

```
Q_N=sum_x V_N(x) delta_f(x),       J_bridge=sum_x V_N(x) D_x.
```

Extract from the supplied U_N graph the actual nonnegative path current
H_Q for Q_N. Then

```
T_N=J_bridge+H_Q,        div T_N=V_N.                  (8)
```

T_N is nonnegative. In the odd branch replace the first arrow of the
known target path by the explicit x prefix; in the even branch prepend
the x prefix to the target path. This constructs an actual absorption
path, exposing no unknown future. A finite signed exact input for U_N is
also sufficient: its finite nonzero-row graph supplies absorbing paths by
the component argument already proved in R20/R23.

If the previous identity is `Pi_N=div J-R'_N`, the new one is

```
Pi_N=div(J-T_N)-(R'_N-V_N).                           (9)
```

Every weight2 root is removed with weight2. If distinct roots use the same
known target, add their target multiplicities; absorption paths are reusable
proof inputs. No annular source capacity is being spent in this construction.

## 3. Exact cylinders and finite count for every cutoff

For each a,d>=2, the exact valuation condition is

```
t=3^(1-a)*(1+2^d) modulo2^(d+1),
x=2^a t-1 modulo2^(a+d+1).                            (10)
```

The inverse of3 is taken modulo the displayed power of2. This includes
the extra exact-valuation bit. These cylinders are disjoint and partition
the entire complementary family: a is v_2(x+1), then d is uniquely fixed.

Intersect (10) by CRT with each R17 weighted interval/class:

```
(N,3N/2),       residue3 modulo12,       weight1;
(9N/8,3N/2),    residue7 modulo12,       weight1;
(N,9N/8),       residue7 modulo36,       weight2;
(N,9N/8),       residue19 modulo36,      weight2.
```

In each row replace the upper endpoint by its minimum with H_(a,d)(N),
and count the intersection using

```
C(L,H;r,m)=ceil((H-r)/m)-floor((L-r)/m)-1,
```

or zero when H<=L. For binary residue b modulo p, p=2^(a+d+1), and
the row residue r modulo m, the combined period is p(m/4) and its residue
is `b+p*((r-b)*p^(-1) modulo(m/4))`, taken modulo that period. Both
original classes are3 modulo4, so this is precisely the CRT intersection.

There are only finitely many relevant pairs: with
`A_N=floor(log2(3N/2))`, a<=A_N and

```
d<=floor(log2(3^(a-1)*floor((3N/2)/2^a)-1)).
```

In particular a+d<3A_N. Thus the formula uses O(log^2 N) exact arithmetic
counts and no orbit searches. `mass_formula` implements this exact sum;
`selected_profile` independently evaluates every actual weighted root.

## 4. Proved leading coefficient, not a finite-density extrapolation

Write the leading slope of f relative to x as

```
L_(a,d)=3^(a-1+(d-1)/2)/2^(a+d)             (d odd),
L_(a,d)=2*3^(a-1+d/2)/2^(a+d)               (d even).
```

Define the nonnegative continuous width function

```
g(h)=(7/9)*max(0,min(9/8,h)-1)
    +(2/3)*max(0,min(3/2,h)-9/8).
```

The factors7/9 and2/3 retain the complete R_N weights and odd-modulus
conditions in the lower and upper portions of the shell. Then

```
alpha=sum_(a,d>=2) g(1/L_(a,d))/2^(a+d+1),
|V_N|=alpha*N+O(log^2 N).                              (11)
```

This is an exact convergent series with a certified rational enclosure.
For K>=4 let alpha_K restrict a+d<=K. Since0<=g<=25/72,

```
alpha_K <= alpha <= alpha_K+(25/72)*(K-1)/2^(K+1).     (12)
```

The tail identity follows by summing `(n-3)/2^(n+1)` over n>K.
At K=64 this gives alpha approximately0.0150802551420555, and

```
|R'_N-V_N|=(25/576-alpha)*N+O(log^2 N),
25/576-alpha approximately0.0283225226357223.          (13)
```

The exact rational bounds, rather than rounded decimals, appear in the
receipt. Roughly34.7449% of the preceding complementary leading mass is
certified by this complete two-run rule. This percentage is a one-pass
conclusion, not an iterable contraction.

For completeness, an explicit error bound for (11) is available. Put
K=3A_N. For odd d, the endpoint H is `N/L+beta` with |beta|<=1.
For even d it is `(N-1)/L+rho-1`, where `0<rho=2^a/3^(a-1)<=4/3`.
If L<=1/2 this endpoint and its limiting endpoint both exceed3N/2 for
N>=8; otherwise the shift beta has magnitude<3. Each weighted progression
therefore differs from its leading interval-length count by at most its
weight times `(1+3/p)`, p>=32. Summing the four weights gives a bound<7
per pair. There are `(K-3)(K-2)/2` pairs a+d<=K. No actual seed belongs
to a pair outside this range, and the omitted leading tail times N is<1.
Consequently

```
abs(|V_N|-alpha*N) <= 7*(K-3)*(K-2)/2+1.              (14)
```

Combining this with R23's error at most6A_N proves the stated remainder
bound in (13). These are uniform integer-count statements derived from
the exact cylinders, rather than an extrapolation of scans with growing
bit depth.

## 5. The full rule: normalize the return before testing its height

The preceding alpha is a useful exact baseline. The actual constructor
uses every available elementary bridge before applying the cutoff test.
Let nu be the canonical normal form from
[the elementary-bridge proof](../bridge_normal_form/BRIDGE_NORMAL_FORM.md):
strip `F(y)=4y+1` while the current state is5 modulo8, then halve once
by R23 if the resulting root is selected. Its canonical outputs are1
modulo8 or complementary3 modulo4. The supplied normal-form module
constructs an exact finite current with divergence `delta_y-delta_nu(y)`.

Replace f(x) in (5)-(9) by

```
f_star(x)=nu(f(x)).
```

Add the normal-form bridge to D_x. The only absorption assumption is now
`f_star(x)<N`; no assumption about the unnormalized f(x) is needed.
The combined bridge may be signed. After adding the known current for
its canonical targets, its divergence is the nonnegative full-weight
removed source. The finite component lemma therefore extracts an actual
nonnegative current on those already specified edges. Target1 is killed
and needs no input current. This is the implemented `certify_normalized`.

For instance at N=168 the actual complementary root187 has weight2,
a=2,d=2,w=35 and raw return211. Its selected normal form is105<N.
The explicit prefixes are187->281->211, then211->317->119 and
105->79->119. Thus the known path from105 supplies all two units at187,
even though211>N. The stored current certifies exactly2 delta_187.

### Exact count through canonical targets

Every elementary bridge class has exactly the two rays

```
F^k(q), F^k(2q+1),          q canonical, k>=0.
```

In a fixed (a,d) cylinder write `x=x0+Pj`, P=2^(a+d+1), and
`f(x)=f0+Gj`, with

```
G=gA,  A=3^(a-1+floor(d/2)),  g=2 for odd d, g=4 for even d.
```

A normal-form stratum has `f=sq+o`, where

```
(s,o)=(4^k,(4^k-1)/3)                  for F^k(q),
(s,o)=(2*4^k,(4^(k+1)-1)/3)            for F^k(2q+1).
```

For a weighted original row `L<x<H`, `x=r modulo4m`, m=3 or9,
the exact canonical-target interval is

```
(G(L-x0)/P+f0-o)/s < q <
min(N,(G(H-x0)/P+f0-o)/s).
```

Its odd congruence is

```
q = [A(r-x0)-(P/g)(o-f0)] * [(P/g)s]^(-1) modulo A*m. (15)
```

All factors being inverted are powers of2, so the inverse exists.
This simultaneously enforces integrality of j and the original odd-modulus
source class. Binary parity is automatic for odd d. For even d only k=0
can occur, since f=3 modulo4; on the nonpartner ray q=f must also be3
modulo4. Count it by subtracting canonical1-modulo8 targets. On the
partner ray f=2q+1, all canonical odd q are admissible.

The normal-form `canonical_count` counts canonical q through any integer
bound in any fixed odd progression exactly, in O(log N) terms. Evaluate
it at the floor of the lower endpoint and one below the ceiling of the
upper endpoint, with the indicated1-modulo8 subtraction. The endpoints
and weights remain exact. There are O(log^2 N) run cylinders, O(log N)
possible F-depths, and O(log N) canonical classes per count. Consequently
the full `normalized_mass_formula` uses O(log^4 N) elementary arithmetic
terms. It includes every normalization depth and every parameter class.

### A rigorous leading coefficient for the full normalized rule

Within each (a,d) cylinder, w advances by an odd multiple of2, so its
remaining binary digits, and those of u=3^floor(d/2)w, range uniformly
over odd residue classes. Fixing one of the original modulo3/9 source
classes preserves this fact by CRT. The canonical normal-form proof gives
the following exact asymptotic binary densities for odd u:

```
u=F^k(q):       probability (1/2)*4^(-k), nu(u)~u/4^k;
u=F^k(2q+1):    probability (1/4)*4^(-k), nu(u)~u/(2*4^k).
```

These statements describe counting proportions, not independent random
steps. For even d the return is2u+1: it halves precisely when u is
canonical, a half of odd u; otherwise it is already canonical. Hence
define, with the same g and L as Section4,

```
h_(a,d) = [g(1/L)+g(2/L)]/2                         (d even),
h_(a,d) = sum_(k>=0) [g(4^k/L)/2+g(2*4^k/L)/4]/4^k (d odd),
beta = sum_(a,d>=2) h_(a,d)/2^(a+d+1).               (16)
```

The inner sum is exactly finite: once4^k/L>=3/2, both g values equal
25/72, and the remaining geometric tail equals `(25/72)*4^(-k)`.
Also0<=h<=25/72, so truncating a+d<=K has the same rigorous remainder
bound as (12). At K=64 the exact rational enclosure gives

```
beta approximately0.02399251818395744,
25/576-beta approximately0.01941025959382034.         (17)
```

Let V_star,N retain every complementary root with f_star(x)<N, at its
full original coefficient. Then uniformly over8|N,

```
|V_star,N|=beta*N+O(log^4 N),
|R'_N-V_star,N|=(25/576-beta)*N+O(log^4 N).           (18)
```

Here is the counting justification, including growing moduli. For fixed
odd modulus m and residue, the canonical count differs from its leading
length/(4m) by O(log N), uniformly in m, when targets are bounded by N.
The difference of endpoint counts has the same order. The1-modulo8
subtraction has bounded error. Each normal-form stratum in (15) therefore
has O(log N) integer-count error. Its affine endpoint offset is uniformly
bounded whenever it can intersect the normalized target interval: the
effective slope L/s>=2 makes both its actual and limiting intervals empty
for N>=8; for L/s<2 the offset is bounded in magnitude by4. Thus replacing
its interval by the leading linear one adds a bounded error as well.

Truncate a+d and k at3A_N. This includes all actual roots and normalization
depths, since raw returns are below2^(2A_N+1). The omitted leading tails
contribute O(1) after multiplication by N: use (12) for a+d and the
geometric4^(-k) tail for normalization. There are O(log^3 N) included
strata. Summing their uniform O(log N) errors proves (18). This supplies
a uniform count proof; it does not exchange an unproved limit with a scan.

The normalized full rule removes about55.2788% of the preceding R23
complementary leading mass. Its own remaining profile is explicit and
must still be solved; neither this proportion nor (18) may be iterated
without a new closure theorem.

## 6. Why these complete bridges do not close the family

The target can grow without bound relative to the starting root. For every
`a=3 modulo4`, a>=7, take

```
x=2^a-1,        N=12*2^(a-4).
```

This is a required-ray cutoff, and x is an actual weight1 complementary
root in `(9N/8,3N/2)`. Since a-1=2 modulo4, elementary repeated squaring
gives `v_2(3^(a-1)-1)=3`. Hence the odd-d target is

```
f(x)=(3^a-3)/8,
f(x)/x -> infinity.
```

No universal height descent or known-cutoff return follows from the block
formula. This is an infinite parameterized failure of the whole rule.

It also survives the strengthened normalization: restrict further to
a=7 modulo16. Then `3^a=11 modulo64`, so `(3^a-3)/8=1 modulo8` is
already canonical. Thus f_star(x)=f(x) has the same unbounded height ratio.

Even ranking only the block labels cannot repair the recurrence:

```
27: (a,d)=(2,2)  ->31: (a,d)=(5,4) ->91: (a,d)=(2,2).
```

Both steps use the actual even-d return (4), and both increase height.
Both targets31 and91 are complementary and already canonical, so the
same two transitions occur under f_star.
Thus there is no strictly decreasing function of (a,d) for every such
transition. Nor can a lexicographic potential with a label rank first and
height second decrease on every transition: these two arrows would require
opposite strict inequalities between the same two label ranks. This rules
out that particular termination strategy; it does not rule out a potential
with additional information or later unequal-time mergers.

The next obligation is precisely the residual branches whose f_star(x)>N,
possibly after processing known smaller targets in a broader finite graph.
The construction presently leaves them unchanged. It never treats a merely
smaller-than-x target as already absorbed when only U_N was supplied.

## 7. Reproduction

```
python3 experiments/residual_progress/complementary_bridge/check_run_bridge.py
```

The default runner is read-only; `--write-receipt` regenerates the receipt
and small stored current. It checks both complete arithmetic branches,
exact cylinders, weighted floor counts, rational series bounds, and actual
supplied-current conversions. Finite input discovery is capped at1000
odd steps per seed; it is evidence for those inputs only. The constructor
itself follows only the fixed prefixes specified by a,d and supplied paths.
