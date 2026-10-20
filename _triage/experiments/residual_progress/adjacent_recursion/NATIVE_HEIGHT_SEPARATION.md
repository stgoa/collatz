# Adjacent currents: a native-height inverse barrier and forward separation

**Status: written scoped separation theorem and finite exact certificates.**
This does not close the whole adjacent-source domain or add a dispatcher
rule. It identifies a complete family on which arbitrary bounded inverse
depth fails at the required height, even though a smaller ancestor exists,
while a fixed ordinary forward word gives a conditional current below that
height. The seed varies with the depth. No infinite divergent orbit, global
search limitation, novel-result claim, or universal current supply follows.

Use absorbed odd Syracuse `S`, the elementary minimum `nu`, quotient
`T=nu S`, killed atoms `[1]=0`, and the complete canonical inverse branches
of R25/R41. For canonical `q=31 mod108`, let

    D(q)=[q+2]-[q],           n(q)=(8q-5)/9.

Here n is the native height from
[R65](../defect_normal_form/ADJACENT_DEFECT_INTERFACE.md). Missing pair
currents must have their original critical-image rank strictly below n,
not merely below q. The all-ray affine argument extends the scoped
[R49 inverse barrier](../inverse_scope/INVERSE_SCOPE.md).

## 1. Why two tempting adjacent rewrites give no new recursion

The ordinary word `(1,2)` takes n to q. Pulling the negative source q
back along this word leaves `[q+2]-[n]`. Since q+2 has an ordinary
successor at most `(3q+7)/4<n`, its positive source already belongs to
the supplied absorbing component under the intended lower-input
induction. The remaining absorption at n has not been supplied.

More precisely, let u=(2q+1)/3 and a=nu(u). R65's pair-to-adjacent
conversion has local current

    K=N_(3u)-N_u+J_(q+2)-J_a.

If G is the full returning prefix from q to r, the R44 plan has current

    L=N_(3u)+G-N_u+J_r-J_a.

Their exact subtraction is

    K-L=J_(q+2)-G-J_r,
    requests=A_(q+2)-A_r.                             (1)

Thus transporting that returning rule through the adjacent equivalence
is exactly the direct forward comparison, including every signed row.
It does not acquire a new endpoint or a better rank by changing notation.

The complete initial paired binary run has the same unresolved upper
endpoint. Write

    q=2^a t-1, a>=2, t odd,
    t=-3^a mod4,       2^a t=5 mod27.

The q-side has word `1^(a-1),2`, length a, ending at
`r=(3^a t-1)/2`. If a=2m, the positive source q+2 has m-1 valuation2
arrows to `F(z)`, z=3^(m-1)t, and the elementary sibling current changes
F(z) to z. Its residual is `[z]-[r]`. If a=2m+1, it has m valuation2
arrows to `2z+1`, z=3^m t, with residual `[2z+1]-[r]`.
The even branch's positive common-tail clocks are `(m,1)` from
`(q+2,z)`; the odd branch has an actual m-arrow prefix. The negative
prefix always has a ordinary arrows. These are not a single ordinary
clock for the signed source. Absorbing the known positive endpoint
alone leaves exactly the R44 endpoint r. No recursive closure is proved.

## 2. A six-state certificate at the native anchor

The canonical origins below27 and their entire T-forward closure are

    Q={1,7,9,11,17,25},
    T: 1->1, 7->11, 9->7, 11->17, 17->1, 25->9.      (2)

Every listed edge is direct arithmetic. Forward closure and omission of31
prove that no canonical origin below27 reaches31 at any depth. The only
canonical integer in `[27,31)` is27, and `T^2(27)=31` through41.
Consequently31 has exactly one canonical ancestor below31, namely27.

The fixed ordinary prefix from31 to23 has length35, total valuation56,
and exact valuation word

    W=(1,1,1,1,2,2,1,2,1,1,2,1,1,1,2,3,1,1,
       2,1,2,1,1,1,1,1,3,1,1,1,4,2,2,4,3).         (3)

Since nu(23)=11 belongs to Q, this also verifies absorption of31.
In particular27 reaches31 only at its second quotient step: a later
occurrence would force a return cycle through31. These finite data are
stored and verified without an uncapped trajectory search.

## 3. The complete all-ray native-height obstruction

**Theorem.** Fix D>=3 and t>=1, and set

    q=31+2^57*3^D*t,
    n=27+2^60*3^(D-2)*t=(8q-5)/9.                    (4)

