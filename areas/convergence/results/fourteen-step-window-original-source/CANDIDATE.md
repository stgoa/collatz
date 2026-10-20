# Candidate finite-boundary reduction beyond the R91 precision horizon

**Historical research candidate, 2026-10-18. Resolved by R92.**
The [completed proof and classification](DEEPER_WINDOW.md) independently
audits this reduction, adds a selective congruence, classifies every required
boundary origin and enumerates every legal suffix. The sole origin p<=Q in
the full extended window is Q itself. The original draft below is preserved
as a dated research handoff; its statements about unfinished work describe
that earlier state, not the current result.

**Original draft status:** unpromoted and awaiting independent review.
This draft is outside the frozen R90/R91 verification scope. It changes no
accepted result, implementation or receipt. The larger finite rational basin
below has **not been enumerated**. In particular, this is not a conclusion
that the next history window succeeds or fails, and not a terminating
universal certificate algorithm.

Dependencies are the frozen R90/R91 statements in:

- [R90: complete Phi exits](../phi_exit_control/PHI_EXIT_CONTROL.md)
- [R91: shadow precision barrier](../shadow_precision/SHADOW_PRECISION.md)

The purpose is to reduce one precisely bounded extension of their history
question, uniformly in the number of growing returns, to finite boundary
origins and finite suffix words. This note uses only exact arithmetic and the
already proved R91 score theorem. No new large search was performed.

## 1. Original family and the precise window

Use the canonical quotient T and the complete inverse branches of R25. Set

    A=3^12=531441, M=2^19=524288, D=A-M=7153,
    B=299947, gamma=A/M,
    Phi(v)=(Av+B)/M, L(v)=Dv+B,
    c0=-3B/D=-899841/7153, t0=899841-D=892688.

The coupled original source family is

    v0=67839005952677+2^18*3^18*ell,
    Q =70506316836123+3*2^45*ell,       ell>=0,
    n0=3v0.

Write

    kappa=2^27/3^18,
    c=213949807/3^17>1.

Then exactly

    Q=kappa*n0-c,       n0>2Q,       Q+1<kappa*n0.          (1)

Suppose at least r>=0 guarded returns are available, equivalently

    v2(L(v0))>=19r+18.

Put v_r=Phi^r(v0), n_r=3v_r, and h=12r+5. R90/R91 give

    n_r-c0=gamma^r(n0-c0),
    v3(n_r-c0)=h,
    T^(18+12r)(Q)=n_r,
    S^(23+12r)(Q)=S^5(n_r).                              (2)

The last two clocks are different statements. The ordinary prefix of length
18+12r ends at 6v_r+1, not at n_r.

R91 excludes every positive canonical p<=Q with T^d(p)=n_r for d<=h.
Here consider a possible such origin in the next window

    h<d<=h+14=12r+19.                                    (3)

Equality p=Q is deliberately included in all necessary bounds. Its known
history has d=h+13 and does not supply a strict original-rank descent.

## 2. Uniform actual-rank bounds, including all intercepts

Every complete quotient inverse branch x -> alpha*x+beta satisfies

    alpha>=2/3, beta>=-1/3, alpha-beta>=1.

For an inverse word of length j and slope lambda_j these imply

    x_j>=lambda_j*[n_r+1-(3/2)^j].                       (4)

This bound uses the full affine intercept. It applies to every actual
inverse word, including beyond the rational-shadow precision horizon.

The exact binary and ternary source orders give

    L(v0)>=81*2^(19r+18),
    n0>=(243*2^(19r+18)-3B)/D
       >=C*2^(7r),
    C=(243*2^18-3B)/D=62801151/7153.                     (5)

Let x_h be the state after the first h inverse steps of a history satisfying
(3), lambda_h its slope, and

    mu_h=lambda_h*gamma^r,
    E_r=(243/32)*2^(7r), K=(3/2)^14.

The remaining t=d-h<=14 steps satisfy

    p+1>=(2/3)^t*(x_h+1),
    x_h+1<=K*(Q+1).

Also, (2) and (4) show

    x_h>=mu_h*[n0-c0+gamma^(-r)(c0+1)-E_r]
       >=mu_h*(n0+1-E_r).

