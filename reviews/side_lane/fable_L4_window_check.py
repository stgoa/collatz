"""Sidekick probe: independent recomputation of the L4 part-1 window certificate on claude/explicit-tao
(lemmas/L4_tao_architecture.md, e89ce02): Tao v7 (5.9) window I_y = [ (a-1)L/log(4/3) + L^0.8,
(a^2-1)L/log(4/3) - L^0.8 ] with L = log x, y = x^a; nonempty iff L > (2 log(4/3)/(a(a-1)))^5; m0 = floor((a-1)L/100).
Uses mpmath-free high-precision decimal arithmetic. Run without -O.
"""
from decimal import Decimal as D, getcontext
from pathlib import Path
import json

getcontext().prec = 50
HERE = Path(__file__).resolve().parent


def ln(x):
    return D(x).ln()


def main():
    a = D("1.001")
    l43 = ln(D(4)/D(3))
    thr = (2*l43/(a*(a - 1)))**5
    # bracket: empty just below, nonempty just above
    def width(L):
        return a*(a - 1)*L/l43 - 2*(L.ln()*D("0.8")).exp()
    assert width(thr*D("0.999")) < 0 < width(thr*D("1.001"))
    L68 = 68*ln(2)
    p = lambda e: (L68.ln()*D(e)).exp()
    lo = (a - 1)*L68/l43 + p("0.8")
    hi = (a*a - 1)*L68/l43 - p("0.8")
    # alpha needed at x = 2^68: a(a-1) = 2 log(4/3) / L^0.2
    k = 2*l43/p("0.2")
    a_need = (1 + (1 + 4*k).sqrt())/2
    out = {"probe": "fable_L4_window_check", "branch": "claude/explicit-tao e89ce02",
           "threshold_logx": f"{thr:.4E}", "threshold_log2x": f"{thr/ln(2):.4E}",
           "m0_ge_1_needs_logx_ge": str((100/(a - 1)).normalize()),
           "at_2^68": {"logx": f"{L68:.4f}", "I_y": [f"{lo:.2f}", f"{hi:.2f}"],
                       "log^0.6/0.7/0.8": [f"{p('0.6'):.2f}", f"{p('0.7'):.2f}", f"{p('0.8'):.2f}"],
                       "steps_between_scales": f"{(a - 1)*L68/l43:.3f}", "n0": f"{D('0.1')*68:.1f}",
                       "alpha_for_nonempty_window": f"{a_need:.4f}"},
           "result": "PASS"}
    (HERE / "fable_L4_window_check.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
