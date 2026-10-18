# A whole decreasing critical phase, its returning branch, and an exhaustive inverse barrier

2026-10-17. **Written exact identities, a conditional decreasing constructor,
and a complete bounded-depth obstruction.** These results do not complete the
critical5-modulo8 pair domain or prove Collatz. They use the
[complete elementary quotient](../bridge_normal_form/BRIDGE_NORMAL_FORM.md),
the [critical-pair compiler](../tripling_equivalence/TRIPLING_EQUIVALENCE.md),
and the [complete critical9 elimination](../w9_closure/CRITICAL_NINE_ELIMINATION.md).
No novelty or formal verification is claimed.

Use positive odd integers and ordinary odd-only Syracuse S, with1 absorbing.
Kill state1 in measures and current rows. Write `[x]` for its killed atom,
`P(w)=[3w]-[w]`, `F(x)=4x+1`, and `div=I-S_*`. Let B be the canonical set,
nu the elementary minimum, and `T=nu S` on B. **A T step is explicitly a
quotient step**, not an extra ordinary-clock assertion: its finite current
can include a selected-halving bridge of unbounded length.

## 1. Every4-modulo9 target has a smaller exact ancestor

Let q>0 be odd and q=4 modulo9. Put

```
h=v3(2q+1)>=2,
p=2^h(2q+1)/3^h-1.
```

Then p is positive odd, p<q, and its **exact ordinary valuation word** is

```
1^(h-1),2;          S^h(p)=q.                          (1)
```

Indeed `p+1=2^h C` with `C=(2q+1)/3^h` positive odd. Its first h-1
arrows have valuation1, ending at `2*3^(h-1)C-1`. The next numerator is
`2(3^h C-1)=4q`, giving valuation exactly2. Also

```
p-q=[2^(h+1)/3^h-1]q + (2/3)^h-1 <0,
```

because h>=2. The negative of the p-to-q path current has divergence
`[q]-[p]`. If q is canonical, all states of this path are canonical:
the final reverse step is R25's canonical valuation2 predecessor, followed
by its complete valuation1 predecessor chain.

The shortest version already covers the entire phase:
`p_2=(8q-5)/9<q` has exact word(1,2). The longer choice in (1) consumes
the whole available valuation1 reverse run. For example q31 has p27;
this is a smaller-seed comparison, not a new absorption proof for27.

Thus a least unabsorbed canonical root cannot be4 modulo9. This is a
whole arithmetic phase, not a finite scan. It does not justify assuming
the absorption of p from a cutoff smaller than p.

## 2. The exact induced branch on critical W5 inputs

Consider the entire domain

```
E={w>0: w=5 modulo8, 3|w, and3w is selected}.          (2)
```

Write

```
h=1+v3(w)>=2,   u=w/3^(h-1),
q=(3w-1)/2,    p=2^h u-1.
```

Then q is canonical complementary, q=4 modulo9, and (1) gives p→q.
The integer p is also complementary canonical: w=1 modulo4 implies
`u=3^(h-1)=-3^h modulo4`. Moreover `p mod3` is0 or1. Its critical
pair index is therefore

```
v=p/3            if p=0 modulo3,
v=(2p+1)/3       if p=1 modulo3.                     (3)
```

The decisive comparison is

```
v <= (2^(h+1)u-1)/3 < (8/9)w.                      (4)
```

The final inequality follows from `2^(h+1)/3^h<=8/9` for h>=2.
Notice that p itself can exceed w: at h2, `p=4w/3-1`. Comparing p
directly with the pair parameter would be an invalid induction. The
smaller object in (4) is its **critical pair index**.

Let N_y denote the proved elementary current `[y]-[nu(y)]`, let A be
the negative path current in (1), and put z=nu(w)<w. The explicit current

```
C=N_(3w)+A-N_(3v)-N_w
```

has the exact boundary

```
div C=P(w)-P(v)-[v]+[z].                             (5)
```

Consequently adding a supplied P(v) current and the difference of supplied
absorption currents for v and z gives a P(w) current. Both absorption
seeds are smaller than w. All signs and repeated input multiplicities in
(5) are retained. This does not consume annular source capacity.

### Absorption from smaller W5 inputs

The R37 absorption plan for a seed s requests critical pair indices strictly
below s. Every W9 index b in that plan comes from a canonical target3b,
so `b<=s/3`. The complete W9 elimination requests only W5 indices at most
`(9b+3)/4`. These are at most `(3s+3)/4<s` for s>3. Seeds1 and3 have
elementary plans with no pair requests. Therefore a finite formal absorption
plan for s uses **only W5 indices below s**. This plan still needs those
currents supplied; its termination does not produce missing inputs.

