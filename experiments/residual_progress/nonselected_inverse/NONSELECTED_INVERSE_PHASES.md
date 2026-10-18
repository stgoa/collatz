# Complete base inverse phases on the nonselected critical-five domain

**Status: written identities, an exact complete phase classification, and a
conditional decreasing constructor.** Two complete ternary phases can
be removed from the sufficient W5 input set, within its nonselected branch.
The rank is the canonical image rho(w)=nu(3w); the pair index may increase.
The remaining inputs are explicit missing premises. This does not prove
Collatz or exclude other inverse branches when this particular rule fails.

Use positive odd integers, odd-only Syracuse S with1 absorbing, killed atoms
[1]=0, F(x)=4x+1, P(w)=[3w]-[w], and div=I-S_*. The elementary minimum nu,
canonical set, and selected-halving identities are [R25](../bridge_normal_form/BRIDGE_NORMAL_FORM.md).
The complete W9 elimination is [R40](../w9_closure/CRITICAL_NINE_ELIMINATION.md).
The absorption plan H_s with only W5 inputs strictly below s is
[R41](../critical_inverse/CRITICAL_INVERSE.md). These are formal plans until
their exact signed input currents are supplied.

## 1. Domain and the two base inverse branches

Consider the whole domain

    B={w>0: w=5 mod8 and3w is not selected}.

Then q=3w is complementary canonical, with q=7 mod8. For k in{4,8}, put

    b=2kw+1,  h=v3(kw+1),  C=(kw+1)/3^h,
    p=2^(h+1)C-1.                                      (1)

Both b are canonical1-modulo8 predecessors of q for T=nu S:

    k4: S(b)=6w+1=2q+1,  nu(2q+1)=q;
    k8: S(b)=12w+1=F(q), nu(F(q))=q.                    (2)

These are the two **base** branches in the complete R25 inverse table.
Higher ray indices and mixed inverse words are not analyzed here.

If h=0, then p=b and there is no valuation1 continuation. If h>=1,

    S^h(p)=b, with exact word1^h; hence T^(h+1)(p)=q.    (3)

The last equality counts quotient steps. It does not assert an ordinary
p-to-q orbit segment: the last step uses an elementary coalescence bridge.
Indeed all h ordinary arrows in (3) are canonical valuation1 arrows.
Since C=3^h mod4, p is complementary canonical with binary exponent h+1.
Also p=0 or1 modulo3, so its exact critical pair index is

    v=p/3 if p=0 mod3,  v=(2p+1)/3 if p=1 mod3.         (4)

It lies in W9={9 mod16} exactly when h=1 and p=0 mod3; in every other
h>=1 case it lies in W5={5 mod8}.

Only one base branch can have h>0: k4 when w=2 mod3, k8 when w=1 mod3.
When3 divides w neither has a valuation1 continuation. Thus switching to
the other base branch cannot fix an unsuccessful positive-h case.

For ordinary clocks, the k8 bridge coalesces after h+2 arrows from p and
one from q. For k4 let a=v2(q+1)>=3. The selected-halving bridge for2q+1
gives coalescence after h+a+2 arrows from p and a+1 from q. These statements
retain the two clocks; neither is silently replaced by the quotient clock.

## 2. Exact rank decrease, including increasing pair indices

Define the positive integer rank rho(w)=nu(3w), as in the R37 critical
bijection. On B, rho(w)=3w=q; on its critical child, rho(v)=p.
The exact thresholds are k4:h>=3 and k8:h>=5, independently of p modulo3.
Indeed p<3w is equivalent to (5) below. The same sign calculation proves
there are no small exceptions; below these thresholds p>3w.
The child is W5 throughout both rank-decreasing domains.

This includes increasing pair indices: at w1613,k4,h3 the child is v2549,
but rho(v)=3823<4839=rho(w). At w17101,k8,h5 the child is v24021 with
rank36031<51303.

For comparison, the complete pair-index decrease table is narrower:

The following table is exhaustive for h>=1.

| Base k | p modulo3 | Exact condition for v<w | Child when this condition holds |
| --- | --- | --- | --- |
|4|0|h>=3|W5|
|4|1|h>=5|W5|
|8|0|h>=5|W5|
|8|1|h>=6|W5|

**Proof.** Write w=(3^h C-1)/k. In the p=0 row the inequality v<w is
equivalent to

    (3^(h+1)-k*2^(h+1))*C > 3-k;                     (5)

in the p=1 row it is equivalent to

    (3^(h+1)-k*2^(h+2))*C > 3-k.                     (6)

At or above the displayed threshold the parenthesized coefficient is
positive. Below it the coefficient is negative, already at most-5 in the
k4 rows and at most-13 in the k8 rows. Since C>=1 and3-k is-1 or-5,
the inequality fails. In particular there is no exceptional small C, and
v=w never occurs. The W9 condition in §1 occurs below all four thresholds.

These comparisons concern the critical **pair index** v. It is not necessary
that p<w. For example the k4,p0,h3 case has p approximately64w/27>w but
v approximately64w/81<w. Replacing v's bound with a bound on p would discard
a legitimate decreasing branch.

## 3. Exact conditional current and all input-rank bounds

Let N_y be the elementary current with div N_y=[y]-[nu(y)]. Let A be the
negative p-to-b prefix current followed by the negative bridge in (2), so
div A=[q]-[p]. Set z=nu(w)<w. Then

    L=A-N_(3v)-N_w,
    div L=P(w)-P(v)-[v]+[z].                          (7)

Substitute the R40 plan for P(v), add the R41 absorption plan H_v, and
subtract H_z. This gives an exact finite current and a signed W5 dependency
vector. In every rank-decreasing row, v is W5 and rho(v)=p<q. The auxiliary
absorption plans must be checked in the same rank.

