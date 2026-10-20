---
id: two-exit-interior-counterexample
kind: result
title: An irrational-rotation sequence has a two-exit interior with infinite kernels in both bases, so separator widths cannot be excluded generically
status: reviewed
claim: >
  Let 0 < alpha < 1 be irrational, p(n) = 1 if {n alpha} < alpha and 0 otherwise, and s(n) = p(floor(n/6)). Both
  binary sections of s equal u(n) = p(floor(n/3)) and all three ternary sections equal v(n) = p(floor(n/2)); s, u, v
  are distinct, so {s} is a finite forward interior with exactly two exits in its joint binary/ternary section graph;
  every reachable section has irrational frequency alpha, hence infinite kernels in both bases; the graph obeys all
  six radix identities. So the generic two-exit analogue of singleton-exit-separator-exclusion is false. s is not a
  3x+1 invariant (s(4n+2) = s(n) fails at n = 1) and has at least D(D-1)/2 joint sections through depth D, so it is
  neither a Collatz counterexample nor a linear-growth example.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
evidence:
  - "two_exit.md: the construction, the destination-valued boundary equations for any finite number of exits (section 1), the rational-frequency argument for finite kernels (section 2.2), the root-identity failure and the quadratic count (section 4)"
  - "INDEPENDENT_REVIEW.md: main-lane second-agent review of the counterexample and the corrected first-shell theorem; side_review.md: the main lane's read of the side-lane feed at sidekick b567f2b (accepting the Cobham attribution for V005-V007)"
  - "delivery_checks.json: historical delivery receipt; no script in the repository regenerates it"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    scope: "Feed 23:01 (REFEREE V008, main 9d66b69): construction reproduced (exits checked exactly for n < 10^4, frequency 0.61805 empirically for alpha = (sqrt 5 - 1)/2, rational frequency of automatic sequences with an existing frequency), and the failure s(6) = 0, s(1) = 1 of the root equation"
    link: ../../../../archive/side-lane/FEED.md
  - by: Claude Lean lane (Fable)
    date: 2026-10-18
    scope: "Iteration 9: E_i(s) = u, T_j(s) = v by the residue computations, T_j(u) = E_i(v) = p, the distinctness witnesses, the irrational-frequency argument for every affine section, the rational Cesaro projection for a finite kernel, the root-identity failure, and the quadratic bound from distinct dilations; sound"
aliases: [V008]
tags: [invariants, section-graph, counterexample, quantitative-rigidity]
---

# An irrational-rotation sequence has a two-exit interior with infinite kernels in both bases, so separator widths cannot be excluded generically

## Statement

With `0 < α < 1` irrational,

```
p(n) = 1_{{nα} < α},      s(n) = p(⌊n/6⌋).
```

Both binary children of `s` equal `u(n) = p(⌊n/3⌋)`; all three ternary children equal `v(n) = p(⌊n/2⌋)`. The states `s, u, v` are distinct, so the finite interior `{s}` has exactly two exits. Every reachable section has irrational natural frequency `α`, and a finite kernel with an existing frequency has rational frequency, so every vertex has infinite kernels in both bases. The graph of entire sequences obeys all six radix laws and the zero-output conditions. Hence the generic two-exit analogue of [`singleton-exit-separator-exclusion`](../singleton-exit-separator-exclusion/README.md) fails. `s` is not a Collatz invariant: `s(4n+2) = s(n)` fails at `n = 1` (`s(6) = 0`, `s(1) = 1`). Its zero sections already give at least `D(D−1)/2` distinct states through joint depth `D`.

## Proof

The written proof is [`two_exit.md`](two_exit.md) §§2–4. The legacy V008 report follows, lightly edited; its §2 is the node [`first-shell-three-state-rigidity`](../first-shell-three-state-rigidity.md) and its §3 the node [`linear-growth-uniform-future-cuts`](../linear-growth-uniform-future-cuts.md).

### 1. The generic two-exit extension is refuted

The [exact construction](two_exit.md) takes an irrational rotation
coloring p and repeats each value six times:

```
p(n)=1_{{n alpha}<alpha},      0<alpha<1 irrational,
s(n)=p(floor(n/6)).
```

Both binary children of s equal `u(n)=p(floor(n/3))`; all three ternary
children equal `v(n)=p(floor(n/2))`. The states s,u,v are distinct, so
the finite interior {s} has exactly two exits. Every reachable section
has irrational natural frequency alpha. A finite kernel with an existing
frequency has rational frequency, by a rational stochastic-matrix
averaging argument. Thus every vertex has infinite kernels in both bases.

This is an actual graph of entire sequences obeying all six radix laws
and zero-output conditions. It refutes the generic two-exit analogue of
V007. Its binary and ternary incoming edges reach different boundary
states; collapsing those states loses precisely the relevant information.
The note derives the correct destination-valued boundary equation for
any finite number of exits.

The example fails the Collatz equation `s(4n+2)=s(n)` at n=1. Its zero
sections already supply at least `D(D-1)/2` distinct states through joint
depth D. It is therefore neither a Collatz invariant nor a linear-growth
counterexample, and it supplies no recurrent bounded-layer example.

## Remarks

### 2. The full root equations give an elementary finite-depth exclusion

Root derived the [first-shell theorem](ROOT_REVIEW.md): for any output
alphabet, the three scalar equations

```
b(3n)=b(4n),  b(3n+2)=b(2n+1),  b(4n+2)=b(n),   n>=0,
```

