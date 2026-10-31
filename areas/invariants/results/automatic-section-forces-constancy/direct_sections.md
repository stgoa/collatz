# V005 — Direct binary-section growth

**Status: bounded investigation; written reductions, full quantitative goal open.**
This note does not assume that an actual component indicator has any regularity.
It uses the all-positive-integer color equations from V004, with absorber 1
retained. The value at 0 is defined to be h(1).

**Dependency clarification (V008):** the final constancy step of the
local automaticity lemma invokes V004, including its published Cobham
input. The reconstruction and quantitative counting argument are
elementary; their use of that constancy conclusion inherits the input.

## 1. Objects and the exact depth comparison

Write

```
K_D(h) = {n -> h(2^a n+r): 0<=a<=D, 0<=r<2^a},
kappa_h(D) = |K_D(h)|.
```

These are sets of entire functions on n>=0, not finite prefixes. Let K_D^+
retain the terms with a>=1 and 0<r<2^a. Binary sectioning sends K_D^+ into
K_(D+1)^+. V004's proof sends every ternary section into K_(D+4)^+:
its nondivisible case has depth a+1 or a+2, and its divisible case has
depth a-ell+4<=a+4. Neither proof needs K_+ to be finite.

Consequently, for b(n)=h(2n+1), define the cumulative mixed family

```
J_D(b) = {n -> b(2^i 3^j n+r): i,j>=0, i+j<=D,
                                      0<=r<2^i 3^j}.
```

Every such affine section is obtained by a mixed word of i binary and j
ternary sections. The radix expansion of r gives the required digits in
any chosen ordering. Thus

```
J_D(b) subset K_(1+4D)^+(h),
|J_D(b)| <= kappa_h(1+4D).                         (1)
```

The sharper individual bound is 1+i+4j. A linear binary-kernel bound would
therefore give linear *joint* section growth. Separate linear bounds for
the two bases do not give (1); the mixed compatibility is extra information.

For the odd section itself, the exact scalar relations are

```
b(3n)   = b(4n),
b(3n+1) = b(16n+8),
b(3n+2) = b(2n+1),
b(4n+2) = b(n),                         n>=0.       (2)
```

The first three are V004's positive-offset formulas at (a,r)=(1,1).
The fourth is its identity h(4x+1)=h(x) at x=2n+1. These equations retain
the additive guard; replacing them by two dilation invariances loses it.

## 2. A local automaticity lemma

**Lemma (written proof).** If h satisfies the V004 color equations and
one positive-offset binary section

```
g(n)=h(2^K n+r),   K>=1, 0<r<2^K,
```

is binary automatic, then h is constant.

The first step is stronger than monochromatic-cylinder rigidity: one
automatic cylinder forces automaticity of the entire coloring. The final
constancy step uses V004. No claim of novelty is made.

### Uniform reconstruction on ternary units

