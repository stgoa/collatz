---
id: additive-section-excess-unbounded
kind: result
title: Every nonconstant 3x+1 invariant has binary section count exceeding D+1 by an unbounded amount
status: reviewed
claim: >
  For every nonconstant finite-valued colouring h of the positive integers with h(2n) = h(n) (n >= 1) and
  h(3n+1) = h(n) (odd n > 1), with h(0) = h(1) and kappa_h(D) the number of distinct entire binary sections
  n -> h(2^a n + r), 0 <= a <= D, 0 <= r < 2^a: kappa_h(D) - (D+1) tends to infinity (equivalently, an eventual
  single-state binary tail, kappa_h(D) = D + O(1), is impossible). This is an additive gain over the generic
  infinite-kernel bound kappa_h(D) >= D+1; it permits growth like D + sqrt(D) and does not give an unbounded
  ratio kappa_h(D)/(D+1). The proof uses the two-base infinitude of sections, obtained through V004/V005/V007, and so
  assumes Cobham's theorem.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [binary-automatic-invariant-colourings-constant, positive-offset-kernel-ternary-closure, automatic-section-forces-constancy, reverse-closure-two-base-automaticity, singleton-exit-separator-exclusion]
certificates: [v009_escape_check.py]
evidence:
  - "binary_tail.md: the written proof (sections 1-11); global_growth.md: the detection theorem (node linear-growth-short-detection)"
  - "ADDITIVE_REVIEW.md, GLOBAL_REVIEW.md: main-lane independent agent reviews; side_review.md: the main lane's read of the side-lane feed"
  - "delivery_checks.json: historical delivery receipt; no script in the repository regenerates it"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: v009_escape_check.py
    scope: "Feed 23:36 (REFEREE V009, main 4be9bae): the finite core (sections 4-7) recomputed by exhaustive search, the return argument (sections 1-3, 8-10) checked by reading; no gap"
  - by: Claude Lean lane (Fable)
    date: 2026-10-18
    scope: "Iteration 10: binary_tail.md sections 1-11 and ADDITIVE_REVIEW.md read in full, no gap; the parent and depth-4 bound, delta stabilisation, the root-of-unity case analysis, the telescoped congruence (7), the sign of v_n and both cycles, the parity in (13), the 2-adic separation of y_n from x_a and the lambda - 1 coefficient re-derived"
aliases: [V009]
tags: [invariants, section-growth, quantitative-rigidity, conditional]
---

# Every nonconstant 3x+1 invariant has binary section count exceeding D+1 by an unbounded amount

## Statement

For every nonconstant finite-valued Collatz invariant `h` (conventions of [`section-count-depth-ratio-unbounded`](../../questions/section-count-depth-ratio-unbounded/README.md)),

```
kappa_h(D) − (D+1) → ∞.
```

The excess is nondecreasing (each binary layer of an infinite kernel is nonempty), so "unbounded" and "tends to infinity" agree. Equivalently, `kappa_h(D) = D + O(1)`, i.e. exactly one new binary state `q_n` at each sufficiently large depth `n`, is impossible.

## Proof

The written proof is [`binary_tail.md`](binary_tail.md). Setup (§1): by V004 the binary kernel of `h` is infinite; under the assumed bound each late binary layer holds one entire sequence `q_n`; `S = K_2(b)`, `b(n) = h(2n+1)`, is the family of positive binary `h`-sections, closed under both bases ([`positive-offset-kernel-ternary-closure`](../positive-offset-kernel-ternary-closure.md)), and every state of `S` has infinite pure kernels in both bases ([`automatic-section-forces-constancy`](../automatic-section-forces-constancy/README.md), [`reverse-closure-two-base-automaticity`](../reverse-closure-two-base-automaticity.md)); these constancy dependencies include V004's Cobham input. The binary parent of `q_(n+1)` is `q_n`, and `rho(T_j(q_n)) ≤ n + 4`. The maximal ternary increment `δ_n` is nonincreasing and stabilises (§2); `δ ≤ 0` would leave a finite ternary-closed set and `δ = 1` is excluded by [`singleton-exit-separator-exclusion`](../singleton-exit-separator-exclusion/README.md). The coefficient-exact boundary equation (§3), the root-of-unity case analysis (§4) and eventual periodicity of the escape digits (§5) leave, after excluding constant escape patterns (§6), exactly two periodic patterns up to phase (§7). Rational coordinates force a nonmaximal move in every return block with a strict depth gain (§8); every nonmaximal ternary edge contracts depth by a fixed factor below 1 up to an additive constant (§9); bounded returns then make the return sequences periodic and induction on inputs forces `q_(n+P) = q_n` as entire sequences, contradicting their distinct minimal depths (§10). The legacy V009 report follows, lightly edited.

