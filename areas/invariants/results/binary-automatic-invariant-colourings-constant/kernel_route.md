# V004 — Positive binary sections close under ternary sections

**Status: written proof, independently derived/audited in the kernel lane.**
The argument covers arbitrary finite binary kernels. Its external theorem is
Cobham's two-base automaticity theorem. It does not establish that an actual
Collatz component indicator has a finite binary kernel. Novelty is undetermined.

This note audits the positive-offset idea supplied by the parallel controls
lane and supplies an elementary finish to the odd-section periodicity argument
proposed by the main lane. It supersedes the proposed need to close mixed
sections of `f_1` as a route to the full classification; the V003 statements
themselves remain valid.

## 1. Objects and conventions

Let `h:N_{>0}->C` be finite-valued and binary automatic, with

```
h(2n)=h(n)       (n>=1),
h(3n+1)=h(n)     (odd n>1).
```

The absorber is1. The omitted color equation at odd source1 follows from
`h(4)=h(1)`, without changing the absorbing dynamics. Set `h(0)=h(1)` to
use sequences indexed by nonnegative integers. A finite change at0 preserves
automaticity. Sections do not carry a Collatz time interpretation.

The finite family to retain is

```
K_+ = { n -> h(2^a*n+r) : a>=1, 0<r<2^a }.
```

It is a subset of the finite binary kernel, although h itself need not be in
this subset. Its binary sections remain in it, since the new offset is
`r+2^a*j` for j=0,1. Positivity of the offset is the crucial retained datum.

## 2. Structural gain: exact ternary closure

V003 proves, for m>=0,

```
h(3m+1)=h(4m+1),
h(3m+2)=h(2m+1),
```

and, for positive odd u,

```
h(3u)=h(9u+1)=h(12u+1)=h(16u+1).                 (A)
```

Take `g(n)=h(2^a*n+r)` in K_+ and j in{0,1,2}. Write
`c=2^a*j+r`; then `0<c<3*2^a` and

```
g(3n+j)=h(3*2^a*n+c).
```

If3 does not divide c, take v=1 when c=2 mod3 and v=2 when c=1 mod3.
The integer `t=(2^v*c-1)/3` is odd and satisfies `0<t<2^(a+v)`.
The odd-source identity and doubling give

```
h(3*2^a*n+c)=h(2^(a+v)*n+t),
```

which is a positive binary section. The possible source1 satisfies the color
identity by the convention already checked above.

If3 divides c, write `t=c/3=2^ell*u`, with u positive odd. Since
`0<t<2^a`, we have `ell<a`; put `s=a-ell>=1`. Doubling and(A) give

```
h(3*2^a*n+c)
 = h(3*(2^s*n+u))
 = h(2^(s+4)*n+16u+1).
```

Here `0<u<2^s`, so `0<16u+1<2^(s+4)`. This again belongs to K_+.
The odd source `2^s*n+u` is positive for every n>=0.

Consequently **K_+ is closed under all three ternary sections**. The
exceptional zero-offset family from V003 never appears. In particular the
ternary kernel of every member of K_+ is finite, as is its binary kernel.

Two small arithmetic examples of the two branches are

```
h(12n+5)=h(8n+3),
h(12n+3)=h(64n+17).
```

These are exact function identities under the hypotheses, not empirical
agreement over an initial interval.

## 3. Cobham gives periodicity of the odd section

