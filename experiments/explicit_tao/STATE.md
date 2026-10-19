# Explicit-Tao programme — STATE

**Updated: 2026-10-18, iteration 1. Branch `claude/explicit-tao`. Collatz
remains open; nothing here claims otherwise.** This file is the resume
point for the self-paced research loop: read it first, do one bounded unit
of work, update it, commit, push.

## Goal and logic

[A] (machine-checked; see PR stgoa/collatz#2, `lean/audit/` on
branch `claude/lean-audit`): for every target `t` with `3 ∤ t`, a positive
proportion `c(t)` of integers reach `t` (`c(t)=1/(t^4·2^2^2^87640)`,
cutoff `2^(t^3·2^2^2^87640)`, logarithmic clock). Consequence: if some `n`
never reaches 1, take `a = S(n)` (never divisible by 3); every predecessor
of `a` is bad, so the bad set `B` has lower natural density `>= c(a) > 0`,
hence lower logarithmic density `>= c(a)` (Abel summation). Therefore

> Collatz ⇔ `B` has logarithmic density 0 ⇔ log-almost all orbits dip
> below the verified range `V` (all `N <= V` reach 1; `V = 2^68` per the
> published Barina verification, to be cited exactly before use).

Tao 2019 (arXiv 1909.03562, corrected v7 of 2026-07-16) proves: for every
`f → ∞`, `Col_min(N) < f(N)` for log-almost all `N`. The gap between
"`f → ∞`" and "`f = V`" is the whole conjecture.

