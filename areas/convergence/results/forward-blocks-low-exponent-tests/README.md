---
id: forward-blocks-low-exponent-tests
kind: result
title: "Complete forward blocks on the nonselected critical-five domain, with exact low-exponent rank tests"
status: reviewed
claim: >
  Odd-only 3x+1 map S, absorbing at 1; rho(w) = nu(3w). For every w in W5 with 3w nonselected write q = 3w = 2^a
  t - 1, d = v2(3^(a-1) t - 1), u = (3^(a-1) t - 1)/2^d. The complete-run-bridge endpoint is f = 3^floor(d/2) u
  (d odd) or 2*3^(d/2) u + 1 (d even), with exact quotient return time a + floor(d/2) - 1 (odd d: ordinary
  comparison clocks a + (d-1)/2 versus 1; even d: an ordinary path of length a + d/2 - 1). The formal current
  D_q - N_w + H_f - H_nu(w) retains every signed W5 request, and the full canonical endpoint bound B(nu(f)) < q
  of returning-forward-interface gives a strict-rho rule. For a = 3 the test accepts exactly odd d, even d >= 6,
  or a selected even endpoint f; for a = 4 exactly odd d, even d >= 10, selected even f with d >= 6, or selected even f with d = 4
  and nu(f) != 3 mod 8 (all intercepts included). The classes 45 mod 384 and 741 mod 768 of multiples of three
  lie inside, and for each a >= 3 an explicit large odd d and CRT progression give further accepted multiples of
  3. For a canonical even endpoint the maximal inverse of variable-depth-inverse-escape-barrier (D = d/2, j =
  a-1) returns exactly to q and cancels the current. These classify this sufficient test, not all possible
  currents; universal endpoint coverage is open.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [complementary-run-bridges, critical-image-rank-composition, returning-forward-interface, variable-depth-inverse-escape-barrier]
certificates: [check_legacy_replay.py]
evidence:
  - "check_nonselected_forward.py, nonselected_forward.py, nonselected_forward_audit.json: the legacy constructor and checker: 2047 inputs, 1536 a = 3/4 decisions, 687 undo identities, 75 CRT examples through a = 128, 32 multiple-of-3 phase examples and 12 actual substitutions; three current tables are retained. Fails at its new path: nonselected_forward.py loads ../complementary_bridge/, ../inverse_escape/ and ../returning_phase/ (now ../complementary-run-bridges/, ../variable-depth-inverse-escape-barrier/, ../returning-forward-interface/) by their pre-migration folder names. Passed at be73a66 as experiments/residual_progress/nonselected_forward/check_nonselected_forward.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran every residual-progress step before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a); replayed unchanged, with its receipt, by check_legacy_replay.py"
reviewed_by:
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Full re-derivation of the parameters, the run-bridge endpoint and clocks, the interface identity, the a = 3/4 classification with every displayed intercept, the stratum inequalities, the CRT families and the undo identity, with an independent implementation on all 8,191 nonselected W5 inputs below 2^17 reproducing the receipt's counts and all 65 low-exponent categories; certificate re-run (PASS, exit 0, 11.5 s); 3x+5 and 3x+13 analogues of the identities checked. HOLDS WITH CORRECTIONS: the omitted hypothesis 'selected' inserted in the a = 4, d = 4 clause of the claim and of Statement item 3"
aliases: [R48]
tags: [convergence, outer-residual, tripling-pairs, critical-rank, forward-blocks, sufficient-set]
---

# Complete forward blocks on the nonselected critical-five domain, with exact low-exponent rank tests

## Statement

Odd-only clock, 1 absorbing; `ρ(w) = ν(3w)`; `B = {w ∈ W5 : 3w nonselected}`.

1. **Whole-domain interface.** Write `q = ρ(w) = 3w = 2^a t − 1` (`a ≥ 3`), `d = v2(3^(a−1)t − 1) ≥ 2`, `u = (3^(a−1)t − 1)/2^d`. The endpoint of the complete run bridge of [`complementary-run-bridges`](../complementary-run-bridges/README.md) is `f = 3^⌊d/2⌋·u` (odd `d`) or `2·3^(d/2)·u + 1` (even `d`), with exact quotient return time `a + ⌊d/2⌋ − 1`; odd `d` has ordinary comparison clocks `a + (d−1)/2` versus 1, even `d` an ordinary path of length `a + d/2 − 1`. The formal current `D_q − N_w + H_f − H_ν(w)` retains every signed `W5` request.
2. **Sufficient test.** The full canonical endpoint bound `B(ν(f)) < q` of [`returning-forward-interface`](../returning-forward-interface/README.md) gives a strict-`ρ` rule.
3. **Exact low-exponent classification of the test.** `a = 3`: accepted exactly for odd `d`, even `d ≥ 6`, or a selected even endpoint `f`. `a = 4`: exactly odd `d`, even `d ≥ 10`, selected even `f` with `d ≥ 6`, or selected even `f` with `d = 4` and `ν(f) ≢ 3 (mod 8)`. All intercepts are included.
4. **New domains.** The complete multiples-of-three classes `45 (mod 384)` and `741 (mod 768)` lie inside; for each `a ≥ 3` an explicit large odd `d` and CRT progression give further accepted multiples of 3.
5. **Undo.** For a canonical even endpoint the maximal inverse of [`variable-depth-inverse-escape-barrier`](../variable-depth-inverse-escape-barrier/README.md) has `D = d/2`, `j = a − 1`, and its predecessor is exactly `q`: it reverses the block and cancels the current literally.

