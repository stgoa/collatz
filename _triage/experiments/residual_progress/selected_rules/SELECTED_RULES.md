# Twelve conditional families under one critical-image rank

**Status: composition of written strict-rank rules, with finite exact
substitutions.** This dispatcher preserves every accepted plan of the
previous nine-family compiler and adds the three selected-input rules.
Unrecognized inputs remain signed premises. Universal current supply and
Collatz remain open; no asymptotic coverage or novelty claim is made.

## Interface and priority

Use the absorbed odd Syracuse map, `P(w)=[3w]-[w]`, and
`rho(w)=nu(3w)` for positive `w=5 mod8`. The order is:

1. The unchanged [nine-family dispatcher](../continued_rules/continued_rules.py),
   preserving its existing internal priority and covering
   R41/R44/R45/R46/R47/R48/R50/R52/R53.
2. [R55 selected forward](../selected_forward/SELECTED_FORWARD.md).
3. [R56 selected inverse](../selected_inverse/SELECTED_INVERSE.md).
4. [R57 selected-cycle exit](../selected_cycle_exit/SELECTED_CYCLE_EXIT.md).

The first successful rule is used. In particular the new rules cannot
replace or invalidate an old accepted plan, and a later rule does not get
priority merely because its proof produced a demonstration seed. The
separate R51 sigma rules are not imported into this dispatcher.

`one_step(w)` returns `None` if every test fails, or an integer current `J`
and nonzero signed W5 request coefficients `c(u)` satisfying

\[
 \operatorname{div}J=P(w)-\sum_u c(u)P(u),\qquad
 \rho(u)<\rho(w)\quad\text{for every remaining request}.       \tag{1}
\]

The shared R43 validator checks both assertions on every returned step,
including steps supplied by the old dispatcher. Equal coefficients are
combined without discarding their signs.

## Finite formal closure and conditional compilation

`close(w,max_nodes=None)` applies the [R43 signed closure
compiler](../critical_rank/CRITICAL_IMAGE_RANK.md). Every local plan has
finite support, and every recursive request in an accepted plan strictly
decreases a positive integer rank. Induction on that rank proves that
the formal substitution tree is finite. This is a termination statement
for constructing the **conditional plan**, not a proof that every leaf
has a recognized rule or a supplied current.

If a leaf `u` is unrecognized, it contributes the exact request `{u:1}`.
Its coefficient is multiplied by all signed coefficients on its route;
requests and current rows are then combined by linearity. Memoization may
reuse a constructed local result without changing (1). A caller's node
cap raises an unresolved computation error; reaching a cap supplies no
certificate. A root unrecognized immediately returns current `{}` and
request `{w:1}`.

`compile_plan(plan,supplied)` requires an exact integer current for every
remaining nonzero request. It checks each supplied boundary before adding
the current with the stored signed multiplicity. The result then has
exact boundary `P(w)`. Missing or malformed input is rejected. No orbit
discovery, conjectural absorption or numerical small-residual shortcut
occurs in these three APIs.

## Finite audit and retained evidence

Run

```sh
python3 experiments/residual_progress/selected_rules/check_selected_rules.py
```

The checker examines all 1024 W5 candidates below 8192. Every old accepted
plan is compared as a complete dictionary, and its current/request digest
must match the previously stored nine-family receipt. For each new
acceptance, the checker also reconstructs the first successful new rule
and verifies exact priority, current and coefficients. The resulting
counts are finite evidence, not asymptotic estimates.

The stored window has 722 accepted inputs versus 493 previously, with
229 new direct acceptances and 302 unresolved inputs. All 229 new window
acceptances choose R55 by priority. Separate exact witnesses 221,
382205941 and 11324620789 exercise the R55, R56 and R57 winning branches
respectively; this prevents small-window overlap from leaving either later
dispatch branch untested.

Seven supplied-current demonstrations use seeds 221, 2813, 10357, 5821,
93301, 1105909 and 11324620789. Each closes all recognized descendants
before supplying the remaining leaves. The full closed plans, supplied
input currents and output currents for 5821 and 1105909 are retained in
`selected_rules_audit.json`; the other examples retain exact hashes and
request lists and are reproduced by the checker. Fixture input discovery
has cycle detection, a 10000-step cap and a 512-bit cap. Formal closure
has a 10000-node cap. These capped discoveries are finite demonstration
inputs, independent of the symbolic rule proofs.

The checker additionally retains an explicit unrecognized root and tests
invalid domains, a closure cap, missing supply and incorrect supply.
`--write-receipt` regenerates the evidence; the default invocation compares
the complete result and source hashes against the stored receipt.
The seven conversions use 12 distinct supplied pairs in total. The closed
5821 plan has no remaining input and produces a 40-row exact current;
1105909 retains four signed supplied inputs and produces 142 rows. Five
negative checks cover invalid domains, the node cap and invalid supply.

This enlarged conditional compiler can be used wherever an exact supplied
W5 comparison is required. Its unresolved leaves are the remaining
obligation. The previous fixed-procedure R54 obstruction is not a claim
against this enlarged rule collection, and no conclusion about a union
with the separate sigma induction is drawn.
