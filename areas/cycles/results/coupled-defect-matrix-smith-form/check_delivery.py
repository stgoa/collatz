#!/usr/bin/env python3
"""Check saved C012 evidence, independent review pins and preserved history."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BASE = 'b896512077a4be31ef3d9fcdcf833d1a59cd1b89'
FROZEN = '9190ccf2519acc56446dd027c6cbf8d45dcceeb6'
SIDE = 'f01ac0e24c42353dedaf67b7bfd73548cdd015e4'
TOP = ('AGENTS.md', 'README.md', 'VIEWPOINT_MAP.md', 'docs/CYCLE_SPECTRUM_BRIEF.md',
       'docs/CYCLE_SPECTRUM_LOG.md', 'docs/RESEARCH_LOG.md', 'docs/RESULTS.md', 'docs/VIEWPOINT_LOG.md')
REVIEWS = {
    'COUPLED_SYSTEM.md': ('EXACT_REVIEW.md', 'INDEPENDENT_THEORY_REVIEW.md', 'ROOT_REVIEW.md'),
    'COUPLED_OBSTRUCTIONS.md': ('EXACT_REVIEW.md', 'ROOT_REVIEW.md'),
    'check_coupled_system.py': ('EXACT_REVIEW.md', 'INDEPENDENT_CHECKER_REVIEW.md'),
    'coupled_system_audit.json': ('EXACT_REVIEW.md', 'INDEPENDENT_CHECKER_REVIEW.md'),
    'check_shared_arcs.py': ('INDEPENDENT_THEORY_REVIEW.md',),
    'shared_arc_audit.json': ('INDEPENDENT_THEORY_REVIEW.md',),
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
    coupled = json.loads((HERE/'coupled_system_audit.json').read_text())
    shared = json.loads((HERE/'shared_arc_audit.json').read_text())
    require(coupled['status'] == shared['status'] == 'PASS', 'receipt failed')
    require(coupled['checker_sha256'] == pins['check_coupled_system.py'], 'coupled checker changed')
    for name, pin in coupled['source_sha256'].items():
        require(digest(ROOT/name) == pin, 'coupled input changed: '+name)
    for name, pin in shared['source_sha256'].items():
        require(digest(HERE/name) == pin, 'shared input changed: '+name)
    actual, generated = coupled['actual'], coupled['generated']
    require(actual['source_cycles'] == 2459 and actual['source_parameters'] == 333
            and len(actual['fixture_controls']) == 11, 'raw corpus coverage changed')
    expected = dict(normalized_cycles=1185, normalized_arrows=28831, raw_arrows=36912,
                    rotations=27646, all_cut_identities=1938204, coupled_equations=969102,
                    independent_determinants=28, independent_minors=552,
                    candidate_passes=27646, candidate_passes_already_implied_by_q=27646)
    require(all(actual['counts'][k] == v for k, v in expected.items()), 'actual coverage changed')
    require(generated['counts']['candidate_rotations'] ==
            generated['counts']['candidate_passes_already_implied_by_q'] == 2887,
            'candidate discrimination changed')
    require(generated['counts']['prime_power_local_profiles'] == 5 and
            generated['counts']['prime_power_three_minors'] == 6704, 'prime-power coverage changed')
    require(shared['counts'] == dict(backgrounds=350, admissible_total_backgrounds=3582,
            prime_set_cases=7, raw_arrows=177288, rotations=173349), 'shared coverage changed')
    previous = git('ls-tree', '-r', '--name-only', BASE, 'experiments/cycle_spectrum').decode().splitlines()
    require(len(previous) == 147, 'prior cycle file count changed')
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
    for name in ('REPORT.md', 'ROOT_REVIEW.md', 'SIDE_REVIEW.md', 'LITERATURE.md',
                 'EXACT_REVIEW.md', 'INDEPENDENT_CHECKER_REVIEW.md', 'INDEPENDENT_THEORY_REVIEW.md'):
        require((HERE/name).is_file(), 'missing document: '+name)
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
    return dict(status='PASS', scope='Saved consistency, review pins and preservation; not a mathematical or formal replay.',
        baseline_commit=BASE, frozen_commit=FROZEN, reviewed_side_commit=SIDE,
        goal_status='All-cycle goal active; growing mismatch target remains open.',
        historical_gate=dict(status='PASS', fields=len(gate)), reviewed_pins=pins,
        independent_reviews=REVIEWS,
        saved_coverage=dict(actual=actual['counts'], generated=generated['counts'], shared=shared['counts']),
        preservation=dict(C001_C011_files_unchanged=len(previous), R1_onward_byte_identical=True,
                          frozen_files_byte_identical=list(frozen), git_diff_check='PASS'),
        markdown_checks=dict(files=len(files), checked_local_links=links, errors=errors),
        top_document_sha256={name: digest(ROOT/name) for name in TOP},
        batch_file_sha256={p.name: digest(p) for p in sorted(HERE.iterdir())
                           if p.is_file() and p.name != 'delivery_checks.json'})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    result = report()
    # JSON field types are normalized before either author mode or replay.
    result = json.loads(json.dumps(result))
    path = HERE/'delivery_checks.json'
    if args.write:
        path.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    require(json.loads(path.read_text()) == result, 'delivery receipt differs')
    print(json.dumps({k: result[k] for k in ('status', 'preservation', 'markdown_checks')}))


if __name__ == '__main__':
    main()
