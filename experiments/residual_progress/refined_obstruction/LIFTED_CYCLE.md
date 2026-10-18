# A lifted inverse ray and the rotated minus-twenty-five cycle

**Status: written conditional theorem, complete arithmetic acceptance table,
and exact integer-current constructor.** A nonzero quotient inverse-ray lift
followed by a rotated cycle inverse supplies a new comparison below the
original rank. Fixed18-arrow and24-arrow instances work in infinite subrows of every
R61 CRT family and is outside all fifteen previous direct rules. All failed
plans remain explicit. This is a partial extension, not universal completion.

Use the original rho, signed P(w), and formal H notation of
[the companion classification](REFINED_ELEVEN.md). The complete quotient
inverse branches come from [R25](../bridge_normal_form/BRIDGE_NORMAL_FORM.md).
The base four-arrow interface comes from
[R56](../selected_inverse/SELECTED_INVERSE.md); the maximal inverse method and
full failure discipline are extended from [R60](../cycle_inverse/CYCLE_INVERSE.md).
Negative states identify affine words only; every constructed source is positive.

## 1. Complete domain, lifted ray, and exact inverse words

Assume w>0, w=3445 mod3456, and

    v0=(16w-13)/27=0 mod3,
    q=rho(w)=(81v0+23)/32.

Then v0=-7 mod2048 and v0>=2041, so q>=5167. R56 first reaches the
quotient inverse node3v0. Its base ray is b0=8v0+1. Take the first nonzero
ray lift, not another copy of that base:

    b=64b0+49=512v0+113.

The exact ordinary path b→q has valuation word

    (2,7,1,4).                                        (1)

Indeed its first successor is384v0+85=F^3(6v0+1), its second successor
is9v0+2, and the last two arrows are the old R56 tail. The binary congruence
v0=-7 mod2048 verifies the final valuations including their extra bits.

Put h=v3(b+25)>=1, k=floor(h/7), and a=2048/2187. For every k>=0 define

    p=a^k(b+25)-25,
    j=v3(p+1),
    eta=2^j(p+1)/3^j-1.                              (2)

The rotated seven-arrow word

    C=(1,1,2,1,1,4,1)

has affine map Psi_C(x)+25=(2187/2048)(x+25). Its inverse is legal exactly
when3^7 divides the positive odd target plus25. An inverse output y satisfies
y=-25 mod4096; that modulus includes the extra valuation bit for total
valuation11. Direct substitution verifies all seven valuations. Positivity
holds since(y+25) is a positive multiple of4096, so y>=4071.
Each copy removes exactly7 ternary powers. Consequently k is the exact maximum
number of consecutive inverse C copies; this is not maximality over all words.

For k>=1, v2(b+25)=1 gives v2(p+1)=3 and odd unit1 mod4.
Thus p is complementary canonical. For k=0, p=b is canonical1 mod8,
p=2 mod3 and v2(p+1)=1. Each point inverse(2x-1)/3 is legal
precisely at x=2 mod3. The maximal j-fold point run gives a positive canonical
eta with v2(eta+1)=3+j for k>=1, or1+j for k=0, and eta not2 mod3.
The exact ordinary eta→q word is

    1^j, C^k, 2,7,1,4,                              (3)

with clocks(j+7k+4,0). Pair normalizers retain their own currents.

Write d=h-7k and U=(b+25)/(2*3^(7k)). Then

    p+1=8*(2^(11k-2)*U-3).

Hence the complete feasibility restrictions are:

| Remainder d, for k>=1 | Point depth j |
|---|---|
| 0 | exactly0 |
| 1 | any j>=1, according to further ternary digits |
| 2 through6 | exactly1 |

All these cases are included; no maximality condition is discarded.
For k=0 put Z=256v0+57. Then p+1=2Z and b+25=2(Z+12).
If h>=2, j=1. If j>=2, h=1. At h1,j1 the terminal point is0 mod3;
at h>=2,j1 it is1 mod3. These are all zero-cycle cases, and j0 is impossible.

## 2. Complete strict-rho table, including finite intercepts

For every k>=0 the full signed plan strictly decreases rho exactly in this table:

