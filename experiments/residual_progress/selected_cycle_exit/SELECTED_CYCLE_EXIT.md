# Maximal selected cycles and a descending exit after any number of repetitions

**Status: written infinite-family theorem, complete finite exit interface, and
conditional integer-current construction.** Every prescribed number of the
growing R54 cycles has an entire arithmetic progression of exits whose
remaining W5 pair inputs have strictly smaller original critical-image rank.
Those inputs are explicit premises. Universal supply and Collatz remain open.
The complete exit interface below covers the whole R54 entry phase; it does
not assert that every exit passes its rank test. No novelty claim is made.

Use positive odd Syracuse S, absorbed at 1, the elementary minimum nu and
canonical quotient T=nu S. Write P(w)=[3w]-[w], W5={w>0:w=5 mod8},
rho(w)=nu(3w), and [1]=0 in current boundaries. The formal absorption
plan H_s is the deterministic R43 plan with all W9 requests eliminated.
It obeys

    [s] = div H_s + sum_u h_s(u) P(u),
    rho(u) <= (9 nu(s)+5)/8 <= (9s+5)/8.                 (1)

The h_s(u) are signed integers. No current for a missing P(u) is assumed.
References: [R43](../critical_rank/CRITICAL_IMAGE_RANK.md),
[R54](../rule_avoidance/RULE_AVOIDANCE.md), and the complete
[R26 run bridge](../complementary_bridge/RUN_BLOCK_BRIDGES.md).

## 1. Exact maximal copies of the guarded cycle

The R54 entry phase is

    q=-17 mod5184,       w=(2q+1)/3=3445 mod3456.          (2)

Every q in (2) is canonical complementary and rho(w)=q. Put

    E=v2(q+17),  u=(q+17)/2^E,
    r=floor((E-6)/11),  e=E-11r in {6,...,16}.

Here u is a positive odd multiple of81. The maximum number of consecutive
copies of the **specified guarded seven-row T cycle**, with each endpoint
again in the entry phase, is exactly r. Its last endpoint is

    Q=3^(7r) 2^e u-17.                                  (3)

Indeed the R54 cycle is

    Psi(x)=(2187x+2363)/2048,
    Psi(x)+17=(2187/2048)(x+17),

and its guard is v2(x+17)>=17. Each copy removes exactly11 binary factors
and preserves the factor81. After r copies the guard fails. Conversely a
further copy of this specified affine return ending with 64|(Psi(Q)+17)
would require e-11>=6. This is impossible. This is not a statement about
all conceivable later returns to the phase through different itineraries.

There is also an exact ordinary-clock strengthening. Each guarded cycle
current equals the seven ordinary arrows with valuations

    (1,1,1,2,1,1,4),       S^7(x)=Psi(x).                (4)

For Z=x+17, their successive states are

    x,
    3Z/2-25, 9Z/4-37, 27Z/8-55,
    81Z/32-41, 243Z/64-61, 729Z/128-91,
    2187Z/2048-17.

Substitution proves every valuation, including the final extra bit. The
ordinary word in (4) already holds when v2(Z)>=12. The stronger >=17
guard ensures the stated canonical T cycle and return to (2). Thus it
would be incorrect to say the ordinary word necessarily fails at Q.

For equality of currents with the quotient construction, its fourth
ordinary state Y is selected with v2(Y+1)=3. With V=(Y-1)/2,
S^3(Y)=S^3(V). The elementary Y-to-V current is the difference of these
two three-arrow prefixes; its negative prefix cancels the next three
quotient arrows. This yields exactly (4), including all row coefficients.
Consequently (3) is reached in both 7r ordinary and 7r quotient steps.

## 2. Complete exit interface

Write Q=2^e U-17 with U odd and divisible81, and 6<=e<=16. Q has first
binary exponent a=4. Its complete R26 parameter is

    d1=2+v2(27*2^(e-6)U-7).                             (5)

For e=6, d1>=3: use this one complete R26 block and retain its raw
endpoint f. This includes arbitrarily large d1, not a bounded-depth
approximation. For e>=7, d1=2 and the first block has ordinary length4:

    Y=S^4(Q)=81*2^(e-5)U-41.

Normalize Y exactly to V=nu(Y). From V take one full R26 block if it is
complementary, one ordinary arrow if V=1 mod8 and V>1, or no arrow if
V=1. Retain that block's raw endpoint f. This is a complete prescription
for every exit in (2); it makes no orbit search or absorption assumption.
The following table makes all binary cases explicit.

