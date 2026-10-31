---
id: affine-common-tail-tree-lifting
kind: result
title: Finite common-tail Syracuse trees lift to affine families of exact currents, and one such family packs into every large annulus
status: reviewed
claim: >
  Odd-only 3x+1 map. (Compiler) For a finite directed tree of positive odd states with common sink w, exact
  edge valuations a_x, d_x edges and A_x total valuation from x to w, and D = max d_x, the states
  x(t) = x + 2^(A_x+1)·3^(D−d_x)·t form, for every integer t ≥ 0, a tree of actual Syracuse edges with the same
  exact valuations; routing integer source weights of total m gives μ_t = (I − P)J_t + m·δ_(w(t)) (sink term
  dropped when w(t) = 1), so zero mass gives an exact current for every t. (Family) The five-source tree from
  A_96, μ_t = −δ_(4591+384t) − δ_(6121+512t) + δ_(6887+576t) + 2δ_(10331+864t) − δ_(13775+1152t), has an exact
  current of positive cost 3; with t = 9s + r, r ∈ {0, 3}, it lies in the annulus A_N (8 | N) exactly when
  96 + 72s ≤ N ≤ 120 + 96s (r = 0) or 120 + 72s ≤ N ≤ 152 + 96s (r = 3); the ten source progressions are
  pairwise disjoint, so all C(N) = N/144 + O(1) admissible copies can be removed together, for every allowed
  N with 96 ≤ N ≤ 152 or N ≥ 168 (none at N = 160). Coverage of actual annuli is a separate check from the
  identity. Removes positive mass N/48 + O(1) of 99N/4; no complete constructor.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [disjoint-annular-recursion, orbit-component-current-criterion, finite-current-certificate-identity]
certificates: [check_stored_annular_currents.py, check_legacy_replay.py]
evidence:
  - "affine_template_compiler.py, affine_templates.json: the legacy compiler; checks both compiled identities at arbitrary-size integer parameters, the linear band bounds on selected scales through 64^20, all 45 progression-capacity checks, and every allowed cutoff from 8 through 4096 for the summed two-class family. Fails at its new path: it imports annular_components from its own folder, which loads experiments/current_construction/recursive/check_annular_recursion.py and experiments/current_construction/obstructions/verify_obstructions.py relative to the repository root (now ../disjoint-annular-recursion/ and ../orbit-component-current-criterion/). Passed at be73a66 as experiments/annular_construction/components/affine_template_compiler.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran these steps before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a). Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
  - "annular_components.py, check_annular_components.py, annular_component_audit.json and the four annular_*.csv tables: the capped incremental constructor and its audit driver (the six component diagnostics, the finite work witnesses and the stored A_96 and A_168 currents). Fail at their new paths for the same reason; passed at be73a66 inside scripts/verify_all.py, as above. Later residual-progress scripts load annular_components.py and affine_template_compiler.py by their legacy paths. Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
reviewed_by:
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Full argument re-derived (compiler theorem, tree data, coverage intervals, capacity, counting, work witnesses, two-row family) with independent code: the identity at 600 parameters and large t, admissibility over all t for every 8 | N <= 4096, the stored A_96 and A_168 currents, and the compiler on 3x+5 and 3x+13 trees (d-uniform); both certificates re-run (PASS, exit 0, under 1 s and 5 s). Verdict HOLDS; one gap-level imprecision (why only t = 0, 3 mod 9 are admissible) supplied in the review, no correction"
aliases: [R8-b]
tags: [convergence, packet-currents, annular, affine-lifting, partial-current, finite-certificate]
---

# Finite common-tail Syracuse trees lift to affine families of exact currents, and one such family packs into every large annulus

## Statement

The source measure is the annulus `A_N = Π^R_(64N) − Π^R_N`, `8 | N`, of [`disjoint-annular-recursion`](../disjoint-annular-recursion/README.md); odd-only clock, absorbing at 1.

**Theorem (affine compiler).** Consider a finite directed tree of positive odd Syracuse states with a common sink `w`. Each non-sink edge `x → y` has its exact valuation `a_x ≥ 1`, so `3x + 1 = 2^(a_x)·y`. Let `d_x` and `A_x` be the number of edges and the total valuation from `x` to `w`, and `D = max_x d_x`. For every integer `t ≥ 0` define

```
x(t) = x + 2^(A_x+1)·3^(D−d_x)·t.
```

Then every lifted edge is an actual Syracuse edge with the same exact valuation, `3x(t) + 1 = 2^(a_x)·y(t)`. Route finite integer source weights along the tree to `w`, producing signed current weights `J(x)`. If the source total is `m`, the same weights on the lifted tree give

```
μ_t = (I − P)J_t + m·δ_(w(t)),
```

with the sink term discarded when `w(t) = 1`. Zero source mass gives an exact current for every `t ≥ 0`; negative source mass gives a nonpositive residual. The positive current cost is at most `Σ_x max(J(x), 0)`.

**Theorem (five-source family).** The identity

```
μ_t = −δ_(4591+384t) − δ_(6121+512t) + δ_(6887+576t) + 2δ_(10331+864t) − δ_(13775+1152t) = (I − P)J_t
```

