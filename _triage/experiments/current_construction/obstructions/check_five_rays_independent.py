"""Independent finite arithmetic audit of the five-ray conditional theorem."""

import json

MANTISSAS = (12, 14, 16, 18, 21)


def step(x):
    value = 3 * x + 1
    return value // (value & -value)


def main():
    times = {}
    for source in range(1, 96, 2):
        x, seen = source, set()
        for depth in range(1001):
            if x == 1:
                times[source] = depth
                break
            assert depth < 1000 and x not in seen, (source, depth, x)
            seen.add(x)
            x = step(x)
    transitions = []
    for i, m in enumerate(MANTISSAS):
        j, carry = (i + 3) % 5, (i + 3) // 5
        target_mantissa = MANTISSAS[j] * 2**carry
        assert 2 * target_mantissa >= 3 * m
        assert 5 * carry + j - i == 3
        assert (2 * target_mantissa == 3 * m) == (i < 3)
        transitions.append(dict(source=m, target=target_mantissa,
                                target_index=j, dyadic_carry=carry))
        for b in range(3, 9):
            N = m * 2**b
            target = MANTISSAS[j] * 2**(b + carry)
            assert N % 8 == 0
            assert (N - 1) // 4 == N // 4 - 1
            assert (3 * N + 1) // 2 == 3 * N // 2 <= target
            assert (3 * N + 1) // 4 == 3 * N // 4 <= target // 2
            for mantissa, exponent in ((m, b - 2), (MANTISSAS[j], b + carry - 1)):
                value = mantissa * 2**exponent
                assert (exponent >= 3) == (value >= 96)
                if value < 96:
                    assert all(x in times for x in range(1, value + 1, 2))
    assert 2**10 > 10**3
    assert 2**5 > 3**3
    assert 9 + 80 == 89 < 90
    print(json.dumps(dict(status="PASS", mantissas=MANTISSAS,
                         exponents="all b>=3 in the conditional theorem",
                         finite_base_odd_seeds=[1, 95],
                         finite_base_maximum_hitting_time=max(times.values()),
                         transitions=transitions,
                         contraction_upper="89/90 (strict)",
                         universal_current_existence_proved=False), indent=2))


if __name__ == "__main__":
    main()
