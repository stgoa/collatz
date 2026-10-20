---
id: critical-nine-elimination
kind: result
title: Complete critical-nine elimination leaves the W5 tripling pairs as the only sufficient pair class
status: written
claim: >
  Odd-only 3x+1 map S on positive odd integers, absorbing at 1, killed atom [1] = 0; P(w) = [3w] - [w], W5 = {w
  = 5 mod 8}, W9 = {w = 9 mod 16}. For every w in W9 there is an explicitly computed finite integer current J_w
  and finitely supported signed integer coefficients c_w(u), supported on W5, with div J_w = P(w) - sum c_w(u)
  P(u) and c_w(u) != 0 only for u <= (9w+3)/4; the algorithm terminates without absorption search or
  hypothetical currents, and missing or invalid inputs are rejected at substitution. Consequently every positive
  odd integer reaches 1 iff every w in W5 has a finite exact current for P(w) (an existence equivalence with a
  finite conditional compiler; no algorithm supplying the W5 premises and no decreasing induction within W5 is
  asserted). The only possible nondecreasing request is one positive W5 input on d = v2(9w-1) in {4, 6, 8} when
  3z is noncanonical, with values (9w+3)/4, (27w+13)/16, (81w+55)/64. The identities use 3x+1 specifically; no
  novelty is claimed.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [critical-tripling-domain-equivalence, elementary-bridge-quotient-normal-form]
certificates: [check_legacy_replay.py]
evidence:
  - "check_w9_closure.py, w9_closure.py, w9_closure_audit.json, w9_inputs.json, w9_current.csv: the legacy compiler (local_plan, five_plan, compile_five_plan) and checker: 4096 local identities for w = 9 mod 16 below 65536, the low-valuation affine table, 4096 sharper tripling bounds, 616 exact high-valuation cases (4 <= d <= 80), 256 recursive reductions, 10 actual substitutions with capped demonstration inputs and four rejection cases; the w = 9 fixture stores its inputs and 45-row current. Fails at its new path: w9_closure.py loads ../tripling_equivalence/tripling.py (now ../critical-tripling-domain-equivalence/) by its pre-migration folder name; w9_closure.py is itself loaded by its old path by the later legacy critical_inverse/, finite_centres/ and all_ray_continuation/ code. Passed at be73a66 as experiments/residual_progress/w9_closure/check_w9_closure.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran every residual-progress step before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a); replayed unchanged, with its receipt, by check_legacy_replay.py"
  - "batch_r40_r41_check.py, batch_r40_r41_check.json: side-lane probe (Claude side lane, 2026-10-17) of the R37 planner as restated here, the sharper tripling bound, and the R41 ancestor identity and inverse barrier (decreasing-w5-phase-inverse-barrier). Fails at its new path: it imports affine_controls from experiments/packet_currents/negative_controls/ by repository-relative path (now ../locally-collatz-like-control-barrier/) and fibre_count_check from its own folder (now ../absorbed-fibre-uniform-counts/). Passed at be73a66 as reviews/side_lane/batch_r40_r41_check.py (archive/legacy-checker-run-be73a66.md, exit 0); its receipt is reproduced byte for byte by check_legacy_replay.py"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-17
    link: batch_r40_r41_check.py
    scope: "Finite only (side-lane feed entry 2026-10-17 21:53, VERIFIED, main 4a45eb0; the R40 part), rebuilt from the text of section 2 with the lane's own nu and Syracuse step: the R37 planner as restated in section 2 terminates for all 99,999 odd x < 200000, every request lies in W5 u W9, requests strictly decrease and u <= (2x+1)/3; the sharper tripling bound (every index in I(3z) u I(z) is at most (3z+1)/2) holds for all odd z < 60000. The entry says: The full R40 elimination compiler, with its per-d local identities, was not independently rebuilt here. The status stays written"
aliases: [R40]
tags: [convergence, outer-residual, tripling-pairs, critical-domain, collatz-equivalent, conditional-compiler]
---

# Complete critical-nine elimination leaves the W5 tripling pairs as the only sufficient pair class

## Statement