### 1. Linear growth imposes a quantitative detection bound

This section is the node [`linear-growth-short-detection`](../linear-growth-short-detection.md).

Let J_D(s) be the whole mixed binary/ternary section family through total
depth D, and W_D its real linear span. The [new elementary theorem](global_growth.md)
proves the following implication, for every fixed C>=1:

```
|J_D(s)|<=C(D+1) for all D
    => every nonzero g in W_A is detected before input 9^L,

L=ceil(2C+sqrt(2C(A+1))+1).
```

Thus at most O_C(sqrt(A+1)) binary or ternary input digits detect every
nonzero linear combination of depth-A states. This is stronger than
pairwise distinguishability. It is a proved prefix test under a stated
all-depth hypothesis, not an inference of whole-function equality from
a finite sample.

The mechanism is exact. If g first becomes nonzero at N>=9^L, sectioning
along each multiplier m=2^a3^b with a+b<=L moves that first nonzero
coordinate to floor(N/m). The resulting indices are distinct. Their
triangular ordering gives (L+1)(L+2)/2 linearly independent functions
inside W_(A+L). This contradicts the assumed linear bound when L is
chosen as above. All offsets lie in their declared cylinders, and the
endpoint N=9^L is retained.

This gives a concrete route to the **full** goal: construct nonzero
combinations g_j in W_(A_j)(b), b(n)=h(2n+1), with

```
log(nu(g_j))/sqrt(A_j+1) unbounded,
```

where nu is the first nonzero input. Their independent mixed sections
would force an unbounded joint ratio and then an unbounded binary ratio
through the existing exact depth conversion. The missing step is to
produce these delays from arbitrary nonconstancy and the full Collatz
identities. No such construction is supplied here.

### 2. Why the new bound is not already a contradiction

An infinite finite-alphabet joint kernel has strictly increasing span
dimension: a rank plateau would make the finite-dimensional span closed
under all section maps, and only finitely many finite-alphabet sequences
can lie in that space. Hence dim W_A>=A+1.

That rank count alone gives a nonzero combination vanishing at only A
initial inputs. The detection bound permits much longer zero prefixes,
of size exponential in sqrt(A). An additional arithmetic mechanism is
essential. The calibration in the proof note recovers the existing
digit-count quadratic phenomenon by constructing exponentially delayed
combinations; it does not assume every invariant has such a section.

### 3. The smallest-growth diagnostic is excluded

The independent [binary-ray analysis](binary_tail.md) assumes the narrower
bound kappa_h(D)=D+O(1). It is equivalent to exactly one new binary state
q_n at each sufficiently large depth n. All returns to previous states
are retained.

The maximal ternary depth increment stabilizes, and the exact radix
equations make its reaching digit and the forward binary digit unique
and eventually periodic. A contraction argument excludes every constant
escape pattern, including the whole increment-two case. Rational
coordinates then leave only two maximal-transition patterns, up to phase:

| Ternary increment | Binary escape word | Ternary escape word |
| --- | --- | --- |
| 3 | 1100 | 1012 |
| 4 | 110111001000 | 222101000121 |

These words describe transitions reaching the largest possible depth.
The proof then controls all other transitions. The nonescaping binary
children obey an exact periodic sequence of ternary maps. Formal rational
coordinates for their digits have an even denominator; maximal transitions
have coordinates with odd denominator. This forces a nonmaximal move in
every fixed-length return block and gives a strict gain in depth.

Radix commutation upgrades that gain: every nonmaximal ternary edge
contracts depth by one fixed factor less than1, up to an additive constant.
Repeated return blocks then stay in a finite set. Including their phases
makes the return sequences periodic, and induction on actual integer
inputs forces two entire q_n states equal. This contradicts their distinct
minimum depths. Every jump into the finite earlier set is retained.

Consequently, for every nonconstant finite-valued Collatz invariant,

```
kappa_h(D)-(D+1) -> infinity.
```

This is a universal additive gain beyond the generic infinite-kernel
argument. It still permits growth such as D+sqrt(D), and therefore proves
neither a fixed fractional improvement nor the active unbounded ratio.

