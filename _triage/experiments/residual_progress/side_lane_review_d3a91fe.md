# Pinned review of the R73/R74 side-lane check

Date: 2026-10-18. Optional external input reviewed at
`d3a91fe33f2c4cd1dcdc0576b78558963278f4f8` on `origin/claude/sidekick`.
The source, independent step implementation and published receipt were read
from that exact commit and materialized in temporary storage. The side
branch was not changed.

The unmodified `reviews/side_lane/batch_r73_r74_check.py` passed, and its output
receipt matched the pinned `batch_r73_r74_check.json` byte for byte. The
execution had a 30-second cap and completed in under one second.

| Pinned file | SHA-256 |
|---|---|
| `reviews/side_lane/batch_r73_r74_check.py` | `b89863a6e4faf20ac9b6d1b7ab3e1f6f79f1998fb702946f41200906892f5045` |
| `reviews/side_lane/batch_r73_r74_check.json` | `711aacecf34c2b31c2ab2744ca6ab47e8e1f0ae4d2bee5bf091b378269681d3e` |
| `experiments/packet_currents/negative_controls/affine_controls.py` | `9e5ad66deaf7ede55b1d607f6d85d57f58d38e9dd2c551d45f1b7a2d58538e3c` |

## What was reproduced

- R73: 4,000 members of each of the two pair identities, testing W5
  membership, strict decrease of the pair index and the stated ordinary
  endpoint clocks. The probe does not reconstruct the full signed currents
  or directly test critical ranks.
- R74: 600 sampled words of length at most12, with three positive lifts per
  word. It checks affine composition, every intermediate complete return
  domain, integrality, the terminal guard and strict growth.
- The fixed point of each sampled periodic word is a negative rational.
  The general eventually periodic conclusion still relies on the written
  pullback argument; this probe does not enumerate arbitrary prefixes.

The receipt contains `status: PASS`, `r73_members_each: 4000` and
`r74_words: 600`. These are finite independent arithmetic checks, not a
proof that the possible positive aperiodic survivor set is empty.

## Use in the next batch

These checks support the existing results without adding a new rule or
coverage claim. The feed's separate ancestor census and wider synthesis
were read, but not reproduced in this batch or imported as proof premises.
In particular, the census is finite and does not establish an asymptotic
density or an obstruction to every possible current construction.

The current investigation changes the source basis before translating rank
rules and separately tests constraints on one fixed positive return seed.
Neither direction assumes the truth of a side-lane heuristic.
