# Reviews

Independent checks of claims made elsewhere in this repository. A review re-derives a proof, re-implements a computation from the statement (preferably without reusing the author's code), or checks Lean receipts against a prose claim. Its verdict is one of:
- `confirmed`;
- `confirmed with corrections`;
- `gap found`;
- `refuted`.

Reviews are what move a result from `written` to `proved` ([`AGENTS.md`](../AGENTS.md) §5).

## Adding a review

Create `reviews/<topic>/`, e.g. `reviews/2026-11-03-c011-arc-identity/`, with:
- a `README.md`: what was reviewed (path and commit), what was checked and how, and the verdict;
- any scripts, `check_<topic>.py`, with their receipts.

Then:
- link the review from the reviewed result's folder or index row;
- if the status should change, update the index rows in the same PR.

The [review playbook](../CONTRIBUTING.md) has the details.

## Contents

| Folder | Contents |
|---|---|
| [`side_lane/`](side_lane/README.md) | The side lane's checking scripts (2026-10-17…19): re-checks of main-lane rounds and batches, independent checks of Lean units, and the S-series producer scripts. The verdicts themselves were posted in the side lane's feed, now [`archive/side_lane/FEED.md`](../archive/side_lane/FEED.md). |

Reviews written inside result folders (e.g. `INDEPENDENT_REVIEW.md`, `SIDE_REVIEW.md` in `experiments/cycle_spectrum/C0xx/`) stay where they are.