These classify this sufficient test, not all possible currents. Universal endpoint coverage is open.

## Proof

The legacy note "Complete forward blocks on the nonselected critical-five domain" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written conditional interface, exact low-exponent classification,
and finite certificates.** The rule is defined on every nonselected W5 pair.
Its accepted domain includes complete multiples-of-three families absent
from the earlier four-rule union. Missing currents remain explicit; universal
closure is open. No novelty or human/formal verification claim is made.

Use positive odd Syracuse `S`, absorbed at 1, killed atoms `[1]=0`,
`P(w)=[3w]-[w]`, elementary minimum `nu`, and rank `rho(w)=nu(3w)`.
The dependencies are the [R26 complete block](../complementary-run-bridges/README.md),
[R43 rank bound](../critical-image-rank-composition/README.md),
[R44 endpoint table](../returning-forward-interface/README.md), and
[R46 maximal inverse word](../variable-depth-inverse-escape-barrier/README.md).

### 1. The whole domain and exact clocks

Let

```
B={w>0: w=5 mod8 and 3w is nonselected}.
q=rho(w)=3w=2^a t-1,      a>=3,
t=-3^a mod4,             2^a t=1 mod3,
d=v2(3^(a-1)t-1)>=2,     u=(3^(a-1)t-1)/2^d.
```

These parameters are unique; conversely they describe the whole domain.
The odd `t` is not divisible by 3. Thus `u=1 mod3` for odd d and
`u=2 mod3` for even d. Put `b=floor(d/2)` and define the complete R26
endpoint

```
f=3^b u                  if d is odd,
f=2*3^b u+1              if d is even.                 (1)
```

The explicit finite current `D_q` has divergence `[q]-[f]`. If d is
even it is an ordinary path of length `a+d/2-1`. If d is odd its positive
path has length `a+(d-1)/2` and its negative path is the single arrow
from f; their endpoints coincide. All current rows use the ordinary clock.
In the canonical quotient `T=nu S`, both cases give the exact identity

```
T^(a+floor(d/2)-1)(q)=nu(f).                            (2)
```

Indeed the even prefix ends at f; in the odd case the prefix one step
shorter ends at `F(f)=4f+1`. Semiconjugacy and `nu(F(f))=nu(f)` prove
(2). This variable-time acceleration is not assumed to decrease rank.

### 2. A whole-domain signed current and a sufficient rank test

Write the formal absorption plan as

```
div H_s=[s]-sum_v A_s(v)P(v),
A_s(v) nonzero => v in W5 and rho(v)<=(9s+5)/8.         (3)
```

The plan is a finite arithmetic object, not a supply of its pair currents.
Let `N_w` have divergence `[w]-[z]`, where `z=nu(w)<=(w-1)/4`.
Then

```
J_w=D_q-N_w+H_f-H_z,
div J_w=P(w)-sum_v (A_f(v)-A_z(v))P(v).               (4)
```

The lower requests have rank below q by (3). For the upper requests put
`n=nu(f)` and use the complete bound:

| n | B(n), an upper bound on every requested rank |
|---|---|
|1|0|
|`n>1`, `n=1 mod8`|`(27n+29)/32`|
|`n=3 mod4`, `n=2 mod3`|`(3n+1)/4`|
|`n=3 mod4`, `n=1 mod3`|n|
|`n=3 mod4`, `n=0 mod3`, `n/3 in W5`|n|
|`n=3 mod4`, `n=0 mod3`, `n/3 in W9`|`(9n+5)/8`|

This is R44's general canonical endpoint table, applied to the full block
endpoint (1). The acceptance test is exactly `B(n)<q`. Every accepted
rule has only strictly smaller-rank W5 requests, with all signed
multiplicities retained. Substitution of supplied exact currents gives
an exact P(w) current; the compiler rejects missing or incorrect inputs.
An unresolved test does not exclude cancellation of its requests by
another rule or a different comparison.

