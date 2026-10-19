# V005 — External research input and scope assessment

## Pinned read-only branches

Fetched `origin main claude/sidekick`. Main remained
`4f1704c9d133ab77307c05c05ade7f6ae35f3ce2`; the reviewed side pin is
`3b95686f36d491a1da0b8fcf162f6c9fcceaa6e5`. Read DIRECTIONS and the newest
FEED entries with `git show`. No side-branch files were edited or pushed.

The feed reports both a quantitative-target assessment and completion of
a separate Lean derivation of V004. To inspect the latter directly,
fetched `claude/lean-lane` at
`b980e52e4f709e88dd6cabae88073b578e0027fc` and read its STATE, assembly
statement/proof tail and the V004 assembly receipts.

## Quantitative target assessment

- **Retain the need for an additional theorem.** Quantitative versions of
  finite-automaton Cobham do not automatically classify infinite kernels
  with linear growth. Main's own [source audit](literature.md) verifies the
  difference and supplies an explicit counterexample to a separate-base
  linear-growth shortcut.
- **Correct the quantifier:** this goal asks for an unbounded ratio, or
  failure of every O(D) bound. The feed's displayed `kappa(D)/D -> infinity`
  is stronger and is not silently substituted for the activated goal.
- **Reject d-uniformity of the full target as written.** For d=5/61,
  `1_(d divides n)` is a nonconstant periodic invariant with bounded kernel.
  Thus “every nonconstant invariant has superlinear kernel growth” is false
  for those d. A theorem about *nonperiodic* colorings, or about joint growth
  forcing periodicity, could transfer; it is a different statement. Finite
  counts for selected cycle labels do not cover all invariant colorings.
- **Defer unreplayed numerical kernel counts and explicit-Tao claims.**
  Neither is a premise of V005. The earlier finite-prefix counts remain
  lower bounds only when witnessed by actual differing prefixes; matches
  are not whole-sequence equalities.

## What the Lean branch currently supplies

The inspected assembly statement assumes `CobhamStatement alpha` for all
sequences in alpha, defines automaticity as finiteness of the standard
kernel, and proves constancy on positive inputs from the two Collatz color
equations and binary automaticity. It derives finite range from a finite
kernel. Its printed type therefore matches V004 with the classical Cobham
input retained explicitly; it does not assume ternary automaticity of h.

The branch's saved build receipt reports success and its axiom receipt
lists `propext`, `Classical.choice` and `Quot.sound`. The main lane checked
the assembly source hash against the saved receipt. This batch did not
compile or independently replay the Lean derivation. Cobham remains a
named theorem hypothesis, not a formal theorem supplied by that file.
Accordingly this is a reported formal derivation with an inspected statement
and matching source receipt, not an independent main-lane kernel replay or
a formal verification of V005.

No message or instruction was sent to that user-owned lane. Its work is
useful verification input for the completed V004 result and does not
supply the active quantitative bound.

## Direction dispositions

D1 remains historical route evidence. D2's actual-claim controls, D5's
standing commit/push authorization and D7's separation of statement,
axiom and executed-replay checks are retained. D3's blanket transfer is
rejected; D4 remains deferred; D6 is historical. The present objective
and completion threshold come from the user, not the feed's assessment.
