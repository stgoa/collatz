# V005 — Independent review of the direct-section arguments

**Review status: PASS for the named partial results, 2026-10-18.**
This is an independent agent's algebraic review, not formal verification
or human peer review. The full superlinear-complexity goal remains open.

## Materials inspected

- [Direct-section note](direct_sections.md), Sections 1–4, including the
  quantitative reconstruction added to Section 2.
- [V003 cylinder predecessor construction](../V003/cylinder_rigidity.md).
- [V004 global finite-state rigidity](../V004/GLOBAL_RIGIDITY.md).

No historical mathematical result is corrected or replaced by this review.

## 1. Local automaticity forces global constancy — PASS

For `g(n)=h(2^K n+r)` with `K>=1` and `0<r<2^K`, the specified raw
shortcut word has at least one odd branch: an all-even K-step word has
source residue zero. Its intercept is

```
B = sum_(i=1)^j 3^(j-i) 2^(t_i),
```

where t_i are the odd branch positions. Its last summand is nonzero
modulo 3 and all earlier terms vanish modulo 3. Thus B, and consequently
`c=(3^j r+B)/2^K`, are ternary units. Also c>0.

For each unit residue a modulo M=3^j, the fact that 2 generates the unit
group supplies arbitrarily large s_a with `2^s_a a=c mod M`. Taking one
large enough makes `u_a=(2^s_a a-c)/M>=1`. Since a<M and c>0,
`u_a<2^s_a`. The proposed reconstruction therefore uses an actual binary
section of g, including its n=0 endpoint.

The affine substitution checks exactly:

```
T^K(2^K(2^s_a q+u_a)+r) = 2^s_a(Mq+a).
```

The source is greater than 2^K. Each raw shortcut branch decreases its
input by at most a factor 2, so all K branch inputs and their endpoint
stay strictly above 1. The remaining halving path reaches the target,
reaching 1 only at its final step if the target is 1. No outgoing arrow
at the absorber has been used.

Both closure arguments are valid for whole kernels. For affine extraction,
the quotient in division of Ar+B by 2^D has a fixed finite range. For
interleaving modulo M, split a section argument as Ml+t: the resulting
quotient offset lies in `[0,2^D)`, so each of the M pieces is an actual
kernel member of one of the original finitely many sequences. The tuple
of pieces determines the whole section.

Finally `b(n)=h(2n+1)=h(6n+4)` uses the guarded identity at positive odd
inputs; n=0 uses only the valid color equality h(1)=h(4). Removing the
power of 2 from a positive binary offset places its section in K_2(b),
while offset zero returns h. The passage from finite K_2(b) to finite
K_2(h), then to V004 constancy, is correct.

## 2. Quantitative reconstruction — PASS

The displayed constants satisfy the required domains:

```
a_t=(6t+4) mod M is a ternary unit,
0<=q_t=floor((6t+4)/M)<=5,
0<B_t=2^s_(a_t) q_t+u_(a_t)<6*2^s_(a_t)=A_t.
```

Consequently `b(Ml+t)=g(A_t l+B_t)` is exact. Splitting a depth-d section
of b into its M residue pieces gives `k(A_v l+q)`, where k is a depth-d
section of g and `0<=q<A_v`. Summing A_v over the M possible v bounds
the fixed transformations of each kernel member. Taking an M-tuple
therefore gives

```
kappa_b(D) <= (C_g*kappa_g(D))^M,
kappa_h(D) <= 1+(C_g*kappa_g(D-1))^M, D>=1.
```

The constants are fixed by the cylinder, and the count includes all depths
up to D. This is a genuine quantitative reconstruction bound, but its
polynomial exponent does not exclude linear growth. The note correctly
retains that limitation.

## 3. Descendant counting — PASS with its stated missing hypothesis

An infinite finitely branching reachable graph adds at least one new
vertex at every cumulative depth; a plateau would make the current set
closed and hence finite forever. Thus m pairwise disjoint infinite
descendant sets beginning by depth A give `m(D-A+1)` distinct sections.

The local automaticity lemma establishes infinitude of each positive
section's descendant set. It does not establish pairwise disjointness.
The note keeps these logically different assertions separate.

## 4. Infinite-state graph control — PASS

Reviewed the transition table in Section 4 of direct_sections.md:
`H:0->H,1->B`; `B:0->C,1->G_2`; `C:0->G_1,1->B`;
`G_t:0->G_t,1->G_(t+1)`.

The outputs on H,B,C,G_1 are all 1, so adding input zeroes after the last
significant bit preserves the value even along B->C->G_1. All G_t states
also preserve outputs on zero transitions. This is essential for a
well-defined sequence on nonnegative integers.

The identities `z(2n)=z(n)` and `z(8n+5)=z(2n+1)` follow from the initial
zero loop and the B->C->B return. For D>=3, every reached state lies in
`{H,B,C,G_1,...,G_D}`, giving the claimed upper bound D+3.

