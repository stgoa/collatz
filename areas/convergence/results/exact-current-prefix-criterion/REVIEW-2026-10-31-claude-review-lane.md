# Review of exact-current-prefix-criterion

## What I checked

- **Certificates.** None are listed. The evidence script named by the node, `right_aligned_packets.py` of [`right-aligned-fixed-core-remainder`](../right-aligned-fixed-core-remainder/README.md) (a certificate of that reviewed node), was run: exit 0, 3.3 s. It checks that the odd seeds below 16 reach 1 and the core hitting times `τ(5), τ(7), τ(11), τ(13) = 1, 5, 4, 2`, which are the two finite inputs of the proof.
- **Pairing facts, re-derived.** `e(x) = 1[τ(x) = ∞]` is `S`-invariant with `e(1) = 0`, so for a finite `μ`, `⟨e, Pμ⟩ = Σ_x μ(x) e(S x) 1[S x ≠ 1] = ⟨e, μ⟩`, and `⟨e, (I − P)J⟩ = 0` for every finite `J`. With `P ν_N = Π^R_N + η_N`, `supp η_N ⊆ {5, 7, 11, 13}` (Theorem 1 of the dependency, `N ≥ 8`) and `e = 0` on the core, `⟨e, Π^R_N⟩ = ⟨e, ν_N⟩`. An exact current therefore forces `⟨e, ν_N⟩ = 0`.
- **1 ⇒ 2.** Every source of `ν_N` is an odd `x ≤ n_1(N) ≤ n_1(M) = floor((3M+1)/2)`, and every packet atom of `Π^R_N` is an endpoint `S(x)` of such a source. Under (1) all of them reach 1 by some finite time `T_N`, so `J_N = Σ_(j<T_N) P^j Π^R_N` is finite and `(I − P)J_N = Π^R_N − P^(T_N) Π^R_N = Π^R_N`. **2 ⇒ 3** is a restriction.
- **3 ⇒ 1, re-derived.** If (1) fails, the least nonterminating odd seed `r` overall lies in the interval. `r ≥ 17` by the base check. If `r ≡ 1 (mod 4)` then `4 | 3r+1` and `S(r) ≤ (3r+1)/4 < r`, a smaller nonterminating odd seed; so `r ≡ 3 (mod 4)`. If `r ≡ 2 (mod 3)` then `x = (2r−1)/3` is a positive odd integer `< r` with `3x+1 = 2r`, so `S(x) = r` (valuation 1) and `x` is nonterminating; so `r ≢ 2 (mod 3)`. Hence `r = 12m+3` or `12m+7`. Then `N = ceil((2r−1)/3)` is `8m+2` (from `(24m+5)/3`) or `8m+5` (from `(24m+13)/3`); `n_1(N) = floor((24m+7)/2) = 12m+3 = r` or `floor((24m+16)/2) = 12m+8 = r+1` (even); `n_2(N) = 6m+1` or `6m+4`, both `< r`. From `r ≤ floor((3M+1)/2)`: `2r − 1 ≤ 3M`, so `N ≤ M`; and `r ≥ 17` gives `N ≥ 13 ≥ 8`. All odd states `< r` terminate, `r` lies only in the first component with coefficient `3·1[r ≡ 2 mod 3] − 1 = −1`, so `⟨e, ν_N⟩ = −1 ≠ 0`, contradicting the exact current at `N` supplied by (3).
- **Arithmetic by script** (`review_prefix.py` in my scratch folder, 0.9 s). For every odd `r` in `[17, 2·10^6]`: `r ≡ 1 (mod 4)` gives `S(r) < r`; `r ≡ 2 (mod 3)` gives the odd lift `x = (2r−1)/3 < r` with `S(x) = r`; the remaining 333,331 seeds are `12m+3` or `12m+7`, and for each the cutoff `N = ceil((2r−1)/3)` satisfies `N mod 8 ∈ {2, 5}`, the formulas `8m+2`/`8m+5`, `N ≥ 13`, `n_1(N) ∈ {r, r+1}`, `n_2(N) < r`, coefficient `−1`, and `N ≤ M` for every `M` with `r ≤ floor((3M+1)/2)`. Conversely, for `8 ≤ N < 200000` the largest odd state `≤ n_1(N)` is of the form `12m+3` or `12m+7` exactly when `N mod 8 ∈ {2, 5}` (24,999 cutoffs in each class): the thinning to one quarter of the cutoffs is exact.
- **Controls** (same script; the conventions of [`locally-collatz-like-control-barrier`](../locally-collatz-like-control-barrier/README.md): `T_d`, `A_d = {1, d}`, `e_d = 1` iff the orbit ends in another cycle, cutoffs `floor((3N+d)/2)`, `floor((3N+d)/4)`, residues `2d mod 3`, `d mod 3`). For `d = 13`: least exceptional seed `r = 19`, `≡ 3 (mod 4)`, `≢ 2d (mod 3)`; `N_iso = ceil((2r−d)/3) = 9`, pairing `⟨e_13, ν_9⟩ = −1`, pairing `≤ 0` through `N = 20`, first positive at `N = 21` (value 2). For `d = 61`: `r = 175`, `N_iso = 97`, pairing `−1` at 97, `≤ 0` through 212, first positive at 213 (value 1), matching the barrier node. So on maps with cycles the isolating cutoff excludes exact currents with pairing exactly `−1`, long before the one-sided criterion fails, as the node's Remark says. The `d = 1` input the controls lack is the base: under `3x+5` and `3x+29` the seed 3 is already exceptional (`r = 3 < d`), so "the odd seeds through 15 terminate" is where the proof uses `3x+1` arithmetic.

## What I did not check

- Theorem 1 of the dependency (reviewed separately); I used it as stated.
- Novelty.

## Findings

1. Proof, 3 ⇒ 1 (imprecision): "`8 ≤ N ≤ M`" is asserted without derivation. It follows from `r ≤ floor((3M+1)/2)` (so `2r−1 ≤ 3M` and `N = ceil((2r−1)/3) ≤ M`) and from `r ≥ 17` (so `N ≥ 13`). No change.
2. Proof, 3 ⇒ 1 (imprecision): `r` is the least nonterminating odd seed overall, which lies in the interval because the interval contains one; the text says this implicitly. No change.
3. Frontmatter `depends_on` (imprecision): `finite-current-certificate-identity` is listed, but the proof uses only the `S`-invariance of `e` and the finiteness of `J`; nothing from that node is invoked. Harmless; no change.
4. Evidence path (cross-reference, fixed by the move): `../right-aligned-fixed-core-remainder/right_aligned_packets.py` did not resolve from the single-file location and is correct from the new folder.
5. Links (corrected): the node was a single file; moving it to `exact-current-prefix-criterion/README.md` required one more `../` on its three relative links, and the incoming links in `sparse-paired-exact-current-criterion/README.md` and `questions/packet-current-supply.md` were repointed. `MAP.md` is regenerated by `tools/build_map.py`.

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