| e | First endpoint or normalization | Next block / raw endpoint |
|---|---|---|
| 6 | One R26 block (a=4,d=d1) | Its exact raw endpoint; no second block |
| 7 | Y=324U-41; selected iff U=3 mod4 | If selected, V=162U-21=1 mod8 and f=(243U-31)/2. Otherwise V=Y has a=2,d=v2(243U-31)>=2 |
| 8 | Y=648U-41, a(Y)=3+v2(81U-5)>=4 | Normalize exactly; take the stated canonical forward or complete-run branch |
| 9 | V=Y=1296U-41, complementary a=3 | d=1+v2(729U-23)>=2 |
| 10 | V=1296U-21, complementary a=2 | d=2, f=1458U-23 |
| 11 | V=2592U-21, complementary a=2 | d=3, f=729U-6 |
| 12 | V=5184U-21, complementary a=2 | d=4+v2(243U-1)>=5 |
| 13 | V=10368U-21, a=2,d=4 | f=8748U-17; selected iff U=3 mod4 |
| 14 | V=20736U-21, a=2,d=4 | f=17496U-17; selected iff U=3 mod4 |
| 15 | V=41472U-21, a=2,d=4 | f=34992U-17, a(f)=4+v2(2187U-1)>=5 |
| 16 | V=82944U-21, a=2,d=4 | f=69984U-17 always selected; nu(f)=34992U-9 |

In the variable a,d rows the full R26 formulas apply. Specifically, if
x=2^a t-1 is complementary, d=v2(3^(a-1)t-1), and
v=(3^(a-1)t-1)/2^d, its raw endpoint is

    f=3^floor(d/2)v                   if d odd,
    f=2*3^(d/2)v+1                   if d even.           (6)

Its quotient clock to nu(f) is a+floor(d/2)-1. Its ordinary common-tail
clocks are (a+floor(d/2),1) for odd d and (a+d/2-1,0) for even d.
The normalizations here use exact elementary currents, never a fictitious
ordinary arrow. Formula (5), Y+1, and

    v2(3(V+1)/4-1)=v2(243*2^(e-8)U-16), e>=10,

prove the table. All finite cases reduce to these integer identities;
the implementation also retains the entire variable-depth branches.

## 3. A descending full progression after every maximal repeat count

**Theorem.** For every integer r>=0, every odd d>=2r+5, and every positive
integer s in the following exact progression, define

    b=(d-1)/2,
    s = 3^(-7r-9)(1+2^(d-4)) mod2^(d-3),
    q=81*2^(11r+12)s-17,       w=(2q+1)/3.              (7)

The inverse power is taken modulo2^(d-3). Then w is in (2), exactly r
guarded cycle copies precede its exit, and the e=12 interface has endpoint

    f=3^b(3^(7r+9)s-1)/2^(d-4).                        (8)

It satisfies

    (9f+5)/8 < q=rho(w).                               (9)

Thus this entire progression admits an exact signed P(w) comparison
whose W5 input ranks are strictly smaller. This holds for every r; no
maximum excursion length is fixed. It supplies a conditional reduction,
not the still-missing currents for every input.

**Proof of the domain and clocks.** The residue in (7) is odd and positive
as its least positive representative; its modulus retains the extra bit
needed for v2(3^(7r+9)s-1)=d-4. Hence E=11r+12 and exactly r guarded
copies leave exit exponent12. In Section2's notation
U=81*3^(7r)s. The first exit block normalizes to

    V=3^(7r+8)*64s-21,

with a=2 and second depth d from (7). Substitution in (6) gives (8).
The total quotient clock to nu(f) is

    K=7r+b+5.                                         (10)

The ordinary common-tail equality is

    S^(7r+b+6)(q)=S(f).                                (11)

For (11), the first exit block reaches selected Y in four ordinary arrows,
and S^3(Y)=S^3(V). The second block uses b+2>=4 ordinary arrows from V
and one from f. These are long enough to extend the equal-time merger
through all b+2 steps. Add the 7r ordinary arrows from (4). The complete
current from q to f is the difference of exactly those two paths; no
later orbit information is required. At d=2r+5 the clocks are
K=8r+7 and ordinary (8r+8,1).

**Proof of strict rank decrease.** Multiplication by2^(d-4) shows (9) is
equivalent to

    [3^4*2^(11r+d+11)-3^(7r+b+11)]s
       > 141*2^(d-4)-3^(b+2).                          (12)

