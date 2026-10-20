---
id: returning-second-forward-interface
kind: result
title: A second complete forward run before requesting inputs on the returning W5 row
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1; original rank rho(w) = nu(3w) throughout. On the whole returning row of
  returning-forward-interface, compose the full returning prefix q -> r, complete normalisation r -> nu(r) and a
  prescribed next forward block before requesting any absorption: the signed current N_(3w) + G + N_r + D - N_w
  + H_f - H_nu(w) is accepted when the old-rho endpoint bound B(nu(f)) < rho(w). Quotient clocks add; the
  intervening signed normaliser is not zero ordinary elapsed time; some previously good tests worsen on this
  path, so prior accepted rules are kept. The entire first a = 3 failure is exactly complementary canonical r =
  157 mod 243 (q = (8r-5)/9, w = (16r-1)/27); for next exponents A = 2, 3, 4 the endpoint test is classified
  completely, including all affine offsets and arbitrarily large next d. For every original a >= 3 and second A
  >= 2, exact CRT families with sufficiently large odd d fail R44 but pass the new comparison, outside all seven
  earlier direct domains; no claim about all earlier supplied history follows, and universal coverage is open.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [returning-forward-interface, complementary-run-bridges, critical-image-rank-composition, elementary-bridge-quotient-normal-form]
certificates: [check_legacy_replay.py]
evidence:
  - "check_returning_continuation.py, returning_continuation.py, returning_continuation_audit.json: the legacy constructor and checker: 910 returning inputs, 768 exact low-exponent cells, 132 long families through a = A = 64 and eight actual conversions; three complete outputs stored. The bounded scan has 184 new acceptances and 23 cases where the alternate path worsens the old test (finite counts). Fails at its new path: returning_continuation.py loads ../returning_phase/, ../complementary_bridge/ and further siblings (now ../returning-forward-interface/, ../complementary-run-bridges/, ...) by their pre-migration folder names. Passed at be73a66 as experiments/residual_progress/returning_continuation/check_returning_continuation.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran every residual-progress step before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a); replayed unchanged, with its receipt, by check_legacy_replay.py"
aliases: [R52]
tags: [convergence, outer-residual, tripling-pairs, critical-rank, returning-row, forward-blocks]
---

# A second complete forward run before requesting inputs on the returning W5 row

## Statement

Odd-only clock, 1 absorbing; the rank is the original `ρ(w) = ν(3w)` of [`critical-image-rank-composition`](../critical-image-rank-composition/README.md). The domain is the whole returning row of [`returning-forward-interface`](../returning-forward-interface/README.md): `w ∈ W5`, `w ≡ 3 (mod 9)`, `3w = 2^a t − 1` selected, `q = ρ(w) = 2^(a−1)t − 1`, `r = (3^(a−1)t − 1)/2`, `z = ν(w)`.

1. **Interface.** Compose the full returning prefix `q → r`, the complete normalisation `r → ν(r)` and a prescribed next forward block (the run bridge of [`complementary-run-bridges`](../complementary-run-bridges/README.md), endpoint `f`) before requesting any `H`. The current `N_(3w) + G + N_r + D − N_w + H_f − H_ν(w)` has boundary `P(w)` minus its signed requests and is accepted when the endpoint bound `B(ν(f)) < ρ(w)`. Quotient clocks add; the intervening signed normaliser is not zero ordinary elapsed time. Some previously good tests worsen along this path, so earlier accepted rules are kept.
2. **First failure.** The entire first `a = 3` failure corresponds exactly to complementary canonical `r ≡ 157 (mod 243)`, with `q = (8r − 5)/9`, `w = (16r − 1)/27`.
3. **Classification.** For next exponents `A = 2, 3, 4` the endpoint test is classified completely, including all affine offsets and arbitrarily large next `d`.
4. **Families.** For every original `a ≥ 3` and second `A ≥ 2`, exact CRT families with sufficiently large odd `d` fail R44 but pass the new comparison, keeping the full ternary modulus `3^(a+2)` and the exact binary bit `2^(d+1)`. They are outside all seven earlier direct domains.

No claim about all earlier supplied history follows; universal coverage is open.

## Proof