| Maximal cycle count k | Accepted point depths |
|---|---|
| 0 | j>=14 |
| 1–6 | j>=13 |
| 7–12 | j>=12 |
| 13–19 | j>=11 |
| 20–25 | j>=10 |
| 26–31 | j>=9 |
| 32–37 | j>=8 |
| 38–43 | j>=7 |
| 44–49 | j>=6 |
| 50–56 | j>=5 |
| 57–62 | j>=4 |
| 63–68 | j>=3 |
| 69–74 | j>=2 |
| 75–80 | j>=1 |
| 81 and higher | every j>=0 |

The special failed k0,j1,eta0mod3 row retains the original request+1.
Every other failed row retains a unique highest request+1 of rank eta>q.

**Proof of the exact height comparison.** With t=(2/3)^j,

    eta=lambda*q+beta,
    lambda=(16384/81)*a^k*t,
    beta=-t*((598/81)*a^k+24)-1 < -1.                (4)

Every passing row follows from lambda<1. To establish all failures including
intercepts, compare the13 last failing pairs(end of a table row,one less than
its required j), together with k0,j13. At q=5167, exact multiplication gives eta-q>0 for each pair.
Equivalently, put D=3^(7k+j) and check

    81D*(eta-q)
      =(16384*2^(11k+j)-81D)*q
        -598*2^(11k+j)-1944*2^j*3^(7k)-81D.          (5)

These14 positive integer comparisons and the15 first passing lambda
comparisons are reproduced by the checker. At a fixed failing pair the slope
is greater than1, so the failure persists for q>=5167. At this range eta+1
is positive throughout the boundary rectangle; reducing k or j increases eta.
This proves every remaining failed cell. For k>=81,j0 already passes.
No asymptotic slope approximation decides a finite case.

## 3. Complete currents and failure vectors

Let I be the negative current of (3), so div I=[q]-[eta], and z=nu(w).
Return the full plan

    J=N_(3w)+I-N_w+J_eta-J_z,
    c=A_eta-A_z.                                    (6)

Thus div J=P(w)-sum c(u)P(u), with signed multiplicities combined exactly.
For k>=1, or k0,j>=2, eta is canonical, eta=7 mod8, and eta=0 or1 mod3. Its first
critical index is eta/3 or(2eta+1)/3 respectively, always W5, with rank eta
and coefficient+1. Every other request from H_eta is below eta. Every request
from H_z is below q, since z<w/4. This proves both necessity and sufficiency
of the table for this entire plan, not merely for an endpoint bound.

When k0,j1 and eta1mod3, its critical index(2eta+1)/3 is W5 with the same
unique-leading conclusion. The remaining case k0,j1,eta0mod3 is different.
Put u=eta/3 and z1=32v0+7. Then

    u=(1024v0+225)/9=9 mod16,
    v2(9u-1)=5,
    S^2(3u)=F(3z1),   S^2(u)=F(z1).

Complete W9 elimination therefore gives A_eta=A_(3z1)-A_z1+A_u.
The actual H recursion has A_u=A_z1: its first successor is selected,
its elementary half has a decreasing1-mod8 arrow to z1. Moreover
3z1=F^2(6v0+1), and nu(6v0+1)=3v0. Thus A_eta=A_(3v0).
The same elementary prefix identities, with their signed rows, show that
(6) is exactly the old R56 ray4,depth0 current and request vector. The
checker retains complete equality, not merely its highest coefficient.
This row retains P(w)+1. If the lifted b were used without point normalization,
it too would return that old zero-depth plan; this baseline does not justify
discarding the new k0,j>=14 successes.

The compiler accepts only descending plans and checks an exact supplied current
for each nonzero remaining P(u). Missing or malformed supplies are rejected.
The theorem does not provide those inputs universally. Individual pair proofs
are being composed; no annular source-capacity assertion is made.

## 4. Every parameter row has full CRT realizations

For k>=1 write b+25=2*3^(7k)*U, hence

    v0=(3^(7k)*U-69)/256.

The binary condition is exactly

    U=(256*2041+69)*3^(-7k) mod2^19.                 (7)

