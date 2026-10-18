# The unique rank excess in formal absorption

**Status: written complete classification of above-seed requests, with a
conditional forward rule on a complete arithmetic domain.** This refines
the R43 absorption bound while keeping the same rank rho. It does not mix
rho with sigma, supply missing currents, or establish universal coverage.

Use the absorbed odd Syracuse map S, the elementary minimum nu, W5 and W9
from [R40](../w9_closure/CRITICAL_NINE_ELIMINATION.md), and
rho(w)=nu(3w). The unchanged formal plan H_s has boundary

    [s] = div H_s + sum_u h_s(u) P(u),    P(u)=[3u]-[u].       (1)

All h_s(u) are signed integers after complete W9 elimination. The
requests in (1) are premises. The existing general bound is
rho(u)<=(9nu(s)+5)/8. Here we characterize exactly when a request can
exceed nu(s), and use the characterization in the original rho order.

## 1. Complete classification of the excess

For a canonical n define the exceptional condition

    n=27 mod48,
    v2(3n-1)=4,
    z=(3n-1)/16, and 3z is noncanonical.                     (2)

**Theorem.** Put n=nu(s). If (2) fails, every request of H_s has rho<=n.
If (2) holds, H_s has exactly one request above n:

    u*=4z+1,  h_s(u*)=+1,  rho(u*)=(9n+5)/8.                (3)

Every other request then has rho<n. In particular, if s is noncanonical,
every request has rho<s even when its minimum is exceptional. At n=1
there are no requests. The bound n outside (2) is an upper bound, not an
assertion that some request always attains n.

### Complete W9 elimination

First take a W9 input v. Its local R40 formulas have one possible
exceptional W5 request u*=4z+1 in the even-depth upper-noncanonical row.
All other local indices are at most

    (27v+13)/32.                                           (4)

For odd depth they are below v/2. For the upper-canonical even case,
(4) is R40's bound (9). In the upper-noncanonical case its lower bound
(9v+11)/12 is at most (4) for every v>=9; the other upper inputs are
smaller still. Thus (4) also applies to every recursive W9 input c.

An ordinary W5 request below v has rho<=3u<3v. Applying R43's already
proved W9 bound to a recursive c gives

    rho <= (27c+5)/8 <= (729v+511)/256 < 3v,                (5)

where the last inequality holds for v>=25. The only smaller W9 input
is v=9. Its exact elimination is P(9) -> P(21)-P(5); the former has
rho31>27 and the latter rho7<27, so it has precisely the stated exception.

The remaining possible large W5 index is the explicitly retained u*.
At depths d=4,6,8 its ranks are respectively

    (27v+5)/8,   (81v+23)/32,   (243v+101)/128.             (6)

Only the first exceeds3v. The latter two are strictly below3v for every
v>=9. At even depths d>=10 the exceptional index itself is below v and
therefore has rho<3v. This proves: in the full W9 plan, an excess over3v
occurs exactly at d4 with 3z noncanonical. Its coefficient remains+1,
since all other contributions have smaller rank. All signs and all
recursive W9 branches have been retained.

### Formal absorption from an arbitrary seed

Normalize to n. For canonical n=1 mod8, the first arrow reaches
(3n+1)/4, so R43 bounds all its requests by(27n+29)/32<n (n>=9).
For a canonical n=2 mod3 outside that row, the prescribed free inverse
reaches(2n-1)/3, giving bound(3n+1)/4<n.

Otherwise n is a critical root. A W5 critical index gives its leading
request with rank n and auxiliary H inputs strictly below n. A W9
critical index can occur only when n=3v with v=9 mod16, equivalently
n=27 mod48. Indeed the alternative index v=(2n+1)/3 in W9 would force
n=5 mod8, contradicting canonicality. The preceding W9 classification
gives (2) and (3). The additional H_v requests have rank at most
(9v+5)/8<3v, so they cannot cancel or add a high request.

For noncanonical s, n<=(s-1)/2. Even the exceptional bound is at most
(9s+1)/16<s for s>1. This completes the theorem. Normalization adds only
its exact current and does not change the request vector.

## 2. Complete original-rho classification on the fifth-exponent family

