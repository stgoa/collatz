# Handoff from the independent lane

This note is for the agent working on `main`. It comes from a separate session working in parallel on branch `claude/claude-vs-chatgpt-perf-8230f6` (directory `collatz_research_20261017/negative_controls/`). It is written to stand on its own: every claim below can be re-derived from the repository definitions.

Ledger labels C1–C4 are deliberately outside your R-series so the two numberings never collide.

## 1. Your claims checked with independent code — all PASS

The code shares nothing with yours. It builds the right-aligned packets from first principles and matches the repository packets exactly for every `8 ≤ N ≤ 3000`.

- **R2–R4.** Every written statement rechecked from definitions. The transfer identity (3) is exact for every horizon, for `8 ≤ N ≤ 160`. The core bounds hold for every `N ≤ 10^5` and 3,132 sampled `N ≤ 10^18`. The dyadic table holds for `b ≤ 1500`.
- **R5 (five rays).** Cutoffs, upper targets, comparison exponents, the sub-96 boundary, and the `89/90` constant hold for all rays and `b ≤ 400`. The written proof was re-read and no gap was found.
- **R6 (annulus).** All 36 band coefficients, the supports, `η_64N = η_N`, `99N/2`, `99N/4`, `267N/8` and `63Q` hold for 68 cutoffs, up to `64N = 262144`.
- **R9 (compression).** `‖P A_N‖₁ = ‖R A_N‖₁ = 171N/4 − |c_N|` holds for those 68 cutoffs. The `2N` survivors are present, and `c_80000 = 0` (checked with a separate point evaluator).
- **R10 (Φ trace).** `Φ(A_96) = 17` at depths 20–27 and `0` at depth 28.
- **Working copy (17:54–18:00).** In `residual_progress/transport`, these all reproduce: the norms 4752, 4103, 3533, 3124; norm 13 and positive mass 4 at both `P^79` and `P^80`; and the nine-row `R P^78 A_96` table.

## 2. Certificate minimality (C3) — written proof

Let `J_0` be a finite exact current, `μ = (I−P)J_0`. Let `(J, ζ)` be any finite certificate with `μ = (I−P)J + ζ` and `ζ ≤ 0`, and suppose `supp(J − J_0)` contains no nontrivial cycle. Then `J ≥ J_0` pointwise.

*Proof.* Put `K = J − J_0`. Then `(I−P)K = −ζ ≥ 0`, so `K(y) ≥ Σ_{Sx=y} K(x)`. Hence every state with `K < 0` has a predecessor with `K < 0`. A finite set closed under taking such predecessors contains a cycle, which is excluded. So `K ≥ 0`. ∎

Consequences:

- The exact current is unique, and it minimises `‖J⁺‖₁` among all one-sided certificates.
- When the support terminates, `J_0(y)` is the signed source mass of `y`'s ancestors, `J_0 = Σ_j P^j μ`.
- *Check against the archive.* The stored currents at `N = 4096` (2,736 rows) and `N = 262144` (132,998 rows) equal `Σ_j P^j Π_N` **row for row**.

So there are no cheaper or alternative currents to search for. Constructing currents means describing this single object uniformly in N and proving it is finite.

## 3. A locally Collatz-like control where the criterion is false (C2) — finite certificates

Take `T_61(x) = (3x+61)/2^v` on odd `x`. It fixes 1 and 61, and has a 41-cycle with minimum 235. Use the same right-aligned packets, absorbing at `{1, 61}`.

- **What matches Collatz.** The core and every odd seed below 175 reach `{1, 61}`. The counting identity holds exactly with nonzero `e`. Packet work is bounded, and one-sided currents exist, at every cutoff `8 ≤ N ≤ 212`.
- **Where it fails.** `⟨e, Π_213⟩ = 1 > 0`, so there is no one-sided current and the work grows linearly. This is certified by explicit orbits.
  - 213 is the first cutoff `⌈(4r − d)/3⌉` at which the least exceptional seed `r = 175` enters component 2 with coefficient `+2`.
  - The same pattern holds for `T_13`: `r = 19`, first failure at `N = 21`.
- **On your five-ray grid.** Failures still occur, first at `N = 224` for d=61 and at `N = 96` for d=−1.

What this rules out:

- Any argument that would also apply verbatim to `T_61` cannot prove the right-aligned obligation.
- In particular, no induction on N that uses only generic properties can work.
- Finite forcing can only yield verification bounds. `T_61` satisfies the criterion on all of `[8, 212]` even though 175 is exceptional.

## 4. Your progress measures behave the same on `T_61` (C4) — finite certificates

Let `A'_N = Π'_{64N} − Π'_N` for `T_61`, at `N = 8, 16, 24, 32`.

- **Compression.** The one-pass ratio `‖P A'‖/‖A'‖` is 0.863, 0.855, 0.849, 0.853. Yours is `19/22 ≈ 0.864`.
- **Exposure.** `Φ` falls from 228–829 to 7–16 by depth 25.
- **Then it stops.** `Φ` stays at 7, 13, 13, 6 through depth 400. That value equals `⟨e, A'_N⟩`. The surviving component contains the whole 41-cycle, which is closed under `T_61`, so it can never be linked to an absorber.

Hence one-pass contraction and early `Φ` decay are not evidence that every positive plateau ends for `3x+1`. The open progress lemma has to use some property of `3x+1` that `T_61` lacks.

## 5. Suggested uses

1. Run any candidate constructor, progress argument, or checker on the controls: `(d, N) = (61, 213)`, `(−1, 16)`, and `A'_8` for `d = 61`. Anything that "succeeds" there is wrong.

   The checker command is `python3 collatz_research_20261017/negative_controls/affine_controls.py --check CERT.json`. The file format is `{"d":1, "N":32, "J":{...}, "zeta":{...}}`. Exit status 0 means valid.
2. When a step is claimed to make progress, name the d=1-specific fact it uses.
3. Treat the remaining obligation as Collatz-equivalent at each reformulation. Report partial-mass percentages as data, not progress.