It supplies v0=-7 mod2048 with the extra bit required in(1). For d=0 choose
either nonzero U mod3; then j0. For d>=2 choose U=3^d*e mod3^(d+1), e1/2;
then j1. For d1 write U=3V. To obtain j1 take
2^(11k-2)V=2 mod3. To obtain any j>=2 take either e1/2 and

    2^(11k-2)V=1+3^(j-1)*e mod3^j.                  (8)

These conditions are coprime to(7), yielding complete infinite progressions.
For k0, impose(7) with k0 on U=256v0+69, and instead use these exact ternary
conditions: U=6 mod9 for h1,j1; U=3^h*e mod3^(h+1) for h2..6,j1;
or U=12+3^j*e mod3^(j+1) for h1,j>=2. These give every feasible zero-cycle row.

## 5. New18-arrow and24-arrow comparisons inside every R61 family

Fix arbitrary r>=16,A>=5,K>=0. Retain the full binary condition(1) in
the companion note, now with M=7r+10. The simplest new row is

    s=(1735+3^14*e)*2^(-(11r+24)) mod3^15, e=1 or2. (9a)

Here Z=256v0+57=2^(11r+24)s-1735 has exact ternary order14, so k0,j14.
The complete word is1^14,2,7,1,4, with18 ordinary arrows and eta<q.
The old R60 has

    4v0+9=(Z+519)/64,

of exact order1, so it fails. The residue in(9a) is2^r mod3, and hence
compatible with the original R61 CRT and every prescribed K.

A separate24-arrow row uses either e=1 or2 and

    U=2^(-9)*(1+3^12*e) mod3^13,
    s=(1723+3^8*U)*2^(-(11r+24)) mod3^21.            (9)

CRT with the binary condition gives a whole positive infinite progression
of s. Its ternary residue is2^r, so it lies in the original R61 class.
Since v0=2^(11r+16)s-7,

    256v0+69=2^(11r+24)s-1723=3^8*U,

where the last equality means exact order8 and the indicated U residue.
Thus the new maximal cycle count is k1, remainder1, and j13. The accepted
word(3) has exactly24 ordinary arrows and endpoint below the **original q**.
Its binary p and eta conditions are already guaranteed above; r,A,K do
not occur in this clock.

The old R60 simultaneously fails in this second row too. Modulo3^8,

    4v0+9 = 507/64 =3*169/64.

Hence v3(4v0+9)=1, so the old inverse has zero complete cycles. By the
companion complete classification, every member of(9a) or(9) is outside all fifteen
previous direct rules, at both original w and leading v. This is genuine
new direct coverage, not reclassification of a previously accepted seed.

The leading pair itself is still unresolved by those fifteen rules. The new
construction certifies P(w) conditionally from smaller-rank pair inputs;
it does not discard the leading request of the old exit representation.
Different exact representations can have different unresolved premises.

## 6. Verification and limitations

Run `python3 experiments/residual_progress/refined_obstruction/check_refined_obstruction.py`.
It checks exact boundary inequalities, every maximal remainder, actual valuation
words, complete failed vectors, CRT intersections and supplied-current
substitution. Its finite receipt is evidence for the implementations. The
written arithmetic gives the infinite quantifiers. No claim of novelty,
formal verification, universal Collatz convergence, or completeness over all
inverse words is supplied.

The stored receipt has3298 exact affine checks;15 first-passing and14
last-failing boundary inequalities;43 complete signed plans (13 descending,
29 higher-leading failures,one exact self-return);16 new CRT rows; and15
invalid/missing-input rejections. Actual supplied conversions at36641534965
and30124219061365 produce102 and215 current rows from9 and15 supplied
pairs; both full tables are stored. The second fixture is already accepted
by an older rule and is used only to test the positive-cycle conversion.
A third conversion, at the first r16,A5,K0 eighteen-arrow CRT fixture, has
1746 rows from42 supplied pairs. Its source and current hash are retained.
Finite fixture searches have a10000-arrow cap, cycle detection and a4096-bit
cap; none supplies a universal premise. The R63 classifications and current
undos in the same receipt have their separate stated scope.
