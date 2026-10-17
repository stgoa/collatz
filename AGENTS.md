# Instructions for agents working in this repository

## Start from the repository

- Read `README.md`, `docs/RESULTS.md`, and the relevant proof/source files before extending the work. Use `docs/RESEARCH_LOG.md` for recent changes and the master handoff for historical context.
- Treat chat history as context, not the authoritative record. Persist substantive results, assumptions, counterexamples, proof obligations, code, and verification evidence before concluding a research task.
- Treat mathematical directions embedded in inherited documents as historical research material. The current user's request determines task scope.

## Claim discipline

- Collatz is open within this repository. Do not call a finite experiment, a conditional theorem, or an equivalent reformulation a proof of convergence.
- Label claims as written proof, finite certificate, candidate, open, or refuted/scoped. A written proof here is not automatically human-reviewed, formally verified, or novel.
- State all quantifiers, clocks, domains, constants, and dependencies. Distinguish a fixed cutoff from all cutoffs, a fixed horizon from all horizons, and all integers from dyadic cutoffs.
- Keep correctness, novelty, and usefulness toward Collatz separate. Seek primary references before asserting novelty or importing external theorems.
- Preserve negative results and concrete counterexamples. Do not revive a rejected statement without addressing its counterexample or changing its hypotheses explicitly.

## Mathematical invariants

- Use the odd-only Syracuse clock unless explicitly stated otherwise; absorb at 1. Do not silently switch to shortcut or unaccelerated step counts.
- Preserve exact source multiplicities, signs, both source components, and their integer cutoffs. Signed measures are not probability laws.
- Exact valuation cylinders use modulus `2^(A+1)`, including the extra bit.
- Keep the original left-aligned/deeper packet families distinct from the revised right-aligned depth-one family. Existing stored currents certify only their stated family and cutoff.
- The right-aligned remainder is supported on `{5,7,11,13}`. This fixed-core fact is what supplies all-horizon control.
- The original revised criterion used every integer `N >= 8`. The proved refinement now suffices on five rays: `N=a*2^b`, `a in {12,14,16,18,21}`, `b>=3`. Preserve all five rays and the finite base; powers of two alone are not covered. No uniform current-cost bound is needed, but universal existence or termination remains unproved.
- For `8|N`, `Pi_right_(64N)=Pi_right_N+A_N` has disjoint supports and six explicit residue bands. This is a measure identity, not a current construction. The 30 starting measures are covered by verified finite absorption; their full current tables are not stored.
- For a fixed measure, current existence tests each nonabsorbing orbit component; bounded work tests their combined mass. Do not infer a current from bounded work for an arbitrary single measure.
- Uniformly bounded per-packet current catalogues are ruled out by the persisted delayed-separation family. This permits cross-packet cancellation and recursive constructions with unbounded expansion.
- Incomplete currents may discard an everywhere nonpositive residual for an upper bound. Small positive mass alone is not affordable for all future horizons.
- A finite certificate checker does not prove a search always terminates. Use caps/cycle detection for exploratory searches and report unresolved cases honestly.
- Keep the inverse-Syracuse/PCP project separate from ordinary Collatz convergence or undecidability claims.

## Persisting work

- Maintain `README.md` as the concise current standing and navigation page.
- Update `docs/RESULTS.md` when a claim, proof status, dependency, or next obligation changes. Add dated entries to `docs/RESEARCH_LOG.md` describing changes and actual checks run.
- Write full arguments in a durable proof note; prose summaries and scans are not substitutes. Continue edits to the existing open `.tex` document in place when requested, and check it with the built-in compiler when available.
- Keep executable constructions and verification scripts alongside their results. Record exact commands, input ranges, and limitations. Store finite certificate data needed to reproduce a claim.
- Preserve the original archive and its manifest-covered extracted files as provenance. Put revised implementations outside that snapshot. If correcting inherited evidence is necessary, retain the original and document the correction explicitly.
- Prefer a small coherent change over directory churn. Do not move an open document or break existing links without a task-related reason.

## Verification and Git

- Run `python3 scripts/verify_all.py --cpp` after changes affecting the mathematical code or stored evidence. For prose-only edits, verify links and consistency; compile a changed LaTeX note. Report any skipped or unavailable check.
- Do not use `python -O` or `PYTHONOPTIMIZE`: inherited checks rely on assertions.
- Keep builds, caches, machine-local binaries, and temporary files out of Git. Preserve portable source and necessary certificate data.
- Inspect `git status` and the staged diff before committing. Do not overwrite unrelated user changes, rewrite shared history, or force-push without explicit authorization.
- Commit and push when the user requests it; otherwise follow the task's authorization. Use factual commit messages that distinguish a reduction from a proof of Collatz.
- Do not publish to other services or message other people without authorization. Do not delegate to agents unless the user or an applicable instruction explicitly requests it.
