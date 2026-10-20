---
id: selected-critical-five-forward-tables
kind: result
title: "Complete forward tables for selected critical-five inputs, with infinite decreasing domains"
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1; original rank rho(w) = nu(3w), no sigma rule. For selected 3w and w = 5
  mod 8, q = rho(w) = (3w-1)/2 = 2^A t - 1 is complementary canonical, A >= 2; applying the complete run-bridge
  block, with its raw endpoint f and elementary normalisation, before requesting H gives the exact plan N_(3w) +
  D_q + N_f - N_w + H_nu(f) - H_nu(w), which strictly decreases rho whenever the branchwise endpoint bound
  B(nu(f)) < q. The first-block table is exact for A = 2, 3, 4; after the failed first A = 2, d = 2 block a
  complete second-block table is exact for second exponents 2, 3, 4; all signed W5 requests and both clocks stay
  explicit. Every selected w = 2 mod 3 is outside the old nine direct predicates, and for each A >= 2 an exact
  CRT progression with large odd d passes (e.g. 221 mod 384, 2813 mod 3072); inside the R54 phase the whole
  progression 10357 mod 13824 (A = 4, d = 3) decreases, while the proposed replacement 3445 mod 13824 is false
  (counterexamples 58741 and 86389). Recognition of all remaining inputs and universal pair currents are not
  proved.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [complementary-run-bridges, returning-forward-interface, forward-blocks-low-exponent-tests, low-block-continuation-prescribed-growth, growing-prefix-unhandled-leading-input, critical-image-rank-composition, elementary-bridge-quotient-normal-form]
certificates: [check_legacy_replay.py]
evidence:
  - "check_selected_forward.py, selected_forward.py, selected_forward_audit.json: the legacy constructor and checker: 2049 selected inputs below 32768, 256 second-block inputs, 683 old-rule exclusions, 78 CRT examples through A = 128, 128 progression points and four actual substitutions; two completed output currents and their supplied inputs are stored. The finite window has 905 new acceptances (no asymptotic coverage claim). Fails at its new path: selected_forward.py loads ../continued_rules/, ../critical_rank/ and ../nonselected_forward/ by their pre-migration folder names. Passed at be73a66 as experiments/residual_progress/selected_forward/check_selected_forward.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran every residual-progress step before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a); replayed unchanged, with its receipt, by check_legacy_replay.py"
aliases: [R55]
tags: [convergence, outer-residual, tripling-pairs, critical-rank, selected-phase, forward-blocks]
---

# Complete forward tables for selected critical-five inputs, with infinite decreasing domains

## Statement

Odd-only clock, 1 absorbing; the rank is always `ρ(w) = ν(3w)`. Domain: `w ≡ 5 (mod 8)` with `3w` selected, so `q = ρ(w) = (3w − 1)/2 = 2^A t − 1` is complementary canonical, `A ≥ 2`.

1. **Interface.** Apply the complete run-bridge block of [`complementary-run-bridges`](../complementary-run-bridges/README.md), including its raw endpoint `f` and elementary normalisation, before requesting `H`. The exact plan `N_(3w) + D_q + N_f − N_w + H_ν(f) − H_ν(w)` strictly decreases `ρ` whenever the complete branchwise endpoint bound `B(ν(f)) < q` (the table of [`returning-forward-interface`](../returning-forward-interface/README.md)).
2. **Tables.** The first-block table is exact for `A = 2, 3, 4`. After the failed first `A = 2`, `d = 2` block, a complete second-block table is exact for second exponents 2, 3, 4. All signed `W5` requests and the ordinary and quotient clocks stay explicit.
3. **New domains.** Every selected `w ≡ 2 (mod 3)` is outside the old nine direct predicates (proved directly from them). For each `A ≥ 2` an exact CRT progression with sufficiently large odd depth `d` passes (examples `221 (mod 384)`, `2813 (mod 3072)`). Inside the phase of [`growing-prefix-unhandled-leading-input`](../growing-prefix-unhandled-leading-input/README.md), the whole progression `10357 (mod 13824)` has `A = 4`, `d = 3` and decreases.
4. **A refuted replacement.** The proposed progression `3445 (mod 13824)` is false: 58741 and 86389 are stored counterexamples; 3445 itself passes a different `A = 4`, `d = 4` branch. The maximal inverse of the first failed `A = 2`, `d = 2` endpoint exactly undoes that block, motivating the second forward comparison.

