# V004 — Global rigidity of finite-state Collatz invariants

**Status: written proof, 2026-10-18; independent agent review.** The proof
covers arbitrary finite automata. It imports the classical finite-kernel
characterization of automaticity and Cobham's theorem. It has not been
formally verified or human peer-reviewed; novelty is undetermined. It does
not establish Collatz convergence.

## 1. The theorem and its dynamical meaning

**Theorem.** Let C be a finite set and let `h:N_{>0}->C` be binary automatic.
Assume

```
h(2n)=h(n)       for every n>=1,
h(3n+1)=h(n)     for every positive odd n>1.              (1)
```

Then h is constant. There is no bound on the number of automaton states,
no restriction to a digit statistic, and no extra ternary-automaticity
hypothesis.

Here binary automatic means that a fixed finite automaton, with an output
attached to each state, returns h(n) when it reads the binary expansion of n.
Leading-zero and zero-input conventions can be accommodated by finitely
many additional states. Equivalently, after setting `h(0)=h(1)`, the family

```
K_2(h)={n -> h(2^a*n+r): a>=0, 0<=r<2^a},   n>=0
```

is finite. A change at the single input0 preserves automaticity.

These color equations express invariance on the positive-integer Collatz
graph with1 absorbing. They also encode the odd-only Syracuse convention:
on odd inputs, doubling invariance removes the full power of2 from3n+1.
Conversely, a binary-automatic odd coloring preserved by Syracuse extends
to all positive integers by `h(n)=h(oddpart(n))`; deleting trailing binary
zeros can be handled by a finite automaton. Thus the theorem covers such
odd-only finite-state colorings too. No equality of orbit clocks is claimed.

The absent equation at source1 follows as a color equality from
`h(4)=h(2)=h(1)`. We use that equality without adding an outgoing dynamical
arrow at the absorber.

## 2. Elementary identities

For every m>=0, applying (1) at4m+1 and2m+1 and removing powers of2 gives

```
h(3m+1)=h(4m+1),
h(3m+2)=h(2m+1).                                      (2)
```

The cases with source1 use the justified color equality above. For every
positive odd u, (1) at3u and the first identity in (2), twice, give

```
h(3u)=h(9u+1)=h(12u+1)=h(16u+1).                     (3)
```

Also, for positive odd x,

```
h(4x+1)=h(3x+1)=h(x).                                (4)
```

Every argument here is a positive integer. There is no appeal to a
convergent orbit or to the existence of a common absorbing time.

## 3. Retain the positive-offset sections

Consider the finite subfamily

```
K_+={n -> h(2^a*n+r): a>=1, 0<r<2^a},   n>=0.          (5)
```

The family contains the odd section `b(n)=h(2n+1)`. It need not contain h.
Taking a binary section with digit j=0 or1 replaces (a,r) by
`(a+1,r+2^a*j)`, so K_+ is closed under binary sections.

We prove it is also closed under every ternary section. Fix (a,r) as in
(5), j in{0,1,2}, and put `c=2^a*j+r`. Then

```
0<c<3*2^a,
h(2^a*(3n+j)+r)=h(3*2^a*n+c).                         (6)
```

### Case A: 3 does not divide c

Take v=1 if c=2 mod3 and v=2 if c=1 mod3. Then

```
t=(2^v*c-1)/3
```

is an odd positive integer with `t<2^(a+v)`. For
`x=2^(a+v)*n+t`, we have `3x+1=2^v*(3*2^a*n+c)`.
Using (1), including its justified color case at1, yields

```
h(3*2^a*n+c)=h(2^(a+v)*n+t),                          (7)
```

which belongs to K_+. The positivity at the lower endpoint is explicit:
c>=2 when v=1, and c>=1 when v=2; in both cases t>=1.

### Case B: 3 divides c

Write `t=c/3=2^ell*u` with u positive odd. Since `0<t<2^a`, we have
ell<a. Put `s=a-ell>=1`; then `0<u<2^s`. Doubling invariance and (3)
give

```
h(3*2^a*n+c)
 = h(3*(2^s*n+u))
 = h(2^(s+4)*n+16u+1).                               (8)
```

The new offset is positive and satisfies
`16u+1<=2^(s+4)-15<2^(s+4)`. The argument2^s*n+u is positive odd,
including at n=0. Thus (8) also belongs to K_+.

This proves full ternary closure of K_+. Repeated sections cannot escape
the same finite family. The exceptional c=0 term that introduced h(3n)
in V003 is absent because r>0. We do not have to close the larger family
containing the zero-offset states before proceeding.

For example, the two cases include the all-n identities

```
h(12n+5)=h(8n+3),
h(12n+3)=h(64n+17),       n>=0.
```

## 4. The published input

Every member of K_+ has finite binary and ternary kernels, both contained
in K_+. The finite-kernel characterization makes it automatic in bases2
and3. Cobham's theorem makes each of its color fibers eventually periodic,
since2 and3 are multiplicatively independent. There are only finitely many
colors, so a common period and cutoff exist. In particular b(n)=h(2n+1)
is eventually periodic.