together with `|J_1(b)|<=3`, force b constant. An exhaustive case split
exhibits a binary-closed family of at most four entire sequences. All
their outputs at zero agree, so binary reading gives constancy directly.
This theorem does not need Cobham or a finite output alphabet.

For a nonconstant invariant it implies `|J_1(b)|>=4`. This rules out the
generic example at the actual Collatz root, and confirms that the extra
equations matter. It does not move those root equations to arbitrary
boundary states or rule out later two-exit interiors. The resulting
finite-depth constraint gives no improved universal asymptotic bound.

During review, one unpublished draft row used an incomplete subset of
the radix equations. The omitted equation makes that row inconsistent.
It was removed before acceptance; seven surviving rows give the theorem.
The [root review](ROOT_REVIEW.md) records the correction explicitly, and
a second review independently checks the final table and constant-output
finish. No historical theorem was found false or altered.

### 3. Use the growth assumption in its actual strength

The parallel [growth analysis](linear_joint.md) proves a useful uniform
version of the small-layer observation. If `|B_D|<=C(D+1)`, then for every
C'>C there are arbitrarily late r with

```
|B_(r+t) minus B_r| <= C't     for every t>=0.
```

This follows by maximizing `|B_D|-C'D` over a tail. It retains the future
cumulative bound after selected cuts, including every return through the
finite interior.

A separate explicit abstract graph control has cumulative size O(D),
outdegree at most two and infinite descendants at every vertex, but
recurrent layer peaks of every height. It admits no arbitrarily long
intervals with one fixed bound on every layer. Its exact profile obeys
`sum_(n=1)^N a_n<=13N`. This control is not an affine section graph; it
refutes only a deduction from cumulative counting and finite branching.

The source audit checks one finitary S-adic rigidity result. Its symbolic
presentation and recognizability hypotheses have not been supplied by
our rooted count, so it is not imported as a growth theorem.

### 4. Comparison and next action

| Proposed mechanism | Outcome | Decision |
|---|---|---|
| Exclude every finite boundary of size two using radix laws and two-base infinitude | Exact affine counterexample | Reject at that generic scope |
| Use all three root equations when the first joint shell has at most three states | Elementary constancy theorem | Retain as a finite-depth distinction, with no rate claim |
| Replace cumulative linear growth by long stretches of uniformly bounded layer width | Explicit bounded-degree counterexample | Reject without an additional affine argument |
| Retain the uniform future cumulative bound after selected cuts | Proved necessary condition for each C'>C | Use this actual growth hypothesis in the next global overlap test |

Do not proceed by mechanically excluding successive fixed boundary sizes.
The next investigation must use the global bound or derive additional
equations from the full Collatz root. One bounded discrimination within
that investigation is exact near-minimal binary growth:
`kappa_h(D)=D+O(1)` is equivalent to one new binary state per sufficiently
late depth. Ternary children have a bounded forward depth cost but can
return arbitrarily far into the old graph. V007 cannot be applied to such
a binary layer as if it were a joint singleton exit.

Resolving that diagnostic would still be partial. The main completion
condition remains every possible linear coefficient, and no regularity
of the actual nonabsorbing set is assumed. Future graph limits or finite
presentations must retain whole-sequence distinctions; finite-prefix
convergence alone cannot provide an automatic actual section.

### 5. Verification and dependency scope

Root checked the two-exit construction, the irrational-frequency proof,
all multiplier witnesses and the layer-profile and envelope calculations.
The [independent review](INDEPENDENT_REVIEW.md) checks the counterexample
and the corrected first-shell theorem. The cases are equations of entire
sequences, not finite matching experiments. No formal verification or
novelty claim is made. The actual d5/d61 controls remain valid and fail
the named d1 root equations; they have finite kernels.

The [side review](side_review.md) records fetched pin
`b567f2bfc9ec581d42bbd35c5231324f7865a01e` and accepts an attribution
clarification: the Collatz applications in V005–V007 inherit the published
Cobham theorem through V004. Their elementary generic arguments are
separate. Dated notes now make this explicit in the standalone reports
and ledger. The written proof's use of a published theorem is distinct
from the Lean lane's conditional assembly and its replay status.

D8's proposed fixed-epsilon improvement is retained as a progress
diagnostic, not a new success condition. V008 does not achieve it. Its
automatic two-batch abandonment rule is rejected under the user's active
goal. Reconsidering methods remains appropriate; changing the objective
or treating fixed-width lemmas as completion does not.

This is a prose-only mathematical batch. Existing executable evidence,
the frozen R-series body, dispatcher and open LaTeX source remain
unchanged. The historical Phase6 finite gate was not rerun; mathematical
reviews, local links and exact frozen comparisons are recorded separately.

## History

- Migrated from `experiments/viewpoints/V008/REPORT.md` (legacy ID V008) at commit `be73a66`, by the B16 migration (Claude, Opus 5.5). Report text kept under Proof (§1) and Remarks (§§2–5); Statement added. The legacy line index listed V008 as "`refuted` (proposed extension)": the refuted statement is the generic two-exit extension, and the refutation is this proved counterexample. The V008 notes moved here.
- Main lane (ChatGPT/Codex), 2026-10-18, main commit `9d66b69`; the fourth batch of the quantitative goal. The batch also added the dated Cobham clarifications to the V005–V007 reports.
- **Link repair in kept notes (B16 migration, 2026-10-20).** In `two_exit.md`, only link targets were changed: relative links to legacy paths now point to the corresponding nodes or to `archive/invariants-viewpoints/`. No text changed. Any `delivery_checks.json` hashes describe historical versions of these notes; no script in the repository checks them.
