# V008 — What a linear joint bound actually supplies

**Status: exact counting reductions and a scoped graph control; no new
affine growth theorem.** This bounded pass found no proof that linear
joint whole-section growth forces an automatic section, and no exact
affine-section counterexample to that assertion. The active unbounded
linear-ratio goal remains open.

The [two-exit example](two_exit.md) already shows why a single finite cut
cannot carry the argument: its actual affine section graph has a finite
interior with two exits and infinite kernels in both bases at every
vertex, yet its joint growth is at least quadratic. The remaining route
must use the assumed growth over all depths.

## 1. Three different growth conditions

Let B_D be the cumulative rooted ball in the exact joint section graph,
and let a_D=|B_D minus B_(D-1)| for D>=1. The following are different:

1. |B_D|<=C(D+1) for every D;
2. a_D<=K for every D, with one fixed K;
3. a_D<=K at arbitrarily large D, with one fixed K.

Condition 2 implies 1, and 1 implies 3 for a suitable K. Neither reverse
implication follows from counting. In particular, condition 1 does not
even guarantee arbitrarily long intervals on which all a_D are bounded
by one fixed K. Section 3 gives an explicit profile with that failure,
including the adjacent-size constraint needed by bounded-degree graphs.
It is not asserted to be an affine section graph.

## 2. A uniform mean bound after arbitrarily late cuts

There is a stronger valid consequence than merely finding isolated small
layers.

**Lemma (written proof).** Suppose |B_D|<=C(D+1) for every D. For every
real C'>C, arbitrarily large integers r satisfy

```
|B_(r+t) minus B_r| <= C' t,             every integer t>=0.       (1)
```

Put F(D)=|B_D|-C'D. The assumed bound gives F(D)->-infinity.
For every R, the set {F(D):D>=R} has a maximum attained at some r>=R.
For this r, F(r+t)<=F(r) for every t>=0, which is exactly (1).