The entire rule is an explicit special case of the R43 rank induction.
It may be joined to any earlier strict-rho domains. No new bound on
current cost, residual mass, or universal acceptance is inferred.

### 3. Complete classification of this test for a=3 and a=4

For **every** member of B with `a=3`, the test accepts precisely when

```
d is odd, or d>=6, or the even-d endpoint f is selected. (5)
```

For **every** member of B with `a=4`, it accepts precisely when

```
d is odd; or
d is even and d>=10; or
d is even, f is selected, and
    [d>=6 or (d=4 and nu(f) is not3 mod8)].             (6)
```

Here selected is the complete arithmetic predicate, with no bounded
valuation truncation. These are complete classifications of the stated
endpoint-bound test, not necessary conditions for current existence.

**Proof.** The allowed t satisfy `t=5 mod12` when a=3 and `t=7 mod12`
when a=4. Thus their respective minima are 5 and 7. At fixed a,t,
increasing d by two scales the odd endpoint by `3/4`, and changes the
even endpoint f to `3(f-1)/4+1`; both decrease whenever meaningful.
Comparing these expressions at the least d gives valid bounds for all
larger d of the same parity, whether or not the smaller d itself is an
exact valuation for that t.

For odd d, the worst case is d=3. At a=3 its generic bound `(9f+5)/8`
is `(243t+13)/64`, below `q=8t-1`. At a=4 it is `(729t+13)/64`, below
`q=16t-1`. Further normalization only improves the bound.

For even d, f is `1 mod3` and `3 mod4`. If f is nonselected, it is
canonical and its bound is exactly f. If it is selected, its elementary
minimum is `n=(f-1)/2`, with bound at most `(9f+1)/16<f`.
At a=3, f is below q exactly when d>=6: at d=6 the difference is
`(13t-37)/32>0`; at d=2 and d=4 the differences f-q are respectively
`(11t+1)/2` and `(17t+7)/8`, both positive. A selected endpoint already
succeeds at d=2, since the difference from its generic normalized bound
is `(13t-25)/32>0`. This proves (5).

At a=4 a nonselected endpoint succeeds exactly for d>=10: at d=10 the
difference q-f is `(1631t-781)/512>0`, while at d=8 it is
`(-139t-175)/128<0`. A selected endpoint succeeds for every d>=6:
at d=6 the difference from its generic normalized bound is
`(1631t-589)/512>0`. For d=4, the canonical minimum is
`n=(243t-9)/16`, divisible by 3. Its possible canonical residues are
1, 3, or 7 modulo 8. The respective bounds give q minus bound equal to

```
(1631t-733)/512,   (-139t-127)/128,   (13t-7)/16.
```

Exactly the middle case fails. At d=2, `n=(81t-3)/4`; the three
corresponding differences are

```
(-139t-163)/128,   (-217t-25)/32,   (-17t-1)/4,
```

all negative. This proves (6), including all intercepts.

### 4. Exact stratum conditions at any first exponent

Every raw endpoint has a unique elementary stratum

```
f=lambda*n+beta,
(lambda,beta)=(4^k,(4^k-1)/3) or
              (2*4^k,(4^(k+1)-1)/3),   n=nu(f).
```

Write `epsilon=0, kappa=1` for odd d and `epsilon=1, kappa=2` for
even d, and put `A=kappa*3^(a-1+b)`, `C=kappa*3^b`. Then
`f=(A*t-C)/2^d+epsilon`. The generic sufficient test is exactly

```
(2^(a+d+3)*lambda-9A)*t
    >13*2^d*lambda+9*2^d*(epsilon-beta)-9C.             (7)
```

For a nonabsorbing `n=1 mod8` the sharper forward test is exactly

```
(2^(a+d+5)*lambda-27A)*t
    >61*2^d*lambda+27*2^d*(epsilon-beta)-27C.            (8)
```

These are exact integer inequalities, including offsets. The full table
in Section 2 can be sharper; neither inequality is assumed universal.

### 5. Nonempty successful multiples-of-three families for every a

For every integer `a>=3`, choose an odd `d>=3` satisfying

```
2^d*(2^(a+3)-13)>9*3^((d-1)/2)*(3^(a-1)-1).          (9)
```

Such odd d exist, since increasing d by two multiplies the left side
by 4 and the right side by 3. Condition (9) is the generic comparison
`(9f+5)/8<q` already at t=1, with a positive slope difference; it
therefore holds for every t>=1. Prescribe the exact CRT family

```
t=3^(1-a)*(1+2^d) mod2^(d+1),
t=2^(-a) mod9.                                         (10)
```

The coprime moduli give one full positive progression. The first
congruence fixes the exact d including its extra bit and makes t odd
with `t=-3^a mod4`. The second gives `q=0 mod9`, hence `3|w`.
Thus every positive member supplies a nonselected W5 pair accepted
by (9), with the exact parameters a,d. If t0 is the least positive
representative, its pair progression is