The legacy note "A second full run before supplying the returning-phase inputs" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written conditional current interface, complete arithmetic subdomains,
and finite certificates.** A first returning run can increase the canonical
state; a second complete run can bring every required pair below the original
critical-image rank. The first run is not followed by its known inverse undo.
The remaining inputs are retained and universal coverage is open.

Use killed odd atoms `[1]=0`, `P(w)=[3w]-[w]`, and
`rho(w)=nu(3w)`. All pair indices lie in `W5={w>0:w=5 mod8}`.
The rank here is precisely R43's rho. No change of induction rank is made.
The side feed at `8bc27dfeeba7804d57964b68f6149eb1f6f6c247` was read as
external context; no sampled coverage statement is used in the proof.

### 1. Complete interface on the returning row

Let `w` belong to R44's entire returning row:

```
w in W5, w=3 mod9, 3w selected,
3w=2^a t-1, a>=3, t=3^a mod4, 2^a t=10 mod27.
```

Put `q=rho(w)=2^(a-1)t-1`, `r=(3^(a-1)t-1)/2`, and `z=nu(w)`.
The exact ordinary word `1^(a-2),2` takes q to r, with current G and length
`a-1`. Normalize r completely: `n=nu(r)`, with current N_r. Take one
additional prescribed block from n:

* If n=1, use the empty block, endpoint f=1, quotient length 0.
* If n=1 mod8 and n>1, use the single ordinary arrow to
  `f=(3n+1)/4`, quotient length 1.
* Otherwise n is complementary canonical. Write
  `n=2^A v-1`, `A>=2`, and
  `d=v2(3^(A-1)v-1)>=2`, `u=(3^(A-1)v-1)/2^d`.
  Use the entire R26 current D_n, with endpoint

```
f=3^floor(d/2) u                  if d is odd,
f=2*3^(d/2) u+1                 if d is even.          (1)
```

In the last case D_n has boundary `[n]-[f]`. The ordinary comparison clocks
are `A+(d-1)/2` versus 1 for odd d, and a single path of length
`A+d/2-1` for even d. Its exact quotient return is
`T^(A+floor(d/2)-1)(n)=nu(f)`. Thus the combined quotient clock from q is
`a-1` plus the specified second quotient length. These quotient clocks are
not the lengths of the original unnormalized ordinary comparison.

Write the formal R43 absorption plan as
`div H_s=[s]-sum A_s(v)P(v)`. It retains missing inputs; it is not an
absorption certificate without them. With D denoting the chosen second
block, define

```
J=N_(3w)+G+N_r+D-N_w+H_f-H_z,
div J=P(w)-sum_v (A_f(v)-A_z(v))P(v).                (2)
```

Every sign follows by telescoping the displayed boundaries. Opposite
requests are combined, including coefficients of magnitude greater than
one. The lower requests always have rho below q because `z<=(w-1)/4`.
Let B(s) denote R44's complete canonical endpoint bound, evaluated after
normalizing s. If `B(f)<q`, every request in (2) strictly decreases rho.
Supplied exact currents for those requests, multiplied by their signed
coefficients, give an exact current for P(w). Missing or incorrect inputs
are rejected. Neither the construction nor this implication uses an
unrestricted orbit search or assumes an unknown larger absorption input.

An alternative block can worsen a previously good test. This rule should
therefore be added after existing accepted rules, not substituted for them.
Its failures are not impossibility claims and could have other certificates.

### 2. The exact first-failure image at a=3

For a=3, R44 fails its bound test exactly when r is complementary canonical.
The other endpoint classes pass its proved low-exponent test, whereas a
complementary r has `r=4 mod9`, so B(r)=r and

```
q=(8r-5)/9 < r.
```

This entire failed domain is in bijection with

```
r>0 complementary canonical, r=157 mod243,
w=(16r-1)/27,   q=(8r-5)/9.                         (3)
```

Indeed the original t phase is exactly `t=35 mod108`, and
`2r+1=9t` gives the stated ternary residue. Conversely (3) gives positive
odd t, the selected binary phase and `w=3 mod9`. The weaker congruence
`r=22 mod27` would ensure only integrality of w and must not replace (3).
All r in (3) exceed or equal157. For `r=2^A v-1`, `A=2,3,4`, this gives
the useful uniform lower bound `v>=11`.

