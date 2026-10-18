# R47: complete two-block interface for nonselected multiples of three

**Status: written proof, exact conditional constructor, and bounded independent
integer checks.** This removes a new, infinite arithmetic subdomain of the
remaining W5 requests. It does not supply the remaining requests or prove
Collatz. The two base rays and the specified maximal blocks are exhausted;
higher inverse rays and other inverse words are outside this classification.

Dependencies are [R25 normal form](../bridge_normal_form/BRIDGE_NORMAL_FORM.md),
[R40 W9 elimination](../w9_closure/CRITICAL_NINE_ELIMINATION.md),
[R43 critical-image rank](../critical_rank/CRITICAL_IMAGE_RANK.md),
[R45 base rays](../nonselected_inverse/NONSELECTED_INVERSE_PHASES.md), and
[R46 inverse blocks](../inverse_escape/INVERSE_ESCAPE.md).
All actual currents use the odd-only Syracuse map S, with 1 absorbed.
Write [x] for the atom at x, e_x for its outgoing current row, N_x for the
elementary current with boundary [x]−[ν(x)], and P(w)=[3w]−[w].
A formal H_x has boundary [x] minus its explicitly retained W5 pair requests.
The formal H used below is exactly the deterministic R43 absorption plan,
including complete R40 substitution. It is not an assumed absorption current.

## 1. Entire domain and both inverse branches

Let w be any positive integer satisfying

    w = 5 modulo8, 3|w, and 3w is nonselected.

Then q=3w is complementary canonical and ρ(w)=q. Write

    D=v_3(w)>=1,  w=3^D u,  3∤u.

For each k in {4,8}, define

    b=2kw+1,
    s=2k·4^D u+1,
    j=v_3(k·4^D u+1),
    C=(k·4^D u+1)/3^j,
    p=2^(j+1) C−1.                                      (1)

The canonical quotient map T=ν∘S satisfies T(b)=q: when k4, S(b)=2q+1
is q's selected partner; when k8, S(b)=F(q). Further,

    S^(D+j)(p)=b, with exact valuation word 1^j 2^D.      (2)

All states in this segment are canonical. Indeed v_3(b−1)=D, so the D
inverse valuation2 arrows give s; its maximal inverse valuation1 run has
length v_3(s+1)=j. This is the complete R46 block, now started at b.
In particular v_2(p+1)=j+1. If j>0, p is complementary canonical and
p modulo3 is either 0 or1. Exactly one base branch has j>0:

| Unit u modulo3 | Active branch | Other branch |
|---|---|---|
| 2 | k4 | k8 has j0 |
| 1 | k8 | k4 has j0 |

This follows by reducing k4^D u+1 modulo3. There is no unit case omitted.
The quotient ancestry in (2) followed by b→q has length D+j+1.

The **ordinary two-clock equalities** are different. Put a=v_2(q+1).
For k8, p and q coalesce after D+j+2 and 1 arrows respectively. For k4,
they coalesce after D+j+a+2 and a+1 arrows respectively. These follow from
b→F(q) and b→2q+1 respectively, followed by the elementary sibling bridge.
No equality of these two clocks is asserted.

## 2. Exact rank test, with no small endpoint exceptions

The whole arithmetic descent criterion is

    p<q  iff  k·2^(2D+j+1) < 3^(D+j+1).                 (3)

To see this, write λ=k·2^(2D+j+1)/3^(D+j+1). Direct substitution gives

    p−q=(λ−1)q + 2^(j+1)/3^j −1.                       (4)

The inequality λ<1 forces j>=4: already the smallest case D1,k4,j3
has λ=256/243>1, and increasing D or k increases λ. For j>=4 the
last term in (4) is negative, proving sufficiency. If λ>1, (4)>−1;
as p−q is an even integer it is >=0. Equality λ=1 is impossible because
the numerator is a power of two times k, while the denominator is an odd
power of three. This proves the iff; no floating-point comparison is used.

