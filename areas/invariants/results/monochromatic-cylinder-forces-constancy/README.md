---
id: monochromatic-cylinder-forces-constancy
kind: result
title: An invariant colouring of 3x+d that is eventually constant on one dyadic residue class is constant
status: reviewed
claim: >
  Fix a positive odd d with 3 not dividing d. If h(2n) = h(n) for all n >= 1, h(3n+d) = h(n) for odd n > 1, and h is
  constant on all sufficiently large members of some residue class r mod 2^K (K >= 0), then h is constant. The proof
  shows that every positive odd target coprime to 3 has arbitrarily large predecessors, respecting absorption at 1,
  in every binary residue class. At d = 1 this is a known consequence of Monks's arithmetic-progression sufficiency
  theorem (which needs any one monochromatic progression, not only a dyadic one); it is not claimed as new.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
evidence:
  - "../digit-count-invariant-colourings-constant/verify_examples.py: V003's bounded replay includes cylinder examples (key cylinders of its receipt)"
  - "../digit-count-invariant-colourings-constant/literature.md, section L5: the published precedent (Monks 2006, Theorem 1.1; Monks-Monks-Monks-Monks, Theorem 4.1)"
reviewed_by:
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Predecessor construction, primitive-root step, absorber bound and colour-representative step re-derived; 68,580 constructed predecessor paths for d in {1, 5, 7, 13, 61} and the 3x+5, 3x+61 controls checked with independent code; verdict HOLDS, status raised to reviewed"
aliases: [V003-d]
tags: [invariants, colourings, sufficiency, cylinders, known-result]
---

# An invariant colouring of 3x+d that is eventually constant on one dyadic residue class is constant

## Statement

Fix positive odd d with 3 not dividing d. Suppose h(2n)=h(n) for all n>=1
and h(3n+d)=h(n) for odd n>1. If h is constant on all sufficiently large
members of any residue class r mod2^K, K>=0, then h is constant everywhere.

We show that every positive odd target a coprime to3 has arbitrarily large
predecessors in each binary residue class, respecting absorption at1. This
also explains transfer to d=5 and61. The stronger arbitrary-modulus d=1
statement does not transfer unchanged.

## Proof

### Exact predecessor construction

For this construction only, use the **raw shortcut** map: even n goes to
n/2, odd n to (3n+d)/2. Specify the first K parity bits of the residue r.
Because d is odd, these bits depend exactly on the input modulo2^K. If j
of the K branches are odd, the composition is

```
T_d^K(n)=(3^j*n+b)/2^K.
```

With odd positions 0<=t_1<...<t_j<K, the intercept is
b=d*sum_i 3^(j-i)*2^(t_i). For j>0 its last summand gives 3 not dividing b.
The word's source residue is the unique solution of 3^j*r+b=0 mod2^K.
This is a shortcut parity cylinder; it does not replace the extra bit
needed for an exact odd-valuation cylinder.

Powers of2 exhaust the units modulo3^j. Their order is 2*3^(j-1): the
base case holds modulo3; cubing 1+3^l*u with 3 not dividing u increases
its difference-from1 valuation from l to l+1. Choose arbitrarily large s
such that

```
2^(K+s)*a=b mod3^j,
n=(2^(K+s)*a-b)/3^j.
```

Then n is integral and belongs to the prescribed class modulo2^K. Take s
large enough that n>2^K. Every state in the first K branches is at least
n/2^K>1, so no raw outgoing arrow from the absorber is used. The endpoint
is 2^s*a; s even branches then reach a, with1 reached only at the end if
a=1. If j=0 the residue is0 modulo2^K and n=2^(K+s)*a gives the result
directly. K=0 is included. This gives arbitrarily large predecessors, not
a bound on their height or total time.

For any starting color, remove factors2. At an odd state other than1,
one odd arrow reaches a ternary unit because 3n+d is a unit modulo3.
The target1 is already a ternary unit. Thus every color has a representative
a as above; its predecessors in the monochromatic cylinder force that color
to agree with the cylinder's color. This proves the claim, including its
sufficiently-large version.

## Remarks

**Status in the legacy note:** "elementary rederivation of a known consequence." At `d = 1` this is covered by the stronger published arithmetic-progression sufficiency theorem ([`monks-2006-sufficiency`](../../../../sources/monks-2006-sufficiency.md), Theorem 1.1; see [literature.md](../digit-count-invariant-colourings-constant/literature.md#l5-one-monochromatic-progression-is-already-covered-by-sufficiency)): an invariant colouring constant on **any one** infinite arithmetic progression is constant. It is not a new theorem; its use is to identify which automatic descriptions are already eliminated by established work. The written proof above covers every positive odd `d` coprime to 3, where the arbitrary-progression `d = 1` statement does not transfer unchanged (the multiples of `d` form a monochromatic progression of the nonconstant control `1_{d|n}`).

### Automatic interpretation and controls

A constant binary-kernel member is a monochromatic cylinder, so an invariant
coloring with such a member is constant. In particular, a most-significant-
digit DFAO with a reset word sending every reachable state to one state gives
such a cylinder: append the word to any positive binary prefix. This is a
sufficient hypothesis, not an assertion that every automaton synchronizes.
Do not confuse that reading direction with the least-significant-digit kernel
automaton.

For d=5 and61, the invariant divisibility colors have no monochromatic binary
cylinder: the Chinese remainder theorem gives arbitrarily large multiples
and nonmultiples of d in every class modulo2^K. They pass this restriction
while remaining nonconstant. Their arbitrary-modulus progression of multiples
of d is monochromatic, so the stronger d=1 sufficiency theorem cannot transfer
unchanged.

**Usefulness:** eliminate constant-section/reset descriptions without an
automaton catalogue. **Limit:** automatic functions can lack every constant
section. For example, the Thue–Morse sequence t(n)=s_2(n) mod2 has every
binary section equal to t or its complement, so none is constant. It fails
the Collatz identity at5 and is only a control on the insufficient
automaticity hypothesis.

The separate [scaling counterexample](../digit-count-invariant-colourings-constant/literature.md#l6-two-scaling-invariances-do-not-imply-periodicity)
does have constant binary sections, such as g(8n+1)=+1. Its role is to
refute inference of full ternary-kernel finiteness from binary automaticity
and dilation invariances alone. It also fails actual Collatz invariance;
neither example is a nonconstant invariant under all the stated hypotheses.

## History

- Migrated from `experiments/viewpoints/V003/cylinder_rigidity.md` (legacy ID V003; report §4, "Monochromatic cylinders") at commit `be73a66`, by the B16 migration (Claude, Opus 5.5). Text kept; the opening status paragraph moved into Remarks.
- Main lane (ChatGPT/Codex), 2026-10-18, main commit `2ac44ef`. Main-lane review only (`../digit-count-invariant-colourings-constant/PROOF_REVIEW.md`).
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. Moved from `monochromatic-cylinder-forces-constancy.md` into this folder to hold the review; the three body links got one more `../`, no text changed (the evidence paths were already written relative to a folder).
