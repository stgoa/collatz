# Notation

Every node uses this notation unless it says otherwise. A node that departs from it defines its symbols in its `## Statement` section.

## 1. Maps and clocks

| Name | Definition | Notes |
|---|---|---|
| Collatz map | `n → n/2` (even `n`), `n → 3n+1` (odd `n`) | Used for statements only; computations use the faster forms below. |
| Shortcut map `T` | `n → n/2` (even), `n → (3n+1)/2` (odd) | Counting with it is the *shortcut clock*. |
| Odd-only (Syracuse) map `S` | odd `n → (3n+1)/2^v`, where `v = v₂(3n+1) ≥ 1` | Counting with it is the *odd-only clock*. The exponent `v` is the step's **valuation** or **letter**. |
| `3x+d` family | odd `n → (3n+d)/2^v₂(3n+d)` | `d` is odd and usually coprime to 6. Some nodes and Lean files call the same parameter `q`. |

- **Clocks.** Never mix the odd-only and shortcut step counts. Every claim says which one it uses.
- **Absorption.**
  - The convergence area uses the odd-only clock and **absorbs at 1**.
  - The cycles area uses **raw cycles with no absorbing state**: the fixed point `1 → 1` of `3x+1` is the trivial cycle, not an absorber.
- **Cylinders.** An exact valuation cylinder for a word of total `A` lives modulo `2^(A+1)`, including the extra bit.

## 2. Cycles, words and denominators

A cycle of the odd-only `3x+d` map is a sequence of odd positive integers `n_0, …, n_(m−1)` with `2^(a_i)·n_(i+1) = 3·n_i + d`, indices taken mod `m`.

| Symbol | Meaning |
|---|---|
| `m` | Period: the number of odd steps. |
| `w = (a_0, …, a_(m−1))` | The cycle's valuation word (its letters), each `a_i ≥ 1`. |
| `A = Σ a_i` | Total valuation. |
| `D_w = 2^A − 3^m` | Must be `> 0` for a positive cycle. |
| `C_w = Σ_j 3^(m−1−j)·2^(a_0+…+a_(j−1))` | The intercept of the word's affine composition, `x → (3^m x + C_w)/2^A`. |
| `x_0 = C_w / D_w` | The word's rational cycle point, a positive rational cycle of `3x+1`. |
| `den(w) = D_w / gcd(C_w, D_w)` | The reduced denominator. `w` is an integer cycle of `3x+d` iff `den(w)` divides `d`. **The cycle half of Collatz is the statement `den(w) = 1` only for repetitions of `(2)`.** |
| rotation `h` | The cyclic shift `w^(h) = (a_h, a_(h+1), …)`, with `|h|_m = min(h, m−h)`. |
| `mis(h)`, `s(h)` | Mismatch set `{i : a_i ≠ a_(i+h)}`, and its size. |
| `ρ(w)` | `min` of `s(h)` over nonidentity rotations: the word's rotation distance. |
| `L`, `H` | Minimum and maximum element of the integer cycle. |
| `ℓ' = log₂ L`; `B = log₂(H/L)` | Log-minimum and height. Some nodes use the integer dyadic band `H < 2^(B+1)·L` instead; each says which. |
| `y_p = log₂(n_p/L)` | Log-profile. |
| `δ = A − m·log₂3` | Drift. The Lean files use the natural-log version `A·log 2 − m·log 3`. |
| `V_h` | Total letter variation at the mismatches of `h`. |
| `K(h/m)` | Sum of the partial quotients of `h/m`. |

**Primitive** means the cycle is not a repetition of a shorter cycle. Equivalently, its `m` states are distinct.

## 3. The `3x+d` controls

Any argument about cycles of `3x+1` must stay consistent with the **actual** nontrivial cycles of other members of the `3x+d` family, such as those of `3x+5`, `3x+7`, `3x+13` and `3x+61`. An argument that would also exclude them is wrong, or it uses a hypothesis they fail; the node must say which.

The controls are cheap to generate: enumerate the cycles of `3x+d` for small odd `d` from small seeds. Shared fixtures:
- [`actual-cycles-3x-d-corpus`](../areas/cycles/results/actual-cycles-3x-d-corpus/README.md): every cycle reached from odd seeds `≤ 5000` for the 333 parameters `d ≤ 999` coprime to 6, with replay certificates;
- `cycle_fixtures.json` in [`baseline-obligation-transfer-controls`](../areas/convergence/results/baseline-obligation-transfer-controls/README.md): eleven exact raw `3x+d` cycles;
- `s1a_integer_cycle_check.py` in [`ordered-gap-closed-form`](../areas/cycles/results/ordered-gap-closed-form/README.md): a helper that finds the actual `3x+q` cycles by iteration, imported by several side-lane checks.

## 4. Writing math in Markdown

- Math may use Unicode, code spans, or GitHub's `$…$` LaTeX. It must stay readable as plain text, because agents read the raw file.
- Define every symbol not in this page at first use.
- Every number in a claim comes from a script whose receipt prints it, or from a proof in the node. Never quote an estimate as a result.
