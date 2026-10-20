---
id: exposure-potential-boundary-flux
kind: result
title: On an exposed graph, positive component masses are exact dual obstructions, and the scale argument misses an explicit boundary flux
status: written
claim: >
  Odd-only 3x+1 map, absorbing at positive 1. (Finite duality) For a finite integer source μ and a finite set
  E of exposed forward arrows, a current supported on E with everywhere nonpositive residual exists iff every
  component of the undirected exposed graph not containing 1 has nonpositive source mass; each positive
  component indicator is a dual obstruction restricted to E. (Potential) Φ(E), the sum of the positive source
  masses of components not containing 1, is a nonnegative integer, nonincreasing as arrows are added, and zero
  iff such a current exists on E; for the annulus A_96 with E_d the first d arrows from every source,
  Φ(E_0) = 2376, Φ = 17 at every depth 20–27 and Φ = 0 at depth 28. (Boundary flux) For 8 | N, with
  F_t = U_(64t) − U_t, V_N = ν_(64N) − ν_N, K_N = V_N + 3(F_N − F_(N/4)) and D_N = 3F_N − 3F_(N/4) − F_(3N/2) − F_(3N/4),
  D_N = A_N + (I − P)K_N exactly; pairing with an exposed-component indicator q adds the flux
  Σ_x K_N(x)(q(x) − q(Sx)), which is −7 for an 83-vertex component of A_96 at depth 27 (source mass 17,
  scale pairing 10). No progress lemma (that every positive plateau of Φ ends) is proved.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [disjoint-annular-recursion, right-aligned-fixed-core-remainder, orbit-component-current-criterion]
certificates: [check_duality.py]
evidence:
  - "duality_audit.json: receipt of check_duality.py, which compares its recomputation with it (including every vertex, source atom and flux row of the depth-27 component); reflected_annulus_96_current.csv and reflected_annulus_96_residual.csv belong to reflected-negative-annulus-control"
  - "../locally-collatz-like-control-barrier/progress_measures_audit.py, progress_measures_audit.json: the PR1 lane's independent check of the Φ(A_96) trace (a certificate of that node)"
reviewed_by:
  - by: Claude PR1 lane (Opus)
    date: 2026-10-17
    link: progress-measures-control-3x-61.md
    scope: "Finite only (ledger C1/C4, NOTE §11): with independent code, Φ(A_96) = 17 at exposure depths 20–27 and 0 at depth 28. The written duality, monotonicity and flux arguments were not re-derived, so the status stays written"
aliases: [R10]
tags: [convergence, packet-currents, annular, duality, progress-potential, boundary-flux]
---

# On an exposed graph, positive component masses are exact dual obstructions, and the scale argument misses an explicit boundary flux

## Statement

The annulus `A_N`, `8 | N`, is the six-band signed measure of [`disjoint-annular-recursion`](../disjoint-annular-recursion/README.md): `Q = 9N/4`, support in `(Q, 64Q)`, total mass zero, coefficients in band `j` depending on the residues `1, 5, 7, 11, 13, 17 mod 18`. All statements use the odd-only clock and absorption at positive 1.

**Theorem 1 (finite duality).** Let `μ` be a finite signed integer source measure, and expose a finite set `E` of actual forward arrows; the vertex set includes their endpoints, every source, and the absorber. A current restricted to `E` may use arbitrary signed coefficients on its arrows. Then

```
μ = (I − P)J + ζ,     supp J ⊆ E,     ζ ≤ 0
```

is solvable exactly when every connected component of the exposed undirected graph not containing 1 has nonpositive total source mass. If component `C` has positive mass, its indicator `q = 1_C` is a finite dual obstruction: `q ≥ 0`, `q(1) = 0`, `q(x) = q(Sx)` on every exposed arrow, and `⟨q, μ⟩ > 0`.

**Proposition 2 (progress potential).** For a nested sequence of exposed graphs put

```
Φ(E) = Σ_(C : 1 ∉ C) max(Σ_(x ∈ C) μ(x), 0).
```

