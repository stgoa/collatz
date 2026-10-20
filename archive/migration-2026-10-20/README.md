# The 2026-10-20 knowledge-graph migration

The record of how the legacy tree became the node graph. At commit `be73a66` everything moved to a temporary `_triage/` folder. It was then migrated in batches B01–B18, each by one agent, and reviewed before the next started. [`../HISTORY.md`](../HISTORY.md) tells the story.

| File | What it is |
|---|---|
| [`TRIAGE.md`](TRIAGE.md) | The note that explained the temporary folder |
| [`MANIFEST.md`](MANIFEST.md) | One row per legacy unit (388), with its fate: the node(s) it became, its archive path, or why it was dropped. **Start here to find where a legacy file went.** |
| [`BATCH_BRIEF.md`](BATCH_BRIEF.md) | The procedure every batch followed: fidelity rules, status rules, certificates and evidence |
| [`PLAN-residual.md`](PLAN-residual.md) | The plan that split the residual-progress line R11–R94 into five batches |
| [`try_script.py`](try_script.py) | The helper batches used to run a moved script with a timeout |

Each node's `## History` section names its legacy path. `tools/legacy_paths.json` maps every legacy file to its current path (or to `null` when it was rewritten), and `tools/legacy_replay.py` replays legacy checkers unmodified in the old layout.
