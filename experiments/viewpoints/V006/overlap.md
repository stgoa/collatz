# V006 — Mixed sections separate every nonperiodic digit-count ray

**Status: written scoped theorem and exact control, 2026-10-18.** The full
unbounded-linear-ratio goal remains open. This investigation proves a
quadratic lower bound when an invariant has one positive binary section
of digit-count type. It does not assert that every linearly growing
section family has such a section. No novelty or formal-verification
claim is made.

**Dependency clarification (V008):** distinctness with F explicitly not
eventually periodic is elementary. The Collatz corollary excludes the
eventually periodic case through V005/V004 and inherits their published
Cobham input. No independent formal replay of that input is asserted.

The argument was developed in parallel with the coordinating lane's
joint-growth investigation. All functions below are entire sequences on
nonnegative integers; finite-prefix agreement is not used as equality.

## 1. The full guard supplies more than the binary return

The [V005 scalar interface](../V005/scalar_interface.md) retains the whole
invariant equation as

```
b(3n)=b(4n),
b(3n+2)=b(2n+1),
b(4n+2)=b(n),                         n>=0.           (1)
```

For example these equations imply the additional binary identity

```
b(8n+1)=b(4n).                                         (2)
```

Indeed apply the second equation at 4n to get
`b(12n+2)=b(8n+1)`, the third at 3n to get
`b(12n+2)=b(3n)`, then the first at n. The old nested-ray graph from V005
does not satisfy (2). This exposes specific missing information, but the
identity by itself is not a growth theorem.

The useful stronger consequence remains the depth-controlled mixed
closure. If

```
g(n)=h(2^K n+r),   K>=1, 0<r<2^K,
```

then a mixed word containing i binary and j ternary section operations
is another positive h-section of depth at most K+i+4j. This follows from
V004's exact formulas and holds without finite-kernel assumptions.

## 2. A quadratic mixed-kernel theorem

Let F:N_0->C be a finite-valued sequence which is **not eventually
periodic**, and write s_2 for binary digit count. Fix t_0>=0 and set

```
g(n)=F(t_0+s_2(n)).
```

**Theorem (written proof).** All the whole sequences

```
Q_(a,t)(n)=F(t_0+t+s_2(3^a n)),       a,t>=0,          (3)
```

are pairwise distinct. Consequently, if J_g(D) counts distinct sequences
obtained from g by at most D binary or ternary section operations, then

```
J_g(D) >= (D+1)(D+2)/2,              D>=0.             (4)
```

### Two exact digit-count formulas

For fixed positive odd m,c and sufficiently large k,

```
s_2(m(2^k-c)) = k-delta_m(c),
delta_m(c)=s_2(mc-1)-s_2(m-1).                         (5)
```

The condition `2^k>mc` is sufficient. The two disjoint binary blocks in

```
m(2^k-c)=(m-1)2^k+(2^k-mc)
```

have total weight `s_2(m-1)+k-s_2(mc-1)`, proving (5). In particular,

```
s_2(m(2^k-1))=k               whenever 2^k>m.         (6)
```

We also need an exact rational-block count. For every r>=1 and every
positive K divisible by L_r=2*3^(r-1),

```
s_2((2^K-1)/3^r)=K/2,
s_2((2^K-1)/3^r-1)=K/2-1.                            (7)
```

Here is an elementary proof. The order of 2 modulo 3^r is L_r, and
`2^(L_r/2)=-1 mod3^r`. These are the same elementary unit-group facts
used in the [V003 predecessor construction](../V003/cylinder_rigidity.md):
lifting `4^q-1` by a factor 3 raises its 3-adic valuation by one, and
the unique nontrivial square root of 1 modulo 3^r is -1.

Put A=2^(L_r/2) and w=(A+1)/3^r. Then

```
(2^L_r-1)/3^r = (w-1)A+(A-w).
```

The two blocks of length L_r/2 are complementary, since
`A-w=(A-1)-(w-1)`. Their combined weight is L_r/2. For K a multiple of
L_r, the quotient `(2^K-1)/3^r` repeats this block K/L_r times without
overlap, proving the first equality in (7). The quotient is odd, so
subtracting 1 removes exactly its last 1-bit, proving the second.

### Distinctness of the entire family

Suppose Q_(a,t)=Q_(b,u). Evaluating at `n=2^k-1` for all sufficiently
large k and using (6) gives

```
F(t_0+t+k)=F(t_0+u+k).
```

If t!=u this is a nonzero eventual period of F. Therefore t=u.

Suppose next a<b. Write m=3^a, l=3^b, and choose an arbitrarily large
positive K divisible by L_b=2*3^(b-1). Define the positive integer

```
c=(2^K-1)/3^b.
```

Then lc=2^K-1 and mc=(2^K-1)/3^(b-a). Formula (7) applies because
L_(b-a) divides L_b, giving

```
delta_l(c)=K-1-s_2(3^b-1),
delta_m(c)=K/2-1-s_2(3^a-1).
```

Their difference is

```
K/2+s_2(3^a-1)-s_2(3^b-1),
```

which is nonzero for sufficiently large K. Keep this c fixed and now
evaluate the presumed equality of Q states at `n=2^k-c` for every k>K.
Equation (5) gives

```
F(t_0+t+k-delta_m(c))=F(t_0+t+k-delta_l(c)).
```

This again makes a nonzero eventual period of F, a contradiction. Thus
a=b as well. The states (3) are pairwise distinct.

To obtain (4), first take t binary sections with digit 1. The resulting
function is `F(t_0+t+s_2(n))`. Then take a ternary sections with digit 0.
The result is Q_(a,t), reached in exactly a+t operations. Counting all
pairs a+t<=D proves (4). This completes the theorem.

