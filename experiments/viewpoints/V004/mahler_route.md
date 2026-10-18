# V004 — Positive binary sections close under ternary sections

**Status: written full-class derivation; the central statement and review
status are in [GLOBAL_RIGIDITY.md](GLOBAL_RIGIDITY.md).** The
argument below proves constancy of every finite-valued binary-automatic
coloring satisfying the stated Collatz identities. The minimal dependency
is now the published Cobham theorem: the independently audited elementary
finish in [kernel_route.md, §4](kernel_route.md) supersedes the need for
arithmetic-progression sufficiency. The original alternative using that
published sufficiency theorem is retained in §4 below. It does not assume that an
actual Collatz component indicator is automatic. It is not a convergence
proof, a formally verified proof, or a novelty claim.

The key refinement of [V003's kernel probe](../V003/kernel_probe.md) is to
retain every **positive-offset** binary section. That finite family closes
under both bases. The possible extra function arising from the zero-offset
ray is unnecessary for the argument.

## 1. Domain, clocks, and the full-class statement

Let C be any finite set and let h:positive integers→C satisfy

```
h(2n)=h(n)                 for every n>=1,
h(3n+1)=h(n)               for every positive odd n>1.          (1)
```

These are value equalities on the absorbed ordinary Collatz graph. At the
omitted odd source1, h(4)=h(1) follows from doubling twice. Thus the same
color equality can be used at source1, without changing the actual
absorbing dynamics.

Set h(0)=h(1) only to use the usual sequence domain n>=0. This changes at
most one sequence entry and does not alter automaticity. Define

```
B_(a,r)h(n)=h(2^a*n+r),    a>=0, 0<=r<2^a,
K={B_(a,r)h:a>=0, 0<=r<2^a}.
```

Binary automaticity means that K is finite. All state equalities below
are equalities of entire sequences on n>=0; no finite-prefix identification
is used. The section operators are

```
D_b g(n)=g(2n+b),           b=0,1,
T_j g(n)=g(3n+j),           j=0,1,2.
```

Their depths count digits of starting integers. They do not count
ordinary, shortcut, or odd-only Collatz arrows.

**Theorem.** Every h satisfying (1) with finite binary kernel K is
constant on the positive integers. With the prescribed extension, it is
also constant at0.

## 2. Elementary identities used by the closure proof

For every integer m>=0,

```
h(3m+1)=h(4m+1),                                     (2)
h(3m+2)=h(2m+1).                                     (3)
```

For (2), use the odd source4m+1, whose image is12m+4, and remove the
factor4. For (3), use the odd source2m+1, whose image is6m+4, and remove
the factor2. At m=0 both statements follow from h(2)=h(1), h(4)=h(1),
as appropriate; no undefined source0 is used.

For every positive odd u, apply (1) at3u, and then (2) at3u and4u:

```
h(3u)=h(9u+1)=h(12u+1)=h(16u+1).                    (4)
```

The source3u is at least3, so this application is within the original
guard. The intermediate equalities in (4) are color identities, not a
claim that those displayed integers are successive odd iterates.

## 3. A finite family closed under both bases

Define

```
K+={B_(a,r)h:a>=1, 0<r<2^a}.                         (5)
```

This is a nonempty finite subset of K: it contains b(n)=h(2n+1).
Different representations can define the same state; this causes no
problem, since sections of equal sequences are equal. A representation
with positive offset is enough for each argument below.

### 3.1 Binary closure

For g=B_(a,r)h in K+ and b=0,1,

```
D_b g=B_(a+1,2^a*b+r)h.
```

Its offset satisfies 0<2^a*b+r<2^(a+1), so D_b g belongs to K+.

### 3.2 Ternary closure when the affine offset is a ternary unit

Take g=B_(a,r)h in K+, j in{0,1,2}, and put c=2^a*j+r. Then

```
0<c<3*2^a,
T_j g(n)=h(3*2^a*n+c).                               (6)
```

Suppose 3 does not divide c. Choose v=1 when c=2 modulo3 and v=2 when
c=1 modulo3, and define t=(2^v*c-1)/3. The integer t is positive and
odd, and

```
0<t<2^(a+v).
```

Indeed 2^v*c-1 is positive, divisible by3, and strictly below
3*2^(a+v). At x=2^(a+v)*n+t we have the exact identity

```
3x+1=2^v*(3*2^a*n+c).
```

The source x is positive odd even at n=0. Apply (1), with the already
justified x=1 case when necessary, and remove the factor2^v. This gives

```
T_j g=B_(a+v,t)h in K+.                              (7)
```

The exponent v need not be the complete valuation of3x+1, since the
rightmost factor may be even. This proof requires only the displayed
color equalities, not a claimed odd-arrow clock.

### 3.3 Ternary closure when the affine offset is divisible by3

Suppose 3 divides c. Write t=c/3. Crucially,

```
0<t<2^a.
```

Write t=2^ell*u with u positive odd. Then 0<=ell<a, and

```
z=2^(a-ell)*n+u
```

is positive odd for every n>=0. Remove the factor2^ell and use (4):

```
T_j g(n)=h(3*(2^a*n+t))
        =h(3z)
        =h(16z+1)
        =h(2^(a-ell+4)*n+16u+1).                     (8)
```

This is again an admissible positive binary section, since

```
0<16u+1
 <=16*(2^(a-ell)-1)+1
 =2^(a-ell+4)-15
 <2^(a-ell+4).
```

Equations (7) and (8) prove T_j(K+)⊆K+ for every ternary digit j.
The c=0 case that formerly produced the extra function h(3n) is absent:
c=2^a*j+r is positive whenever r>0. No assertion that h or h(3n)
belongs to K+ is needed.

## 4. Full-class conclusion through Cobham and sufficiency

**Dependency update.** The elementary periodic-odd-section argument in
[kernel_route.md, §4](kernel_route.md) was independently audited after this
route was written. It removes the transient and the factors2 and3 from
the odd-section period, then forces constancy by a unit translation in
the remaining residue ring. Thus Monks's theorem is optional; the
following is a second finish, not an additional premise of the main proof.

Every member of K+ has both its binary and ternary kernels contained in
the same finite set K+. It is therefore automatic in both bases. Apply
Cobham's theorem to each color fiber: a sequence over a finite alphabet
automatic in multiplicatively independent bases2 and3 is eventually
periodic. The published theorem is stated as Theorem2.1 in
[Adamczewski–Bell, *A problem about Mahler functions*, §2](https://arxiv.org/html/1303.2019#S2).

In particular b(n)=h(2n+1) is eventually periodic. Thus there are
integers M>=1 and N>=0 such that b(n+M)=b(n) for every n>=N. Fix any
n0>=N. Then h is constant, with some color c0, on the entire progression

```
A={2*n0+1+2*M*k:k>=0}.                              (9)
```

Use the published arithmetic-progression sufficiency theorem: every
nonconstant arithmetic progression of positive integers meets every
Collatz orbit component, meaning that every positive integer merges with
some member of that progression. See
[K. M. Monks, *The sufficiency of arithmetic progressions for the 3x+1 Conjecture*, Theorem1.1 (2006)](https://www.researchgate.net/publication/238083063_The_sufficiency_of_arithmetic_progressions_for_the_3x_1_conjecture),
also explicitly recalled in the introduction of
[Monks–Monks–Monks–Monks, *Strongly sufficient sets and the distribution of arithmetic sequences in the 3x+1 graph*](https://arxiv.org/html/1204.3904v2).
The progression in (9) starts at its indicated positive term; no finite
initial segment has to be added.

For arbitrary x>=1, choose y in A with a common future iterate. Equation
(1), including its justified color extension at source1, makes h constant
along every ordinary or shortcut orbit. Hence h(x)=h(y)=c0. This proves
the theorem.

The sufficiency theorem may use unbounded, unequal shortcut clocks for
the two sources. The proof needs only existence of a common future;
it does not assert a uniform clock, odd-step count, or absorbing time.
If a raw path continues through1, its color remains h(1) because
1,2,4 have the same color, so the absorbed convention causes no issue.

## 5. The requested characteristic-zero Mahler formulation

The same closure supplies the missing analytic structure directly for
the positive sections. Fix one color and replace h by its0–1 indicator
f. Its positive-section family is a finite image of K+ and is closed
under the same operators. Enumerate its distinct states f1,...,fq and
write Fi(z)=sum_(n>=0)fi(n)z^n in Q[[z]]. There are maps beta_b and
tau_j on{1,...,q} such that the exact formal identities are

```
Fi(z)=F_(beta_0(i))(z^2)+z*F_(beta_1(i))(z^2),
Fi(z)=F_(tau_0(i))(z^3)+z*F_(tau_1(i))(z^3)
                           +z^2*F_(tau_2(i))(z^3).   (10)
```

Thus F(z)=A_2(z)F(z^2)=A_3(z)F(z^3) with polynomial matrices. No matrix
invertibility, roots-of-unity regularity, or assumed rank condition is
required.

For completeness, a scalar finite Mahler relation follows algebraically.
Fix k=2 or3 and a component i. Unroll its k-system to depth q. Each of
the q+1 functions Fi(z^(k^j)), j=0,...,q, is a polynomial row combination
of the q entries of F(z^(k^q)); for j=q the row is the ith coordinate
row. These q+1 rows are linearly dependent over Q(z). Clearing
denominators gives polynomials P0,...,Pq, not all zero, with

```
sum_(j=0)^q Pj(z)*Fi(z^(k^j))=0.                     (11)
```

If the first nonzero index is j0>0, split each coefficient polynomial
into its residue classes of exponents modulo k^j0. At least one resulting
coefficient identity is nontrivial; substituting w=z^(k^j0) in that
identity yields a relation with a nonzero coefficient on Fi(w). Thus
the standard scalar Mahler form is available even if a particular
row dependence initially omits Fi(z).

Adamczewski–Bell's Theorem1.1 over characteristic zero makes a series
simultaneously2- and3-Mahler rational. A rational series with finite-valued
coefficients is eventually periodic: beyond its initial terms its finite
linear recurrence determines each next value from a fixed-length tuple,
and only finitely many such tuples are possible. This gives the same
eventual periodicity of the odd section and the conclusion in §4.
[Source: *A problem about Mahler functions*, Theorem1.1 and §2](https://arxiv.org/html/1303.2019).

This is an alternative invocation of published rigidity, not an
independent proof of Cobham: Adamczewski–Bell's proof itself uses Cobham.
The analytic construction is supplied for every positive-section
indicator before constancy is established. We do not assume a ternary
equation for the original generating function at the outset.

## 6. Controls, dependencies, and remaining Collatz gap

- **No subclass restriction:** K+ contains every positive binary offset,
  with no bound on its depth. Its finiteness follows only from the full
  assumed binary automaticity; no synchronizing automaton, bounded state
  count, special digit statistic, or prescribed transition graph is used.
- **Additive controls:** for d=5 and61, the nonconstant automatic coloring
  1_(d divides n) is invariant under doubling and the absorbed3x+d map.
  The d=1 identity (2) fails for it at m=1,d=5 (arguments4,5), and at
  m=15,d=61 (arguments46,61). The closure proof cannot transfer unchanged.
  Arithmetic-progression sufficiency with arbitrary moduli also does not
  transfer: multiples of d retain their own divisibility color.
- **Scaling-only control:** the binary-automatic coloring of oddpart(n)
  modulo8 with colors{1,3} and{5,7} is invariant under multiplication by2
  and3 but not eventually periodic. It violates actual Collatz invariance
  at3→5. It therefore does not satisfy the affine hypotheses used in (2)
  and (4), and is no counterexample to this theorem.
- **Proof dependencies:** the elementary closure argument is written here.
  Cobham (or the stated Mahler theorem) is an imported published result,
  not formally replayed here. Arithmetic-progression sufficiency is used
  only by the optional finish in §4; the elementary finish needs no such
  theorem.
  The central proof and its independent review record distinguish these
  mathematical dependencies from the bounded arithmetic checks.
- **Convergence remains open:** if Collatz fails, its nonabsorbing-set
  indicator is a nonconstant invariant coloring, since1 is absorbing and
  its value differs from a nonabsorbing seed. This theorem would force
  that indicator to be nonautomatic. It neither supplies automaticity of
  the actual indicator nor excludes a nonautomatic bad set.

The previous V003 mixed-section obstruction was an obstruction to closing
the particular family K union{h(3n)} by its displayed argument. It was
not a counterexample to the positive-offset family (5). The present
closure is a structural proof, with no automaton catalogue or trajectory
experiment used to extrapolate the full-class statement.
