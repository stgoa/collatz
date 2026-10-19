# C007 root review and verification

## Mathematical review

The main and independent notes agree on the exact min-height inequality
and the missing weighted-divisibility step. I checked the modular lemma
directly from `2^c_i z_(i+1)=3z_i+q2^(-h_i)`, preserving the reduced
denominator condition separately from primitive period. The weighted
intercept uses `P_i-h_i=sum_(j<i) a_j`, so its displayed powers are
nonnegative integers on actual odd cycles.

Two wording issues were corrected before publication:

1. Reduction of the numerator/denominator pair, rather than period
   primitivity alone, supplies `q=D/gcd(C_h,D)`.
2. Repeated residue classes disprove disjointness of the full sets.
   They do not disprove a choice of distinct representatives. The q5
   control admits such a choice, recorded explicitly in the note.

The rationally rescaled q5 example retains denominator 5. Its first
cleared gap 96/5 is not an integer. It rejects dropping the integer
constraints, without being a purported integer q1 cycle. Pairwise
examples at arbitrarily large B only satisfy the relaxed pair test;
they are not claimed to be complete cycles.

The candidate `B<=q-1` is open. No new denominator exclusion, novelty,
human peer review or formal verification is claimed. The all-period
ordered q1 recommendation does not replace or complete the active
all-cycle objective.

## Finite verification

- Author census write and full replay: PASS, reported at frozen script
  hash `516ea313c3f2829eef6546a84210234ec85c2ceb79f35cc147e1364d0248f22f`.
- Separate root full census replay: PASS at the same hash. It repeats
  all 8,800,033 requested seeds, retaining exact arrows and unresolved
  behavior at caps. No capped or unprocessed seeds occurred.
- The frozen census receipt hash is
  `b35a18cb4209b5d0afd104f5c9e38926dc2de5dbef890cc324cf05ae83ce4ceb`.
- The independent arithmetic implementation checks all 1,185 normalized
  cycles, 28,830 modular arrows, both residue and rational-rescaling
  examples, and 99 relaxed pair examples. Its write and replay pass;
  [arithmetic_obstructions.json](arithmetic_obstructions.json) pins the
  precise sources and scope.
- The required historical gate `python3 scripts/verify_all.py --cpp
  --transfer-controls` completed with exit 0 and all 119 report fields
  checked. Its C++ checks cover 4096 and 262144; all eleven raw transfer
  fixtures are retained. [historical_gate.json](historical_gate.json)
  saves the full finite receipt.
- The saved code in [RESIDUE_MATCHING.md](RESIDUE_MATCHING.md) was
  separately replayed: all 2,368 raw/normalized matching certificates
  pass. [residue_matching_replay.json](residue_matching_replay.json)
  records the source hash and explicit omission of q1. Missing height
  labels in 371 unordered cases are retained, rather than treated as
  observed vertices.

Preservation and local-link checks are recorded in
[delivery_checks.json](delivery_checks.json). The open LaTeX source and
historical mathematics are not edited. Reported side-lane Lean builds
remain distinct from this main-lane verification.
