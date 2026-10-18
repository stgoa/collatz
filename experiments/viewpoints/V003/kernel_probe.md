# V003 — The first ternary image of a finite binary kernel

**Status: written elementary section identities and a finite-family
consequence; full automatic-coloring classification remains open here.**
This is a bounded structural probe, with no automaton catalogue, trajectory
scan, new current, convergence claim or novelty claim. It continues
[V13](../V002/invariant_colors.md).

## 1. Domain and section conventions

Let h be finite-valued on positive integers and assume

```
h(2n)=h(n)                 (n>=1),
h(3n+1)=h(n)               (positive odd n>1).
```

These are component-coloring identities for ordinary arrows, with1
absorbing. They do not assign shortcut or odd-only time to a section
operation. At the missing odd source1 the same value identity follows
from h(4)=h(1), so the second displayed equality can also be used there
at d=1 without changing the dynamics.

Set h(0)=h(1) solely to use the usual sequence domain n>=0. For a>=0 and
0<=r<2^a write

```
B_(a,r)h(n)=h(2^a*n+r),
K={B_(a,r)h:a>=0,0<=r<2^a},
T_j f(n)=f(3n+j),        j=0,1,2.
```

Assume K finite. Equality of states means equality of entire sequences,
not agreement below a checked cutoff. Binary sections of states in K
again lie in K by direct composition.

## 2. Both nonzero ternary sections are already binary sections

For every m>=0,

```
h(3m+1)=h(4m+1).                                  (1)
```

For m>=1, apply the odd-source identity at4m+1 and remove the factor4
from12m+4. At m0 both sides are h(1). Likewise

```
h(3m+2)=h(2m+1).                                  (2)
```

For m>=1 use the odd source2m+1 and remove the factor2; at m0 this is
h(2)=h(1). Therefore

```
T_1 h=B_(2,1)h,       T_2 h=B_(1,1)h.
```

The missing first section is f_1(n)=T_0 h(n)=h(3n).

## 3. All binary states have only this one possible extra ternary image

**Proposition.** With f_1(n)=h(3n),

```
T_j(K) is contained in K union {f_1},     j=0,1,2.  (3)
```

First, for every positive odd u,

```
h(3u)=h(9u+1)=h(12u+1)=h(16u+1),
```

where the last two equalities use (1). Hence

```
f_1(2n)=f_1(n),
f_1(2n+1)=h(32n+17)=B_(5,17)h(n).                (4)
```

Every binary section of f_1 is therefore either f_1 or a state in K:
successive zero sections retain f_1, and the first1 section enters K.
This is a statement about reading the section digits, not about a
Collatz orbit or a finite bound on its future.

Now take g=B_(a,r)h and fix j. Put c=2^a*j+r, so 0<=c<3*2^a. Then

```
T_j g(n)=h(3*2^a*n+c).
```

If 3 does not divide c, choose v=1 for c=2 mod3 and v=2 for c=1 mod3.
The number t=(2^v*c-1)/3 is odd and satisfies0<=t<2^(a+v). Applying
the odd-source identity at x=2^(a+v)*n+t gives

```
T_j g=B_(a+v,t)h in K.                            (5)
```

Indeed 3x+1=2^v*(3*2^a*n+c), and the even-source identity removes
that factor. No assertion that v is the complete odd-arrow valuation is
needed: the target itself can be even. The possible x=1 case obeys the
same value identity by h(4)=h(1).

If 3 divides c, put t=c/3, with0<=t<2^a. Then

```
T_j g=B_(a,t)f_1 in K union {f_1},                 (6)
```

by (4). This proves (3) for every binary state and all three sections,
without a bound on a or an enumeration of automata.

## 4. Every pure-zero ternary orbit is finite

For t>=0 put f_t(n)=h(3^t*n). For positive odd u, odd-source invariance
and t+1 successive applications of (1) give

```
h(3^t*u)=h(3^(t+1)*u+1)=h(4^(t+1)*u+1).
```

Consequently

```
f_t(2n)=f_t(n),
f_t(2n+1)=h(2^(2t+3)*n+2^(2t+2)+1) in K.         (7)
```

The second line denotes a member of K as a function of n. A function
f_t on positive integers is uniquely determined by this odd section,
because every positive integer has a unique odd part. All f_t also
have the same prescribed value at0. Thus

```
|{f_t:t>=0}| <= |K|.                              (8)
```

