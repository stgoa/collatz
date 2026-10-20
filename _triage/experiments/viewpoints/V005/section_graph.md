# V005 — A linear section graph can satisfy the first return identities

**Status: written scoped counterexample.** This note rejects a proposed
growth argument. It is not a counterexample to Collatz invariance or the
active quantitative goal.

## 1. The tempting inference

The [direct investigation](direct_sections.md) proves that a hypothetical
nonconstant invariant has an infinite binary kernel below every positive
binary section. It also has the identities

```
h(2n)=h(n),
h(8n+5)=h(2n+1).
```

Neither these identities nor infinitude below every section forces
superlinear growth. The explicit model below has all those properties
and only linearly many entire binary sections. Its descendant families
overlap in nested infinite tails.

## 2. An explicit infinite automaton

For t>=1 let F(t)=1 when t is a power of2, and F(t)=0 otherwise. Consider
states H,B,C and G_t for t>=1, with binary transitions

| State | Digit0 | Digit1 | Output |
|---|---|---|---|
| H | H | B | 1 |
| B | C | G_2 | 1 |
| C | G_1 | B | 1 |
| G_t | G_t | G_(t+1) | F(t) |

Read binary digits from least significant to most significant; for0 read
no digits. The output at the ending state defines the corresponding
sequence. Appending leading zeros does not change the output, since each
state has the same output as its digit0 successor. Thus this is a
well-defined sequence model on all n>=0, and each transition is an actual
binary section of the indicated sequence.

In particular

```
G_t(n)=F(t+s_2(n)),
H(0)=H(1)=1,
H(2n)=H(n),
H(8n+5)=B(n)=H(2n+1).                                (1)
```

The second return follows from the low-order digit path101:
H→B→C→B. Equivalently B(4n+2)=B(n). These are identities of entire
sequences, not finite agreement observations.

## 3. Distinctness and exact linear count

The G_t are pairwise distinct. For t!=u, choose a power of2, P, greater
than2*max(t,u). Set s=P-t>=0 and n=2^s-1. Then s_2(n)=s,
G_t(n)=F(P)=1, while P+u-t lies strictly between P/2 and2P and is not P.
Hence G_u(n)=0.

None of H,B,C can equal G_t as an entire function. Equal functions have
equal sections. If B=G_t, then C=G_t by digit0, but the digit1 transition
from C would give B=G_(t+1), a contradiction. If C=G_t, its digit1 section
gives B=G_(t+1), then B's digit0 section gives C=G_(t+1), again impossible.
If H=G_t, its digit1 section would give B=G_(t+1), already excluded.

H,B,C are also pairwise distinct. If H=B, digit0 gives H=C and digit1
gives B=G_2, impossible. If H=C, digit0 gives H=G_1. If B=C, digit0
gives C=G_1. Both contradict the exclusions above.

At depths0,1,2 the cumulative reachable states number1,2,4. At depth3
they are exactly H,B,C,G_1,G_2,G_3. For every D>=3, the states through
depth D are exactly

```
H,B,C,G_1,...,G_D.
```

Indeed G_1 is reached by100, G_t for t>=2 by t successive1 digits,
and no transition can increase t faster than one per digit. Consequently

```
kappa_H(0)=1, kappa_H(1)=2, kappa_H(2)=4,
kappa_H(D)=D+3                       for D>=3.          (2)
```

Every reachable state has an infinite binary kernel: G_t reaches all
G_(t+j), B reaches G_2, C reaches G_1, and H reaches B. For every pair
of states, their descendant families intersect in an infinite tail of
the G_t ray. Thus no two states have disjoint full descendant cones.

## 4. Where the actual Collatz guard fails

The model is not a Collatz invariant:

```
H(9)=F(2)=1,
H(3*9+1)=H(28)=F(3)=0.
```

For its odd section B, the scalar identity B(3n)=B(4n) already fails at
n=1: B(3)=H(7)=0, while B(4)=H(9)=1. The remaining ternary relations
are not supplied by the two retained binary identities.

This example therefore rejects the graph inference while keeping a
specific possible source of additional rigidity: the full ternary
relations derived from3n+1. It does not establish a linear-growth
Collatz invariant or refute the active target.

## 5. Why group-growth theorems do not apply automatically

The section operators act on an orbit of functions and need not be
invertible. Their finite out-degree graph is not a Cayley graph of a
finitely generated group, and linear orbit growth does not identify the
acting transformation semigroup or make it virtually cyclic. Even an
infinite ray can have all descendant families infinite and nested.

The example supplies an actual sequence realization of that obstruction,
including the zero-input compatibility that an arbitrary drawn graph
might lack. It rules out using graph size and the first return loop as
a substitute for the unexamined additive relations.

## 6. Seven-field assessment

| Field | Assessment |
|---|---|
| Objects | Entire binary-section states with a depth filtration; a deterministic infinite digit automaton. |
| Structural gain | An explicit realization isolates why infinite descendants and a positive-offset return do not imply independent growth. |
| Translated unresolved gap | Control overlaps using the full mixed2/3 identities, or prove another quantitative mechanism. |
| Worked example | H(9)=1,H(28)=0 and the exact count D+3 above. |
| Known-cycle controls | The genuine d5/d61 divisibility invariants remain periodic and nonconstant. This auxiliary model is not offered as a dynamical control or actual orbit coloring. |
| Cheapest meaningful next test | Retain all four scalar odd-section relations from the direct note and try to rule out a shared infinite tail with linear growth. |
| Genuinely intermediate milestone | The requested unbounded linear ratio remains the target. This counterexample rejects one mechanism and does not complete it. |