### Complete decrease classification within E

The critical index v in (3) is W5 except in exactly one case:

| Domain inside E | v's domain | consequence after W9 elimination |
|---|---|---|
|h>=3, equivalently9 divides w|W5|all missing W5 inputs are below w|
|h=2 and u=2 modulo3, equivalently w=6 modulo9|W5|all missing W5 inputs are below w|
|h=2 and u=1 modulo3, equivalently w=3 modulo9|W9|an exact request for P(w) returns|

For h>=3, p has binary exponent at least3, so either critical inverse
formula gives W5. At h2, p=4u-1 has exponent2; its divisible-by3 branch
gives W9, while the other branch gives W5. This proves the table exhaustively.

Hence (5), together with the smaller absorption plans, is a **complete
strictly decreasing conditional constructor** on the first two rows. It
returns a finite signed sum of strictly smaller W5 pair requests and an
explicit current. It is not a constructor for every W5 input: the other
W5 classes and the returning row remain unresolved.

**Sufficient-set refinement.** Put
`E_good=E intersect {w not3 modulo9}`. It is enough to supply universal
finite P currents only on `W5 minus E_good`. Indeed, use strong induction
on the positive W5 index w. Outside E_good the current is a premise;
inside E_good the strict-smaller plan just proved supplies it from currents
already constructed in the induction. This yields all W5 currents, and the
complete W9 elimination and R37 then imply Collatz. Conversely Collatz
supplies these restricted currents. Thus the refined premise is equivalent
to Collatz. This removes an entire domain without assuming any omitted
current; it retains the returning w3-modulo9 row and every other unresolved
W5 class.

## 3. The returning row is an exact composition loop

For the last row write w=3u. Its equivalent full conditions are

```
u=7 modulo24,   9u selected,
v=(4u-1)/3=9 modulo16.
```

Then the W9 rule has

```
d=v2(9v-1)=4,
z0=(9v-1)/16=(3u-1)/4,
3z0 noncanonical,       4z0+1=w.                     (6)
```

The last noncanonical assertion follows from the fact that
`6z0+1=(9u-1)/2` is canonical: a number r is canonical exactly when
2r+1 is selected. Therefore the W9 rule's exceptional W5 request is
**the original input w, with coefficient+1**. All its other requests,
and all requests from the absorption plans in (5), are smaller than w.
They cannot cancel the coefficient of the original request.

This is an infinite phenomenon. For every j>=0,

```
u=7+768j,        w=21+2304j
```

satisfies these conditions. Indeed
`9u+1=64(1+108j)`, so9u has exact selected exponent6.

The smallest instance is completely tautological after current cancellation:
the formal P21 plan asks only P21 and its explicit current is zero. At the
raw identity level the reason is visible for every member. Here
`3v→q` has word(1,2), while `v→u→2z0+1` is the other two-arrow prefix.
The E identity reverses the first prefix, and the W9 identity restores it.
Keeping the lower endpoint differences cancels the remaining second prefix.
Different subsequent lower-seed normalizations may leave known lower
identities, but they still provide no P(w) current without its self-request.

The implementation marks this outcome `self_dependency` and refuses to
compile it as a decreasing certificate. Merely counting fewer unresolved
pair types would hide this exact loop.

## 4. Exhaustive inverse obstruction after all elementary normalization

**Theorem.** Let D>=1 and let q>1 be canonical with

```
q=1 modulo3^D.
```

For every canonical p and every1<=d<=D,

```
T^d(p)=q    implies    p>q.                           (7)
```

This quantifies over **all** inverse branches, all unbounded ray indices,
and all choices at subsequent levels. No greedy choice or height cap occurs.
It already allows the complete elementary normalization at every T step.

### The full inverse affine table

Every canonical T predecessor is `a y+b`, with these base rows:

| y modulo3 | kind | a | b |
|---|---|---|---|
|0|ray0|8/3|1|
|0|ray1|16/3|1|
|1|ray0|4/3|-1/3|
|1|ray1|32/3|19/3|
|2|point|2/3|-1/3|
|2|ray0|64/3|19/3|
|2|ray1|128/3|83/3|

Every ray includes all its iterates under `p→64p+49`. The point has no
ray extension. Completeness is R25's inverse theorem. Every base row has
`a-b>=1`, with equality only at the point. If a ray has been iterated j
times, its difference becomes

```
a_j-b_j=64^j(a-b-7/9)+7/9 >1.                       (8)
```

All slopes are positive powers of2 divided by3.

