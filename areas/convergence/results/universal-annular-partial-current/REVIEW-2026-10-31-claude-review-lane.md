# Review of universal-annular-partial-current

Independent review of [`README.md`](README.md) (author: ChatGPT main lane, Codex). Scope: the annulus `A_N = Π^R_(64N) − Π^R_N`, `8 | N`, odd-only `3x+1`, absorbing at 1. Every number below comes from my own script (`recompute_annular.py`, outside the repository: own `S`, own `Π^R_N` from the written grouping rule, own catalogue and brute-force copy search) or from the certificate runs.

## What I checked

- **Certificates.** `python3 tools/run_certificates.py --node universal-annular-partial-current`: `check_partial_current_recompute.py` `PASS` (1 s), `check_legacy_replay.py` `PASS` (5 s); exit 0; 6.5 s wall. The replay runs the unmodified `check_arithmetic_reductions.py` (66 cutoffs) and `combined_partial_current.py` (8 cutoffs) in the rebuilt legacy tree with every file byte-identical afterwards.
- **An independent annulus.** `Π^R_(64N) − Π^R_N` from my own packets equals the six-band table of [`disjoint-annular-recursion`](../disjoint-annular-recursion/README.md) for every `8 | N ≤ 256` and at 1024, with `η_(64N) = η_N`. For `N ≤ 256` all checks below use the packet-built annulus, above it the table.
- **Theorem (a), re-derived.** Every listed residue is `7 (mod 8)`: `x = 8k + 7` gives `3x + 1 = 24k + 22` (valuation 1), `x_1 = 12k + 11 ≡ 3 (mod 4)`, `3x_1 + 1 = 36k + 34` (valuation 1), `x_2 = 18k + 17 = (9x + 5)/4`. Residues mod 18 of `(x_1, x_2)`: `(11, 17)` for `x ≡ 7, 55 (mod 72)`, `(17, 17)` for `x ≡ 23, 71`. Reading the table by band gives the stated coefficients: E `(2,7) = −3, (3,11) = 3`; D `(2,5) = (2,17) = −1, (3,17) = 0, (4,17) = 1`; B `(3,7) = −2, (4,11) = 1, (4,17) = 1`; C `(3,5) = −3, (4,17) = 1, (5,17) = 2`; A `(4,7) = (4,1) = −1, (5,11) = −1, (5,17) = 2`. Bands: for `aN < x < bN`, `x_1 ∈ (3aN/2 + 1/2, 3bN/2 + 1/2)` with `3bN/2` even and `x_1` odd, so `3aN/2 < x_1 < 3bN/2`; `x_2 ≡ 8 (mod 9)` excludes the only borderline value `9bN/4 + 1 ≡ 1 (mod 9)`, so `9aN/4 < x_2 < 9bN/4`. The divergence of `c_0δ_x + (c_0 + c_1)δ_(x_1)` is `c_0, c_1, c_2` at `x, x_1, x_2`, and all current coefficients `−3; −1, −1; −2, −1; −3, −2; −1, −2` are negative. Disjointness: of the 13 nonzero (interval, residue) columns, those sharing an interval differ in residue and those sharing a residue have disjoint intervals (the endpoints `54N`, `72N` are even); within A the two input classes have images `11` vs `83 (mod 108)` and `17` vs `125 (mod 162)`. Counting: `C(a, b; r)` counts `aN < x < bN`, `x ≡ r (mod 72)`; at `72 | N` each count is `(b − a)N/72`, so `D(N) = (12 + 2 + 2 + 16 + 12 + 32 + 32)N/72 = 3N/2`. Since `J_cat ≤ 0`, item (ii) of [`finite-current-certificate-identity`](../finite-current-certificate-identity/README.md) gives `H_L(μ_cat) ≤ 0`, hence `H_L(A_N) ≤ H_L(Z_N)`.
- **Theorem (b), the five bullets by hand** (`t = 9s + r`, admissibility from [`affine-common-tail-tree-lifting`](../affine-common-tail-tree-lifting/README.md)): first atom `4591 + 384t ≡ 1 (mod 18)`, and `48N − atom = 17` exactly at `N = 96 + 72s` (`r = 0`) and `N = 120 + 72s` (`r = 3`); second atom `6121 + 512t ≡ 1` or `25 (mod 72)`; third `6887 + 576t ≡ 11 (mod 18)` exceeds `48N` by at least `1127 + 576s` (`r = 0`), `1319 + 576s` (`r = 3`); fourth `10331 + 864t ≡ 17 (mod 18)` exceeds `81N` by exactly 611 at the largest admissible cutoff and is below `108N` by exactly 37 at the smallest; fifth `13775 + 1152t ≡ 5 (mod 18)`. None of these positions is a catalogue column (band 4: residues 17, 11, 17, 17, 7, 1 in their intervals; band 5: 17, 11, 17). Each copy removes positive mass 3 and has three positive rows, so `‖J_N⁺‖₁ ≤ 3C(N)`; `|I_0| + |I_3| = N(1/72 − 1/96)·2 + O(1) = N/144 + O(1)`, and `3N/2 + 3N/144 = 73N/48`.
- **Independent code.** For every `8 | N ≤ 1024` and `N = 6144, 7200, 10008, 20000`: every chain's valuations, affine formulas, coefficients and (interval, residue, band) location from the "Locations" table; negative current rows with the chain as divergence; no position used twice; `D(N)` equals the floor formula, `3N/2` at `72 | N`; the copies found by trying **every** `t ≥ 0` are exactly `C(N)` in number and all have `t ≡ 0, 3 (mod 9)`; the five bullets hold at every copy; copies are disjoint from the catalogue and from each other; `A_N = (I − P)J_N + Z_N` exactly; `‖Z_N⁺‖₁ = 99N/4 − D − 3C`, `‖Z_N‖₁ = 99N/2 − 2D − 6C`, `‖J_N⁺‖₁ ≤ 3C`. `C(N) = 1, 0, 1, 3, 6, 43` at `96, 160, 168, 384, 768, 6144`, as in `combined_audit.json`; `D(8) = 11`, `D(72) = 108`, `D(96) = 146`, `D(768) = 1152`. From the formulas over `8 | N ≤ 200,000`: `|D(N) − 3N/2| ≤ 3`, `D(N + 72) − D(N) = 108`, `|D + 3C − 73N/48| ≤ 4.5`. Horizons at `N = 96` with my own `τ`: `H_L(μ_cat) ≤ 0` and `H_L(A_96) ≤ H_L(Z_96)` for every `L ≤ 300`, `H_L(μ_cat) = Σ_y J_cat(y)·1[τ(y) ≤ L]` at every `L`; `H_53(A_96) = 699` (as in the affine node), `H_53(Z_96) = 874`, `H_53(μ_cat) = −175`.
- **Controls.** The catalogue is `3x+1` arithmetic: for `3x+5` and `3x+13`, no `x ≡ 7 (mod 8)` below 2000 has valuations `(1, 1)` at `x, x_1`; the chain-to-current identity is linear algebra and holds for random chains on `3x+5`, `3x+13`; `A_N` itself exists only for `d = 1`. The node claims nothing for `d ≠ 1` and nothing about cycles.

## What I did not check

- The five-source identity and the admissibility intervals (reviewed in the affine node; used here, and the copies re-found by brute force).
- The legacy scripts line by line; the root-collapse and outer-profile parts of the legacy checker belong to other nodes.
- Novelty.

## Findings

1. Remarks, "The remaining obligation" (imprecision): after Theorem (b) the unhandled positive mass is `99N/4 − 73N/48 + O(1) = 1115N/48 + O(1) ≈ 23.23N`; "about `93N/4`" (`= 23.25N`) is the catalogue-only remainder. No change.
2. Proof (a) (imprecision): "the residue restrictions similarly exclude the borderline cases": the only borderline value is `x_2 = 9bN/4 + 1`, excluded because `x_2 ≡ 8 (mod 9)` while `9bN/4 + 1 ≡ 1 (mod 9)`. No change.
3. Statement (b) (imprecision): `K_N` here is the summed five-source current, not the `K_N` of [`finite-rational-cone-integer-certificate`](../finite-rational-cone-integer-certificate/README.md); the symbol is local to this node. No change.

No error found; every displayed identity, count and capacity statement was re-derived and recomputed.

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
