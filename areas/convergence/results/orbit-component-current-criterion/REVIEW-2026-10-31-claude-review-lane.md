# Review of orbit-component-current-criterion

## What I checked

- **Certificate.** `python3 tools/run_certificates.py --node orbit-component-current-criterion`: `PASS`, exit 0, 0 s reported by the runner (0.40 s wall for the whole call). Run directly, `verify_obstructions.py` exits 0 and its standard output is byte-identical to [`audit.json`](audit.json).
- **Theorem 1, re-derived.** Necessity: for a nonabsorbing component `C`, `S` maps `C` into `C`, so `⟨1_C, PJ⟩ = Σ_y J(y)·1_C(S y) = ⟨1_C, J⟩` (mass killed at `o` never lies in `C`), hence `⟨1_C, (I − P)J⟩ = 0` and `m_C = ⟨1_C, μ⟩ = ⟨1_C, ζ⟩`, which is `0` or `≤ 0`. Sufficiency: for a path `x = p_0 → … → p_d = z` the current `c·Σ_(i<d) δ_(p_i)` has divergence `c(δ_x − δ_z)`, or `c·δ_x` when `z = o`; summing over the finitely many sources gives `μ = (I − P)J + Σ_C m_C δ_(z_C)`. A common descendant of finitely many states of one component exists because two meeting points on one orbit are comparable along it. Weak connectivity in a functional graph is equivalent to `S^a(x) = S^b(y)`, by induction along an undirected path.
- **Work formula.** For `L ≥ max{τ(x) < ∞}`, `min(L, τ(x))` is `τ(x)` or `L`, so `H_L(μ) = L·Σ_(τ=∞) μ(x) + Σ_(τ<∞) μ(x)τ(x)`, and the states with `τ = ∞` are exactly those in nonabsorbing components. A linear function of `L` is bounded above iff its slope is `≤ 0`; this gives (3) and shows why it is weaker than (2).
- **Semidecision theorem.** Soundness: every exposed arrow is a true arrow, so the routed current is a genuine current and the residual sits at the anchors with the component masses. Completeness: at depth `d* = ` the largest path length supplied by Theorem 1, each orbit component meeting `supp μ` forms one exposed component containing all its sources, with mass `m_C`; the absorbing sources are joined to `o`; so the search succeeds at `d*`.
- **Independent computation** (`review_components.py` in my scratch folder, exact rational arithmetic, 22 s). For every functional graph on 3 and on 4 non-absorbing vertices with targets in `{0, …, n}` (`0` absorbing) and every `μ` with coefficients in `{−1, 0, 1}`: existence of an exact current decided by Gaussian elimination over `Q`, existence of `(J, ζ ≤ 0)` decided by the Farkas lemma using the extreme rays of `{f ≥ 0 : (I − P)^T f = 0}` found by support enumeration, with no use of the component criterion. 1,728 and 50,625 cases: both agree with conditions 1 and 2. Cross-check for `n = 3` by brute force over integer `J ∈ [−6, 6]^3`: 1,728 cases agree.
- **Controls.** On `3x+5` and `3x+13` (1 is fixed; among odd states `3..1999`, 851 and 525 have `τ = ∞`), 300 random measures each on odd states `≤ 3000`: the work formula holds at `L = L_max, L_max + 1, L_max + 10, L_max + 1000`, and the increments beyond `L_max` equal the sum of the nonabsorbing masses (components labelled by the cycle each orbit enters).
- **Examples.** `S(−1) = −1`, `S(−5) = −7`, `S(−7) = −5`; `H_L(δ_(−1) − δ_(−5)) = L − L = 0`; the `{−1}` component has mass `+1`. The ray example `(I − P)δ_2 = δ_2 − δ_3` with `P^d(δ_2 − δ_3) = δ_(2+d) − δ_(3+d) ≠ 0`.
- **Depth search.** My own implementation (exposure of `d` arrows from every source, union-find components, spanning-tree routing) on 600 random functional graphs with up to 14 vertices and random `μ`: success at some depth `≤ 2n + 2` iff the component condition holds, in both modes; 485 successes, each verified as `μ = (I − P)J + ζ` with the right sign of `ζ`; 645 correct non-successes.

## What I did not check

- The nodes cited in the remarks ([`reflected-negative-annulus-control`](../reflected-negative-annulus-control/README.md), [`whole-packet-historical-certificates`](../whole-packet-historical-certificates/README.md), [`exposure-potential-boundary-flux`](../exposure-potential-boundary-flux/README.md)).
- The second half of `verify_obstructions.py` (the delayed-separation and coalescence checks that belong to [`bounded-packet-certificate-obstruction`](../bounded-packet-certificate-obstruction/README.md)) beyond running it.
- Novelty.

## Findings

1. Certificates (hygiene, imprecision): `verify_obstructions.py` checks by `assert`, so under `python3 -O` it would exit 0 without checking anything; the node says so, and the runner executes it without `-O`. AGENTS.md §6 asks certificates not to rely on `assert`. The script is a byte-identical legacy file; not changed.
2. Statement (imprecision): "There is one absorbing component, the states that reach `o`" also covers the case where no state of `X \ {o}` reaches `o`, when that component is `{o}` alone and imposes no condition. Harmless.
3. Semidecision theorem (imprecision): the depth at which the search must succeed is the largest of the finitely many path lengths supplied by Theorem 1, and no bound on it is claimed; the node's remarks say this correctly.

No error found.

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