Odd-only clock, `S(x) = (3x+1)/2^v2(3x+1)` on positive odd integers, 1 absorbing, killed atom `[1] = 0`, `F(x) = 4x+1`, `P(w) = [3w] − [w]`, `W5 = {w ≡ 5 (mod 8)}`, `W9 = {w ≡ 9 (mod 16)}`. The elementary normal form `ν` is that of [`elementary-bridge-quotient-normal-form`](../elementary-bridge-quotient-normal-form/README.md) and the decreasing critical plans `H_x`, `I_x` are those of [`critical-tripling-domain-equivalence`](../critical-tripling-domain-equivalence/README.md).

1. **Elimination.** For every `w ∈ W9` there is an explicitly computed finite integer current `J_w` and finitely supported signed integers `c_w(u)`, supported on `W5`, with `div J_w = P(w) − Σ c_w(u) P(u)` and `c_w(u) ≠ 0 ⇒ u ≤ (9w+3)/4`. The algorithm terminates without absorption search or hypothetical current; supplied exact inputs give an exact current for `P(w)`, and missing or invalid inputs are rejected.
2. **Equivalence.** Every positive odd integer reaches 1 iff every `w ∈ W5` has a finite exact current for `P(w)`. This is an existence equivalence with a finite conditional compiler, not an algorithm supplying the `W5` premises or a decreasing induction within `W5`.
3. **Shape of the requests.** With `d = v2(9w − 1) ≥ 4`, odd `d` gives only smaller critical inputs; even `d` gives requests below `w` except one positive `W5` input `u* = 4z+1` when `3z` is noncanonical, with values `(9w+3)/4`, `(27w+13)/16`, `(81w+55)/64` at `d = 4, 6, 8`. The exceptional parameter `z` has ternary unit 2, outside the odd-`h` parameterization of [`odd-h-pair-interface-compiler`](../odd-h-pair-interface-compiler/README.md).

The identity at `w = 9` retains `P(21) − P(5)` and cannot justify a circular rule for `P(21)`; at `w = 1561` exact signed cancellation removes every premise (a finite example only). Neither universal `W5` supply nor convergence is proved.

## Proof

The legacy note "Eliminating the complete critical-nine domain" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written proof and finite executable conditional compiler.** This
eliminates one entire remaining pair domain. It does not construct the
critical-five input currents, prove their universal existence, or claim novelty.
All clocks below are odd-only Syracuse clocks, with 1 absorbing.

Write `S(x)=(3x+1)/2^v2(3x+1)`, `F(x)=4x+1`, and use killed atoms `[1]=0`.
The divergence of row `e_x` is `[x]-[S(x)]`. Set

\[
P(w)=[3w]-[w],\qquad
W_5=\{w>0:w\equiv5\pmod8\},\quad
W_9=\{w>0:w\equiv9\pmod{16}\}.
\]

The elementary normal form `nu` and its exact finite currents are from
[R25](../elementary-bridge-quotient-normal-form/README.md). The finite decreasing
critical plans are from
[R37](../critical-tripling-domain-equivalence/README.md). All input currents in
this note are finite signed **integer** currents with exact divergence.

### 1. Complete-domain elimination and its scope

**Theorem.** For every `w in W9`, there is an explicitly computed finite integer
current `J_w` and finitely supported integer coefficients `c_w(u)`, supported
on `W5`, such that

\[
\operatorname{div}J_w
  =P(w)-\sum_{u\in W_5}c_w(u)P(u),
\qquad c_w(u)\ne0\Longrightarrow u\le{9w+3\over4}. \tag{1}
\]

The algorithm producing this formal identity terminates without an absorption
search or any hypothetical current. If exact currents for all its nonzero
inputs are supplied, substitution produces an exact current for `P(w)`.
Missing or invalid inputs are rejected.

Consequently the following assertions are equivalent:

1. Every positive odd integer reaches 1.
2. For every `w in W5`, a finite exact current for `P(w)` exists.

For `2 => 1`, (1) supplies every `W9` input, and the R37 critical-domain theorem
applies to `W5 union W9`. Conversely, absorption currents for `3w` and `w`
give their difference. This is an existence equivalence with a finite
conditional compiler. It does **not** assert an algorithm supplying the
universal `W5` premises, or a decreasing induction within `W5` itself.