In particular the orbit under repeated T_0 is eventually periodic as
an orbit of functions: once f_s=f_t with s<t, applying T_0 repeats
that equality forever. This does **not** say that h is eventually
periodic as a sequence in n.

## 5. The exact remaining closure gap

If f_1 were already a member of K, proposition (3) would make K closed
under every ternary section. The ternary kernel would be finite. The
published [Cobham theorem](https://research.ibm.com/publications/on-the-base-dependence-of-sets-of-numbers-recognizable-by-finite-automata)
would then make the finite-valued h eventually periodic, and V002's
elementary component-coloring classification would force constancy.
This uses Cobham as a published input, not a theorem formally replayed here.

Membership f_1 in K is **not proved**. Adding f_1 to K gives a finite
binary-closed family, but (3) applies to the original K. It does not
automatically control T_1 f_1=h(9n+3) or T_2 f_1=h(9n+6). They are
individual automatic subsequences, which supplies no uniform bound for
all their subsequent ternary sections. Equation (8) controls repeated
zero digits only; mixed ternary words remain the unresolved obligation.

The missing sections can be organized without pretending that they close.
Put b_t(n)=f_t(2n+1), which belongs to K by (7), and
u_t(n)=f_t(3n+1), v_t(n)=f_t(3n+2). Their exact binary sections obey

```
u_t(2n)   =T_0 b_t(n),     u_t(2n+1)=v_t(n),
v_t(2n)   =u_t(n),         v_t(2n+1)=T_2 b_t(n).   (9)
```

The two boundary functions on the right belong to K union {f_1} by
(3). The two new functions form a mutually linked pair under the other
binary sections. These equations correctly describe a finite binary
presentation of each pair. They do not show that all subsequent ternary
sections of these pairs belong to one fixed finite family.

There is also no monochromatic binary cylinder supplied by these
identities. A finite kernel may have no constant state; h(2n)=h(n)
alone does not prevent that. For example, binary digit-sum parity has
that dilation invariance and a finite kernel, but fails the Collatz
identity at5, where its colors at5 and16 differ. It is a control on an
insufficient hypothesis, not a counterexample to the proposed theorem.

A sharper control supplied by the parallel [literature investigation](literature.md)
is

```
g(n)=+1 if oddpart(n)=1 or3 mod8,
g(n)=-1 if oddpart(n)=5 or7 mod8.
```

This is2-automatic: after skipping low zero bits, three bits determine
the odd part modulo8. Multiplication by3 permutes1,3 and separately5,7,
so g(2n)=g(3n)=g(n). Nevertheless g is not eventually periodic. To test
any proposed period P=2^a*m with m odd, take sufficiently large
n=c*2^k with k>a+3 and odd c chosen so g(c) differs from g(m). Then
oddpart(n+P)=c*2^(k-a)+m is m modulo8, so g(n+P)!=g(n).

Thus even a singleton pure-zero ternary orbit and both dilation
invariances do not supply eventual periodicity. This does not refute
the full target or proposition (3): g violates actual Collatz invariance
at3→5, where its colors differ. It also has constant binary cylinders,
unlike a hypothetical nonconstant invariant subject to the predecessor
sufficiency condition reviewed in the literature note.

## 6. Additive controls and assessment

For d=5 and61 the nonconstant periodic colorings1_(d divides n) remain
valid. They are2-automatic and have finite ternary kernels, so even a
successful two-base closure would not imply constancy at these d. The
last periodic-rigidity step has the genuine d=1 restriction.

The precise identities above also depend on +1. For general d, the
corresponding elementary identity is h(3m+d)=h(4m+d), with positivity
and the absorber checked. It cannot be replaced by (1). Thus these
controls are preserved rather than passed through an unchanged formula.

**First-pass result:** the closure problem is narrower than the initial
card suggested: the first ternary image of the entire binary kernel
adds at most one function, and pure powers of3 produce only finitely
many functions. This is a structural reduction, not full ternary closure
or a regularity result for the actual nonabsorbing set. A useful next
test must address the mixed sections of the extra function, or prove
its membership in K; counting more finite-state examples would not do so.

The bounded source search found standard primary references on automatic
sequences and Cobham's theorem but did not settle whether this particular
invariant-coloring question or the displayed reduction has appeared before.
No absence-of-prior-work or novelty claim is made.