The right side is positive for odd d>=5. It is enough that the left
coefficient exceeds the right side, or equivalently

    2^(d-4)(3^4*2^(11r+15)-141)
       > 3^(b+2)(3^(7r+9)-1).                         (13)

At d=2r+5, the left side is strictly greater than
3^4*2^(13r+15); the right side is strictly less than3^(8r+13).
The required comparison follows from
2^15>3^9 and2^13>3^8. Increasing d by2 multiplies the two sides of
(13) by4 and3 respectively. Thus (13) holds throughout (7), proving
(12) for every positive s, not merely the least representative.

The w progression in (7) has residue
54*2^(11r+12)s_0-11 and period27*2^(11r+d+10), where s_0 is the least
positive residue in (7). These are complete infinite arithmetic families.
All their initial inputs fail the fixed seven direct rules by the whole
phase argument of R54. This does not claim disjointness from every newer
rule or from individual finite absorption histories.

There is also a complete subprogression missed by both the new R55
selected-forward dispatcher and the R56 two-inverse-ray dispatcher.
Impose the additional, coprime ternary condition

    2^(11r+17)s=1 mod3.                                 (16)

R55 sees first parameters (a,d)=(4,2), which its complete table rejects;
its second-block option has domain (2,2) and therefore does not apply.
For R56 the auxiliary parameter is

    v=(32q-23)/81=2^(11r+17)s-7=0 mod3.

Both inverse-ray valuations v3(4v+1) and v3(8v+1) are then zero, so
neither ray is descending. Conditions (7) and (16) have one nonempty
class modulo3*2^(d-3). Thus the successful exit theorem has direct
coverage beyond those two dispatchers for every r and permitted d.
The older R52/R53 additions have returning-divisible-by3 or nonselected
domains respectively; (2) belongs to neither. This comparison is against
the stated direct rules, not all possible recursive substitutions or
all already-known finite currents. `family(...,avoid_inverse=True)`
constructs exactly this CRT subprogression; its w period is three times
the period stated above.

## 4. Full signed pair construction and its exact scope

Let N_x be the elementary current with boundary[x]-[nu(x)], and let D
be the full cycle-and-exit current from q to f constructed above. Put
z=nu(w) and

    J=N_(3w)+D-N_w+H_f-H_z,
    c(u)=h_f(u)-h_z(u).                                (14)

Then

    div J=P(w)-sum_u c(u)P(u).                         (15)

All coefficients are retained before cancelling equal rows or requests.
For the high inputs, (1) and (9) give rho(u)<rho(w). For the low inputs,
w=5 mod8 implies z< w/4, hence

    9z+5 < 9w/4+5 < 8q

on the phase w>=3445. They too have strictly smaller rank. Substitution
of exact supplied pair currents C_u gives J+sum c(u)C_u, with exact
boundary P(w). A missing, malformed, or nondecreasing premise is rejected.

For arbitrary exits, `exit_plan` uses the previously proved piecewise
R44 absorption bound B(f), which can improve on (9f+5)/8. It returns
`descending` exactly when B(f)<q; otherwise it retains an `unresolved`
plan. This is an exact test of this sufficient bound, not a classification
of all possible currents. `one_step` returns only descending plans and
can join a common-rho dispatcher. It does not belong to the separate
sigma induction without a fresh compatibility check.

## 5. Reproduction

Run `python3 experiments/residual_progress/selected_cycle_exit/check_selected_exit.py`.
The receipt records finite checks of all eleven exit rows, maximal-cycle
counts, both clocks, exact currents, full progression examples, and a few
conversions using explicitly supplied capped finite input histories.
`--write-receipt` regenerates that evidence. The infinite statements are
proved above; finite samples do not establish their quantifiers.

The focused check covers352 complete exit cases (all e=6..16 and odd
s=1..63),264 maximal-cycle cases (r=1..8, all eleven exit exponents,
and three odd indices), and128 progression cases through r=64. Of the
latter,64 include the extra CRT condition excluding the R55 and R56
direct dispatchers. It checks eight invalid requests and retains an
explicit e=16,r=10 failure of the sufficient bound.

Three actual supplied-input substitutions yield P(1105909),
P(11324620789), and P(121530394607605), with142,178,252 output rows
respectively and maximal guarded-cycle counts0,1,2. All three output
tables and the18 distinct supplied pair-current tables are retained in
[selected_exit_audit.json](selected_exit_audit.json). Demonstration input
discovery is capped at10000 odd steps and4096 bits, with cycle detection;
failure to meet the cap would leave that demonstration unresolved.