### 3. Complete next-run classification for A=2,3,4

On (3), let d and f be as in (1), and put m=nu(f). The exact test
`B(f)<q` has the following classification. An endpoint described as selected
in the table is always the even-d endpoint.

| Second exponent | Exactly the accepted cases |
|---|---|
|A=2|d odd; or even d>=4; or selected f|
|A=3|d odd; or even d>=8; or selected f with d>=4 or m not3 mod8|
|A=4|d odd; or even d>=10; or selected f with d>=6 or (d=4 and m=1 mod8)|

These are complete classifications of the stated endpoint-bound test,
not classifications of all possible currents. In each row d may be
arbitrarily large and v ranges over every allowed positive value.

#### Proof including intercepts

In terms of v, `q=(2^(A+3)v-13)/9`. Odd-d endpoints scale by 3/4 under
`d->d+2`. The generic bound `(9f+5)/8` at the worst value d=3 has positive
differences

```
A=2: (1319v-949)/576,
A=3: (1909v-949)/576,
A=4: (1631v-949)/576.                               (4)
```

Thus every odd-d endpoint passes. For even d, f is 1 mod3 and3 mod4.
If it is nonselected it is canonical and B(f)=f. At the last failing and
first passing depths the exact differences q-f are

|A|Last failure|First success|
|---|---|---|
|2|d2: `(-17v-17)/18`|d4: `(13v-95)/72`|
|3|d6: `(-139v-461)/288`|d8: `(1631v-2087)/1152`|
|4|d8: `(-3299v-2087)/1152`|d10: `(6487v-9077)/4608`|

The relation `f_(d+2)=3(f_d-1)/4+1` proves all other even thresholds.
Every stated positive expression is positive at v>=11.

If even f is selected, `m=(f-1)/2` is canonical and divisible by3.
Its residues1,3,7 modulo8 have respective bounds
`(27m+29)/32`, `(9m+5)/8`, and m. The worst generic bound is already
strictly below q at (A,d)=(2,2),(3,4),(4,6), with differences

```
(295v-353)/288, (1631v-1655)/1152, (6487v-7349)/4608. (5)
```

These remain positive for every larger even d. The boundary cases, in the
order m1,m3,m7 modulo8, are

```
(A,d)=(3,2):
 (1631v-1979)/1152, (-139v-353)/288, (13v-25)/36;
(A,d)=(4,4):
 (6487v-8645)/4608, (-3299v-1655)/1152, (-139v-127)/144;
(A,d)=(4,2):
 (-3299v-1979)/1152, (-2465v-353)/288, (-217v-25)/36.  (6)
```

Their signs at v>=11 prove every row and every failure in the table.

### 4. New full families for every pair of first exponents

For every original `a>=3` and second `A>=2`, there is a complete nonempty
congruence family in which the first R44 test fails and (2) passes.
The first endpoint is complementary canonical, so this is genuine new
coverage of that test, rather than a restatement of its earlier sibling
families.

Choose an odd d>=3 satisfying

```
7*3^(a+A+floor(d/2)-3) <= 2^(a+A+d-1).              (7)
```

Such d exist because the ratio improves by3/4 when d increases by2. Put
`M=3^(a+2)`, and choose v by the two coprime congruences

```
2*(2^A v-1)+1 = 10*3^(a-1)*2^(-a) mod M,
v = (1+2^d)*3^(1-A) mod2^(d+1).                    (8)
```

The first congruence retains the complete original returning phase; the
second gives the exact second valuation d, including its extra binary bit.
Every positive member yields

```
r=2^A v-1,
t=(2r+1)/3^(a-1),
w=(2^a t-1)/3.                                    (9)
```

All three are positive integers. The second congruence gives
`v=-3^A mod4`, so r is complementary canonical. Since r=4 mod9,
B(r)=r. Write `c=(2/3)^(a-1)`. Then
`q=c(2r+1)-1<r`, because c<=4/9. Thus the first test always fails.

