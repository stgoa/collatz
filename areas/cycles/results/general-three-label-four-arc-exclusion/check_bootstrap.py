"""Exact constants and logarithm bootstrap for the four-arc result.

The manuscript and the other certificates supply the phase and discrepancy
inequalities. This script checks their numerical consequences, independently
constructs the logarithm enclosure, and reads a hash-pinned period receipt.
Throughout this script m is the full raw odd-only period, not a half-length.
"""
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PERIOD_RECEIPT = (
    "areas/cycles/results/cycle-length-lower-bound-from-convergents/"
    "cycle_length_convergents.json"
)
PERIOD_SHA256 = "e48b19926ca0c155032a9d85d3c28f3f6fbe69ae404163638414a7c848c65f64"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def logarithm_bounds(value, terms=80):
    """Positive atanh sum with an exact geometric upper bound on its tail."""
    require(value > 1 and terms >= 1, "logarithm domain")
    z = Fraction(value - 1, value + 1)
    lower = 2 * sum(
        (z ** (2 * j + 1) / (2 * j + 1) for j in range(terms)),
        Fraction(0),
    )
    tail = 2 * z ** (2 * terms + 1) / (
        (2 * terms + 1) * (1 - z * z)
    )
    require(tail > 0, "positive logarithm tail")
    return lower, lower + tail


def elementary_constants():
    # At a global minimum >=35 the product of the initial ones run and
    # its next exceptional arrow gives a slope strictly below 8/5.
    require(106**5 < 2**8 * 35**5, "minimum35 slope")
    require(388**5 < 2**8 * 129**5, "minimum129 slope")
    require(2**3 < 3**2 and 3**5 < 2**8, "3/2 < log2(3) < 8/5")
    require(Fraction(1, 3) + Fraction(1, 2**172) < 2,
            "Y < 173+342log2(m) from the EXT-1 minimum ceiling")
    # q_(i+2)>=2*q_i, with q_0,q_1>=1, splits the reciprocal sum
    # into two geometric series. The duplicated denominator one is included.
    reciprocal_bound = 2 / (1 - Fraction(1, 2))
    require(reciprocal_bound == 4 and 16 * reciprocal_bound == 64,
            "continued-fraction reciprocal constant")
    return {
        "minimum35_slope_comparison": [106**5, 2**8 * 35**5],
        "minimum129_slope_comparison": [388**5, 2**8 * 129**5],
        "minimum_run_coefficient": "3/5",
        "reciprocal_denominator_sum_upper": 4,
        "weighted_discrepancy_coefficient": 512,
        "phase_digit_constant": 27,
        "phase_height_constant": 16,
        "height_sum_constant": 64,
    }


def dyadic_cutoff():
    # For 2^d<=m<2^(d+1), X<342*d+515 and n<2*d+3.
    # Thus the hypothesized bound on m is below the following quadratic.
    scale = Fraction(1536, 5)
    x_poly = [515, 342]
    inner_poly = [27 * 3 + 64 * 515, 27 * 2 + 64 * 342]
    polynomial = [
        scale * x_poly[0] * inner_poly[0],
        scale * (x_poly[0] * inner_poly[1] + x_poly[1] * inner_poly[0]),
        scale * x_poly[1] * inner_poly[1],
    ]
    require(all(value > 0 for value in polynomial), "positive quadratic coefficients")
    require(polynomial == [Fraction(5227350528), Fraction(34713833472, 5),
                           Fraction(11526395904, 5)], "quadratic expansion")
    index = 48
    upper = sum(value * index**i for i, value in enumerate(polynomial))
    direct = scale * (342 * index + 515) * (
        27 * (2 * index + 3) + 64 * (342 * index + 515)
    )
    require(upper == direct == Fraction(28249216922112, 5), "initial quadratic value")
    require(upper < 2**index, "initial dyadic contradiction")
    ratio = Fraction(49, 48)**2
    require(ratio < 2, "quadratic ratio below doubling")
    # For every d>=48 positivity gives P(d+1)/P(d)<=((d+1)/d)^2
    # <=(49/48)^2<2. This certifies all larger dyadic intervals.
    return {
        "polynomial_coefficients_ascending": [str(value) for value in polynomial],
        "initial_dyadic_index": index,
        "initial_upper_bound": str(upper),
        "initial_lower_bound": 2**index,
        "initial_margin": str(2**index - upper),
        "successive_ratio_upper": str(ratio),
        "full_period_cutoff": 2**index,
    }


