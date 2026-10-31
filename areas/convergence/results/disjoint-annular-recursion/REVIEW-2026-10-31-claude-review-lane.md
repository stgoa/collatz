# Review of disjoint-annular-recursion

## What I checked

- **Certificate.** `python3 tools/run_certificates.py --node disjoint-annular-recursion`: `PASS`, exit 0, 5 s reported by the runner (5.58 s wall for the whole call). The replay runs the unmodified `check_annular_recursion.py` against `right_aligned_packets.py` in the rebuilt legacy tree and requires every copied file byte-identical afterwards.
- **The recursion, re-derived.** From formula (1) of [`right-aligned-fixed-core-remainder`](../right-aligned-fixed-core-remainder/README.md): `(2^(a+6) − 1)/3 = 64·(2^a − 1)/3 + 21` and `(5·2^(a+6) − 1)/3 = 64·(5·2^a − 1)/3 + 21`, so `q_(a+6) = 64q_a + 21`, `M_(a+6) = 64M_a`, `e_(a+6) = e_a`, and `t_0` depends only on the parity of `a`. For `8 | N` the cutoffs `3N/2`, `3N/4` are even and `q_a` is odd, so `n_i − q_a` is odd and its residue modulo the even `M_a` is at least 1; subtracting `21/(64M_a) < 1/M_a` cannot cross an integer, also for negative quotients under floor semantics. Hence the lift counts, leftover counts and triple partitions agree, `x' = 64x + 21 ≡ x (mod 3)` keeps every coefficient, and `b(64N) = b(N) + 6` (checked for powers of two and for other `N` separately).
- **New valuations `1..6` at `64N`.** `96N` and `48N` are multiples of `3·2^(a+1)` for `a ≤ 6` and `8 | N`; since `0 < q_a < M_a`, the last lift index is `n_i/M_a − 1`, so the lift count is `n_i/M_a` (odd `a`, `t_0 = 0`), divisible by 3, or `n_i/M_a − 1` (even `a`), `≡ 2 (mod 3)`. The leftover sources are `9, 17` (`a = 2`), `37, 69` (`a = 4`), `149, 277` (`a = 6`) at endpoints `7, 13`; combined coefficients `(−2, 1)`, `(1, −2)`, `(1, 1)`, total `(0, 0)`. So `η_(64N) = η_N` and `A_N` is the full pushforward of valuations `1..6`.
- **Bands.** `x_a = (2^a y − 1)/3` is an integer iff `y ≡ (−1)^a (mod 3)`; `x_a ≤ 96N` iff `y ≤ 2^(7−a)Q + 2^(−a)` and `x_a ≤ 48N` iff `y ≤ 2^(6−a)Q + 2^(−a)`, with even thresholds and odd `y`; so band `j` takes outer `a ≤ 6 − j`, inner `a ≤ 5 − j`. Below `Q` all three valuations of each parity occur and `x_(a+2) = 4x_a + 1` cycles the residue mod 3. The table recomputed from the displayed formula agrees at all 54 (band, odd residue) pairs; row sums 0; weighted residue sums `(−18, −36, −18, 18, 36, 18)` with `Σ 2^j w_j = 1134 = 18·63`; absolute sums `(4, 8, 10, 10, 8, 4)` with `Σ 2^j s_j = 396`; supports `(3, 6, 5, 5, 6, 3)` with `Σ 2^j = 267`; blocks per band `2^j Q/18 = 2^j N/8`. Disjointness: an odd endpoint is at most `(3(n_1 − 1) + 1)/2 = Q − 1`.
- **Independent code** (`review_annular.py` in my scratch folder; my own implementation of `Π^R_N`, `η_N` from the written definition, not the legacy module). At the 67 cutoffs `N ∈ {8, 16, …, 512, 1000, 2048, 4096}` (expanded cutoffs to 262144): `Π^R_(64N) − Π^R_N` equals the table measure; `η_(64N) = η_N`; both supports; every band total; `Σ y·A_N(y) = 63Q`; the three norms; `V_N` equals the displayed three-interval measure and `P·V_N = A_N`; the floor lemma for every valuation and both components; the divisibility, lift counts and leftover pairs; and `P ν_N = Π^R_N + η_N` at `N` and `64N` as a sanity check of my implementation against the dependency. Also `Π^R_(64²N) = Π^R_N + A_N + A_(64N)` with `η` unchanged and the norm and atom recursions for `h = 2` at `N = 8, 16, 24, 40`. All passed in 4.3 s.
- **Quotient identity.** I derived the exact identity `ν_N − (3U_N − 3U_(n_0) − U_(n_1) − U_(n_2)) = −(I − P)(3U_N − 3U_(n_0))` from the valuation partition (`4j+3 → 6j+5`, `8j+1 → 6j+1`, `4z+1` and `z` share their image), verified it exactly at `N` and `64N` for every `8 | N ≤ 256`, and with `U_(16N−1) = U_(16N)`, `U_(N/4−1) = U_(N/4)` obtained the displayed `[A_N] = 3[F_N] − 3[F_(N/4)] − [F_(3N/2)] − [F_(3N/4)]`. The `h`-fold recursion, `11N/14·(64^h − 1)`, `267N/(8·63)·(64^h − 1)` and the limits `11/14`, `89/168` follow from disjoint supports and geometric sums.
- **Corollary input.** The 30 initial cutoffs `a·2^r` are distinct, divisible by 8, largest 5376, endpoint bound `9N/4 − 1 = 12095`; all 6048 odd seeds below 12096 reach 1, largest odd-only hitting time 98 (my own iteration). The PR1 review of [`five-ray-current-criterion`](../five-ray-current-criterion/README.md) had excluded this corollary.
- **Controls** (the remark "specific to `d = 1`"). For `3x+d`, `q_a(d) ≡ (2^a − d)·3^(−1) (mod 2^(a+1))` gives `q_(a+6)(d) ≡ 64q_a(d) + 21d`, and the floor argument needs `21d/64 < 1`, i.e. `d ≤ 3`. With this natural generalisation and the same cutoffs, the shift identity (`a ≤ 13`) and the lift-count invariance (`N ≤ 256`) both fail for `d = 5, 13, 61`, consistent with the remark and with the PR1 note that `T_61` has no exact `×64` recursion. I did not reconstruct the PR1 lane's `T_d` packets.

## What I did not check

- The general proof of `P ν_N = Π^R_N + η_N` (a reviewed node; re-confirmed only numerically here).
- The five-ray maximum principle that the corollary rests on (reviewed node).
- The later nodes cited in the remarks. Novelty.

## Findings

1. Proof, "The recursion" (imprecision): "its fractional quotient by the even integer `M_a` is at least `1/M_a`" means the fractional part of `(n_i − q_a)/M_a`; correct as such, because the residue of an odd number modulo an even `M_a` is odd. No change.
2. Proof, "The recursion" (imprecision): the lift counts at `64N` are `n_i/M_a` (odd `a`) and `n_i/M_a − 1` (even `a`); the proof states only their residues mod 3, which is all it needs. No change.
3. Statement, corollary (imprecision): the existence of exact currents for the 30 initial packets rests on the finite check below 12096 recorded in `five-ray-current-criterion`, whose review did not cover that corollary; re-checked above. No change.

No error found; every displayed statement the dependents cite (recursion, table, band totals, moments, norms, `V_N`) was re-derived and re-computed.

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