For the second block write
`L=3^(A-1+floor(d/2))/2^(A+d)`. The positive odd endpoint satisfies
`f<L(r+1)<=4Lr/3`, since r>=3. Also `(9f+5)/8<=7f/4`. Because
`2r+1=3^(a-1)t`, t>=1, one has `q>cr`. Condition (7) is exactly
`7L/3<=c`. Therefore

```
B(f) <= (9f+5)/8 <= 7f/4 < 7Lr/3 <= cr < q.        (10)
```

This proves the whole family, with all intercepts and every positive
progression member. If v0 is the least positive CRT representative, the
progression has v period `2^(d+1)*3^(a+2)` and w period
`9*2^(a+A+d+2)`.

These inputs are outside the old seven direct rule domains. They are
returning, hence outside R41's good phase and every nonselected rule; the
old R44 test fails as proved. The selected R46 rule has at the original
q the exact parameters D=1,j=1: q=4 mod27 and
`v3(4(q-1)/3+2)=v3(2w)=1`. It therefore fails the required j>=2 predicate.
This does not assert that none was already certified by supplied history
or by a different finite comparison.

### 5. Executable scope and checks

`returning_continuation.py` exports `continuation_plan`, `recognized`,
`compile_plan`, and `long_family(a,A,index=0,d=None)`. The constructor
uses only prescribed finite blocks and formal absorption plans. All
currents are integer and all source coefficients are retained. A finite
rule application may have no remaining inputs by actual cancellation;
this is a finite certificate, not universal supply.

Run `python3 experiments/residual_progress/returning_continuation/check_returning_continuation.py`.
The stored deterministic receipt checks whole bounded interfaces, exact
quotient and ordinary clocks, all displayed affine intercepts, the complete
low-exponent table, long CRT families, rejection of missing inputs, and
actual substitutions for designated examples. Only the demonstration
inputs use capped absorption discovery. The written arithmetic arguments,
not the finite sample, establish the unbounded families and classifications.

The default replay covers910 returning inputs below131072, including184
that pass the new test after failing the first test. It also records23
old accepted inputs that this alternate continuation would fail, enforcing
the priority warning above. There are99 low-exponent cases in that range,
768 independently generated low-exponent CRT cases, and132 accepted long
families with first and second exponents through64. Eight actual supplied
conversions use18 distinct finite pair inputs. The receipt stores full
inputs and output tables for w1533 (66 rows), w3837 (46 rows) and w5565
(58 rows). Seven invalid or missing-input requests are rejected. Generation
and deterministic default replay both passed in approximately7.4 seconds
in this environment. These are finite implementation checks, not estimates
of asymptotic coverage or evidence that every remaining leaf is supplied.

Dependencies: [first returning run](../returning-forward-interface/README.md),
[complete second run](../complementary-run-bridges/README.md),
[elementary quotient](../elementary-bridge-quotient-normal-form/README.md), and
[common rank](../critical-image-rank-composition/README.md).

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B11 migration; standard library). The legacy scripts in this folder load their sibling modules by pre-migration folder names, so they no longer run here. This certificate rebuilds the legacy directory layout in a temporary directory from the node folders that now hold those files, runs the unmodified legacy checks there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied receipt unchanged. It writes nothing in the repository. It replays: the legacy checker `check_returning_continuation.py` (about 8 s; the counts of section 5 and three stored outputs, compared with `returning_continuation_audit.json`). The command in the legacy text names `experiments/residual_progress/returning_continuation/`.

## Remarks

- Added after the seven earlier rules in the nine-family dispatcher (`continued_rules.py`, in [`low-block-continuation-prescribed-growth`](../low-block-continuation-prescribed-growth/README.md)). The legacy note read the side-lane feed at `8bc27df` as context only; no sampled coverage figure is a premise.
- Novelty undetermined (none claimed).

## History

- Migrated from `experiments/residual_progress/returning_continuation/RETURNING_SECOND_BLOCK.md` (legacy ID R52) at commit `be73a66`, by the B11 migration (Claude, Opus 5.5). Note, scripts and receipts moved byte-identical; `check_legacy_replay.py` was added at the migration. Legacy status: "written conditional interface, exact low-exponent classification and complete CRT families".
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `8764158`. The batch's "independent model" proof and code reviews (archive/convergence-residual-progress/REPORT.md) were the main lane's own agents, not a different lane.