For j>0, the critical inverse v of p is

    v=p/3 if p=0 modulo3;
    v=(2p+1)/3 if p=1 modulo3.                          (5)

It belongs to W9 precisely when j1 and p0mod3; otherwise it belongs to W5.
All cases satisfying (3) have j>=4, hence v∈W5 and ρ(v)=p<ρ(w).
The index v itself need not decrease.

## 3. Exact signed plan in the decreasing domain

Let B be the negative prefix current from p to b, followed by the negative
elementary quotient bridge from b to q. Thus

    div B=[q]−[p].                                     (6)

The implementation constructs B using only the explicit word (2) and the
normalizer of S(b). It does not follow an unknown orbit. Set z=ν(w)<w/4.
Since ν(3v)=p, the local current

    L=B−N_(3v)−N_w

has exact boundary

    div L=P(w)−P(v)−[v]+[z].                           (7)

Therefore the full formal plan is

    J_w=L+J_v+H_v−H_z,                                 (8)

where J_v is a missing W5 pair current, or its complete formal R40 W9
substitution. Every signed coefficient is retained. In the decreasing
domain, J_v is simply the requested input v. The R43 bound gives

    every rank in H_v <=(9v+5)/8 <=(3p+4)/4 <p,
    every rank in H_z <=(9z+5)/8 <q.

Thus every missing input in (8) has strictly smaller positive integer
rank than ρ(w). Supplied exact currents for these inputs give an exact
current for P(w), by linearity. R43's finite conditional closure can
compose this rule with any other strict-rank rules. Missing leaves remain
explicit: strict decrease establishes termination of this rewriting,
not universal availability of the leaves.

Example: w=16653, D1,k8,j5 gives p=46783 and v=31189. The pair index grows
from16653 to31189 while its rank falls from49959 to46783. Its complete
dependency vector is

    P(31189)+P(325)−P(93).

The local current and supplied finite input fixtures are persisted. They
certify this particular pair; their absorption discovery is capped and is
not used to justify (1)–(8).

## 4. Exhaustive failure classification for this interface

Here “failure” means that the **full formal plan (8)** has a nondecreasing
rank request after exact signed cancellation. It does not prohibit another
inverse word, another representation of H, or later coupled cancellation.

### 4.1. j0: literal self-return

Then p=s is canonical1mod8. Its deterministic absorption plan follows the
D valuation2 arrows to b, then the canonical quotient arrow b→q. At q it
requests P(w) and the formal H_w. Those prefixes cancel B; H_w's elementary
normalization cancels −N_w−H_z. Consequently the complete plan is exactly

    local current 0, missing coefficients {w:1}.        (9)

This includes the inactive branch of every input in the domain.

### 4.2. j>0 with v∈W5 and (3) false

The request v has coefficient+1 and rank p>=q. All H_v requests have rank
strictly below p; all H_z requests have rank below q. Therefore v is the
unique largest-rank request and cannot cancel. This includes every j>=2
failure and the j1,p1mod3 failures.

### 4.3. j1,p0mod3: exact W9 return and a forward defect

Here p=4C−1, C1mod3, and v=(4C−1)/3∈W9. Direct calculation gives

    d=v_2(9v−1)=2D+4 (k4), or 2D+5 (k8).               (10)

In the R40 two-run formula the parameter z is **the original w**.
The upper/lower endpoints are respectively

    (6w+1,2w+1) for k4;
    (F(3w),F(w)) for k8.                               (11)

Both upper endpoints normalize to q. The lower prefix starts v→C→S(C),
then takes D valuation2 arrows to the second endpoint in (11). Moreover

    C=11 modulo16,  C=1 modulo3,
    S(C)=k·2^(2D−1)u+1.                                (12)

Substituting these prefixes in (8), cancelling each shared row, and using
the deterministic H identity along the canonical1mod8 lower spine gives
the exact formal expression

    P(w) + ( H_C − e_C − H_(S(C)) ).                    (13)

