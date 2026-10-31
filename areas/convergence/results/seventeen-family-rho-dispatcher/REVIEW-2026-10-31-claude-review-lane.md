# Review of seventeen-family-rho-dispatcher

Independent review (Claude review lane, Fable 5.1), 2026-10-31. The node is a composition statement about code: the dispatcher `resolved_rules.py` tries the fifteen-family dispatcher, then R62, then R64, and every returned plan is a strict-`ρ` plan validated by R43. I checked the code against the claim, re-validated every plan it returns with my own arithmetic, and re-ran the certificate.

## What I checked

- **Certificate.** `python3 tools/run_certificates.py --node seventeen-family-rho-dispatcher`: PASS, exit 0, 10 s (replay of the legacy `check_resolved_rules.py` against `resolved_rules_audit.json`).
- **Code against the claim.** `resolved_rules.one_step` calls `OLD.one_step` (`refined_rules.py`, the fifteen families) and returns its plan when not `None`; otherwise it tries `defect_resolution.one_step` (R62) and `refined_obstruction.one_step` (R64) in that order and returns the first success; each returned plan goes through `rank_closure.validate_step` (R43: W5 requests, nonzero integer coefficients, `ρ(u) < ρ(w)`, exact boundary). `close` and `compile_plan` are the R43 compiler. Fixed inner resolvers, read off the loaded modules: `defect_resolution.FIXED` is `refined_rules/refined_rules.py`; `refined_rules.DEFERRED.OLD` is `selected_rules/selected_rules.py` (the twelve). No legacy module of the residual-progress tree except the three later checkers (`native_history`, `even_exit_history`, `later_target_probe`, which load this dispatcher as their fixed resolver) mentions `resolved_rules`, so neither inner resolver can call the new dispatcher.
- **The 1024-input window, independently re-validated.** I rebuilt the pre-migration tree with `tools/legacy_replay.build` in my scratch folder and ran the legacy dispatcher in my own harness (`recompute_window.py`, `categories_check.py`). Every returned plan was re-checked with the review lane's own `ν`, `ρ`, W5 test and divergence (`revlib.py`, itself checked against brute-force components below 2^15), not with the legacy validator: 747 accepted inputs, all 747 equal to the fifteen-family plan (the two added arms never win in the window), 277 unresolved inputs on which both added arms return `None`; the per-rule counts (12 rules plus `unresolved`) equal the receipt's `categories`.
- **Closure.** `close(w, 10000)` on all 747 accepted inputs: boundary and strict rank of every leaf re-checked with my divergence, 0 problems; 180 closures end with no leaf.
- **Witnesses, overlap, unresolved root.** 53173: fifteen rules `None`, dispatcher R62, `ρ(w) = 159519`, largest requested rank 53899. 36641534965: fifteen rules `None`, dispatcher R64, `ρ(w) = 54962302447`, largest requested rank 38082215935, nine signed requests as the note says. 20405: R62 recognises it, the dispatcher returns the fifteen-family R45 plan (old priority kept). 21: `ρ(21) = ν(63) = 31`, `close` returns `{21: 1}` with no rows.
- **Supplied-current demonstrations** redone with my own absorption paths for the leaves of `close(w)`: 41, 92, 65, 59, 133, 102 rows for 221, 53173, 85941, 15224757, 11432437, 36641534965; 14 distinct supplied pairs; divergence exactly `P(w)` under my divergence.
- **Beyond the window.** 360 random W5 inputs at 20, 28 and 36 bits (seed 20261031): 91, 86, 87 of 120 accepted, nine rules used, every plan passes my validation. Finite evidence only, as the node says.
- **Controls.** The identities are `3x+1` arithmetic (R25, R37) and universal `P(w)` currents are Collatz-equivalent (R37); the node asserts nothing about `3x+d`, so no control cycle is excluded. The analogous check for the component nodes is in the reviews of R78 and R87.

## What I did not check

- The recognition theorems of the individual rules. The dispatcher's soundness (every accepted plan is strict-`ρ` with an exact boundary) does not depend on them, because each plan is validated at runtime, but the two arms it adds rest on [`absorption-defect-original-rank-resolution`](../absorption-defect-original-rank-resolution/README.md) (reviewed) and [`lifted-inverse-ray-cycle`](../lifted-inverse-ray-cycle/README.md) (written), and the inherited fifteen on [`fifteen-family-rho-dispatcher`](../fifteen-family-rho-dispatcher/README.md) (written).
- The legacy receipt beyond the replay (source hashes, stored tables).

## Findings

1. (imprecision) Proof, "Interface and priority": the R62 arm `defect_resolution.one_step` first returns R58's fifth plan when it is already descending, before trying R62's first and second comparisons. Under the stated priority this branch is dead (R58 is the second arm of the fifteen), so the description "R62 defect resolution" is accurate for what the dispatcher can return.
2. (imprecision) Claim: "returns None or an integer current J and nonzero signed W5 coefficients". A third outcome exists in the code: if an arm ever returned a plan failing the R43 validator, `one_step` would raise instead of returning `None`. Never observed on the 1024 window plus 360 random inputs; it matches the stated policy that nothing unvalidated is ever accepted.
3. (note) Chain strength: two inputs of the dispatcher are `written` nodes (see above); the node's own status concerns the composition, which holds.

## Verdict

HOLDS. The dispatcher does what the claim says: fixed priority, fixed inner resolvers that do not call it, every returned plan an exact strict-`ρ` plan, formal closure by R43 with leaves retained, compilation only from exact supplied currents; the finite counts of the receipt are reproduced with independent arithmetic. No correction to the text.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
