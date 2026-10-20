#!/usr/bin/env python3
"""Check saved C011 evidence, review pins, links and preserved history.

This is a delivery consistency check, not a fresh mathematical replay.
"""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
BASE='cae57b0d248c0178e3347a934e73b5f0586bcfe8'
FROZEN='9190ccf2519acc56446dd027c6cbf8d45dcceeb6'
SIDE=('c138d948eb17c2f847e9b0efff793e0da191c346',
      'bab760a670973cc98a874dfc713996bc0dca8470')
TOP=('AGENTS.md','README.md','VIEWPOINT_MAP.md','docs/CYCLE_SPECTRUM_BRIEF.md',
     'docs/CYCLE_SPECTRUM_LOG.md','docs/RESEARCH_LOG.md','docs/RESULTS.md','docs/VIEWPOINT_LOG.md')
PINS={'DEFECT_OBSTRUCTIONS.md': 'a769a6a5238b123dd561c3097adb00aaa6556c8cdfc18e535fd8234ad523ea79',
 'EXCLUSION.md': '0edfdb40ffbb05b43c1e88bd26555ceaf8311135ea31a5ff122761d045f68032',
 'GENERAL_DEFECTS.md': 'c1edc51a9714114c9cd92cc86c90b49031e035d7e392953aa3b1b06083a57ac7',
 'ROTATION_DEFECTS.md': '9b390b7f8e456bbf52f3563cf7fe4243cf052846a1175dc0d4098a11ba59c801',
 'check_coupled_defects.py': '6d6cdf4ebdc75bee9b46638bf998748aa89f985c514296f1388f9b959e57a0bb',
 'check_exclusion_constants.py': 'f63bb7621e6e22d4fee13abea2f356a8871d1b07dcc3ad8ba4ba41642cad1ac7',
 'check_rotation_defects.py': 'ba9a2b7fb269d619378c4c7b25d3cb6430e5a8078ea5658e0d81b71ba2d855ad',
 'coupled_defect_controls.json': '061810c3261b299f3db1ff941ae6b31498667dd442058a61387a330e97c41f94',
 'exclusion_constants.json': 'bbf7e8616bff39574d05ca075fe26c78a0dc88ac6380f55e73861dc26407225f',
 'rotation_defect_audit.json': '1eee49577e35bf5f28aac0ba2a572c8a863266575c4a0e2a4babf2f233d9844d'}
REVIEWS={'DEFECT_OBSTRUCTIONS.md': ['ARITHMETIC_REVIEW.md'],
 'EXCLUSION.md': ['INDEPENDENT_REVIEW.md'],
 'GENERAL_DEFECTS.md': ['EXACT_CHECKER_REVIEW.md'],
 'ROTATION_DEFECTS.md': ['ARITHMETIC_REVIEW.md', 'INDEPENDENT_REVIEW.md'],
 'check_coupled_defects.py': ['EXACT_CHECKER_REVIEW.md'],
 'check_exclusion_constants.py': ['INDEPENDENT_REVIEW.md'],
 'check_rotation_defects.py': ['INDEPENDENT_REVIEW.md',
                               'EXACT_CHECKER_REVIEW.md'],
 'coupled_defect_controls.json': ['EXACT_CHECKER_REVIEW.md'],
 'exclusion_constants.json': ['INDEPENDENT_REVIEW.md'],
 'rotation_defect_audit.json': ['INDEPENDENT_REVIEW.md',
                                'EXACT_CHECKER_REVIEW.md']}


def require(ok,message):
    if not ok: raise ValueError(message)


