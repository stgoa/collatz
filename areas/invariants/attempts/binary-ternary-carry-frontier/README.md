---
id: binary-ternary-carry-frontier
kind: attempt
title: Binary/ternary carry diagrams (base conversion) as a language for invariant colourings
status: reviewed
claim: >
  Tried (viewpoint card V14, then V003's bounded test): represent the 3x+1 map as Stérin–Woods' two-dimensional
  base-conversion diagram (sum/carry cells with a non-local +1 bootstrap) and look for a new relation between
  binary and ternary section data across a complete carry frontier. Verdict: on one complete conversion rectangle
  (ternary 12 = 5 to binary 101, giving 3*5 + 1 = 16) eliminating the internal cells recovers exactly the existing
  affine arrow and the V13 section identities; no new closure relation, no finite bound on frontier families. The
  test was closed; reopen only with a specific relation between whole frontier families.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
evidence:
  - "base_conversion.md: the V14 viewpoint card (objects, structural gain, translated gap, local-rule example, d = 5 control, next test, the published small-cycle milestone)"
  - "../../results/digit-count-invariant-colourings-constant/verify_examples.py: V003's bounded replay includes the carry patch (key carry_patch of its receipt); ../../results/periodic-invariant-colourings-classification/verify_examples.py includes the V14 card's base-conversion trace"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    scope: "VIEWPOINTS.md referee sheet and feed 18:24: V14 'relocates (main closed it in V003: no new relation)'; the difficulty lands at a growing frontier, finite support and a nonlocal bootstrap (closest literature: Collatz as a quasi-cellular automaton, Cloney-Goles-Vichniac 1987)"
    link: ../../../../archive/side-lane/FEED.md
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Argument read line by line; the complete carry rectangle, the division sweeps, the bootstrap row, the affine arrow and every quoted number recomputed independently; the local rule, bootstrap predicate, state values, base-3-prime encoding and small-cycle question checked against Stérin-Woods v4; no certificates listed; verdict HOLDS"
aliases: [V003-e, VP-V14]
tags: [invariants, viewpoints, base-conversion, carries, rejected-mechanism]
---

# Binary/ternary carry diagrams (base conversion) as a language for invariant colourings

## Idea

Viewpoint card V14 ([`base_conversion.md`](base_conversion.md)): Stérin–Woods ([*The Collatz process embeds a base conversion algorithm*, v4](https://arxiv.org/html/2007.06979v4)) show that the Collatz process embeds a quasi-cellular automaton converting ternary to binary, with sum/carry cells and a non-local bootstrap for the `+1`. Binary and ternary data then share one complete carry boundary, which might supply relations between binary and ternary sections of an invariant colouring beyond those of [`periodic-invariant-colourings-classification`](../../results/periodic-invariant-colourings-classification/README.md) (card V13). The survey retained it for one complementary probe ([`viewpoint-language-survey`](../viewpoint-language-survey/README.md)).

## What happened

V003's bounded test: one complete conversion rectangle (the legacy note follows, lightly edited). Its outcome line: "exact boundary bookkeeping; no new section closure. This bounded V14 test converts the integer 5 from ternary to binary, fills the carry frontier, and derives the next binary sum row. It exposes the information a valid cut must retain. On this example the resulting relation is already contained in V13's invariant identities and the guarded affine arrow. No simulator, broad search, novelty claim or convergence inference is used."

### 1. Source rules and conventions

The primary source is Stérin–Woods,
[*The Collatz process embeds a base conversion algorithm*, v4](https://arxiv.org/html/2007.06979v4),
Definitions 1/3/8, Lemmas 5/6/15 and Theorem 16. Its cell state is (sum,carry).
The four full states 00,01,10,11 have ternary digit values 0,1,1,2.
The local arithmetic uses a full east state (s,c) and the current sum r:

\[
  c'=\lfloor(r+s+c)/2\rfloor,
  \qquad r'=(r+s+c)\bmod2.                       \tag{1}
\]

It completes the current state to (r,c') and emits r' immediately south.
The +1 bootstrap additionally requires a half-defined 1 immediately west
and only undefined or half-defined zero cells on the entire east ray.
These are the paper's rules; the tables below are our direct small
calculation from them. They are dependency tables, not snapshots at a
claimed common parallel time. Directions and coordinates are those of the
paper: east increases x, north increases y.

We use the paper's raw diagram to read the first odd arrow 5→1, then stop
the repository's trajectory at 1. Parallel update count, a transducer's
number of digit transitions, and Collatz clocks remain separate.

### 2. Initial boundary: ternary 12 represents 5

The canonical base-3' encoding of `12` is `1,bar1`, namely states 10,11.
Use the following complete initial data:

| Location | Initial state |
|---|---|
| (0,2) | 10 |
| (0,1) | 11 |
| (x,2), every x<0 | (0,⊥), the specified leading-zero ray |
| Every other location | (⊥,⊥) |

Thus the east ray of (0,0) is genuinely undefined; this is supplied boundary
data, not something inferred from finitely many inspected cells. The top
zero ray is equally explicit. No arbitrary infinite binary tail is allowed.

For a vertical sweep, let t=s+c be the input digit and r the incoming
remainder, initially zero. Equation (1) outputs the digit
`r+floor((r+t)/2)=floor((3r+t)/2)` and the remainder `(r+t) mod2`.
This is ordinary division by 2 in base 3, expressed in the split sum/carry
encoding. The complete nonzero conversion is:

| New column | Input column's two states, north first | Output states, north first | Bottom remainder | Input / quotient |
|---|---|---|---:|---|
| x=-1 | 10,11 | 00,11 | 1 | 5 / 2 |
| x=-2 | 00,11 | 00,01 | 0 | 2 / 1 |
| x=-3 | 00,01 | 00,00 | 1 | 1 / 0 |
| Every further column left | 00,00 | 00,00 | 0 | 0 / 0 |

The bottom sum bits, read left to right, are therefore `...000101`: the
binary representation of 5. At this stage the bottom sums alone are not
the full carry frontier.

### 3. Bootstrap and the complete upper patch

The remainder at (-1,0) is 1. At (0,0), the west half-defined 1 and the
entire undefined east ray meet the bootstrap predicate. It inserts **01**
at (0,0). Apply (1) along row 0, from right to left:

| x | Input sum r | Full east state | r+s+c | Completed state at (x,0) | Emitted sum at (x,-1) |
|---|---:|---|---:|---|---:|
| -1 | 1 | 01 | 2 | 11 | 0 |
| -2 | 0 | 11 | 2 | 01 | 0 |
| -3 | 1 | 01 | 2 | 11 | 0 |
| -4 | 0 | 11 | 2 | 01 | 0 |
| -5 | 0 | 01 | 1 | 00 | 1 |
| Every x<=-6 | 0 | 00 | 0 | 00 | 0 |

Here is every full cell in a rectangle large enough to include the carry
flush. Each entry is the pair (sum,carry), abbreviated as above:

| y \\ x | -5 | -4 | -3 | -2 | -1 | 0 |
|---|---|---|---|---|---|---|
| 2 | 00 | 00 | 00 | 00 | 00 | 10 |
| 1 | 00 | 00 | 00 | 01 | 11 | 11 |
| 0 | 00 | 01 | 11 | 01 | 11 | **01 bootstrap** |

The complete frontier description, including its constant tails, is:

- On the west side, all three displayed rows have state 00 for x<=-6.
- Above the input and to the right of it, cells remain undefined: y>2,
  or x>0 with 0<=y<=2. They are not silently replaced by zero-valued full
  states. The only added anchor on x=0 is the bootstrap at y=0.
- The south cut is the **entire completed row 0** in the table plus its
  west zero tail and east undefined ray. This supplies every sum/carry
  input used to compute the next sum row.
- The generated south sums are `...00010000` on x<=-1, with their lone 1
  at x=-5. Their own carries and any later bootstrap belong to the next
  region and have not been assumed. We do not claim that these emitted
  half-states coexist in a single parallel snapshot.

In particular, the first leading binary zero at x=-4 still has carry 1.
Replacing every zero sum by state 00 would lose the output 1 at x=-5.
Retaining the completed frontier gives exactly

\[
  3\cdot 5+1=16=(10000)_2.
\]

The conversion's first three vertical divisions are 5→2→1→0; these are
**not** a Collatz orbit. Once row 0 is included, the column readings at
x=-1,-2,-3,-4 instead give `(022)_3=8`, `(011)_3=4`, `(002)_3=2`,
and `(001)_3=1`. Those are the four shortcut arrows 5→8→4→2→1.
The corresponding odd-only path has one arrow, of valuation 4. Five
nontrivial horizontal digit transitions in the table are neither of those
clock counts. No parallel-update count is asserted.

## Why it fails

### 4. Comparison with V13 and guarded affine data

The first completed column has value 8, so an invariant coloring gives
`h(8)=h(5)`. This is exactly the n=2 instance of the existing identity

\[
 h(3n+2)=h(2n+1),
\]

obtained from `3(2n+1)+1=2(3n+2)`. Doubling invariance subsequently gives
`h(8)=h(4)=h(2)=h(1)`. The diagram gives a compatible digit-level account
of these equalities. The separate kernel probe also derives
`h(3n+1)=h(4n+1)`. This diagram adds no further section relation and does
not bound the number of iterated ternary sections of a sequence with finite
binary kernel. General mixed-section closure remains missing.

The same computation as a guarded odd affine arrow is

\[
 x=5+32t\longmapsto\frac{3x+1}{16}=1+6t,
 \qquad t\ge0.                                    \tag{2}
\]

The modulus is 32=2^(4+1), retaining the exact valuation bit. Its t=0
case is the diagram above. For example x=37 has the same five low binary
bits as 5 and the same valuation 4, but its endpoint is 7. More generally
5+2^B for B>=5 shares the first B low bits and maps to
`1+3*2^(B-4)`. A finite low-bit view cannot supply the assumed leading-zero
tail. The exact affine expression already preserves that unresolved upper
input through its parameter t.

This is an information-preservation comparison, not a new obstruction to
all boundary methods. The diagram organizes the simultaneous quotient,
remainder and carry data clearly. In this test, eliminating its internal
cells leaves precisely ordinary arithmetic and (2), without an additional
restriction or a smaller unbounded family of boundary states.

### 5. Control scope and decision

No generalized d=5 tile rule was constructed. The arithmetic control
19→31→49→19 remains external to this d=1 diagram; importing that cycle
as an execution of these same tiles would be incorrect. Changing +1 to
+5 changes the bootstrap/carry input. A claim that a finite alphabet, carry
flush, or local consistency by itself implies absorption would still fail
the arithmetic control. No such claim is made here.

**Decision: stop this complementary test as a redraw with complete boundary
accounting.** It produces a useful checked fixture and identifies exactly
which zero and carry information must cross the cut, but no finite-kernel
closure or new component-coloring relation. Do not pursue a broader tile
search from this example. Reopen V14 only with a specific proposed relation
between whole frontier families that adds to the affine/section identities.
The main V13 kernel investigation is logically separate and may reach its
own conclusion.

**Verification scope:** all six vertical digit transitions and five
nonzero horizontal transitions are displayed explicitly, with the remaining
constant tails closed by (1). Every value in the rectangle is determined
from the stated input and bootstrap. The calculation is a finite exact
example with symbolic constant tails, not a formal verification of the
published automaton or any all-input classification.

## What survives

- A checked fixture: the carry example has three division sweeps, four shortcut Collatz arrows, one odd-only arrow and five horizontal digit transitions; none is substituted for a parallel-update count.
- The exact list of zero and carry information that must cross a cut.
- The card's published milestone, the small-cycle question of Stérin–Woods (exclude `T^k(x) = x` for every integer `x > 2` and `1 ≤ k ≤ ⌈log₂ x⌉`, shortcut clock), was recorded as a deferred target, not adopted: it leaves divergence and longer cycles, and a new proposal would first have to show that a boundary argument contributes beyond the periodic affine equation. The `d = 5` check on the card is external arithmetic; no generalised `d = 5` tile construction was tested.
- The side lane's verdict on the card: relocates (a growing frontier, finite support and a nonlocal bootstrap).

## History

- Migrated from `experiments/viewpoints/V003/carry_boundary.md` (legacy ID V003, report §4 "Complete carry frontier") at commit `be73a66`, by the B16 migration (Claude, Opus 5.5); the V14 card `experiments/viewpoints/V002/base_conversion.md` moved here. Text kept; sections regrouped under the attempt headings.
- Main lane (ChatGPT/Codex), 2026-10-18 (card at main `cdfb143`, test at `2ac44ef`). Main-lane review: [`PROOF_REVIEW.md`](../../results/digit-count-invariant-colourings-constant/PROOF_REVIEW.md) (the carry calculation was produced by the reviewer and spot-checked by the coordinating agent).
- **Link repair in kept notes (B16 migration, 2026-10-20).** In `base_conversion.md`, only link targets were changed: relative links to legacy paths now point to the corresponding nodes or to `archive/invariants-viewpoints/`. No text changed. Any `delivery_checks.json` hashes describe historical versions of these notes; no script in the repository checks them.
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. No corrections; the review is [`REVIEW-2026-10-31-claude-review-lane.md`](REVIEW-2026-10-31-claude-review-lane.md).
