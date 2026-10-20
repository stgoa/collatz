# What the nonzero lower relation in the immediate self-loop supplies

**Status: written scope classification and finite exact audit.** This identifies
all lower relations left by the immediate blocked-W9/E composition in R75.
Its nonzero cases give already decreasing W9 comparisons. It supplies no new
accepted domain and does not concern arbitrary longer loops or other currents.

Use the notation and exact currents of the
[critical-basis compiler](../critical_basis/CRITICAL_BASIS.md). Write the
original critical formal absorption plans as

    [x] = div H_x + sum A_x(v) P(v).

All missing pair currents remain premises. This note preserves the nonzero
counterexample in R75; it does not reinstate the refuted universal-zero claim.

## 1. The full immediate-loop identity

Let u belong to E_return, and set

    b = (4u-3)/9, y = u/3 = (3b+1)/4, s = S(y).

Thus y=7 modulo 24, 9y is selected, and b is the blocked W9 input.
The sum K of its local R40 current and the R75 returning conversion is
exactly, row for row,

    K = H_y - delta_y - H_s,
    requests = {b:+1} + A_y - A_s.                    (1)

To prove this, the local upper prefix is the same path 3b→rho(u) as the
returning conversion, with opposite sign. The formal plan at rho(u) is
`-N_(3u)+H_u` with requests `{u:+1}+A_u`; these terms cancel as well.
The local lower path is b→y→s. Since b is canonical and 1 modulo 8,
its formal plan begins `H_b=delta_b+H_y`. This proves (1), including the
signed rows, rather than just the divergence. In particular

    div K = -sum (A_y-A_s)(v) P(v).                  (2)

## 2. Complete zero/nonzero classification

**Theorem.** Both K and A_y−A_s vanish unless

    u = 453 mod 576.

On that entire progression put

    v = (u-3)/18 = 25 mod 32, z = (9v+1)/2.

Then b=8v+1, y=6v+1, and

    K = H_v - delta_(3v) - H_z,
    A_y-A_s = {v:+1}+A_v-A_z.                        (3)

The unique largest critical rank in this vector is rho(v)=3v, with
coefficient +1. All other requests have rank strictly below 3v.

**Proof.** Put a=v2(y+1)>=3. If y is canonical, s is canonical and 2
modulo 3, and its formal inverse step returns y. Therefore
`H_s=-delta_y+H_y`, with identical request vectors, proving zero in (1).

If y is selected, put c=(y-1)/2. Then c is canonical, s is selected, and
`nu(s)=S(c)`. The explicit selected-prefix currents satisfy
`N_y=delta_y-delta_c+N_s`: remove their first arrow on each side and the
remaining prefixes agree. Consequently (1) becomes

    K = H_c - delta_c - H_(S(c)),
    A_y-A_s = A_c-A_(S(c)).                           (4)

The condition that 9y is selected excludes a=4. For a>=5, S(c) is again
canonical and 2 modulo 3; its formal inverse step returns c, so (4) is
zero. For a=3 write y=8t-1. Selection of y requires t=3 modulo 4;
selection of 9y sharpens this to t=3 modulo 8. The condition y=7 modulo
24 also gives t=1 modulo 3. Thus t=19 modulo 24, equivalently
u=3y=453 modulo 576. Now c=3v with v=25 modulo 32, and S(c)=z.
The critical formal step at c requests P(v) and then H_v, which gives (3).

Finally A_v has rank at most v. The number z is 1 modulo 8, so its first
ordinary successor x is at most (27v+5)/8. If v2(3z+1)>=3, then x<3v.
Otherwise x=(27v+5)/8 is 1 modulo 4. If x=5 modulo 8 it normalizes below
x/4; if x=1 modulo 8 its next ordinary step is at most
(81v+23)/32<3v. These compulsory initial steps have no critical requests.
Thus every A_z request has rank below 3v. It cannot cancel the coefficient
+1 at v, so the vector and its nonzero divergence are genuinely nonzero.
The pair sources are linearly independent on finite critical supports:
the atom at the largest upper endpoint 3w has no larger index to cancel it.
This also proves K is nonzero. ∎

## 3. What orienting the relation accomplishes

Equation (3) gives the valid conditional comparison

    P(v) = div(delta_(3v)+H_z-H_v) + sum(A_z-A_v) P.  (5)

This is precisely the single ordinary arrow 3v→z, followed by the existing
formal plans. Every v=25 modulo 32 already has v2(9v−1)>=5, so it is in the
accepted local W9 domain of R75. No new pair coverage follows from (5).
The source of the b=201,u=453 counterexample is v=25, and its lower vector
is `{25:+1,5:+1}`. The original parent b still has coefficient +1 in (1).

This settles the immediate-loop simplification only. Longer comparisons,
alternative source representations and useful signed cancellations remain
outside the classification.

## 4. Reproduction

Run `python3 experiments/residual_progress/lower_loop_scope/check_lower_loop.py`.
The default replay verifies the stored receipt; `--write-receipt` refreshes
it intentionally. Checks include the full rows of (1) and (3), independent
one-arrow divergences, progression boundaries, all stated zero cases,
large exact inputs, already accepted W9 targets, and rejection controls.
Finite checks support the implementation; the universal classification
rests on the proof above. No absorption search is used.
