#!/usr/bin/env python3
"""Check C009 saved receipts, reviewed source pins, links, and frozen history.

This checks preservation and delivery consistency. It does not rerun the
mathematical experiments or historical gate, and does not independently prove
the mathematical claims or turn a saved receipt into a fresh formal replay.
"""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BASE = '93117c0989c6bee557c601f0667589cd4985b0ab'
FROZEN = '9190ccf2519acc56446dd027c6cbf8d45dcceeb6'
SIDE_COMMITS = ('215759608ee8197a9a0862b0dfc9c41b07410359',
                '960b3b9825cc86a0a2ffb4a1e9f77732122b22f2')
LEAN_STATE = 'c8f3d2e80b7cd5e1513219036bf74d1d41aebf0c'
TOP = ('AGENTS.md', 'README.md', 'VIEWPOINT_MAP.md', 'docs/CYCLE_SPECTRUM_BRIEF.md',
       'docs/CYCLE_SPECTRUM_LOG.md', 'docs/RESEARCH_LOG.md', 'docs/RESULTS.md',
       'docs/VIEWPOINT_LOG.md')
PINS = {
    'EXCURSION_ARITHMETIC.md': '7d4a0f7413dea67be2f3fd6e6643ace2ccb8b2decee6dc17f2b77f10b27eabcd',
    'INDEPENDENT_EXCURSION.md': 'b37655989a8f43a17ced1632a404fd34dfdb8d6d5dcadaa0d6533df1e3be58ac',
    'FIRST_RETURN_ORDER.md': '10a7f10d396a8631c197f3203af498467d92551ad35f4e9ded63c7c621d354fa',
    'check_return_order.py': '58b016702d0292a5294027dd75139b36dad171fc2e314971ae07a46fb2a59355',
    'return_order_audit.json': 'ab4672a38fa2dc688d34ced57d3af0148eab1b821267eb44ed013b016eba5d34',
    'check_excursions.py': 'a7631d433cd5952d8a27de3eb41addb8d01784da410064fb9e479d5cff3e17cb',
    'excursions_audit.json': '414c04dd9042d378674659f2ddf824a6228756f230ebe28fb2282795425f19e1',
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
    require(len(gate) == 119, 'historical gate coverage changed')
    metadata = {'archive_sha256', 'manifest_entries', 'scope'}
    require(all(isinstance(value, str) and value.startswith('PASS')
                for key, value in gate.items() if key not in metadata),
            'historical gate contains non-PASS result')

    for name, expected in PINS.items():
        require(digest(HERE/name) == expected, 'reviewed source changed: '+name)
    checker_review = (HERE/'CHECKER_REVIEW.md').read_text()
    require(all(value in checker_review for value in PINS.values()),
            'checker review is missing a reviewed source pin')
    for name in ('EXCURSION_ARITHMETIC.md', 'FIRST_RETURN_ORDER.md',
                 'check_return_order.py', 'return_order_audit.json'):
        require(PINS[name] in (HERE/'ARITHMETIC_REVIEW.md').read_text(),
                'arithmetic review is missing a reviewed source pin: '+name)

    excursions = json.loads((HERE/'excursions_audit.json').read_text())
    returns = json.loads((HERE/'return_order_audit.json').read_text())
    sources = {
        'check_excursions.py': HERE/'check_excursions.py',
        'C001/actual_cycles.json': HERE.parent/'C001/actual_cycles.json',
        'C007/height_denominator_audit.json': HERE.parent/'C007/height_denominator_audit.json',
        'phase6/cycle_fixtures.json': ROOT/'experiments/phase6/cycle_fixtures.json',
    }
    require(set(excursions['source_sha256']) == set(sources),
            'excursion dependency list changed')
    for name, path in sources.items():
        require(digest(path) == excursions['source_sha256'][name],
                'excursion dependency changed: '+name)
    require(set(returns['source_sha256']) == {'FIRST_RETURN_ORDER.md', 'check_return_order.py'},
            'return-order dependency list changed')
    for name, expected in returns['source_sha256'].items():
        require(digest(HERE/name) == expected, 'return-order dependency changed: '+name)

    existing = excursions['existing']
    counts = existing['counts']
    require(existing['source_cycles'] == 2459 and existing['source_parameters'] == 333
            and len(existing['fixture_controls']) == 11
            and existing['scaled_source_instances'] == 1275
            and counts['all']['cycles'] == 1185
            and counts['all']['segments'] == 2593
            and counts['all']['prefix_cylinder_checks'] == 28831
            and excursions['rejection_controls']['rejected'] == 6,
            'saved excursion receipt coverage changed')
    require(counts['ordered']['cycles'] == 52
            and counts['ordered']['nontrivial_cycles'] == 51
            and counts['ordered']['segments'] == 177
            and counts['ordered']['positive_height_segments'] == 60
            and counts['ordered']['positive_contracting_increase'] == 2
            and counts['ordered']['return_not_rank_rotation'] == 12,
            'ordered-domain receipt coverage changed')
    require(returns['status'] == 'PASS'
            and returns['deletion']['permutations'] == 105388
            and returns['deletion']['checked_arrows'] == 6250510
            and returns['endpoints']['positive_odd_endpoint_pairs'] == 16368
            and returns['endpoints']['exact_arrows'] == 76464,
            'saved return-order receipt coverage changed')

    previous = git('ls-tree', '-r', '--name-only', BASE,
                   'experiments/cycle_spectrum').decode().splitlines()
    previous = [name for name in previous
                if re.match(r'experiments/cycle_spectrum/C00[1-8]/', name)]
    require(len(previous) == 96, 'historical cycle file coverage changed')
    for name in previous:
        require((ROOT/name).read_bytes() == git('show', BASE+':'+name),
                'historical cycle batch changed: '+name)
    marker = '## R1 — Exact source transport and original packets'.encode()
    current_ledger = (ROOT/'docs/RESULTS.md').read_bytes()
    frozen_ledger = git('show', FROZEN+':docs/RESULTS.md')
    require(current_ledger.count(marker) == frozen_ledger.count(marker) == 1,
            'frozen result ledger boundary is missing or ambiguous')
    require(current_ledger.split(marker, 1)[1] == frozen_ledger.split(marker, 1)[1],
            'frozen result ledger changed')
    kept = ['collatz_research_20261017/right_aligned_reduction.tex',
            'experiments/residual_progress/resolved_rules/RESOLVED_RULES.md',
            'experiments/residual_progress/resolved_rules/resolved_rules.py']
    for name in kept:
        require((ROOT/name).read_bytes() == git('show', FROZEN+':'+name),
                'frozen file changed: '+name)

    files = [ROOT/name for name in TOP]+sorted(HERE.glob('*.md'))
    require((HERE/'ROOT_REVIEW.md').is_file(), 'root review is not ready')
    links, errors = 0, []
    for path in files:
        body = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
        for target in re.findall(r'\]\(([^)]+)\)', body):
            target = target.split('#', 1)[0].strip('<>')
            if not target or re.match(r'[a-zA-Z]+:', target):
                continue
            links += 1
            destination = (path.parent/target).resolve()
            # This receipt is being constructed, rather than an external input.
            if destination == HERE/'delivery_checks.json':
                continue
            if not destination.exists():
                errors.append([str(path.relative_to(ROOT)), target])
    require(not errors, 'broken local link: '+repr(errors))
    side_review = (HERE/'SIDE_REVIEW.md').read_text()
    require(all(commit in side_review for commit in (*SIDE_COMMITS, LEAN_STATE)),
            'side review is missing a reviewed commit')
    git('diff', '--check')
    hashes = {str(path.relative_to(ROOT)): digest(path) for path in sorted(HERE.iterdir())
              if path.is_file() and path.name != 'delivery_checks.json'}
    return dict(
        status='PASS', baseline_commit=BASE, frozen_commit=FROZEN,
        scope='Preservation and consistency of saved evidence; no fresh mathematical or formal replay.',
        goal_status='All-cycle objective active; ordered q1 exclusion remains open and is intermediate.',
        historical_gate=dict(status='PASS', command='python3 scripts/verify_all.py --cpp --transfer-controls',
                             field_count=len(gate), independent_cpp=gate['independent_cpp'],
                             phase6_transfer_controls=gate['phase6_transfer_controls']),
        source_reviews=dict(status='PASS', pinned_sha256=PINS),
        saved_receipt_coverage=dict(source_cycles=existing['source_cycles'],
                                   source_parameters=existing['source_parameters'],
                                   normalized_cycles=counts['all']['cycles'],
                                   first_returns=counts['all']['segments'],
                                   prefix_cylinders=counts['all']['prefix_cylinder_checks'],
                                   ordered_cycles=counts['ordered']['cycles'],
                                   deletion=returns['deletion'], endpoints=returns['endpoints']),
        preservation=dict(C001_C008_files_unchanged=len(previous), R1_onward_byte_identical=True,
                          frozen_files_byte_identical=kept, git_diff_check='PASS'),
        markdown_checks=dict(files=len(files), checked_local_links=links, errors=errors),
        top_document_sha256={name: digest(ROOT/name) for name in TOP},
        batch_file_sha256=hashes,
        side_reports=dict(reviewed_commits=list(SIDE_COMMITS), lean_state_commit=LEAN_STATE,
                          scope='Reported formal builds only; no independent kernel replay in main.'))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    result = report()
    path = HERE/'delivery_checks.json'
    if args.write:
        path.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    else:
        require(json.loads(path.read_text()) == result, 'delivery receipt mismatch')
    print(json.dumps({key: result[key] for key in ('status', 'preservation', 'markdown_checks')}))


if __name__ == '__main__':
    main()
