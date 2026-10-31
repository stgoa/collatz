# Review of affine-common-tail-tree-lifting

Independent review of [`README.md`](README.md) (legacy R8-b), its two certificates and every displayed statement, against the annulus of [`disjoint-annular-recursion`](../disjoint-annular-recursion/README.md) and the current identity of [`finite-current-certificate-identity`](../finite-current-certificate-identity/README.md). Every number below comes from my own script (own `S`, own `A_N` from the six-band table, own divergence and hitting-time code; nothing imported from the node's scripts) or from a derivation written out here.

## What I checked

- **Certificates.** `python3 tools/run_certificates.py --node affine-common-tail-tree-lifting`: `check_stored_annular_currents.py` PASS, exit 0, under 1 s; `check_legacy_replay.py` PASS, exit 0, 5 s (real total 5.1 s). The first is self-contained and exits 1 on failure without `assert`; the second replays `affine_template_compiler.py` and `check_annular_components.py` with every file unchanged.
- **Compiler theorem.** For an edge `x → y` with `3x+1 = 2^(a_x) y`: `d_x = d_y + 1` and `A_x = a_x + A_y` give `3v_x = 2^(A_x+1)3^(D−d_x+1) = 2^(a_x)·2^(A_y+1)3^(D−d_y) = 2^(a_x) v_y`, hence `3x(t)+1 = 2^(a_x)(y + v_y t)`; `v_y` is even, so `y(t)` is odd and the valuation stays exactly `a_x`. Routing source weights along the tree telescopes to `(I − P)J = μ − m·δ_w`. Checked on the five-source tree for `t = 0, …, 599` and `t = 10^12+7, 3^80, 2^200+1, 7^150` (identity and exact valuation of every lifted edge), and on 300 random finite common-tail trees of `3x+1` with random weights (identity including the sink term).
- **Tree data.** The two paths have valuations `(2,1,1,1,2,1)` and `(1,1,1,3)`; recomputed `d_x`, `A_x`, `D = 6`, the slopes and the routed coefficients: the table is exact, positive cost 3, sink slope `2·3^6`.
- **Coverage.** Residues modulo 18 `(1,1,11,17,5)` for `r = 0` and `(1,7,11,17,5)` for `r = 3` give the row-4 and row-5 coefficients `(−1,−1,1,2,−1)`. The binding bounds are `N > (13775+10368s)/144` (last source) and `N < (4591+3456s)/36` (first source), so `96+72s ≤ N ≤ 127+96s`, and for `r = 3` `120+72s ≤ N ≤ 159+96s`; all five pairs of bounds recomputed for `s < 40`, the other three are weaker. Exhaustively over **all** `t ≥ 0` (not only `t = 9s + r`) for every `8 | N ≤ 4096`: the admissible `t` are exactly `{9s : s ∈ I_0(N)} ∪ {9s+3 : s ∈ I_3(N)}`; `C(N) > 0` iff `96 ≤ N ≤ 152` or `N ≥ 168` (`C(96) = 1`, `C(120) = 2`, `C(152) = 1`, `C(160) = 0`, `C(168) = 1`, `C(248) = 2`, `C(1024) = 6`, `C(4096) = 28`); the copies have disjoint supports, `|supp M_N| = 5C(N)`, `‖M_N⁺‖₁ = 3C(N)`, `M_N = (I − P)K_N` with `‖K_N⁺‖₁ ≤ 3C(N)`. The 45 gcd tests pass.
- **Work and cost.** `H_53(A_96) = 699` and `H_9(A_384) = 42` with my own hitting-time code; `H_L(μ_t) ≤ 3` for `t ∈ {0,1,2,5,17,100}` and `L` up to 1000, as identity (ii) of R1-b predicts. The stored tables re-verified with my own divergence: `A_96` one-sided current, 4,901 rows, positive cost 7,272, residual `−2δ_8959 − δ_10919 − δ_11291`; `A_168` exact current, 8,702 rows, positive cost 13,263. Both are consistent with the lower bound 699.
- **Two-row family.** For every `8 | N ≤ 1024` and `x ≡ 7 (mod 72)` in `(48N, 64N)`: `Sx = (3x+1)/2 ≡ 11`, `S²x = (9x+5)/4 ≡ 17 (mod 18)`, coefficients `(−1,−1,2)`, and `(I − P)(−δ_x − 2δ_(Sx))` equals the measure; slopes `(8, 12, 18)` follow from the compiler.
- **Annulus.** `A_N` rebuilt from the table has `267N/8` atoms, mass 0 and positive mass `99N/4` at `N = 96, 168, 384, 1024`.
- **Controls.** The compiler is `d`-uniform: for `3x+d`, `3x+d = 2^a y` and `3v_x = 2^a v_y` give the same lifted identity; verified on 300 random `3x+5` and 300 random `3x+13` common-tail trees (exact valuations, identity with sink term, `t` up to 29 and `t = 2^64+1, 3^50`). So the compiler alone carries no `3x+1`-specific information; only the annular coverage does (the table of R6 uses the `3x+1` offsets). This is consistent with the node's "no complete constructor" and refutes nothing.

## What I did not check

- The legacy incremental constructor and the first-success-depth table of the Remarks, beyond the replay's exit 0 and unchanged receipt `annular_component_audit.json`.
- The cross-catalogue capacity proof, which lives in [`universal-annular-partial-current`](../universal-annular-partial-current/README.md) and was not assigned to me.
- The three dependents (`release-source-packing`, `universal-annular-partial-current`, `annular-complement-outer-descent`).

## Findings

1. **Statement and proof, "all C(N) admissible copies" (imprecision).** The proof computes the residues only for `r ∈ {0, 3}` and never says why the other residues of `t` modulo 9 carry wrong coefficients, which is what makes `C(N)` the count of *all* copies and the claim's "exactly when" complete. The missing two lines: the second source `6121 + 512t ≡ 1 + 8t (mod 18)` must be 1 or 7 (the band-4 residues with coefficient `−1`), which forces `t ≡ 0` or `3 (mod 9)`; the first source `1 + 6t` independently excludes `t ≡ 2 (mod 3)`. Verified exhaustively for `N ≤ 4096`. The claim is correct as stated; no change.
2. **Compiler theorem (remark).** It is `d`-uniform (see Controls). The node does not claim otherwise; recorded so that no later node reads the compiler as `3x+1`-specific.
3. **Statement, "sink term discarded when w(t) = 1" (imprecision).** Since `w(t) = w + 2·3^D·t`, this happens only for `w = 1`, `t = 0`; harmless.

## Verdict

HOLDS. No correction; both certificates passed; the status is raised to `reviewed`.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