The proof is a local identity followed by strong induction on the unresolved
`W9` index. We give all bounds, including the possible larger `W5` request.

### 2. Finite formal critical plans and a sharper endpoint bound

For any positive odd `x`, R37 computes a finite current `H_x` and a list
`I_x` of missing critical indices, each in `W5 union W9`, satisfying

\[
\operatorname{div}H_x=[x]-\sum_{u\in I_x}P(u). \tag{2}
\]

At each step it first replaces `x` by its elementary minimum `q=nu(x)`.
If `q=1`, it stops. If `q=1 mod8`, it takes its strictly decreasing ordinary
arrow. If `q=2 mod3`, it uses the strictly smaller inverse predecessor
`(2q-1)/3`. Otherwise `q` is complementary canonical and the requested index
and next seed are both

\[
u=q/3\quad(q=0\bmod3),\qquad
u=(2q+1)/3\quad(q=1\bmod3).
\]

Each seed strictly decreases. Thus the process terminates and every requested
index satisfies `u <= (2x+1)/3`. Its requested list is strictly decreasing;
subtracting two lists nevertheless requires retaining both signs and any
equal-index cancellations.

**Sharper tripling bound.** Every index in `I_(3z) union I_z`, for any odd
positive `z`, is at most `(3z+1)/2`.

* If `3z` is complementary canonical, its first request is `z`, and all later
  requests are at most `(2z+1)/3`.
* If `3z` is noncanonical, `nu(3z) <= (3z-1)/2`, so all requests are at most `z`.
* If `3z=1 mod8`, its first ordinary arrow, with valuation exactly 2, reaches
  `(9z+1)/4`. The generic bound for that seed is `(3z+1)/2`.

These exhaust all cases. The generic bound for `I_z` is smaller as well.
This sharper estimate, rather than the generic estimate for `3z`, is needed
for the factor-one-half conclusion below.

### 3. The full `W9` run identity

Fix `w=9 mod16` and put `d=v2(9w-1) >= 4`. On `3w` the first two valuations
are `(1,2)`; on `w` they are `(2,1)`. Their endpoints are

\[
S^2(3w)=3v-2,\qquad S^2(w)=v,
\qquad v={9w+7\over8}. \tag{3}
\]

For `v=1 mod8`, both endpoints in this pair have valuation 2 and

\[
(3v-2,v)\longmapsto(3v'-2,v'),\qquad v'={3v+1\over4}. \tag{4}
\]

Since `v2(v-1)=d-3`, (4) can be iterated exactly until that valuation is 1 or 2.
Let `Gamma_w` be the difference of the two prefix currents of length `k+2`
specified below. Its divergence is `P(w)` minus the endpoint pair.

#### 3.1 Odd `d=2k+5`, `k>=0`

Set

\[
C={9w-1\over2^{2k+5}},\qquad z=3^kC.
\]

After the prescribed `k+2` arrows the endpoints are `(F(3z),F(z))`.
The explicit sibling current

\[
E_z=e_{F(3z)}-e_{3z}-e_{F(z)}+e_z
\]

has divergence `[F(3z)]-[F(z)]-P(z)`, including the killed-1 convention.
Consequently

\[
\operatorname{div}(\Gamma_w+E_z+H_{3z}-H_z)
 =P(w)-\sum_{u\in I_{3z}}P(u)+\sum_{u\in I_z}P(u). \tag{5}
\]

Here `32z <= 9w-1`, so every requested index obeys

\[
u\le{3z+1\over2}\le{27w+29\over64}<{w\over2}; \tag{6}
\]

the last inequality holds for every `w>=9`. Thus **every odd-valuation
branch** has only smaller critical inputs, for all valuations and phases.

#### 3.2 Even `d=2k+4`, `k>=0`

Set

\[
C={9w-1\over2^{2k+4}},\quad z=3^kC,\quad
J(z)=[6z+1]-[2z+1].
\]

The endpoints after `k+2` arrows are exactly `(6z+1,2z+1)`, so

\[
\operatorname{div}(\Gamma_w+H_{6z+1}-H_{2z+1})
 =P(w)-\sum_{u\in I_{6z+1}}P(u)+\sum_{u\in I_{2z+1}}P(u). \tag{7}
\]