**Main target.** An explicit function `C(δ)` with: all but logarithmic
density `δ` of positive integers have an orbit dipping below `C(δ)`.
Tabulate `C(δ)` for `δ ∈ {0.9, 0.5, 0.1, 0.01}`. Any `δ < 1` with
`C(δ) <= V` is a new theorem ("an explicit proportion `1−δ` of integers
reach 1"). Report honestly how far `C(δ)` is from `V` and why.

## Lemma decomposition of Tao's argument (to be made explicit)

| Lemma | Content | Status | Transfer to 3x+d |
|---|---|---|---|
| L1 | Exact valuation cylinders: the first `n` Syracuse valuations `(a_1..a_n)`, `A = Σ a_i`, are determined by `N mod 2^(A+1)`; each word is exactly one odd class | written proof (frozen repo S.1; handoff §2.3; Terras 1976) | transfers |
| L2 | Explicit large deviations for `A`: Chernoff with exact rate `I(θ)`; integer counts with boundary error `C(⌊θn⌋, n)` | **written proof + finite certificate (iteration 1)**: `lemmas/L2_valuation_tail.md`, `check_L2.py` | transfers (checked for d=5) |
| L3 | One-round explicit descent: outside an explicit exceptional count, `S^n(N) < N(3/2^θ)^n + (3/2)^n` (additive term from `C_w/2^A <= (3/2)^n − 1`; a first multiplicative draft was false and was caught by the checker) | written proof (iteration 1, corollary of L1+L2) | transfers |
| L4 | Syracuse random variables `Syrac(Z/3^n)` and their mixing (Tao Prop. 1.17, §§3–4): explicit Fourier/total-variation bound | **open — the crux.** Part 0 done: a machine-checked explicit variant exists in the AxiomMath library (`lemmas/L4_formal_constants.md`): Fourier decay `C_*/n^(10241/4096)` with a thousands-of-digits `C_*`, mixing only for 3-adic levels `m >= 2^80000`; any `C(δ)` from it is `>~ 3^(2^80000)`, hopeless against `2^68`. Tao's own constants (`exp(δ^(−O(1)))`, Remark 1.4) remain to be traced; the target exponent is below ~5.6 at δ=1/2, below ~36 at δ=0.9 | model statement, d-blind |
| L5 | Renewal / first-passage transfer from the random model to actual integers with explicit error (Tao §§5–6) | open | transfers |
| L6 | Iteration across scales in logarithmic density, summable explicit errors; assembly of `C(δ)` | open | transfers |
| L7 | Verified range: every `N <= V` reaches 1 (computational, published) | published; not re-run here | **d-specific** (false for d=5: 19→31→49) |

## Post-mortem for Leg 1 (written at iteration 2, 2026-10-18 late evening)

**What was attempted.** Make Tao 2019 explicit and read off `C(δ)`.

**Why it cannot close the target.** Two independent readings (this lane
and the side lane) of v7 agree on the printed parameter choices: the
auxiliary scales of the proof are powers of `log x` — the first-passage
window has half-width `log^0.8 x` around a centre that moves by only
`(α−1) log x / log(4/3)` with `α = 1.001`, the 3-adic level is
`m_0 = ⌊(α−1) log x / 100⌋`, the union bound needs
`exp(−c log^0.2 x) <= log^(−10) x`. The finite certificate
`check_L4_window.py` shows the window is empty unless
`log x > 6.3 × 10^13`, and `m_0 = 0` unless `log x >= 10^5`. At the
verified range `log x = 47`. So, as written, the method certifies no
`C(δ) < exp(6 × 10^13)` for any `δ < 1`; the constants `c`, `C_A`, `ε`
(none of which the paper gives numerically) never enter. The
machine-checked AxiomMath variant (part 0) is worse still (`m >= 2^80000`).
Re-optimising the free parameters inside the same architecture is judged
(candidate, `lemmas/L4_tao_architecture.md`) unable to bring the vacuity
threshold within many orders of magnitude of `log x = 47`.

**What was learned that stays true.**
1. With [A] machine-checked, Collatz ⇔ `B` has logarithmic density 0 ⇔
   log-almost all orbits dip below the verified range. This is the
   sharpest honest form of the remaining problem.
2. The d-specific step of any such proof is the verified range itself
   (L7); everything else in the averaging toolbox is d-blind.
3. Explicit one-round descent (L2/L3) is cheap and exact; iteration is
   what fails, and it fails for architectural reasons at fixed scale.
4. A fixed-scale version would need mixing statements with no
   `log x`-sized auxiliary windows. None is known; this is the precise
   research gap, and it is not a constants problem.

**Decision.** Leg 1 is closed as a scoped barrier (two units: L2/L3 proved;
L4 parts 0–1 recorded). Leg 2 receives one bounded unit next: state
exactly what dichotomy [A] already gives (it already yields "`B` empty or
lower density `>= c(a)`") and what the needed converse would require; if
that unit produces no proved lemma, move to Leg 3 (cycle exclusion), the
one leg where explicit, checkable progress is realistic.

## Explicit-constant table (the progress metric)

| δ | C(δ) | derivation | status |
|---|---|---|---|
| 0.9 | — | — | open |
| 0.5 | — | — | open |
| 0.1 | — | — | open |
| 0.01 | — | — | open |
| `1 − 2^(−2^(2^87640))` | `1` (reaches 1), natural density, `N >= 2^2^2^2^87640` | [A], `Main.positive_density_collatz_reaches_one` | machine-checked; calibration only, useless for the target |

Lower bounds on what the available methods can give (not upper-bound
theorems): the AxiomMath mixing lemma, no `C(δ)` below about `3^(2^80000)`
for any `δ` (`lemmas/L4_formal_constants.md`); Tao's architecture with its
printed parameters, no `C(δ)` below `exp(6.3 × 10^13)` for any `δ`
(`lemmas/L4_tao_architecture.md`, `check_L4_window.py`). The target
`2^68 = e^47` is unreachable by both.

What L2/L3 already give (iteration 1): a one-round statement at scale `X`
with exceptional fraction `e^(−n I(θ)) + 2 C(⌊θn⌋,n)/X` and descent factor
`(3/2^θ)^n`; the explicit `(θ, I(θ), descent)` trade-off is tabulated in
`receipts/L2_receipt.json`. This is not yet a `C(δ)`: iterating rounds
needs L4–L6.

## Open lemmas and blockers

1. **L4 constants.** Read Tao v7 §3 (Fourier decay of the Syracuse random
   variables) and §4 and extract every implied constant. Expect
   `C(δ) ~ exp(δ^(−O(1)))`; the question is the exponent, which must be
   below ~5.6 (δ=1/2) or ~36 (δ=0.9) for `C(δ) <= 2^68`. The
   machine-checked AxiomMath constants are known to be hopeless for this
   (part 0 above), so no further time goes into tightening that proof.
2. **Bookkeeping choice.** Which first-passage/log-density formulation
   (Tao's, or a direct dyadic-block version) gives the cleanest explicit
   error accumulation in L6.
3. **Literature check before deriving.** Search for any existing explicit
   version of Tao's constants (none known as of iteration 1).
4. **Citation of `V`.** Pin the exact published verified bound and its
   clock before it is used in any theorem statement.

## Consecutive iterations without a new explicit constant or proved lemma: 0

(Iteration 2 produced a finite certificate and a scoped barrier rather than
a new `C(δ)`; the Leg-1 post-mortem was written immediately because the
evidence was decisive, not because the counter reached three.)

## Legs

- **Leg 1 (main):** L1–L7 above.
- **Leg 2 (secondary):** a density dichotomy for the invariant bad set `B`
  (density 0 or `>= c` for the explicit `c` from [A]) using invariance
  inside Tao's framework. Not started.
- **Leg 3 (background):** extend `m`-cycle exclusion beyond Hercher's 91
  local minima (Baker-type bounds plus computation). Not started.

## Rules in force

Never claim a proof of Collatz. Every constant, clock, quantifier and
dependency explicit. Status labels: written proof / finite certificate /
candidate / open / refuted. d-controls: each estimate is checked for 3x+5;
only L7 is d-specific. No new frameworks, viewpoints, dispatchers, rule
catalogues or route maps. Three consecutive iterations without a new
explicit constant or proved lemma trigger a one-page post-mortem here and a
move to the next leg.
