# The prescribed ternary child requires unbounded clocks

**Status: written scoped proof with an exact finite rational-word certificate.**
This does not exclude a merger at input-dependent, unbounded clocks. It does
not exclude a different child family, several signed children, or a general
finite current. It supplies no missing Collatz current.

The proposed child in [the later-target template](../deeper_window/NEXT_TARGET.md)
is `Q(floor(ell/3))`, where

    Q(ell)=Q0+QP*ell,
    Q0=70506316836123, QP=3*2^45.

Throughout, S is the ordinary odd-only Syracuse map, absorbed at1. Both clocks
in a common-tail comparison are ordinary clocks. No quotient-clock conversion
is used here.

## 1. Complete quantifiers

For each digit `c in {0,1,2}`, each clock cap `K>=0`, and each prescribed return
count `R>=0`, there is a positive binary progression of integers j such that:

1. `ell=c+3j>j>0`, so `Q(j)<Q(ell)`;
2. the original coupled source at ell has at least R guarded Phi returns;
3. for every pair of clocks `0<=a,b<=K`,

       S^a(Q(c+3j)) != S^b(Q(j)).                       (1)

The progression is infinite. It is constructed from finite rational arithmetic
for any prescribed c,K,R. Thus a comparison supplying this particular child
for every input cannot have a uniform bound on its two ordinary clocks, even
within any one digit class and after restricting to arbitrarily many initial
Phi returns. A finite catalogue of fixed word pairs, with any finite binary
refinement or choice policy, is therefore insufficient for this child rule.

This conclusion concerns the prescribed merger. The conditional signed-current
identity in NEXT_TARGET.md remains correct if the merger is supplied. The result
does not obstruct input-dependent words of unbounded length or a terminating
recursion that generates such words.

## 2. One common binary center

Write

    D=7153, B=299947, v*=-B/D,
    q*=(2^27*v*-213949807)/3^17
       =-515908491727/11404192419,
    ell*=(q*-Q0)/QP=-22852975802/34212577257.

The denominators are odd. In particular ell* is a binary-integral rational,
`v2(ell*)=1`, and `v2(q*-Q0)=46`. For each digit put

    j*_c=(ell*-c)/3,
    p*_c=Q0+QP*j*_c.

All j*_c are negative, binary-integral rationals. Their parent center is always
`Q(c+3j*_c)=q*`. The child centers are

|c|p*_c|
|--|--|
|0|1608135207907736055411347 / 34212577257|
|1|404387159579536788517523 / 34212577257|
|2|−799360888748662478376301 / 34212577257|

The first two are positive. Their rational Syracuse orbits stay positive:
for a positive odd rational with odd denominator, `3x+1>0`, and division by
its exact positive power of2 preserves positivity and oddness.

Rational Syracuse is used only as exact arithmetic on these auxiliary centers.
It is not being substituted for the positive integer dynamics. For an odd
rational x with odd denominator and `3x+1!=0`, define

    S_hat(x)=(3x+1)/2^v2(3x+1).

Every auxiliary state used below satisfies these conditions. A finite word is
locally constant in the binary topology, which transfers it to actual positive
integer sources in Section4.

## 3. The upper shadow and the third child are disjoint

Starting from q*, an exact 18-arrow prefix reaches

    6v*+1=-1792529/7153.

The subsequent exact word

    (1,1,1,1,3,1,4,1,2,1,1,2)

returns to the same rational state. Its length is12 and its cost is19. Every
state of the initial prefix and this cycle is negative. These are precisely
the original prefix and guarded return formulas, evaluated at the fixed
center; they can also be checked directly using rational arithmetic.

For c=2, the exact112-arrow word stored in
`check_child_catalogue_scope.py` and the audit receipt takes p*_2 to

    S_hat^112(p*_2)=1663/7153>0.                         (2)

All112 earlier states of this path are negative. None is equal to any state of
the upper18-prefix and12-cycle. The checker verifies every exact valuation,
the endpoint, all signs, and every equality comparison. The receipt retains
all113 child states and the complete112-word; its largest numerator has only
80 bits. This is a finite certificate, not an orbit extrapolation. After (2),
positivity supplies the infinite continuation argument without requiring a
cycle classification or any convergence assertion.

Consequently, for every c and every pair of finite nonnegative clocks a,b,

    S_hat^a(q*) != S_hat^b(p*_c).                       (3)