The integer relation `2^(2k+4) C+1=9w` gives

\[
C\equiv-2^{-(2k+4)}\pmod9,\qquad C\equiv2\pmod3,
\quad v_3(z)=k. \tag{8}
\]

In particular `z>=5` and `16z <= 9w-1`. These ternary restrictions are part
of the actual domain; arbitrary `z` cannot be substituted.

##### The upper canonical case

If `3z` is canonical, `6z+1` is its elementary selected partner and its
missing list is `I_(3z)`. The sharper bound above applies to it.

For the lower endpoint, if `z` is canonical, its list is `I_z`. Otherwise
`2z+1` is complementary canonical. If `k=0`, (8) gives `z=2 mod3`; the first
inverse step goes to `(4z+1)/3` and all requests are at most `(8z+5)/9`.
If `k>=1`, then `z=0 mod3`, and the first request is `(4z+3)/3`, with all
later requests smaller. In either case every lower request is at most
`(3z+1)/2`, since `z>=5`.

Thus in this entire case every request satisfies

\[
u\le{3z+1\over2}\le{27w+13\over32}<w. \tag{9}
\]

##### The upper noncanonical case and the only possible expansion

If `3z` is noncanonical, `6z+1` is complementary canonical and equals 1
modulo 3. Its first requested index is

\[
u_*=4z+1\in W_5. \tag{10}
\]

The remaining upper list is exactly `I_z`, because `nu(F(z))=nu(z)`.
Every remaining upper request is at most `(2z+1)/3`. The lower list has the
same bounds just proved: if `z` is canonical it is `I_z`; otherwise it is
bounded by `(8z+5)/9` at `k=0` or `(4z+3)/3` at `k>=1`.

All these other indices are strictly less than both `w` and `u_*`. For
example `(4z+3)/3 <= (9w+11)/12 < w` for `w>=9`. Hence after exact signed
cancellation `u_*` remains with coefficient **+1**, and it cannot be canceled
by any lower or subsequent upper request. If `z` is canonical, the two
remaining lists cancel completely, leaving just `P(u_*)`.

For `k>=3`, (10) is also strictly smaller than `w`, since

\[
u_*<w\quad\Longleftrightarrow\quad
\bigl(2^{2k+4}-36\,3^k\bigr)C>8. \tag{11}
\]

At `k=3` the parenthesized integer is 52. It strictly increases thereafter:
the next value is four times the current value plus `36*3^k`. Since `C>=1`,
(11) follows for every `k>=3`.

The only possible nondecreasing request is therefore the following single
positive `W5` input, and it occurs precisely when `3z` is noncanonical:

| `d` | `k` | `z` | larger input `u_*` |
|---|---|---|---|
| 4 | 0 | `(9w-1)/16` | `(9w+3)/4` |
| 6 | 1 | `3(9w-1)/64` | `(27w+13)/16` |
| 8 | 2 | `9(9w-1)/256` | `(81w+55)/64` |

Each displayed `u_*` exceeds `w`; every other request is strictly smaller.
The rows apply to their exact valuation and canonical conditions, not every
integer in the displayed affine formula. The actual ternary unit is 2, so
these exceptions are outside R38's odd-`h` parameterization with ternary
unit 1. Reversing that parameterization cannot certify them.

### 4. Strong induction and an exact finite input bound

Equations (5) and (7) have the common form

\[
\operatorname{div}L_w=P(w)-\sum_{u\in W_5\cup W_9}b_w(u)P(u). \tag{12}
\]

Every `W9` child is smaller than `w`. Every child, including a possible
expanding `W5` child, is at most `(9w+3)/4`. Replace each `W9` child by its
own identity (12), multiplying **all** its rows and coefficients by the
signed parent coefficient. Each branch terminates by strict descent of a
positive integer `W9` parameter. Finite branching makes the expansion finite.
The bound on final `W5` inputs survives, since every recursively expanded
`W9` index is at most the original `w` and `(9w+3)/4` increases with `w`.
This proves (1), including exact multiplicities and signs.

