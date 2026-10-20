#!/usr/bin/env python3
"""Bounded discovery and exact replay of RAW positive odd 3x+d cycles.

Default: verify the saved cycle certificates, not rerun the discovery scan.
--scan writes a new receipt. State1 is never absorbed in this experiment.
No finite scan establishes completeness of the cycle spectrum.
"""

import argparse
from collections import Counter
from hashlib import sha256
import json
from math import gcd
from pathlib import Path
import subprocess
import sys
import time


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
FIXTURES = ROOT / "experiments/phase6/cycle_fixtures.json"


def require(test, message):
    if not test:
        raise ValueError(message)


def digest(value):
    return sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def step(n, d):
    require(n > 0 and n % 2 and d > 0 and gcd(d, 6) == 1,
            "positive odd source and positive d coprime to6 required")
    value = 3 * n + d
    a = (value & -value).bit_length() - 1
    return value >> a, a


def canonical(states):
    require(states and len(set(states)) == len(states), "cycle states must be distinct")
    i = states.index(min(states))
    return tuple(states[i:] + states[:i])


def word_data(word):
    C, A = 0, 0
    for a in word:
        require(isinstance(a, int) and a >= 1, "positive valuations required")
        C = 3 * C + 2**A
        A += a
    return len(word), A, C, 2**A - 3**len(word)