For c=0,1 this is simply the sign difference. For c=2 the finite negative
prefix is checked against the complete upper prefix and cycle; every later
child state is positive. The extra repeated upper endpoint is checked as well.

## 4. From disjoint shadows to a whole positive progression

Fix c,K. Compute the first K exact rational valuations at q* and p*_c, and
let E_max be the larger of their two total costs. The finite words exist:
the upper shadow has the stated negative cycle; both positive child shadows
never have `3x+1=0`; the third child reaches positivity by the finite certificate.

A word of total cost E occupies exactly one source cylinder modulo `2^(E+1)`.
The extra bit is retained. If

    j=j*_c (mod 2^N),  N+45>=E_max+1,                  (4)

both actual positive sources have their respective first K shadow valuations,
because the source slopes are `3QP` and `QP`, each of exact binary order45.
Absorption at1 introduces no discrepancy: the odd-only formula also fixes1
with valuation2.

For each `a,b<=K`, the two endpoints on (4) are affine functions of j:

    f_a(j)=[3^a*(Q0+QP*c+3QP*j)+C_a]/2^A_a,
    g_b(j)=[3^b*(Q0+QP*j)+C'_b]/2^B_b.                (5)

They cannot be identical affine functions. Indeed, evaluating (5) at j*_c
would contradict (3). Their equality therefore has either no solution or
one rational solution. Retain just their finitely many nonnegative integer
roots, forming a set F.

No member t of F equals j*_c, since j*_c<0. Increase N, if necessary, so

    N>v2(t-j*_c) for every t in F.                    (6)

Every valuation in (6) is finite. Thus the complete binary cylinder (4)
contains none of the roots. All positive j in it satisfy (1). This excludes
all clock pairs simultaneously, rather than only a sampled set of j.

The implementation follows (4)--(6) literally. It checks that no affine
equation vanishes identically, solves every remaining equation exactly, and
rejects every nonnegative integer root from the returned cylinder.

## 5. Compatibility with any prescribed initial return count

The original source coordinate is

    v0=67839005952677+2^18*3^18*ell.

At ell*, its value is v* and `Dv*+B=0`. Hence on `ell=c+3j`,

    Dv0+B = D*2^18*3^19*(j-j*_c).                   (7)

Taking N at least19R in addition to (4)--(6) gives

    v2(Dv0+B)>=19R+18.

By the complete guarded-return criterion, every such positive source has at
least R Phi returns. Increasing the binary precision does not remove the
infinite positive tail of the progression. This proves all quantifiers in
Section1, including independent choices of K and R.

The conclusion does not say that any fixed positive source fails forever.
The obstructing positive sources may change when K or R increases. It also
does not say that all sources in one exact return-count cell fail: the
constructed cylinder has a lower bound on its return count.

## 6. An independent argument for the c=2 digit

Without the112-word certificate, a weaker version of the c=2 conclusion
(without independently prescribing many Phi returns) follows at j*=-1.
There both rational sources equal the same negative integer `Q0-QP`.
All finite ordinary words are well-defined there. On a sufficiently small
binary cylinder, both sources follow prefixes of this single infinite word.

If an affine endpoint equation were identical, its slopes would require

    3^(a+1)*2^B = 3^b*2^A,

so `b=a+1` and `A=B`. The child word of length a+1 extends the identical
length-a prefix by one positive valuation, which forces `B>A`, a contradiction.
The same finite-root exclusion then works. This provides an independent
structural check of the prescribed-child limitation. The main theorem uses
the stronger common Phi center for all three digits.

## 7. Reproduction and limits

Run

    python3 experiments/residual_progress/child_history_scope/check_child_catalogue_scope.py

The checker constructs complete cylinders for caps
`0,1,2,4,8,16,32,64,128` in all three digits, and separately combines cap16
with return lower bounds `1,4,16,128`. It independently replays four positive
integer pairs from every cylinder and checks all their bounded-clock endpoint
intersections. These positive samples check the implementation; the full
progression guarantee comes from the finite affine-root certificate, not from
the samples. The receipt also pins the proof and checker source hashes.

Regenerate the receipt only after an intended source change using `--write`.
No repository dispatcher is extended. No terminal pair inputs are supplied.
No general signed-current obstruction or Collatz nonconvergence is inferred.
