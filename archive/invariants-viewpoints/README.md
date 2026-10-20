# Viewpoints

**Status: finished** (2026-10-18). The quantitative goal is unresolved and retired in favour of [`cycle_spectrum`](../cycle_spectrum/).

**What this line did.** It explored, breadth-first, which mathematical "language" might express a Collatz invariant. It then pursued arithmetic regularity of invariant colourings. The main theorem is V004: every binary-automatic colouring of the positive integers invariant under the Collatz map is constant. It is `formal` (Lean unit V004-iii), with Cobham's theorem as a named hypothesis. A d-uniform extension to all `3x+d`, [`V004/D_UNIFORM_AUTOMATIC.md`](V004/D_UNIFORM_AUTOMATIC.md), is `written`. The later quantitative target, an unbounded ratio of section count to binary depth ([brief](briefs/QUANTITATIVE_RIGIDITY_BRIEF.md)), was not reached.

- [`MAP.md`](MAP.md): the map of viewpoints. Its V1–V14 cards are candidate languages, not results.
- [`LOG.md`](LOG.md): the line's log.
- [`briefs/`](briefs/): the successive goal documents, oldest first:
  - [`VIEWPOINT_BRIEF.md`](briefs/VIEWPOINT_BRIEF.md) (V001–V002);
  - [`ARITHMETIC_REGULARITY_BRIEF.md`](briefs/ARITHMETIC_REGULARITY_BRIEF.md) (V003);
  - [`NEXT_GOAL_PROPOSAL.md`](briefs/NEXT_GOAL_PROPOSAL.md), which led to [`GLOBAL_RIGIDITY_BRIEF.md`](briefs/GLOBAL_RIGIDITY_BRIEF.md) (V004);
  - [`QUANTITATIVE_RIGIDITY_BRIEF.md`](briefs/QUANTITATIVE_RIGIDITY_BRIEF.md) (V005–V009).

| ID | Entry | Status |
|---|---|---|
| V001 | [lifting_probe.md](V001/lifting_probe.md) | probe |
| V002 | [SELECTION_REVIEW.md](V002/SELECTION_REVIEW.md) | language decision |
| V003 | [REPORT.md](V003/REPORT.md) | `written`; completed by V004 |
| V004 | [GLOBAL_RIGIDITY.md](V004/GLOBAL_RIGIDITY.md) | `formal` (Cobham as a hypothesis) |
| V005 | [REPORT.md](V005/REPORT.md) | `written`; V005-a `formal` |
| V006 | [REPORT.md](V006/REPORT.md) | `written`; V006-a `formal` |
| V007 | [REPORT.md](V007/REPORT.md) | `written`; V007-a `formal` |
| V008 | [REPORT.md](V008/REPORT.md) | `refuted` (proposed extension) |
| V009 | [REPORT.md](V009/REPORT.md) | `written` |

Verify: `python3 scripts/run_checks.py --line viewpoints`. This runs the `verify_examples.py` scripts of V002–V006.

The line is **frozen**: build on it in a new folder rather than editing it.
