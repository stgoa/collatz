# The exact critical domain for tripling-pair currents

2026-10-17. **Written equivalence and conditional finite compiler; bounded
checks.** Neither universal pair existence nor Collatz convergence is proved.
No novelty or formal verification is claimed. This note uses only the proved
[elementary normal form](../bridge_normal_form/BRIDGE_NORMAL_FORM.md) and
ordinary Syracuse arrows. It sharpens the scope discussion in
[the general pair decomposition](../pair_scope/PAIR_SCOPE.md).

Write `S(x)=(3x+1)/2^v2(3x+1)` on positive odd integers, with S(1)=1 for
path algebra. Kill state1 in measures and currents. For a finite integer
current J, `div J=(I-S_*)J`. Write `[x]` for the killed point mass and

```
P(w)=[3w]-[w],       F(x)=4x+1.
```

Here P(w) is a signed **source**, not an already supplied current. An exact
pair current must have precisely that divergence. No synchronised merger
clock is required by this note.

## 1. Elementary components and the remaining induction seeds

Recall the canonical set B:

* q=1 modulo8;
* q=2^a t-1 with a>=2, t positive odd, and t=-3^a modulo4.

The second class consists of the complementary roots. The complete proved
elementary component of q is the pair of F-rays

```
C_q={F^j(q), F^j(2q+1): j>=0}.
```

Its least member is q. Write nu(x) for this canonical minimum, and N_x for
the proved finite elementary current with
`div N_x=[x]-[nu(x)]`. The partner 2q+1 is selected, so
`nu(2q+1)=q`. In general a root `x=2^a t-1`, a>=2, is selected when
`t=3^a modulo4`; its half `(x-1)/2` is canonical and is its minimum.
These facts are proved in the linked normal-form note, not premises about
unproved tripling pairs.

Three kinds of seed already admit a reduction to a smaller positive odd
integer:

1. A noncanonical x has `nu(x)<x` through N_x.
2. A canonical q=1 modulo8, q>1, has `S(q)<= (3q+1)/4<q`.
3. A canonical q=2 modulo3 has the positive odd predecessor
   `p=(2q-1)/3<q`, with `3p+1=2q`, hence `S(p)=q` exactly.
   Its reverse arrow is the signed current `-delta_p` with divergence
   `[q]-[p]`.

Consequently the only remaining least-counterexample seeds are

```
C={q in B: q=3 modulo4 and q is not2 modulo3}.          (1)
```

This is a reduction of the possible least counterexample, not a claim that
each earlier operation decreases on every unrestricted orbit.

## 2. A bijection with two binary tripling domains

Define

```
W={w>0 odd: w=5 modulo8 or w=9 modulo16},
g(w)=nu(3w).                                          (2)
```

**Theorem.** The map g is a bijection from W onto C. Every w in W satisfies
`w<g(w)`. Its inverse is

```
w=q/3,          q in C and q=0 modulo3;
w=(2q+1)/3,     q in C and q=1 modulo3.                 (3)
```

**Proof.** If w=9 modulo16 then 3w=11 modulo16. This is complementary
with a=2, so `g(w)=3w`, a member of C divisible by3.

If w=5 modulo8 then 3w=7 modulo8, an F-root with a>=3. If it is
complementary, `g(w)=3w` belongs to C and is0 modulo3. Otherwise it is
selected; its canonical half `(3w-1)/2` has exponent a-1>=2 and therefore
is complementary rather than1 modulo8. This half is1 modulo3. Both
possible images are strictly larger than w, since w>=5.

Conversely, take q in C. When q=0 modulo3, put w=q/3. If q has a=2,
complementarity says q=11 modulo16, hence w=9 modulo16. If a>=3,
q=7 modulo8 gives w=5 modulo8. In both cases `nu(3w)=q`.
When q=1 modulo3, put w=(2q+1)/3. Because q=3 modulo4,
`2q+1=7 modulo8`, hence w=5 modulo8. Its triple is the selected partner
2q+1 and has minimum q. The image's residue modulo3 distinguishes the
two formulas, proving uniqueness. Every operation is on positive odd
integers, and both formulas in (3) give w<q. This proves the theorem.

The apparent binary simplicity of W does not mean that its tripling
currents are known. For instance its first inputs include5,9,13,21,25.

## 3. Restricted universal tripling is already Collatz-equivalent

The following statements are equivalent:

1. Every positive odd integer reaches1 under S.
2. For every w in W there is a finite integer current J_w with
   `div J_w=P(w)`.
3. For every positive odd w there is such a current J_w.

There is no uniform cost, support-height, clock, or computability assumption
in statement2. Each current is finite; its size may depend arbitrarily on w.

**Proof.** Statement1 supplies finite absorption path currents H_x, and
`J_w=H_(3w)-H_w` proves statement3. Statement3 implies statement2.

