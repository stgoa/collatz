# Invariants

**The question.** If some positive integers never reach 1 under `3x+1`, their orbit components can be told apart from the component of 1 by an *invariant colouring*: a function `h` with `h(2n) = h(n)` and `h(3n+1) = h(n)` for odd `n > 1`, 1 absorbing. How complicated must such an `h` be? "Every invariant colouring is constant" is just convergence, so nothing here answers the Collatz question. The nodes classify restricted classes of colourings (periodic, digit-count, automatic, linearly complex) and record what each class excludes; the status of each is in [`MAP.md`](../../MAP.md).

**The approach.** Treat a hypothetical obstruction as a sequence with exact arithmetic symmetries and measure its complexity by its *sections* `n ↦ h(2^a n + r)` (binary) and `n ↦ h(3^b n + r)` (ternary), always as entire sequences, never finite prefixes. Every argument is tested against the `3x+d` controls: for `d = 5` or `61` the indicator `1_{d|n}` is a nonconstant periodic invariant, so any rigidity proof must use `d = 1` at a named step ([`conventions/NOTATION.md`](../../conventions/NOTATION.md) §3).

**Who did what.** The area came out of the owner's 2026-10-18 request for a better "language" after the convergence programme froze at R94. The main lane (ChatGPT/Codex) ran the viewpoint survey and the V002–V009 batches. The Claude side lane refereed every batch, checked them with its own code and wrote the `3x+d` version of the automatic theorem. The Claude Lean lane (Fable) read each proof and formalised the periodic, kernel, automatic, scalar, quadratic and reverse-closure units, with Cobham's theorem as a named hypothesis. On 2026-10-19 the owner replaced the area's open goal with the cycle-spectrum programme ([`areas/cycles/`](../cycles/OVERVIEW.md)).

## The main lines

### 1. Choosing the language (V001–V002)

Fourteen candidate languages (cards V1–V14) were compared, and a shortlist was tested with bounded exact probes ([`viewpoint-language-survey`](attempts/viewpoint-language-survey/README.md), reviewed). Every card *relocates* the difficulty, either to integer realisation of symbolic objects or to uniform control of the non-absorbed set. Arithmetic regularity of invariant colourings (V13) was chosen as a working language, explicitly without any claim of better convergence prospects, because it gave a checkable theorem. Periodic invariant colourings of `3x+d` factor through `gcd(M, d)` and are constant on the ×2, ×3 orbits, so for `3x+1` they are constant ([`periodic-invariant-colourings-classification`](results/periodic-invariant-colourings-classification/README.md), formal for every odd `d`). V14, carry diagrams, was tested and closed: it adds no relation ([`binary-ternary-carry-frontier`](attempts/binary-ternary-carry-frontier/README.md)).

### 2. Finite-state rigidity (V003–V004)

- **Partial classification (V003).** An invariant `F(s_2(n))` that depends only on the binary digit count is constant, for any `F` ([`digit-count-invariant-colourings-constant`](results/digit-count-invariant-colourings-constant/README.md), reviewed).
- **Kernel reduction.** The first ternary image of a finite binary kernel adds at most the one function `h(3n)` ([`binary-kernel-first-ternary-image`](results/binary-kernel-first-ternary-image/README.md)).
- **Guards are needed.** A binary-automatic character invariant under doubling and tripling need not be eventually periodic ([`scaling-invariant-character-not-eventually-periodic`](results/scaling-invariant-character-not-eventually-periodic/README.md)).
- **A known result.** One monochromatic dyadic class forces constancy; at `d = 1` this already follows from Monks's progression sufficiency ([`monochromatic-cylinder-forces-constancy`](results/monochromatic-cylinder-forces-constancy/README.md)).
- **The theorem (V004).** Keep the positive-offset sections `K_+`. They are closed under binary and ternary sections, and a ternary step costs at most 4 binary digits ([`positive-offset-kernel-ternary-closure`](results/positive-offset-kernel-ternary-closure.md), formal). Eventually periodic odd values force constancy ([`odd-eventually-periodic-invariants-constant`](results/odd-eventually-periodic-invariants-constant.md), formal). With Cobham's theorem these give: **every finite-valued binary-automatic invariant colouring of `3x+1` is constant** ([`binary-automatic-invariant-colourings-constant`](results/binary-automatic-invariant-colourings-constant/README.md), formal, conditional on Cobham).
- **All `3x+d`.** For `gcd(d, 6) = 1` the automatic invariants are exactly the functions of `n mod d` that are constant on the ×2, ×3 orbits; `d = 1` matters only in a commutator step ([`d-uniform-automatic-invariant-colourings`](results/d-uniform-automatic-invariant-colourings/README.md), side lane, written).
- **What it means.** The indicator of a nonempty nonabsorbing set would have an infinite binary kernel. "The bad set is automatic" is equivalent to convergence, so the theorem excludes one description class and nothing more.