The bracket is positive by (5). Consequently

    mu_h<K*(Q+1)/(n0+1-E_r)
        <(8192/81)*n0/(n0+1-E_r)<102.                    (6)

Here K*kappa=8192/81 exactly. The final inequality holds for every r and
every admitted ell, not just asymptotically: its sufficient arithmetic check
is

    (70/81)*C-102*(243/32)
       =21052290557/3090096>0.

This is stronger than (70/81)*n0>102*(E_r-1), which is the exact inequality
needed in (6).

There is also a useful uniform bound for the slope of the **whole** history.
Writing mu_total=lambda_d*gamma^r, (3)-(4) give

    p>=mu_total*[n0+1-(3/2)^19*2^(7r)].

Its bracket exceeds 2Q. Indeed (1) and (5) reduce this to the exact positive
constant

    (1-2*kappa)*C-(3/2)^19
      =232269104057100257855/484305580032786432>0.

It follows that

    mu_total<1/2.                                       (7)

No slope-only extrapolation or omission of a small-parameter exception is
being used in (6)-(7).

## 3. Finite rational boundary universe

The first h steps share a legal rational inverse word from c0, because the
actual-shadow difference has ternary order h. Let its boundary shadow be
-u/D, and write t_j=u_j-D>0 along its prefixes. R91 gives

    lambda_j*gamma^k(j)>=1,
    k(j)=max(0,ceil((j-5)/12)).

For each inverse edge define delta_j=alpha_j-beta_j-1. Then

    t_j=alpha_j*t_(j-1)+D*delta_j,
    0<=delta_j<alpha_j.

Expanding this recurrence, bounding 1/lambda_i by gamma^k(i), and using
that each positive k occurs at twelve prefix depths (k=0 occurs only six
times), gives

    t_h<mu_h*[t0+12D*gamma/(gamma-1)]
       =mu_h*(t0+12A).

Combining with (6), every candidate boundary shadow satisfies

    D<u<D+102*(t0+12A)=741545113,
    u odd, gcd(u,D)=1, and -u/D canonical.                (8)

Thus the largest possible odd numerator is 741545111. This is a bound on
the boundary origin only. Its deterministic signed forward orbit may visit
much larger numerators; imposing (8) on intermediate states would invalidate
completeness.

**The basin in (8) has not been classified.** R91 classified a smaller
universe for another threshold. Its old table cannot simply be reused as an
exhaustive table here. A finite number of starting origins does not by itself
prove that every attempted forward classification terminates. Exact paths to
known states, invariant-interval exits, or complete other cycles are needed;
any caps or unresolved orbits remain proof obligations.

## 4. Repeated cycles compress to seven possible boundary costs

Suppose a candidate in (8) is actually in the c0 basin. Let d0 be its first
forward hitting time of c0, and E0 its total binary exponent, so its first-hit
inverse tail W0 has slope 2^E0/3^d0. The deterministic signed c0 cycle has
length 12 and exponent sum 19. A boundary inverse word of length h therefore
has

    h=d0+12j, j>=0.

As h=12r+5, necessarily

    d0=12k0+5, k0>=0,
    j=r-k0, r>=k0.                                      (9)

The word consists of r-k0 complete inverse c0 cycles, then its one fixed
first-hit tail W0. This follows from determinism of the forward quotient;
there is no unlisted alternative path from a given rational origin.

Put m=E0-19k0. The boundary score is then

    mu_h=(2^E0/3^d0)*gamma^k0=2^m/3^5.

R91 and (6) show 1<=2^m/243<102, hence exactly the necessary list

    m in {8,9,10,11,12,13,14}.                           (10)

This is a list of possible costs, not a statement that every value is
realized by a relevant basin tail.

On an actual source, undoing r-k0 cycles first reaches n_k0. Applying W0
then gives the boundary affine formula

    x(ell)=mu_h*(n0(ell)-c0)-u/D.

In particular it is independent of r, once r>=k0, and its ell coefficient is

    x(ell)=x(0)+2^(m+18)*3^14*ell.                       (11)

