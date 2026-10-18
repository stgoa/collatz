#!/usr/bin/env python3
"""Replay named Phase 6 obligation controls; this is setup, not a Collatz proof.

Only positive odd d coprime to 6 and positive odd states are supported.
The dynamics uses one odd-only arrow per step and absorbs at 1, except where
raw cycles are explicitly checked. A cap produces UNRESOLVED, never success.
Run normally to reproduce the persisted receipt, or use --write-receipt PATH
to materialize it after all exact checks and rejection tests pass.
"""
import argparse
from copy import deepcopy
from dataclasses import dataclass
import hashlib
import json
from math import gcd
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
FIXTURE = HERE / "cycle_fixtures.json"
RECEIPT = HERE / "transfer_controls_audit.json"
SIDE_PIN = "f244b7a5b77a51f8dd7e6bccf2c6d5f18932df88"
EXPECTED_MINIMA = {5: (1, 19, 23, 187, 347), 7: (5,),
                   13: (1, 131, 211), 61: (1, 235)}
POSITIVE_SAMPLES = (1, 3, 5, 7, 9, 11, 15, 27, 31, 41, 63, 127, 255, 447)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def positive_integer(x, name):
    require(type(x) is int and x > 0, f"{name} must be a positive integer")


def domain(d, x):
    positive_integer(d, "d")
    positive_integer(x, "state")
    require(gcd(d, 6) == 1, "supported d must be coprime to 6")
    require(x % 2 == 1, "state must be odd")


def raw_step(d, x):
    domain(d, x)
    numerator = 3 * x + d
    return numerator // (numerator & -numerator)


def step(d, x):
    """The declared working map: absorb only at 1."""
    domain(d, x)
    return 1 if x == 1 else raw_step(d, x)


def valuation(d, x):
    domain(d, x)
    return ((3 * x + d) & -(3 * x + d)).bit_length() - 1


def check_cycle(record):
    require(type(record) is dict, "cycle record must be an object")
    require(set(record) == {"d", "minimum", "states", "valuations"},
            "unknown or missing cycle field")
    d, minimum, states = record["d"], record["minimum"], record["states"]
    domain(d, minimum)
    require(type(states) is list and bool(states), "empty cycle")
    for x in states:
        domain(d, x)
    require(len(set(states)) == len(states), "cycle repeats before its closure")
    require(states[0] == minimum == min(states), "cycle must start at its minimum")
    require(type(record["valuations"]) is list and
            all(type(a) is int and a >= 1 for a in record["valuations"]),
            "cycle valuations must be positive integers")
    require(record["valuations"] == [valuation(d, x) for x in states],
            "wrong exact valuation")
    for i, x in enumerate(states):
        require(raw_step(d, x) == states[(i + 1) % len(states)],
                f"incorrect raw cycle arrow at d={d}, x={x}")
    return {"d": d, "minimum": minimum, "length": len(states),
            "valuation_sum": sum(record["valuations"]),
            "contains_absorber_1": 1 in states,
            "primitive_relative_to_d": all(gcd(x, d) == 1 for x in states)}


def check_fixtures(data):
    require(type(data) is dict and set(data) == {"schema", "cycles"},
            "unknown or missing fixture field")
    require(data["schema"] == "phase6-cycles-v1", "unknown fixture schema")
    require(type(data["cycles"]) is list, "cycles must be a list")
    checked = [check_cycle(record) for record in data["cycles"]]
    actual = [(row["d"], row["minimum"]) for row in checked]
    expected = [(d, m) for d, minima in EXPECTED_MINIMA.items() for m in minima]
    require(actual == expected, "missing, duplicate, reordered or unknown cycle fixture")
    return checked


@dataclass(frozen=True)
class Mechanism:
    node: str
    failure_step: str
    obligation: str
    success: object


# These are exact baseline obligation tests, not putative solutions of the nodes.
# Register a proposed proof mechanism separately; do not relabel one of these
# observations as proof that the new mechanism is d=1-specific.
MECHANISMS = {
    "strict_descent": Mechanism(
        "S.2", "S.2.strict_orbit_descent",
        "Every odd start > 1 eventually has an odd iterate strictly below itself.",
        lambda start, x: x < start),
    "one_absorption": Mechanism(
        "C.2", "C.2.one_absorption",
        "The tested odd seed eventually reaches the sole absorber 1.",
        lambda start, x: x == 1),
    "nonprincipal_cycle_exclusion": Mechanism(
        "Y.2", "Y.2.nonprincipal_cycle_exclusion",
        "The tested orbit has no cycle disjoint from the sole absorber 1.",
        lambda start, x: x == 1),
}


