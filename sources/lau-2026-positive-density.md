---
id: lau-2026-positive-density
kind: source
title: "Lau / AxiomMath: explicit positive lower density of predecessors (Lean)"
status: replayed
citation: >
  K. Lau, "Explicit positive lower density for the Collatz Conjecture", Hexagon 2610.00249v1
  (2026-10-14), with the Lean development AxiomMath/CollatzPositiveDensity at commit
  3a38bfbb70379e051b51155def1423846fab3a90. Hexagon is not arXiv.
url: https://github.com/AxiomMath/CollatzPositiveDensity/tree/3a38bfbb70379e051b51155def1423846fab3a90
created: 2026-10-18
tags: [predecessors, density, lean, external-library, ai-generated]
---

# Lau / AxiomMath: explicit positive lower density of predecessors (Lean)

## Citation

Kenny Lau, *Explicit positive lower density for the Collatz Conjecture*, [Hexagon 2610.00249v1](https://hexagonmath.org/2610.00249v1), 2026-10-14. The identifier belongs to Hexagon, not arXiv. The formal development is [AxiomMath/CollatzPositiveDensity](https://github.com/AxiomMath/CollatzPositiveDensity/tree/3a38bfbb70379e051b51155def1423846fab3a90), pinned at `3a38bfbb70379e051b51155def1423846fab3a90` (toolchain `leanprover/lean4:v4.35.0-rc2`, Mathlib `065356127b1dc0016f66b7283ce0ce2c4055aa55`). The statements are the four theorems of [`Challenge/Basic.lean`](https://github.com/AxiomMath/CollatzPositiveDensity/blob/3a38bfbb70379e051b51155def1423846fab3a90/Challenge/Basic.lean), proved in `Solution/Basic.lean`. It refines [mazur-2026-predecessor-density](mazur-2026-predecessor-density.md).

**Provenance.** The Hexagon page states that AxiomProver "autonomously produced the mathematics in this paper and formalized it in Lean". Hexagon is an archive for LLM-assisted mathematics (launched August 2026). This is not a reason to reject the claim; it is why the claim was built rather than read. The full Hexagon article was unavailable during the audit: the adopted statement is the accessible formal challenge, not a page-by-page match to the article.

## What we use

Put `L = 2^(2^(2^87640))`, `c(t) = 1/(t^4·L)`, `X_0(t) = 2^(t^3·L)`. For any natural target `t` with `3 ∤ t` and every integer `N ≥ X_0(t)`, at least `c(t)·N` odd integers `n < N` both reach `t` under the ordinary Collatz map within `⌊10.46·log(n/t)⌋₊` steps and reach `t/2^(v₂(t))` under the accelerated map within `⌊3.4881·log(n/t)⌋₊` steps (real division, natural floors). The count is normalised by all `N` integers; sources are distinct integers. There is **no hypothesis** that `t` reaches 1 or is nonperiodic.

Legacy use: Phase 6 route node C.1a, batch P6-004 (`experiments/phase6/linear_density_audit/`, now [lau-density-formal-replay](../areas/convergence/results/lau-density-formal-replay/README.md)); the result that uses its theorem as a premise is [nonabsorbing-set-linear-lower-density](../areas/convergence/results/nonabsorbing-set-linear-lower-density/README.md). If a bad odd seed `m` exists, `a = S(m)` is a bad target with `3 ∤ a`, so the bad set has positive lower density at every cutoff `X ≥ X_0(a)`; this turns C.2a into an exact remaining convergence obligation, which stays open. Scope: `d = 1` only; the statement is `d`-sensitive (its `d = 5` analogue is false). Lau's explicit constants and clocks are not transferred to `3x+d`. Positive predecessor density is not a proof of Collatz.

## How it is checked

`replayed`, by building from source; see [`lean/audit/README.md`](../lean/audit/README.md) and its receipts. A second, earlier replay by the Phase 6 main lane (macOS, network-denied sandbox, same toolchain and Mathlib cache, statement comparison in an independent namespace and fresh same-kernel replay) is [lau-density-formal-replay](../areas/convergence/results/lau-density-formal-replay/README.md).

- **Source audit.** 743 `.lean` files; `lakefile.toml` declarative. Whole-tree grep: the only `sorry`s are the four intentional challenge statements; no `admit`, `native_decide`, `implemented_by`, `extern`, `unsafe`, `axiom`, `#eval`, `run_cmd`. The one `initialize` is a no-op attribute registration.
- **Build and axioms.** From-source `lake build` (4102 jobs for `Solution.Basic`); `#print axioms` on all four theorems gives only `propext`, `Classical.choice`, `Quot.sound`; the challenge statements were matched against the solution in an independent namespace copy (eight axiom reports in the P6-004 replay).
- **Comparator.** The authors' `lake comparator` passed, and so did its `--paranoid` mode (nanoda, Lean paranoid kernel, lean4lean, con-leche, con-ron and the default kernel all accept the four-theorem export).

Caveats, kept as recorded:
- **Kernel bug.** Lean kernel soundness bug #14576 (fixed by lean4 PR #14577, merged 2026-07-28, after an AI-assisted Collatz "disproof" exploited it). The pinned toolchain `v4.35.0-rc2` was checked to contain the fix (363 commits ahead of the merge, 0 behind).
- **The authors' CI certifies little.** It restored a ~2.1 GB build cache instead of compiling from source, ran with `nanoda-allow-sorry: true`, and has no axiom or comparator step.
- **Sandbox.** The comparator's `bwrap` sandbox could not run in the unprivileged container, so it ran with `--inadvisably-no-sandbox` and printed "Sandbox disabled, this run is not trustworthy"; the Docker container served as the sandbox.
- **Unresolved rejections.** `lake check --paranoid` on the whole `CollatzPosDens` library: the Lean paranoid kernel, lean4lean and the default kernel accept; nanoda was killed by the 7 GB memory limit; con-leche and con-ron report "rejected" on this larger export without a printed reason. This is not the authors' specified certification, but the two rejections are unexplained.
- **Trust boundary.** Lean's trusted base; cached Mathlib dependencies were not all rebuilt from source; the replay used the same kernel, not a second kernel implementation for every check.
- The four **Lean statements** are theorems under the standard axioms; nothing about the paper's prose, transfer to `3x+d`, or C.2a is established. No complete human proof review is claimed.