def git(*args):
    return subprocess.check_output(['git',*args],cwd=ROOT)


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def report():
    gate=json.loads((HERE/'historical_gate.json').read_text())
    metadata={'archive_sha256','manifest_entries','scope'}
    require(len(gate)==119 and metadata<=set(gate),'gate coverage changed')
    require(gate['status']=='PASS' and all(isinstance(v,str) and v.startswith('PASS')
            for k,v in gate.items() if k not in metadata),'gate not passed')
    for name,pin in PINS.items():
        require(digest(HERE/name)==pin,'reviewed file changed: '+name)
        for review in REVIEWS[name]:
            require(pin in (HERE/review).read_text(),'missing independent pin: '+name)
    audit=json.loads((HERE/'rotation_defect_audit.json').read_text())
    constants=json.loads((HERE/'exclusion_constants.json').read_text())
    coupled=json.loads((HERE/'coupled_defect_controls.json').read_text())
    for receipt in (audit,constants,coupled):
        require(receipt['status']=='PASS','receipt not passed')
        for name,pin in receipt['source_sha256'].items():
            path=ROOT/name if '/' in name else HERE/name
            require(digest(path)==pin,'receipt source changed: '+name)
    actual=audit['actual'];counts=actual['counts']
    expected=dict(normalized_cycles=1185,normalized_arrows=28831,rotations=27646,
                  word_positions_compared=1481154,cycles_with_two_defects=108,
                  two_defect_rotations=192,two_arc_identities=384,
                  adjusted_quadratic_bounds=192,amplitude_free_quadratic_bounds=192)
    require(actual['source_cycles']==2459 and actual['source_parameters']==333
            and actual['source_raw_arrows']==36912 and len(actual['fixture_controls'])==11,
            'actual corpus coverage changed')
    require(all(counts[k]==v for k,v in expected.items()),'rotation coverage changed')
    require(audit['generated']['counts']==dict(family_raw_arrows=4224,family_rotation_checks=4173,family_words=51),
            'generated coverage changed')
    require(audit['marker_family']['counts']==dict(all_rotation_checks=1012,cases=8,
            half_period_two_arc_checks=8,mechanical_prefix_bounds=510,raw_cycle_arrows=1020),
            'marker coverage changed')
    require(audit['rejection_controls']['rejected_inputs']==4,'rejection coverage changed')
    c=constants['certificate']
    require(c['period_boundary']==137500000000 and c['boundary_margin']==[2450000000,1]
            and c['derivative_lower']==[373,2750] and c['coefficient_used']==600000000,
            'constant receipt changed')
    require([(r['q'],r['g'],r['mismatch_count']) for r in coupled['cases']]==
            [(97,5,3),(233,7,4),(359,73,6)],'coupled control coverage changed')
    previous=git('ls-tree','-r','--name-only',BASE,'experiments/cycle_spectrum').decode().splitlines()
    require(len(previous)==127,'prior cycle evidence coverage changed')
    for name in previous:
        require((ROOT/name).read_bytes()==git('show',BASE+':'+name),'prior cycle file changed: '+name)
    marker='## R1 — Exact source transport and original packets'.encode()
    ledger=(ROOT/'docs/RESULTS.md').read_bytes();old=git('show',FROZEN+':docs/RESULTS.md')
    require(ledger.count(marker)==old.count(marker)==1,'frozen ledger boundary changed')
    require(ledger.split(marker,1)[1]==old.split(marker,1)[1],'frozen ledger changed')
    frozen=['collatz_research_20261017/right_aligned_reduction.tex',
            'experiments/residual_progress/resolved_rules/RESOLVED_RULES.md',
            'experiments/residual_progress/resolved_rules/resolved_rules.py']
    for name in frozen:
        require((ROOT/name).read_bytes()==git('show',FROZEN+':'+name),'frozen file changed: '+name)
    files=[ROOT/name for name in TOP]+sorted(HERE.glob('*.md'))
    for name in ('REPORT.md','ROOT_REVIEW.md','SIDE_REVIEW.md','LITERATURE.md',
                 'ARITHMETIC_REVIEW.md','INDEPENDENT_REVIEW.md','EXACT_CHECKER_REVIEW.md'):
        require((HERE/name).is_file(),'missing delivery document: '+name)
    links,errors=0,[]
    for path in files:
        body=re.sub(r'```.*?```','',path.read_text(),flags=re.S)
        for target in re.findall(r'\]\(([^)]+)\)',body):
            target=target.split('#',1)[0].strip('<>')
            if not target or re.match(r'[a-zA-Z]+:',target): continue
            links+=1
            destination=(path.parent/target).resolve()
            if destination==HERE/'delivery_checks.json': continue
            if not destination.exists():errors.append([str(path.relative_to(ROOT)),target])
    require(not errors,'broken links: '+repr(errors))
    for pin in SIDE:
        require(pin in (HERE/'SIDE_REVIEW.md').read_text() and
                pin in (ROOT/'docs/VIEWPOINT_LOG.md').read_text(),'side pin absent: '+pin)
    git('diff','--check')
    return dict(status='PASS',baseline_commit=BASE,frozen_commit=FROZEN,
        scope='Saved evidence consistency and preservation; not a mathematical or formal replay.',
        goal_status='All-cycle objective active; the two-defect class is excluded under declared inputs.',
        historical_gate=dict(status='PASS',fields=len(gate),command='python3 scripts/verify_all.py --cpp --transfer-controls'),
        reviewed_pins=PINS,independent_reviews=REVIEWS,
        saved_coverage=dict(source_cycles=2459,source_parameters=333,fixtures=11,
                            rotations=expected,marker=audit['marker_family']['counts'],coupled_actual_controls=3),
        preservation=dict(C001_C010_files_unchanged=127,R1_onward_byte_identical=True,
                          frozen_files_byte_identical=frozen,git_diff_check='PASS'),
        markdown_checks=dict(files=len(files),checked_local_links=links,errors=errors),
        reviewed_side_commits=list(SIDE),
        top_document_sha256={name:digest(ROOT/name) for name in TOP},
        batch_file_sha256={p.name:digest(p) for p in sorted(HERE.iterdir())
                           if p.is_file() and p.name!='delivery_checks.json'})


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write',action='store_true')
    args=parser.parse_args();result=report();path=HERE/'delivery_checks.json'
    if args.write:path.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    else:require(json.loads(path.read_text())==result,'delivery receipt mismatch')
    print(json.dumps({k:result[k] for k in ('status','preservation','markdown_checks')}))


if __name__=='__main__':main()
