# Explicit-Tao programme — LOG

Newest entries first. Each entry: iteration, what was done, checks run,
status label, primary source calibrated, and the C(δ) table at that time.

## Iteration 2 — 2026-10-18 late evening: Tao's architecture at the verified scale

- Verified the side lane's trace of v7 against the arXiv HTML: Theorem 3.1
  (`1 − O(log^(−c) N_0)`, `c` never numerical), `α = 1.001`, `n_0` with
  `2^(n_0) ≍ x^(0.1)` (5.1), `m_0 = ⌊(α−1) log x/100⌋` (5.2), window
  `I_y` (5.9) with half-width `log^(0.8) x`, (5.10)–(5.12), (5.16), (5.20);
  §6 `C_A` "sufficiently large depending on A"; §7 `ε < 1/100`,
  `exp(−ε³)`, `(1/10) log(1/ε)`.
- **Unit of work:** `lemmas/L4_tao_architecture.md` + `check_L4_window.py`
  (finite certificate): with the printed choices the first-passage window
  is empty unless `log x > 6.3 × 10^13` and `m_0 = 0` unless
  `log x >= 10^5`; at `x = 2^68`, `I_y = [22.0, −21.5]`. Status:
  **scoped barrier** (as written) + **candidate** (no re-optimisation
  inside the architecture reaches `2^68`). Calibrates Tao v7 §§1, 5–7.
- Wrote the Leg-1 post-mortem in STATE.md (decisive evidence; counter not
  used). Next: one bounded Leg-2 unit, then Leg 3.
- C(δ) table: the four target rows remain open; method lower bounds
  recorded (`>= exp(6.3e13)` for Tao's architecture as written).

## Iteration 1, lead from the side lane — 2026-10-18 evening

- The side lane pointed out that the audited AxiomMath library already
  contains a machine-checked explicit mixing estimate. Read the statements
  from the pinned source: primitive Fourier decay `C_*/n^(10241/4096)` with
  `C_* = (160 D_*)^(10241/4096)` and `D_*` a max of thousands-of-digits
  rationals; mixing lemma only for 3-adic levels `m >= 2^80000`;
  `N_* = 6103914`. Recorded in `lemmas/L4_formal_constants.md`
  (**calibration of a machine-checked source**; no re-derivation). Any
  `C(δ)` from these constants is `>~ 3^(2^80000)`; the machine-checked route
  contributes only the row `C = 1` at `δ = 1 − 2^(−2^(2^87640))`. This
  sharpens L4 into a numeric question about Tao's own exponent.

## Iteration 1, review follow-up — 2026-10-18 evening

- The side lane confirmed L2, L2′ and L3 by independent code
  (`claude/sidekick` a244490, probe `sidekick/probes/fable_L2_check.py`:
  Chernoff vs exact law n<=60, rate formula vs numerical minimisation,
  hockey-stick count, integer counts at X=2^20 for d∈{1,5}, affine identity
  and descent on 4,000 random odd N<2^64) and found one documentation
  error: the hand-quoted `I(θ)` values in the lemma note were off in the
  third decimal (three overstated). Corrected from the receipt. No computed
  result changes.

## Iteration 1 — 2026-10-18 evening

- Closed step (0): the AxiomMath Lean audit's external-checker replay
  (authors' comparator config: nanoda + Lean kernel, "Your solution is
  okay!"; paranoid run: nanoda, Lean paranoid kernel, lean4lean (39,480
  declarations), con-leche all accept; con-ron and `lake check --paranoid`
  still running) recorded on branch `claude/lean-audit`, PR #2.
- Created this branch from `origin/main`, with `STATE.md` (goal logic,
  lemma decomposition L1–L7, empty C(δ) table, blockers) and this log.
- **Unit of work: L2 + L3.** Written proof of the explicit valuation
  large-deviation bound with exact rate `I(θ) = θ log(2(θ−1)/θ) − log(θ−1)`,
  exact integer counting with boundary error `C(⌊θn⌋, n)`, and the
  one-round descent corollary `S^n(N) < N(3/2^θ)^n + (3/2)^n` off the
  exceptional set. Checker `check_L2.py` verifies the Chernoff bound
  against the exact distribution, the cylinder counts on actual integers
  (also for 3x+5), the affine formula and bound, and the integer tail
  counts; receipt `receipts/L2_receipt.json`. The first draft of L3 stated
  the multiplicative form `S^n(N) <= 3^n(N+1)/2^A`; the checker's exact
  test rejected it (word `(10,1)`: `C_w = 1027 > 9`) and the additive
  Terras form replaced it before any commit.
- Status: L2, L3 **written proof + finite certificate**; calibrates Terras
  1976 / Everett 1977 (cylinders and density of finite stopping time) and
  the standard Chernoff step of Lagarias's 1985 survey, Theorem B.
- C(δ) table: all four entries open (no iterated estimate yet).
