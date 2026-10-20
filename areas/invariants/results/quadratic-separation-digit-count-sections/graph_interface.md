# V006 — The exact graph interface for the remaining growth problem

**Status: written representation and necessary condition, not a new growth
theorem.** This records which structure the next overlap argument must keep.
The quadratic theorem in [overlap.md](overlap.md) covers a specified type
of section; it supplies no classification of all graphs below.

## 1. Every joint section graph has six radix identities

For a sequence s, write

```
E_i(s)(n)=s(2n+i),       i=0,1,
T_j(s)(n)=s(3n+j),       j=0,1,2,
o(s)=s(0).
```

The vertices are entire sequences, so they are identified only when all
their values agree. For every vertex s and every i,j, uniquely write
`2j+i=3l+k`, with l in{0,1} and k in{0,1,2}. Then

```
T_j(E_i(s))=E_l(T_k(s)).                              (1)
o(E_0(s))=o(T_0(s))=o(s).                             (2)
```

Both sides of (1) are the sequence n->s(6n+2j+i). There are six such
identities. They express reordering two successive radix operations;
they do not say that all digit operators commute. Equation (2) is the
leading-zero output condition.

For the root b(n)=h(2n+1), the full Collatz equations add

```
T_0(b)=E_0(E_0(b)),
T_2(b)=E_1(b),
E_1(E_0(b))=b.                                      (3)
```

The order in the last relation matters: its sequence is b(4n+2).
These three relations are exactly the [V005 scalar interface](../scalar-interface-three-identities.md).
In particular, a collision among zero-digit dilations is already present
at b. The generic collision obtained by comparing a triangular number
of exponent pairs with a linear ball gives no missing additive control
there.

## 2. These graph conditions recover actual sequences

This converse prevents importing arbitrary graph examples as if they
were affine section actions. Suppose a rooted graph has the five
everywhere-defined transitions above, finitely many output colors,
and (1)-(2) at every vertex. For each vertex s, define f_s(n) by reading
the binary digits of n from least to most significant and taking the
output of the resulting vertex. At n=0 use the empty word. Appending
zero digits does not change the output by (2).

The same rule using ternary digits gives the same value. Indeed choose
a,b with n<2^a and n<3^b. Read a binary digits for n followed by b
ternary zero digits. Repeated use of (1) reorders the same mixed-radix
representation into b ternary digits followed by a binary digits. Its
integer residue remains n. Since n<3^b, the final binary digits are all
zero. Equation (2) removes them. The remaining ternary digits are the
ordinary representation of n, proving the claim.

Consequently

```
f_(E_i(s))(n)=f_s(2n+i),
f_(T_j(s))(n)=f_s(3n+j).
```

If two vertices cannot be distinguished by the output after any finite
binary word, their entire functions are equal and they must be merged.
Assume this merger has been performed. Then vertices reachable from the
root in at most D transitions correspond exactly to its distinct joint
sections through depth D. If (3) also holds at the root, the V005 scalar
converse reconstructs a genuine Collatz-invariant coloring h.

Thus a proposed linear-growth countermodel must satisfy all of (1), (2),
(3) and whole-function distinguishability. The abstract T,U action in
[joint_literature.md](joint_literature.md) and the binary 11-pair example
do not supply such a model.

## 3. Linear growth would force small separating layers

Let B_D be the set of vertices at distance at most D from the root. If
`|B_D|<=C(D+1)` for every D, then for infinitely many D,

```
|B_(D+1) minus B_D| <= floor(C).                     (4)
```

Otherwise, after some depth each increase would be at least floor(C)+1,
which is strictly larger than C, contradicting the assumed bound after
summing. Every directed path from the root to a vertex outside B_D must
pass through B_(D+1) minus B_D at its first exit. Thus (4) supplies
arbitrarily distant separating sets with a fixed finite size.

For a nonconstant Collatz invariant every vertex in this joint graph has
an infinite binary descendant family: V004 represents it as a positive
binary h-section, and V005 rules out automaticity of any such section.
These facts do not rule out small separating sets by themselves; the
retained binary controls demonstrate the danger of that inference.

## 4. Next bounded discrimination

Test whether (1)-(3), including the zero-output condition, force an
automatic section whenever arbitrarily distant layers have bounded size.
A first bounded case is a repeated one-vertex separating layer. A proof
for that case alone would be partial; completion needs every possible
linear coefficient or another argument yielding the full unbounded ratio.

This is a concrete graph obligation using the full affine structure.
Do not replace it with a theorem counting distinct transformations, assume
that all linear-growth graphs consist of finitely many counter rays, or
infer small global pattern complexity from a rooted ball count. The
earlier controls explicitly exclude those shortcuts.

The finite d5/d61 divisibility-color graphs obey the universal radix and
zero-output identities; they need not obey the d1 root identities (3).
A successful argument must retain that distinction. Neither this faithful
representation nor the necessary small-layer condition completes the
active quantitative theorem.