It does not prove that the remaining inputs are recognised or that every pair current exists.

## Proof

The legacy note "Selected critical-five inputs: complete forward interfaces" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written proof, exact conditional constructors, and bounded replay.**
This extends the old-rank forward method to every selected critical-five
input. It proves complete low-exponent decision tables and infinite arithmetic
domains outside all nine earlier rule predicates. It does not prove that the
remaining inputs are recognized or that every pair current exists. The rank is
always `rho(w)=nu(3w)`; no rule using the separate rank `sigma` is used here.

The independent feed at `75b60f4844bf8d096c125817aef2b840f247cecf` reported
finite selected-phase coverage gaps. Its finite coverage percentages and
scale-uniform interpretations are not premises. The whole selected
`w=2 mod3` exclusion below is proved directly from the existing predicates.

### 1. Domain, endpoint, and exact current

Use the absorbed odd Syracuse map `S`, the elementary minimum `nu`, and
`P(w)=[3w]-[w]`. Let `w=5 mod8` and suppose `3w` is selected in the sense of
[R25](../elementary-bridge-quotient-normal-form/README.md). Then

\[
 q=\rho(w)=\nu(3w)=(3w-1)/2=2^A t-1,\qquad A\ge2,
\]

where `t` is odd, `t=-3^A mod4`, and `2^A t=2 mod3`. In particular `q=1
mod3` is a complementary canonical climber. Conversely these conditions on
`A,t` yield the stated selected W5 input `w=(2^(A+1)t-1)/3`.

Write

\[
 d=v_2(3^{A-1}t-1)\ge2,\quad
 u=(3^{A-1}t-1)/2^d,\quad b=\lfloor d/2\rfloor.
\]

The complete [R26 block](../complementary-run-bridges/README.md) has
raw endpoint

\[
 f=\begin{cases}3^b u,&d\text{ odd},\\2\,3^b u+1,&d\text{ even}.
 \end{cases}                                                   \tag{1}
\]

Let `D_q` denote its exact current, with divergence `[q]-[f]`, and let
`N_s` denote the elementary current with divergence `[s]-[nu(s)]`. If
`z=nu(w)` and `m=nu(f)`, the exact formal pair plan is

\[
 J=N_{3w}+D_q+N_f-N_w+H_m-H_z.                    \tag{2}
\]

Here each `H` is the finite formal absorption plan of R41/R43. Its signed
missing W5 requests remain explicit. Thus (2) has divergence `P(w)` minus
the signed sum of those missing pair sources. No intermediate absorption
premise is silently supplied. The constructor combines coefficients before
returning the remaining requests.

For odd `d`, the ordinary merger clocks of `D_q` are `(A+b,1)`; for even
`d` they are `(A+b-1,0)`. The quotient clock from `q` to `m` is always
`A+b-1`. The upper normalizer `N_(3w)` has two ordinary prefixes of length
`A+1`. The lower and endpoint normalizers retain their own explicit prefixes
and, when present, their F-ray rows. These normalizer currents are not zero
ordinary elapsed time. The quotient clock starts at `q`, not at `3w`.

For a canonical `n`, use the proved branchwise upper bound from
[R44](../returning-forward-interface/README.md):

| Canonical endpoint `n` | Bound `B(n)` on every missing request's `rho` |
|---|---:|
| `n=1` | `0` |
| `n=1 mod8`, `n>1` | `(27n+29)/32` |
| `n=3 mod4`, `n=2 mod3` | `(3n+1)/4` |
| `n=3 mod4`, `n=1 mod3` | `n` |
| `3 divides n`, `n/3=5 mod8` | `n` |
| `3 divides n`, `n/3=9 mod16` | `(9n+5)/8` |

Put `B(f)=B(nu(f))`. The general bound `B(f)<=(9nu(f)+5)/8` also holds.
The lower input satisfies `4z<=w-1`, so all its request ranks are already
strictly below `q`. Consequently

\[
                         B(f)<q                              \tag{3}
\]

is sufficient for a strict-`rho` pair reduction. The test is a sufficient
criterion for the formal construction, not a necessary criterion for the
existence of a pair current.

### 2. Complete table for the three smallest initial exponents

Let `E` mean that the even raw endpoint `f` is selected and put `m=nu(f)`.
For each row, (3) holds **if and only if** the displayed condition holds:

| `A` | Complete accepted domain |
|---:|---|
| 2 | `d` odd, or even `d>=4`, or `E` |
| 3 | `d` odd, or even `d>=6`, or `E` |
| 4 | `d` odd, or even `d>=10`, or `E` and (`d>=6` or (`d=4` and `m!=3 mod8`)) |

This includes all three residue classes of `w mod3`. In particular both
selected unit classes are included.

**Proof.** The domain forces `t=11 mod12` for `A=2,4`, hence `t>=11`.
For `A=3`, `t=1 mod12`; its least case `t=1` has `d=3`, so every even-`d`
case has `t>=13`.

For odd `d`, increasing `d` by two multiplies `f` by `3/4`. It suffices to
check the general bound at `d=3`. For `A=2,3,4` respectively,

\[
 q-\frac{9f+5}{8}
 =\frac{175t-77}{64},\quad\frac{269t-77}{64},\quad
 \frac{295t-77}{64}>0.                              \tag{4}
\]

For even `d`, `f=1 mod3` and `f=3 mod4`. If it is not selected it is
canonical and `B(f)=f`. Increasing `d` by two multiplies `f-1` by `3/4`.
At `A=2`, the last failing value is `d=2`, where `f-q=(t+1)/2`, and the
first passing value is `d=4`, where `q-f=(5t-7)/8`. If `f` is selected,
`m=(f-1)/2` is canonical and divisible by3. Its three possible bounds are

\[
 B(f)=\begin{cases}(27m+29)/32,&m=1\pmod8,\\
 (9m+5)/8,&m=3\pmod8,\\m,&m=7\pmod8.
 \end{cases}                                            \tag{5}
\]

The common bound is `(9f+1)/16`; already at `A=2,d=2`,
`q-(9f+1)/16=(47t-25)/32>0`. This proves the first row. The remaining
two rows follow from the same endpoint algebra as the complete A3/A4 table
in [R48](../forward-blocks-low-exponent-tests/README.md), with the valid
minima above. In particular the formerly exceptional `A3,t1` is an odd case
already covered by (4). For clarity, the last failing/first passing raw
differences are `(17t+7)/8` at A3d4, `(13t-37)/32` at A3d6;
`(-139t-175)/128` for `q-f` at A4d8 and `(1631t-781)/512` at A4d10.
At A4d4, (5) separates the passing residues1,7 from the failing residue3;
at A4d2 all three fail. At A4d6 their common upper bound passes. Every
strict sign holds at the stated least `t`, proving exhaustion. ∎

### 3. A complete second block after the failed A2 case

The first A2 case fails exactly when `d=2` and `f` is canonical. Put

\[
 n=f=G(q)=(9q+5)/8=2^B v-1.                         \tag{6}
\]

It is another complementary canonical climber, with `n=1 mod3`. Let its
R26 second depth be `e`, its raw endpoint `y`, and `m=nu(y)`. The exact
two-block current replaces `D_q+N_f` in (2) by
`D_q+D_n+N_y`. The first block uses two ordinary and two quotient arrows;
the second block has ordinary clocks `(B+floor(e/2),1)` for odd `e` and
`(B+e/2-1,0)` for even `e`. Thus the total quotient clock is `B+floor(e/2)+1`.

For `B=2,3,4`, the test `B(y)<q` is completely classified as follows;
`E` now means that `y` is selected.

| `B` | Complete accepted domain after (6) |
|---:|---|
| 2 | `e` odd, or even `e>=4`, or `E` |
| 3 | `e` odd, or even `e>=8`, or `E` and (`e>=4` or `m!=3 mod8`) |
| 4 | `e` odd, or even `e>=10`, or `E` and (`e>=6` or (`e=4` and `m=1 mod8`)) |

**Proof.** The first exact A2d2 condition gives `t=23 mod24`, hence
`q>=91`. Substitute `v=(9q+13)/2^(B+3)` into (1). As before, increasing
`e` by two multiplies `y` (odd `e`) or `y-1` (even `e`) by `3/4`.
The following endpoint differences prove every boundary sign. An entry
`(Lq-C)/D` is `q` minus the bound named in its second column.

