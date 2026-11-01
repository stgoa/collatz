# Review of two-inverse-phases-intermediate-increase

Independent review (Claude review lane, Fable 5.1), a different lane from the main lane that wrote the node (R50) and from the side lane whose meter is stored here. Every number below comes from my own code or from the node's proof.

## What I checked

- **Certificate.** `python3 tools/run_certificates.py --node two-inverse-phases-intermediate-increase`: `check_legacy_replay.py` PASS, exit 0, 15 s (replays `check_double_inverse.py` and `check_expanded_union.py`; both receipts unchanged).
- **Inputs.** [`base-inverse-phases-increasing-pairs`](../base-inverse-phases-increasing-pairs/README.md) (first phase, thresholds `h ≥ 3` / `h ≥ 5`), [`decreasing-w5-phase-inverse-barrier`](../decreasing-w5-phase-inverse-barrier/README.md) §1 (ancestor of a `4 (mod 9)` target), [`critical-image-rank-composition`](../critical-image-rank-composition/README.md) (bound `(9s+5)/8`, composition theorem), [`elementary-bridge-quotient-normal-form`](../elementary-bridge-quotient-normal-form/README.md); all `reviewed`.
- **Section 1, by hand and by code** (own `S`, `ν`, canonical, `ρ`; all 16,384 `W5` inputs below `2^17`, of which 301 lie in the domain with `L ≥ 3`). `k`, `h`, `C`, `b = 2kw+1`, `r = 2^(h+1)C − 1`: `r` is complementary canonical with `v2(r+1) = h+1`, the word `r → b` is `1^h`, `T(b) = 3w = q` (`S(b) = 2q+1` for `k = 4`, `F(q)` for `k = 8`). `L = v3(2r+1) ≥ 3` gives `r ≡ 4 (mod 9)` (already `L ≥ 2` does), `p + 1 = 2^L C'` with `C' ≡ −3^L (mod 4)`, so `p` is complementary canonical, `p ≡ 7 (mod 8)`, `p ≢ 2 (mod 3)`, the word `p → r` is `1^(L−1), 2`, every intermediate state is canonical, and `T^(h+L+1)(p) = q`. The critical child `v = p/3` or `(2p+1)/3` is `≡ 5 (mod 8)` because `p ≡ 7 (mod 8)`, with `ρ(v) = p`.
- **Section 2.** Identity (2) re-derived: `k·3^L(p − 3w) = (k·2^(h+L+2) − 3^(h+L+1))C + (3−k)3^L − k·2^L`. The coefficient of `C` is negative exactly for `h + L ≥ 5` (`k = 4`) and `≥ 6` (`k = 8`) (checked for `n = h+L ≤ 40`); the constant is negative. Below threshold the only rows with `h ≥ 1`, `L ≥ 3` are the four in the table, with constants `13C − 59`, `269C − 199`, `295C − 533`, `295C − 199` as displayed; `8^(−1) ≡ 17 (mod 27)` and `≡ 71 (mod 81)`, so `C ≥ 17` resp. `C ≥ 71` in rows one and three; all four are positive, so `p > 3w` and never `p = 3w`. Verified on every domain input below `2^17`: `p < 3w` iff the threshold holds, and all 177 failing inputs fall in the four rows.
- **Section 3.** The plan `J = A + B + K − N_w + H_v − H_z` built with my own currents and my own `W5`-only `H` for all domain inputs below 8192 and for 60 CRT members: divergence `P(w) − P(v) − Σ (A_v − A_z)(u) P(u)` exactly; in every accepted case all requests are `W5` with `ρ < q`, `ρ(u) ≤ (9v+5)/8 ≤ (3p+4)/4 < p` on `H_v`, `4z < w`; in every failed case the unique request of rank `≥ q` is `v` with coefficient `+1`. The five additional domains are populated below `2^17` with `(k,h)` counts `(4,1): 36`, `(4,2): 34`, `(8,1): 11`, `(8,2): 11`, `(8,3): 12`, `(8,4): 4`, all with `r > q` and `p < q`. Examples: `w = 53 → (q, r, p) = (159, 283, 111)`, `w = 37 → (111, 175, 103)`.
- **Section 4.** The CRT families (3) for `k ∈ {4, 8}`, `h = 1..6`, `L = 3..9`, three members each: `w ≡ 13 (mod 32)`, `3w` complementary with exponent 3 (nonselected), `3 ∤ w`, exact `h` and `L`, and the test outcome matches `h + L` against the threshold.
- **Section 5–6 and receipts.** Among the 8192 `W5` candidates below 65536: 153 domain inputs with `L ≥ 3`, 65 strict plans, and the six receipt classes by `(k, accepted, r > 3w)` reproduced exactly. My local plan for `w = 53` equals the stored plan in `w53_inputs.json` row for row (current and request vector); the stored output `w53_current.csv` has divergence `P(53)` with positive rows. Seven-rule union below 8192 with my own predicates for the seven rules: 195 under the earlier four rules, 442 under the seven, as in `expanded_union_audit.json`; 5 inputs are accepted only by this rule among the seven.
- **Controls.** The two phase identities are identities of the `3x+1` step; with `1` replaced by `5` they hold verbatim for `3x+5` (277 second phases checked). They have no absorption content (R43's composition reduces to premises), so the actual `3x+5` cycles are not excluded.

Scratch work: `rederive_r50.py` in my review folder.

## What I did not check

- The legacy scripts' internals and hashes beyond the replay (`double_inverse.py`, `expanded_union.py`, the dispatcher's priority order and its stored outputs other than `w = 53`).
- The side-lane meter (41–44% accepted share); it is a sample of the dispatcher and not part of the claim.

## Findings

1. Proof §1 (imprecision). "Since `r ≡ 4 (mod 9)`" is a consequence of the imposed `L ≥ 3` (indeed of `L ≥ 2`: `2r + 1 ≡ 0 (mod 9)`), not an extra hypothesis; the text should say so.
2. Statement 2 and claim (imprecision). "Then `p ≡ 7 (mod 8)`" reads as a consequence of the test; it holds for every domain input with `L ≥ 3`, since `v2(p+1) = L`, independently of whether `p < 3w`.
3. Statement 3 and claim (imprecision). The listed domains are the *additional* ones (`r > 3w`); the rule also accepts inputs already in R45's `G` (`h ≥ 3` for `k = 4`, `h ≥ 5` for `k = 8`, `L ≥ 3`), 8 of the 65 strict plans below 65536, as §3 notes ("add no new R45 domain"). The claim's "each have `r > 3w`" is right for the listed domains only.

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