holds for every integer `t ≥ 0`, with the exact current of the table in the proof (positive cost 3), so `H_L(μ_t) ≤ 3` at every horizon and parameter, without following the common sink. For `t = 9s + r`, `s ≥ 0`, `r ∈ {0, 3}`, and `8 | N`, the five sources carry exactly these coefficients in `A_N` if and only if

```
r = 0:   96 + 72s ≤ N ≤ 120 + 96s;        r = 3:   120 + 72s ≤ N ≤ 152 + 96s.
```

The ten source progressions are pairwise disjoint, so all admissible copies can be removed simultaneously. With `C(N) = |I_0(N)| + |I_3(N)|`, where

```
I_0(N) = {s ≥ 0 : ceil((N−120)/96) ≤ s ≤ floor((N−96)/72)},
I_3(N) = {s ≥ 0 : ceil((N−152)/96) ≤ s ≤ floor((N−120)/72)},
```

the sum `M_N` of the copies has a finite current `K_N` with `M_N = (I − P)K_N`, `|supp M_N| = 5C(N)`, `‖M_N⁺‖₁ = 3C(N)` and `‖K_N⁺‖₁ ≤ 3C(N)`. The remainder `A_N − M_N` is `A_N` with those atoms deleted; its positive mass is `99N/4 − 3C(N)`. `C(N) = N/144 + O(1)`; copies exist for every multiple of 8 with `96 ≤ N ≤ 152` or `N ≥ 168`, and `N = 160` has none.

## Proof

From §§2–3 of the legacy note `AFFINE_COMPONENTS.md`, kept as written.

**Compiler.** Write the slope as `v_x = 2^(A_x+1)·3^(D−d_x)`. For every edge, `d_x = d_y + 1` and `A_x = a_x + A_y`, whence `3v_x = 2^(a_x)·v_y`. Therefore `3x(t) + 1 = 2^(a_x)·y(t)`. Every `y(t)` is odd, so the valuation remains **exactly** `a_x`, and all lifted edges are actual Syracuse edges. At a sink originally equal to 1 the lifted sink can exceed 1; no continuation from that sink is used. Any coincident lifted states are combined; linearity preserves the identity. ∎

This turns one finite tree into an infinite family of exact identities. It does **not** assert that the lifted source coefficients occur in an actual annular measure; that coverage check is separate and essential.

**The five-source tree.** The five sources found at `N = 96` (below) have common sink 17435. Their relevant paths are

```
6121 → 4591 → 6887 → 10331 → 15497 → 11623 → 17435
13775 → 20663 → 30995 → 46493 → 17435
```

The maximum path length is six. The compiler gives the identity above with this exact current; a row `(x, v, c)` means current coefficient `c` at the state `x + vt`:

| x | v | c |
|---:|---:|---:|
| 4591 | 384 | −2 |
| 6121 | 512 | −1 |
| 6887 | 576 | −1 |
| 10331 | 864 | 1 |
| 11623 | 972 | 1 |
| 13775 | 1152 | −1 |
| 15497 | 1296 | 1 |
| 20663 | 1728 | −1 |
| 30995 | 2592 | −1 |
| 46493 | 3888 | −1 |

The positive current cost is 3.

**Coverage.** The first three source states must lie in band 4, `(36N, 72N)`, and the last two in band 5, `(72N, 144N)`. Their residues modulo 18 are `(1, 1, 11, 17, 5)` for `r = 0` and `(1, 7, 11, 17, 5)` for `r = 3`. Both give exactly the required coefficients `(−1, −1, 1, 2, −1)` from the annular table. The largest lower bound on `N` comes from the last source (and agrees after integer rounding with the third source); the smallest upper bound comes from the first source. For `r = 0` these give `96 + 72s ≤ N ≤ 127 + 96s`, and for `r = 3` they give `120 + 72s ≤ N ≤ 159 + 96s`; restricting `N` to multiples of eight gives the displayed endpoints. The other three bounds are weaker for every `s ≥ 0`.

**Capacity.** There are ten source progressions, with offsets `x_i + r·v_i` and periods `9v_i`. For each pair of different progressions, `gcd(9v_i, 9v_j)` does not divide the offset difference (45 exact integer checks). Consequently the progressions have no common integer state, even if their parameters differ, and no annular source coefficient is used twice.

**Counting.** For the eventual claim, the `r = 0` intervals with `s ≥ 2` overlap and cover all multiples of eight from 240 onward, while the `s = 1` intervals cover 168 through 248. So this is a universal partial construction for every sufficiently large allowed cutoff, not merely the scale line `N = 96(1 + s)`. Its removed positive mass is asymptotically `N/48`, about `1/1188` of the annulus's full positive mass. ∎

## Certificates

