# V003 — Literature baseline for binary-automatic invariant colorings

**Status: bounded primary-source check, 2026-10-18.** Read against main
`c47d91b`, the current `README.md`, and
[V13](../V002/invariant_colors.md). No novelty claim and no classification
of the single-base automatic case is established by this note. Search
results advertising Collatz proofs or repository assertions were not adopted.

## Exact question and outcome

Let h take finitely many values on positive integers and satisfy

```
h(2n)=h(n)                 for every n>=1,
h(3n+1)=h(n)               for every odd n>1.
```

Assume its binary representations are read by a finite automaton with output.
Must h be constant? This concerns colors indexed by **starting integers**,
not the parity word along one trajectory, not a finite-depth ancestor
language, and not the automatic presentation of the one-step graph.

**Bounded-search outcome:** no primary theorem answering this exact
single-base question was located. This is a search limitation, not a claim
that the question is new or open in the literature. Verified nearby theorems
and their missing hypotheses are listed below. None currently closes it.

## L1. Fixed-depth regularity is established prior work

[Stérin, *Binary expression of ancestors in the Collatz graph*, v4,
Theorem 1 and introduction](https://arxiv.org/html/1907.00775v4), proves
regularity for every fixed target x and fixed number k of odd shortcut
branches, with any number of even branches. Its regular expression has
star height 1 and alphabetic width `O(2^k 3^(k(k+1)/2))`. The paper credits
Shallit–Wilson for the earlier regularity argument.

**Scope check:** the fixed integer k is part of the theorem. The whole basin
uses an unbounded union over k; countable unions of regular languages need
not be regular. A coloring invariant under every arrow is a different
object from the recognizer for one fixed budget. The original
Shallit–Wilson article was not obtained in this pass, so its scope is
reported through the directly read Stérin source, not as an independent
inspection of that older article.

## L2. Rational inverse-orbit series: a close precedent for periodic rigidity

[Bell–Lagarias, *3x+1 inverse orbit generating functions almost always have
natural boundaries*, Acta Arithmetica 170 (2015), Theorem 1.1,
pp. 104–105](https://www.impan.pl/shop/publication/transaction/download/product/82190)
concerns a **finite union of backward orbits** for `3x+k`, `k=±1 mod6`.
Its positive-integer generating series is rational exactly when its
coefficients eventually describe a union of residue classes modulo `|k|`.
Those classes are closed under multiplication by 2 and 3. Theorem 1.2
also distinguishes the inverse basin of 1 from most other inverse orbits
using rationality versus a natural boundary.

This is substantial prior context for the repository's periodic-color
classification. It is not the requested automatic-color theorem: an
arbitrary color class need not be a finite union of inverse orbits, and
binary automaticity does not imply rationality of its integer-indexed
generating series.

An especially important distinction is between

```
sum_(n in A) z^n
```

and the length-counting series of the binary language for A. Regularity
gives rationality of the latter, not automatically the former. For example,
positive powers of 2 have regular binary language `10*`, but their
integer-indexed series `sum_(j>=0) z^(2^j)` is nonrational: its 0–1
coefficients have arbitrarily long zero gaps and are not eventually
periodic. A natural boundary therefore does not by itself refute
binary automaticity. This example is an elementary scope check, not an
invariant Collatz coloring.

## L3. Cobham is applicable after a genuine second-base theorem

[Adamczewski–Bell, *A problem about Mahler functions*, §2,
Theorem 2.1](https://arxiv.org/html/1303.2019#S2), states Cobham's theorem:
a set recognizable in two multiplicatively independent bases is eventually
periodic. Applying it separately to each color fiber would prove that a
coloring automatic in both bases 2 and 3 is eventually periodic. V13's
elementary argument then forces constancy at d=1.

The missing premise is **3-automaticity of the whole coloring**. Closure of
2-automatic sequences under each fixed affine subsequence does not bound the
number of distinct ternary subsequences as their depth grows.

[Mol–Rampersad–Shallit–Stipulanti, *Cobham's Theorem and Automaticity*,
§§1–2](https://arxiv.org/html/1809.00679v2) supplies quantitative comparisons
once both base automata exist. Its normalization procedure and common-prefix
results do not construct the missing ternary automaton from the guarded
Collatz identity. This prevents mistaking a large finite agreement check for
an unbounded closure theorem.

The broader substitution theorem of Durand, *Cobham's theorem for
substitutions*, was located at [arXiv:1010.4009](https://arxiv.org/abs/1010.4009).
Only its abstract was accessible during this pass. It requires two
substitutive descriptions with multiplicatively independent Perron numbers;
no second description is presently supplied here. It is a bibliographic
lead, not an additionally verified applicable theorem.

## L4. Mahler rationality offers a weaker sufficient second structure

Adamczewski–Bell's directly read **Theorem 1.1** states that, over a field
of characteristic zero, a formal series that is both k-Mahler and l-Mahler
for multiplicatively independent k,l is rational. Here “l-Mahler” requires
a nontrivial finite polynomial-coefficient relation among
`F(z),F(z^l),...,F(z^(l^r))`; see their Lemma 4.1.

Apply this over Q to an individual 0–1 color indicator f. Binary
automaticity supplies a 2-Mahler series `F(z)=sum_(n>=0)f(n)z^n`.
A **3-Mahler equation**, if independently derived, would already suffice;
full 3-automaticity is stronger than this analytic requirement. Rationality
and the finite coefficient alphabet give eventual periodicity, then V13
gives constancy. No 3-Mahler equation has been derived in this note.

This theorem is characteristic-zero. One cannot replace its hypotheses by
the automatic-series/algebraic-series correspondence in characteristic 2
without proving a valid bridge back to characteristic zero.

## L5. One monochromatic progression is already covered by sufficiency

[K. M. Monks, *The sufficiency of arithmetic progressions for the 3x+1
Conjecture*, Theorem 1.1, Proc. AMS 134 (2006), 2861–2872](https://www.researchgate.net/publication/238083063_The_sufficiency_of_arithmetic_progressions_for_the_3x_1_conjecture)
proves that every nonconstant arithmetic progression is sufficient:
every positive integer merges with an element of that progression. The
theorem statement and definition were read in the article's fulltext
transcription; the publisher PDF was unavailable through this browser.

Consequently, an invariant coloring that is constant on **any one infinite
arithmetic progression** is constant everywhere. This deduction does not
require automaticity. A monochromatic dyadic cylinder is a special case,
so an elementary inverse-density proof of that case is a rederivation of
a consequence of established sufficiency, not an additional novelty claim.
The exception at 1 does not obstruct the deduction: doubling already gives
the missing color identity there.

The original author also coauthors [Monks–Monks–Monks–Monks, *Strongly
sufficient sets and the distribution of arithmetic sequences in the 3x+1
graph*, introduction and Theorem 4.1](https://arxiv.org/html/1204.3904v2).
Its directly read fulltext confirms the stronger input: each positive
target coprime to 3 has a backward path into every prescribed residue
class. Section 4 adds modulus-dependent bounds on the number of odd
inverse branches; it does not bound the total shortcut length by the same
quantity. Thus backward density of ternary-unit targets in dyadic
cylinders also has explicit published precedent.

This supports the proposed constant-section/synchronizing subclass, but
does not show that every binary-automatic invariant has a monochromatic
progression. No exact prior statement classifying invariants of the form
`h(n)=F(s_2(n))` was located in the brief additional search; that negative
search outcome does not establish novelty of the digit-sum calculation.

## Exact interface: what the guarded equations presently supply

The following is our elementary transcription, not a published theorem
being imported. At d=1 the omitted n=1 equation is already consistent with
doubling: `h(4)=h(1)`. Substituting the odd inputs `2m+1` and `4m+1` gives

```
h(3m+2)=h(2m+1)             for every m>=0.
h(3m+1)=h(4m+1)             for every m>=0.
```

For a color indicator f, set f(0)=f(1). Define the
section operator `Lambda_(b,r) F = sum_(n>=0) f(bn+r) z^n`. Then

```
Lambda_(2,0) F = F,
Lambda_(3,2) F = Lambda_(2,1) F.
Lambda_(3,1) F = Lambda_(4,1) F.
```

Thus both nonzero ternary sections of h are binary-kernel sections.
The subsequent [kernel probe](kernel_probe.md), sections 3–4, strengthens
this further. Writing `K=K_2(h)` and `f_t(n)=h(3^t n)`, it proves

```
T_j(K) subset K union {f_1},             j=0,1,2,
f_t(2n)=f_t(n),
f_t(2n+1)=h(2^(2t+3)n+2^(2t+2)+1) in K,
|{f_t:t>=0}| <= |K|.
```

Here T_j sends a sequence g to `n -> g(3n+j)`, and the displayed
membership in K concerns the entire sequence in n. This is an exact
finite-family statement, not agreement below a finite cutoff. The
first ternary image of K has at most one extra state, and the pure-zero
ternary orbit is finite. Mixed ternary sections of the extra state remain
uncontrolled. Neither full ternary closure nor a finite 3-Mahler relation
follows yet. The counterexample below shows why pure-zero finiteness alone
cannot replace that missing mixed-section argument.

## L6. Two scaling invariances do not imply periodicity

**Refuted auxiliary statement, with a written counterexample.** Binary
automaticity together with `g(2n)=g(n)` and `g(3^p n)=g(n)` does not force
eventual periodicity, even when p=1. This refutes only the proposed
scaling-only shortcut; it does not refute the original guarded problem.

Write `n=2^v m` with m odd, and put

```
chi(m)=+1   for m=1 or3 mod8,
chi(m)=-1   for m=5 or7 mod8,
g(n)=chi(oddpart(n)).
```

The formula defines g on positive integers. For the usual kernels indexed
by n>=0, set `g(0)=g(1)=+1`; oddpart(0) is never used. This extension
preserves both scaling identities at 0 as well.

For the full periodic character, set chi=0 on even integers. This is the
Dirichlet character modulo 8 associated with -8. The construction is a
special case of [Konieczny–Lemańczyk–Müllner, *Multiplicative automatic
sequences*, Lemma 8 and Theorem 1](https://link.springer.com/article/10.1007/s00209-021-02834-3).
Lemma 8, read in full, states that the p-free-part extension of an
eventually periodic multiplicative function is p-automatic. The present
example can also be checked directly, without importing that result:

- For a binary section `g(2^e n+r)`, r=0 leaves g unchanged.
- If `r=2^a u>0` with u odd and a<e, the section is
  `chi(2^(e-a)n+u)`. Modulo 8, this gives only finitely many functions.
- Doubling leaves oddpart unchanged. Multiplication by 3 permutes
  `{1,3}` and `{5,7}` modulo 8, so g is also invariant under tripling.

**Not eventually periodic.** Let any proposed period be `M=2^a m`, m odd.
Choose u=1 or5 with `chi(u) != chi(m)`, and let `n=2^(a+k)u` for arbitrarily
large k>=3. Then

```
g(n)=chi(u),
oddpart(n+M)=2^k u+m = m mod8,
g(n+M)=chi(m).
```

This contradicts periodicity beyond any proposed threshold. In contrast,
the original Collatz identity fails already at n=3: `g(3)=+1` whereas
`g(10)=-1`.

**The full ternary kernel really is infinite.** More precisely, the
sections `n -> g(3^t n+1)`, t>=1, are pairwise distinct, although every
pure-zero section `g(3^t n)` equals g. Here t>=1 ensures offset 1 is a
valid ternary-kernel residue; at t=0 only offset 0 is valid. For distinct
t,s>=1, write
`Delta=3^t-3^s=2^a D`, with D an odd, possibly negative integer. Choose
K>a+3. By the Chinese remainder theorem choose a positive odd v satisfying

```
2^K v = 1 mod3^t,
chi(v) != chi(D),
```

where the second condition is achieved by v=1 or5 modulo 8. Take v large
enough that `n=(2^K v-1)/3^t` is positive. Then

```
g(3^t n+1)=g(2^K v)=chi(v),
3^t(3^s n+1)=3^s 2^K v+Delta
                =2^a(3^s 2^(K-a)v+D).
```

The last parenthesis is positive and odd, and is D modulo 8. Invariance
under multiplication by `3^t` therefore gives
`g(3^s n+1)=chi(D)`, the opposite value. This is an exact separation of
pure-zero orbit finiteness from full-kernel finiteness, not just an
absence of a theorem in the search.

The explicit scaling counterexample and section-separation calculation
above are elementary checks made in this batch. The cited paper supplies
the encompassing automatic family; it is not being credited with this
exact Collatz-route counterexample. No novelty claim is made for either.

## Recommended bounded next step

1. Keep the binary-kernel investigation, but name the full finite family
   whose closure under **all three** ternary sections is being claimed.
2. In parallel, ask the weaker algebraic question: can those identities
   generate a finite 3-Mahler relation for each color indicator? Retain
   every auxiliary section; do not eliminate an unknown section by assumption.
3. Treat regular-language and transducer calculations as exact checks of
   a proposed finite closure, not as evidence that some closure must exist.

Do not infer regularity of an actual nonabsorbing-set indicator from any
of these sources. A successful classification of automatic invariant
colorings would only rule out that particular description of a hypothetical
obstruction. It would still leave more complicated colorings possible.
