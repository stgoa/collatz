# No finite affine-valuation rank for the two fixed phases

**Status: written scoped obstruction, exact conditional-current construction,
and bounded executable audit.** No potential in the class defined in Section1
can rank the named R67 dependencies and all the accepted R44 comparisons below.
The obstruction permits finitely many arbitrary rational valuation centres,
arbitrary real valuation weights, and nonnegative phase-dependent height
powers. It supplies no universal pair current and changes no dispatcher.
Collatz convergence remains open. No novelty or formal-verification claim is
made.

Dependencies are the [R67 mixed block](../mixed_rank_recursion/MIXED_GROWING_BLOCK.md),
[R44 returning interface](../returning_phase/RETURNING_FORWARD_INTERFACE.md),
[R43 formal absorption bound](../critical_rank/CRITICAL_IMAGE_RANK.md), and
[R69 two-centre obstruction](../arithmetic_progress/VALUATION_DEBT.md).
All source coefficients are signed integers. Use the ordinary odd Syracuse
map S, absorbed at1, and write T=nu S for the separately clocked canonical
quotient. Pair currents have source P(w)=[3w]-[w], with [1]=0.

## 1. The precise potential class and requirements

Let W5 be the positive integers congruent to5 modulo8. Partition it into the
same **two fixed phases** used in R69:

- E consists of w=3 modulo9 with selected3w;
- W is its complement in W5.

For p in{W,E}, choose constants C_p>0 and a positive increasing affine
height h_p(x)=c_p x+d_p, with c_p>0 and h_p(x)>0 on that phase. Choose a
real exponent alpha_p>=0. Independently in each phase choose a finite list
of rational affine forms f_(p,i)(x)=a_(p,i)x+b_(p,i), and arbitrary real
weights beta_(p,i). Every retained form must be nonzero at every input in
its phase, so all values below are finite. Nonzero constant forms are
allowed and can be absorbed into C_p. For rational values use the ordinary
extension v2(n/d)=v2(n)-v2(d). Define

    Phi_p(x)=C_p h_p(x)^alpha_p
                    2^(sum_i beta_(p,i) v2(f_(p,i)(x))).       (1)

Repeated or proportional forms are allowed; their weights add at the same
centre. A nonconstant form's centre is its rational zero. The theorem
allows negative valuation weights and different finite lists in the two
phases. It does not assume that (1) is integer-valued or well-founded.

**Theorem.** No choice in(1) has all three properties:

1. Nonincrease along both actual leading dependency edges of every guarded
   R67 mixed block.
2. Strict decrease from the first to the last W state of each such block.
3. Nonincrease from the parent to the retained positive leading request in
   every R44 comparison constructed in Section3.

Thus (1) cannot be a strict global dependency rank for a rule collection
containing these comparisons. Only positive coefficient+1 dependencies are
needed for the contradiction. Requiring all signed premises to decrease
would be stronger, and does not avoid it. This is an obstruction to the
specified rank class and rule requirements, not to all currents or to
choosing a different set of rules.

## 2. What the mixed block forces on arbitrary finite lists

Put

    D=7153, B_W=311195, B_E=656187,
    theta_W=-B_W/D, theta_E=-B_E/D,
    L_W(x)=Dx+B_W, L_E(x)=Dx+B_E.                         (2)

R67's guard is w=40529845 modulo2^26, equivalently H=v2(L_W(w))>=26.
It gives two actually accepted leading requests of coefficient+1:

    w in W -> u=(2187w+1209)/1024 in E
           -> v=(243u+17)/512 in W.                      (3)

Their natural forms obey

    L_E(u)=(3^7/2^10)L_W(w),
    L_W(v)=(3^5/2^9)L_E(u).                              (4)

Consequently u tends to theta_E in the binary metric when w tends to
theta_W; v again tends to theta_W. The exact natural orders are H,H-10,H-19.
The completed block grows in ordinary height:

    v=(3^12 w+311195)/2^19>w.                            (5)

For each phase let b_p be the sum of the weights in(1) whose centres equal
theta_p; an absent centre has sum zero. Every form centred elsewhere has
eventually constant order as the phase input approaches theta_p. Indeed,

    f(x)=f(theta_p)+a(x-theta_p),

and once the second summand has strictly larger order, the first determines
the order. A form centred at theta_p has order v2(x-theta_p)+v2(a).
There are only finitely many forms, so one precision threshold works for
all of them, including the orders H-10 and H-19 in(4).

First fix an exact H above this threshold. Its full positive progression
is w=(2^H-B_W)D^(-1) modulo2^(H+1). Along that progression let w grow without
bound. Every valuation factor on both edges is fixed, whereas the affine
heights grow linearly. Nonincrease on the first edge forces alpha_E<=alpha_W;
on the second it forces alpha_W<=alpha_E. Hence

    alpha_W=alpha_E=alpha>=0.                            (6)

