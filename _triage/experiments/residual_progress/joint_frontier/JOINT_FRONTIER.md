# Complete joint-source interface and an expanding unfinished frontier

**Status: written proof and bounded executable checks.** This gives a complete
arithmetic interface for the R39 source, then exhausts one previously unresolved
residue class. The resulting positive frontier need not decrease. This is a
scoped failure of that proposed closure, not a universal current construction,
an obstruction to other constructions, or a convergence/divergence claim.

Use the odd-only Syracuse map S, absorbed at1. Write delta1=0 and
div J=(I-P)J. A prefix current of length k from x has divergence
delta_x-delta_(S^k x). We retain signed currents and all positive residuals.
The relevant prior construction is [R39](../even_pair_closure/EVEN_PAIR_CLOSURE.md).

## 1. Complete two-arrow interface

For every positive v=3 modulo4 set

    C(v) = delta_(18v+3) - delta_v.

The following table covers every such v. Here a and e are exact valuations.

| Domain | Lower endpoint z=S²(v) | Upper endpoint y=S²(18v+3) | Upper/lower valuation words |
| --- | --- | --- | --- |
| v=3 mod8 | a=v2((9v+5)/2)>=2; z=(9v+5)/2^(a+1) | 9*2^(a-1)*z-7 | (2,1)/(1,a) |
| v=7 mod8 | z=(9v+5)/4; e=v2(9z-7)>=1 | (9z-7)/2^e | (2,e+1)/(1,1) |

Subtracting the two prefix currents gives exactly

    C(v) = div J + delta_y - delta_z.                         (1)

**Proof.** The upper first arrow always has valuation2 and endpoint
(27v+5)/2. In the first row its next arrow has valuation1 and endpoint
(81v+17)/4. Substitution of9v+5=2^(a+1)z gives the stated y.
In the second row, 9z-7=(81v+17)/4, so the upper second valuation is e+1.
The two lower arrows follow by direct substitution. All displayed endpoints
are positive odd integers. Telescoping gives (1).

In the first row a=2 exactly when v=11 mod16, and then z>v; for v=3 mod16
we have a>=3 and z<v. In the second row z>v. Thus even this complete local
classification does not supply a height-decreasing closed family of C states.

## 2. Exhausting the entire v=3 modulo32 class

For every positive v=3 mod32 define

    t=(3v-1)/8,   h=v2(3t+1)>=2,   u=S(t).

Then t=1 mod4 and the exact prefixes are

    S³(18v+3)=27*2^(h-1)*u-5,     upper word (2,1,2),
    S²(v)=u,                     lower word (1,h+2).         (2)

The lower closing valuation is h+2: S(v)=F(t)=4t+1. Moreover

    u <= (9v+5)/32 <= v/3,                                (3)

with equality in the second inequality only at v=3. The full parameterization
is

    v=(2^(h+3)*u-5)/9,
    h>=2, u positive odd, 2^h*u=4 mod9.                    (4)

Every pair (h,u) in (4) gives a positive v=3 mod32 and its exact valuation h.
Indeed division by9 is integral, and modulo32 gives v=-5/9=3; also
3t+1=2^h*u. Conversely (2) gives (4). Formula (3) follows from h>=2 and
u=(9v+5)/2^(h+3). The upper three arrows give (2) directly.

For any positive odd A,u and m>=4, the following two arrows are exact:

    A*2^m*u-5 --1--> 3*A*2^(m-1)*u-7
               --2--> 9*A*2^(m-3)*u-5.                   (5)

The first numerator has exactly one factor2 and the second exactly two,
since m>=4. The constants -5 and -7 shadow the negative3x+1 cycle; all actual
states in (5) are positive. This does not assert a positive cycle.

Put

    j=floor((h-2)/3),    s=h-1-3j in {1,2,3},
    q=2^s*3^(2j+3)*u-5.

Apply (5) j times after (2). This gives the complete finite block

    S^(3+2j)(18v+3)=q,      S²(v)=u,
    C(v)=div L_v + delta_q-delta_u.                        (6)

Here L_v is the upper prefix current minus the lower two-row prefix current.
Equation (6) keeps the unresolved pair. Exhausting the binary exponent
increases its ternary coefficient; the new pair is generally not C(u).
The lower parameter u alone cannot certify progress of the full signed state.

Every q in (6) satisfies q=22 mod27. When q is a critical canonical state,
it lies in R38's omitted phase: q=1 mod3, v3(q-1)=1, and the ternary unit
of q-1 is1. This identifies an unresolved interface, not a new impossibility
theorem for those targets.

## 3. Explicit expansion with an already absorbed lower source

For each integer r>=0 set

    h=6r+2,   v_r=(2^(6r+5)-5)/9,   u=1.