`Φ(E)` is a nonnegative integer, never increases when arrows are added, and is zero exactly when the exposed graph supports a current with nonpositive residual. For the actual annulus `A_96`, with `E_d` the first `d` steps from every original nonzero source atom (historical intersections retained): `Φ(E_0) = 2376`; `Φ = 17` at every depth from 20 through 27, with one positive component at depth 27 containing 31 source atoms; and `Φ = 0` at depth 28.

**Theorem 3 (exact scale identity).** For an integer `t`, let `U_t` count the positive odd states `1 < x ≤ t`, and `F_t = U_(64t) − U_t`. Fix `8 | N` and define

```
V_N = ν_(64N) − ν_N,
K_N = V_N + 3(F_N − F_(N/4)),
D_N = 3F_N − 3F_(N/4) − F_(3N/2) − F_(3N/4).
```

Then, with the original source multiplicities and all integer cutoffs retained,

```
D_N = A_N + (I − P)K_N.                                                                 (1)
```

For a finite exposed-component indicator `q` with `q(1) = 0`,

```
⟨q, D_N⟩ = ⟨q, A_N⟩ + 𝓕_N(q),     𝓕_N(q) = Σ_x K_N(x)·(q(x) − q(Sx)).                    (2)
```

On every exposed arrow `q(x) = q(Sx)`, so the flux comes entirely from **unexposed rows of the explicit finite measure `K_N`**. For a globally invariant indicator, such as the nonhalting indicator, the flux vanishes.

**Example (a positive component with nonzero flux).** At depth 27 for `A_96`, the component `q` containing 1819 has 83 vertices and 31 source atoms, source pairing 17, and `⟨q, D_96⟩ = 10 = 17 − 7`, `𝓕_96(q) = −7`. There are exactly 11 nonzero flux rows, each with `q(x) − q(Sx) = −1`:

| `K_96(x)` | Row states `x` |
|---:|---|
| 1 | 2553, 3639, 3831, 4095, 4311, 4539 |
| 2 | 4851, 6057 |
| −1 | 6375, 9079, 9087 |

Adding every arrow whose tail has nonzero coefficient in `K_96` to this depth-27 graph makes every component indicator's `K_96` flux zero, yet the enlarged graph still has one positive component, of mass 17 (its scale pairing has changed to 17 with its enlarged vertex set). One more ordinary exposure level resolves the example.

## Proof

From §§1–3 of the legacy note `aggregate_duality.md`, kept as written.

**Theorem 1.** Pairing a proposed identity with a positive component indicator `q` yields a contradiction. Conversely, when all component masses have the required sign, route source coefficients along undirected spanning trees to an anchor of each component, using signed flow when traversing an arrow backwards, with 1 as the absorbing component's anchor. The residual is the component mass at each other anchor. This is an integral construction, the elementary graph version of finite linear-programming duality; no numerical optimizer is required. ∎

The dual is **restricted to the exposed graph**: it does not prove that a current using unexposed arrows is impossible. To prove global impossibility the function must be invariant on the entire relevant deterministic graph ([`orbit-component-current-criterion`](../orbit-component-current-criterion/README.md)).

**Proposition 2.** A new arrow either stays in one component or merges two components. For real `u, v`, `max(u + v, 0) ≤ max(u, 0) + max(v, 0)`. If a component merges into the absorbing component, its formerly counted positive mass disappears. These prove monotonicity; Theorem 1 proves the zero criterion. The `A_96` values are exact finite computation (certificate below). At depth 27 the single positive component's indicator pairs to 17, so **no** current restricted to that entire exposed graph has an everywhere nonpositive residual. ∎

**Theorem 3.** Partition odd sources by first valuation. Valuation 1 maps bijectively to residue 5 modulo 6 up to `3N/2`; valuation 2 maps to residue 1 modulo 6, excluding the absorber, up to `3N/4`. Sources with valuation at least 3 are `4z + 1`, with odd `z ≤ N/4`, and have the same successor as `z`. The exceptional `z = 1`, source 5, contributes nothing after absorption. The floor in `(N − 1)/4` causes no difference because `N/4` is even. Consequently, if `T_r(t)` counts the odd nonabsorbing states in the stated residue class, `P(U_N − U_(N/4)) = T_5(3N/2) + T_1(3N/4)`. The definition of the two-component source gives