Now let exact H tend to infinity. Each exact-order progression is nonempty;
its positive inputs satisfy w>=(2^H-B_W)/D and therefore tend to infinity.
With the common exponent(6), the affine-height ratios on either edge tend
to fixed positive constants. The valuation ratios have growing exponents
(b_E-b_W)H and(b_W-b_E)H, respectively. Nonincrease on both edges forces

    b_W=b_E=b.                                          (7)

Finally compare the W endpoints of a sufficiently deep block. Every
off-centre order is exactly the same at w and v; every theta_W-centred
form loses exactly19 order units. The potential ratio is therefore

    Phi_W(v)/Phi_W(w)
      = (h_W(v)/h_W(w))^alpha 2^(-19b).                 (8)

Since h_W is increasing, (5) and alpha>=0 imply that b<=0 makes(8) at
least1. Strict block decrease requires

    b>0.                                               (9)

This argument neither assumes that the two old forms are the only centres
nor overlooks bounded changes at other centres. Those changes have become
exact constants before applying the argument. The conclusion concerns net
weight after combining all forms at a centre.

## 3. Complete balanced returning-ray families

Fix any integer L>=1 with L=1 modulo3 and set p=4^L. Let a be the least
integer a>=3 for which

    lambda=6p(2/3)^a<=4.                               (10)

Already at a3 the value exceeds4, so a>3 and minimality gives
8/3<lambda<=4. For a positive odd input u define

    r=F^L(3u)=3pu+(p-1)/3,
    t=(2r+1)/3^(a-1),
    w=g_L(u)=(2^a t-1)/3.                              (11)

The returning conditions are enforced before asserting integrality. Put

    d_L=(2p+1)/9,
    tau=10*2^(-a) modulo27.

The integer d_L exists because L=1 modulo3 gives p=4 modulo9. Impose

    2p u+d_L = 3^(a-2) tau modulo3^(a+1),              (12)
    D u+B_W = 2^H modulo2^(H+1),   H>=26.             (13)

The coefficient2p is a ternary unit. Thus(12) is one complete residue
class modulo3^(a+1), and(13) is one exact-order binary class. CRT gives a
complete infinite positive progression for each L,H, of period
3^(a+1)2^(H+1). Its least residue is positive and odd. The module returns
both residues and that whole progression; a cap is not part of this family.

Since 2r+1=3(2p u+d_L), condition(12) proves

    v3(2r+1)=a-1,  t=tau modulo27,
    2^a t=10 modulo27.                                (14)

The number r=F^L(3u) is5 modulo8, so t is odd and t=3^a modulo4. Therefore
w is a positive W5 integer, w=3 modulo9, and3w is selected with exact
exponent a. It is a valid R44 returning input. Meanwhile(13) places u
in the R67 W phase, with canonical3u and rho(u)=3u.

The parent is the affine function

    w=lambda u+kappa,
    kappa=lambda/9-1/3+(2/3)^a/3.                      (15)

Here -1/27<kappa<1. For positive integer u, (10) and(15) give

    2u<w<=4u,
    q=rho(w)=(3w-1)/2>3u.                             (16)

The upper inequality uses integrality: w<4u+1. No unmentioned
large-size threshold is needed.

### Full current and the unique highest request

Let z=nu(w), let N_s have source[s]-[nu(s)], and write the unchanged formal
absorption plan as div H_s=[s]-sum_x A_s(x)P(x). Along R44's ordinary word
1^(a-2),2 from q to r let G be the path current. Then

    J=N_(3w)+G-N_w+H_r-H_z,
    div J=P(w)-sum_x (A_r(x)-A_z(x))P(x).              (17)

The sibling normalizer sends r to canonical3u. Hence, with exact integer
multiplicities,

    A_r={u:1}+A_u,
    final requests={u:1}+A_u-A_z.                     (18)

Every request of H_u has rho at most(9u+5)/8<3u. Since w is W5,
z<=(w-1)/4, and every request of H_z has rank at most

    (9z+5)/8 <=(9w+11)/32 <=(36u+11)/32<3u.           (19)

Thus P(u) is the unique highest request, with coefficient+1, and cannot
cancel. All other positive and negative requests remain explicit. By(16)
the entire plan is rho-descending, so these are already valid R44 rules,
not merely hypothetical added edges. Exact currents for every remaining
signed input produce a current with source P(w); they are still premises.

The ordinary word from q to r has length a-1. For L>=1, S(F^L(3u))=S(3u),
so the normalized comparison has ordinary clocks(a,1):

    S^a(q)=S(3u),    T^(a-1)(q)=3u.                  (20)

Selected halving also gives S^a(3w)=S^a(q), so the same ordinary(a,1)
identity holds between3w and3u. The quotient statement in(20) starts atq.
One must not call a-1 an ordinary path length to the normalized endpoint.

## 4. Infinitely many necessary parent centres