### Shadow every inverse word at the absorber

Take any inverse word of length d<=D starting from q. Apply the same
choices to a shadow starting from1. After i steps write its positive
canonical shadow c_i and its accumulated slope lambda_i. Inductively

```
p_i=lambda_i(q-1)+c_i,
lambda_i=2^A_i/3^i.                                (9)
```

Before step i<=D the actual and shadow states have the same residue
modulo3: their difference is divisible by `3^(D-i+1)`. Thus each
chosen branch is legal at both states. R25 ensures that every shadow is
a positive canonical integer; this includes every possible ray index.
The equality in (9) follows by affine composition. This proves the
shadow construction for the **whole** inverse tree, not just a finite
collection of words.

Initially c_0=1 and lambda_0=1. Set
`G_i=lambda_i-(c_i+1)/2`. A step with coefficients a,b gives exactly

```
G_i=a G_(i-1)+(a-b-1)/2.                             (10)
```

At the first step the shadow is1 modulo3, so it must use one of the two
rays and has a-b>1. Hence G_1>0. Formula (8), positivity of a and
(10) preserve strict positivity at every later step. Therefore

```
lambda_i>(c_i+1)/2>=1.
```

Using q>1 in (9) now gives `p_i>q`, proving (7).

There is a useful sharper description. If the final shadow is1, every
preceding shadow was1 because T(1)=1. The word therefore followed only
the first base row at residue1, and

```
p_i=(4/3)^i(q-1)+1.
```

Otherwise c_i>=7, the smallest canonical integer above1, so (9)-(10)
give `p_i>4q+3`. Consequently the exact smallest predecessor over **all
positive lengths at most D** is `(4q-1)/3`, attained in one step. The
rest of the possible low part is only the displayed expanding spine.

The theorem also excludes every ordinary predecessor p<=q in at most D
S steps, including noncanonical p: semiconjugacy would give
`T^d(nu(p))=q`, contrary to (7), since nu(p)<=p.

## 5. Infinite obstructions inside the fixed W5 binary class

For every D>=1 impose the compatible CRT conditions

```
q=7 modulo32,
q=1+2*3^D modulo3^(D+1).                             (11)
```

They specify a nonempty infinite positive class modulo `32*3^(D+1)`.
Every member is complementary canonical with exact binary exponent3,
and `v3(q-1)=D`. Its critical pair input is

```
w=(2q+1)/3=5 modulo64,       nu(3w)=q.
```

Thus (7) applies at every prescribed depth to infinitely many actual
critical W5 inputs even with one fixed binary phase. For D>=2 these
have w=1 modulo3 and lie outside E, so this does not conflict with the
decreasing phase of Sections1-2.

It follows that no uniformly bounded number of inverse quotient steps,
even with complete elementary normalization and all inverse rays, can
produce a smaller ancestor for every remaining critical root. In particular
no finite catalogue whose only progress certificate is such a bounded
ancestor descent covers this family.

This is a scoped obstruction. It does not preclude an arbitrarily long
inverse construction depending on the input, additional forward steps,
unequal-time pair mergers, supplied-history reuse, or general signed
currents. The q changes with D. No positive seed is claimed to remain
unresolved forever, and no universal depth bound is assumed elsewhere.

## 6. Code, evidence, and remaining obligation

Run from the repository root:

```
python3 experiments/residual_progress/critical_inverse/check_critical_inverse.py
```

The source implements the whole phase current, exact W5-only formal plans,
the three-way classification, a compiler that rejects self-dependency,
all inverse affine branches, arbitrary supplied inverse-word lifting, and
the complete CRT family. The receipt records bounded identity tests,
independent forward checks of all small possible origins, actual supplied
pair-current examples, and exact tables for two examples. Fixed bounds and
caps are recorded; finite checks do not substitute for the universal proofs.

The default verification checks1,820 phase currents,1,024 W5-only absorption
plans,683 eligible pair plans (455 decreasing and228 self-dependent),24
actual supplied-current examples,73 inverse affine cases including ray
index1024,2,478 finite inverse words,27 CRT witnesses through depth128,
and six independent all-origin forward checks through depth6. The source
tables for P69 and P117 are retained in the receipt. All counts are finite
evidence; (7) includes every ray index by its written proof.

The remaining target still includes W5 inputs outside E and the returning
row inside E. Sections2-3 explain exactly when composing individually
decreasing rules succeeds and when eliminating the other pair type returns
the original obligation. Sections4-5 prevent closing the whole gap by a
fixed amount of inverse preprocessing. A complete constructor needs a new
rule or a proved unbounded recursion on those remaining states.
