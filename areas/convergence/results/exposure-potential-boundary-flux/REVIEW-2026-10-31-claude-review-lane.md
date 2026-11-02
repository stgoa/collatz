# Review of exposure-potential-boundary-flux

Independent review (wave 7). Definitions were followed into [`right-aligned-fixed-core-remainder`](../right-aligned-fixed-core-remainder/README.md), [`disjoint-annular-recursion`](../disjoint-annular-recursion/README.md) and [`orbit-component-current-criterion`](../orbit-component-current-criterion/README.md). Scratch code lives outside the repository; every number below was computed by it or by the node's own proof.

## What I checked

- **Certificate.** `python3 tools/run_certificates.py --node exposure-potential-boundary-flux`: PASS, exit 0, 1.1 s wall (`check_duality.py` about 1 s; it compares with `duality_audit.json` and the two CSV tables).
- **Theorem 1, re-derived.** Necessity: pairing `μ = (I − P)J + ζ` with `q = 1_C` gives `⟨q, μ⟩ = Σ_x J(x)(q(x) − q(Sx)) + ⟨q, ζ⟩ ≤ 0`, since `q(1) = 0` absorbs the killed mass and `q(x) = q(Sx)` on every exposed arrow. Sufficiency: a component is closed under its exposed arrows, so routing every source coefficient along an undirected spanning tree to one anchor (1 for the absorbing component) leaves exactly the component mass at each other anchor; nonpositive masses give `ζ ≤ 0`. Isolated sources are singleton components, so their atoms must be `≤ 0`.
- **Proposition 2, re-derived.** A new arrow keeps the partition, merges two components (`max(u+v, 0) ≤ max(u, 0) + max(v, 0)`), merges a component into the absorbing one (its positive mass leaves the sum), or adds a new zero-mass vertex. The zero criterion is Theorem 1.
- **Theorem 3, re-derived.** For odd sources `1 < x ≤ N`: valuation 1 (`x ≡ 3 mod 4`) maps bijectively onto `y ≡ 5 mod 6`, `y ≤ (3N+1)/2`; valuation 2 (`x ≡ 1 mod 8`) onto `y ≡ 1 mod 6`, `y ≤ (3N+1)/4`; valuation `≥ 3` means `x = 4z + 1` with odd `z ≤ N/4` and `S(x) = S(z)`, so this part of `P U_N` is exactly `P U_(N/4)` (the source 5 is absorbed). Hence `P(U_N − U_(N/4)) = T_5(3N/2) + T_1(3N/4)` for `8 | N`, `ν_N = 3P(U_N − U_(N/4)) − U_(3N/2) − U_(3N/4)`, `V_N = 3P(F_N − F_(N/4)) − F_(3N/2) − F_(3N/4)`, `D_N = V_N + 3(I − P)(F_N − F_(N/4))`, and with `A_N = P V_N` (R6, reviewed) `V_N = A_N + (I − P)V_N`, which is (1). Pairing with `q`, `q(1) = 0`, gives (2); the flux vanishes on exposed rows and for a globally invariant indicator.
- **Independent computation** (scratch script `recompute_r10.py`, own `S`, `P`, `U_t`, `ν_N`, union-find). `A_N` recomputed as `P(ν_(64N) − ν_N)` equals the six-band table at `N = 8, 16, 24, 96, 112, 128, 144, 168, 512`, with `‖A_N⁺‖₁ = 99N/4`; identity (1) holds at all nine cutoffs. For `A_96`: `Φ = 2376, 787, 126, 48` at depths `0, 1, 5, 10`, `19` at depth 19, `17` at every depth 20–27, `0` at depth 28, nonincreasing throughout, equal to the receipt's trace. At depth 27 there is one positive component; it contains 1819, has 83 vertices, 31 source atoms, mass 17, scale pairing `⟨q, D_96⟩ = 10`, flux `−7`, and exactly the 11 flux rows of the table (`K_96 = 1` at 2553, 3639, 3831, 4095, 4311, 4539; `2` at 4851, 6057; `−1` at 6375, 9079, 9087), each with indicator difference `−1` and none an exposed arrow. Adding every arrow with tail in `supp K_96` leaves one positive component of mass 17, flux 0, scale pairing 17.
- **Theorem 1 on random graphs.** 400 random functional graphs on at most 5 vertices with sink 1, random exposed subsets and sources in `{−1, 0, 1}`: the component criterion agreed with a direct search for a current on the exposed arrows in every case.
- **Controls.** For `3x+5` (cycle `19 → 31 → 49`) and `3x+13` (fixed point 13), a unit source on the cycle keeps `Φ = 1` at every depth through 40, as Theorem 1 predicts: the component never contains 1. Theorems 1–2 are `d`-uniform; the open progress lemma is where `d = 1` must enter. Identity (1) uses the `3x+1` valuation partition and was not transferred.

## What I did not check

- The decomposition `P ν_N = Π_N + η_N` and `η_(64N) = η_N` (R2, R6: reviewed nodes), beyond recomputing `A_N = P V_N`.
- The parts of `check_duality.py` belonging to other nodes (binary projection, reflected annulus, the `19/22` collapse) and the `3x+61` remark.
- Anything about the open progress lemma; none is claimed.

## Findings

1. Proof of Theorem 3, "Valuation 1 maps bijectively to residue 5 modulo 6 up to `3N/2`" (imprecision): this describes `P U_N`, while the pushed measure is `U_N − U_(N/4)`; the identity holds because the valuation-`≥ 3` part of `P U_N` is exactly `P U_(N/4)`. The text states equal successors but not this cancellation. Derivation above.
2. Statement, Example (imprecision): that exposing every row of `K_96` "makes every component indicator's `K_96` flux zero" is immediate; the substantive, verified part is that one positive component of mass 17 remains with pairing 17 and that depth 28 resolves it.
3. Certificates (imprecision, already documented in the node): `check_duality.py` checks by `assert`, so it must run without `-O`, as CI does.

No error found.

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
