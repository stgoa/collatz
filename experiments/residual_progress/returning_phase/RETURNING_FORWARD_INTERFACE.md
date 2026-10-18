# A forward interface for the complete returning phase

**Status: written conditional reduction and finite certificates.** The interface
below is defined on the entire returning row of R41. Two complete subdomains,
and nonempty families with arbitrarily long initial runs, have strictly
decreasing critical-image rank. The other inputs remain explicit obligations.
No universal current or convergence theorem is supplied.

Use the odd-only Syracuse map `S`, killed atoms `[1]=0`, and
`P(w)=[3w]-[w]`. Let `nu` be the elementary minimum from R25 and
`rho(w)=nu(3w)` for a critical pair. Let `W5={w>0:w=5 mod8}`.
An elementary current `N_x` has divergence `[x]-[nu(x)]`.
All currents and requests below are signed integer objects.

Dependencies are the [elementary normal form](../bridge_normal_form/BRIDGE_NORMAL_FORM.md),
[R37 formal absorption](../tripling_equivalence/TRIPLING_EQUIVALENCE.md),
[R40 W9 elimination](../w9_closure/CRITICAL_NINE_ELIMINATION.md),
[R41 returning phase](../critical_inverse/CRITICAL_INVERSE.md), and
[critical-image rank bound](../critical_rank/CRITICAL_IMAGE_RANK.md).

## 1. Exact whole-domain parameters and two undo loops

The domain is exactly

```
E_return={w in W5: w=3 mod9 and 3w is selected}.
```

Here selected means `x=2^a t-1`, with `t` odd and `t=3^a mod4`.
Every member, and conversely every positive parameter choice below, has

```
3w=2^a t-1,   a>=3,
t=3^a mod4,   2^a t=10 mod27.                         (1)
q=rho(w)=(3w-1)/2=2^(a-1)t-1,
r=(3^(a-1)t-1)/2=4 mod9.
```

The binary congruence makes `w=5 mod8` and selected `3w`; the ternary
congruence is precisely `w=3 mod9`. Both fix exact valuations, including
the binary phase beyond the divisibility bit. The ordinary path from `q`
to `r` has the exact valuation word

```
1^(a-2),2,     length a-1.                             (2)
```

For `0<=j<=a-3` its intermediate values are
`q_j=3^j 2^(a-1-j)t-1`. Each is complementary canonical; for `j>=1`
it is `2 mod3`. Consequently R37's first inverse step at `q_j` is exactly
`(2q_j-1)/3=q_(j-1)`. Appending the old absorption plan after any such
prefix cancels that prefix, including its formal coefficients. This is
the first complete undo loop. At the next state `q_(a-2)`, the binary
phase is instead canonical `1 mod8`; R37 takes its forward arrow to `r`.
The undo claim stops before that state. For example `w=93` has `q=139`
and `S(q)=209=1 mod8`; appending `H_209` need not cancel the first arrow.

At the endpoint, `v3(2r+1)=a-1`, because (1) makes `3` coprime to `t`.
The complete R41 inverse phase at `r` has lower endpoint
`2^(a-1)(2r+1)/3^(a-1)-1=q` and uses precisely the reverse of (2).
Appending this inverse current cancels the entire forward current. This is
the second complete undo loop. Neither observation rules out a different
forward comparison; both delimit a failed recipe exactly.

## 2. A complete signed interface with a different endpoint comparison

Write the finite formal W5 absorption plan of R41 as

```
div H_s=[s]-sum_u A_s(u)P(u).                         (3)
```

It is available arithmetically for every positive odd `s`, but its missing
pair currents are not supplied. Let `G` be the ordinary current along (2),
and put `z=nu(w)`. Since `w=5 mod8`, `z<=(w-1)/4`. Then

```
L_w=N_(3w)+G-N_w+H_r-H_z,
div L_w=P(w)-sum_u (A_r(u)-A_z(u))P(u).               (4)
```

Indeed the first three terms have divergence `P(w)-[r]+[z]`.
Adding (3) proves (4), with full multiplicities and both signs. Formula
(4) is the promised finite interface on every member of (1). It makes
no unknown orbit search. Opposite requests are combined before use.

The generic R43 bound is

```
A_s(u) nonzero => rho(u)<=(9s+5)/8.                  (5)
```

The lower plan `H_z` always has rank strictly below `q`, since
`z<=(w-1)/4` and `(9z+5)/8<q`. Only the upper plan needs a new test.
An exact current for every remaining requested pair, substituted with its
signed coefficient, produces an exact current of divergence `P(w)`.
The compiler rejects missing or incorrect currents and does not search
for them.

### A sharper complete endpoint bound

Put `n=nu(r)`. Applying (5) after the first prescribed R37 step gives the
following rational upper bounds on **every** rank requested by `H_r`:

| Canonical minimum `n` | Rank bound |
|---|---|
|`n=1`|`0`|
|`n=1 mod8`, `n>1`|`(27n+29)/32`|
|`n=3 mod4`, `n=2 mod3`|`(3n+1)/4`|
|`n=3 mod4`, `n=1 mod3`|`n`|
|`n=3 mod4`, `n=0 mod3`, `n/3 in W5`|`n`|
|`n=3 mod4`, `n=0 mod3`, `n/3 in W9`|`(9n+5)/8`|