Apply [Cobham's theorem, as stated in Adamczewski–Bell, section2,
Theorem2.1](https://arxiv.org/html/1303.2019#S2), separately to each color
fiber of a member of K_+. A fiber is recognizable in both bases2 and3;
these bases are multiplicatively independent. It is therefore ultimately
periodic. Finitely many fibers have a common eventual period and cutoff.

In particular `b(n)=h(2n+1)` is eventually periodic. This step does **not**
say that h already has a finite ternary kernel; that stronger claim is
unnecessary. Cobham is an imported published theorem, not formally replayed
in this note. The primary-source statement was already checked in V003.

## 4. Elementary finish: periodicity on odd inputs suffices

The following argument avoids importing progression sufficiency as an
additional theorem.

For every positive odd x, the identities imply

```
h(4x+1)=h(3x+1)=h(x).
```

Thus `b(4n+2)=b(n)` for all n>=0. Suppose b has eventual period M, write
`M=2^e*L` with L odd, and let `G(n)=4n+2`. For any n>=0 choose k large
enough that `G^k(n)` lies past the eventual cutoff and `2^e` divides `4^k`.
Then

```
G^k(n+L)-G^k(n)=4^k*L
```

is a multiple of M. The eventual period and repeated G-invariance show
`b(n+L)=b(n)`. Hence L is a global odd period of b.

Because2 is invertible modulo L, there is a coloring q of `Z/LZ` such that
`h(x)=q(x modL)` for every positive odd x. Taking sufficiently large odd
representatives of each residue gives the identities, for every residue x,

```
q(4x+1)=q(x),
q(3x)=q(16x+1)=q(4x).                            (B)
```

The middle equality uses(A). In particular, with `H(x)=3*4^(-1)*x` in
`Z/LZ`, the second identity says `q(H(x))=q(x)`.

Write `L=3^e3*m`, with m coprime to6. If x=y modm, then
`H^e3(x)=H^e3(y)` modulo L. H-invariance shows that q factors through m.
The same(B) identities descend to this quotient. If m=1, q is constant.
Otherwise H and `J(x)=4x+1` are both invertible on `Z/mZ` and preserve q.
Their compositions are

```
H(J(x))=3x+3/4,
J(H(x))=3x+1.
```

Both have color q(x). Since multiplication by3 is invertible modulo m,
this gives `q(y+1/4)=q(y)` for every residue y. Translation by the unit
`1/4` generates the whole additive group, so q is constant. Thus h is
constant on odd positive integers, and doubling invariance makes it
constant on all positive integers.

This proves the requested full classification, conditional only on the
stated published Cobham theorem, with no bound on the automaton size.

## 5. Known-cycle controls and genuine additive dependence

For d=5 and d=61, the explicit nonconstant periodic colorings
`h_d(n)=1_(d divides n)` satisfy doubling and `3n+d` invariance, including
the absorber convention. They are binary automatic and have finite
ternary kernels. They do not satisfy the +1 identities used here.

The final residue calculation exposes exactly the relevant parameter: if
the corresponding identities are available with `J_d(x)=4x+d`, then

```
J_d(H(x))-H(J_d(x))=d/4.
```

At modulus d this translation is zero, and the coloring distinguishing
zero from nonzero residues survives. For d=1 it is a unit translation.
This is an arithmetic control on the actual argument, not a cycle replay
substituted for checking its hypotheses. No d=5 or d=61 extension of the
positive-section closure lemma is asserted here; its inverse offset
`(2^v*c-d)/3` need not have the positive-offset bounds used above.

The V003 odd-part character also remains a valid scoped counterexample:
it satisfies doubling/tripling invariance but fails the +1 identity at3.
It therefore cannot be substituted into the hypotheses of this proof.

## 6. Unresolved gap, next test and milestone

- **Objects:** finite binary kernels of invariant finite-valued colorings;
  the retained subfamily has strictly positive offsets.
- **Structural gain:** that subfamily is closed under every ternary
  section. This covers all automaton sizes at once.
- **Translated unresolved gap:** none within the stated classification
  after Cobham is supplied. Regularity of actual component indicators is
  wholly separate and unproved.
- **Worked example:** the two exact identities in section2 exercise both
  branches, including the former divisible-by3 exceptional case.
- **Known-cycle controls:** section5 identifies the +1 dependence and
  the surviving d=5/d=61 residue colors.
- **Cheapest meaningful next test:** independently audit the offset bounds,
  zero-extension convention, two-base theorem hypotheses and finite-residue
  argument. A bounded arithmetic script can check the conversions; it is
  supplementary evidence, not the universal proof.
- **Intermediate milestone:** the full finite-state classification is
  genuinely weaker than Collatz. It excludes finite binary memory as a
  description of a nontrivial invariant coloring; it supplies no such
  description for an arbitrary component.

No additional automaton catalogue, assumption about a nonabsorbing set,
trajectory-density estimate or discarded boundary function is used.