These are valid parameters in (4). Thus

    S²(v_r)=1,
    18v_r+3=2^(6r+6)-7,
    S^(4r+3)(18v_r+3)=q_r=2*3^(4r+3)-5.                   (7)

The upper word is (2,1,2)(1,2)^(2r), and the lower word is (1,6r+4).
The positive frontier is canonical: q_r=1 mod8. Since q_r=1 mod3, both the
R25 elementary normal form and the R34 decreasing inverse-chain normalizer
leave it unchanged. Its ordinary valuation2 arrow does decrease it to
`S(q_r)=(3^(4r+4)-7)/2`, but that endpoint still has unbounded ratio to
v_r. Further information is needed to absorb it; this note does not
exclude those subsequent ordinary steps.

In particular,

    q_r/v_r ~ (243/16)*(81/64)^r -> infinity.              (8)

Thus the prescribed complete block has no universal linear frontier-height
bound in v, even with its lower source absorbed. This does not exclude another
bridge, a richer rank with intermediate growth, or an unrelated decreasing
ancestor. Each r describes a different finite prefix.

## 4. Genuine complementary d4 roots and a required-ray family

For r>=0 divisible by9, v=v_r satisfies v=3 mod9. Define

    w=16v/3+1,     t0=(16w+1)/3,     x=4t0-1,
    p=(x-1)/2=(32w-1)/3.

Here w=17 mod128 and w=2 mod3. The seed x has a=2, odd t0=3 mod4 and exact
complementary run parameter d=v2(3t0-1)=4. It is the R39 A-entry with child v.
For the modular assertion, 2^54=1 mod81 gives v=3 mod9 when9 divides r.

The smaller half has the complete four-arrow absorption certificate

    p --5--> w --2--> F(v) --3--> S(v) --(h+2)--> 1.       (9)

The upper prefix is

    S³(x)=18w+1,
    S⁴(x)=F(2(18v+3)+1),
    S⁵(x)=F(S(18v+3)),
    S⁶(x)=S²(18v+3).

Combining with (7) gives

    S^(4r+7)(x)=q_r.                                     (10)

Its exact word is (1,2,2,1,3,3,2)(1,2)^(2r).
Subtracting the current in (9) from the prefix in (10) returns an explicit
**unfinished** comparison:

    delta_x-delta_p = div J_r + delta_(q_r).              (11)

Adding the supplied four-row absorption current of p merely leaves the upper
prefix and its positive frontier; it does not complete x's absorption.

There are actual residual sources on a required ray. For every positive
multiple r of27 set

    N_r=12*2^(6r+5),
    x_r=(2^(6r+15)-3365)/81.

These are the same x as above, and

    x_r=3 mod12,       N_r<x_r<9N_r/8,
    p<N_r,            R_(N_r)(x_r)=1.                    (12)

Indeed 2^162=1 mod243 and 2^15-3365=243*121 show3 divides x_r;
x_r=3 mod4 was already established. Also

    x_r/N_r=256/243 - 3365/(81N_r),

which is between1 and9/8 for r>=27. On this interval the retained-graph
residual has weight1 on3 mod12. Thus (12) uses its full actual coefficient.
No claim about the total mass of this sparse family is made.

Finally

    q_r/x_r ~ (2187/16384)*(81/64)^r -> infinity.          (13)

In fact q_r>x_r for r>=9: verify4374*81^9>32768*64^9 and use the increasing
ratio (81/64)^r in81(q_r-x_r)=4374*81^r-32768*64^r+2960.
The required-ray subfamily therefore has a smaller half with a four-arrow
certificate and an unresolved canonical frontier above the original root.
This is a concrete dependency failure for the prescribed joint block, not a
counterexample to Collatz or to the existence of another current.

## 5. Executable interface and evidence

[joint_frontier.py](joint_frontier.py) exports `interface`, `shadow_frontier`,
`expanding_family`, `embedded_family`, and `required_ray_family`. Every
constructor returns its full current and exact residual. It exposes only a
prescribed number of arrows; no absorption search is used.

Run the bounded checker:

```sh
python3 experiments/residual_progress/joint_frontier/check_joint_frontier.py
```

The checker compares the table with8192 exact two-arrow cases, the complete
block with2048 parameters,45 parameterized(h,u) cases, and11 expanding-family
instances. It checks five d4 embeddings and four actual required-ray roots.
The r=27 comparison current and its lower absorption input are stored as
[actual_r27_frontier_current.csv](actual_r27_frontier_current.csv) and
[actual_r27_lower_current.csv](actual_r27_lower_current.csv). Their replay
checks (11), including the positive residual; neither table is labeled as an
absorption certificate for x. The deterministic
[receipt](joint_frontier_audit.json) records clocks, sizes and hashes.

The proof establishes the infinite families. The finite checker only audits
their implementation and selected instances. Full C(v) closure and universal
completion of the remaining complementary roots stay open.
