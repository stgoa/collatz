# Results

## General finite proof

The packet reduction can be rebuilt from exact source cylinders. Every three consecutive lifts of one valuation word have zero total source coefficient and map to a ternary-spaced triple. The new remainder is

    6 binom(b,d) + 2 sum_{j<d} binom(b,j),

rather than the earlier homogeneous-profile/fringe bound. At d=floor(2b/9), its norm is <=16 N^(7/9); the entire target-window remainder still costs o(N). The hatted packet family is a new grouping, not literally the old homogeneous-cell family.

## New cancellation mechanism

Finite paths to a common state cancel the unknown tail even when arrival times differ. The old packet (-1,-1,2) at (6929,6947,6965) reaches23 at times49,32,3. Its signed stopping work lies in [-75,0] at every horizon, without using the continuation after23.

## Current certificate

If a finite signed table J satisfies (I-P)J=mu, then

    H_L(mu)=sum_y J(y) 1_{tau(y)<=L}.

This is checked using one step per table row. Exit-level cumulative sums improve the resulting all-horizon bounds, while leaving exit continuations unresolved.

## What is only finite

At N=262144 the complete source-exact packet family has a stored, independently checked current giving

    -57661 <= H_L(Pi_hat_N) <= 63824 for EVERY L.

Combining its exact four-step residual with this current gives

    -34504 <= E_T(262144) <= 37090 for every 0<=T<=231.

These statements hold at a named finite source cutoff. They do not establish uniform O(N) current cost. Fourteen source cutoffs were tested; two complete current tables are included.

## Remaining problem

Find a source-arithmetic construction or bound for the one-sided current/exit-profile cost that is uniform in N. The present constructor discovers tables by following finite trajectories; its success and cost cannot be extrapolated. No Collatz proof, new convergence-verification record, Lean verification, independent human review, or novelty claim is made.