Both states are canonical and q is in the entire R65 adjacent domain.
For every canonical predecessor p with `T^d(p)=q`, 1<=d<=D, exactly
one of the following occurs:

* d=2 and p=n, from the base ray0 followed by the point inverse;
* p>q.

The statement includes every inverse ray index. In particular no ordinary
odd source below n reaches q in at most D ordinary arrows.

**Proof.** Shadow any complete inverse word at31. Congruence modulo3^D
keeps each branch legal at the actual and shadow states throughout d<=D.
Write the affine result as

    p_i=lambda_i*(q-31)+c_i,    lambda_i=2^(A_i)/3^i.

Every c_i is a positive canonical ancestor of31. By (2), either c_i=27
or c_i>=31. The complete inverse affine branches `y->alpha*y+beta`
satisfy `alpha-beta>=1`, strictly on every ray, including all ray indices.
The first inverse at31 is a ray, since31=1 mod3. Therefore the exact gap

    G_i=lambda_i-(c_i+1)/32,
    G_i=alpha_i*G_(i-1)+(alpha_i-beta_i-1)/32

is strictly positive for i>=1. If c_i>=31, this gives lambda_i>1 and
p_i>q. If c_i=27, the finite anchor path proves that this word has length2
and is precisely ray0 at index0 followed by point. Its slope is8/9,
so p_i=8(q-31)/9+27=n. This exhausts every branch, without a ray-index
cutoff. For an ordinary predecessor x<n, semiconjugacy gives the canonical
predecessor nu(x)<=x<n, contradicting this classification. ∎

The presence of the explicit smaller ancestor n is the point of this
variant: a test which asks only for descent below q reports progress,
although the actual adjacent obligation requires strict descent below n.
The theorem concerns the prescribed depth and varies q with D. It does
not assert that every lifted q permanently misses smaller supplied history.

## 4. The same family has a fixed forward conditional certificate

Every q in (4) preserves word W because the exact cylinder modulus is
`2^(56+1)`. Its endpoint is

    y=23+2*3^(D+35)*t.

The complete original-rho formal absorption bound gives all H_y requests
below n, since

    8n-(9y+5)
      =4+2*3^(D-2)*t*(2^62-3^39)>0.                 (5)

The strict integer inequality `2^62>3^39` is checked exactly. For the
positive source, q+2 has one valuation2 arrow to
`s=(3q+7)/4<n`. Here s=1 mod3, so R58 gives every H_s request at most s:
its sole possible above-minimum exception is divisible by3.

Let G_q be the ordinary 35-arrow current along W and let E be the
one-row current at q+2. Then

    J=E+J_s-G_q-J_y,
    c=A_s-A_y,
    div J=D(q)-sum_v c(v)P(v),     rho(v)<n.          (6)

Every signed coefficient and both sources are retained. Exact supplied
currents for the remaining pairs yield an exact D(q) current; missing or
incorrect supply is rejected. The same formula is valid at the anchor
q31, with n27. The inverse obstruction and the fixed forward certificate
therefore hold on the same full parameter family. This is a structural
separation, not a new universal rule or a claim that these examples were
outside every previous accepted domain.

## 5. Reproduction and limits

`native_height.py` implements the finite anchor verification, arbitrary
all-ray shadow-word audit, the family (4), complete paired binary prefixes,
and the conditional current (6). `check_native_height.py` records bounded
word and family checks and finite supplied-current demonstrations. The
infinite inverse quantifiers follow from the proof, not from sampling ray
indices. Fixture discovery has explicit step/bit caps and cycle detection.

Run `python3 experiments/residual_progress/adjacent_recursion/check_native_height.py`.
The receipt checks 2496 complete sampled inverse words through depth 5 with
ray indices 0/1, three eight-branch words at ray indices 8/32/128, 120 full
paired binary runs, 120 exact transported-current identities, and 48 family
instances through D128. These samples do not replace the unbounded-ray
proof. Two complete current demonstrations are stored: q31 has 45 rows
and no supplied pair, while q3891110078048108575 has 345 rows after 15
distinct pair currents are supplied. All fifteen input tables are retained.
Nine negative checks reject invalid domains, insufficient precision,
an illegal inverse, an incorrect native height, missing or malformed
supply, and a zero fixture cap. The fixture limits are 10000 steps and 512
bits. Default execution compares the complete receipt and local source
hashes; `--write-receipt` regenerates it after inspection.

Universal closure of D(q) is still open. Retained lower history and new
forward comparisons remain available; another inverse search or a renamed
returning pair does not by itself establish the required native descent.