This is not a claim that (12) decreases the full critical index on every
branch: the table contains the precise exceptions. Nor may a separate rule
for those `W5` inputs simply be appended to obtain termination without a new
rank proof. For example, the exact local formal request for `w=9` is

\[
P(9)=\operatorname{div}L_9+P(21)-P(5). \tag{13}
\]

The larger obligation `P(21)` is retained. A rule returning it to `P(9)`
would create a dependency loop; it would not prove either current exists.

Signed cancellations can also remove every premise in an individual case.
For example, recursively expanding the indices `1561,73,41,9` produces the
following nine-row current with divergence exactly `P(1561)`:

\[
e_{247}+e_{4683}+e_{5269}+e_{7025}
-e_{659}-e_{989}-e_{1171}-e_{1561}-e_{1757}. \tag{14}
\]

This finite certificate uses no supplied pair input. It illustrates why
signed coefficients must be combined exactly; it is not universal coverage.

### 5. Reproduction and saved evidence

`w9_closure.py` provides `local_plan(w)`, `five_plan(w)`, and
`compile_five_plan(data, supplied)`. Formal plans expose signed coefficients;
they never treat their missing leaves as actual currents. The compiler checks
every exact input divergence and rejects missing or malformed inputs.

Run:

```sh
python3 experiments/residual_progress/w9_closure/check_w9_closure.py
```

The checker records exact local identities, the child bounds, finite recursive
elimination, cap/input rejection, and a small separately capped set of actual
input substitutions. The latter are finite examples and are not used in the
universal written proof. The JSON receipt records the tested domains and
certificate hashes; the saved small current/input fixture allows an explicit
compiled identity to be inspected. No universal input-current construction
is supplied.

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B11 migration; standard library). The legacy scripts in this folder load their sibling modules by pre-migration folder names, so they no longer run here. This certificate rebuilds the legacy directory layout in a temporary directory from the node folders that now hold those files, runs the unmodified legacy checks there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied receipt unchanged. It writes nothing in the repository. It replays: the legacy checker `check_w9_closure.py` (about 5 s; the counts in the Statement's last paragraph and in section 5 of the note, compared field by field with `w9_closure_audit.json`, `w9_inputs.json` and `w9_current.csv`) and the side-lane probe `batch_r40_r41_check.py` (about 6 s, receipt reproduced byte for byte). The command in the legacy text names `experiments/residual_progress/w9_closure/`.

## Remarks

- **What uses it.** The `W5`-only formal absorption plans of [`decreasing-w5-phase-inverse-barrier`](../decreasing-w5-phase-inverse-barrier/README.md) and every later critical-pair rule expand `W9` requests through this compiler; [`critical-image-rank-composition`](../critical-image-rank-composition/README.md) bounds its requests in the rank `ρ(w) = ν(3w)`, and [`rank-excess-absorption-classification`](../rank-excess-absorption-classification/README.md) classifies exactly when a request exceeds the seed.
- **The remaining premise** is the open question [`universal-w5-tripling-currents`](../../questions/universal-w5-tripling-currents.md).
- **Side-lane check of the R37 planner.** The same probe also checks the planner of [`critical-tripling-domain-equivalence`](../critical-tripling-domain-equivalence/README.md) as restated here; that node records it under `reviewed_by`.
- Novelty undetermined (none claimed).

## History

- Migrated from `experiments/residual_progress/w9_closure/CRITICAL_NINE_ELIMINATION.md` (legacy ID R40) at commit `be73a66`, by the B11 migration (Claude, Opus 5.5). Note, scripts and receipts moved byte-identical; `check_legacy_replay.py` was added at the migration. The side-lane probe `reviews/side_lane/batch_r40_r41_check.*` moved here. Legacy status: "written proof and finite executable conditional compiler".
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `4a45eb0`. The batch's "independent model" proof and code reviews (archive/convergence-residual-progress/REPORT.md) were the main lane's own agents, not a different lane.
- Before the commit, a main-lane model review caught a transcription error in the `d = 8` row of section 3: its intercept is 55, not 175 (archive/convergence-residual-progress/REPORT.md); the note was corrected and 2688 direct affine-row checks were added. The migrated text has 55.
