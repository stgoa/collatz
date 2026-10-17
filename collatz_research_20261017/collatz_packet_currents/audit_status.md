# Audit status

## General proofs included

- Exact-source packet decomposition for every N and 1<=d<=ceil(log2 N)/2.
- Improved universal remainder and target-window reduction error.
- Common-tail lag formula, including a possibly infinite remaining hitting time.
- Finite current identity and all-horizon upper/lower bounds.
- Exit-profile refinement, with an explicitly checked acyclic current support.

These are candidate written proofs, not kernel-checked formalizations. No independent human review or publication-priority assessment has been completed.

## Finite results versus uniform claims

The remainder theorem is uniform in N. The current certificates apply only to the fourteen named source cutoffs; complete stored tables are supplied for two of them. No extrapolation of their O(N)-sized observed costs is made. The input-to-current search aborts on a path-cap exceedance or an unhandled cycle; success for arbitrary inputs is not assumed.

## Certificate verification versus discovery

Discovery followed a finite union of trajectories to a small core and then combined signed contributions. Verification is different: it checks only the finite equation (I-P)J=Pi_hat and the directed graph inside the support of J. It does not continue any of the exits into an unresolved future.

## Independent algorithm

Python builds the packets by exact cylinder inversion and groups their lift parameters. C++ builds them by directly iterating every original source and grouping its observed word. C++ independently checks the current divergence and computes exit profiles by direct finite path following instead of Python's memoized labels. Their outputs agree on the stored complete instances and the resulting target-window bounds.

The implementations have the same assistant author. This is algorithmic cross-checking, not independent mathematical authorship.

## Prior artifact audit

The uploaded packet ZIP was extracted and its certificate rerun unchanged; its assertions passed. The source hash and output are stored in audit/. No analytic gamma-decay result or the rest of the historical corpus is newly certified here.

## External background

Finite parity cylinders are classical (Bernstein--Lagarias). The current method is an elementary coboundary calculation. Tao's transport discussion is relevant context but no theorem from it is used. No Rhin estimate, mixing theorem, conjectural stochastic model, or global convergence hypothesis is a dependency of the new proofs.
