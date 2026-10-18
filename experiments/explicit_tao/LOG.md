# Explicit-Tao programme — LOG

Newest entries first. Each entry: iteration, what was done, checks run,
status label, primary source calibrated, and the C(δ) table at that time.

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