The precise published statements used are Theorems2.1 (Cobham) and7.1
(finite-kernel characterization) in
[Adamczewski–Bell, *A problem about Mahler functions*](https://arxiv.org/html/1303.2019).
They are external mathematical inputs, not theorems formally replayed here.
The standard kernel has offsets `0<=r<k^a`; the displayed Definition7.1
in that source has an apparent offset-range typo, which we do not adopt.

## 5. Elementary finish from periodicity on odd inputs

By (4), b satisfies `b(4n+2)=b(n)` for every n>=0. Let M be an eventual
period, write `M=2^e*L` with L odd, and define G(n)=4n+2. For any n>=0,
choose k so that G^k(n) is past the eventual cutoff and2^e divides4^k.
The two indices G^k(n+L) and G^k(n) differ by4^k*L, a multiple of M.
Therefore

```
b(n+L)=b(G^k(n+L))=b(G^k(n))=b(n).                    (9)
```

L is a global period, including all originally exceptional inputs.
Because L is odd, any two odd positive integers congruent modulo L
differ by a multiple of2L. Equation (9) consequently defines a coloring
q on Z/LZ with `h(x)=q(x modL)` for every positive odd x.

Every residue has arbitrarily large positive odd representatives. Equations
(3) and (4), applied to such representatives, show on every residue that

```
q(4x+1)=q(x),
q(3x)=q(16x+1)=q(4x).                                (10)
```

The final equality uses the first relation at residue4x; it does not
require4x itself to be an odd positive representative.

Since4 is invertible modulo L, let H(x)=3*4^(-1)*x. The second relation
in (10) is q(H(x))=q(x). Write `L=3^e3*m`, with gcd(m,6)=1. If x=y
modulo m, then H^e3(x)=H^e3(y) modulo L: the factor3^e3 kills their
difference on the3-primary part, and their difference was already0
modulo m. H-invariance implies q(x)=q(y). Thus q factors through m,
and (10) descends to that quotient.

If m=1, q is constant. Otherwise on Z/mZ both H and J(x)=4x+1 are
invertible and preserve q. Their compositions satisfy

```
H(J(x))=3x+3/4,
J(H(x))=3x+1.
```

Both values have color q(x). As3 is invertible, `y=3x+3/4` ranges over
every residue. Hence `q(y)=q(y+1/4)` for every y. The unit1/4 generates
the additive group Z/mZ, forcing q constant. Consequently h is constant
on odd positive integers, and doubling invariance makes h constant on
all positive integers. This proves the theorem.

## 6. What this contributes toward Collatz

Any subset A whose membership is preserved across every Collatz arrow
has an invariant indicator. If A is binary recognizable, the theorem
forces A to be empty or all positive integers. Thus, if the nonabsorbing
set B were nonempty, its indicator would have an infinite binary kernel.
The same holds for any nonempty proper union of orbit components.

We have not proved that B has a finite kernel, an automatic description,
a bounded complexity growth rate, or any other regularity that would make
this exclusion imply B is empty. The theorem excludes a whole description
class for a hypothetical obstruction. It supplies no convergence bound,
universal current, or absence of an irregular divergent component.

The statements “B is binary automatic” and “Collatz converges” are now
equivalent, given this theorem: convergence makes B empty, while
automaticity would force its invariant indicator to be the constant0
because1 is absorbed. Merely asking for automaticity of B therefore
reinstates the full problem; it is not an intermediate next milestone.

## 7. Controls and verification scope

For d=5 or61, `h_d(n)=1_(d divides n)` is a nonconstant binary-automatic
coloring preserved by doubling and by3n+d at odd sources. Division by2
preserves divisibility by either odd d, and gcd(3,d)=1. The absorber is1.
Actual odd cycles include5→5 for d=5 and61→61 for d=61, disjoint from1.
Both demonstrate a surviving component distinction.

The crucial d1 identity (3) fails for h_d at u=d: h_d(3d)=1 and
h_d(16d+1)=0. The corresponding general-d affine identities contain d;
their commutator translates by d/4, which is0 modulo d and cannot force
constancy. This exercises the named mechanism rather than merely replaying
an unrelated cycle. Cycle controls do not settle hypothetical divergence.

The [independent review](INDEPENDENT_REVIEW.md),
[kernel audit](kernel_route.md), [automaton audit](automaton_route.md),
and [Mahler derivation](mahler_route.md) separate algebraic proof from
finite checks. The [verifier](verify_examples.py) and
[receipt](verification.json) test bounded exact arithmetic and controls;
they do not verify Cobham or replace the all-input proof above. Historical
mathematical code and the frozen R-series are unchanged.

## 8. Comparison of the three requested mechanisms

| Mechanism | Gain | Remaining obligation for this theorem | Decision |
|---|---|---|---|
| Positive binary kernel | A finite family closed under both bases; elementary residue finish | Only the explicitly imported classical inputs | Adopt as the shortest proof |
| Direct automaton structure | Identifies why a constant section is useful; scaling-only shortcut has a counterexample | An independent direct argument would need additional structure | Retain failed shortcuts and audit; no further search needed for this goal |
| Generating functions | Closure gives finite polynomial2- and3-Mahler systems for positive sections | Published two-base Mahler theorem also supplies rationality | Valid complementary derivation; unnecessary extra machinery for the main proof |

The seven-field candidate records are in the linked route notes. Changing
the retained family resolved the obstacle; no additional state-size bound
or empirical automaton catalogue was needed. The earlier V003 results and
counterexample remain valid. Novelty of this full classification requires
a separate literature assessment and is not claimed by this completion.
