# Review of band-three-ordering-extension

Independent review of the attempt (legacy S03). The question for an attempt is whether "Why it fails" and "What survives" are correct and claim nothing unproved. Scope of the node: raw odd-only `3x+1` (`q = 1`), primitive integer cycles with `H < 16L`, the inversion pair `(n, 8n+1)` at heights `(0, 3)`; no cycle is excluded.

## What I checked

- Read `AGENTS.md`, `conventions/SCHEMA.md`, `conventions/NOTATION.md` §3, `CONTRIBUTING.md` ("Review a node"), `areas/cycles/OVERVIEW.md`, the node, and its dependencies [`q-one-inversion-pair-reduction`](../../results/q-one-inversion-pair-reduction/README.md) (formal) and [`dyadic-order-lemma`](../../results/dyadic-order-lemma.md) (reviewed); also [`three-band-collatz-cycles-are-ordered`](../../results/three-band-collatz-cycles-are-ordered.md) and [`paired-state-run-law`](../../results/paired-state-run-law.md) for the cross-references.
- **§1, re-derived.** With `z_i = n_i/2^(h_i)` and `F_i = 3z_i + q/2^(h_i)`: for `h_j = h_i + k`, `z_j − z_i = r/2^(h_j)` with `r = n_j − 2^k·n_i`, so `F_j − F_i = 3r/2^(h_j) + q(2^(−h_j) − 2^(−h_i)) = [3r − q(2^k − 1)]/2^(h_j)`. `r` is odd (`n_j` odd, `2^k·n_i` even) and positive (`z_i < z_j`). At `q = 1`: `k = 1` needs `3r < 1`, `k = 2` needs `3r < 3`, impossible for `r ≥ 1`; `k = 3` needs `3r < 7`, so `r = 1`. Equality `3r = q(2^k − 1)` means `3n_j + q = 2^k(3n_i + q)`, so `S(n_i)` and `S(n_j)` differ by a power of 2 and are both odd, hence equal, hence `n_i = n_j`: excluded by primitivity. Sorted adjacency: no `odd/2^h` with `h ≤ 3` lies in `(n, n + 1/8)`. With `B ≤ 3` the only inversion has `k = 3`, heights `(0, 3)`. All as stated.
- **§2, re-derived.** `3(8n+1) + 1 = 4(6n+1)`; `3(6n+1) + 1 = 2(9n+2)`, odd for odd `n`; then `27n + 7`. `9n + 2 ≤ H < 16L ≤ 16n` gives `n < 16L/9`. Checked numerically for every odd `n < 10^5`: 0 violations.
- **§3, re-derived.** From `n_(t+h) = 2^K·n_t − c` and `3n_t = 2^(a_t)·n_(t+1) − q`: `n_(t+h+1) = 2^(K + a_t − a_(t+h))·n_(t+1) − (q·2^K + 3c − q)/2^(a_(t+h))`; at `q = 1` this is the node's recursion, closing at `(3, −1)`. Verified with exact rationals along the full period on all 37 `(n, 8n+1)` pairs found at `q > 1` (the `q`-general form): the identity holds at every step and `(K_m, c_m) = (3, −1)` in every case.
- **§4, data.** The probe `s3_inversion_pairs.py` re-run with `areas/cycles/results/ordered-gap-closed-form/` on `PYTHONPATH`: exit 0, 50.7 s wall, receipt byte-identical to `s3_inversion_pairs.json`. Independent re-count with my own cycle finder and exact arithmetic (odd `q < 400`, `3 ∤ q`, odd seeds `≤ 6001`, 4000-step cap): 719 cycles with `m ≥ 2`, 37 pairs `(n, 8n+1)` at height gap exactly 3, the four quoted examples `(121, 35, 46)`, `(175, 29, 12)`, `(181, 23, 10)`, `(191, 47, 24)` present with heights `(0, 3)`. The inversion formula tested on all 133,155 pairs `z_i < z_j` of those cycles: 24,447 inversions, the equivalence `F_j < F_i ⟺ (h_j > h_i and 3r < q(2^k − 1))` holds in every case, no ties, `r` always positive and odd.
- **Lean lane's precision.** The `3x+121` cycle through 35 and 281 has `m = 46`, `L = 19`, `H = 1097`, `H/L = 57.7 > 16`: correct.
- **Controls** `3x+5`, `3x+7`, `3x+13`, `3x+61` (seeds `≤ 20000`): the formula holds on all 1,274 pairs; inversions occur at `q = 7` (`k = 1`), `q = 13` (`k = 3`), `q = 61` (`k = 1..5`), none at `q = 5`; none of the four contains a `(n, 8n+1)` pair at gap 3. The node excludes nothing, so no control can contradict it.

## What I did not check

- The Lean declarations behind `q-one-inversion-pair-reduction` (not rebuilt here).
- §2's "a positive density of `n` survives any finite number of steps": plausible (each step adds one 2-adic condition and the band inequalities are satisfiable for suitable valuations), but informal; the node uses it only to say that no finite-step contradiction is known.
- §3's judgment "not easier than the general one", and the third bullet of "What survives" (a pointer to S02 and S04).

## Findings

1. **Imprecision (claim field).** "odd `q < 400`" omits "`3 ∤ q`", which the body and the probe use. Corrected: ", 3 ∤ q" added to the claim.
2. **Imprecision (evidence receipt).** The probe caps `r < 14q`, so its inversion counts for `k ≥ 6` are undercounts (complete counts: `k = 6`: 1465 vs 1360; `k = 7`: 912 vs 722; `k = 8`: 548 vs 388; `k = 9`: 351 vs 236; `k = 10`: 165 vs 115; `k = 11`: 84 vs 57; inversions exist up to `k = 15`). The node quotes only "inversions at every height gap `k = 1…11`", which stands; the `k = 3`, `r = 1` count is complete.
3. **Remark (strengthens "Why it fails").** Of the 37 pairs, 16 have heights exactly `(0, 3)`, and one lies in a cycle with `H < 16L`: `3x+229`, cycle `(29, 79, 233)`, word `(2, 1, 5)`, `B = 3`, `H/L = 8.03`, with the inversion `F(233) = 116 < 316 = F(29)`, `r = 1`. So the band-3 inversion configuration itself is realised at `q = 229`: the inversion lemma together with the band constraint cannot exclude the pair, exactly as "Why it fails" says. The Lean lane's precision (the listed examples have `H > 16L`) is correct for the twelve examples in the receipt.
4. **Imprecision (evidence).** The probe does run at its new path once the helper's folder is on `PYTHONPATH`, and reproduces its receipt byte for byte.

## Verdict

HOLDS WITH CORRECTIONS. Correction applied: finding 1 (the hypothesis `3 ∤ q` added to the claim). Findings 2–4 are recorded under History; no claim changes.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