```
ν_N = 3P(U_N − U_(N/4)) − U_(3N/2) − U_(3N/4).
```

Subtracting this identity at `N` from the one at `64N`, `V_N = 3P(F_N − F_(N/4)) − F_(3N/2) − F_(3N/4)`. Hence `D_N = V_N + 3(I − P)(F_N − F_(N/4))`. The fixed core cancels under the 64-fold scale change, so `A_N = P·V_N`. Substitution proves (1), including its sign and the factor 3; no asymptotic cutoff replacement occurs. Pairing (1) with `q` gives (2). ∎

## Certificates

[`check_duality.py`](check_duality.py) (main lane, about 1 s, standard library; checks by `assert`, so run it without `-O`). It compares its recomputation with [`duality_audit.json`](duality_audit.json) and the two CSV tables. For this node it checks seven exact annular source-scale identities (1), the positive `A_96` exposure potential through depth 28, every recorded finite-component flux row and the depth-27 closure example. The same run checks [`binary-residue-projection-information-loss`](../binary-residue-projection-information-loss.md) (`K = 1, …, 8`), [`reflected-negative-annulus-control`](../reflected-negative-annulus-control.md), and, independently, the `19/22` collapse formula of [`annular-root-collapse-contraction`](../annular-root-collapse-contraction.md) at nine cutoffs. The graph search has a depth cap of 128; an unresolved cap is never interpreted as nonexistence.

## Remarks

- **What is missing: a progress lemma.** `Φ` is a useful monotone measure of progress, not a termination proof: it can decrease strictly only finitely many times and still stay positive forever on a plateau. A constructor needs an arithmetic argument that every positive plateau ends after finitely many new exposures, for the annuli on the 30 sequences: [`annular-component-progress-lemma`](../../questions/annular-component-progress-lemma.md). A capped scan cannot establish it. On the false analogue `3x+61` the potential falls by about 97% early and then stays positive forever ([`progress-measures-control-3x-61`](../progress-measures-control-3x-61.md)), so an early fall is not evidence.
- **The five-ray maximum principle does not supply the strict decrease.** Its comparison is in the cutoff index, and its hypothesis already controls the pairing with the nonhalting indicator ([`five-ray-current-criterion`](../five-ray-current-criterion/README.md)). At a finite graph stage there are many separate component-indicator duals, with unknown future mergers; contracting a scalar count across cutoffs gives no bound on the duration of their plateaus.
- **The flux is the missing term.** Equation (2) is the precise term omitted when a scalar cutoff comparison is applied to an unresolved finite component; the `A_96` example is an exact counterexample, on positive integers and the actual annulus, to omitting it. Zeroing it at one cutoff while ignoring the change of the component indicator does not prove progress either. A possible constructor can use `K_N` to expose arithmetic boundary rows instead of expanding every orbit uniformly; the obligation is then to prove that the resulting extensions eventually reduce positive mass.
- **Relation to the recursion.** Equation (1) is the exact finite representative of the quotient identity `[A_N] = 3[F_N] − 3[F_(N/4)] − [F_(3N/2)] − [F_(3N/4)]` of [`disjoint-annular-recursion`](../disjoint-annular-recursion/README.md), whose expanding `3N/2` term blocks a terminating induction.
- Novelty undetermined.

## History

- Migrated from `experiments/annular_construction/duality/aggregate_duality.md` §§1–3 and 6 (legacy ID R10; the legacy folder README listed only R8–R9, but the ledger `archive/docs/RESULTS.md` (legacy path) links R10 to this note) at commit `be73a66`, by the B08 migration (Claude, Opus 5.5). Its §4 became [`binary-residue-projection-information-loss`](../binary-residue-projection-information-loss.md) and §5 [`reflected-negative-annulus-control`](../reflected-negative-annulus-control.md). Script, receipt and tables moved byte-identical. Legacy status: "written graph/arithmetic identities and exact scoped counterexamples. The progress lemma remains open".
- Main lane (ChatGPT, Codex), 2026-10-17, commit `ce56699`. Cross-checked on finite ranges by the PR1 lane the same day.