Follow the fixed K-bit raw shortcut parity word associated with r mod2^K.
As in [V003's predecessor proof](../monochromatic-cylinder-forces-constancy/README.md), let j be its
number of odd branches and write

```
T^K(x)=(3^j x+B)/2^K,
M=3^j,
c=(M r+B)/2^K.
```

Because r is a positive residue, j>=1: the only all-even K-bit word has
source residue 0. The intercept B is a ternary unit, so c is also a ternary
unit. All of K,j,M,B,c are fixed once the cylinder is fixed.

For each a in {1,...,M-1} with 3 not dividing a, choose s_a>=0 such that

```
2^s_a a = c (mod M),
u_a=(2^s_a a-c)/M >=1.
```

Such arbitrarily large s_a exist because 2 generates the units modulo
3^j. Since a<M and c>0, also u_a<2^s_a. For every q>=0 put

```
x=Mq+a,
t=2^s_a q+u_a,
y=2^K t+r.
```

Direct substitution gives

```
T^K(y)=M t+c=2^s_a x,
h(Mq+a)=g(2^s_a q+u_a).                           (3)
```

Here y>2^K. Every state during the first K shortcut branches exceeds 1,
because a shortcut arrow decreases a positive integer by at most a factor
2. The following s_a halving arrows reach x, with 1 reached only at the
end when x=1. Equation (3) therefore respects absorption; it does not use
a raw arrow leaving 1. No cutoff exception is needed.

Each right side of (3) is an actual binary section of g. Thus all the
finitely many sequences q -> h(Mq+a), for unit a, are binary automatic.

### Elementary automaticity closures used here

We use these finite-kernel facts, and give the kernel argument to specify
their scope.

1. If f is binary automatic and A,B are fixed nonnegative integers with
   A>=1, then f(An+B) is binary automatic. In its depth-D section, divide
   Ar+B by 2^D. The quotient belongs to a fixed finite range, and the
   remainder chooses one of the finitely many kernel members of f.
   The resulting functions have the form k(An+q), with k in K_2(f) and q
   in that fixed range.
2. Interleaving finitely many binary-automatic sequences on residues modulo
   any fixed positive integer M preserves automaticity. To see this, first
   pass to the union of their finite kernels. In a depth-D section split
   n=Ml+t, 0<=t<M. The original argument is
   `2^D(Ml+t)+r`, so its quotient on a fixed residue modulo M is
   `2^D l+floor((2^D t+r)/M)`. This latter floor is in [0,2^D), hence
   selects a kernel member. The M choices form a tuple from a fixed finite
   set. There are only finitely many such interleaved tuples.

Define f on all nonnegative integers by f(n)=h(n) when 3 does not divide n,
and give f an arbitrary fixed color at the remaining inputs. Equation (3)
and closure 2 make f binary automatic. The original odd section satisfies

```
b(n)=h(2n+1)=h(6n+4)=f(6n+4),    n>=0.
```

At n=0, the middle equality is h(1)=h(4), justified by doubling invariance.
Closure 1 makes b binary automatic. Finally h(2n)=h(n) and
h(2n+1)=b(n) imply that K_2(h) is contained in `{h} union K_2(b)`.
It is finite. V004 now makes h constant, proving the lemma.

**Consequence.** If h is a hypothetical nonconstant invariant, every
positive-offset binary section has an infinite binary kernel. This is
stronger than the infinite-kernel conclusion for h alone, but by itself it
still gives no superlinear bound for kappa_h(D).

### A quantitative version of the reconstruction

The same argument gives an explicit, weaker complexity transfer. Keep the
choices above and let, for 0<=t<M,

```
a_t = (6t+4) mod M,   q_t=floor((6t+4)/M),
A_t = 6*2^s_(a_t),    B_t=2^s_(a_t)*q_t+u_(a_t),
C_g = sum_(t=0)^(M-1) A_t.
```

Every a_t is a ternary unit; 0<=q_t<=5 and 0<B_t<A_t. Equation (3) gives

```
b(Ml+t)=g(A_t*l+B_t),                  l>=0.       (4)
```

For a depth-d binary section of b, split its argument n=Ml+t. Put
v=(2^d*t+r) mod M and w=floor((2^d*t+r)/M); then 0<=w<2^d. Equation (4)
turns that piece into

```
g(A_v*2^d*l+A_v*w+B_v)=k(A_v*l+q),
```

where k is a binary section of g of depth d and
q=floor((A_v*w+B_v)/2^d) lies in {0,...,A_v-1}. Across every d<=D there
are at most C_g*kappa_g(D) possibilities for each piece. The M pieces
determine the whole function, so

```
kappa_b(D) <= (C_g*kappa_g(D))^M.
```

Finally every nonzero-offset binary section of h of depth at most D is a
binary section of b of depth at most D-1, by removing its common power of2.
Therefore, for D>=1,

```
kappa_h(D) <= 1+(C_g*kappa_g(D-1))^M.               (5)
```

This is an all-depth inequality for entire sections, with constants fixed
by the chosen cylinder. The exponent M can be large. In particular it
does not turn a linear bound into a finite bound, and is not the requested
superlinear obstruction theorem.

## 3. The precise branching obligation

For a state g, let Desc_2(g) be its entire binary descendant family. A
simple graph-growth lemma isolates a sufficient next step.

**Lemma (written proof).** Suppose g_1,...,g_m occur in K_A(h), all their
binary descendant families are infinite, and those families are pairwise
disjoint. Then, for every D>=A,

```
kappa_h(D) >= m*(D-A+1).                            (6)
```

Proof: in an infinite finitely branching rooted directed graph, the
cumulative reachable set after t steps has at least t+1 vertices. If one
layer added no vertex, all later layers would also add none. Apply this
to each g_i at t=D-A and add the disjoint counts.

The local lemma supplies infinitude for every positive g_i. It does **not**
supply disjointness. If arbitrarily many pairwise disjoint descendant
families could be produced from the additive identities, (6) would prove
the full requested unbounded ratio. Proving that amplification is an open
obligation here. Infinitely many states or infinite descendants at every
state do not suffice: an infinite ray with all descendant cones nested has
linear growth.

Thus neither a plateau argument nor merely repeating V004 on every
cylinder completes the quantitative goal. A valid proof must either
produce arbitrarily many independent descendants, or control their
overlaps strongly enough to recover equivalent growth.

## 4. Worked example and controls

Take K=1,r=1. The shortcut word has j=1, M=3, B=1 and c=2. The choices

```
a=1: s_a=3, u_a=2,
a=2: s_a=2, u_a=2
```

give exact color identities

```
h(3q+1)=g(8q+2),
h(3q+2)=g(4q+2).
```

For q=0, the source integers are 5 and 5; their shortcut images are 8,
followed respectively by three or two halvings. Both end at the declared
targets 1 and 2 without leaving the absorber.

For d=5 and d=61, h_d(n)=1_(d divides n) is an automatic nonconstant
invariant and every positive binary section is automatic. The uniform
predecessor construction itself transfers to these d, but the last step
using V004's d=1 rigidity does not. Their actual cycles d->d remain
disjoint from absorber 1. V004's named +1 identity fails at u=d, so the
argument does not silently eliminate these controls.

### Exact control on the tempting graph shortcut

The coordinating lane supplied the following infinite least-significant-
digit automaton. This lane independently checked its transitions, the
absorber-independent color equations, and its failure of the full guard.
Let F(t) be 1 when t is a positive power of 2 and 0 otherwise. Use states
H,B,C,G_t for t>=1, with transitions

```
       digit 0   digit 1   output
H         H         B       F(1)
B         C        G_2      F(1)
C        G_1        B       F(1)
G_t      G_t      G_(t+1)    F(t).
```

Start in H and call the resulting sequence z. All trailing input zeroes
(leading zeroes in ordinary notation) preserve the output, including the
path B->C->G_1. Thus the rule defines a sequence on nonnegative integers.
It has z(0)=z(1)=1, and

```
z(2n)=z(n),
z(8n+5)=z(2n+1).
```

The second identity is the state return H--1-->B--0-->C--1-->B. For D>=3,
all states reached in at most D digits lie in
`{H,B,C,G_1,...,G_D}`, giving kappa_z(D)<=D+3. The functions generated by
G_t are exactly `n -> F(t+s_2(n))`; they are pairwise distinct, since for
t<u a sufficiently large power 2^k makes F(2^k)=1 while
F(2^k+u-t)=0. Every G_t has infinitely many such descendants, and each of
H,B,C reaches a G_t. Hence every binary section of z has infinite kernel.

Nevertheless the full guard fails: the input 9 follows H,B,C,G_1,G_2 and
has color 1, whereas 28 follows H,H,H,B,G_2,G_3 and has color 0. Thus
z(9) differs from z(3*9+1). This is an exact counterexample to the proposed
shortcut from linear graph growth, doubling, the positive return loop,
and nonautomaticity of every section. It is **not** a counterexample to the
active goal. Every descendant cone meets the common nested G_t tail, so
the disjointness obligation in Section 3 is exactly absent.

## 5. Seven-field assessment

| Field | Assessment |
|---|---|
| Objects | Entire binary sections and their mixed binary/ternary descendants, with exact depth filtration. |
| Structural gain | The additive identities force linear joint growth under a hypothetical linear binary bound. Local automaticity anywhere in a positive dyadic cylinder would already force global constancy. |
| Translated unresolved gap | Prove enough independent descendant growth, or a valid linear-growth rigidity theorem for the full mixed section action. Neither finite Cobham nor separate-base growth supplies this. |
| Worked example | The K=1,r=1 reconstruction above, with both ternary-unit residue classes and explicit absorbed paths. |
| Known-cycle controls | Divisibility invariants for d5/d61 survive; the d1 classification is exactly the unavailable transfer step. |
| Cheapest meaningful next test | Audit the local reconstruction, then determine whether overlapping descendant cones under equations (2) can be forced to split into arbitrarily many disjoint infinite cones. A finite-prefix state count cannot test equality of entire sections. |
| Genuinely intermediate milestone | Prove the unbounded linear ratio for arbitrary finite-valued invariants, as activated. The local lemma is partial progress; it does not satisfy that milestone. |

## Decision

Retain the exact joint-depth comparison and local automaticity lemma.
Do not declare the active goal complete. The next direct investigation must
address descendant overlaps or a comparably strong joint-growth statement;
another finite-state reformulation would not move the quantitative target.