This equation describes a current together with its formal pair requests:
the local current is current(H_C)−e_C−current(H_(S(C))); its request vector
is {w:1}+requests(H_C)−requests(H_(S(C))). The parenthesized expression has
zero boundary after these requests are supplied. It is not a new positive
source measure. Using a forward absorption representation for H_C would
make it a literal tautology; the canonical representation retains a defect.

This remaining defect still cannot yield rank descent here. The plan H_C
has a unique leading input

    r=(2C+1)/3 ∈W5,  ρ(r)=C,

and all its other ranks are <C. The plan H_(S(C)) follows the explicit
canonical1mod8 spine to the lower endpoint in (11), so all its ranks are
<q: for k4 use the R43 bound (9(2w+1)+5)/8<3w (w>=5), and for k8 normalize
F(w) to z<w/4. Finally,

    C<q exactly when k4 and D∈{1,2};
    C>q for k4,D>=3 and for all k8,D>=1.                (14)

Indeed C/q=(k/9)(4/3)^D+1/(3q). For the only two small cases, q−C=11u/3−1/3
and 17u/3−1/3 respectively; the other cases have positive leading difference.
Thus when C<q the unique largest request is the original w with coefficient1;
when C>q it is r with coefficient1. Equality is impossible. This proves
nondecrease after the complete formal W9 substitution, without a scan.

Combining 4.1–4.3: for either base branch, the full plan is strictly
rank-decreasing **if and only if** the integer slope test (3) holds.

## 5. Infinite new cylinders for every ternary depth

Fix any D>=1, k4 or8, j>=1, and c in{1,2}. The simultaneous congruences

    k4^D u+1 = c3^j modulo3^(j+1),
    3^D u =13 modulo32                                (15)

define one complete positive CRT progression for u modulo32·3^(j+1).
The first congruence makes u a unit and gives exact j and C=cmod3; the
second gives w=13mod32, so q=7mod32 is complementary canonical. Hence all
these inputs lie in the required domain with exact D. Their w period is
32·3^(D+j+1). This is a symbolic cylinder statement, not interpolation of
finite examples. Each terminal choice in (15) is allowed independently.

For every D and k, all sufficiently large j satisfy (3). The explicit
choice j=2D+6 suffices, since

    λ=(2k/3)(16/27)^D(2/3)^6 <1.

Thus there are new infinite strict-rank families at **every** ternary depth,
with unbounded exact inverse length. Earlier direct rules R41/R44/R46 need
selected3w; R45's decreasing phases have 3∤w. Every accepted input here is
outside those direct domains. This does not claim it was absent from every
previous finite supplied history or recursive closure.

## 6. Reproduction and limits

Run `python3 experiments/residual_progress/nonselected_multiples/check_multiple_escape.py`.
The checker replays the stored receipt, tests both branches in a bounded
range, verifies exact clocks and signed boundaries, synthetic CRT classes,
every failure type, index growth with rank decrease, rejection
of missing inputs, and supplied finite substitutions. The stored input
currents are sufficient to replay the featured w16653 certificate without
assuming their existence. Regenerate with `--write-receipt`.

The saved receipt checks 4096 W5 candidates below32768, of which682 satisfy
the whole domain; it constructs both branches, for1364 complete formal
plans. It includes240 exact CRT cases with D1..12, both branches, both
terminal units, and boundary j values, plus24 further progression terms.
There are four actual supplied substitutions. The first receipt generation
passed in3.1 seconds; runtimes are not mathematical bounds. These exploratory
limits are explicit, and the fixture absorption cap is10000 arrows.

The proof is (1)–(15), not the finite counts. This result supplies neither a
closed constructor for all W5 nor a proof that the remaining requests are
absorbed. It does provide a complete arithmetic test for both prescribed
two-block branches, with explicit failure interfaces and honest signed
dependencies.