Thus the outside layer C_r=B_(r+1) minus B_r has at most floor(C')
vertices, and the complete future part beyond this cut retains a uniform
linear *cumulative* bound. More explicitly, vertices reached from C_r
in at most t joint transitions and lying outside B_r form a subset of
B_(r+t+1) minus B_r, hence number at most C'(t+1). Returns through B_r
are permitted; no finite interior is discarded or declared absorbing.

This does not bound every later layer by C', supply a periodic sequence
of transition matrices, or give a uniform bound on an equality witness
between whole sequences. Excluding these uniformly bounded-mean futures
for every C' would address the active goal; the lemma itself supplies
neither an exclusion nor a new intermediate milestone.

## 3. A bounded-degree control against long bounded-width intervals

For n>=1 define

```
t_j(n) = max(0, j-dist(n,(2Z+1)*2^j)),       j>=1,
a_n    = 2+max_(j>=1) t_j(n),
a_0    = 1.
```

Here dist is ordinary integer distance. Only finitely many t_j(n) are
nonzero at any n: the nearest positive center of the jth family is 2^j,
and 2^j-j eventually exceeds n. Each triangular profile t_j is
1-Lipschitz, so |a_(n+1)-a_n|<=1 for n>=1. Also a_1=2, so the same
inequality holds at n=0.

The jth profile has period P_j=2^(j+1) and total mass j² per period.
For 1<=n<=N, only j<=L=1+floor(log_2 N) can contribute: for j>=2,
2^j-j>=2^(j-1). Consequently

```
sum_(n=1)^N a_n
 <= 2N + sum_(j=1)^L (N/P_j+1)*j²
 <= 5N + sum_(j=1)^L j²
 <= 13N.                                                   (2)
```

The last bound uses sum j²<=L³ and L³<=8*2^(L-1)<=8N;
the ratio L³/2^(L-1) attains its maximum 8 at L=4.
Thus the cumulative profile is O(N).

Nevertheless a_(2^j)=j+2. More generally, peaks of height at least j+2
recur at every integer congruent to 2^j modulo 2^(j+1). For any fixed
K, choose j with j+2>K. Every interval of P_j consecutive integers
contains such a peak. Hence every interval on which all widths are at
most K has length less than P_j. There are no arbitrarily long intervals
with a common fixed width bound.

This profile is realizable as the distance layers of a rooted directed
graph of outdegree at most two, with every vertex having infinitely
many descendants. Between adjacent levels, give every old vertex a
successor and cover every next-level vertex; an increase of at most one
requires at most one additional outgoing edge. All edges advance one
level, so the assigned levels are exact distances and every path
continues forever.

**Scope of the control.** It invalidates a deduction using only cumulative
growth, finite branching, and infinite descendants. It does not preserve
the six radix identities or identify vertices with entire sequences.
It therefore does not refute a corresponding theorem using the full
affine structure. The two-exit example and this profile serve different
purposes: one is an actual affine example with quadratic growth, the
other has linear graph growth without the affine identities.

## 4. The near-minimal binary case is an exact narrower question

For an infinite binary kernel, every layer is nonempty: an empty layer
would make the preceding finite ball binary-closed. Thus

```
e_D = kappa_h(D)-(D+1)
```

is a nonnegative, nondecreasing integer sequence. It follows that

```
kappa_h(D)=D+O(1)
```

holds if and only if exactly one new binary vertex is added at every
sufficiently large depth. This equivalence is an elementary counting
fact, not yet a contradiction with the Collatz equations.

For a positive section with a binary representation at depth a, V004
represents each ternary child at binary depth at most a+4. Applied to
such a thin tail, this permits several forward vertices and arbitrary
returns into earlier levels. It does not make a singleton *binary*
layer a singleton *joint* exit, so V007's theorem does not apply directly.
The representation bound is relative to the root coloring h; it does
not state that the ternary child is obtained by at most four binary
transitions from the current section.

This leaves a precise diagnostic: can the full radix identities and
the bounded forward depth of ternary transitions coexist with an
eventually single-vertex binary tail in a nonconstant invariant?
Excluding that situation would prove kappa_h(D)-(D+1) is unbounded.
It would still not prove an unbounded ratio, nor even a fixed positive
fractional improvement infinitely often. No answer to this diagnostic
was proved in this pass.

## 5. One new source checked: finite-rank symbolic presentations

Valérie Berthé, Paulina Cecchi Bernales, and Reem Yassawi,
*Coboundaries and eigenvalues of finitary S-adic systems*,
[primary manuscript, version 3](https://arxiv.org/pdf/2202.07270v3),
Corollary 6.9, requires two finitary, straight, aperiodic, recognizable
constant-length directive sequences, each possessing a fully essential
word of length two. If some prime divides infinitely many substitution
lengths in one presentation and only finitely many in the other, their
shift systems cannot be topologically conjugate. Constant lengths 2
and 3 would satisfy the prime-divisibility condition.

A small rooted section frontier has not been converted here into these
two presentations of one shift system. In particular neither bounded
alphabet presentations with the required properties nor recognizability
is provided by (1). The theorem therefore supplies no growth gap at
present. The section graph's radix identities must not be identified
with the theorem's dynamical hypotheses. This was a focused source
check; the earlier rejected imports were not re-surveyed.

## 6. Seven-field assessment and decision

1. **Objects.** Entire joint affine sections and cumulative balls; the
   additional binary height bound available for Collatz sections.
2. **Structural gain.** Linear cumulative growth provides arbitrarily
   late cuts with the uniform future mean bound (1). Near-minimal binary
   growth has the exact eventual singleton-layer characterization.
3. **Translated unresolved gap.** Use affine compatibility to exclude
   the bounded-mean futures for every coefficient. Counted sparse layers
   alone cannot be replaced by uniformly bounded-width stretches.
4. **Worked example.** The explicit triangular-peak profile has linear
   cumulative growth, bounded degree and recurrent peaks of every size.
5. **Known-cycle controls.** The generalized-map divisibility colorings
   have finite kernels and do not satisfy the needed two-base infinitude.
   The actual two-exit example satisfies infinitude but fails the full
   Collatz guard and has quadratic joint growth.
6. **Cheapest meaningful next test.** Resolve the exact eventually
   singleton binary-tail diagnostic in Section 4 while retaining the
   four-level ternary bound and all old-state returns. This tests an
   additional use of the Collatz structure; it is not the all-coefficients
   theorem.
7. **Genuinely intermediate milestone.** The active unbounded-ratio
   obstruction remains the intended result. The soft reductions and
   source audit in this file are supporting analysis, not its completion.

No universal rate improvement, classification, novelty, or formal
verification is claimed. The full goal stays active.
