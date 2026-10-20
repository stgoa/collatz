# `_triage/`: legacy content awaiting migration

This folder is **temporary**. It holds the whole repository as it stood at commit `be73a66`, before the move to the knowledge-graph layout described in [`../AGENTS.md`](../AGENTS.md).

Migration happens in batches, one commit per batch. Each batch takes a slice of this folder and does one of three things with each file:
- **reclassifies** it into a node under `areas/`, `sources/` or `lean/`, lightly edited to obey the conventions;
- **moves** it to `archive/` if it is valuable but does not fit the new layout;
- **drops** it if it is redundant, for example a duplicate or a generated file. The PR or commit message says why.

[`MANIFEST.md`](MANIFEST.md) lists every item and its fate. When every row is done, this folder is deleted.

Paths inside these files still refer to the old layout, so links and script loaders here are expected to be broken. Every checker was run at commit `be73a66`, and the results of that run are the reference for "this script passed".