| `(B,e)` | Compared bound | Difference |
|---|---|---|
| `(2,3)` | `(9y+5)/8` | `(1319q-1469)/2048` |
| `(3,3)` | `(9y+5)/8` | `(1909q-3991)/4096` |
| `(4,3)` | `(9y+5)/8` | `(1631q-11141)/8192` |
| `(2,2)` | `y` | `(-17q-85)/64` |
| `(2,4)` | `y` | `(13q-319)/256` |
| `(2,2)` | `(9m+5)/8` | `(295q-829)/1024` |
| `(3,6)` | `y` | `(-139q-3479)/2048` |
| `(3,8)` | `y` | `(1631q-12485)/8192` |
| `(3,2)` | `(27m+29)/32`, `(9m+5)/8`, `m` | `(1631q-11717)/8192`, `(-139q-2711)/2048`, `(13q-159)/256` |
| `(3,4)` | `(9m+5)/8` | `(1631q-9413)/8192` |
| `(4,8)` | `y` | `(-3299q-34447)/16384` |
| `(4,10)` | `y` | `(6487q-119725)/65536` |
| `(4,2)` | `(27m+29)/32`, `(9m+5)/8`, `m` | `(-3299q-32911)/16384`, `(-2465q-8581)/4096`, `(-217q-669)/512` |
| `(4,4)` | `(27m+29)/32`, `(9m+5)/8`, `m` | `(6487q-113581)/65536`, `(-3299q-28303)/16384`, `(-139q-2007)/2048` |
| `(4,6)` | `(9m+5)/8` | `(6487q-95149)/65536` |

All positive cases are positive already at `q=91`; all negative cases are
negative for positive `q`. Formula (5) and the `3/4` comparison exhaust
all even depths. ∎

This avoids an exact undo trap. At a failed first block, the complete
R46 inverse spine at `n` has `D=1,j=1` and returns `q`, and its current
is exactly `-D_q`. Recognizing a higher-rank request through that inverse
therefore restores the original obligation. The forward second block above
is tested against the original `q`, before requesting any absorption input.

### 4. Full new arithmetic domains

#### 4.1 The previously uncovered selected unit class

If selected `w=2 mod3`, then `q=7 mod9`. The R46 inverse classification
therefore has `D=v3(q-1)=1`, unit `(q-1)/3=2 mod3`, spine value
`4(q-1)/3+1`, and final point depth `j=0`. R46 requires `j>=2`.
R41/R44/R52 require `3|w`; R45/R47/R48/R50/R53 require nonselected `3w`.
Thus **every selected `w=2 mod3` is outside all nine earlier direct rule
domains**. This is a statement about those predicates, not about absence of
other currents or about the separate sigma dispatcher.

For every `A>=2` choose odd `d>=3` such that

\[
 2^d(2^{A+3}-13)>9\,3^{(d-1)/2}(3^{A-1}-1).          \tag{7}
\]

Such `d` exist: increasing `d` by two multiplies the left/right ratio by
`4/3`. Specify `t` by the complete coprime CRT cylinder

\[
 t\equiv(1+2^d)3^{1-A}\pmod {2^{d+1}},\qquad
 t\equiv7\,2^{-A-1}\pmod9.                           \tag{8}
\]

The extra binary bit fixes the exact depth. The first congruence gives
`t=-3^A mod4`; the second gives the required integrality and `w=2 mod3`.
Every positive solution has exactly the prescribed `A,d`. Inequality (7)
is the general endpoint test at `t=1`; its coefficient of `t` is positive
(use `13*2^d>9*3^((d-1)/2)`), so it proves `(9f+5)/8<q` for every solution.
The seed period is `3*2^(A+d+2)`. This is a nonempty accepted arithmetic
family for every first exponent A, wholly outside all old nine predicates.

Examples are

\[
  w\equiv221\pmod{384}\quad(A,d)=(2,3),\qquad
  w\equiv29\pmod{1536}\quad(A,d)=(2,5).              \tag{9}
\]

The complete two-block table adds, for example,

\[
                 w\equiv2813\pmod{3072}.             \tag{10}
\]

Indeed set `v=1187+1296j`; then
`n=4v-1`, `q=(32v-13)/9`, and `w=(64v-17)/27` give the first failed
`(A,d)=(2,2)` and second `(B,e)=(2,3)`. This is again selected `w=2 mod3`,
so the whole progression is new to the old nine domains.

#### 4.2 A full subphase of the R54 obstruction

The [R54 untouched phase](../growing-prefix-unhandled-leading-input/README.md) is
`w=3456k-11`, `k>=1`, hence `q=5184k-17`. It has `A=4` and