def evaluate(name, d, start, max_steps=10000):
    """Return a bounded, exact observation of a registered d-parametric test.

    A repeated state certifies obstruction only after checking its whole cycle.
    Encountering 1 is a terminal baseline even for strict descent from start=1;
    that baseline is not a claim that an iterate is strictly below 1.
    """
    require(name in MECHANISMS, f"unknown mechanism: {name}")
    domain(d, start)
    require(type(max_steps) is int and max_steps >= 0, "invalid step cap")
    mechanism = MECHANISMS[name]
    seen, path, x = {}, [], start
    for elapsed in range(max_steps + 1):
        if x == 1 or mechanism.success(start, x):
            return {"status": "SUCCESS", "steps": elapsed, "endpoint": x,
                    "reason": "terminal baseline" if start == 1 else "witnessed obligation",
                    "path": path + [x]}
        if x in seen:
            cycle = path[seen[x]:]
            minimum = min(cycle)
            j = cycle.index(minimum)
            canonical = cycle[j:] + cycle[:j]
            check_cycle({"d": d, "minimum": minimum, "states": canonical,
                         "valuations": [valuation(d, y) for y in canonical]})
            require(1 not in cycle, "absorbed orbit unexpectedly contains a raw 1 cycle")
            return {"status": "OBSTRUCTED", "steps": elapsed, "endpoint": x,
                    "reason": mechanism.failure_step, "path": path + [x],
                    "cycle": canonical}
        if elapsed == max_steps:
            return {"status": "UNRESOLVED", "steps": elapsed, "endpoint": x,
                    "reason": "step cap", "path": path + [x]}
        seen[x] = len(path)
        path.append(x)
        x = step(d, x)
    raise RuntimeError("unreachable")


def demand_status(observation, expected, context):
    require(observation["status"] == expected,
            f"{context}: expected {expected}, got {observation['status']}")


def rejection_tests(data):
    """Check defects which would otherwise make a transfer control vacuous."""
    rejected = []

    def reject(label, action):
        try:
            action()
        except ValueError:
            rejected.append(label)
        else:
            raise ValueError(f"negative check was accepted: {label}")

    bad = deepcopy(data)
    bad["cycles"][1]["states"][1] += 2
    bad["cycles"][1]["valuations"] = [
        valuation(bad["cycles"][1]["d"], x) for x in bad["cycles"][1]["states"]]
    reject("corrupt cycle arrow", lambda: check_fixtures(bad))
    bad_valuation = deepcopy(data)
    bad_valuation["cycles"][1]["valuations"][0] += 1
    reject("wrong exact valuation", lambda: check_fixtures(bad_valuation))
    missing = deepcopy(data)
    missing["cycles"].pop()
    reject("missing cycle", lambda: check_fixtures(missing))
    duplicate = deepcopy(data)
    duplicate["cycles"].append(deepcopy(duplicate["cycles"][0]))
    reject("duplicate cycle", lambda: check_fixtures(duplicate))
    unknown = deepcopy(data)
    unknown["unexpected"] = True
    reject("unknown fixture field", lambda: check_fixtures(unknown))
    reject("unknown mechanism", lambda: evaluate("unregistered-proof", 1, 3))
    reject("unsupported d", lambda: evaluate("strict_descent", 3, 3))
    reject("even state", lambda: evaluate("strict_descent", 1, 4))
    reject("boolean state", lambda: evaluate("strict_descent", 1, True))
    for name in MECHANISMS:
        capped = evaluate(name, 1, 27, 0)
        demand_status(capped, "UNRESOLVED", name)
        reject(f"cap cannot pass {name}",
               lambda observation=capped: demand_status(observation, "SUCCESS", "cap"))
    # A short positive sample must not suppress genuine cycle obstructions.
    for name in MECHANISMS:
        obstructed = evaluate(name, 5, 19)
        reject(f"cycle cannot pass {name}",
               lambda observation=obstructed: demand_status(observation, "SUCCESS", "cycle"))
    return rejected