### 3. Quantitative rigidity (V005–V009)

The next target asks a nonconstant invariant to have more binary sections than any linear function of the depth ([`section-count-depth-ratio-unbounded`](questions/section-count-depth-ratio-unbounded/README.md), open). The five batches ([`quantitative-rigidity-programme`](attempts/quantitative-rigidity-programme/README.md)) produced the following.

**Interfaces**
- Three identities on the odd values `b(n) = h(2n+1)` are equivalent to invariance ([`scalar-interface-three-identities`](results/scalar-interface-three-identities.md), formal).
- For such `b`, 2-automatic and 3-automatic are equivalent, with no external input ([`reverse-closure-two-base-automaticity`](results/reverse-closure-two-base-automaticity.md), formal).
- One automatic positive section forces constancy, and linear binary growth of `h` is equivalent to linear joint 2/3 growth of `b` ([`automatic-section-forces-constancy`](results/automatic-section-forces-constancy/README.md)).

**Scoped gains**
- The mixed sections of a non-eventually-periodic digit-count sequence are pairwise distinct ([`quadratic-separation-digit-count-sections`](results/quadratic-separation-digit-count-sections/README.md), formal). So one digit-count section of an invariant forces quadratic growth ([`digit-count-section-forces-quadratic-growth`](results/digit-count-section-forces-quadratic-growth.md), reviewed).
- The joint section graph has no finite interior with a single exit ([`singleton-exit-separator-exclusion`](results/singleton-exit-separator-exclusion/README.md), reviewed); numerically this gives only `|J_D(b)| ≥ 2D + 1`.
- At most three first-shell sections force constancy ([`first-shell-three-state-rigidity`](results/first-shell-three-state-rigidity/README.md)).

**Controls**
- Separate linear growth in bases 2 and 3 does not force periodicity, contrary to Bell's Conjecture 3.4 as printed ([`sparse-indicator-linear-growth-in-both-bases`](results/sparse-indicator-linear-growth-in-both-bases/README.md), reviewed).
- Generic two-exit interiors exist ([`two-exit-interior-counterexample`](results/two-exit-interior-counterexample/README.md), reviewed).
- Cumulative linear growth gives late cuts with a uniform future mean bound, but no stretches of bounded layer width ([`linear-growth-uniform-future-cuts`](results/linear-growth-uniform-future-cuts.md), reviewed).

**Final batch**
- `kappa_h(D) − (D+1) → ∞` for every nonconstant invariant ([`additive-section-excess-unbounded`](results/additive-section-excess-unbounded/README.md), reviewed).
- Under linear growth, every nonzero combination of depth-`A` sections is detected within `O(√A)` digits ([`linear-growth-short-detection`](results/linear-growth-short-detection.md), reviewed).

## Strongest results

"Status" gives the node's own status and the weakest status along its chain (MAP.md). "Rests on" lists the external inputs.

