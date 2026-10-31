# Review of local-packet-calibration-extension

Independent review of [`README.md`](README.md) (author: ChatGPT main lane, Codex). Scope as in the node: odd-only `3x+1`, absorbing at 1, `8 | N`. Every number below comes from my own script (`recompute_local.py`, outside the repository: own `S`, own `ν_N`, own right-aligned grouping written from the definition in [`right-aligned-fixed-core-remainder`](../right-aligned-fixed-core-remainder/README.md), own union-find) or from the certificate run.

## What I checked

- **Certificate.** `python3 tools/run_certificates.py --node local-packet-calibration-extension`: `PASS`, exit 0; the runner reports 6 s for `check_legacy_replay.py`, 6.5 s wall for the call. The replay runs the unmodified `check_local_extension.py` in the rebuilt legacy tree and requires every copied file byte-identical afterwards.
- **Split (2), re-derived.** For odd `y > 1` the `S`-preimages are `x_a = (2^a y − 1)/3` with `a` odd for `y ≡ 2 (mod 3)`, even for `y ≡ 1`, and `x_(a+2) = 4x_a + 1`. So `(N/4, N]` contains at most one preimage, and exactly one iff the least one is `≤ N`: iff `y ≤ 3N/2` for `y ≡ 2`, iff `y ≤ 3N/4` for `y ≡ 1` (using `4 | N`). Hence `ν_N = 3P(U_N − U_(N/4)) − U_(3N/2) − U_(3N/4)`, `D_N − ν_N = 3(I − P)(U_N − U_(N/4))`, and with `Pν_N = Π_N + η_N` this is (2) with `K_N = ν_N + 3(U_N − U_(N/4))`; `D_N = I_N − L_N` is a rearrangement. Coefficients: `I_N` is `0, 1, 2, 0` and `L_N` is `2, 0, 0, 1` on `(1, N/4]`, `(N/4, 3N/4]`, `(3N/4, N]`, `(N, 3N/2]`; with `‖U_t‖₁ = t/2 − 1` for even `t` the masses are `N/2`, `N/2 − 2`, `N/4`.
- **(4), (6), §4.** Algebra from (2) and (5); checked symbolically and numerically.
- **(7), (8), exact-input extension.** On a weak component `K` of the nonzero-row graph that does not contain 1, every row's arrow stays inside `K` and none ends at 1, so `Σ_K (I − P)C = 0` and `Σ_K L_N = −Σ_K ζ`; summing over these components gives `2M_low + M_out = −Σ ζ(x)` over them, at most `‖ζ⁻‖₁`; (8) is the same with the second identity and `(·)⁺`. For `ζ = 0`, the integer-component lemma of [`finite-rational-cone-integer-certificate`](../finite-rational-cone-integer-certificate/README.md) with `μ = L_N ≥ 0`, `Z = 0` puts every source in the component of 1; in a graph of out-degree `≤ 1`, a weak component containing a vertex of out-degree 0 (the absorber) is a tree whose every vertex flows to it.
- **(9)–(11).** Integer form of (9): `0` for `3N < 2x`; `−1` for `2x ≤ 3N < 3x`; `2` for `x ≤ N`, `3N < 4x`; `1` for `4x ≤ 3N`, `N < 4x`; `−2` for `N ≥ 4x`. Taking the coefficient at `x` in (10): `Σ α_N D_N(x) = μ(x) + V(x) − Z(x) ≥ 1 − ε`, positive terms only from `x ≤ N < 4x` with `D_N(x) ≤ 2`, giving (11); `x ≤ N < 4x` is `x ∈ (N/4, N]`, the support of `I_N`.
- **Top atom.** `3N/2 − 1 ≡ 3 (mod 4)` has valuation 1 and endpoint `9N/4 − 1`; `ν_N(3N/2 − 1) = 2` (component 1 only), `K_N(3N/2 − 1) = 2` because `3N/2 − 1 > N`; so `(I − P)K_N(9N/4 − 1) = −2` cancels the packet coefficient 2.
- **Independent code.** My grouping reproduces `Pν_N = Π_N + η_N` for every `8 ≤ N ≤ 600`. For every `8 | N ≤ 1024`: both forms of (2), nonnegativity, the four-interval patterns, the masses (3), formula (9) at 66,048 pairs `(N, x)` and as a function of `N` for `x = 3, 5, 97, 101, 1001`, and the top atom. Stored [`outer_96_current.csv`](outer_96_current.csv): 102 rows, all weights positive (total 489), divergence exactly 1 at each odd state `97..143` and 0 elsewhere. The three examples rebuilt from scratch, `H` and `E_N` as path currents, `J` and `ζ` from my own one-sided historical search of `Π_N` with anchors at component minima (the exposed graph is a forest at success, so `J` is fixed by the depth and the anchors): `N = 24`: depth 1, `ζ = −δ_31 − δ_47`, `C` has 14 rows, unabsorbed outer seeds exactly 27, 31, identity (7) `2 = 2`, bound (8) `2`. `N = 96`: depth 18, `ζ = 0`, 106 rows, nothing unabsorbed, and routing `W_96` along the arrows of `C` returns exactly the stored 102-row table. `N = 384`: depth 6, `ζ = −δ_415 − δ_671 − δ_743 − δ_767 − δ_839`, unabsorbed 447, 495, 511, 559, mass 4 against budgets 5 and 5. Those seeds stay unlinked to 1 even on the larger graph of every arrow of `H`, `K_N`, `E_N`, `J` before cancellation, so the examples do not hinge on cancelled rows. Feedback at `N = 8, 24, 96`: `C = 0` and `−ζ = L_N` with masses 2, 10, 46.
- **Controls.** The component identity behind (7) concerns finite graphs of out-degree `≤ 1` and is map-independent: on `3x+5` and `3x+13`, with 300 random finite currents `C` each and `L := ((I − P)C)⁺`, `ζ := −((I − P)C)⁻`, the sum of `L` over the components not containing 1 equalled `−Σ ζ` over them in every case. The `3x+1`-specific input is (2) itself (the packets `Π_N`), for which the node claims nothing at other `d`; it makes no cycle claim, so the actual `3x+d` cycles are not a test here.

## What I did not check

- The proof of `Pν_N = Π_N + η_N` (reviewed node; re-confirmed only numerically).
- The legacy search code line by line; I re-implemented the stated rule instead and reproduced its outputs.
- The dependent [`retained-graph-complement-constructor`](../retained-graph-complement-constructor/README.md) beyond noting that it uses (2), (4), (6), all re-derived here. Novelty.

## Findings

1. Statement item 3 (imprecision): "on the graph of the nonzero rows of `C`" is shorthand for the graph `E` of Proof §3, which also has every source state of `L_N`, every residual state and 1 as vertices; without them `M_low`, `M_out` would be undefined for seeds no row touches. The proof defines `E` correctly. No change.
2. Proof §2 (imprecision): "Equivalently, the odd seeds in `(N/4, N]` have finite absorption certificates": for a rational `H` the forward direction uses the integer-component lemma (`μ = I_N ≥ 0`, `Z = 0`); for path currents it is immediate. No change.
3. Proof §5 (imprecision): the finite cone's lower boundary `b` is supported on cutoffs `≤ 84`, so the barrier applies to seeds above that base, which is what the hypothesis `b(x) = 0` encodes. No change.

No error found. Every displayed identity ((2)–(4), (6)–(11)) and every finite example was re-derived or recomputed.

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
