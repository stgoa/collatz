# Review of predecessor-density-conditional-reconstruction

Independent review of [`README.md`](README.md), [`audit_notes.md`](audit_notes.md) and [`transfer_scope.md`](transfer_scope.md). Scratch scripts (outside the repository): `review-work/predecessor-density-conditional-reconstruction/recheck_arith.py`, `controls_3xd.py`.

## What I checked

- **Certificate.** `python3 tools/run_certificates.py --node predecessor-density-conditional-reconstruction`: PASS, exit 0, 0.88 s wall. I read `check_audit.py`: it tests exact finite laws, three central histories at `b_0 = 325, 500`, 64 histogram fibres, eight signed transfers, 108 branch/tail identities, the `d`-controls and six rejections, against the receipt. It certifies finite arithmetic only, as its scope string says.
- **Single-block bounds (audit §2).** Re-derived (1): `β ≤ (3/2)^s − 1 < 2^b` from `s ≤ 8b/5` and `(3/2)^8 < 2^5`; the weight window `2^(−K−1)(3/4)^b ≤ ω ≤ 2(3/4)^b` from the two ceilings in `H_b`; (2) from `R − β ≥ R/2`; (3) from `(4/3)^5 > 4`.
- **Histogram lemma (7)–(8).** Re-derived: sources of one `(D, A)` group lie in an interval of length `≤ 2^(b_0+1)/W`, spacing `≥ 3^q` in a class, so weight `· 3^q ≤ 2^(b_0+1) + 3^q W ≤ 2^(b_0+1) + 16^(b_0)(9/16)^(b_n)` using `q ≤ 2b_n`; (8) with `P_n ≤ 6(4b_0^(3/5)+1)(n+1)^3 G^n`, which needs `G ≥ 1.01^(3/5)`, i.e. `2013^5·100^3 > 2000^5·101^3`.
- **Mixing step (10)–(13).** The reference recursion `Y_(q+1) = 2^(−E)(3Y_q + 1)` gives `ρ_Q = Σ_w T_(w,Q) ρ_(Q−|w|)` over words of a fixed depth, so for a prefix-disjoint family the omitted complement is nonnegative with mean `(2/3)(1 − p(V))`; (10) is then the triangle inequality with (9) applied at `m = k ≤ Q − d` and `m = ℓ`. Pairing with the same physical histogram and (8) gives `|Z_(n+1) − Z_n| ≤ E_n`; `q_1 = G(200/201)^6 < 1` and `q_2 = G·2^(−1/100) < 1` are the comparisons `2013·200^6 < 2000·201^6`, `2013^100 < 2·2000^100`. The admitted blocks are prefix-disjoint by the first-crossing rule. Exact finite laws for `q ≤ 4`: mean `2/3`, unit support, marginal compatibility and the normalisation identity (2) of `transfer_scope.md` hold exactly (code).
- **Concentration exponents.** From `2 exp(−min(v²/(32t), v/8))` with `t ≤ 2b`: deviation `e_b ≥ b/200` gives `b/2560000` (4); `b/16` gives `b/16384` (7); `m_b/3` gives `m_b²/(576 b)` (12). The barrier gaps `H(ℓ) − 2ℓ = u + 2e_b` and `2h − H(h) = 2r_b + 2e_b − u` re-derived; early or late crossing outside `|s − b| ≤ m_b` forces a deviation `≥ (2 − log₂3) m_b − 1 ≥ m_b/3` for `m_b ≥ 13`. The series majorants `e^(−x) ≤ k!/x^k` behind `D_s`, `C_s` and `4·6!·2560000^6 ≤ C_s` checked.
- **Scales (README §4).** `r_b ≥ (3g/5 − 1/50)b − g − 1` by hand; (12), (13) and (16) verified for `325 ≤ b < 20000`; the exponent `σ_n + K_n + 1 + g b' − r_b − r_(b')` bounded by `4 − 83b/2500` as displayed. The first stage `n ≥ 400` with `325(201/200)^n ≥ 200(4(n+1)² + 1)` is `n = 3447`, and `((n+2)/(n+1))² ≤ 201/200` for `n ≥ 400`.
- **Terminal and counting steps (§§5–7).** `Ψ_j(x) = 4^j x + (4^j − 1)/3` and the weight factor `4^(−j)` re-derived; (15), the class bound `≤ 33X/3^(k_n)` from (16), (18), the budget `p − p/4 − p/8 − p/8 = p/2`, (19) `η = 9p/(32·3^m)` from `m² ≥ 176 M C_*/p`, and (20) `c_a = 9p/(1024 M 3^m)` all re-derived. Root family: `R_j = (2^(e+2j)a − 1)/3` integral, odd, positive, reaching `a` in `1 + e + 2j` ordinary arrows, `v₃(R_(j+h) − R_j) = v₃(h)` (`v₃(4^h − 1) = 1 + v₃(h)` checked to `h < 3^7`), for twelve targets including even ones.
- **Transfer to `3x+d` and controls** (`controls_3xd.py`, exit 0, 54 s): for `d ∈ {5, 7, 13, 61}` and a target `a` inside an actual cycle (`19, 5, 131, 235`), 81 consecutive roots `R_j = (2^(e+2j)a − d)/3` are integral, odd, positive, reach `a` under `C_d`, represent every class mod `3^4`, and at most one of the first 30 is periodic (`49, 11, 1393, 293`), as §5 of `transfer_scope.md` says; `S_d(dm) = d S_1(m)`; the predecessors of a target divisible by 3 below `5·10^4` are exactly its multiples by powers of 2. The conjugation `μ_(q,d)(y) = μ_q(d^(−1) y)` follows from `Y = dZ` in the recursion. No step of the node excludes these cycles; the lower bound is compatible with the density-`1/d` nonabsorbing sector.

## What I did not check

- Tao's Proposition 1.14 (external, `cited`), and whether the corrected v7 states it for all `1 ≤ m ≤ q` in the normalisation of `transfer_scope.md` §1: I had no access to the text.
- The exact numerical constants `C_(b_0)`, `C_s`, `D_s` beyond the inequalities above; `M_(n,X)` and `Z_n` were checked for structure, not recomputed on an actual root; the restricted terminal histograms per shift (§2.1) only by the argument given.
- The Mazur manuscripts themselves; the review concerns the node's own chain.

## Findings

1. **README §3 (imprecision).** "composing the finite central transfers through stage `N` gives a function on a fixed ternary residue space" does not name the modulus (`3^t`, `t` = total depth through stage `N` plus `k_N`) in which the root's residue is fixed, nor say explicitly that `Z_N(M)` equals that function at `M`'s residue; both follow from audit §5, but the reader must supply them.
2. **README §2.1 (imprecision).** The bound (4) is stated for the unfiltered terminal words with cap `K_n` while the central code uses cap `K_j`; the depth used (`≤ 2b`) is correct since terminal depths are `≤ h_b ≤ 8b/5`.
3. **Claim and `assumes` (imprecision).** The claim's conditional premise is Tao's proposition only; the controls paragraph of the Remarks, correctly, asserts no transfer of Lau's constants. Consistent, no change.

## Verdict

**HOLDS**, conditional on the imported mixing estimate (T) as stated: every displayed inequality, identity and case split that I could re-derive is correct, the finite laws and constants are exact, and the transfer to `3x+d` with its controls is consistent. The three findings are imprecisions.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