## Certificates

- [`v009_escape_check.py`](v009_escape_check.py) (under a second; side lane, independent code): recomputes the finite core of `binary_tail.md` §§4–7 by exhaustive search. For `δ = 2, 3, 4` every window on a cycle of the transition graph allowed by the boundary identity is the all-digits case or all singletons; the singleton digit system has the constant tails `(0,0)` and `(1,2)`, no other cycle for `δ = 2`, one cycle for `δ = 3` (a rotation of `1100 / 1012`) and one for `δ = 4` (a rotation of `110111001000 / 222101000121`); on both cycles `j_n ∈ {0,1,2}`, the parity condition holds, every `y_n` has denominator exactly `2M` and `x_n ≠ j + 3x_m` for `j ≠ d_n`. It rewrites [`v009_escape_check.json`](v009_escape_check.json) identically.

## Remarks

### 4. Comparison and next action

| Mechanism | What this batch proves | What must still be supplied |
| --- | --- | --- |
| Global count and linear combinations | Explicit short detection under every fixed linear coefficient | Nonzero combinations with delays exceeding that bound, from full Collatz invariance |
| Near-minimal binary graph | All eventual one-state binary tails excluded, giving unbounded additive excess | Extension to growth allowing recurrent layers with several states |
| Pure dimension counting | Rank increases at every depth in an infinite finite-alphabet kernel | A reason for long zero prefixes; rank alone supplies only a linear delay |

Compare the global detection route with the now proved return-contraction
mechanism. Test the scalar equations for delayed nonzero combinations,
and identify which contraction steps can handle several states per layer
without assuming bounded layer sizes from cumulative growth. A formally
cancelled expression that is identically zero is not a witness. Periodic
escape digits alone do not prove periodicity of entire states: the return
analysis is essential. No regularity is assumed for the actual nonabsorbing set.

### 5. Verification and preservation

The [global review](GLOBAL_REVIEW.md) checks the affine substitutions,
strict pivot separation, linear independence, explicit cutoff and
finite-alphabet rank argument. The [additive review](ADDITIVE_REVIEW.md) checks
the full radix constraints, finite earlier-state exceptions, contraction
and rational-coordinate classification, followed by the full return-block
contraction. Root independently checked these arguments and the two
displayed words. This is written proof with agent
review; novelty, human peer review and formal verification are unclaimed.

The generic detection theorem imports no external theorem. The tail's
Collatz application uses the existing two-base infinitude argument and
therefore imports Cobham through V004. The [side review](side_review.md)
records the newly fetched formalization report without claiming a main
replay. Known d5/d61 periodic controls fail the infinitude premises and
have no unbounded-delay witness.

This is a prose-only mathematical batch. Frozen R1–R94, dispatcher code
and evidence, and the open LaTeX document are preserved. Local links,
source hashes and frozen comparisons are recorded in the delivery checks;
the unrelated historical finite gate is not rerun.

### Calibration

The side lane called this "the first quantitative improvement over the generic infinite-kernel bound that holds for every nonconstant invariant": the additive diagnostic named in the main lane's reply to direction D8, not the `(1+ε)` gain and not the unbounded-ratio goal (feed 23:36). Extending the return contraction to several states per layer remains open; cumulative growth does not supply a uniform layer-width bound ([`linear-growth-uniform-future-cuts`](../linear-growth-uniform-future-cuts.md)). Not formalised: the Lean lane recorded the whole-sequence return argument as a large unit, deferred (iteration 10).

## History

- Migrated from `experiments/viewpoints/V009/REPORT.md` (legacy ID V009) at commit `be73a66`, by the B16 migration (Claude, Opus 5.5). Report text kept under Proof and Remarks; Statement and Certificates added. The detection theorem (`global_growth.md`, report §§1–2) is the node [`linear-growth-short-detection`](../linear-growth-short-detection.md). The side-lane check `reviews/side_lane/v009_escape_check.*` moved here.
- Main lane (ChatGPT/Codex), 2026-10-18, main commit `4be9bae`; the fifth and last batch of the quantitative goal before the owner replaced it with the cycle-spectrum programme on 2026-10-19.
- **Link repair in kept notes (B16 migration, 2026-10-20).** In `global_growth.md`, only link targets were changed: relative links to legacy paths now point to the corresponding nodes or to `archive/invariants-viewpoints/`. No text changed. Any `delivery_checks.json` hashes describe historical versions of these notes; no script in the repository checks them.
