#!/usr/bin/env python3
"""Check C013 saved evidence, review pins and preservation of prior results."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BASE = 'de7db672582eb3745efa2eb9a99326ccf43206b9'
FROZEN = '9190ccf2519acc56446dd027c6cbf8d45dcceeb6'
SIDE = '3529355a5b77740c5ff3f874d228ee9a1b5bb478'
TOP = ('AGENTS.md', 'README.md', 'VIEWPOINT_MAP.md', 'docs/CYCLE_SPECTRUM_BRIEF.md',
       'docs/CYCLE_SPECTRUM_LOG.md', 'docs/RESEARCH_LOG.md', 'docs/RESULTS.md', 'docs/VIEWPOINT_LOG.md')
REVIEWS = {
    'OVERLAP_CONTROLS.md': ('THEORY_REVIEW.md', 'ROOT_REVIEW.md', 'EXACT_REVIEW.md'),
    'OVERLAP_THEORY.md': ('OBSTRUCTION_REVIEW.md', 'ROOT_REVIEW.md', 'EXACT_REVIEW.md'),
    'check_overlap.py': ('INDEPENDENT_CHECKER_REVIEW.md', 'ROOT_REVIEW.md', 'EXACT_REVIEW.md'),
    'overlap_audit.json': ('INDEPENDENT_CHECKER_REVIEW.md', 'ROOT_REVIEW.md', 'EXACT_REVIEW.md'),
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def report():
    gate = json.loads((HERE/'historical_gate.json').read_text())
    metadata = {'archive_sha256', 'manifest_entries', 'scope'}
    require(len(gate) == 119 and metadata <= set(gate), 'historical coverage changed')
    require(gate['status'] == 'PASS' and all(isinstance(v, str) and v.startswith('PASS')
            for k, v in gate.items() if k not in metadata), 'historical gate failed')
    pins = {name: digest(HERE/name) for name in REVIEWS}
    for name, reviews in REVIEWS.items():
        for review in reviews:
            require(pins[name] in (HERE/review).read_text(), 'missing review pin: '+name+' in '+review)
    receipt = json.loads((HERE/'overlap_audit.json').read_text())
    require(receipt['status'] == 'PASS' and receipt['checker_sha256'] == pins['check_overlap.py'],
            'checker status or version changed')
    for name, pin in receipt['source_sha256'].items():
        require(digest(ROOT/name) == pin, 'input changed: '+name)
    actual = receipt['actual']
    require(actual['source_instances'] == 2459 and actual['source_parameters'] == 333
            and len(actual['fixture_controls']) == 11, 'raw corpus coverage changed')
    expected = dict(normalized_cycles=1185, normalized_arrows=28831, raw_arrows=36912,
        rotations=27646, fourier_complexity_checks=27646, exact_polynomial_gcds=1185,
        coprime_total_polynomial_controls=423, nonconstant_polynomial_gcds=20,
        empty_background_uniform_bounds=1177, fixed_points_outside_nonconstant_marker_theorem=8,
        maximal_agreeing_runs=969102, positive_length_runs=334590, overlap_orbit_sums=75577,
        unit_difference_multipliers=5242, positive_run_unit_multipliers=4202,
        scaled_source_instances=1275)
    require(actual['counts'] == expected, 'actual evidence coverage changed')
    stress = receipt['structured_candidate_stress']['counts']
    require(stress['words'] == stress['candidate_passes'] == stress['passes_already_implied_by_q'] == 243,
            'candidate discrimination scope changed')
    common = receipt['common_background']
    require(len(common['long_background_exclusions']) == 4 and
            all(c['certified_lower_bound_exceeds_one'] for c in common['long_background_exclusions']),
            'nonempty quantitative controls changed')
    require(len(common['negative_full_D_controls']) == 2 and
            len(common['trivial_repetition_controls']) == 3, 'boundary controls changed')
    near = receipt['near_critical_height']['cases']
    require([(c['m'], c['B'], c['q_bits']) for c in near] ==
            [(51, 6, 78), (123, 12, 191), (918, 76, 1447)], 'height controls changed')
    previous = git('ls-tree', '-r', '--name-only', BASE, 'experiments/cycle_spectrum').decode().splitlines()
    require(len(previous) == 163, 'prior cycle file count changed')
    for name in previous:
        require((ROOT/name).read_bytes() == git('show', BASE+':'+name), 'historical cycle file changed: '+name)
    marker = b'## R1 \xe2\x80\x94 Exact source transport and original packets'
    ledger, old = (ROOT/'docs/RESULTS.md').read_bytes(), git('show', FROZEN+':docs/RESULTS.md')
    require(ledger.count(marker) == old.count(marker) == 1, 'frozen ledger boundary changed')
    require(ledger.split(marker, 1)[1] == old.split(marker, 1)[1], 'frozen ledger changed')
    frozen = ('collatz_research_20261017/right_aligned_reduction.tex',
              'experiments/residual_progress/resolved_rules/RESOLVED_RULES.md',
              'experiments/residual_progress/resolved_rules/resolved_rules.py')
    for name in frozen:
        require((ROOT/name).read_bytes() == git('show', FROZEN+':'+name), 'frozen file changed: '+name)
    files = [ROOT/name for name in TOP]+sorted(HERE.glob('*.md'))
    links, errors = 0, []
    for path in files:
        body = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
        for target in re.findall(r'\]\(([^)]+)\)', body):
            target = target.split('#', 1)[0].strip('<>')
            if not target or re.match(r'[a-zA-Z]+:', target):
                continue
            links += 1
            destination = (path.parent/target).resolve()
            if destination != HERE/'delivery_checks.json' and not destination.exists():
                errors.append([str(path.relative_to(ROOT)), target])
    require(not errors, 'broken local links: '+repr(errors))
    require(SIDE in (HERE/'SIDE_REVIEW.md').read_text() and
            SIDE in (ROOT/'docs/VIEWPOINT_LOG.md').read_text(), 'side review pin missing')
    git('diff', '--check')
    return dict(status='PASS', scope='Saved evidence consistency, review pins and preservation; not a mathematical or formal replay.',
        baseline_commit=BASE, frozen_commit=FROZEN, reviewed_side_commit=SIDE,
        goal_status='All-cycle goal active; unrestricted growing mismatch target remains open.',
        historical_gate=dict(status='PASS', fields=len(gate)), reviewed_pins=pins,
        independent_reviews=REVIEWS, saved_actual_coverage=actual['counts'],
        preservation=dict(C001_C012_files_unchanged=len(previous), R1_onward_byte_identical=True,
            frozen_files_byte_identical=list(frozen), git_diff_check='PASS'),
        markdown_checks=dict(files=len(files), checked_local_links=links, errors=errors),
        top_document_sha256={name: digest(ROOT/name) for name in TOP},
        batch_file_sha256={p.name: digest(p) for p in sorted(HERE.iterdir())
                          if p.is_file() and p.name != 'delivery_checks.json'})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    result = json.loads(json.dumps(report()))
    path = HERE/'delivery_checks.json'
    if args.write:
        path.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    require(json.loads(path.read_text()) == result, 'delivery receipt differs')
    print(json.dumps({k: result[k] for k in ('status', 'preservation', 'markdown_checks')}))


if __name__ == '__main__':
    main()