def audit(data, max_steps=10000):
    cycles = check_fixtures(data)
    rows = []
    for record in data["cycles"]:
        d, start = record["d"], record["minimum"]
        expected = "SUCCESS" if start == 1 else "OBSTRUCTED"
        observations = {name: evaluate(name, d, start, max_steps)
                        for name in MECHANISMS}
        for name, observation in observations.items():
            demand_status(observation, expected, f"d={d}, start={start}, {name}")
        rows.append({"d": d, "start": start, "expected": expected,
                     "role": "terminal baseline" if start == 1 else "negative cycle control",
                     "observations": observations})

    positive = []
    for start in POSITIVE_SAMPLES:
        observations = {name: evaluate(name, 1, start, max_steps) for name in MECHANISMS}
        for name, observation in observations.items():
            demand_status(observation, "SUCCESS", f"d=1, start={start}, {name}")
        positive.append({"d": 1, "start": start, "observations": observations})

    # These extra controls are not in the primitive side-lane cycle list.
    fixed_d = []
    for d in EXPECTED_MINIMA:
        require(step(d, d) == d, "d must be a fixed point distinct from 1")
        observations = {name: evaluate(name, d, d, max_steps) for name in MECHANISMS}
        for name, observation in observations.items():
            demand_status(observation, "OBSTRUCTED", f"fixed d={d}, {name}")
        # Exact scaling is the witness for the invariant set d*(positive odd).
        scaling = []
        for k in (1, 3, 5, 7, 27, 127):
            lhs, rhs = raw_step(d, d * k), d * raw_step(1, k)
            require(lhs == rhs and lhs % d == 0, "multiples-of-d scaling failed")
            scaling.append({"k": k, "image": lhs})
        fixed_d.append({"d": d, "observations": observations,
                        "scaling_samples": scaling,
                        "odd_multiples_up_to_20000": (20000 // d + 1) // 2})

    require(raw_step(7, 1) == 5 and step(7, 1) == 1,
            "raw and absorbed maps must remain distinct")
    # Legacy packet controls deliberately absorb at {1,d}; Phase 6 uses {1}.
    require(step(61, 61) == 61 and step(61, 1) == 1,
            "Phase 6 must not silently import the legacy second absorber")

    return {
        "schema": "phase6-transfer-audit-v1", "status": "PASS",
        "batch_label": "none", "confirmation": "pending side-lane review",
        "side_lane_proposal_commit": SIDE_PIN,
        "clock": "odd-only; absorbed at 1; raw map only for explicit cycle/scaling checks",
        "d_domain": "positive odd d coprime to 6",
        "max_steps": max_steps,
        "registered_mechanisms": {
            name: {"node": mechanism.node, "failure_step": mechanism.failure_step,
                   "obligation": mechanism.obligation,
                   "scope": "baseline obligation control; no candidate proof step supplied"}
            for name, mechanism in MECHANISMS.items()},
        "cycle_summary": cycles,
        "cycle_controls": rows,
        "d1_positive_samples": positive,
        "fixed_d_and_scaling_controls": fixed_d,
        "absorption_conventions": {"raw_T7_at_1": raw_step(7, 1),
                                   "absorbed_T7_at_1": step(7, 1),
                                   "absorbed_T61_at_61": step(61, 61),
                                   "legacy_packet_absorbers_at_d61": [1, 61]},
        "rejections": rejection_tests(data),
        "scope": ("Finite exact cycle and positive-sample controls, with the separately "
                  "written multiples-of-d invariant. No d=1 theorem, no quotient/rank "
                  "implementation, no density theorem and no exclusion of divergence."),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=FIXTURE)
    parser.add_argument("--max-steps", type=int, default=10000)
    parser.add_argument("--write-receipt", type=Path)
    args = parser.parse_args()
    require(not sys.flags.optimize, "run without -O")
    data = json.loads(args.fixture.read_text())
    result = audit(data, args.max_steps)
    result["fixture_sha256"] = hashlib.sha256(args.fixture.read_bytes()).hexdigest()
    text = json.dumps(result, indent=2) + "\n"
    if args.write_receipt:
        args.write_receipt.write_text(text)
    else:
        require(result == json.loads(RECEIPT.read_text()),
                "transfer controls differ from the persisted receipt")
    print(text, end="")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, OSError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