For the first nontrivial row, `S(n)=(3n+1)/4`, giving (5). For the next,
the free inverse seed is `(2n-1)/3`. In the direct W5 rows, the first
request has rank exactly `n`; subsequent absorption of the smaller pair
index has rank below `n` by (5). The W9 row uses R43's complete W9 bound.
These are all possible canonical minima. If the applicable bound is below
`q`, (4) is a strictly rank-decreasing rule. This test is sufficient; an
unresolved result is not a proof of impossibility or of nonconvergence.

## 3. Two complete low-valuation subdomains

The rank test always succeeds on:

1. Every returning input with `a=3` for which `r` is **not** complementary
   canonical: `r` is noncanonical or `r=1 mod8`.
2. Every returning input with `a=4` for which `r` is noncanonical.

If `r` is noncanonical, `nu(r)<=(r-1)/2`; hence (5) improves to
`rho(u)<=(9r+1)/16`. If `r=1 mod8`, the first forward step instead gives
`rho(u)<=(27r+29)/32`.

For `a=3`, (1) is exactly `t=35 mod108`, so `t>=35`.
The noncanonical bound is smaller than `q=4t-1`; the `1 mod8` bound is
smaller precisely when `13t>95`, which always holds here.
For `a=4`, (1) is exactly `t=85 mod108`; the noncanonical bound is
smaller than `q=8t-1` precisely when `13t>25`, again always true.
The corresponding pair indices are also strictly below `w`.
These assertions cover their entire parameter domains, without a size cap.

## 4. Exact stratum thresholds and arbitrarily long successful runs

Every endpoint has a unique elementary stratum

```
r=lambda*n+beta,    n=nu(r),
(lambda,beta)=(4^k,(4^k-1)/3), or
              (2*4^k,(4^(k+1)-1)/3).                 (6)
```

The generic sufficient test `(9n+5)/8<q` is exactly

```
(2^(a+3)lambda-3^(a+1))*t >26lambda-18beta-9.        (7)
```

If `n>1` and `n=1 mod8`, the sharper forward test is exactly

```
(2^(a+5)lambda-3^(a+2))*t >122lambda-54beta-27.       (8)
```

These are also exactly the index tests `(3n+3)/4<w` and
`(9n+15)/16<w`, respectively. They are not assumed to hold for all
strata. In particular the new rank condition must not be replaced by an
index-only assertion on a direct critical request. For example `w=6645`
has parent rank `9967`; its formal request `u=4205<w` has rank `12615`.
The implementation retains this plan as unresolved for the common-rank
compiler, even though its pair-index bound decreases.

For each `a>=3`, choose any integer `k>=1` satisfying

```
4^k(2^(a+3)-20)>3^(a+1)-3.                          (9)
```

Such a `k` exists. Every returning member whose endpoint has at least `k`
sibling factors, `r=F^k(s)=4^k s+(4^k-1)/3` with `s` positive odd,
passes the generic bound using `s`. Substituting this scale and offset
in (7) makes its right side `20*4^k-3`; (9) makes the slope difference
larger than that already at `t=1`. Further elementary normalization only
reduces the generic bound.

This domain is nonempty and explicit for every `a,k`. Put
`lambda=4^k`, `beta=(lambda-1)/3`, `B=4lambda`, and choose the CRT progression

```
t=(2beta+2lambda+1)*3^(1-a) mod B,
t=10*2^(-a) mod27.                                  (10)
```

The moduli are coprime. The first congruence means exactly that
`(3^(a-1)t-1)/2=F^k(s)` for odd `s`; as `k>=1` it also implies the selected
phase `t=3^a mod4`. Every positive member of (10) gives (1), a positive
odd `s`, and strict descent. If `t0` is its least positive representative,
the pair indices are

```
w=(2^a t0-1)/3 + (9*2^a*B)j,   j>=0.               (11)
```

Thus the initial path length `a-1` is unbounded. Along these families,
`r/w` is unbounded as `a` grows: explicitly
`r/w=(3/2)(3^(a-1)t-1)/(2^a t-1)` has leading ratio
`(1/2)(3/2)^a`, and for `a>=3,t>=1` it exceeds
`(4/9)(3/2)^a`. A long or high first excursion therefore does not by
itself defeat this rule. This does not cover every endpoint of such a run.

## 5. Executable scope

`returning_phase.py` exports `forward_plan(w)` on the whole domain. Its
`seed`, `rank`, `current`, and signed `coefficients` satisfy (4).
`status='descending'` means the proved endpoint rank bound is strictly
below the parent rank. `index_status` is recorded separately. Unresolved
plans retain all requests. `compile_forward_plan` requires a descending
plan and exact supplied pair currents. `sibling_family` constructs (10).

Run:

```
python3 experiments/residual_progress/returning_phase/check_returning_phase.py
```

The deterministic receipt records exhaustive bounded interface checks,
both undo loops, the rational bounds, low-valuation classes, long CRT
families, capped discovery only for specified demonstration inputs, and
actual substituted currents. This finite evidence checks implementation;
the arguments above give the unbounded quantifiers. Universal coverage of
the remaining returning phase is open.