Assume statement2. Use strong induction on the positive odd source x.
Apply the smaller-seed reductions in Section1 whenever possible. In the
remaining case x=q in C, the unique w from (3) is smaller than q. The
supplied pair current and the elementary current at its upper endpoint give

```
div (J_w-N_(3w)) = [q]-[w].                           (4)
```

Add the already proved absorption current of w. This constructs a finite
integer current with divergence `[q]`. The same construction works in the
other three induction cases, and x=1 requires the zero current.

For completeness, a finite current with divergence `[x]` forces actual
absorption of x. In the finite graph of its nonzero current arrows and their
endpoints, summing divergence over a component not meeting1 gives zero.
Thus the component containing x must meet1. Every edge is an actual
deterministic S arrow; any finite undirected path to the absorbing state
implies that the forward orbit of x joins the orbit of1. Hence x reaches1.
This completes the implication to statement1.

The theorem identifies the precise missing comparison interface in this
induction. Completing it is a full-strength convergence problem, not a proved
helper lemma. Proved partial constructions on W can still be useful if they
leave a smaller, explicitly described unresolved family.

## 4. All tripling edges connect the complete elementary identity graph

For a separate operation-set statement, form an undirected **formal** graph
using all proved elementary identities and an added edge `3w--w` for every
positive odd w. Ordinary S arrows outside the elementary identities are
not needed in this paragraph. The graph is connected, and it has the
following terminating normalizer.

First reduce x to q=nu(x). Stop at q=1. For q>1 use the appropriate row:

| q modulo3 | formal path | smaller endpoint v | required pair base |
|---|---|---|---|
|0|q=3v -- v|q/3|v|
|1|q -- 2q+1=3v -- v|(2q+1)/3|v|
|2|q -- F(q)=3u -- u -- v|(2q-1)/3|u=(4q+1)/3|

The first and third moves in the final row are proved elementary moves.
To check the last move, it remains to prove u is selected. If q=1 modulo8
and q=2 modulo3, then q=17 modulo24 and u=23 modulo32. Thus u has a=3
and odd part3 modulo4, exactly the selected condition. Otherwise write
q=2^a t-1 complementary. Since q=2 modulo3, t is divisible by3, and

```
u+1=2^(a+2)(t/3),
t/3 = 3t = -3^(a+1) = 3^(a+2) modulo4.
```

So u is selected and its minimum is v=(u-1)/2. This also proves v is
canonical in that row. In every row v is positive odd and v<q.
Normalize v and repeat. This proves connectivity even when intermediate
vertices exceed the original input.

More quantitatively, every row has

```
v-1 <= (2/3)(q-1).                                    (5)
```

Thus the number of formal tripling invocations is logarithmic in the starting
height: if at least r invocations occur, then
`2 <= (2/3)^(r-1)(x-1)`. This bounds only the number of missing inputs
requested by a formal plan. It bounds neither the cost of J_w nor the work
needed to discover it. The algorithm terminates as a **conditional plan**;
its actual current is obtained only after all its missing pair inputs are
supplied and checked.

This statement includes selected-halving identities. No connectivity theorem
is asserted here for the smaller graph generated by F and tripling alone.
Nor does it contradict the earlier disconnected graph that grants tripling
only at w=3 modulo8: the operation sets differ.

## 5. Executable boundary checks and finite evidence

`tripling.py` implements both decreasing plans. For each local step from x
to v it returns an explicit elementary/ordinary current C and either no
missing input or a specified w, with the checked exact boundary

```
div C=[x]-[v]-P(w).
```

The plan retains every occurrence of a missing pair. Its total boundary is
`[x]-sum P(w)`. `compile_plan` accepts only explicitly supplied currents,
checks every pair divergence, and adds them with positive orientation.
Missing or incorrect inputs cause an error. Current-row cancellation is
performed exactly, with state1 killed.

The bounded checker verifies local boundaries, the finite portions of the
bijection in both directions, complete decreasing plans, and compiled
absorption examples. The demonstration input currents are obtained by capped
ordinary absorption searches on explicitly bounded sample inputs; those
searches prove only their finite examples. The stored receipt includes exact
final current tables for selected examples, hashes of all other checked
rows, input bounds, and caps.

The default receipt checks16,384 local steps,6,144 inputs of W,2,731
critical inverse inputs,2,048 formal plans, and40 actual compiled examples.
The examples use34 distinct supplied pair currents. These are bounded
verification counts, not a universal pair construction.

Reproduce from the repository root:

```
python3 experiments/residual_progress/tripling_equivalence/check_tripling.py
```

The proof, not these finite tests, supplies the universal equivalence and
the formal plan's termination. No universal pair current is generated. The
construction certifies individual roots; it makes no simultaneous source
capacity claim for an annular submeasure. Ordinary arrow identities and the
elementary bridges specifically use3x+1; generalized odd maps are not
automatically covered by this theorem.