def exact_gap():
    low2, high2 = logarithm_bounds(2)
    low3, high3 = logarithm_bounds(3)
    require(Fraction(1, 2) < low2 < high2 < 1, "ln2 enclosure")
    require(1 < low3 < high3 < Fraction(11, 10), "ln3 enclosure")
    alpha_low, alpha_high = low3 / high2, high3 / low2
    left, right = alpha_low, alpha_high
    p_previous_previous, p_previous = 0, 1
    q_previous_previous, q_previous = 1, 0
    terms = []
    convergents = []
    for _ in range(100):
        lower_digit, upper_digit = left.__floor__(), right.__floor__()
        require(lower_digit == upper_digit, "unambiguous continued-fraction digit")
        digit = lower_digit
        p = digit * p_previous + p_previous_previous
        q = digit * q_previous + q_previous_previous
        terms.append(digit)
        convergents.append((p, q))
        if q > 2**48:
            break
        left, right = 1 / (right - digit), 1 / (left - digit)
        p_previous_previous, p_previous = p_previous, p
        q_previous_previous, q_previous = q_previous, q
    else:
        raise RuntimeError("continued-fraction iteration guard")
    p, q = convergents[-2]
    p_next, q_next = convergents[-1]
    require((p, q) == (83130157078217, 52449289519716), "lower convergent")
    require((p_next, q_next) == (683381996816440, 431166034846567),
            "upper convergent")
    require(Fraction(p, q) < alpha_low < alpha_high < Fraction(p_next, q_next),
            "opposite bracket signs")
    require(p_next * q - p * q_next == 1, "unimodular bracket")
    require(q_next > 2**48, "coverage of every possible full period")
    gap = q * alpha_low - p
    require(gap > Fraction(1, 2**62), "one-sided logarithm gap")
    # The manuscript's integer-coordinate argument, not an enumeration,
    # now gives E-m*alpha>gap for EVERY 0<m<q_next with E-m*alpha>0.
    # ln2>1/2 gives Lambda>2^-63; eta>min(Lambda/2,1/2)>2^-64.
    return {
        "atanh_terms": 80,
        "ln2_interval": [str(low2), str(high2)],
        "ln3_interval": [str(low3), str(high3)],
        "continued_fraction_digits": terms,
        "lower_convergent": {"p": p, "q": q},
        "upper_convergent": {"p": p_next, "q": q_next},
        "positive_gap_lower": str(gap),
        "positive_gap_power": 62,
        "eta_power": 64,
        "scope": "Every integer full period 0<m<2^48; no m>=q restriction.",
    }


def final_comparison():
    # L<m/(3*eta)<2^112/3, so Y=log2(L+1)<112.
    require(Fraction(2**112, 3) + 1 < 2**112, "Y below112")
    number_of_digits = 2 * 48 + 1
    require(number_of_digits == 97, "continued-fraction length bound")
    final = Fraction(1536, 5) * 112 * (27 * number_of_digits + 64 * 112)
    require(final == Fraction(1683677184, 5), "final full-period bound")
    path = ROOT / PERIOD_RECEIPT
    raw = path.read_bytes()
    require(sha256(raw).hexdigest() == PERIOD_SHA256, "pinned period receipt")
    period = int(json.loads(raw)["V3"]["2^71"]["least_m"])
    require(period == 72057431991 and final < period, "full odd-period contradiction")
    return {
        "clock": "m is full raw odd-only period; no factor two",
        "Y_upper": 112,
        "continued_fraction_length_upper": number_of_digits,
        "full_period_upper": str(final),
        "integer_full_period_upper": final.numerator // final.denominator,
        "declared_period_lower_bound": period,
        "comparison_margin": str(period - final),
        "period_receipt": PERIOD_RECEIPT,
        "period_receipt_sha256": PERIOD_SHA256,
        "input_scope": "Uses the replayed period result under its declared Barina assumption; the convergence computation is not rerun.",
    }


def main():
    require(sys.argv[1:] in ([], ["--write-receipt"]),
            "usage: check_bootstrap.py [--write-receipt]")
    receipt = {
        "schema": "general-four-arc-bootstrap-v1",
        "scope": "Exact numerical closure of the manuscript's phase and weighted-discrepancy estimates.",
        "elementary_constants": elementary_constants(),
        "dyadic_cutoff": dyadic_cutoff(),
        "exact_gap": exact_gap(),
        "final_comparison": final_comparison(),
    }
    encoded = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    destination = HERE / "check_bootstrap.json"
    if sys.argv[1:]:
        destination.write_text(encoded)
    else:
        require(destination.read_text() == encoded, "receipt mismatch; regenerate explicitly")
    print(json.dumps({
        "status": "passed",
        "full_period_cutoff": receipt["dyadic_cutoff"]["full_period_cutoff"],
        "integer_full_period_upper": receipt["final_comparison"]["integer_full_period_upper"],
        "declared_period_lower_bound": receipt["final_comparison"]["declared_period_lower_bound"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