## 3. Consequence for the active invariant problem

**Corollary (written proof).** Suppose a hypothetical nonconstant
finite-valued Collatz invariant has a positive binary section of the form

```
h(2^K n+r)=F(s_2(n)),     K>=1, 0<r<2^K.             (8)
```

Then, for every D>=0,

```
kappa_h(K+4D) >= (D+1)(D+2)/2.                        (9)
```

More sharply the distinct state Q_(a,t) is an h-section of depth at most
K+t+4a. The simpler common bound K+4D suffices for (9). For every N>=K,
one may set D=floor((N-K)/4); thus the bound holds on all sufficiently
large depths, with leading lower-bound coefficient 1/32.

To justify the theorem's nonperiodicity premise, if F were eventually
periodic then `F(s_2(n))` would be binary automatic: a finite automaton can
retain the exact digit count below its fixed eventual cutoff and the
digit count modulo the eventual period above that cutoff. V005's local
automaticity lemma would then make h constant. Therefore the F in (8)
must be non-eventually-periodic for a nonconstant h, and Section 2 applies.

The same conclusion holds when the section is `F(t_0+s_2(n))`; absorb
t_0 into F. This excludes the entire mechanism in which a mixed section
family shares a tail of arbitrary-output digit-count states. It does
not require that the whole graph consist of that tail: the presence of
one such section already suffices.

**Unresolved hypothesis:** nothing here shows that an arbitrary
linearly growing binary-section graph contains a digit-count section.
The full active goal requires all nonconstant finite-valued invariants,
so (9) is a scoped gain rather than completion.

## 4. A linear control with no digit-count section

The extraction hypothesis cannot follow from linear growth, doubling,
and the binary return alone. Let N_11(n) count adjacent 11 pairs in the
binary expansion of n, with N_11(0)=0. Put

```
F(t)=1 if t is a positive power of 2, and 0 otherwise,
z(n)=F(N_11(n)).
```

Then z(0)=z(1)=0, and for all n>=0,

```
z(2n)=z(n),
z(8n+5)=z(2n+1).                                    (10)
```

Appending 0 creates no 11 pair. Appending either the word 101 or the
word 1 adds exactly the same boundary pair, namely n mod2, and neither
suffix has an internal 11 pair. This proves (10), including n=0.

For every positive depth a and residue 0<=r<2^a, let t be the number of
11 pairs inside the a-bit word for r and let epsilon be that word's
most significant bit. Then the whole section is exactly

```
z(2^a n+r)=F(t+N_11(n)+epsilon*(n mod2)),
0<=t<=a-1, epsilon in {0,1}.                         (11)
```

Hence `kappa_z(D)<=2D` for D>=1, and kappa_z(0)=1. This is an upper
bound on whole sections from their explicit formulas, not a prefix count.

No section (11), including z itself, is a function only of s_2(n). To
prove this, fix k>=1 and compare the two even integers

```
n_1=2(2^k-1),
n_2=sum_(i=1)^k 2^(2i).
```

Both have k ones, while N_11(n_1)=k-1 and N_11(n_2)=0. The boundary term
vanishes because both are even. If (11) equaled J(s_2(n)) for some J,
then `F(t+k-1)=F(t)` for all k>=1, forcing F to be constant on a tail.
The chosen F is not, a contradiction.

Every section in (11) also has an infinite binary kernel. Taking its
binary section with m low-order ones gives

```
n -> F(t+m-1+epsilon+N_11(n)+(n mod2)),    m>=1.
```

These are pairwise distinct: evaluate at n=2^k-1, k>=1, to obtain tails
of F shifted by t+m-1+epsilon, since `N_11(n)+(n mod2)=k`. Equality for
different m would make F eventually periodic.

The full Collatz guard fails at the actual positive odd input 3:

```
z(3)=F(1)=1,   z(10)=F(0)=0.
```

Thus the example is a control on extracting a digit-count ray from
reduced graph data, not a Collatz invariant or a counterexample to the
active goal. It satisfies every reduced premise tested here while
lacking every section covered by the new corollary.

## 5. Scope and next discrimination

The d5/d61 divisibility colorings remain valid periodic, nonconstant
invariants for their respective maps. The quadratic theorem is a generic
statement about a non-eventually-periodic digit-count ray; it does not
claim that those divisibility colorings contain such a ray. In the
Collatz corollary the step excluding eventually periodic F uses V004's
specific d1 classification and does not transfer unchanged to d5/d61.
Their odd fixed cycles d->d remain disjoint from absorber 1.

| Field | Assessment |
|---|---|
| Objects | Mixed sections of one arbitrary-output digit-count state, embedded in a positive h-section. |
| Structural gain | Explicit quadratic separation: every pair of parameters (ternary dilation depth, digit-count shift) gives a different entire function. |
| Translated unresolved gap | An arbitrary linear-growth section graph need not contain a digit-count state; no full-guard extraction or general overlap theorem is proved. |
| Worked example | The binary blocks of `(2^K-1)/3^r` have exactly K/2 ones, providing exact state-separation witnesses. |
| Known-cycle controls | d5/d61 remain permitted; the auxiliary 11-pair sequence satisfies the reduced loop assumptions but explicitly fails the full guard at 3. |
| Cheapest meaningful next test | Determine whether the full three identities force an appropriate richer counter-state structure, or prove joint separation for a general class of linear-growth graphs without assuming such a structure. |
| Genuinely intermediate milestone | The active all-invariant unbounded-linear-ratio theorem. The conditional quadratic result excludes a broader mechanism, but is not completion. |

**Decision:** retain the quadratic theorem and the no-digit-count-section
control. Do not assume a classification of all linear-growth graphs or
replace the active objective by this subclass result.