\[
                  d=2+v_2(2187k-7).                  \tag{11}
\]

When `k=3 mod4`, the valuation on the right is exactly1. Thus every

\[
                   w\equiv10357\pmod{13824}          \tag{12}
\]

has `A4,d3` and is accepted. This whole progression has `w=1 mod3` and
was outside all nine earlier direct domains by R54. For this case
`f=(81q+33)/128`, so the generic bound gives
`q-(9f+5)/8=(295q-937)/1024>0`. No assertion is made that the full
phase `3445 mod3456` is resolved by (12).

An early candidate incorrectly replaced `10357` by `3445` in (12).
That claim is refuted: `w=58741` has A4d4 and nonselected endpoint 167275,
larger than its rank 88111; `w=86389` has A4d4, selected endpoint 246007,
and minimum `123003=3 mod8`, whose bound 138379 exceeds rank 129583. Both lie
in `3445 mod13824`. The checker retains these counterexamples. At `w=3445`
itself the first depth is4, not3; that individual input passes the selected
minimum1-mod8 branch. The corrected progression (12) uses the exact
valuation established from (11).

### 5. Reusable interface and verification

`selected_forward.py` provides:

- `parameters(w)`: exact selected canonical upper source and block parameters.
- `forward_plan(w)`: complete one-block formal current and its rank status.
- `two_block_plan(w)`: complete second block after the failed A2d2 case.
- `one_step(w)` / `recognized(w)`: first accepted one-block plan, then the
  two-block plan where applicable; otherwise no recognized rule.
- `long_family(A,index,d=None)`: the complete CRT family (8).
- `compile_plan(plan,supplied)`: validates and substitutes exact supplied
  currents for every remaining signed W5 premise.

The construction is finite: no unrestricted orbit search occurs in these
APIs. Increasing the first exponent makes explicit prefix lengths grow;
there is no universal fixed exposure depth claim. Both complete tables
classify the specified endpoint-bound test, not every possible cancellation
in the resulting signed input list.

Run `python3 experiments/residual_progress/selected_forward/check_selected_forward.py`.
The stored receipt checks all 2049 selected W5 inputs below 32768, including
256 failed A2d2 first blocks and their two-block continuations. It verifies
683 whole-unit-class instances excluded by the old nine predicates, 905
newly recognized inputs in that finite window, 78 CRT examples through
first exponent 128, and 128 points in the four displayed progressions.
It also checks every displayed affine difference, the two refuted-phase
counterexamples, seven invalid-call rejections, and four actual substitutions
using nine supplied pair currents. Two resulting full current tables and
their supplied inputs are retained in the receipt. These finite counts are
not scale-uniform coverage claims. The small fixture inputs are
discovered under explicit step/bit caps; the theorem does not depend on
their finite absorption tests. The full repository gate belongs to the
integrating parent batch.

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B11 migration; standard library). The legacy scripts in this folder load their sibling modules by pre-migration folder names, so they no longer run here. This certificate rebuilds the legacy directory layout in a temporary directory from the node folders that now hold those files, runs the unmodified legacy checks there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied receipt unchanged. It writes nothing in the repository. It replays: the legacy checker `check_selected_forward.py` (about 12 s; the counts of section 5 and two stored outputs, compared with `selected_forward_audit.json`). The command in the legacy text names `experiments/residual_progress/selected_forward/`.

## Remarks

- The legacy note read the side-lane feed at `75b60f4` (finite selected-phase coverage gaps) as context; its percentages are not premises.
- First in priority among the three selected rules of [`twelve-family-rho-dispatcher`](../twelve-family-rho-dispatcher/README.md); the side lane's sample attributes most of that dispatcher's growth (to about 70% of sampled `W5`) to this rule. Novelty undetermined (none claimed).

## History

- Migrated from `experiments/residual_progress/selected_forward/SELECTED_FORWARD.md` (legacy ID R55) at commit `be73a66`, by the B11 migration (Claude, Opus 5.5). Note, scripts and receipts moved byte-identical; `check_legacy_replay.py` was added at the migration. Legacy status: "written full conditional interfaces, complete low-exponent tests and infinite decreasing arithmetic domains".
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `7206f9c`. The batch's "independent model" proof and code reviews (archive/convergence-residual-progress/REPORT.md) were the main lane's own agents, not a different lane.
