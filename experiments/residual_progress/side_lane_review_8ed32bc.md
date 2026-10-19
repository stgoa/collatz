# Independent basin reproduction at 8ed32bc

**Status: reproduced finite evidence, 18 October 2026.** Main baseline is
`61fd041bf837a276a1cca5a37dec9749c2bb6cb6`; the reviewed side commit is
`8ed32bc45912c7621227280013f32ae1387ff386`. This is newer work on the optional
`claude/sidekick` feed. The merged PR1 and its scope correction are covered
by the [previous assessment](side_lane_review_86ead16.md).

## What was reproduced

The pinned `reviews/side_lane/c0_basin_classify.c`, its Python wrapper
`c0_basin_receipt.py`, and its stored JSON receipt were extracted into
temporary storage. The wrapper ran unmodified with a 60-second process
timeout and finished in 5.71 seconds. Its new receipt is byte-identical
to the pinned receipt. File hashes, exact output and scope are retained
in the [reproduction record](side_lane_review_8ed32bc.json).

| Complete origin universe | Eligible origins | Hits on the specified cycle | Unknown |
|---|---:|---:|---:|
| `7153 < u < 7277133` |1,732,883|19|0|
| `7153 < u < 741545113` |176,754,119|1,939|0|

The origin conditions are oddness, coprimality with7153 and canonicality
of `-u/7153`. The larger computation has134 hits at first-hit depths
`d0=12k0+5`; precisely16 have adjusted cost `m=E0-19k0` in8..14.
Their complete list agrees with the [R92 boundary list](deeper_window/DEEPER_WINDOW.md).
The largest intermediate numerator is23,508,760,799,607,151.
No height cap is used. The implementation's path cap4096 was not reached;
its longest new segment is235. New-segment lengths depend on caching and
cycle detection and need not agree with the main implementation's206.

The source was inspected for the signed quotient convention, first-hit
clock and exponent accumulation, memoization and cycle handling. All
reported intermediate values, together with the starting range, keep
`3u-7153` below `2^63`, so the casts used in this completed execution
are exact. The C implementation also computes that expression in128 bits.
The wrapper's minimum weighted slope is a floating-point diagnostic;
this review does not use it as an exact inequality certificate.

## What changes in our assessment

Unlike the older feed reviewed at86ead16, this work **does** independently
reproduce R91's full finite origin classification, and it reproduces the
larger origin classification used in R92. These are useful checks by a
different implementation. The side program does not enumerate R92's
fourteen-step positive suffixes or verify the all-parameter lifting proof.
Those remain the responsibility of the main proof and its checked code.

The agreement strengthens confidence in the excluded window. It adds no
smaller-source current and no reason to abandon the signed-current
framework. The immediate research priority remains a later common target
or a different retained comparison, with complete domain coverage,
original-rank control and terminal supply. Another search inside the
proved window cannot furnish that construction.

To reproduce, extract the three named files from the exact side commit to
one temporary directory, then run `python3 c0_basin_receipt.py` there and
compare its generated JSON byte for byte with the extracted original.
The optional external branch was not edited or pushed.
