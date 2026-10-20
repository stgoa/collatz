---
id: right-aligned-reduction-independent-checks
kind: result
title: An independent implementation reproduces the right-aligned packets and checks R2–R4 (and R5, R6) on finite ranges
status: reviewed
claim: >
  Finite statements only, odd-only clock absorbing at 1, d = 1. Independent code (sharing nothing with
  right_aligned_packets.py) reproduces Π^R_N and η_N exactly for every 8 ≤ N ≤ 3000 and N = 4096 (η_N also at
  10001, 65537, 262144), and checks: the transfer identity 3E_T(N) − H_(T−1)(Π^R_N) = ⟨1, ν_N⟩ + H_(T−1)(η_N)
  for every 8 ≤ N ≤ 160 and every T up to extinction (largest gap 17); supp η_N ⊆ {5, 7, 11, 13} and
  ‖η_N‖₁ ≤ 6b for every N ≤ 10^5 and 3,132 sampled N ≤ 10^18; the dyadic table for b = 3…1500; the ratio
  bounds of the comparison function on 16 ≤ N ≤ 2·10^4 (maximum 0.96751); the valuation partition with
  orbit indicators for 8 ≤ N ≤ 4000; and the five-ray cutoffs and constant for 3 ≤ b ≤ 400 and the
  annular-recursion identities at 68 cutoffs (legacy R5, R6).
authors:
  - Claude PR1 lane (Opus)
created: 2026-10-17
depends_on: []
evidence:
  - "locally-collatz-like-control-barrier/reduction_audit.py, reduction_audit.json: the R2–R4 checks. The script fails at its new path (it reads the snapshot's data from its old relative location); passed on 2026-10-17 inside scripts/verify_all.py --cpp (legacy)"
  - "locally-collatz-like-control-barrier/affine_controls.py, negative_controls_audit.json: the agreement with the repository construction (d1_agreement). Fails at its new path; passed in the legacy gate"
  - "locally-collatz-like-control-barrier/main_claims_audit.py, main_claims_audit.json: the R5 and R6 checks (a certificate of that node; exits 0 at the new path)"
  - "locally-collatz-like-control-barrier/NOTE.md §§6 and 10, HANDOFF_FOR_MAIN.md §1"
reviewed_by:
  - by: ChatGPT main lane (Codex)
    date: 2026-10-17
    link: locally-collatz-like-control-barrier/PR1_REVIEW.md
    scope: "§1: 'valuable verification evidence'; finite checks, the general reductions resting on their written proofs. The combined verifier scripts/verify_all.py reproduced all five PR1 receipts; the focused review did not independently repeat the entire reported range"
aliases: [PR1-C1]
tags: [convergence, packet-currents, right-aligned, independent-check, finite]
---

# An independent implementation reproduces the right-aligned packets and checks R2–R4 (and R5, R6) on finite ranges

## Statement

The PR1 lane built the right-aligned packets of [`right-aligned-fixed-core-remainder`](right-aligned-fixed-core-remainder/README.md) from first principles, for the whole family `T_d` of [`locally-collatz-like-control-barrier`](locally-collatz-like-control-barrier/README.md), and checked the main lane's written statements at `d = 1` on these finite ranges:

| Item | Check | Range |
|---|---|---|
| Construction | `Π^R_N` and `η_N` equal the repository's | every `8 ≤ N ≤ 3000`, `N = 4096`; `η_N` also at `10001, 65537, 262144` |
| Fixed-core theorem, (3) | `3E_T(N) − H_(T−1)(Π^R_N) = ⟨1, ν_N⟩ + H_(T−1)(η_N)` exactly, `E_T` built from `Q_T` and `R_(r,T)` | every `8 ≤ N ≤ 160`, every `T` up to extinction; largest gap 17, within `8 + 30b` |
| Fixed-core theorem, (2) | `supp η_N ⊆ {5,7,11,13}`, `‖η_N‖₁ ≤ 6b` | every `N ≤ 10^5`, plus 3,132 sampled `N` up to `10^18` (including `2^b ± 1`, `2^b + 3`) |
| Dyadic table (7) | period-6 core remainder; transfer correction in `[−12, 1]` | `b = 3 … 1500` |
| Lemma 2 (`505/512`) | ratio bounds algebraic for `N ≥ 16`; numeric maximum ratio 0.96751 | `16 ≤ N ≤ 2·10^4` |
| Partition (6) | non-vacuous test with orbit indicators `f_z(x) = 1[z ∈ orbit(x)]`, `z ∈ {27, 31, 41, 47, 91, 103}` | `8 ≤ N ≤ 4000` |
| Least-exception arithmetic | `n_1 ∈ {r, r+1}`, `n_2 < r`; the predecessor of Lemma 3 | odd `r ≤ 10^6` |
| Five rays (legacy R5) | exact cutoffs `(n_0, n_1, n_2) = (M/4 − 1, 3M/2, 3M/4)`, upper targets, comparison exponents, every target with exponent below 3 lies below 96, constant `< 89/90` | `a ∈ {12, 14, 16, 18, 21}`, `3 ≤ b ≤ 400` |
| Annular recursion (legacy R6) | `Π_(64N) − Π_N` matches the six-band table mod 18 in `(Q, 64Q)`, `η_(64N) = η_N`, `supp Π_N ⊂ (1, Q)`, band totals 0, `Σ A_N = 0`, `Σ y·A_N(y) = 63Q`, `‖A_N‖₁ = 99N/2`, `‖A_N⁺‖₁ = 99N/4`, `|supp A_N| = 267N/8` | 68 cutoffs `N ∈ {8, 16, …, 512, 768, 1024, 2048, 4096}` |

All checks passed; no discrepancy was found. The partition test is needed because at `d = 1` the counting identity can only be tested with `e ≡ 0`; the orbit indicators satisfy `f_z(x) = f_z(Sx) + 1[x = z]`, giving `B_f(N) = B_f(n_0) − 1[z ≤ n_0] + B_(f,5 mod 6)(n_1) + B_(f,1 mod 6)(n_2) + 1[z ≤ N]`.

## Proof

Exact integer computation by the scripts listed under `evidence`, with receipts. The ranges are those printed in `reduction_audit.json`, `negative_controls_audit.json` and `main_claims_audit.json` (folder [`locally-collatz-like-control-barrier`](locally-collatz-like-control-barrier/README.md)). Of these, only `main_claims_audit.py` runs at its new path; the other two passed in the legacy gate and need their old layout (see `evidence`).

## Remarks

- **What this is not.** It is a finite, model-assisted check, not human peer review or formal verification; the general statements rest on their written proofs. Alongside these checks the PR1 lane re-derived the written arguments of the fixed-core theorem and of the qualitative criterion and found no gap, and re-read the five-ray proof (legacy `NOTE.md` §§6 and 10). Those re-derivations are recorded as reviews on [`right-aligned-fixed-core-remainder`](right-aligned-fixed-core-remainder/README.md) and [`qualitative-current-criterion`](qualitative-current-criterion.md), not as a claim of this node.
- **A by-product.** Lemma 3, that the `N^(3/2)` maximum principle is load-bearing, is recorded in [`qualitative-current-criterion`](qualitative-current-criterion.md).
- **Legacy R9 and R10.** The same lane also cross-checked two later main-lane claims; those checks are in [`progress-measures-control-3x-61`](progress-measures-control-3x-61.md).

## History

- Migrated from the legacy ledger entry C1 ("Independent audit of R2–R4 and of main's R5, R6, R9, R10"; `archive/docs/RESULTS.md`, legacy path) and `experiments/packet_currents/negative_controls/NOTE.md` §§6 and 10, at commit `be73a66`, by the B07 migration (Claude, Opus 5.5). Alias `PR1-C1`, not `C1`, to keep the PR1 series apart from the cycle series. The R5 and R6 nodes belong to a later migration batch (B08).
- PR1 lane (Claude, Opus), 2026-10-17. Main-lane review in `PR1_REVIEW.md` the same day.
