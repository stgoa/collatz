# Review of bounded-packet-certificate-obstruction

## What I checked

- Read the node, [`right-aligned-fixed-core-remainder`](../right-aligned-fixed-core-remainder/README.md) (R2, the packet construction), [`orbit-component-current-criterion`](../orbit-component-current-criterion/README.md) (R7, the sign convention of one-sided currents in `finite_certificate`) and the evidence script `verify_obstructions.py`. This node was the single file `bounded-packet-certificate-obstruction.md`; I moved it to this folder, added one `../` to its six relative links and repointed the eleven inbound links in nine files (listed in the lane report).
- **Packet membership, re-derived from R2's definitions.** For `a = 1`: `(q_1, e_1, t_0) = (3, 5, 0)`, `M_1 = 4`, lifts `x_t = 3 + 4t → y_t = 5 + 6t` with `3x_t + 1 = 2(5 + 6t)`, valuation exactly 1. For `N = 4·2^K + 5`: `n_1 = ⌊(3N + 1)/2⌋ = 6·2^K + 8`, `ℓ = ⌊(n_1 − 3)/4⌋ = 3·2^(K−1) + 1 = t + 2` with `t = 3·2^(K−1) − 1` (source `6·2^K + 7 ≤ n_1`, next source `6·2^K + 11 > n_1`); `s = t + 3 ≡ 2 (mod 3)`, so two lifts stay ungrouped and the triples start at `t ≡ 2 (mod 3)`; `x_t, x_(t+1), x_(t+2) ≡ 2, 0, 1 (mod 3)` give coefficients `2, −1, −1`; `y_t = 9·2^K − 1 = y`. Independent materialisation of the whole right-aligned construction (both components, all valuations `a ≤ b`) for `H = 0, 1, 2, 3` (`N = 517, 2053, 8197, 32773`): the last valuation-1 packet of component 1 is exactly `2δ_y − δ_(y+6) − δ_(y+12)`, the ungrouped endpoints lie in `{5, 7, 11, 13}`, the total packet mass is 0.
- **Delayed separation, re-derived.** Base orbits `−1` (valuations `1, 1, …`, `A_j = j`), `5 → 1` (`4, 2, 2, …`, `A_j = 2j + 2` for `j ≥ 1`), `11 → 17 → 13 → 5 → 1` (`1, 2, 3, 4, 2, …`, `A_j ≤ 2j + 2`); so `A_j ≤ 2H + 2` and `K − A_j ≥ 5` for `j ≤ H`. The perturbation formula `S^j(z_0 + 9·2^K) = z_j + 9·3^j·2^(K−A_j)` follows by induction because the perturbation is divisible by `2^(K−A_j)` and the quotient stays odd while `K − A_(j+1) ≥ 1`. Residues: `31 (mod 32)` along the `y`-orbit, `{1, 5, 11, 13, 17} (mod 32)` along the other two; no state of the `y`-orbit is 1. Verified by independent code for every `H ≤ 80` (formula, residues, disjointness of the first `H + 1` states; 0 violations).
- **The graph argument, re-derived.** Summing `div J` over the undirected component `D` of `y` in the graph of nonzero arrows (rows at 1 killed) gives 0 when `D` misses the absorber, since every nonzero arrow with an endpoint in `D` has both endpoints in `D`; with `μ_y = div J + ζ`, `ζ ≤ 0`, this forces `y + 6`, `y + 12` or the absorber into `D`. In a functional graph a simple undirected path cannot have an interior vertex with both adjacent arrows leaving it (two successors), so its arrows point toward one meeting vertex; the endpoints therefore meet under forward iteration within the path length `≤ H`, or `y` reaches 1 within `H` steps. Both contradict the separation, so at most `H` rows is impossible. The one-sided case uses the same sign convention as `finite_certificate` (`divergence(current) + residual = μ`, residual `< 0`).
- **The local identity.** `S²(69 + 256t) = 5 + 18t` (valuations 4, 3), `S²(75 + 256t) = 85 + 288t = 16·S²(x) + 5` (valuations 1, 2), `3(16u + 5) + 1 = 16(3u + 1)`, hence `S³(x) = S³(x + 6)`; checked for all `t < 20000`; the current has at most six rows.
- **Evidence script.** `python3 areas/convergence/results/orbit-component-current-criterion/verify_obstructions.py`: exit 0, 0.08 s; it checks the formulas at `H ∈ {0, 1, 2, 4, 8, 16, 32, 64, 128}` and the identity for `t ≤ 9999` by `assert` (run without `-O`). The node lists no certificates.
- **How loose the bound is.** The first actual coincidence of the `y`-orbit with the orbits of `y + 6`, `y + 12` or with 1 (raw map) is at depth 17 for `H = 0`, 53 for `H = 1`, 48 for `H = 2`, 36 for `H = 3`, …, 184 for `H = 12`, always with the orbit of `y + 6`; the theorem's `H + 1` is far below the true forced size, as its own Complement remark anticipates.
- **Controls.** The statement is a lower bound on certificate size for `3x+1` packets and excludes nothing about cycles; the perturbation arithmetic is specific to `3x+1`. The `3x+d` controls do not apply.

## What I did not check

- [`exact-current-minimality`](../exact-current-minimality.md) and the PR1 NOTE §10 cited in the Complement remark.
- Whether cancellations across packets in the aggregated `Π^R_N` reduce the cost (explicitly outside the claim).

## Findings

1. Frontmatter `evidence`: the path `../orbit-component-current-criterion/verify_obstructions.py` was written relative to a node folder that did not exist (from the single file in `results/` it resolved to `areas/convergence/orbit-component-current-criterion/`). After the conversion to a folder it resolves correctly; the text is unchanged. Imprecision, now moot.
2. Proof, "Delayed separation": "For `0 ≤ j ≤ H`, each `A_j ≤ 2H + 2`" is what the induction uses; the sharper `A_j ≤ 2j + 2` is what the three base orbits give. Imprecision, harmless.
3. The label "Theorem 2" is inherited from the legacy note whose Theorem 1 became `orbit-component-current-criterion`. Typo-level.
4. The bound `> H` is very loose (see above); not an error.

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
