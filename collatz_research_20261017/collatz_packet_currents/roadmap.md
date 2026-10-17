# Roadmap after source-exact packets and current certificates

## New general proof units

1. The packet family can be constructed directly from exact positive source cylinders. Retain triples of consecutive lifts separately in the two source components. The only remainder is over-budget sources plus at most two ungrouped lifts per word/component. The bound is 6*binom(b,d)+2*sum_(j<d)binom(b,j).
2. A finite current identity mu=(I-P)J certifies the signed stopping work at EVERY future horizon using only one-step arrows. Opposite contributions may cancel at different elapsed times.
3. Exit-level prefix sums improve the simple positive-current bound. The continuations beyond those exits need not be resolved.

The time-shift and current identities are elementary coboundary/telescoping mathematics. They are not claimed as a new general theory.

## What has actually been checked for the full family

Finite current tables were constructed at fourteen named cutoffs. Two complete tables are supplied and verified independently. At N=2^18 the packet work is between -57661 and63824 at every horizon. This is a statement at one source size, not evidence sufficient for a uniform source-size bound.

The complete finite-source error is also bounded on the requested source-power window at the two supplied cutoffs, by combining the current with the exact anchor residual. The residual is not followed into the future.

## The active proof obligation

Produce an ARITHMETIC construction or uniform estimate for currents representing the exact-source packet family. A sufficient form is

    Pi_hat_N = (I-P)J_N + zeta_N,
    exit-profile positive cost(J_N) = O(N),
    ||zeta_N^+|| = O(N^(4/5)/log N).

The negative residual can be discarded for the one-sided upper estimate. Exact complete currents with O(N) cost would be stronger and sufficient. Neither bound is proved uniformly.

The challenge is not to discover a larger collection of finite currents by running all sample orbits to a small core. It is to derive their cost from the source-word arithmetic and the fixed interval cutoffs. A universal current-construction algorithm with no cost control would also be insufficient.

## Guardrails

- The hatted source-exact family differs from the uploaded homogeneous-cell family. Do not identify their individual packets.
- The remainder bound is uniform; the computed current-cost table is not.
- A current is signed arithmetic on arrows, not a probability distribution.
- Equal-time total-variation contraction is unnecessary for signed stopping work; do not charge the same unknown common tail repeatedly.
- Packet balance alone does not determine the sign: the supplied 55,73,91 example has nonnegative work, while the 6929,6947,6965 example has nonpositive work.
- No iid tail, no assumed convergence of an unexamined exit, and no deletion of source multiplicities.
- No claim that the new certificate method proves Collatz, the finite-window hypothesis, or a logarithmic mean hitting-time bound.

## Verification priority

The short source-packet lemma and current/exit-profile identities are suitable for a fresh human or proof-assistant audit. They require none of the earlier joint-mixing extension, Rhin, or mechanical-word results. Keep the inverse-Syracuse/PCP manuscript independent.
