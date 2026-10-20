# Cycle spectrum

**Status: active.** The research lanes paused on 2026-10-19, and new contributions are welcome.

**Goal.** Exclude nontrivial cycles of `3x+1` by studying the reduced denominators `den(w)` of rational cycles across the whole `3x+d` family. The cycle half of Collatz is the statement that `den(w) = 1` only for repetitions of the word `(2)`.

The intermediate target is an explicit `F(m) → ∞` such that every hypothetical cycle word differs from each of its nonidentity rotations in at least `F(m)` places. In the notation of [`docs/CONVENTIONS.md`](../../docs/CONVENTIONS.md), this is `ρ(w) ≥ F(m)`.

- [`BRIEF.md`](BRIEF.md): the goal as set by the owner, with the success ladder and the standing requirements on controls. Its opening part is a stack of dated status updates; the goal text proper starts at its "Prove that Collatz has no nontrivial cycles" paragraph.
- [`LOG.md`](LOG.md): the batch-by-batch log of C001–C013.
- Current standing: [`docs/STATUS.md`](../../docs/STATUS.md). Open targets: [`docs/FRONTIER.md`](../../docs/FRONTIER.md).

## Index

The C-batches come from the main lane (ChatGPT/Codex). The S-results come from the side lane (Claude); their scripts and receipts live in [`reviews/side_lane/`](../../reviews/side_lane/) under the prefix `sNN_`.

Lean unit statuses: [`lean/STATE.md`](../../lean/STATE.md).

| ID | Entry | One line | Status |
|---|---|---|---|
| C001 | [REPORT](C001/REPORT.md) | A fixed perturbation bounds denominator cancellation for repeated blocks. | `written`; C001-a/b `formal` |
| C002 | [REPORT](C002/REPORT.md) | Two growing blocks; uniform exclusion for distinct equal-total blocks. | `written`; C002-a and part of C002-b `formal` |
| C003 | [REPORT](C003/REPORT.md) | Bounded-denominator finiteness, uniform over changing blocks. | `written`, agent-reviewed; C003-a `formal` |
| C004 | [REPORT](C004/REPORT.md) | `H < 2L` ⟺ mechanical word ⟹ every nontrivial cycle has `H > 2L`. | `formal` |
| C005 | [REPORT](C005/REPORT.md) | Concatenations of rotations of a mechanical base are excluded. | `written`; core `formal` |
| C006 | [REPORT](C006/REPORT.md) | Ordered cycles: few height changes force large gaps. | `written` (two-log bound); units `formal` |
| C007 | [REPORT](C007/REPORT.md) | Height–denominator candidate `B ≤ q − 1`; two shortcuts refuted. | `open` / `refuted` |
| C008 | [REPORT](C008/REPORT.md) | Sorted residues; primewise matching refuted. | `written` / `refuted` |
| C009 | [REPORT](C009/REPORT.md) | Excursion compression rejected. | `refuted` (mechanism) |
| C010 | [REPORT](C010/REPORT.md) | Exact gap lattices; local rounding rejected. | `written`; units `formal` |
| C011 | [REPORT](C011/REPORT.md) | Two-defect rotations are excluded (`ρ ≥ 3`). | `conditional` (Matveev, period); core `formal` |
| C012 | [REPORT](C012/REPORT.md) | What a uniform rotation bound must retain. | `written` / `refuted` |
| C013 | [REPORT](C013/REPORT.md) | Shared background with markers forces denominator growth. | `conditional` (Matveev); units `formal` |
| C014 | [COMPATIBLE_ARCS](C014/COMPATIBLE_ARCS.md) | Compatible arcs: limits of a common partition. | **work in progress**, unreviewed |
| S01 | [feed entry](../../archive/side_lane/FEED.md) | The J-term gap lead; no separate note. | Lean units S1-a…e `formal` |
| S02 | [note](S02/RENORMALISATION.md) | Run-compression renormalisation rejected. | `refuted` (mechanism) |
| S03 | [note](S03/INVERSION_PAIRS.md) | Ordering to `H < 16L` reduces to the pair `(n, 8n+1)`. | reduction `formal` |
| S04 | [note](S04/BAND1_GCD.md) | No `gcd` law on ordered band-1 cycles. | `evidence` |
| S05 | [note](S05/MISMATCH_HEIGHT.md) | Mismatches against height: `s > log₂3·m/(B + 342 log₂m + 172)`. | `formal`, conditional on EXT-1 |
| S06 | [note](S06/C011_VIA_S5.md) | C011 via S05, without Matveev. | `formal`, conditional on EXT-1 |
| S07 | [note](S07/THREE_MISMATCHES.md) | No 3-mismatch rotation: `ρ ≥ 4`. | `formal`, conditional on EXT-1 |
| S08 | [note](S08/FOUR_MISMATCH_MAP.md) | The 4-mismatch map; headline withdrawn. | `withdrawn` |
| S09 | [note](S09/DENOMINATOR_LAW.md) | Denominator laws for 2 and 3 mismatches, for every `3x+q`. | `formal` |
| S10 | [note](S10/MULTI_ROTATION.md) | Multi-rotation model: the size method's reach is 4. | `evidence` (model) |
| S11 | [note](S11/C013_GAP.md) | C013 with EXT-1 instead of Matveev. | `written`, conditional on EXT-1 |
| S12 | [note](S12/DENJOY_KOKSMA.md) | Denjoy–Koksma height bound and denominator law. | `formal` |
| S13 | [note](S13/RISE_LEMMA.md) | Rise lemma; growth for short rotations; reduction to the largest letter. | lemma `formal`; numbers conditional on EXT-1 |

## Running the checks

```sh
python3 scripts/run_checks.py --line cycle_spectrum      # every C-batch checker (~6 min)
python3 experiments/cycle_spectrum/C011/check_rotation_defects.py   # one batch
```

The C008–C013 `check_delivery.py` scripts are pinned to the commits that produced them, so they fail at `HEAD` by design ([`scripts/run_checks.py`](../../scripts/run_checks.py) skips them).

Shared data:
- [`C001/actual_cycles.json`](C001/actual_cycles.json), the actual-cycle corpus used by later batches;
- [`../phase6/cycle_fixtures.json`](../phase6/cycle_fixtures.json).

## Adding a result

Create `experiments/cycle_spectrum/<YYYY-MM-DD>-<slug>/` with a `README.md` carrying the status header of [`AGENTS.md`](../../AGENTS.md) §4. Add a row to the index above and to [`docs/RESULTS.md`](../../docs/RESULTS.md). Every argument must respect the `3x+d` controls.
