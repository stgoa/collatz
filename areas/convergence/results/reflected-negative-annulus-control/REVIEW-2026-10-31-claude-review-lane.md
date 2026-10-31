# Review of reflected-negative-annulus-control

## What I checked

- Read the node, the annulus `A_96` of [`disjoint-annular-recursion`](../disjoint-annular-recursion/README.md), Theorem 1 of [`orbit-component-current-criterion`](../orbit-component-current-criterion/README.md), [`binary-residue-projection-information-loss`](../binary-residue-projection-information-loss.md), the definition of `H_L` in [`finite-current-certificate-identity`](../finite-current-certificate-identity/README.md), and the checker `check_duality.py` with the two stored tables in [`exposure-potential-boundary-flux`](../exposure-potential-boundary-flux/README.md).
- Certificates: none are listed in this node. Evidence: `exposure-potential-boundary-flux/check_duality.py`, re-run from a scratch copy of its folder: PASS, exit 0, 0.7 s (its `reflected_counterexample` recomputes the routing, the masses, the projections, and compares both CSV tables).
- **Independent code** (own `A_96` from the band table: 3204 atoms, mass 0; own signed Syracuse step, `(3x+1)/2^v` with exact division for negative values): the three cycles verified arrow by arrow (`−1 → −1`; `−5 → −7 → −5`; `−17 → −25 → −37 → −55 → −41 → −61 → −91 → −17`); each of the 3204 reflected sources iterated until it meets an anchor, with detection of any other cycle (none occurred); basin counts 1054, 1027, 1123; signed masses −20, −73, +93, summing to 0; at most 86 steps to the anchor (84 to the first cycle state); the path current has 5868 rows and satisfies `Ã_96 = (I − P)J − 20δ_(−1) − 73δ_(−5) + 93δ_(−17)`, with `P` killing only at positive 1, which is never reached. Both stored tables equal the recomputation.
- **`H_L`.** Every source has `τ = ∞` (a negative odd state maps to a negative odd state), so `h_L ≡ L` on the support and `H_L(Ã_96) = L·Σ Ã_96 = 0` for every `L`.
- **Projections.** `y ↦ −y` sends the class `r mod m` to `−r mod m`, so the projections of `Ã_96` are a permutation of those of `A_96`; the cited theorem gives band-by-band vanishing modulo `2^K` and `3·2^K` when `2^(K+2) | 96`, i.e. `K ≤ 3`, which is exactly the list 2, 4, 8, 6, 12, 24. All six vanish in my computation; modulo 16 and 48 (where the hypothesis fails) they do not (`l¹` norm 10 each), so the list is exhaustive.
- **Impossibility.** `q` = indicator of the basin of the seven-cycle is invariant under `S` on all odd integers (positive states stay positive, so `q = 0` there and at 1), `q ≥ 0`, `q(1) = 0`, and `⟨q, Ã_96⟩ = 93` is read off the explicit paths. Pairing `μ = (I − P)J + ζ` with `q` gives `Σ_x J(x)(q(x) − q(Sx)) + ⟨q, ζ⟩ = ⟨q, ζ⟩ ≤ 0` for `ζ ≤ 0`, a contradiction, for every finite `J` on arbitrary auxiliary states; `ζ = 0` is the exact case. This is Theorem 1 of the orbit-component node (reviewed this wave) on the negative odd integers with absorber 1.
- **Controls.** The node is itself a control outside the positive domain; it excludes nothing about `3x+1` or any `3x+d` cycle, and the criterion it uses is `d`-uniform.

## What I did not check

- Whether every negative odd integer reaches one of the three cycles (the negative Collatz question). The node does not need it: the basin indicator is well defined regardless, and its pairing is computed from the 3204 explicit paths.
- The other parts of `check_duality.py` (they belong to `exposure-potential-boundary-flux`).

## Findings

1. (imprecision) "at most 86 steps" counts steps to the chosen anchor of each cycle (−1, −5, −17); the first cycle state is reached within 84 steps. Harmless.
2. (imprecision) The Proof's "the projections vanish by [the projection theorem] at `N = 96`" could say that the six moduli are all the theorem gives at `N = 96` (`K ≤ 3`), and that the next ones, 16 and 48, indeed fail; the counterexample thus uses exactly the information the projection theorem destroys.
3. (imprecision) The Statement says "positive 1 remains the only absorber", while the one-line proof of the impossibility needs that `q` vanishes at the absorber; it does, since 1 is positive. Worth one clause; no gap.

## Verdict

HOLDS

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