def z_array(word):
    z = [0] * len(word)
    left = right = 0
    for i in range(1, len(word)):
        if i <= right:
            z[i] = min(right - i + 1, z[i - left])
        while i + z[i] < len(word) and word[z[i]] == word[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > right:
            left, right = i, i + z[i] - 1
    return z


def split_checks(word, Cw, Dw, G):
    """All splits and repeated prefixes in the minimum-state orientation only."""
    m = len(word)
    prefix = [(0, 0, 0, 0)]
    A, C = 0, 0
    for i, a in enumerate(word):
        C = 3 * C + 2**A
        A += a
        prefix.append((i + 1, A, C, 2**A - 3**(i + 1)))
    suffix = [None] * (m + 1)
    suffix[m] = (0, 0, 0, 0)
    for i in range(m - 1, -1, -1):
        length, A, C, _ = suffix[i + 1]
        C = 3**length + 2**word[i] * C
        A += word[i]
        suffix[i] = (length + 1, A, C, 2**A - 3**(length + 1))
    all_splits, repeated = [], []

    def check(length, k):
        _, Au, Cu, Du = prefix[length]
        _, Av, Cv, Dv = suffix[k * length]
        K = Du * Cv - Dv * Cu
        require(Du * Cw - Cu * Dw == 2**(k * Au) * K,
                "two-block elimination identity failed")
        require(K != 0, "a simple cycle cannot have two blocks with the same fixed point")
        require(K % G == 0, "cycle gcd does not divide the cancellation constant")
        require((Dw // G) * abs(K) >= Dw, "reduced denominator lower bound failed")
        return {"u_length": length, "k": k, "v_length": m - k * length,
                "A_u": Au, "C_u": Cu, "D_u": Du,
                "A_v": Av, "C_v": Cv, "D_v": Dv, "K": K,
                "denominator_lower_bound": (Dw + abs(K) - 1) // abs(K)}

    for length in range(1, m):
        all_splits.append(check(length, 1))
    z = z_array(word)
    for length in range(1, (m - 1) // 2 + 1):
        max_k = min((m - 1) // length, 1 + z[length] // length)
        for k in range(2, max_k + 1):
            require(word[:k * length] == word[:length] * k, "repeated prefix mismatch")
            repeated.append(check(length, k))
    return {"orientation": "canonical minimum-state word only; no all-rotation catalogue",
            "all_two_block_splits": len(all_splits),
            "two_block_sha256": digest(all_splits),
            "minimum_abs_K": min((abs(row["K"]) for row in all_splits), default=None),
            "all_K_nonzero": True, "all_gcd_divisibilities_pass": True,
            "repeated_prefixes": repeated}


def certificate(d, states):
    states = list(canonical(list(states)))
    word = []
    for i, n in enumerate(states):
        target, a = step(n, d)
        require(target == states[(i + 1) % len(states)], "cycle arrow does not close")
        word.append(a)
    m, A, C, D = word_data(word)
    require(D > 0 and states[0] * D == d * C, "positive cycle equation failed")
    G = gcd(C, D)
    numerator, denominator = C // G, D // G
    require(d % denominator == 0 and gcd(denominator, 6) == 1,
            "reduced denominator does not divide the additive parameter")
    scale = d // denominator
    require(states[0] == numerator * scale, "actual scaling failed")
    for n in states:
        require(d // gcd(n, d) == denominator and n % scale == 0,
                "reduced denominator is not invariant around the cycle")
    primitive_states = [n // scale for n in states]
    for i, n in enumerate(primitive_states):
        require(step(n, denominator)[0] == primitive_states[(i + 1) % m],
                "normalized primitive integer cycle failed")
    return {"d": d, "minimum": states[0], "states": states, "word": word,
            "m": m, "A": A, "C": C, "D": D, "gcd_C_D": G,
            "reduced_numerator": numerator, "reduced_denominator": denominator,
            "actual_scaling": scale, "primitive_states": primitive_states,
            "contains_raw_state1": 1 in states,
            "two_block": split_checks(word, C, D, G)}


def load_fixtures():
    raw = json.loads(FIXTURES.read_text())
    rows = []
    require(raw["schema"] == "phase6-cycles-v1", "unexpected fixture schema")
    for i, fixture in enumerate(raw["cycles"]):
        row = certificate(fixture["d"], fixture["states"])
        require(row["minimum"] == fixture["minimum"]
                and row["word"] == fixture["valuations"], "fixture is not exact/canonical")
        rows.append((f"phase6_fixture_{i + 1:02d}", row))
    require(len(rows) == 11, "the eleven historical fixtures must be retained")
    return rows


def scan(args):
    params = {"d_max": args.d_max, "seed_max": args.seed_max,
              "steps_per_new_path": args.steps, "state_bit_cap": args.bit_cap,
              "wall_time_budget_seconds": args.seconds,
              "memoization": "only exact certified cycle basins; capped paths are not memoized"}
    ds = [d for d in range(1, args.d_max + 1, 2) if d % 3]
    seeds = range(1, args.seed_max + 1, 2)
    started = time.monotonic()
    discovered, summaries, witnesses = {}, [], []
    total_outcomes = Counter()
    halted = False
    for d in ds:
        memo = set()
        outcomes = Counter()
        new_arrows, peak_bits, found = 0, 0, set()
        for seed in seeds:
            if time.monotonic() - started >= args.seconds:
                halted = True
                break
            if seed in memo:
                outcomes["certified_cycle_basin"] += 1
                continue
            path, positions, n = [], {}, seed
            reason = None
            while True:
                if n in memo:
                    reason = "certified_cycle_basin"
                    break
                if n in positions:
                    cyc = canonical(path[positions[n]:])
                    key = (d, cyc)
                    discovered.setdefault(key, {"first_seed": seed, "discovery_d": d})
                    found.add(cyc)
                    reason = "certified_cycle_basin"
                    break
                peak_bits = max(peak_bits, n.bit_length())
                if n.bit_length() > args.bit_cap:
                    reason = "state_bit_cap"
                    break
                if len(path) >= args.steps:
                    reason = "path_step_cap"
                    break
                if len(path) % 256 == 0 and time.monotonic() - started >= args.seconds:
                    reason, halted = "wall_time_cap", True
                    break
                positions[n] = len(path)
                path.append(n)
                value = 3 * n + d
                n = value >> ((value & -value).bit_length() - 1)
                new_arrows += 1
            outcomes[reason] += 1
            if reason == "certified_cycle_basin":
                memo.update(path)
            else:
                witnesses.append({"d": d, "seed": seed, "reason": reason,
                                  "new_arrows": len(path), "last_state": n,
                                  "last_state_bits": n.bit_length()})
            if halted:
                break
        total_outcomes.update(outcomes)
        summaries.append({"d": d, "seed_outcomes": dict(sorted(outcomes.items())),
                          "processed_seeds": sum(outcomes.values()), "new_arrows": new_arrows,
                          "peak_state_bits": peak_bits, "certified_memo_states": len(memo),
                          "cycles_discovered": len(found)})
        if halted:
            break
    scan_seconds = time.monotonic() - started
    records = {}
    for (d, states), discovery in discovered.items():
        row = certificate(d, states)
        row["discovery"] = discovery
        row["fixture_ids"] = []
        records[(d, tuple(states))] = row
    fixture_matches = []
    for fixture_id, fixture in load_fixtures():
        key = (fixture["d"], tuple(fixture["states"]))
        found = key in records
        if not found:
            fixture["discovery"] = None
            fixture["fixture_ids"] = []
            records[key] = fixture
        records[key]["fixture_ids"].append(fixture_id)
        fixture_matches.append({"fixture_id": fixture_id, "d": key[0],
                                "minimum": key[1][0], "also_discovered_by_scan": found})
    cycles = sorted(records.values(), key=lambda row: (row["d"], row["minimum"]))
    processed = sum(total_outcomes.values())
    total_requested = len(ds) * len(seeds)
    receipt = {"schema": "C001-actual-raw-cycles-v1", "status": "finite certificates verified",
               "clock": "raw odd-only map n -> (3n+d)/2^v2(3n+d); state1 is not absorbed",
               "scope": "Bounded discovery, not a complete cycle census or convergence evidence. Unprocessed and capped seeds remain unresolved.",
               "replay_scope": "Every cycle, first discovery-seed connection, decomposition, fixture and receipt count is checked. Default replay does not rerun every scanned seed.",
               "sources": {"repository_head_at_scan": subprocess.check_output(
                   ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
                   "fixture_path": str(FIXTURES.relative_to(ROOT)),
                   "fixture_sha256": sha256(FIXTURES.read_bytes()).hexdigest(),
                   "scanner_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
                   "external_theorems_used": []},
               "parameters": params, "discovery_seconds": round(scan_seconds, 6),
               "requested_d_count": len(ds), "requested_seed_count": total_requested,
               "processed_seed_count": processed, "unprocessed_seed_count": total_requested - processed,
               "seed_outcomes": dict(sorted(total_outcomes.items())),
               "d_summaries": summaries, "unresolved_path_witnesses": witnesses,
               "fixture_matches": fixture_matches, "cycles": cycles}
    receipt["summary"] = summarize(cycles)
    return receipt


def summarize(cycles):
    primitive = {(row["reduced_denominator"], tuple(row["primitive_states"])) for row in cycles}
    return {"actual_cycles": len(cycles),
            "cycles_discovered_by_scan": sum(row["discovery"] is not None for row in cycles),
            "fixture_only_cycles": sum(row["discovery"] is None for row in cycles),
            "primitive_normalized_cycles": len(primitive),
            "distinct_reduced_denominators": sorted({row["reduced_denominator"] for row in cycles}),
            "cycle_length_histogram": dict(sorted(Counter(str(row["m"]) for row in cycles).items(),
                                                   key=lambda item: int(item[0]))),
            "maximum_cycle_length": max(row["m"] for row in cycles),
            "maximum_state": max(max(row["states"]) for row in cycles),
            "two_block_split_checks": sum(row["two_block"]["all_two_block_splits"] for row in cycles),
            "repeated_prefix_checks": sum(len(row["two_block"]["repeated_prefixes"]) for row in cycles)}


def verify(receipt):
    require(receipt["schema"] == "C001-actual-raw-cycles-v1", "wrong receipt schema")
    require(receipt["sources"]["scanner_sha256"] == sha256(Path(__file__).read_bytes()).hexdigest(),
            "scanner source hash mismatch")
    require(receipt["sources"]["fixture_sha256"] == sha256(FIXTURES.read_bytes()).hexdigest(),
            "historical fixture hash mismatch")
    params = receipt["parameters"]
    ds = [d for d in range(1, params["d_max"] + 1, 2) if d % 3]
    seed_count = (params["seed_max"] + 1) // 2
    require(receipt["requested_d_count"] == len(ds)
            and receipt["requested_seed_count"] == len(ds) * seed_count,
            "requested scan domain mismatch")
    seen = set()
    fixture_ids = {}
    discovery_counts = Counter()
    for row in receipt["cycles"]:
        expected = certificate(row["d"], row["states"])
        expected["discovery"], expected["fixture_ids"] = row["discovery"], row["fixture_ids"]
        require(row == expected, "cycle arithmetic/decomposition certificate mismatch")
        key = (row["d"], tuple(row["states"]))
        require(key not in seen, "duplicate canonical cycle")
        seen.add(key)
        discovery = row["discovery"]
        if discovery is not None:
            require(row["d"] in ds and discovery["discovery_d"] == row["d"],
                    "discovery parameter is outside the declared scan")
            n = discovery["first_seed"]
            require(1 <= n <= params["seed_max"] and n % 2,
                    "discovery seed is outside the declared scan")
            cycle_states = set(row["states"])
            for _ in range(params["steps_per_new_path"] + 1):
                if n in cycle_states:
                    break
                require(n.bit_length() <= params["state_bit_cap"],
                        "discovery connection violates the state cap")
                n, _ = step(n, row["d"])
            else:
                raise ValueError("discovery seed did not reach its stated cycle within the cap")
            discovery_counts[row["d"]] += 1
        for fixture_id in row["fixture_ids"]:
            require(fixture_id not in fixture_ids, "fixture identifier reused")
            fixture_ids[fixture_id] = key
    fixtures = load_fixtures()
    require(len(fixture_ids) == len(fixtures), "unexpected or missing fixture identifier")
    expected_matches = []
    cycle_lookup = {(row["d"], tuple(row["states"])): row for row in receipt["cycles"]}
    for fixture_id, fixture in fixtures:
        require(fixture_ids.get(fixture_id) == (fixture["d"], tuple(fixture["states"])),
                "historical fixture missing or incorrectly assigned")
        row = cycle_lookup[(fixture["d"], tuple(fixture["states"]))]
        expected_matches.append({"fixture_id": fixture_id, "d": row["d"],
                                 "minimum": row["minimum"],
                                 "also_discovered_by_scan": row["discovery"] is not None})
    require(receipt["fixture_matches"] == expected_matches, "fixture match summary mismatch")
    require(receipt["summary"] == summarize(receipt["cycles"]), "summary mismatch")
    outcomes = Counter()
    summaries = receipt["d_summaries"]
    require([row["d"] for row in summaries] == ds[:len(summaries)],
            "per-parameter scan prefix mismatch")
    allowed_reasons = {"certified_cycle_basin", "path_step_cap", "state_bit_cap", "wall_time_cap"}
    for row in summaries:
        require(set(row["seed_outcomes"]) <= allowed_reasons,
                "unknown seed outcome")
        require(row["processed_seeds"] == sum(row["seed_outcomes"].values())
                and 0 <= row["processed_seeds"] <= seed_count,
                "per-parameter seed accounting mismatch")
        require(row["cycles_discovered"] == discovery_counts[row["d"]],
                "per-parameter cycle count mismatch")
        outcomes.update(row["seed_outcomes"])
    require(dict(outcomes) == receipt["seed_outcomes"], "aggregate outcome mismatch")
    capped = Counter()
    for witness in receipt["unresolved_path_witnesses"]:
        reason = witness["reason"]
        require(reason in allowed_reasons - {"certified_cycle_basin"},
                "invalid unresolved-path reason")
        n = witness["seed"]
        require(witness["d"] in ds and 1 <= n <= params["seed_max"] and n % 2,
                "unresolved witness is outside the scan domain")
        for _ in range(witness["new_arrows"]):
            n, _ = step(n, witness["d"])
        require(n == witness["last_state"] and n.bit_length() == witness["last_state_bits"],
                "unresolved witness path mismatch")
        if reason == "path_step_cap":
            require(witness["new_arrows"] == params["steps_per_new_path"],
                    "step cap mismatch")
        if reason == "state_bit_cap":
            require(n.bit_length() > params["state_bit_cap"], "bit cap mismatch")
        capped[reason] += 1
    require(dict(capped) == {key: value for key, value in outcomes.items()
                            if key != "certified_cycle_basin"}, "unresolved witness count mismatch")
    require(receipt["processed_seed_count"] == sum(receipt["seed_outcomes"].values())
            and receipt["processed_seed_count"] + receipt["unprocessed_seed_count"]
            == receipt["requested_seed_count"], "seed accounting mismatch")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scan", action="store_true")
    parser.add_argument("--output", type=Path, default=HERE / "actual_cycles.json")
    parser.add_argument("--d-max", type=int, default=999)
    parser.add_argument("--seed-max", type=int, default=5000)
    parser.add_argument("--steps", type=int, default=10000)
    parser.add_argument("--bit-cap", type=int, default=4096)
    parser.add_argument("--seconds", type=float, default=100)
    args = parser.parse_args()
    try:
        require(min(args.d_max, args.seed_max, args.steps, args.bit_cap, args.seconds) > 0,
                "all scan bounds must be positive")
        if args.scan:
            receipt = scan(args)
            verify(receipt)
            args.output.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
        else:
            receipt = json.loads(args.output.read_text())
            verify(receipt)
    except (OSError, ValueError, TypeError, KeyError, subprocess.SubprocessError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(json.dumps({"status": "PASS", "summary": receipt["summary"],
                      "unprocessed_seeds": receipt["unprocessed_seed_count"],
                      "seed_outcomes": receipt["seed_outcomes"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
