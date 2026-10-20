# Two inverse choices escape part of the untouched selected phase

**Status: written complete arithmetic interface and conditional construction.**
This classifies both prescribed inverse choices, including their failed signed
plans. It removes two whole selected domains from the missing-current premise.
It does not exhaust all inverse rays, prove universal supply, or assert novelty.

Use positive odd Syracuse S, absorbed at1, killed atoms[1]=0, and
P(w)=[3w]-[w]. The canonical minimum nu and quotient T=nu S are R25's.
Write N_x for the explicit ordinary current[x]-[nu(x)] and H_s for the
unchanged R43 formal absorption plan. H_s retains its signed W5 requests;
it is not an absorption certificate without supplied inputs. Its request
ranks obey rho(u)<= (9s+5)/8, with rho(w)=nu(3w).

Dependencies: [R25](../bridge_normal_form/BRIDGE_NORMAL_FORM.md),
[R40](../w9_closure/CRITICAL_NINE_ELIMINATION.md),
[R43](../critical_rank/CRITICAL_IMAGE_RANK.md),
[R46](../inverse_escape/INVERSE_ESCAPE.md), and
[R54](../rule_avoidance/RULE_AVOIDANCE.md).

## 1. The complete starting domain and the two choices

Let w be positive, w=5 mod8, w=16 mod27, with3w selected. Equivalently,
w=205 mod216 and3w selected. Put

    q=(3w-1)/2,   v=(16w-13)/27,   p=3v.

Then q is canonical complementary, and

    q=-17 mod81,   v=-7 mod128,   v>=121,
    q=(81v+23)/32,   p=(32q-23)/27.

The R46 maximal first inverse word is exactly1,2,2, from p to q.
Indeed D=v3(q-1)=2, its unit is u=(q-1)/9, and
v3(16u+2)=1. Thus p is canonical11 mod16 and v belongs to W9.
This first inverse increases: p>q. Its R26 forward block returns to q,
so replaying that forward block alone yields no descent.

At p, R25's two base inverse rays are b=8v+1 and b=16v+1. For each
choice k in{4,8}, define its maximal point continuation:

    b=2kv+1,   h=v3(kv+1)>=0,   C=(kv+1)/3^h,
    r=2^(h+1)C-1.                                      (1)

The first h ordinary arrows from r have valuation1 and end at b.
Thereafter the actual ordinary valuation words to q are:

| k | Complete r-to-q valuation word | Ordinary length |
|---|---|---|
|4|1^h,2,1,1,4|h+4|
|8|1^h,2,3,2,2|h+4|

For k4, the four states after b begin
6v+1,9v+2,(27v+7)/2,q. For k8 they begin
12v+1,(9v+1)/2,(27v+5)/8,q. The congruence v=-7 mod128
gives every displayed valuation exactly, including the last extra binary
bit. For example 81v+23 is32 mod64, giving the final odd q. These are
actual ordinary paths; no quotient arrow has been silently counted as an
ordinary arrow. All h point predecessors are canonical by the complete
inverse table. There is also a quotient path of length h+4: h point steps,
then b-to-p and the three p-to-q steps.

Consequently the negative of this finite path is an explicit integer
current I with div I=[q]-[r]. It is valid even when r>=q.

## 2. Exact endpoint classification, with all small rows retained

Direct substitution gives

    32*3^h*(r-q)
      =(k*2^(h+6)-3^(h+4))*v +2^(h+6)-55*3^h.       (2)

Thus, on the entire domain in Section1,

    r<q iff h>=3 for k4;  r<q iff h>=5 for k8.         (3)

For the accepted rows both terms in(2) are negative. Below threshold,
the exact right sides are:

| k,h | Right side of(2) |
|---|---|
|4,0|175v+9|
|4,1|269v-37|
|4,2|295v-239|
|8,0|431v+9|
|8,1|781v-37|
|8,2|1319v-239|
|8,3|1909v-973|
|8,4|1631v-3431|

They are strictly positive for v>=121. There are no small-integer
exceptions or equality cases. For h>0, r is complementary canonical and
v2(r+1)=h+1. Maximality makes r=0 or1 mod3, never2 mod3.
For h>=2 its critical input is therefore in W5. At h1 the same holds
when r=1 mod3; the r=0 row instead has a W9 input and is treated below.

The accepted domain has the simpler exact description

    w=5 mod8, selected3w, and
    [w=718 mod729 or w=4255 mod6561].                 (4)

Indeed kv+1 equals(64w-25)/27 or(128w-77)/27. The two congruences
express exactly h>=3 and h>=5, respectively. They are disjoint, and both
imply w=16 mod27. This is a whole ternary-domain statement, retaining the
full binary selection hypothesis.

## 3. Exact signed plans, successful and failed

Let z=nu(w)<w/4. The formal current

    J=N_(3w)+I-N_w+H_r-H_z                           (5)

satisfies div J=P(w)-sum_u c(u)P(u), with every signed coefficient retained.
Here c=A_r-A_z, where A_s is H_s's request vector.

If(3) holds, the first critical request at r is a W5 input a with
rho(a)=r<q. All further H_a ranks are at most
(9a+5)/8<=(3r+4)/4<r. All lower H_z ranks are below q. Hence(5)
strictly decreases the original rho on every request. Supplied exact
currents for these requests turn(5) into an exact finite P(w) current.

