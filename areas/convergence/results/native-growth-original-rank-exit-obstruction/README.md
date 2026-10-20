# Guarded native-W9 growth, exact exits, and inverse undos

**Status: written scoped theorem and finite exact-current audit.** This gives
no new accepted pair domain. It separates local contraction from decrease
below an original rank, and proves two precise inverse undos. A finite end of
the specified growing guard does not itself supply the final pair current.

Use the [retained critical basis](../critical_basis/CRITICAL_BASIS.md), with
`P(b)=[3b]−[b]`, `rho(b)=nu(3b)`, and the deterministic formal absorption plans

    [x] = div H_x + sum A_x(v) P(v).

Both W5 and W9 inputs are retained. Every request of H_x has rank at most
nu(x). Currents here are integer signed tables. Missing pair inputs remain
premises. The native a5 interface is recorded separately in
[Native W9 continuation](../native_nine/NATIVE_NINE_CONTINUATION.md).

## 1. Complete guarded return and its exact current

Put

    G = {b>0 : b=905 mod8192},
    U(b) = (729b+223)/512,       Y(b)=217b+223.                 (1)

For every b in G, the canonical root 3b has six ordinary arrows with exact
valuations `(1,2,1,1,1,2)` to `6U(b)+1`. This endpoint is23 modulo32 and its
selected-halving normal form is `3U(b)`. Thus

    D_b = [six forward arrows] + N_(6U(b)+1),
    div D_b = [3b]−[3U(b)].                                  (2)

Here N is the explicit elementary normalizer current. The upper and lower
ordinary clocks in (2) are `(9,3)`; its quotient clock is6. The six intermediate
quotient states are precisely the ordinary states until the final selected
normalization. We have U(b)>b and U(b)=9 modulo16.

The relation Y(U(b))=729Y(b)/512 proves that U(b) is again in G exactly when
`v2(Y(b))>=22`. Its exact order drops by9 on every such return. At a source
of order13 through21, (2) is still available, but its endpoint has left G.

This is also the full prescribed R40/R75 return, including all signed lower
terms, whenever the endpoint is in G. To see this, write c=U(b) and

    x=S(c)=(3c+1)/4,       y=S(x)=(9c+7)/8.

For c=905 modulo8192, x is canonical of the form8t−1 with t=1 modulo4, and
y is canonical and2 modulo3. The deterministic formal plans therefore give

    H_c=delta_c+H_x,       H_y=−delta_x+H_x,
    A_c=A_y.                                                (3)

The R40 lower two-arrow path cancels (3) exactly. The blocked upper path
and its R75 returning conversion have opposite rows. Consequently the full
composed pair comparison is exactly

    C_b=D_b+H_c−H_b,
    requests={c:+1}+A_c−A_b.                                 (4)

This is a row-for-row identity, not only equality of divergence. Its unique
largest request is c with coefficient+1 and rank3c>3b.

## 2. Exact finite count at one positive seed

For r>=0 define

    C_r=223(729^r−512^r)/217,
    U^r(b)=(729^r b+C_r)/512^r.                               (5)

The integer C_r exists since729=512 modulo217. Exactly the positive integers
in the single cylinder

    b=(512^r*905−C_r)*729^(−r) mod2^(13+9r)                   (6)

make at least r complete guarded returns. The modulus includes the final
guard. For any fixed positive b in G the maximum is exactly

    r(b)=floor((v2(217b+223)−13)/9).                          (7)

After these r(b) returns the last guarded source has order13 through21.
There is one further native comparison (2) to an endpoint outside G.
Positivity makes Y(b) a nonzero integer, so (7) is finite. Arbitrarily long
finite cylinders have positive integer representatives; these representatives
vary with the requested length. No positive infinite trajectory follows.
The affine fixed point is the negative rational −223/217.

For s>=1 native steps, with s<=r(b)+1, let b_i=U^i(b). Exact telescoping gives

    D_(b,s)=sum_(i=0)^(s−1) D_(b_i),
    div D_(b,s)=[3b]−[3b_s],
    C_(b,s)=D_(b,s)+H_(b_s)−H_b,
    requests={b_s:+1}+A_(b_s)−A_b.                           (8)

The ordinary clocks of D_(b,s) are `(6s+3,3)`, and its quotient clock is6s.
For example, the equality of the two ordinary prefixes for one step permits
successive extension of the upper prefix by six arrows; the intervening
three-arrow prefixes cancel. Every b_s>b. Every other request in (8) has
rank below3b_s. Thus the growing request cannot disappear through cancellation
with the displayed helpers.

## 3. Complete binary exit phases

At the last guarded source write

    Y(b)=2^H omega,       omega positive odd,       13<=H<=21,
    c=U(b),              D=v2(9c−1).

The exact identities

    217(9c−1)=(6561*2^H*omega−2^13*139)/2^9,
    217(3z+1)=19683*2^(H−13)*omega−200,  z=(9c−1)/16         (9)

give the following full binary classification of the next local R40 step.
The second line applies only when D=4.

| H | D and the upper canonical test |
|---|---|
|13|D=4+v2(6561*omega−139)>=5; use the ordinary R40 D-row.|
|14 or15|D=4; 3z is canonical exactly when omega=3 modulo4.|
|16|D=4. Put k=v2(19683*omega−25), t=(19683*omega−25)/(217*2^k). Then 3z is canonical exactly when t differs from3^(k+3) modulo4.|
|17|D=4 and 3z is always canonical.|
|18 through21|D=4 and 3z is always selected, hence noncanonical.|

For H16, `3z+1=2^(k+3)t` and k>=1, which proves the stated exact selection
test. The other lines follow directly from (9). These are local binary
phases, not success claims at the original starting rank.

## 4. The H17 exit can decrease locally and increase globally