Let gamma_L=g_L(theta_W). Exact substitution gives

    gamma_L =
      [2^a(7153-5587204*4^L)-7153*3^a]/[7153*3^(a+1)]. (21)

All these rationals have odd denominator. For each fixed L, as H grows
in(12)–(13), u approaches theta_W and w approaches gamma_L. The primitive
integer form at gamma_L has exact order

    v2(den(gamma_L)w-num(gamma_L))=H+a+2L+1.           (22)

Indeed g_L(u)-g_L(theta_W)=lambda(u-theta_W), and lambda has binary order
a+2L+1. Both reduced denominators are odd.

The subsequence L=4 modulo9 gives a particularly exact distinction.
Now p=13 modulo27, so d_L=0 modulo3. Put

    K_L=7153d_L-2p*311195=2 modulo3.

Formula(21) becomes

    gamma_L=[3*2^a K_L-7153*3^(a-1)]/[7153*3^a].      (23)

Because a>3, its numerator has exact ternary order1 and its denominator
has order a. The reduced denominator therefore has **exact order a-1**.
Minimality in(10) makes a strictly increase with L, and a>=3L+2. Thus this
subsequence contains infinitely many distinct parent centres.

For completeness, every L=1 modulo3 with L>=13 also has an elementary
lower bound, without an exponential-Diophantine estimate. Put
T_L=7153-5587204*4^L. Then

    |T_L|<3^(2L+15),  v3(T_L)<=2L+14<a,
    v3(den(gamma_L))=a+1-v3(T_L)>=L-11.              (24)

The bound a>=3L+2 follows from
(3/2)^a>=(3/2)4^L>(3/2)^(3L+1).
The exact balanced subsequence(23) suffices for the theorem.

## 5. Contradiction for any finite list

Suppose(1) satisfies the three requirements of Section1. Section2 gives
a common height exponent alpha and a strictly positive net child-centre
weight b at theta_W.

The E phase has only finitely many centres. By(23), choose a fixed
L=4 modulo9 for which gamma_L is absent from that finite list. Now let
exact H tend to infinity along the complete CRT families(12)–(13), using
for example their least positive representatives. Their u,w grow without
bound, w/u tends to the fixed positive lambda, and every E valuation order
becomes constant because no E form vanishes at gamma_L. Every W order
away from theta_W also becomes constant. The net valuation factor in the
child/parent ratio is therefore a positive constant times2^(bH).

The common height exponent contributes a factor tending to
(c_W/(c_E lambda))^alpha, strictly positive and finite. Thus

    Phi_W(u)/Phi_E(w) tends to infinity.              (25)

This violates nonincrease on the actual retained coefficient+1 child in
(18). Finite values and all source signs are preserved throughout. This
proves the theorem for arbitrary real weights, not just the rational
examples in the checker. The additive logarithmic form of(1) is excluded
by the same argument. No search or asymptotic integer-density estimate is
used in the proof. □

## 6. Scope and reproducibility

The theorem permits different finite affine valuation lists in the two
fixed phases. It does **not** cover arbitrary additional phase partitions,
nonlinear valuation forms, negative height exponents, infinitely many
centres, nonmonomial functions, history-dependent or amortized signed
frontier potentials, or omitting one of the named rule families. It does
not assert that any such alternative succeeds. The contradiction concerns
individual dependency ranks; no conservation law for a weighted sum of
signed requests is assumed.

Run from the repository root:

    python3 experiments/residual_progress/finite_centres/check_finite_centres.py

The default run recomputes the stored receipt. Its bounded audit includes:

- 192 exact CRT cases: L=1,4,...,70, H=26,27,64,256, and indices0 or2^32;
- 48 complete signed R44 plans at L=1,4,...,22, H=26,64,128, and indices0/1,
  with independently computed divergence and both clocks;
- 24 distinct balanced parent poles through L211, with exact reduced
  ternary denominator orders;
- three finite-list pole examples at H512,768,1024, and four arithmetic
  mixed-block stabilization cases that separately vary height and order;
- two full supplied-current conversions: parent189106655349, using three
  supplied pairs and158 output rows, and parent3688333493785941, using
  thirteen supplied pairs and211 output rows;
- twelve rejection checks, including missing and incorrect signed inputs
  and a vanishing valuation form.

The receipt stores both supplied-current demonstrations in full. Their
ordinary absorption paths are capped at10000 arrows and4096 bits with
cycle detection; these designated finite examples do not prove universal
supply. Source hashes cover41 reachable local mathematical modules,
including dynamic imports absent from `sys.modules`, using portable
repository-relative paths. The written argument establishes the universal
quantifiers; finite checks audit implementation. The constructor is
[finite_centres.py](finite_centres.py), the replay is
[check_finite_centres.py](check_finite_centres.py), and the evidence is
[finite_centres_audit.json](finite_centres_audit.json).
