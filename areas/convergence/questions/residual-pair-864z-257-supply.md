---
id: residual-pair-864z-257-supply
kind: question
title: Can the residual pair [864z - 257] - [z] of the coupled cell be closed at the original rank?
status: open
claim: >
  Odd-only 3x+1 map S, absorbing at 1. On the original coupled family z = 471104208005 + 2^14 3^16 ell, ell >= 0,
  with Q = (2^31 z - 665034679)/3^15, b = Q/3 and P(b) = div(I(Q,18) - I(b,16)) + [864z - 257] - [z] (R93),
  construct, for every ell, a finite exact current for the residual [864z - 257] - [z], or a terminating
  construction whose every signed premise has rank strictly below the original Q, covering the whole family; or
  prove that a stated class of such constructions cannot. The positive residual source 864z - 257 = 6v + 1 lies
  above Q and the negative one below it; R93 classifies the lower path's first departure for every upper return
  count. This was the final open obligation of the residual-progress line (frozen at R94); answering it for the
  whole family would supply P(b) on this cell only, not the universal premise universal-w5-tripling-currents.
created: 2026-10-18
tags: [convergence, outer-residual, retained-history, two-source, frontier]
---

# Can the residual pair [864z - 257] - [z] of the coupled cell be closed at the original rank?

## Question

Odd-only clock `S`, 1 absorbing; `I(x, t)` the current of the first `t` ordinary arrows from `x`. On the original coupled family of [`two-source-normalisation-first-departure`](../results/two-source-normalisation-first-departure/README.md) (R93),

    z = 471104208005 + 2^14·3^16·ℓ,   v = 144z − 43,   Q = (2^31·z − 665034679)/3^15,   b = Q/3,

the two actual original paths give exactly

    P(b) = div(I(Q, 18) − I(b, 16)) + [864z − 257] − [z],   864z − 257 = 6v + 1 > Q > z.

**Target.** For every `ℓ ≥ 0`, supply a finite exact current for the residual `[864z − 257] − [z]`, or give a construction on the whole family that terminates (a closed domain with a well-founded parameter and a complete base) and whose every signed premise, negative ones included, has rank strictly below the **original** `Q`. Alternatively, prove that a stated class of such constructions cannot work on a complete subfamily.

## Why it matters

This is where the legacy residual-progress line stopped (frozen at R94; see [`packet-current-supply`](packet-current-supply.md)). Every earlier round on this family reduced the pair `P(b)` to this residual or to a single higher W5 request, without supplying it. A positive answer would close `P(b)` on one whole remaining cell; it would not by itself give the Collatz-equivalent premise [`universal-w5-tripling-currents`](universal-w5-tripling-currents.md), since other types remain, and unconditional absorption of a whole exit cell would already imply Collatz ([`binary-return-exit-control`](../results/binary-return-exit-control/README.md), section on the ancestor cover).

## Known progress

- **The upper source.** Its guarded return `Ψ(z) = (3^12·z − 53)/2^19` re-enters exactly when `v2(7153z − 53) ≥ 33`; the countdown proves exit from that subsystem only, and the fresh forward continuation creates no negative high request ([`binary-return-exit-control`](../results/binary-return-exit-control/README.md), R90). The return leaves the explicit defect `[Ψ(z)] − [z]` (R93).
- **The lower source.** It follows a 448-state rational shadow while its cost stays below `n = v2(7153z − 53)`; its first departure is classified exactly, and it stays below `Q` through the departure and eleven more arrows (R93). No high negative frontier has appeared in that window.
- **No smaller history at the repeated target** through `12r + 19` quotient steps: [`rational-basin-precision-barrier`](../results/rational-basin-precision-barrier/README.md) (R91, computer-assisted) and [`fourteen-step-window-original-source`](../results/fourteen-step-window-original-source/README.md) (R92, computer-assisted).
- **Named procedures that fail:** the bounded-clock ternary child ([`prescribed-ternary-child-unbounded-clocks`](../results/prescribed-ternary-child-unbounded-clocks/README.md), R94); the one-ray/point inverse procedure at later exits ([`two-ray-point-procedure-later-target`](../attempts/two-ray-point-procedure-later-target/README.md)); retained-history W9 repair leaves one high W5 input with an exact undo on the canonical-Z branch ([`retained-history-w9-reduction`](../results/retained-history-w9-reduction/README.md), R89); one fixed word gives no smaller origin on the whole R88 cell ([`four-target-history-classification`](../results/four-target-history-classification/README.md)).
- **A candidate route:** a common-tail merger to a smaller original-cell child, [`common-tail-comparison-after-r92`](common-tail-comparison-after-r92.md).

## Suggested attacks

- The legacy line's own next step: a comparison after the complete departure interface of R93 that supplies the positive residual with a proved original-rank decrease, using an explicit well-founded parameter or supplied lower inputs. Any absorption or pair current beyond the displayed actual paths must be stated and supplied.
- Later common targets of the two sources, or genuinely different retained signed histories, with input-dependent (unbounded) clocks; R91, R92 and R94 rule out searching the excluded window and bounded-clock children.
- Any argument must use arithmetic that fails for the `3x+d` controls of `conventions/NOTATION.md` §3, as the negative controls of [`locally-collatz-like-control-barrier`](../results/locally-collatz-like-control-barrier/README.md) require. Speculation: a progress measure across successive exits that survives both the upper countdown and the lower departure has not been proposed.

## History

- New question at the B13 migration (Claude, Opus 5.5), from the final obligation stated in `experiments/residual_progress/two_source_history/TWO_SOURCE_HISTORY.md` (R93, now [`two-source-normalisation-first-departure`](../results/two-source-normalisation-first-departure/README.md)) and the legacy line's frozen state (archive/convergence-residual-progress/README.md and REPORT.md, at commit `be73a66`).