Fix r>=0 and any positive b with

    v2(217b+223)=9r+17.                                     (10)

These are entire progressions:

    b=(2^(9r+17)−223)*217^(−1) mod2^(9r+18).                 (11)

There are r complete returns, followed by the native step to
`c=U^(r+1)(b)`. The next local R40 step has D=4 and canonical upper root

    q=3z,        z=(9c−1)/16,        z=5 mod8 and5 mod9.       (12)

Here c=137 modulo512. Its lower two-arrow path again cancels H_c−H_y by
(3): x=(3c+1)/4 is canonical, and y=(9c+7)/8 is canonical and2 modulo3.
The whole comparison therefore simplifies exactly to

    C_exit=E_(b,z)+H_z−H_b,
    requests={z:+1}+A_z−A_b,                                (13)

where `div E_(b,z)=[3b]−[3z]`. Its ordinary clocks are `(6r+12,4)` and its
quotient clock is `6r+8`. The R40 upper prefix contributes two ordinary
arrows to the selected partner6z+1, whose merger with3z takes four arrows.
This proves both clocks and the equality of the full signed prefix tables.

**Theorem.** The unique largest request in (13) is z with coefficient+1.
The comparison strictly decreases the original rho exactly when r=0.
For every r>=1, its leading rank exceeds3b.

Indeed, A_z has rank at most z and A_b at most b. Also

    3z=(27U^(r+1)(b)−3)/16.

For r0,

    3b−3z=(4893b−4485)/8192>0.

The coefficient of3b in3z is `(9/16)(729/512)^(r+1)`. At r1 it is
`4782969/4194304>1`, and then increases. Its affine constant is already
positive at r0 and increases. Thus3z>3b for all r>=1. The local step at c
always decreases from3c, but that is a different starting rank. For long r,
some helpers may also exceed3b; no bound of every helper below the original
rank is asserted. The leading request nevertheless exceeds all of them.
The accepted r0 cases are already covered by the native/R52 continuation;
this theorem adds no accepted domain.

## 5. The two standard inverse choices do not repair this exit

Apply the two base inverse rays of
[the nonselected interface](../nonselected_inverse/NONSELECTED_INVERSE_PHASES.md)
to the leading P(z). Their exact point depths are

    h4=v3(4z+1)=1,        h8=v3(8z+1)=0.                     (14)

This holds on all (10), since `4z+1=3(3c+1)/4` and z=2 modulo3.
The k4 maximal point predecessor is exactly3c. Its forward path to the
upper root3z is the R40 upper comparison E_(c,z), with opposite current
orientation in the inverse formula. Substituting the full k4 pair plan
into (13) gives exactly (8) with s=r+1: all current rows and all signed
requests agree. It restores the preceding unfinished comparison.

For k8 the canonical inverse base is16z+1, which is1 modulo8. Its compulsory
forward arrow and normalizer are exactly how the formal H at this base
begins. They cancel the inverse comparison. Substitution therefore restores
(13) itself, row for row. A zero point depth here is not an extra downward
step. Neither operation supplies the missing current or lowers the original
rank for r>=1.

These claims concern precisely the two base rays and the deterministic
formal H. Higher rays, different words, supplied histories and joint
comparisons remain available.

## 6. Why a local W9 contraction is only a stopping interface

For a nonblocked local W9 plan at input c, let M=3c. Every retained request
has rank at most

    B(M)=(27M+23)/32.                                       (15)

The D6 noncanonical-upper row attains this bound. The D8 row has rank
`(81M+101)/128`; further even rows decrease their excess over1 by3/4.
The odd rows and canonical-upper even rows are smaller. These follow directly
from the complete R40 local endpoint formulas.

Along a chain that continues to use only these nonblocked W9 rows,

    M_k <= 23/5 + (27/32)^k (M_0−23/5).                      (16)

For an original target rank N>23/5 the finite inequality

    (5M_0−23)*27^k < (5N−23)*32^k

therefore forces crossing below N. This proves a finite stop **at a smaller
rank or an unhandled W5/blocked W9 leaf**. It does not prove all leaves can
be expanded by the same bound. Equations (8) and (13) show exactly why the
blocked native continuation cannot be included under (15).

## 7. Unpromoted higher-ray direction

There is an arithmetic route worth separating from the proved procedure.
At the H17 upper root3z, the two complete quotient inverse rays have bases
`8z+1` and `16z+1`, followed by `a→64a+49`. At ray index L,

    a_L+1=(64^L(81c+23)+4)/18,
    a'_L+1=(64^L(81c+7)+2)/9.                               (17)

Writing s=r+1, the native chain forces
`c=−223/217 mod3^(6s)`. To make the point inverse order exceed this forced
precision, one can match respectively

    64^L=217/3268 mod3^(6s+4),
    64^L=217/8272 mod3^(6s+4).                               (18)

Both targets are1 modulo9; powers of64 generate this subgroup. The first
smallest solutions at s1 are L6069 and L740, and at s2 are L2466444 and
L2028089. These exact congruences are not a completed current construction
or a new accepted domain. Their indices quickly become large, and all
original-rank inequalities, capacity-independent signed cancellations and
explicit premise supply would still need to be completed. The checker
records only the small modular arithmetic; it generates no huge paths.

## 8. Evidence and reproduction

Run `python3 experiments/residual_progress/native_nine_growth/check_nine_growth.py`.
The default verifies the stored receipt; `--write-receipt` refreshes it
intentionally. The checker independently recomputes ordinary arrows,
divergence, all nine binary exit phases, complete cylinders and exact counts,
full return and inverse-undo rows, local contraction bounds and invalid-input
rejections. It stores concrete unfinished H17 current tables at r1 andr2.
No absorption search or acceptance dispatcher is added.