R51 proved a whole sigma domain. Here the same current is tested in rho.
For every m>=0 set

    w=437+512m,  t=41+48m,  q=3w=32t-1,
    f=(243t-3)/8=3v,  v=415+486m.                         (7)

The full R26 block has exact first parameters a5,d3, ordinary common-tail
clocks(6,1) and quotient clock5 to nu(f). It obeys

    q-f=(13t-5)/8>0.                                    (8)

Let N_w be the normalizer current. The full signed comparison is

    J=D_q-N_w+H_f-H_nu(w).                               (9)

**Complete decision theorem for (9).** Every remaining request strictly
decreases rho if and only if the following failure condition is false:

    m=7 mod16,  j=(m-7)/16,
    z=2147+4374j, and 3z is noncanonical.                 (10)

When (10) holds, the sole request of rank at least q is u*=4z+1 with
coefficient+1. It has rank(9f+5)/8>q. This is an exact classification of
this signed plan, not a claim that failing inputs lack other currents.

**Proof.** By Section1 and f<q, a failure can occur only if f itself is
canonical and exceptional. A noncanonical f has all requests below f.
The condition v=9 mod16 in (7) is m=7 mod8. Write m=7+8l. Then

    v=3817+3888l,  9v-1=16(2147+2187l).

The depth is exactly4 iff l is even, giving m=7+16j and the z in (10).
This proves equivalence to the exceptional condition. At such a point,

    (9f+5)/8-q=(139t+77)/64>0.                           (11)

All other H_f requests have rank<f<q. Also nu(w)<w/4, so every lower
H_nu(w) request is below q. Hence the unique excess cannot cancel,
and the theorem follows including both implications.

### A complete new subdomain of the twelve-rule complement

Every member of

    w=4021+294912k,   k>=0                              (12)

passes (9) and is outside all twelve previous direct predicates.
Here m=7+576k, j=36k, z=2147+157464k, and3z=1 mod8, hence3z is
canonical and (10) fails.

For the old predicates, 3w is nonselected with a5,d3, so every selected
rule and the first-a3/a4 R53 continuation is excluded. Also w=7 mod9,
so3 does not divide w. R45's k4 depth is0, while its k8 depth is1
and its endpoint r=4(8w+1)/3-1 is divisible3; that plan retains the
original request. R50's second depth v3(2r+1) is0. Thus R45, R47 and
R50 do not apply. The R48 endpoint is canonical f=3v with v in W9,
so its old sufficient bound is(9f+5)/8>q by (11), despite the actual
high request being absent. These exclusions exhaust the old twelve
families. No claim is made against later rules or supplied histories.

The former sigma example w44981 remains a failure here: its retained
child96069 has rho144103 above parent134943. The new classification
therefore does not silently make the two rank systems interchangeable.

## 3. Reproduction and exact supply

`exact_bound.py` returns the exceptional input explicitly and checks its
coefficient against the unchanged absorption implementation. It supplies
the complete fifth-family comparison and returns only strict-rho plans
from `one_step`. Missing or malformed supplied currents are rejected by
the existing R43 compiler. No unknown orbit is searched by these APIs.

Run:

```sh
python3 experiments/residual_progress/exact_absorption_bound/check_exact_bound.py
```

The adjacent receipt records bounded whole-seed checks, complete W9
eliminations, the fifth-family iff test, full new-progression samples,
the retained sigma incompatibility, and actual supplied-current conversions.
These finite checks verify the implementations; the universal quantifiers
and complete domain statements rest on the proofs above.

The focused replay checks16384 odd seeds below32768, including342 with
exceptional normalized minima,2048 complete W9 plans and2048 fifth-family
inputs (1983 decreasing,65 unresolved). It checks69 members of the new
progression through index2^128, the retained44981 failure and seven invalid
or missing-supply rejections. Three actual substitutions at4021,298933
and593845 store complete30-,105- and119-row outputs and all12 distinct
supplied pair currents. Fixture discovery is capped at10000 steps and1024
bits with cycle detection. Default replay reproduces the receipt and its
module/checker source hashes; these counts are finite evidence only.
