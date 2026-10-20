# A separate rank absorbs the critical-nine expansion

**Status: written uniform bound and conditional construction.** The rank
below changes how the returning W5 inputs are ordered. It removes the
factor9/8 from formal absorption bounds and certifies a complete further
forward domain. It cannot be substituted silently into the earlier rule
union. Universal supply of the remaining inputs is still open.

Use the notation of [R43](../critical_rank/CRITICAL_IMAGE_RANK.md).
All currents are finite signed integer currents; H_s is the unchanged
R41 formal absorption plan with divergence[s] minus its signed W5 requests.
Let E_return={w in W5:w=3 modulo9 and3w selected}, as in
[R44](../returning_phase/RETURNING_FORWARD_INTERFACE.md). Define

```
sigma(w) = 4w/3−1 = (8rho(w)−5)/9, if w in E_return;
           rho(w),                  otherwise.                 (1)
```

Every w in W5 satisfies w<sigma(w)<=rho(w). The exceptional value is
the canonical W9 ancestor in the R41 returning phase. This is a specified
integer rank, not a claim that it is the minimum of all inverse ancestors.

## 1. Uniform absorption bound

**Theorem.** Every W5 request u in H_s satisfies

```
sigma(u) <= nu(s) <= s.                                      (2)
```

First consider the complete R40 elimination of a W9 request b. Every
resulting request u has sigma(u)<=3b. In its local proof, all ordinary
smaller-index requests satisfy rho(u)<=3u<3b. The only larger indices
occur in the three rows d=4,6,8 listed in R43. The d6 and d8 exceptional
rho values are already strictly below3b. In the d4 row the exceptional
index is u=(9b+3)/4, with selected3u and u=3 modulo9. Consequently

```
sigma(u)=4u/3−1=3b.                                        (3)
```

All auxiliary requests in this row have smaller index than b. Every
recursive W9 request c is also smaller than b; induction bounds its
descendants by3c<3b. This proves the asserted bound for the full signed
elimination. Cancellation can remove requests and cannot introduce a
larger one.

Now the original R37 absorption plan first normalizes s and strictly
decreases its seed thereafter. A direct W5 request has rho<=nu(s), hence
sigma<=nu(s). A W9 request b comes from a critical root3b<=nu(s), and
the preceding argument handles its elimination. This proves(2).
The bound can be attained: H_27 requests21, with sigma(21)=27.

## 2. Complete first-step endpoint bounds

The following integer bounds B_sigma(n) apply to every request in H_s,
where n=nu(s):

| Canonical n | Bound |
|---|---|
|n=1|0|
|n>1,n=1 modulo8|(3n+1)/4|
|n=3 modulo4,n=2 modulo3|(2n−1)/3|
|critical n with W5 index v|sigma(v)|
|critical n with W9 index|n|

The first two nontrivial rows apply(2) after the prescribed forward or
inverse step. In the W5 row the leading request is v and all other
requests have sigma<=v<sigma(v). The W9 row uses(2). Thus the table is
a proved upper bound; it is not asserted to equal the actual maximum in
every case. Each row includes its integer offset.

The R44 returning and R48 nonselected full forward interfaces remain exact
signed identities. Reuse their currents and accept an interface when

```
B_sigma(nu(endpoint)) < sigma(w).                            (4)
```

The lower absorption input z=nu(w)<w/4 always has sigma ranks<=z<sigma(w).
Hence every final request in an accepted interface strictly decreases(1).
The ordinary and quotient clocks remain precisely those of R44/R48.

## 3. A complete additional forward domain

Every positive input

```
w=437+512m,   m>=0,                                        (5)
```

has nonselected q=3w=32t−1, with t=41+48m and exact first parameters
a=5,d=3. Conversely these conditions on nonselected W5 give(5): the
valuation condition is t=9 modulo16 and integrality is t=2 modulo3.
The full R26 endpoint is

```
f=(243t−3)/8,
q−f=(13t−5)/8>0.                                         (6)
```

By(2) every upper request has sigma<=nu(f)<=f<q=sigma(w).
The full forward current therefore gives a strict-sigma reduction on
every member of(5). More generally a=5 and any odd d>=3 satisfy f<q:
increasing d by2 multiplies f's positive affine numerator by3 and its
denominator by4, so its value decreases for fixed t. This comparison is
used only for parameter values having the stated exact valuation.

This need not decrease rho. At w44981 the current has a request96069:

```
parent: rho=sigma=134943;
child:  rho=144103, sigma=128091.
```

The parent is outside the earlier seven direct rule domains. The example
illustrates the different order; the proof of(5) does not depend on it.

## 4. Compatibility is a theorem obligation

Every old strict-rho rule at a parent outside E_return also decreases
sigma: its parent ranks agree, and every child's sigma is no larger than
its rho. Thus the six old rule families outside R44 remain valid.
The returning rule must be retested. A concrete failure is

```
w4629: rho=6943, sigma=6171;
R44 requests {5:−1,69:+1,2197:+1};
sigma(2197)=rho(2197)=6591>6171.
```

This is a valid old-rho rule and an invalid sigma step. It prevents claiming
that all previously accepted rules automatically compose with the new
ones. Neither rank invalidates the proofs using the other rank.

For any fixed family of exact signed rules whose every edge decreases
sigma, strong induction on its positive integer values supplies the same
conditional composition theorem as R43. Universal currents on its
unrecognized W5 complement suffice by R40/R37; the complement remains
missing. `sigma_rank.py` uses the old nonreturning rules and the retested
forward interfaces. It is a separate dispatcher and compiler, with
explicit rank validation and missing-input rejection. It does not modify
the old seven-rule dispatcher.

## 5. Reproduction

Run `python3 experiments/residual_progress/phase_rank/check_sigma_rank.py`.
The finite audit checks complete W9 and absorption samples, endpoint
bounds, all members of(5) within a declared range and large prescribed
examples, both rank-comparison counterexamples, signed mixed closure and
actual supplied-current substitution. The saved44981 fixture retains its
inputs and output. The infinite statements rest on the proof above.

The deterministic receipt contains1024 W9 eliminations,4096 absorption
plans,132 progression examples (including indices through2^128) and five
actual substitutions. On1024 W5 inputs below8192, the old dispatcher accepts
442 and this dispatcher459;441 are shared,18 occur only in the sigma
dispatcher and one only in the old dispatcher. These finite sets are
incomparable, consistent with the explicit4629 counterexample. They are
conditional rule domains, not counts of independently proved absorption.

No universal current constructor, asymptotic coverage or novelty claim is
supplied. In particular improving an input bound does not force every
forward block to satisfy(4).
