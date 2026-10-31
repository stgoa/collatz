# Review of first-shell-three-state-rigidity

## What I checked

- The statement and the proof in [`ROOT_REVIEW.md`](../two-exit-interior-counterexample/ROOT_REVIEW.md) sections 2-4, re-derived in full: the six radix identities, the setup, the universal relations (1), all seven rows of the table with every choice of `t`, and the constant-output finish (derivations below).
- An independent mechanical check (own code, not committed): congruence closure over all operator words of length `<= 6` in `E_0, E_1, T_0, T_1, T_2` applied to `b` (19,531 terms), with the three identities imposed at `b` only (`T_0 b = E_0 E_0 b`, `T_2 b = E_1 b`, `E_1 E_0 b = b`), the radix identities at every term, and, for each of the 27 assignments `(p, q, t)` in `{b, u, v}^3` (`v` the third state), the induced equalities. In all 27 cases the `E`-closure of the class of `b` is a complete family of at most 4 classes whose outputs at zero are among `b(0), b(1), b(2)`, so `b` is constant. With no first-shell hypothesis the `E`-closure has 728 classes within the universe and is incomplete, so the check is not vacuous. Word length 7 gives the same results for the rows discussed in Finding 1.
- The dependency as used: the reverse direction of Lean `LeanLane.Scalar.scalar_interface_iff` in [`scalar-interface-three-identities`](../scalar-interface-three-identities.md) is exactly "the odd-value sequence of an invariant colouring satisfies the three identities", and `colouring_oddPart` gives `h(n) = h(oddpart n)`, so constant `b` means constant `h` on the positive integers.
- Certificates: none listed; nothing to run.
- Controls, own code: for `b_d(n) = c_d(2n+1)`, with `c_5` and `c_13` the "which cycle" colourings of `3x+5` and `3x+13`, the identities fail (`b(3n) = b(4n)` first at `n = 1` and `n = 2`; `b(3n+2) = b(2n+1)` at `n = 0` and `n = 4`; `b(4n+2) = b(n)` at `n = 0` and `n = 1`) and the six first-shell sequences are pairwise distinct on 400-term prefixes, so `|J_1(b_d)| = 6`; for the periodic invariants `1_{5|n}` and `1_{13|n}` the identities fail too and 5 of the six are distinct. These genuine nonconstant `3x+d` invariants fail the hypotheses, as the Remarks say; the theorem excludes none of them.
- Links, `evidence` paths and frontmatter after converting the node to a folder.

Key derivations. `T_j E_i b(n) = b(6n + 2j + i)` and `E_l T_k b(n) = b(6n + 3l + k)`, which gives R0-R5. The identities read `T_0 b = E_0 u`, `T_2 b = E_1 b = p` and `E_1 u = b`, with `u = E_0 b`. If `u = b`, both children of `b` equal `b`, so `b(n) = b(floor(n/2))` and `b` is constant. Otherwise R0-R5 at `b` give (1): `(T_0 u, T_1 u, T_2 u) = (E_0 q, E_0 p, E_1 t)` and `(T_0 p, T_1 p, T_2 p) = (E_0 t, E_1 q, E_1 p)`. If `p, q` lie in `{b, u}`, that family is `E`-closed and `u(0) = b(0)`. The five remaining pairs `(p, q)` and their values of `t` go as in section 3; I confirm each displayed child and each exclusion (3.3 with `t = b` forces `u = v`; 3.4 with `t = b` forces `u = v`; 3.5 with `t = b` forces `u = b` and with `t = v` forces `v = b`). Finish: the second and third identities at `n = 0` give `b(2) = b(1)` and `b(2) = b(0)`; reading the bits of `n` least significant first inside an `E`-closed family `F` gives `b(n) = x(0)` for some `x` in `F`, and every `x` in `{b, u, v, w}` has `x(0)` in `{b(0), b(1), b(2)}`.

## What I did not check

- Nothing numerical about `3x+1` itself: no nonconstant `3x+1` invariant is available, so the theorem can only be checked as a derivation, which was done twice (by hand and by the closure engine).
- The two main-lane audits were read for context only.

## Findings

1. Imprecision (`ROOT_REVIEW.md` section 3, "Corrected surviving table", echoed by the Remarks' "seven surviving rows"): four of the seven rows are themselves inconsistent with the distinctness of `b, u, v`, each by one more radix identity, exactly as the removed draft row was.
   - `(p, q, t) = (v, b, b)`: R1 at `p`, `T_0 E_1 p = E_0 T_1 p`; here `E_1 p = v = p`, `T_0 p = E_0 t = u`, `T_1 p = E_1 q = p` and `E_0 p = b` (the row's `A = b`); so `u = b`.
   - `(v, v, u)`: R1 at `v`, `T_0 E_1 v = E_0 T_1 v`, with `E_1 v = u`, `T_0 u = E_0 q = A`, `T_1 v = E_1 q = u`, `E_0 u = v`, gives `A = v`; then R2 at `v`, `T_1 E_0 v = E_0 T_2 v`, gives `u = T_1 v = E_0 T_2 v = E_0 u = v`.
   - `(b, v, v)`: R5 at `u`, `T_2 E_1 u = E_1 T_2 u`; `E_1 u = b`, `T_2 b = b`, `T_2 u = E_1 t = E_1 v = v`, `E_1 v = v`; so `b = v`.
   - `(u, v, u)`: R3 at `u`, `T_1 E_1 u = E_1 T_0 u`; `E_1 u = b`, `T_1 b = u`, `T_0 u = E_0 q = E_0 v = v`, `E_1 v = v`; so `u = v`.
   The closure engine confirms these collapses (every class merges) and finds no such collapse for `(v, u, b)`, `(v, v, v)` and `(b, v, u)` at word length `<= 7`. The theorem is unaffected: an inconsistent row is vacuous and the children displayed for it remain valid consequences. Only the word "surviving" overstates what the table shows; by the theorem itself every row with a third state is vacuous, since a sequence realising it would be constant.
2. Imprecision (README, Proof): "`q` the remaining first-shell state" names neither `q = T_0 b = E_0 u` nor `t = T_1 b`; the split is over `(p, q)` and then over `t` in `{b, u, v}`, as `ROOT_REVIEW.md` has it. The sentence is a summary; the proof it points to is complete.
3. Structure, not mathematics: the written proof lives in another node's folder (`two-exit-interior-counterexample/ROOT_REVIEW.md`), against the one-folder rule of `AGENTS.md` section 3; the migration recorded the choice in History. A copy or move would make this node self-contained.
4. Scope confirmed: no finite output alphabet, no Cobham, and `|J_1(b)| <= 3` is a condition on entire sequences. The claim's "Hence" clause needs `h` nonconstant on the positive integers, which gives `b` nonconstant through `h(n) = h(oddpart n)`.

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
