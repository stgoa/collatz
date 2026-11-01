# Review of nonabsorbing-set-linear-lower-density

Independent review of the node [`README.md`](README.md), its two sources and the Lean file it cites. Scratch scripts: `review-work/nonabsorbing-set-linear-lower-density/controls_nonabsorbing.py` (outside the repository).

## What I checked

- **Inheritance**, by hand and by code: for odd `m`, `a = S(m)` is odd and `3 ∤ a` (since `3m + 1 ≡ 1 (mod 3)` and halving preserves the class); `a = 1` exactly when `3m + 1` is a power of 2, so `a > 1` for every `m ∈ B`; `a ∈ B` because its orbit is the tail of the orbit of `m`; every odd `S`-predecessor of `a` is in `B` because `S(1) = 1` (an odd path that visited 1 could never leave it, so it could not reach `a > 1`). Checked for all odd `m ≤ 10^5` (exit 0).
- **(i)**, line by line. Lau's statement at `t = a` counts odd `n < X` reaching `a` under the ordinary map; each such `n` has `oddpart(n) ∈ B` (the ordinary orbit of 1 is the 3-cycle `1, 4, 2`, so a path to `a ∉ {1, 2, 4}` never visits 1), hence `#(B~ ∩ [1, X)) ≥ X/(a^4 L)` for `X ≥ 2^(a^3 L)`. The C.2a contradiction with `ε = c(a)/2`, `M = X_0(a)`: every `n ∈ B~` has `tau_1 = ∞ > H` for every finite `H`, so at least `c(a)X > εX` late seeds below every `X ≥ M`. The converse (convergence gives a finite maximum hitting time below `X`) is immediate. So C.2a is equivalent to convergence **given the Lau input**.
- **(ii)**: if `m ∈ B`, every `n ≤ X` with some shortcut iterate equal to `a = S(m) ≥ 5` has an orbit that never visits 1 (the shortcut orbit of 1 is the 2-cycle `1, 2`), so `#{n ≤ X : tau_1(oddpart(n)) > H(X)} ≥ π_a(X) ≥ X^0.84` for all `X ≥ X_0(a)`, contradicting `≤ C X^(0.84 − ε)` once `X^ε > C`. Correct as written, relative to the cited Theorem 6.1.
- **Which steps rest on the external AI-generated source.** Only two things do: the displayed inequality `#(B~ ∩ [1, X)) ≥ X/(a^4 L)` in (i), and therefore the direction "C.2a implies convergence" of the equivalence (the direction "convergence implies C.2a" is elementary). The inheritance lemma and part (ii) do not use it; (ii) rests on [`krasikov-2003-predecessors`](../../../../sources/krasikov-2003-predecessors.md) (status `cited`, not replayed). Both sources stay under `assumes`; the node remains conditional and MAP.md must keep listing them.
- **Lean.** Read [`lean/Dichotomy.lean`](../../../../lean/Dichotomy.lean): `exists_bad_target` produces `t = 3m + 1` with `m` the odd part of a bad `n` (so `3 ∤ t`, `t` bad); `bad_of_reach` is the "path cannot pass through 1" lemma; `bad_positive_lower_density` applies the external theorem at `t` and `collatz_of_bad_density_zero` is its contrapositive. The receipt [`lean/receipts/Dichotomy.axioms.txt`](../../../../lean/receipts/Dichotomy.axioms.txt) lists only `propext`, `Classical.choice`, `Quot.sound`. The declarations match the prose argument; the file is not built by this repository's CI, as the node says.
- **Certificates:** none listed (nothing to run). Related: `python3 tools/run_certificates.py --node lau-density-formal-replay` was not needed for this node.
- **Controls** (`controls_nonabsorbing.py`, exit 0): for `d ∈ {5, 7, 13, 61}`, `S_d(dm) = d·S_1(m)` for odd `m ≤ 20000` and `S_d(d) = d`, so the multiples of `d` never reach 1 and the late fraction at every horizon is at least `⌊X/d⌋/X` (0.2000, 0.1429, 0.0769, 0.0164 at `X = 10^6`): both upper conditions fail for every `d > 1`, as the claim says. From odd seeds `≤ 5000` the raw odd map has 5, 2, 9 and 2 cycles other than `{1}` (for `d = 61` the 41-cycle with minimum 235), so `B_d ≠ ∅` and the dichotomy's positive branch is the one these controls exercise; nothing in the node would exclude them.

## What I did not check

- The two external theorems themselves: Lau's Lean development (I relied on the replay node [`lau-density-formal-replay`](../lau-density-formal-replay/README.md), status `reviewed`, and on [`lean/audit/`](../../../../lean/audit/README.md)) and Krasikov–Lagarias Theorem 6.1 (cited, not reproduced here; in particular I did not verify that their `π_a` counts all integers `n ≤ X` under the shortcut map, which the node asserts).
- Compiling `lean/Dichotomy.lean` (it needs a checkout of the external project).

## Findings

1. **Statement, "so B is empty or has positive lower density" (imprecision).** The proof bounds `B~ ∩ [1, X)` (all integers), not `B` (odd seeds). The passage is true but unstated: if `B` had lower density 0 along `X_j`, then `#(B~ ∩ [1, X_j)) = Σ_k #(B ∩ [1, X_j/2^k)) ≤ Σ_k min(δ_j X_j, X_j/2^k) ≤ (log₂(1/δ_j) + 3) δ_j X_j = o(X_j)`, so `B~` would too; hence positive lower density of `B~` gives it for `B`.
2. **Lean section, "which is the same set (halving does not change badness)" (imprecision).** `B` and `B~` are different sets; the Lean `Bad` set is `B~`, and the sentence should say the Lean set equals `B~`, which determines `B` as its odd part.
3. **Part (ii), clock remark (imprecision).** "all integers, in the shortcut clock of Krasikov–Lagarias" is right for the count, but the node's hitting time `tau_1` is odd-only; the argument only needs that the shortcut orbit of `n` hits 1 iff the odd-only orbit of `oddpart(n)` does, which holds. No change to the claim.

## Verdict

**HOLDS.** The equivalence (i) and the implication (ii) are correct conditional on the two sources named in `assumes`; the only steps resting on the AI-generated positive-density theorem are the linear lower bound in (i) and the direction "C.2a implies convergence". The three findings are imprecisions that do not affect the claim.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