If h>=2 fails(3), or h1 has r=1 mod3, the same critical request a is
present with coefficient+1 and rank r>q. All other requests have smaller
rank than r, so cancellation cannot remove it. This specific plan fails
strict descent; this is not nonexistence of some other comparison.

### The other failed rows return the original request

For h0, and for h1 with r=0 mod3, the complete W9 elimination retains
the original w with coefficient+1, with all other ranks below q. This
assertion includes every signed auxiliary request, not just a displayed
forward chain.

To prove it, set ell=(q+2)/3. Since v=-7 mod128, the W9 plan for v has
exact d=v2(9v-1)=6. Its two endpoints are q and ell. Therefore the full
request vectors satisfy

    A_p=A_q-A_ell+A_v,   A_q={w:1}+A_w.              (6)

These are exact equalities of vectors after full W9 substitution, by
linearity of the unchanged formal compiler. At h0, H_b first takes its
ordinary arrow and normalizes either2p+1 or F(p) to p, so A_r=A_p.

At h1,r=0 mod3, let c=r/3=(4kv+1)/9 in W9. Its d is4 for k4 and5
for k8; its R40 comparison is P(c) reduced to the formal difference
between p and v. Hence

    A_r=A_p-A_v+A_c=A_q-A_ell+A_c.                  (7)

All requests besides w are strictly below q. Specifically H_w and H_ell
are bounded by(3q+4)/4 and(3q+11)/8, and H_v by(9v+5)/8<q.
For k4, H_c has bound(16v+6)/8<q. For k8, c=1 mod8 and its ordinary
successor is C=(8v+1)/3=3 mod16, a selected state. Its canonical minimum
is(4v-1)/3, so H_c has bound(12v+2)/8<q. H_z is lower as well.
Equations(6)–(7) thus preserve the coefficient+1 at w exactly.

Consequently(3) is also the complete strict-rho classification of the
two prescribed formal plans(5), including h0 and both h1 residue rows.
It is not a classification of all inverse rays or all possible currents.
In particular selected w=16 mod81 gives v=0 mod3, so both choices have
h0 and retain the original request. This entire subdomain remains
unresolved by this rule, rather than being hidden behind a resource cap.

By R43's decreasing-rank induction, universal currents on the complement
of(4), together with any other supplied strict-rho rules, would supply all
W5 currents. The new rule removes(4) from the missing premise but does not
establish universal supply on that complement.

## 4. Complete cylinders and escape after arbitrarily long forward growth

For every k in{4,8}, h>=1 and e in{1,2}, impose

    v=-7 mod2048,
    v=k^(-1)*(3^h e-1) mod3^(h+1).                 (8)

CRT supplies an infinite full progression of positive v, with exact h
and C=e mod3. Every such member has w=3445 mod3456, inside the R54
untouched phase. The finite checker retains both terminal units, including
every failed row. Formula(8) is not the entirety of the broader domain(4).

For the stronger intersection with R54, fix any L>=1. Put K=11L+6 and

    q_0=81*2^K*s-17,   v=32*2^K*s-7.

For any accepted h, choose every positive s in the congruence

    k*2^(K+5)*s=7k-1+3^h e mod3^(h+1).             (9)

The coefficient is invertible modulo3^(h+1), so this is a nonempty full
infinite progression. R54 gives7L quotient steps of growing forward
prefix, each noninitial state above q_0, with its full leading-dependency
obstruction. Nevertheless(1)–(5) construct a strict original-rho inverse
comparison for that same seed. In particular fixed h3,k4 uses seven
ordinary arrows, or fixed h5,k8 uses nine, for every prescribed L.

This does not contradict R54: its obstruction concerns a named forward
prefix/H/rule procedure, whereas the new inverse branch supplies a new
leading rule. The seed changes with L. Neither statement constructs one
infinite positive growing orbit or covers the whole original phase.

## 5. Implementation and evidence

[selected_inverse.py](selected_inverse.py) exposes both successful and failed
plans, their exact valuation words and every signed request. `one_step`
accepts exactly(4). `compile_plan` checks strict rho and substitutes only
explicitly supplied exact currents; it rejects missing, incorrect or
nondecreasing premises. It performs no unknown orbit search.

Run `python3 experiments/residual_progress/selected_inverse/check_selected_inverse.py`.
The checker independently verifies words, quotient clocks, affine endpoint
arithmetic, complete failed-vector classifications and CRT constructions.
Its receipt covers300 eligible inputs among16384 W5 candidates below131072,
600 two-choice plans,102 independent affine comparisons,192 exact phase
examples through h128, and36 intersections with growing prefixes through
L128. Twelve plans in that finite input interval are strict; these are not
an asymptotic coverage estimate. Both accepted classes are populated by
the separate CRT checks. Eight designated invalid requests are rejected,
as are all failed plans when submitted for compilation.

Four actual substitutions produce P5821,P93301,P148597 and P382205941
currents with40,73,122 and203 rows. The two middle examples' local plans,
all supplied inputs and complete output tables are stored in
[selected_inverse_audit.json](selected_inverse_audit.json). Every demonstration
input search is capped at10000 ordinary steps and512 bits, with cycle
detection; a cap would leave the demonstration unresolved. These finite
supplied currents are distinct from the symbolic construction and its
explicit missing premises.

Finite checks audit the code; the infinite quantifiers follow from the
arguments above. Universal completion on the remaining complement is open.