| Result | Status (own / chain) | Rests on |
|---|---|---|
| Periodic invariant colourings of `3x+d` factor through `gcd(M, d)`; constant for `3x+1` ([`periodic-invariant-colourings-classification`](results/periodic-invariant-colourings-classification/README.md)) | formal / formal | nothing external |
| Binary-automatic invariant colourings of `3x+1` are constant ([`binary-automatic-invariant-colourings-constant`](results/binary-automatic-invariant-colourings-constant/README.md)) | formal / formal | `cobham-recognizability-theorem`, `eilenberg-finite-kernel` |
| `K_+` is closed under ternary sections, at most 4 digits per step ([`positive-offset-kernel-ternary-closure`](results/positive-offset-kernel-ternary-closure.md)) | formal / formal | nothing external |
| Scalar interface; two-base automaticity is one condition ([`scalar-interface-three-identities`](results/scalar-interface-three-identities.md), [`reverse-closure-two-base-automaticity`](results/reverse-closure-two-base-automaticity.md)) | formal / formal | Cobham for the constancy part of the second |
| Quadratic separation of digit-count mixed sections ([`quadratic-separation-digit-count-sections`](results/quadratic-separation-digit-count-sections/README.md)) | formal / formal | nothing external |
| Digit-count invariants are constant ([`digit-count-invariant-colourings-constant`](results/digit-count-invariant-colourings-constant/README.md)) | reviewed / reviewed | nothing external |
| Unbounded additive section excess ([`additive-section-excess-unbounded`](results/additive-section-excess-unbounded/README.md)) | reviewed / written | Cobham, Eilenberg (through V004) |
| Automatic invariants of `3x+d` are functions of `n mod d` ([`d-uniform-automatic-invariant-colourings`](results/d-uniform-automatic-invariant-colourings/README.md)) | written / written | Cobham, Eilenberg |

## Open questions

- **The quantitative target:** [`section-count-depth-ratio-unbounded`](questions/section-count-depth-ratio-unbounded/README.md). Its side-lane calibration says it looks `d`-uniform: the actual `3x+5` and `3x+13` cycle labellings already have at least 242 and 259 binary sections by depth 9.
- **Card targets kept by the survey:** [`occupation-measure-tightness`](questions/occupation-measure-tightness.md) (V11) and [`capped-first-passage-power-bounds`](questions/capped-first-passage-power-bounds.md) (V12).
- **The side lane's ×2×3-rigidity milestone:** [`invariant-sets-meet-every-residue-class`](questions/invariant-sets-meet-every-residue-class.md) (S2). Proved for every modulus `M ≤ 100` by a finite closure search over residues ([`saturated-sets-meet-residue-classes-small-moduli`](results/saturated-sets-meet-residue-classes-small-moduli/README.md)) and for every modulus `2^k·3^b` by a digit-by-digit induction ([`saturated-sets-meet-residue-classes-six-smooth-moduli`](results/saturated-sets-meet-residue-classes-six-smooth-moduli/README.md): every saturated set is dense in `Z_2 × Z_3`); the case of moduli with a prime factor `≥ 5` reduces to a base case that is open.
- **The analytic analogue on the canonical quotient** lives in the convergence area: [`canonical-rigidity-bounded-invariants`](../convergence/questions/canonical-rigidity-bounded-invariants.md).

## Dead ends

- **The other languages.** V1–V12 relocate the obstacle ([`viewpoint-language-survey`](attempts/viewpoint-language-survey/README.md)). The relational-history and graph-geometry shortlists reproduced existing results (R81, R93, R7). The carry frontier redraws known arithmetic ([`binary-ternary-carry-frontier`](attempts/binary-ternary-carry-frontier/README.md)).
- **Shortcuts to superlinear growth.** These are refuted by exact controls ([`quantitative-rigidity-programme`](attempts/quantitative-rigidity-programme/README.md)):
  - local nonautomaticity with the first return identity allows `kappa = D + 3`;
  - linear growth need not contain a digit-count section (the adjacent-11 control);
  - semigroup growth theorems count the wrong object;
  - excluding boundary widths one at a time fails (the two-exit counterexample);
  - cumulative growth does not give bounded-width stretches.
- **Regularity of the actual bad set.** It is never supplied. Assuming it, or asking for it as a milestone, reinstates the whole problem.

## History

Written by the B16 migration (Claude, Opus 5.5) from the legacy viewpoints line (`experiments/viewpoints/`, V001–V009, 2026-10-18), its map, log and briefs, the side lane's referee sheet and feed, and the V-units of the legacy `lean/STATE.md`. Every claim was checked against its node at commit time. The line's index, map, log and briefs are archived in [`archive/invariants-viewpoints/`](../../archive/invariants-viewpoints/README.md).
