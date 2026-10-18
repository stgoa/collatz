# Valuation debt across actual current comparisons

**Status: written local progress theorem, whole-family obstruction, and exact
conditional-current implementation.** The mixed growing block has an explicit
positive-integer potential on its two leading edges. It cannot be extended to
a global rank by any phase-dependent monomial combination of the two natural
linear sizes and their binary orders. A complete accepted R44 family resets
the proposed debt by an arbitrarily large amount. All signed helpers remain
present. This is not an obstruction to every arithmetic potential, to a larger
state, or to other current constructions. Collatz remains open.

Dependencies: [R67's mixed block](../mixed_rank_recursion/MIXED_GROWING_BLOCK.md),
[R44's returning forward plan](../returning_phase/RETURNING_FORWARD_INTERFACE.md),
and [R43's absorption bounds](../critical_rank/CRITICAL_IMAGE_RANK.md).
Use positive W5 pair indices, P(w)=[3w]-[w], rho(w)=nu(3w), and ordinary
odd-only Syracuse steps. E is the returning class w3mod9 with selected3w;
W denotes its complement in W5, not a different set of allowed pair indices.
No universal pair input is assumed.

## 1. Exact binary debt transport through the growing block

Set

    D=7153, B_W=311195, B_E=656187,
    L_W(w)=Dw+B_W, L_E(u)=Du+B_E,
    H_W(w)=v2(L_W(w)), H_E(u)=v2(L_E(u)).                 (1)

These positive linear forms define finite nonnegative orders at every
positive input. R67's complete binary cylinder w40529845mod2^26 gives actual
accepted comparisons with leading requests

    w in W -> u=(2187w+1209)/1024 in E
           -> v=(243u+17)/512 in W.                   (2)

The first is the sigma fifth-exponent rule; the second is the rho-valid
R44 returning rule. Both leading coefficients are+1 in their full signed
plans. Direct arithmetic gives

    L_E(u)=(3^7/2^10)L_W(w),
    L_W(v)=(3^5/2^9)L_E(u),                            (3)
    H_E(u)=H_W(w)-10,
    H_W(v)=H_W(w)-19.

The different centre at the intermediate phase is forced by(3), not chosen
by a finite fit. Thus the positive-integer function

    K(s)=L_phase(s)*2^H_phase(s)                        (4)

strictly decreases on these two **leading** edges: its ratios are exactly
3^7/2^20 and3^5/2^18. The product also strictly decreases on every guarded
mixed block. This is only a leading-state statement. It asserts neither
that all other signed helpers decrease K nor that subsequent block exits
obey this rule. The old rho/sigma validations of the full currents remain
the ones proved in R67.

## 2. A complete valid comparison that resets the debt

For every integer H>=26 choose any positive integer u satisfying

    Du+B_W=2^H mod2^(H+1),
    u=13 mod81.                                       (5)

CRT gives a complete infinite progression with period81*2^(H+1).
The first condition places u inside R67's nonreturning binary cylinder;
in particular u5mod8,3u is canonical and rho(u)=3u. The second condition
also makes u outside E. Define

    w=(64u+5)/9.                                      (6)

Every such w is a returning W5 input with exact initial exponent a3.
Indeed

    3w+1=8t, t=(8u+1)/3,
    t odd, t=3mod4, w=3mod9,
    q=rho(w)=(32u+1)/3,
    r=(9t-1)/2=12u+1=F(3u).                          (7)

The original returning forward word is(1,2), from q to r, followed by the
usual elementary normalization to3u. Thus T^2(q)=3u and S^3(q)=S(3u):
the ordinary common-tail clocks are(3,1), not(2,0). It is one of R44's complete accepted
a3/noncanonical-endpoint cases. The full current is

    J=N_(3w)+path(q->r)-N_w+H_r-H_z, z=nu(w),          (8)
    div J=P(w)-sum_x (A_r(x)-A_z(x))P(x).

Since r=F(3u), A_r={u:1}+A_u. The direct request P(u) has rank3u<q;
all other requests in H_u have rank at most(9u+5)/8<3u. Also

    z<=(w-1)/4=(16u-1)/9,
    every H_z rank <=(9z+5)/8 <=2u+1/2 <3u.           (9)

Therefore the final signed vector has a **unique highest request P(u),
coefficient+1**, and every request strictly decreases the original rho.
There is no absent-supply assumption hiding this child. More precisely,
the **entire** signed frontier has exactly three requests:

    P(u)+P(a)-P(b),
    a=(u-13)/72, b=(32u-11)/81.                       (9a)

Here a,b are positive W5 indices. To verify the cancellations, the fixed
binary phase and u13mod81 give these prescribed absorption steps:

- Normalize u=F^2((u-5)/16); its canonical minimum is2mod3 and takes the
  inverse predecessor(u-13)/24=3a, a direct W5 critical root. Hence
  A_u={a:1}+A_a.
- The raw sibling predecessor of w is z0=(16u-1)/9. Its selected half
  is z=nu(w)=(8u-5)/9, a canonical2mod3 seed; its inverse predecessor
  is(16u-19)/27=(3b-1)/2, the critical image of b. Hence A_z={b:1}+A_b.
- Write u=648c+13, so a=9c and b=256c+5; the fixed binary guard gives
  c=101mod128. Normalize b=F(64c+1), then take the two
  canonical1mod8 arrows64c+1→48c+1→36c+1=F(a). Thus A_b=A_a.
  The currents satisfy J_b=G+J_a exactly, where
  G=delta_b+delta_(48c+1)+delta_(36c+1)-delta_a and div G=[b]-[a].

The fixed binary residues make every stated canonical/selected choice
exact. Combining them with A_r={u:1}+A_u proves(9a), including its minus
sign. The checker retains the current equality as well as the coefficient
cancellation. Negative helper coefficients remain mandatory exact inputs.

That statement concerns this unchanged R44 compiler. The subsequent
[R73 joint normalizer](../frontier_progress/SIGNED_FRONTIER_NORMAL_FORM.md)
constructs an explicit current for P(b)-P(a) and proves that the entire
three-request frontier reduces to P(u), with the full current equality
J_44-C_II(b)=C_I(w). It removes both helper premises by exact cancellation;
the positive P(u) remains required and still resets the valuation debt.

Nevertheless, the proposed valuation debt resets:

    9L_E(w)=64L_W(u)-13975032,
    v2(13975032)=3,
    H_E(w)=3, H_W(u)=H.                              (10)

The middle equality and H>=26 prove the exact parent order. The ratio in(4)
is

    K(u)/K(w)=9*2^(H-3)*L_W(u)/(64L_W(u)-13975032)
             >9*2^(H-9).                            (11)

It is unbounded, even though rho(u)/rho(w)=9u/(32u+1)<9/32. Thus a
substantial original-height descent can create arbitrarily large debt.
This family is already supplied as a conditional R44 rule. It is a
progress-measure obstruction, not an additional coverage claim.

## 3. No two-phase monomial repair of this type

Consider arbitrary positive constants C_W,C_E, real exponents alpha_W,
alpha_E>=0, and arbitrary real beta_W,beta_E. Define on the two phases

    Phi(s)=C_phase * L_phase(s)^alpha_phase
                   * 2^(beta_phase H_phase(s)).       (12)

**Theorem.** No such function can be nonincreasing on every actual accepted
leading dependency in(2) and every R44 comparison(5)–(8), while strictly
decreasing across each completed R67 growing block. Consequently no member
of this class is a global strict dependency rank for those two rule families.
The same statement covers their logarithmic additive versions.

**Proof.** First keep H_W(w)=26 fixed in the R67 cylinder and let w tend
to infinity along its exact-order progression modulo2^27. The orders of u
and v are then16 and7. If the first edge is always nonincreasing, its
size factor in(3) forces alpha_E<=alpha_W. The second forces the reverse
inequality. Hence alpha_E=alpha_W=alpha.

Now take arbitrarily large exact values H=H_W(w), which have nonempty
positive progressions because D is odd and the R67 guard is precisely
H>=26. With the size exponents equal, the ratios in(3) have size factors
independent of w. The first edge requires beta_E<=beta_W as H tends to
infinity. The second requires beta_W<=beta_E. Thus both equal beta.

The phase constants cancel across a complete block, whose ratio is exactly

    (3^12/2^19)^alpha * 2^(-19 beta).                  (13)

Since3^12>2^19, beta<=0 makes this ratio at least1. Therefore strict
block decrease requires beta>0. But on(5)–(8), using(10),

    Phi(u)/Phi(w)
      >(C_W/C_E)*(9/64)^alpha*2^(beta(H-3)),           (14)

which tends to infinity. This violates nonincrease on an already valid
returning comparison. The contradiction includes alpha0 and all positive
phase constants. No numerical optimization or limiting density assumption
is used. ∎

The conclusion is unchanged if each phase also uses an arbitrary fixed
power of the **other** existing linear form's binary order. Indeed
v2(B_E-B_W)=5. In(2), the inactive order is exactly5 at w,u,v, so its
factor is absorbed into each phase constant in the preceding argument.
In(5)–(8), the child orders at(L_W,L_E) are(H,5), and both parent orders
are3. Those extra factors are again bounded constants and cannot offset(14).
Thus merely evaluating both old centres in both phases does not repair the
obstruction.

This rules out the specified two-centre power/logarithm class, even though
it uses an unbounded valuation state. It does not rule out a nonmonomial
rank, more centres, a context-dependent amortized argument, an unbounded
arithmetic state or different rule choices. It also does not turn the
leading-state function(4) into a full-current potential before rejecting it.

## 4. What a finite set of valuation centres would have to preserve

The following elementary pole test clarifies a possible next state choice.
Let a legal affine comparison be parent g(u) and child u on a complete CRT
family approaching a rational binary-integer theta. Suppose finitely many
nonzero affine forms are used to define each phase's valuation terms, with
fixed real weights, and a common nonnegative power of a positive size
comparable to the ordinary integer height. In the family below the two
heights have a fixed positive limiting ratio, so their common power cannot
absorb a valuation jump.

For each affine form f not vanishing at theta, v2(f(u)) is eventually
constant as v2(u-theta) tends to infinity. This follows directly by writing
f(u)=f(theta)+a(u-theta); once the second summand has greater order, the
first determines the order. A form vanishing at theta instead has order
v2(u-theta)+v2(a). The same argument applies to parent forms pulled back
through g.

It follows that the coefficient of the growing order in the logarithmic
child/parent potential ratio is

    sum of child weights at centre theta
      minus sum of parent weights at centre g(theta).           (15)

If this coefficient is positive, the proposed nonincrease fails on a
whole sufficiently deep CRT subfamily. Other finitely many centres
contribute only bounded constants. This is a necessary centre/weight
compatibility condition on a **proved legal branch**, not an assertion
that every finite-centre collection fails globally.

For(5)–(8), the original child centre and its required parent image are

    theta=-311195/7153,
    g(theta)=-6626905/21459,
    21459w+6626905=(64/3)(7153u+311195).                (16)

The second centre differs from the natural returning centre
-656187/7153. A positive weight at theta must therefore be carried by a
matching parent weight at the new centre if this affine-valuation strategy
is to rank the whole branch. Its order would be H+6. Whether a larger
collection, another functional form, or context can handle all actual
branches and exits remains open; no closure theorem is claimed.

One further candidate is the R44 a3 ray lift r=F^L(3u), whose parent
would be g_L(u)=(16r-1)/27. Its pulled-back valuation centre varies with L.
Only L1 is established here. At larger L the lower absorption helpers can
exceed3u or cancel the proposed child, so legality and survival of that
child would both need proof before inferring any need for infinitely many
centres.

## 5. Exact verification and supplied currents

Run `python3 experiments/residual_progress/arithmetic_progress/check_valuation_debt.py`.
The checker verifies the actual two leading comparisons, all arithmetic
identities, exact-order CRT families, full R44 signed vectors and divergence,
and complete supplied-current substitutions at designated inputs. Failed
candidate potentials do not alter the validity of those original rho
currents. Search caps in the supplied fixtures are finite evidence only.
No existing rule, dispatcher or receipt is modified.

The frozen receipt records14 exact leading transports (including two large-height
samples at fixed order),24 full signed reset examples through H512,
35 exact rational-power illustrations and9 invalid/missing-input rejections.
Two supplied conversions are stored in full: parent61849410141, child8697573301
at H26 uses3 supplied pairs and180 output rows; parent1008756393712221,
child141856367865781 at H40 uses3 supplied pairs and235 rows. Fixture searches
have cycle detection and caps of10000 ordinary arrows and4096 bits; they
completed. Generation and default replay passed. These finite counts verify
the implementation; the written CRT and exponent arguments supply the
infinite quantifiers.
