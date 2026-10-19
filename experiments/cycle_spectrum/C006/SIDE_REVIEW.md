# C006 — Side-lane review

The fetch of `origin main claude/sidekick` was attempted this batch.
Automatic approval review failed because its selected model was at
capacity; the fetch was not executed. The tool identified a review
service failure, not an unsafe-action determination. No workaround was
used. A later authorized retry succeeded, as recorded below.

The locally available tracking ref initially read was
`2ea1c7f6e51e31b80d354b458d8fa121e4f6e8aa`. It later advanced in the
shared repository to `f054db41be4688dec8200208e4994e96379bc0dd`.
At that latter pin, `sidekick/DIRECTIONS.md` and `sidekick/FEED.md`
were read with `git show`. This review treats their contents as external
research input. No side branch was edited, committed to or pushed.

At final review, `git fetch origin main claude/sidekick` succeeded.
Main remained at `61cf54ad52df1caa5cc250b0d1464432ed90b162`; the fetched
side pin is `9ac12a8b7c960333f6ee7c2a0f39651209b486b9`. DIRECTIONS
and the updated FEED were read again at that pin. DIRECTIONS retains
SHA-256 `9581e29ef2b6e462065fc32c2c597f1b459a3411ec8690ff82ed928c3dde0793`.

## New Lean reports and their exact scope

- C003-a, reported Lean commit `8388c38`: the effective contracting
  bounds and supporting algebra are reported built with standard axioms
  and a matching source hash. The effective enumeration, proportional
  comparison, Corvaja–Zannier argument and d499 example are not part of
  that reported formalization.
- C004-a, reported Lean commit `7959806`: the one-letter cut identities,
  mechanical word identities and the direction mechanical implies
  narrow are reported built. The feed reports 75 declarations and
  standard-axiom subsets, with no diagnostics or proof placeholders.
  The converse narrow implies mechanical, R71's unit gcd, integer
  exclusion, full spectrum law and Smith statements are explicitly
  outside that reported unit.
- C004-b part1, reported Lean commit `5be60e6`, added in the final
  fetched feed: cyclic intercept recursion, adjacent-exponent dichotomy,
  high/low successor ordering and rank lemmas on an abstract NarrowCycle
  structure are reported checked. The feed reports 103 declarations,
  standard-axiom subsets, a clean build/source scan and matching hash.
  The full forward mechanical-word identification and its coprimality
  conclusion are still a later unit. Main did not replay this build.

These reports improve the available validation record for earlier
algebra. Main did not independently compile or kernel-replay those Lean
commits in C006. They verify no C006 theorem here and supply no missing
denominator-one argument. The new gap proof and finite checker were
reviewed independently within this batch.

The previous bounded-discrepancy correction remains: an m/L term cannot
be dropped, and a claim for every discrepancy ceiling is not a smaller
goal than all-cycle exclusion. C005's q23 word `(2,3)` remains the exact
control against an unqualified identification of narrowness with a
discrepancy below one centered on log_2(3).

## Direction assessment

| Proposal | Assessment for this batch |
| --- | --- |
| D1 | Retain historical routes as evidence; the active cycle goal controls scope. |
| D2 | Retain actual-cycle controls. All eleven stored raw fixtures are exercised by the C006 checker. |
| D3 | Reject the blanket almost-all transfer rule; previous correction stands. |
| D4 | Defer a repository-wide transfer taxonomy; check each imported premise when used. |
| D5 | Retain standing authorization to finish and publish batches without routine approval requests. |
| D6 | Historical calibration management; it does not replace the active batch criterion. |
| D7 | Retain statement matching and independent formal replay distinctions. Reported builds are not main's replay. |
| D8 | Proposal for a replaced quantitative goal; it does not change the cycle objective. |

The user's high-level goal question is addressed by recommending the
whole ordered-cycle exclusion as an intermediate target under the
unchanged all-cycle headline. Neither proposing that milestone nor
proving fixed-`q,J` finiteness completes or replaces the active goal.