The affine intercept is integral: one admissible binary-guard member exists
for every r>=k0, the inverse word is legal there, and the coefficient in
(11) is an integer. This also proves integrality at every integral ell.
Positivity and the actual required guard remain explicit conditions; no
claim about arbitrary unguarded seeds is needed.

Since the coefficient is divisible by 3^14, the next at most fourteen
ternary branch decisions of any chosen inverse suffix are independent of
ell and of r. At the j-th suffix step the remaining difference still has
ternary order at least 14-j+1. Consequently the proposed reduction does not
generate an r-dependent explosion of ternary states.

## 5. The remaining suffix alphabet is finite too

Let the suffix have t<=14 arrows and total binary exponent E_s. Its slope is

    lambda_suffix=2^E_s/3^t.

The boundary prefix has mu_h>=1, whereas (7) gives

    mu_h*lambda_suffix<1/2.

Therefore every candidate suffix necessarily satisfies

    2^E_s/3^t<1/2,       E_s<=21.                        (12)

The last bound follows from t<=14 and
2^21<3^14/2<2^22. Every quotient inverse arrow has a positive integral binary
exponent. A ray at index L has exponent e_base+6L, with e_base>=2, so (12)
also forces every ray index to be at most 3.

Thus, after a complete basin table, only finitely many suffix words need to
be examined: t<=14, E_s<=21, both complete inverse rays and the point branch
where legal. The binary exponent is a slope/normalizer cost; it must not be
silently presented as an ordinary Syracuse step count.

For each legal suffix the resulting origin is an exact affine function of
ell. Its coefficient divided by the original Q coefficient is

    2^(m+E_s-27)*3^(13-t).                              (13)

This ratio alone does not decide p<=Q. Positivity, the full affine
intercept, strict p<Q versus the self-history p=Q, and the binary guard must
all be retained. The known Q history occurs at t=13 with m+E_s=27; it is an
essential self-return control, not a new source of supply.

The bound (12) is derived from actual p<=Q, so it does not lose finite
small-ell successes with affine slope greater than one. Such cases would be
checked by their complete affine inequality, not discarded by slope pruning.

## 6. Exact scope and remaining work

The written reduction establishes the following conditional finite
classification interface:

1. Any canonical p<=Q reaching n_r within h+14 either contradicts R91 at
   depth<=h or has a boundary origin in (8).
2. Every relevant first-hit boundary tail has (9)-(10), independent of r
   except for the requirement r>=k0.
3. Every relevant suffix belongs to the finite alphabet (12), with fixed
   ternary decisions and exact affine output (13).
4. Testing complete affine inequalities and source guards on that finite
   template list would classify this entire window for all r and ell.

Remaining proof/certificate obligations before promotion are:

- Classify every relevant canonical numerator in (8), or supply a different
  exhaustive reduction. Intermediate excursions need checked arithmetic and
  explicit cap handling. A larger scan that leaves any unknown basin state
  is not a certificate.
- Independently verify each first-hit path, its d0/E0, both all-ray formulas,
  the seven cost possibilities, and every retained suffix.
- Preserve strict original-Q inequalities and the self-return at Q. If a
  smaller origin is found, construct its full signed comparison and use
  only actually supplied smaller input currents.
- Distinguish a finite-window conclusion from all-depth history supply.
  Histories longer than h+14, different future targets, and other signed
  comparisons remain outside this reduction.

Only the small exact constant checks in Sections2 and5 were executed for
this scratch handoff. They can be reproduced with Python's `Fraction`:

    from fractions import Fraction as F
    D,B=7153,299947
    C=F(243*2**18-3*B,D)
    kappa=F(2**27,3**18)
    assert F(70,81)*C-102*F(243,32)>0
    assert (1-2*kappa)*C-F(3,2)**19>0
    assert D+102*(892688+12*3**12)==741545113
    assert 2**21<F(3**14,2)<2**22
    assert [m for m in range(-20,30) if 1<=F(2)**m/243<102]==list(range(8,15))

No new basin search, dispatcher change, terminal-current construction, or
Collatz conclusion is claimed.