```
w=(2^a*t0-1)/3 + 3*2^(a+d+1)*j,   j>=0.               (11)
```

In particular the full classes `w=45 mod384` (a3,d3) and
`w=741 mod768` (a4,d3) succeed. More generally all multiples-of-three
members in (5) or (6) succeed, not just these two illustrations.
For each a the initial rising block has a-1 valuation-one arrows;
these lengths grow without bound as a varies. The full ordinary and
quotient clocks remain those in Section 1.

Every such multiple-of-three input was an unaccepted leaf of the earlier
R41/R44/R45/R46 union: R41, R44 and R46 require selected3w, and R45's two
accepted ternary phases exclude3|w. This is new whole-domain coverage
within that specified union. It is not a claim that no other earlier
certificate can happen to prove one of these inputs.

### 6. An exact forward/inverse undo on the remaining even block

For every even d with canonical raw endpoint f, R46's maximal inverse
parameters at f are exactly

```
D=d/2=b,      j=a-1,      predecessor=q.               (12)
```

Indeed `f-1=2*3^b*u` and `3` does not divide u, so D=b. Its inverse
spine ends at `2^(d+1)u+1`; adding 1 gives
`2*(2^d*u+1)=2*3^(a-1)t`, of exact ternary order a-1. The following
point block therefore ends at `2^a*t-1=q`. Its ordinary word is
exactly the original `1^(a-1),2^b` path, reversed as a signed current.
The sum of the forward and inverse currents is literally zero.

Thus applying the maximal inverse block to that same forward endpoint
does not itself create a new comparison. This exact whole-domain undo
does not rule out a different inverse word, another forward excursion,
joint signed cancellation, or composition through other accepted rules.

### 7. Implementation and finite evidence

`nonselected_forward.py` exports `forward_plan(w)`, with fields
`seed,rank,status,current,coefficients`. The exact boundary is (4);
`status='descending'` means the table bound is below rho(w). Missing
inputs are retained with their signs. `small_exponent_domain` implements
the complete classification (5)–(6); `long_family` constructs (10).
`even_undo` checks (12). No construction searches an unknown future.

```
python3 experiments/residual_progress/nonselected_forward/check_nonselected_forward.py
```

The receipt records bounded whole-domain checks, direct verification of
the low-exponent table and its affine comparisons, exact long CRT cases,
undo identities, capped discovery only for designated demonstration
inputs, and actual supplied-current substitutions. Those checks audit
the implementation; the written arguments give the universal quantifiers.

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B11 migration; standard library). The legacy scripts in this folder load their sibling modules by pre-migration folder names, so they no longer run here. This certificate rebuilds the legacy directory layout in a temporary directory from the node folders that now hold those files, runs the unmodified legacy checks there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied receipt unchanged. It writes nothing in the repository. It replays: the legacy checker `check_nonselected_forward.py` (about 6 s; the counts of section 7 and three stored current tables, compared with `nonselected_forward_audit.json`). The command in the legacy text names `experiments/residual_progress/nonselected_forward/`.

## Remarks

- Continued through a second block by [`low-block-continuation-prescribed-growth`](../low-block-continuation-prescribed-growth/README.md); its whole-cylinder three-step plans contain those of [`inverse-only-exclusions-short-forward`](../inverse-only-exclusions-short-forward/README.md) section 5. Joined to the dispatcher in [`two-inverse-phases-intermediate-increase`](../two-inverse-phases-intermediate-increase/README.md).
- Novelty undetermined; the legacy note also disclaims human or formal verification.

## History

- Migrated from `experiments/residual_progress/nonselected_forward/NONSELECTED_FORWARD.md` (legacy ID R48) at commit `be73a66`, by the B11 migration (Claude, Opus 5.5). Note, scripts and receipts moved byte-identical; `check_legacy_replay.py` was added at the migration. Legacy status: "written whole-domain conditional interface and exact classification of its rank test for a3/a4".
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `bcde58e`. The batch's "independent model" proof and code reviews (archive/convergence-residual-progress/REPORT.md) were the main lane's own agents, not a different lane.
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. Correction: the `a = 4`, `d = 4` clause of the claim field and of Statement item 3 now reads "selected even `f` with `d = 4` and `ν(f) ≢ 3 (mod 8)`", the hypothesis the proof's (6) uses; read literally, the old wording admitted nonselected endpoints `f ≡ 7 (mod 8)`, which the test rejects (65 inputs below `2^17`, the first `w = 1893`). See [`REVIEW-2026-10-31-claude-review-lane.md`](REVIEW-2026-10-31-claude-review-lane.md).