[`check_stored_annular_currents.py`](check_stored_annular_currents.py) (written at the migration, about 1 s, standard library, self-contained). It checks the five-source identity `μ_t = (I − P)J_t` at `t = 0, …, 199` and at three very large `t`; the 45 pairwise gcd tests; the stored nonpositive-residual current for `A_96` ([`annular_96_aggregate_one_sided.csv`](annular_96_aggregate_one_sided.csv), residual [`annular_96_aggregate_one_sided_residual.csv`](annular_96_aggregate_one_sided_residual.csv): `−2δ_8959 − δ_10919 − δ_11291`) and the stored exact current for `A_168` ([`annular_168_aggregate_exact.csv`](annular_168_aggregate_exact.csv)), each against `A_N` rebuilt from the six-band table; and the work witnesses `H_53(A_96) = 699` and `H_9(A_384) = 42`. The admissibility intervals and `C(N)` are re-checked, with the cross-catalogue capacity, by the certificate of [`universal-annular-partial-current`](../universal-annular-partial-current/README.md).

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B18-replay-revival migration; standard library) replays the unmodified legacy checks `affine_template_compiler.py`, `check_annular_components.py` in a temporary copy of the legacy layout built by `tools/legacy_replay.py`, requiring exit 0 and every file unchanged (about 21 s). It checks finite steps only; the status is unchanged.

## Remarks

- **Incremental graph findings (finite, from the legacy run).** The legacy constructor uses multi-source breadth-first exposure and union-find: every original nonzero source is at depth zero, each newly discovered state is expanded once, the graph after layer `d` is exactly the union of the first `d` arrows from every source, and each component keeps its total signed source mass and its six band contributions. With cap 128, first success depths were:

  | N | Aggregate nonpositive residual | Each band nonpositive residual | Aggregate exact | Each band exact |
  |---:|---:|---:|---:|---:|
  | 96 | 28 | 33 | 45 | 45 |
  | 112 | 32 | 32 | 45 | 45 |
  | 128 | 44 | 44 | 45 | 45 |
  | 144 | 29 | 34 | 45 | 45 |
  | 168 | 34 | 44 | 41 | 44 |
  | 384 | 42 | 42 | 84 | 84 |

  The per-band columns use the **same exposed graph**, so the comparison isolates actual cancellation across bands. At `N = 168`, aggregate exact success at depth 41 leaves one component unlinked to 1, with sources `(10087, 15131, 22697)`, coefficients `(−1, −1, 2)` and band masses `(0, 0, 0, 0, −1, 1)`: the fifth and sixth bands cannot both be certified alone on this graph, while their combined measure is an exact divergence. At `N = 96`, nonpositive-residual success at depth 28 leaves a balanced component on `(4591, 6121, 6887, 10331, 13775)` with coefficients `(−1, −1, 1, 2, −1)` and the same band masses; it is the five-source tree above. These rest on the legacy receipt `annular_component_audit.json`; only the two stored tables are re-checked here.
- **The two-row cross-band family.** For every `8 | N` and every `x` with `48N < x < 64N`, `x ≡ 7 (mod 72)`: `Sx = (3x+1)/2`, `S^2x = (9x+5)/4`, with actual annular coefficients `(−1, −1, 2)`, and `−δ_x − δ_(Sx) + 2δ_(S^2 x) = (I − P)(−δ_x − 2δ_(Sx))`, a nonpositive current. The `N = 168` component is one instance; the compiler lifts it with slopes `(8, 12, 18)`, and `t = 1008s` keeps it in `A_(168(1+s))`. This rule is family A of the catalogue in [`universal-annular-partial-current`](../universal-annular-partial-current/README.md), where the cross-family capacity proof now sits.
- **A failed stronger candidate.** An everywhere-nonpositive current with nonpositive residual would imply `H_L(A_N) ≤ 0` at every horizon. This is false: `H_53(A_96) = 699` and `H_9(A_384) = 42` (certified above). By [`finite-current-certificate-identity`](../finite-current-certificate-identity/README.md), every current with nonpositive residual for `A_96` has positive cost at least 699. Zero-cost local rules cannot by themselves eliminate the positive-work obligation.
- **What remains.** A universal construction for the residual after valid partial families are removed, or a proof that further families cover it without overusing source coefficients. The compiler proves each supplied tree's identity and checks coverage; it does not prove that mining enough trees terminates or that the unhandled positive components disappear ([`annular-component-progress-lemma`](../../questions/annular-component-progress-lemma.md)).
- Novelty undetermined.

## History

- Migrated from `experiments/annular_construction/components/AFFINE_COMPONENTS.md` (part of the legacy R8 round; alias `R8-b`) at commit `be73a66`, by the B08 migration (Claude, Opus 5.5). Its §4 capacity proof moved to [`universal-annular-partial-current`](../universal-annular-partial-current/README.md). Scripts, receipts and tables moved byte-identical; `check_stored_annular_currents.py` was added at the migration because the legacy scripts no longer run at their new paths. Legacy status: "written proofs and finite certificates".
- Main lane (ChatGPT, Codex), 2026-10-17, commit `ce56699`. The round report records "independent model reviews" of both capacity arguments by the main lane's own agents; no review from another lane is on record.
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. No corrections; the review supplies the omitted argument that only `t ≡ 0, 3 (mod 9)` can give admissible copies (so `C(N)` counts all of them) and records that the compiler theorem is `d`-uniform: [`REVIEW-2026-10-31-claude-review-lane.md`](REVIEW-2026-10-31-claude-review-lane.md).