The G_t sequence is `F(t+s_2(n))`, with F indicating positive powers of
2. For t<u choose a power 2^k larger than u-t and at least t, then choose
n with digit sum 2^k-t. The two outputs differ. Hence the G_t states are
pairwise distinct as **whole functions**, independently of finite samples.
Each has infinitely many distinct G_t descendants; H,B,C each reach one.
Every binary section is therefore nonautomatic.

The least-significant-digit paths give `z(9)=1` and `z(28)=0` exactly.
Since 9 is a positive odd nonabsorbing input, this violates the full
guard `z(3n+1)=z(n)`. Thus the example refutes the reduced graph shortcut
and is not a counterexample to the active Collatz-specific goal.

## Overall disposition

Adopt the local automaticity lemma, the quantitative reconstruction bound,
and the graph-control counterexample with their stated scopes. Preserve
the full additive identities and the unresolved descendant-overlap
obligation. None of the reviewed statements establishes that
`sup_D kappa_h(D)/(D+1)` is infinite for a nonconstant invariant.

## Addendum — independent verifier replay and exact graph count

**PASS, 2026-10-18.** A second reviewer read the complete
[verifier](verify_examples.py), [saved receipt](verification.json),
[section graph proof](section_graph.md), and the sparse construction in
[the literature note](literature.md). The reviewer then ran
`python3 -B experiments/viewpoints/V005/verify_examples.py`; it exited 0
and matched the existing receipt without writing it.

### Actual reconstruction paths and receipt scope

The raw shortcut template at r is used only to obtain affine parity data.
Every checked witness starts strictly above 2^K, and the checker requires
every actual template step to start above 1. It then requires the prescribed
endpoint, verifies each suffix arrow is an even halving above 1, and checks
the exact target. Thus no raw template passage through 1 is mistaken for
an allowed path leaving the absorber. A failed exponent cap raises an error;
it is not counted as a completed witness.

The replay checked 224 cylinder/residue choices, 896 actual paths and
15,288 shortcut arrows for K=1,...,4 and q=0,...,3. It separately checked
5,040 exact affine tuple decompositions. These are bounded checks of the
written universal formulas, not independent proof of the universal
quantitative reconstruction inequality.

The default program reads its own source and the receipt, computes the
checks, and compares the full result. It writes a receipt only under the
explicit `--write-receipt` option. The stored source hash identifies the
replayed verifier. No external processes or network requests are made.
The receipt explicitly excludes proof of the full quantitative goal and
equality of unknown infinite sections.

### Entire-state distinctness and exact count — PASS

The stronger [graph proof](section_graph.md#3-distinctness-and-exact-linear-count)
correctly proves that H,B,C differ from every G_t: equality of whole functions
would imply equality of both digit sections, and the displayed transitions
would then force G_t=G_(t+1). The same transition argument separates H,B,C
from one another. This supplements the already proved pairwise distinctness
of all G_t and is necessary to turn a reachable-label count into an exact
whole-kernel count.

G_1 is reached by the least-significant-first word 100, and G_t for t>=2
by t consecutive ones. The transition graph adds no other states through
depth D. Therefore the written proof establishes exactly
`kappa_H(D)=D+3` for D>=3, with initial values 1,2,4. The replay checks
the reachable labels through depth 16, leading-zero compatibility, actual
section transitions, 120 G-state distinguishing witnesses and the claimed
identity values through input 1024. It explicitly checks the full-guard
failure H(9)=1 and H(28)=0. Finite label checks alone are not being offered
as proof of entire-state distinctness.

### Sparse and actual dynamical controls — PASS

The sparse checker implements exactly the indicator of `{6^(2^j):j>=0}`.
For a nonzero p-adic residue, e<a is necessary and distinct e have distinct
p-adic valuations, so the singleton-cell classification in the written
proof is correct. The checked pure-base counts are consistent with the
proved linear upper bounds; 59,823 actual cell evaluations supplement that
classification. The mixed test separates all 45 zero-offset sections with
a+b<=8 using 990 ordered witness comparisons. The shared support exponent
32 is larger than twice the tested depth, so a nonzero shift of size at
most 8 cannot produce another power of 2. The general quadratic lower bound
continues to rest on the written valuation argument.

The checker explicitly records the sparse example's failure of doubling
at 3 and 6. It also exercises actual d5/d61 invariant divisibility colors,
their odd fixed cycles away from absorber 1, and failure of the named d1
identity. These checks do not test hypothetical divergence or establish
the desired superlinear bound for a Collatz invariant.

**Disposition:** accept the replay receipt and exact graph counterexample
with these scopes. No verifier or mathematical correction was required.
The active goal remains open.

### Complete scalar interface — PASS

The direct-section reviewer also checked the three-equation interface in
[scalar_interface.md](scalar_interface.md). The converse's induction covers
odd n, n=0 modulo4 and n=2 modulo4; the last case uses only E(m) with m<n.
Doubling then gives the required odd-source invariant equation. Stripping
the binary valuation of a positive section offset gives the stated exact
kernel-family comparison. The interface preserves the full guard, but
does not establish the desired growth bound.
