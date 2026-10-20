# Pinned review: independent native-prefix and high-history checks

Date: 2026-10-18. Reviewed optional side-lane commit
`9849c53d58bd83e62f17e5979ff354a36fe4bde0`. Remote main remained
`3b0c8a536281ab2c4ed24b2f1d5ee5708ad8d10b`. GitHub again listed only
[PR1](https://github.com/stgoa/collatz/pull/1), merged on17 October and
already incorporated. The latest findings are on the separate side branch.
That branch was read without modification.

## Reproduction

The unmodified `reviews/side_lane/batch_r78_r80_check.py` was materialized
with its exact pinned dependencies in temporary storage and run with a
60-second process cap. Its generated JSON was byte-identical to the
published receipt. All checks passed:

- 2,000 R78 native prefixes, with exact six-arrow valuations and normalization;
- 3,000 R79 return-count cases, including forced high binary orders;
- 30 R80 family cases, D12..16 and t0..5, with both clocks, peak and phases;
- complete forward closure of every canonical origin below11547, excluding
  that anchor and hence certifying no smaller canonical ancestor at any depth.

The anchor conclusion uses a complete finite absorbing closure, not merely
a bounded inverse search. The probe independently reconstructs the arithmetic
with its own step/normalizer; it does not reconstruct the full signed
R78–R80 current tables or prove the family quantifiers by sampling. Those
remain supported by the written proofs and main's separate certificates.

| Pinned file | SHA-256 |
|---|---|
| `reviews/side_lane/batch_r78_r80_check.py` | `59d0b84fe0cfb462c7bf38e6df21b89b072e810cfd7c00fe8f072812c76d6810` |
| `reviews/side_lane/batch_r78_r80_check.json` | `f477cf6a4a8ad9cd33928fa83be83d0b4167df7ffbbc067bfacef34855cb58ec` |
| `reviews/side_lane/fibre_count_check.py` | `071b2d076702ff0ab87746b9c130c0271c2adcf82b45f59e5d0ffec53b14923a` |
| `experiments/packet_currents/negative_controls/affine_controls.py` | `9e5ad66deaf7ede55b1d607f6d85d57f58d38e9dd2c551d45f1b7a2d58538e3c` |

The dependency hashes match the preceding pinned review. The new feed also
accepts that the informal average-valuation complexity refinement needs
explicit window and prefix hypotheses; it is not promoted as a theorem.
The earlier [general-spacing review](side_lane_review_fcc7e88.md) stands.

## Opinion and research decision

Retain the merged PR's negative controls and conditional minimality lemma.
The [exact counterexamples](../packet_currents/negative_controls/PR1_REVIEW.md)
still refute its broad no-alternative-certificate conclusion. These controls
make early numerical compression an inadequate progress test; they do not
make exact constructive comparisons pointless.

Continue the focused pivot to smaller-origin histories. R81 provides complete
arithmetic cells for paired words. R82 gives a complete all-ray history
classification within a stated ternary horizon. R83 constructs high meetings
after any prescribed number of native returns, but also proves a fixed
failure of the named inverse procedure. Together these sharpen both the
constructor and its limitations. The remaining target is an entire unresolved
type with all signed inputs smaller at the original rank and universal
terminal supply. No broad abandonment of currents, coverage theorem or
Collatz proof follows from the parallel work.
