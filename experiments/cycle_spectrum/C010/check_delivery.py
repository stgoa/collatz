#!/usr/bin/env python3
"""Check C010 saved receipts, review pins, local links, and preserved history.

This checks delivery consistency. It does not rerun mathematical experiments
or the historical gate and does not turn saved evidence into formal replay.
Run only after the historical gate has completed and the batch is frozen.
"""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BASE = 'ec48fbde29258e88cd6e7cd226e2cb6aebc6011e'
FROZEN = '9190ccf2519acc56446dd027c6cbf8d45dcceeb6'
SIDE_COMMITS = ('0448ab3d463db61e261e4998e8604dbfb756947a',
                '4856ed7c3eb03fcc2dcbadbb9d799ebc08887860')
LEAN_STATE = 'a1e1054ff8d509a84f7f373068b2d6e324987a82'
TOP = ('AGENTS.md', 'README.md', 'VIEWPOINT_MAP.md', 'docs/CYCLE_SPECTRUM_BRIEF.md',
       'docs/CYCLE_SPECTRUM_LOG.md', 'docs/RESEARCH_LOG.md', 'docs/RESULTS.md',
       'docs/VIEWPOINT_LOG.md')
PINS = {
    'GAP_LATTICE.md': 'e8eed1e1a08aeefc1632ef4e762da8bc9182ee6456bb390a5e804c86c968ee64',
    'ODD_ROUNDING.md': '4647d1b51ddf73e1e6a5b5161414c5368d3c9098baa115cd61748c52132a59ac',
    'ROUNDING_PROBE.md': '62b9d2da833ce97fa1025e2bc22aafa6ee768c16e84c24044330beed8b76dbf2',
    'check_integer_gaps.py': '87221a51c008668a8e36513096080cfc352ad16a86ba842976342a1c7deead78',
    'integer_gap_audit.json': 'f26028a1d6c9f5f725e1d0bece4d1f3e44dc5dc895863c105433c9eed8d92d5c',
}
INDEPENDENT_PIN_REVIEWS = {
    'GAP_LATTICE.md': 'ARITHMETIC_REVIEW.md',
    'ODD_ROUNDING.md': 'EXACT_CHECKER_REVIEW.md',
    'ROUNDING_PROBE.md': 'ARITHMETIC_REVIEW.md',
    'check_integer_gaps.py': 'ARITHMETIC_REVIEW.md',
    'integer_gap_audit.json': 'ARITHMETIC_REVIEW.md',
}
DEPENDENCIES = {
    'experiments/cycle_spectrum/C010/check_integer_gaps.py',
    'experiments/cycle_spectrum/C009/check_excursions.py',
    'experiments/cycle_spectrum/C001/actual_cycles.json',
    'experiments/cycle_spectrum/C007/height_denominator_audit.json',
    'experiments/phase6/cycle_fixtures.json',
    'experiments/cycle_spectrum/C004/SIZE_PROBE.md',
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def report():
    gate = json.loads((HERE/'historical_gate.json').read_text())
    metadata = {'archive_sha256', 'manifest_entries', 'scope'}
    require(len(gate) == 119 and metadata <= set(gate), 'historical gate coverage changed')
    require(all(isinstance(value, str) and value.startswith('PASS')
                for key, value in gate.items() if key not in metadata),
            'historical gate contains a non-PASS result')
    require(gate['status'] == 'PASS', 'historical gate has not passed')

    for name, expected in PINS.items():
        require(digest(HERE/name) == expected, 'reviewed source changed: '+name)
        review_name = INDEPENDENT_PIN_REVIEWS[name]
        require(expected in (HERE/review_name).read_text(),
                'independent review is missing the source pin: '+name)
    for name in ('check_integer_gaps.py', 'integer_gap_audit.json'):
        require(PINS[name] in (HERE/'INDEPENDENT_REVIEW.md').read_text(),
                'second independent replay review is missing source pin: '+name)

    audit = json.loads((HERE/'integer_gap_audit.json').read_text())
    require(audit['status'] == 'PASS' and audit['schema'] == 'C010-integer-gaps-v1',
            'integer-gap receipt status or schema changed')
    require(set(audit['source_sha256']) == DEPENDENCIES,
            'integer-gap dependency list changed')
    for name, expected in audit['source_sha256'].items():
        require(digest(ROOT/name) == expected, 'integer-gap dependency changed: '+name)

    existing = audit['existing']
    counts = existing['counts']
    expected_existing = dict(source_cycles=2459, source_parameters=333,
                             scaled_source_instances=1275, source_raw_arrows=36912,
                             C007_new_distinct_cycles=1)
    require(all(existing[key] == value for key, value in expected_existing.items())
            and len(existing['fixture_controls']) == 11,
            'saved actual-cycle receipt coverage changed')
    expected_counts = dict(normalized_cycles=1185, normalized_arrows=28831,
        coordinate_gcd_one=1185, ordered_cycles=52, ordered_nonfixed_cycles=51,
        ordered_wide_cycles=47, ordered_arrows=474,
        actual_sharp_local_rounding_checks=474, actual_sharp_circular_pair_checks=7022,
        rescaled_additive_one_local_pass=20, noninteger_rescaled_additive_one_local_pass=19,
        rescaled_additive_one_all_circular_pairs_pass=20,
        rescaled_additive_one_sum_pass=31, rescaled_additive_one_odd_ceiled_sum_pass=28)
    require(all(counts[key] == value for key, value in expected_counts.items()),
            'saved coordinate or ordered-domain receipt coverage changed')
    expected_grid = dict(integer_vectors=19530, rational_vectors=78120,
        rank_operator_commutations=131835, unimodular_determinants=12,
        coprime_rank_determinants=46, independent_sharp_bound_checks=1428)
    require(audit['independent_grid']['counts'] == expected_grid,
            'saved algebra-grid coverage changed')
    mechanical = audit['mechanical_complete_gaps']
    expected_mechanical = dict(cycles=4, raw_cycle_arrows=355, interior_monomials=351,
        exact_seam_checks=4, phase_intercept_summands=95351,
        proper_circular_pair_checks=94996, noninteger_shapes_passing_all_pair_bounds=3)
    require(mechanical['counts'] == expected_mechanical and
            [(c['A'], c['m']) for c in mechanical['cases']] ==
            [(5, 3), (8, 5), (65, 41), (485, 306)],
            'saved mechanical complete-gap coverage changed')
    require(audit['rejection_controls']['rejected_inputs'] == 5,
            'saved rejection controls changed')

    previous = git('ls-tree', '-r', '--name-only', BASE,
                   'experiments/cycle_spectrum').decode().splitlines()
    previous = [name for name in previous
                if re.match(r'experiments/cycle_spectrum/C00[1-9]/', name)]
    require(len(previous) == 112, 'historical cycle file coverage changed')
    for name in previous:
        require((ROOT/name).read_bytes() == git('show', BASE+':'+name),
                'historical cycle batch changed: '+name)
    marker = '## R1 — Exact source transport and original packets'.encode()
    current_ledger = (ROOT/'docs/RESULTS.md').read_bytes()
    frozen_ledger = git('show', FROZEN+':docs/RESULTS.md')
    require(current_ledger.count(marker) == frozen_ledger.count(marker) == 1,
            'frozen result-ledger boundary is missing or ambiguous')
    require(current_ledger.split(marker, 1)[1] == frozen_ledger.split(marker, 1)[1],
            'frozen result ledger changed')
    kept = ['collatz_research_20261017/right_aligned_reduction.tex',
            'experiments/residual_progress/resolved_rules/RESOLVED_RULES.md',
            'experiments/residual_progress/resolved_rules/resolved_rules.py']
    for name in kept:
        require((ROOT/name).read_bytes() == git('show', FROZEN+':'+name),
                'frozen file changed: '+name)

    files = [ROOT/name for name in TOP]+sorted(HERE.glob('*.md'))
    for name in ('ROOT_REVIEW.md', 'REPORT.md', 'LITERATURE.md', 'SIDE_REVIEW.md',
                 'ARITHMETIC_REVIEW.md', 'INDEPENDENT_REVIEW.md', 'EXACT_CHECKER_REVIEW.md'):
        require((HERE/name).is_file(), 'batch document is not ready: '+name)
    links, errors = 0, []
    for path in files:
        body = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
        for target in re.findall(r'\]\(([^)]+)\)', body):
            target = target.split('#', 1)[0].strip('<>')
            if not target or re.match(r'[a-zA-Z]+:', target):
                continue
            links += 1
            destination = (path.parent/target).resolve()
            if destination == HERE/'delivery_checks.json':
                continue  # The output being constructed is not an input dependency.
            if not destination.exists():
                errors.append([str(path.relative_to(ROOT)), target])
    require(not errors, 'broken local link: '+repr(errors))
    for commit in (*SIDE_COMMITS, LEAN_STATE):
        require(commit in (HERE/'SIDE_REVIEW.md').read_text() and
                commit in (ROOT/'docs/VIEWPOINT_LOG.md').read_text(),
                'side review or viewpoint log is missing the reviewed commit: '+commit)
    git('diff', '--check')
    hashes = {str(path.relative_to(ROOT)): digest(path) for path in sorted(HERE.iterdir())
              if path.is_file() and path.name != 'delivery_checks.json'}
    return dict(status='PASS', baseline_commit=BASE, frozen_commit=FROZEN,
        scope='Preservation and consistency of saved evidence; no fresh mathematical or formal replay.',
        goal_status='All-cycle objective remains active; ordered q1 exclusion is open and intermediate.',
        historical_gate=dict(status='PASS', command='python3 scripts/verify_all.py --cpp --transfer-controls',
            field_count=len(gate), independent_cpp=gate['independent_cpp'],
            phase6_transfer_controls=gate['phase6_transfer_controls']),
        source_reviews=dict(status='PASS', pinned_sha256=PINS,
            independent_pin_reviews=INDEPENDENT_PIN_REVIEWS,
            scope='Review authorship and independent replay are identified in each review; no formal verification claimed.'),
        saved_receipt_coverage=dict(**expected_existing, fixture_controls=11,
            coordinate_and_rounding=counts, algebra_grid=expected_grid,
            mechanical_complete_gaps=expected_mechanical, rejected_inputs=5),
        preservation=dict(C001_C009_files_unchanged=len(previous), R1_onward_byte_identical=True,
            frozen_files_byte_identical=kept, git_diff_check='PASS'),
        markdown_checks=dict(files=len(files), checked_local_links=links, errors=errors),
        top_document_sha256={name: digest(ROOT/name) for name in TOP},
        batch_file_sha256=hashes,
        side_reports=dict(reviewed_commits=list(SIDE_COMMITS), lean_state_commit=LEAN_STATE,
            scope='Side-lane research reports were inspected. No main-side independent Lean kernel replay is claimed.'))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    result = report()
    path = HERE/'delivery_checks.json'
    if args.write:
        path.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    else:
        require(path.exists() and json.loads(path.read_text()) == result,
                'delivery receipt mismatch')
    print(json.dumps({key: result[key] for key in ('status', 'preservation', 'markdown_checks')}))


if __name__ == '__main__':
    main()
