# History

How this repository came to be, and who (or what) did the work. All research here was produced by AI agents directed by the repository owner, over a few days in October 2026. Each agent worked in its own "lane" (a branch with a role).

## Timeline

| Date (2026) | Event |
|---|---|
| Oct 17 | The repository starts from a ChatGPT conversation's hand-off: [`archive/COLLATZ_PROGRAMME_MASTER_HANDOFF.md`](../archive/COLLATZ_PROGRAMME_MASTER_HANDOFF.md) and the packet-currents snapshot (`collatz_research_20261017/`). The **main lane** (ChatGPT/Codex, working on `main`) develops the *packet currents* programme, R1–R94. |
| Oct 17 | An **independent audit lane** (Claude) adds negative controls C1–C5 and a review, merged as PR #1. The same session continues as the **side lane** on `claude/sidekick`, an independent reviewer that posts verdicts in a feed. |
| Oct 18 | The main lane pivots to **Phase 6**, which grades named proof obligations on a route map. A Claude **audit lane** builds and checks an external positive-density Lean development (PR #2, merged). An **explicit-Tao lane** (Claude) closes its first leg with a scoped barrier. |
| Oct 18 | The **viewpoints** programme (V001–V009) explores invariant colourings; V004 proves finite-state rigidity. The **Lean lane** (Claude Fable) begins formalising the main lane's results. |
| Oct 18–19 | The owner activates the **cycle-spectrum** goal: reduced denominators of rational cycles across `3x+d`. The main lane produces C001–C013. |
| Oct 19 | The main lane pauses (ChatGPT quota), leaving C014 uncommitted. The side lane becomes the producer (S1–S13) and the Lean lane formalises its results. Highlights: `ρ ≥ 4`, the Denjoy–Koksma height bound and the rise lemma. The owner merges the Lean lane as PR #3. |
| Oct 19 (evening) | The owner stops all research lanes and asks for one clean layout on `main`, open to outside contributors. Every lane is merged with full history, C014 is committed as work in progress, the repository is restructured, and the MIT license is added. |

## Lanes and agents

| Lane | Agent | Role | Where its work lives now |
|---|---|---|---|
| Main | ChatGPT / Codex | Producer: R-, P6-, V- and C-series | `experiments/*` |
| Side lane (`sidekick`) | Claude (Opus) | Independent reviewer, then producer of S1–S13 | `experiments/cycle_spectrum/S*`, `reviews/side_lane/`, the feed in `archive/side_lane/FEED.md` |
| Lean lane | Claude (Fable) | Formal verification of claims, adversarial reviewer | `lean/` (journal: `lean/STATE.md`, `lean/LOG.md`) |
| Audit lane | Claude | Independent build audit of an external Lean artifact | `lean/audit/` |
| Explicit Tao | Claude | Making Tao (2019) explicit | `experiments/explicit_tao/` |
| PR1 lane | Claude | Negative controls for the packet-currents claims | `collatz_research_20261017/negative_controls/` |

The lanes cross-checked one another: the side lane refereed the main lane's batches and every Lean unit, and the Lean lane reviewed the side lane's results adversarially. The records of that traffic are in [`archive/side_lane/FEED.md`](../archive/side_lane/FEED.md), [`lean/LOG.md`](../lean/LOG.md) and the review files inside each batch folder.

## The 2026-10-19 restructure

Before the restructure, the content was spread over four branches. The root held seven large documents:
- `README`, `AGENTS`, `ROUTE_MAP`, `VIEWPOINT_MAP`;
- the master handoff;
- a 785 KB zip.

The restructure:
- merged `claude/sidekick`, `claude/lean-lane` and `claude/explicit-tao` into `main` with true merges, so every commit is preserved, then deleted those branches;
- moved files with `git mv` into the layout described in the [README](../README.md). [`archive/README.md`](../archive/README.md) gives the old-to-new path map;
- **kept every checked artefact byte-identical.**
  - Many checkers pin SHA-256 hashes of each other's sources, data and notes, so `experiments/` and `collatz_research_20261017/` keep their paths.
  - No Python script or receipt changed, apart from removing a hard-coded local path in five side-lane probes.
  - The notes whose hashes are re-verified by a running checker were not touched.
  - Relative links and plain-text paths in the other Markdown files were rewritten automatically.
  - Every checker that passed before the move was re-run after it;
- replaced the agent rules with a short [`AGENTS.md`](../AGENTS.md) and added [`CONTRIBUTING.md`](../CONTRIBUTING.md), the status pages in `docs/`, CI, and the MIT license.

The previous `README.md` and `AGENTS.md` are kept in [`archive/`](../archive/). Their links were updated to the new layout; their text is otherwise unchanged.