Every W5 input u in H_s satisfies rho(u)<=(9s+5)/8. Here is the proof needed
by this constructor. Every original R37 request has critical image at most
s. A W5 request stays unchanged. A W9 request b has image3b; its R40
reduction leaves input ranks at most (27b+5)/8. All nonexceptional local
requests have rank below3b. The exceptional input4z+1 has rank6z+1, whose
three possible expanding-index values are (27b+5)/8, (81b+23)/32, and
(243b+101)/128; only the first exceeds3b. Every recursive W9 index is
smaller than b, so the same bound survives substitution.

Since v<=(2p+1)/3, every input from H_v consequently satisfies

    rho(u) <= (9v+5)/8 <= (3p+4)/4 < p,

where p>=7. Also z=nu(w)<w/4, so every H_z input has rank below q=3w.
Thus every missing input in (7) has rank below rho(w), with all signs and
multiplicities retained. The general interface and composition theorem are
in the [critical-image rank proof](../critical_rank/CRITICAL_IMAGE_RANK.md).

The entire rank-decreasing domain is exactly

    G={w in B: w=20 mod27 or w=91 mod243}.

These congruences mean v3(4w+1)>=3 and v3(8w+1)>=5 respectively, and include
the full unbounded-depth tails. They are disjoint modulo3.
Universal exact P currents on W5 minus G are equivalent to Collatz: strong
induction on rho(w) constructs omitted inputs with (7), then R40 and R37
apply. This reduces the missing premise; it does not supply the remaining
currents. Combining G with other rules requires checking the same rank.

### The narrower pair-index-decreasing subdomain

The pair-index-decreasing subdomain has a finite ternary description. Within B,
the k4 rows are equivalent to

    w mod243 in{47,101,128,182,209},

and the k8 rows to

    w mod729 in{91,577}.                              (8)

For k4 the alternatives are h3,p0, namely47 mod81; h4,p0, namely101 mod243;
or h>=5, namely182 mod243. For k8 they are h5,p0, namely577 mod729; or
h>=6, namely91 mod729. This proves (8), including the unbounded-depth tails.
Equivalently there are exactly17 classes modulo729:

    47,91,101,128,182,209,290,344,371,425,452,
    533,577,587,614,668,695.

This narrower subset is contained in G. The extra rank-decreasing cases
have increasing pair indices and cannot be justified by induction on w.
The R43 finite compiler composes the rules only after verifying their
common rho rank; no missing leaf is treated as an existing current.

## 4. Complete failure classification for the other positive-h cases

If h>=1 and the child v lies in W5 but the rank does not decrease, then
rho(v)=p>q. Its supplied-input coefficient is exactly+1 and cannot cancel:
the plan for P(v) is the single request P(v), while every H_v input has
rank below p and every H_z input has rank below q. Thus v has the unique
largest remaining rank. Smaller signed coefficients cannot remove it.

The only other case is h1,p0, where v lies in W9. For **both** base rays,
the complete specified plan reduces exactly to the original input:

    coefficients={w:1},  explicit current=0.           (10)

Here is the cancellation proof. Interpret H_s as the full formal absorption
object (current and signed input vector), and P(w) as a missing input with
zero explicit current. The equality H_(3w)=P(w)+H_w is exact because3w is
canonical critical. Also H_w=N_w+H_z.

For k4, put C=(4w+1)/3. Then p=3v=4C-1, C=7 mod32 is canonical,
v→C→2w+1, and p→b→6w+1. The R40 W9 rule has d4 and parameter z0=w.
Its upper absorption object is N_(6w+1)+P(w)+H_w. Its lower one is
H_(2w+1)=-e_C+H_C, while H_v=e_v+H_C. Substituting these into (7) cancels
both upper prefix rows, N_(6w+1), the two lower prefix rows, and
H_w-N_w-H_z. What remains is exactly (10).

For k8, put C=(8w+1)/3. Now C=35 mod64 is selected, p=3v=4C-1,
v→C→F(w), and p→b→F(3w). The R40 W9 rule has d5 and z0=w. Its sibling
correction is

    e_(F(3w))-e_(3w)-e_(F(w))+e_w.

The selected bridge of C and the ordinary step from nu(C) to w give

    H_C=e_C+e_(F(w))-e_w+H_w,  H_v=e_v+H_C.

The inverse bridge cancels the upper prefix and its sibling correction;
the displayed lower identity cancels the rest, leaving H_w-N_w-H_z=0
and the single request P(w). This again proves (10).

The classification is therefore complete for these two base branches and
their maximal valuation1 continuations: strict decrease on G, exact return
in the h1,p0 row, and an uncancelled larger W5 input in every other
positive-h row. Nothing here rules out a different ray, a longer mixed
inverse word, a forward excursion, or another signed current identity.

## 5. Implementation and verification

[inverse_phases.py](inverse_phases.py) returns exact parameters, bridge rows,
conditional pair plans, and the complete rank-decreasing phase test. It
never searches for absorption. The checker uses separately capped finite
absorption paths only to provide a few explicit substitution fixtures.
All rejected or nondecreasing inputs remain visible.

```sh
python3 experiments/residual_progress/nonselected_inverse/check_inverse_phases.py
```

The [receipt](nonselected_inverse_audit.json) records the exact ranges,
ordinary-clock checks, phase classes, tautological rows, conditional
substitutions and stored fixture hashes. The finite checks audit these
implementations; the written arguments establish the quantified phase and
induction statements. No universal certificate, novelty claim or formal
verification is supplied.
