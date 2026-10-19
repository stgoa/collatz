# V007 — Read-only side-lane assessment

**Reviewed pin:** `bc76c7d3f3d31c109d63984c595866ba9054aef3`, fetched
from `origin/claude/sidekick` and read through `git show` on 2026-10-18.
Both `sidekick/DIRECTIONS.md` and the newest `sidekick/FEED.md` entries
were inspected. The branch was not edited.

## New evidence and its scope

The newest entry reports independent reproduction of V006's mixed
digit-count separation theorem, its complementary-block identities and
the adjacent11-pair control. This agrees with the main-lane proof scope:
the quadratic conclusion needs an actual positive digit-count section.
It does not supply such a section for an arbitrary invariant.

The lane also reports that its tested cycle colorings for d=5,13,61 have
no nonconstant digit-count section within the stated finite range. Those
colorings are not hypothetical linear-growth d=1 invariants. The test
therefore neither establishes nor refutes the missing extraction theorem.
No universal nonexistence or novelty conclusion is imported from that scan.

The same entry reports verification of the Lean lane's scalar-interface
source and receipt at `3dd6cb7`, including the strong-induction converse
and the value at zero. This batch read that assessment; it did not fetch,
compile or independently replay the Lean artifact. The mathematical
scalar interface used here remains the independently reviewed written
[V005 argument](../V005/scalar_interface.md). The reported formal work
adds no quantitative growth bound.

## Direction decisions

- D1 remains useful historical evidence, with the existing scope corrections.
- D2's actual-map cycle controls remain required when a claim uses them.
- D3's blanket dismissal of almost-all absorption results remains rejected.
- D4 remains deferred; classify a historical input when it is used.
- D5's persistence and no-waiting protocol remains in force.
- D6's route calibration sequence remains historical management guidance.
- D7's statement, axiom and independent-replay distinctions remain in force.

No side proposal changes the active completion criterion: every nonconstant
finite-valued invariant must have unbounded `kappa_h(D)/(D+1)`. The bounded
separator investigation is progress toward that question, not a replacement
goal and not evidence of convergence.
