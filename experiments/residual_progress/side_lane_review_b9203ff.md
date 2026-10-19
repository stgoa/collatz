# Pinned review: clocks, merger cells and the merged audit PR

Date: 2026-10-18. Main was `355c173fad974c4b4605f3fcd18276f2d4032397`.
The optional side lane was first read at
`49083cbb83c6fc923b34a69184a4f171034179de`, then at
`b9203ff32801b15725d4c9b7e5890386f1d8a07f`. The independent branch was not modified.

## Remote PR and research decision

The user's report of a merged parallel PR prompted a fresh fetch of main
and the side lane, and a GitHub merged-PR query. The query returned only
[PR1](https://github.com/stgoa/collatz/pull/1), merged at
2026-10-17 21:30:44 UTC as `ba6b3371fabd7fcabebb442d7c89ea3ed5c02149`.
That commit is already an ancestor of current main. Its original PR body
still contains the broad certificate-minimality conclusion; the corrected
repository note and [review](../packet_currents/negative_controls/PR1_REVIEW.md)
retain the valid lemma and explicit counterexamples to the overstatement.

Keep the false-map controls, independent arithmetic and conditional
minimality theorem. They do not exclude alternative one-sided certificates
or structural construction. They do exclude treating early compression
alone as a termination argument. The newer independent work is on the
side branch; it is not a second merged PR in this remote read.

The research decision is to continue exact comparisons with supplied
smaller inputs, with whole-domain decisions and the original parent rank
as the progress test. R85 requires input-dependent clocks in any universal
history approach. A new successful subfamily is partial progress; every
unresolved signed input and the missing global termination argument must
remain explicit. No general abandonment of currents follows from this PR.

## Reproductions

Each probe was inspected, materialized unchanged with its exact pinned
dependencies in temporary storage, and run without Python optimization.
Every generated receipt matched its published JSON byte for byte.

| Pin | Probe | Process cap | Reproduced scope |
|---|---|---:|---|
| `49083cb` | `batch_r81_r83_check.py` | 90 seconds | 3,301 R80-cell lifts, 400 random merger cells, R83 arithmetic parameters for s=1,2 |
| `49083cb` | `r56_selected_inverse_check.py` | 90 seconds | 4,800 exact word, comparison-identity and threshold cases over both k=4,8 branches |
| `b9203ff` | `batch_r84_r85_check.py` | 60 seconds | 3,000 R84 prefixes, 300 sharp twentieth-step cases, 24 bounded R85 brute-force instances |

These are finite arithmetic checks. R83's full CRT construction and signed
currents were not rebuilt by its probe. R84's fourteen-template decision
was not rebuilt by the new probe. R85's independent enumeration is bounded
by the tested sources and clocks. No probe replaces a written universal
argument or supplies all terminal pair currents.

## Correction to the R81 probe's claimed minimality coverage

The binary half-period test runs. The claimed ternary-removal check is
guarded by `M % 3 == 0 and P % 3 == 0`. This condition never holds:
the two period factors are respectively `3^max(b-a,0)` and
`3^max(a-b,0)`, so at most one is divisible by3. Consequently the receipt
does not test the ternary-removal claim, despite the feed's description.

This is a coverage defect in the finite probe, not a counterexample to
R81. Coupled integrality proves the relevant minimality: removing a factor3
from the period on the divisible side would require dividing the other,
nondivisible period by3 as well. The purported next coupled lift would
then have a noninteger coordinate. Preserve the distinction between that
argument and the branch which the probe actually executes.

## Pinned SHA-256 values

Paths in the first column are relative to the pinned side branch.

| File | SHA-256 |
|---|---|
| `reviews/side_lane/batch_r81_r83_check.py` | `274f7581af91dc84e6b09b0aaa0b20caff7d280f8cb3d24816eec1c17a4b1e84` |
| `reviews/side_lane/batch_r81_r83_check.json` | `70d8a78fd624806cf03b9b062fd173883ee5f71c9c52a98323c063914968fe7b` |
| `reviews/side_lane/r56_selected_inverse_check.py` | `ce986126042ad7537e44d19cd98898b7f7de40246dcff3eb7d7f4953b95a02e9` |
| `reviews/side_lane/r56_selected_inverse_check.json` | `4ed429453d4001c6d02c0a3a20a2c9ad96f5d2624fd809bf3f20c0a0c3ae4849` |
| `reviews/side_lane/batch_r84_r85_check.py` | `f19a46ed83fec41fb0fbe27d5f43af20b1100e02f82a79162ee15d4d74db6709` |
| `reviews/side_lane/batch_r84_r85_check.json` | `358d0af434935d691438a0c7b7f8c657d2c181044f8bb68f423ebd1607a2e37c` |
| `reviews/side_lane/fibre_count_check.py` | `071b2d076702ff0ab87746b9c130c0271c2adcf82b45f59e5d0ffec53b14923a` |
| `experiments/packet_currents/negative_controls/affine_controls.py` | `9e5ad66deaf7ede55b1d607f6d85d57f58d38e9dd2c551d45f1b7a2d58538e3c` |

The last two dependencies were identical at both pins.
